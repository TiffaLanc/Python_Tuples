#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

#Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_title(library, book):
    
    if book not in library:
        library.append(book)
        print("Book added successfully.")
    else:
        print("This book is already in the library.")

add_title(library, ("The Emerald Tablets" ,"Thoth the Atlantean"))
add_title(library, ("Death Masks", "Jim Butcher"))
add_title(library, ("Brave New World", "Aldous Huxley"))
    
print("Book List: ")

for i, book in enumerate(library, start=1):
    title, author = book
    print(f"{i}. {title} by {author}")