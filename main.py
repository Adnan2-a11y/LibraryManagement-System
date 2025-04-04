import pandas as pd
import datetime
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page configuration
st.set_page_config(
    page_title="AMUST Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load book data from CSV file
@st.cache_data
def load_data():
    try:
        LibraryData = pd.read_csv('engineering_books_filtered.csv')
        return LibraryData
    except FileNotFoundError:
        st.error("Book database file not found!")
        return pd.DataFrame()

# Load borrowed books data
@st.cache_data
def load_borrowed_books():
    try:
        return pd.read_csv('borrowed_books.csv')
    except FileNotFoundError:
        return pd.DataFrame()

# Function to extract unique department names
def get_departments(books):
    return sorted(set(book['Dept Name'] for book in books))

# Class to manage library operations
class LibraryManager:
    def __init__(self, available_books):
        self.books = available_books
        self.departments = get_departments(available_books)
        self.similarity_matrix = None
        self.books_df = None
        self._prepare_similarity_matrix()

    def _prepare_similarity_matrix(self):
        """Prepare data and compute similarity matrix for recommendations"""
        self.books_df = pd.DataFrame(self.books)
        self.books_df['content'] = self.books_df['Book'] + ' ' + self.books_df['Author'] + ' ' + self.books_df['Dept Name']
        
        # Create TF-IDF matrix
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.books_df['content'])
        
        # Compute cosine similarity matrix
        self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Create indices for books
        self.indices = pd.Series(self.books_df.index, index=self.books_df['Book']).drop_duplicates()

    def Available_books_by_dept(self):
        st.subheader("Available Books by Department")
        selected_dept = st.selectbox("Select a department:", self.departments)
        
        dept_books = [book for book in self.books if book['Dept Name'] == selected_dept]
        
        if dept_books:
            st.write(f"**Available Books in {selected_dept}:**")
            cols = st.columns(2)
            for i, book in enumerate(dept_books):
                with cols[i % 2]:
                    st.markdown(f"""
                    **{book['Book']}**  
                    *by {book['Author']}*  
                    📚 Department: {book['Dept Name']}
                    """)
        else:
            st.warning(f"No books available in {selected_dept} department.")

    def borrow_books(self):
        st.subheader("Borrow a Book")
        with st.form("borrow_form"):
            std_name = st.text_input("Your Name:")
            std_id = st.text_input("Your ID:")
            book_name = st.selectbox(
                "Book Name:",
                options=[book['Book'] for book in self.books]
            )
            
            submitted = st.form_submit_button("Borrow")
            
            if submitted:
                if not std_name or not std_id:
                    st.error("Please fill all fields!")
                    return
                
                for book in self.books:
                    if book['Book'] == book_name:
                        self.books.remove(book)
                        
                        borrow_record = {
                            'Name': std_name,
                            'Id': std_id,
                            'Book': book['Book'],
                            'Author': book['Author'],
                            'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        try:
                            borrow_df = pd.read_csv('borrowed_books.csv')
                            borrow_df = pd.concat([borrow_df, pd.DataFrame([borrow_record])], ignore_index=True)
                        except FileNotFoundError:
                            borrow_df = pd.DataFrame([borrow_record])
                        
                        borrow_df.to_csv('borrowed_books.csv', index=False)
                        
                        # Update similarity matrix
                        self._prepare_similarity_matrix()
                        
                        st.success(f"📚 {book['Book']} borrowed successfully!")
                        st.balloons()
                        return
                
                st.error(f"❌ {book_name} is not available")

    def return_books(self):
        st.subheader("Return a Book")
        borrowed_df = load_borrowed_books()
        
        if borrowed_df.empty:
            st.warning("No books currently borrowed.")
            return
            
        with st.form("return_form"):
            # Get books borrowed by the user
            user_id = st.text_input("Enter your ID:")
            user_books = borrowed_df[borrowed_df['Id'] == user_id]['Book'].unique()
            
            if len(user_books) > 0:
                book_name = st.selectbox(
                    "Select book to return:",
                    options=user_books
                )
            else:
                st.warning("No books borrowed with this ID.")
                return
                
            submitted = st.form_submit_button("Return")
            
            if submitted:
                if not user_id:
                    st.error("Please enter your ID!")
                    return
                
                # Remove from borrowed records
                borrow_df = borrowed_df[~((borrowed_df['Id'] == user_id) & 
                                       (borrowed_df['Book'] == book_name))]
                borrow_df.to_csv('borrowed_books.csv', index=False)
                
                # Add back to available books
                original_book = next((book for book in LibraryData.to_dict('records') 
                                    if book['Book'] == book_name), None)
                if original_book:
                    self.books.append(original_book)
                    # Update similarity matrix
                    self._prepare_similarity_matrix()
                    st.success(f"📚 {book_name} returned successfully!")
                    st.balloons()
                else:
                    st.error(f"❌ {book_name} not found in library records.")

    def recommend_books(self, book_title, n_recommendations=5):
        """Recommend similar books based on content"""
        idx = self.indices.get(book_title, -1)
        
        if idx == -1:
            return []
        
        # Get pairwise similarity scores
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        
        # Sort books by similarity score
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get top N recommendations (excluding itself)
        sim_scores = sim_scores[1:n_recommendations+1]
        book_indices = [i[0] for i in sim_scores]
        
        return self.books_df.iloc[book_indices][['Book', 'Author', 'Dept Name']].to_dict('records')

# Main Streamlit app
def main():
    st.title("📚 AMUST Library Management System")
    st.markdown("---")
    
    # Load data
    global LibraryData
    LibraryData = load_data()
    if LibraryData.empty:
        return
    
    # Initialize available books
    available_books = LibraryData[['Book', 'Author', 'Dept Name']].to_dict('records')
    
    # Create library manager instance
    CentralLibrary = LibraryManager(available_books)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    options = [
        "View Books by Department",
        "Borrow a Book",
        "Return a Book",
        "Get Recommendations",
        "View All Books"
    ]
    choice = st.sidebar.selectbox("Choose an option:", options)
    
    if choice == "View Books by Department":
        CentralLibrary.Available_books_by_dept()
    elif choice == "Borrow a Book":
        CentralLibrary.borrow_books()
    elif choice == "Return a Book":
        CentralLibrary.return_books()
    elif choice == "Get Recommendations":
        st.subheader("Book Recommendations")
        selected_book = st.selectbox(
            "Select a book you like:",
            options=[book['Book'] for book in available_books]
        )
        
        if st.button("Get Recommendations"):
            with st.spinner("Finding similar books..."):
                recommendations = CentralLibrary.recommend_books(selected_book)
                if recommendations:
                    st.success("📚 We think you'll also enjoy these books:")
                    cols = st.columns(2)
                    for i, book in enumerate(recommendations):
                        with cols[i % 2]:
                            st.markdown(f"""
                            **{book['Book']}**  
                            *by {book['Author']}*  
                            📚 Department: {book['Dept Name']}
                            """)
                else:
                    st.warning("No recommendations found or book not recognized.")
    elif choice == "View All Books":
        st.subheader("All Available Books")
        if available_books:
            cols = st.columns(2)
            for i, book in enumerate(available_books):
                with cols[i % 2]:
                    st.markdown(f"""
                    **{book['Book']}**  
                    *by {book['Author']}*  
                    📚 Department: {book['Dept Name']}
                    """)
        else:
            st.warning("No books available in the library.")
    
    # Display borrowed books in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("Currently Borrowed Books")
    borrowed_df = load_borrowed_books()
    if not borrowed_df.empty:
        st.sidebar.dataframe(borrowed_df[['Name', 'Book', 'Date']])
    else:
        st.sidebar.write("No books currently borrowed.")

if __name__ == '__main__':
    main()
