import pandas as pd
import datetime

print("😎----Welcome to AMUST Library----😎")
df=pd.DataFrame({
    "Name":['Fahim','Jafir','Himel','Haseb','Rafi','Hasan','Jisan','Soron','Rafshan'],
    'Id':[1,3,5,10,17,18,19,26,27]
})

class LibraryManager():
    def __init__(self,df,available_books):
        self.df = df
        self.books = available_books
        
    def StdLogin(self):
        print("😕----Enter your name and login id for verification----😕")
        std_name=input("Enter your name:")
        std_id=int(input("Enter your id:"))
        
        std_exist=self.df[(self.df['Name']==std_name) & (self.df['Id']==std_id)]
        if not std_exist.empty:
            print("---verification sucessfull---")
        else:
            print('---verification failed---')
    def Available_books(self):
        for book in self.books:
            print(f"\t  📓 :{book}")
    def borrow_books(self,bookName):
        if bookName in self.books:
            print(f"📚 :{bookName} is borrowed successfully")
            self.books.remove(bookName)
        else:
            print(f"📚 :{bookName} is not available")

if __name__ == '__main__':
    CentralLibrary=LibraryManager(df,['Introduction to Algorithms', 'Engineering Mathematics', 'Digital Logic Design',
            'Thermodynamics', 'Fluid Mechanics', 'Heat Transfer',
            'Control Systems', 'Signals and Systems', 'Microelectronics',
            'Structural Analysis', 'Concrete Technology', 'Geotechnical Engineering',
            'Machine Design', 'Manufacturing Processes', 'Material Science',
            'Power Electronics', 'Electrical Machines', 'Circuit Theory',
            'Computer Networks', 'Operating Systems', 'Database Systems'])
    CentralLibrary.StdLogin()
    while True:
        welcome='''===Welcome to AMUST Library===
        1.---Available_books---.
        2.---Borrow_books---.
        3.---Returning_books---.
        4.---Exit---.'''
        print(welcome)
        
        choice=int(input("Enter your choice: "))
        if choice==1:
            CentralLibrary.Available_books()
        elif choice==2:
            bookName=input("Enter the book name: ")
            CentralLibrary.borrow_books(bookName)
        elif choice==3:
            bookName=input("Enter the book name: ")
            CentralLibrary.books.append(bookName)
            print(f"📚 :{bookName} is returned successfully")
        elif choice==4:
            print("😎----Thanks for visiting AMUST Library----😎")
            break