from tkinter import *
from tkinter import messagebox

class LibraryGUI:

    def __init__(self,master):

        self.master=master
        self.lib=Library()
        master.title("Library App")

        self.label=Label(master,text="MENU")
        self.label.pack()

        self.list_button=Button(master,text="List Books",command=self.list_books)
        self.list_button.pack()

        self.add_button=Button(master,text="Add Book",command=self.add_book)
        self.add_button.pack()

        self.delete_botton=Button(master,text="Delete Book",command=self.delete_book)
        self.delete_botton.pack()

    def list_books(self):
        self.lib.list_books()
        messagebox.showinfo("Kitaplar")
    
    def add_book(self): 
        self.book_name =input("Enter book name:")
        self.book_author =input("Enter author's name:")
        self.book_year =input("Enter year of publication:")
        self.book_nop =input("Enter number of pages:")
        self.lib.add_book(self.book_name, self.book_author, self.book_year, self.book_nop)
        messagebox.showinfo("Kitap Eklendi", "Kitap başarıyla eklendi.")     

    def delete_book(self):
        book_name=input("Name of the book to be deleted: ")
        self.lib.delete_book(book_name)    
        messagebox.showinfo("Kitap Kaldırıldı", "Kitap başarıyla kaldırıldı.")                                                                                                                  

class Library:

    def __init__(self):
        self.dosya_exe="Kitaplar.txt"

    def open_file(self,mode):
        self.file=open(self.dosya_exe,mode) 
    
    def close_file(self):
        self.file.close()
    
    def list_books(self):
        self.open_file("r")
        books_list = []
        for line in self.file:
            book_info = line.strip().split(',')
            if len(book_info) >= 2:
                book_name, book_author = book_info[:2]
                books_list.append(f"Book name: {book_name}, Book author: {book_author}")
        self.close_file()
        return books_list                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                       
    def add_book(self,book_name,book_author,book_year,book_nop):
        self.open_file("a+")
        line=f"{book_name},{book_author},{book_year},{book_nop}\n"
        self.file.write(line)
        self.close_file()
    
    def delete_book(self,book_name):
        self.open_file("r")
        lines=self.file.readlines()
        delete_lines=[]
        for line in lines:
            if book_name in line:
                delete_lines.append(line)
        self.close_file()
        self.open_file("a+")
        for line in lines:
            if line not in delete_lines:
                self.file.write(line)
        self.close_file()
    
def main():
    root = Tk()
    app = LibraryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()