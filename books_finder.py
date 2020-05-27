import pandas 
import time
import numpy as np

def read_file():
    # open the file for books published two years ago
    file_path1 = "Resources/books_list/"
    with open(file_path1) as f:
        recent_books = f.read().split('\n')
    
    # open the file for all coding books
    file_path2 = "Resources/books_list/"
    with open(file_path2) as f:
        coding_books = f.read().split('\n')
    return recent_books, coding_books
        
recent_books, coding_books = read_file()
        
def method_one():
    # start time 
    start_time = time.time()
    
    recent_coding_books = []
    
    # for each book in recent books
    for book in recent_books:
        # if each book in recent books is found in coding books
        if book in coding_books:
            recent_coding_books.append(book)
            recent_coding_books_count = len(recent_coding_books)
        else:
            recent_coding_books_count = len(recent_coding_books)
        
    return recent_books_count

method_one()

# Tip #1: Use vector operations over loops when possible
# Use numpy's intersect1d method to get the intersection of the recent_books and coding_books arrays
def method_two(recent_books, coding_books):
    start_time = time.time()
    
    recent_coding_books = np.intersect1d(recent_books, coding_books)
    
    recent_coding_books_count = len(recent_coding_books)
    
    return recent_coding_books_count

method_two(recent_books, coding_books)

# Tip  #2: Know your data structures and which methods are faster
# Use the set's intersection method to get the common elements in recent_books and coding_books
def method_three(recent_books, coding_books):
    start_time = time.time()
    
    recent_coding_books = set(recent_books).intersection(coding_books)
    
    recent_coding_books_count = len(recent_coding_books)
    
    return recent_coding_books_count

method_three(recent_books, coding_books)




