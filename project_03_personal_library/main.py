import os
import json
import streamlit as st

LIBRARY_FILE = 'library.txt'


def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []


def save_library(library):
    with open(file, 'w') as file:
        json.dump(library, file, indent=4)


def add_book(library):
    st.header('Add a Book')
    title = st.text_input('Enter the book title')
    author = st.text_input('Enter the author')
    publication_year = st.number_input('Enter the publication year', min_value=0, step=1)
    genre = st.text_input('Enter the genre')
    read_status = st.checkbox('Have you read this book?')
    if st.button('Add Book'):
        book = {
            'title': title,
            'author': author,
            'year': int(publication_year),
            'genre': genre,
            'read': read_status
        }
        library.append(book)
        save_library(library)
        st.success('Book added successfully!')


def remove_book(library):
    st.header('Remove a Book')
    title = st.text_input('Enter the title of the book to remove')
    if st.button('Remove Book'):
        for book in library:
            if book['title'].lower() == title.lower():
                library.remove(book)
                save_library(library)
                st.success('Book removed successfully!')
                return
        st.error('Book not found.')


def search_books(library):
    st.header('Search for a Book')
    search_by = st.selectbox('Search by', ['Title', 'Author'])
    keyword = st.text_input('Enter the keyword')
    if st.button('Search'):
        results = [book for book in library if keyword.lower() in book[search_by.lower()].lower()]
        if results:
            st.write('Matching Books:')
            for book in results:
                st.write(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning('No matching books found.')


def display_books(library):
    st.header('Your Library')
    if not library:
        st.info('Your library is empty.')
        return
    for index, book in enumerate(library, start=1):
        st.write(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")


def display_statistics(library):
    st.header('Library Statistics')
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    st.write(f'Total books: {total_books}')
    st.write(f'Percentage read: {percentage_read:.2f}%')


def main():
    st.set_page_config(page_title="Library Manager",page_icon="📕")
    st.title('📕Personal Library Manager')
    library = load_library()

    options = ['Add a Book', 'Remove a Book', 'Search for a Book', 'Display All Books', 'Display Statistics']
    st.sidebar.header("📕Choise your option")
    choice = st.sidebar.selectbox('Select an Option', options)

    if choice == 'Add a Book':
        add_book(library)
    elif choice == 'Remove a Book':
        remove_book(library)
    elif choice == 'Search for a Book':
        search_books(library)
    elif choice == 'Display All Books':
        display_books(library)
    elif choice == 'Display Statistics':
        display_statistics(library)


if __name__ == '__main__':
    main()
