# 📚 AMUST Library Management System  

![Library Banner](https://via.placeholder.com/1200x400/4B6E97/FFFFFF?text=AMUST+Library+Management+System)  
*A modern, user-friendly library management system powered by Streamlit and machine learning.*  

---

## 🚀 **Features**  

✨ **Department-wise Book Browsing** – Easily filter books by department.  
📖 **Borrow & Return System** – Track book loans with student details.  
🤖 **AI-Powered Recommendations** – Get personalized book suggestions using **TF-IDF & Cosine Similarity**.  
📊 **Real-time Updates** – See currently borrowed books in the sidebar.  
🔍 **Search & Explore** – View all available books at a glance.  

---

## 🛠 **Tech Stack**  

| **Category**       | **Technologies Used** |
|--------------------|----------------------|
| **Frontend**       | Streamlit 🎈          |
| **Backend**        | Python 🐍            |
| **Data Processing**| Pandas 🏷️            |
| **ML for Recommendations** | Scikit-learn (TF-IDF, Cosine Similarity) 🤖 |
| **Data Storage**   | CSV (Pandas) 📂      |

---

## ⚙️ **Installation & Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/amust-library.git
cd amust-library
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```
*(Sample `requirements.txt`)*:  
```
streamlit
pandas
scikit-learn
```

### **3. Run the App**  
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.  

---

## 📂 **File Structure**  

```
📁 amust-library/
├── 📄 app.py               # Main Streamlit application
├── 📄 engineering_books_filtered.csv  # Sample book database
├── 📄 borrowed_books.csv   # Tracks borrowed books
└── 📄 README.md            # This file
```

---

## 🎨 **How It Works**  

### **1. View Books by Department**  
- Select a department to see available books.  

### **2. Borrow a Book**  
- Enter student details and choose a book.  
- The system updates availability in real time.  

### **3. Return a Book**  
- Enter student ID and select the book to return.  

### **4. Get AI Recommendations**  
- Select a book you like, and the system suggests similar books.  

### **5. View All Books**  
- Browse the entire library collection.  

---

## 📊 **Screenshots**  

| **Department View** | **Borrow System** |
|---------------------|------------------|
| ![Department View](https://via.placeholder.com/400x250/4B6E97/FFFFFF?text=Department+View) | ![Borrow System](https://via.placeholder.com/400x250/4B6E97/FFFFFF?text=Borrow+Book) |

| **AI Recommendations** | **Borrowed Books Log** |
|-----------------------|-----------------------|
| ![Recommendations](https://via.placeholder.com/400x250/4B6E97/FFFFFF?text=AI+Recommendations) | ![Borrowed Log](https://via.placeholder.com/400x250/4B6E97/FFFFFF?text=Borrowed+Books) |

---

## 🤝 **Contributing**  

Want to improve this project?  
1. **Fork** the repository.  
2. Create a new branch (`git checkout -b feature/your-feature`).  
3. **Commit** your changes (`git commit -m "Add new feature"`).  
4. **Push** to the branch (`git push origin feature/your-feature`).  
5. Open a **Pull Request**.  

---

## 📜 **License**  

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

---

## 🌟 **Credits**  

- Developed with ❤️ by **Rafshan Jani**  
- Powered by **Streamlit & Scikit-learn**  

---

### 🔗 **Live Demo**  
👉 [Try it out!](#) *(Coming soon!)*  

---

**Happy Reading!** 📖✨
