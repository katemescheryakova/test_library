
class Book:
    """
        Класс для представления книги в библиотеке.

        Атрибуты:
            id (int): Уникальный идентификатор книги.
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания.
            status (str): Статус книги ("в наличии" или "выдана").
            next_id(int): Статический атрибут для ID
        """
    next_id = 1
    def __init__(self, title, author, year, status="в наличии"):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    # метод для вывода строки в консоль
    def __str__(self):
        return f"ID: {self.id}\nНазвание: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nСтатус: {self.status}"

class LibraryManager:
    """
            Класс для обработки книг в библиотеке.

            Атрибуты:
            filename (str): Путь к файлу с данными о библиотеке.
            books (list): Список с книгами.
    """
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.books = self.load_library()
    # загрузка данных о книгах из файла (с обработкой исключения, если файл пустой)
    def load_library(self):
        books = []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 5:
                        books.append(Book(parts[1], parts[2], int(parts[3]), parts[4]))
                if books:
                    Book.next_id = max(book.id for book in books) + 1
        except FileNotFoundError:
            pass
        return books
    # сохранение данных о книгах в файл
    def save_library(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.id}|{book.title}|{book.author}|{book.year}|{book.status}\n")
    # создание нового объекта книги и сохранение его в файл
    def add_book(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        while True:
            try:
                year = int(input("Введите год издания книги: "))
                break
            except ValueError:
                print("Некорректный год. Попробуйте ещё раз.")
        book = Book(title, author, year)
        self.books.append(book)
        self.save_library()
        print("Книга добавлена!")

    # удаление объекта книги и сохранение изменений в файл
    def delete_book(self):
        while True:
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                break
            except ValueError:
                print("Некорректный ID. Попробуйте ещё раз.")

        for i, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[i]
                self.save_library()
                print("Книга удалена!")
                return
        print("Книга не найдена.")
    # поиск книги по запросу пользователя
    def search_book(self):
        search_term = input("Введите поисковый запрос (название, автор или год): ").lower()
        results = [book for book in self.books if search_term in book.title.lower() or
                                                search_term in book.author.lower() or
                                                search_term in str(book.year)]
        if results:
            print("Найденные книги:")
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")
    # отображние всех книг в библиотеке
    def show_all_books(self):
        if self.books:
            print("Список всех книг:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")
    # изменение статуса книги в библиотеке
    def change_book_status(self):
        while True:
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                break
            except ValueError:
                print("Некорректный ID. Попробуйте ещё раз.")

        for book in self.books:
            if book.id == book_id:
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").lower()
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_library()
                    print("Статус книги изменен!")
                    return
                else:
                    print("Неверный статус.")
                    return
        print("Книга не найдена.")

# функция-меню для работы с классами
def main():
    library = LibraryManager()
    while True:
        print("Меню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.delete_book()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.show_all_books()
        elif choice == "5":
            library.change_book_status()
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
