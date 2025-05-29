class Book:
    page_material = 'бумага'
    text_availability = 'текст есть'
    reserved = False

    def __init__(self, book_name, author, number_pages, ISBN):
        self.book_name = book_name
        self.author = author
        self.number_pages = number_pages
        self.ISBN = ISBN

    def __str__(self):
        reserved_status = ', зарезервирована' if self.reserved else ''
        return (f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.number_pages}, материал: {self.page_material}'
                f'{reserved_status}')


book_one = Book('Алмазный огранщик', 'Майкл Роуч', 300, 1)
book_two = Book('Преступление и наказание', 'Достоевский', 700, 2)
book_three = Book('Война и мир', 'Толстой', 400, 3)
book_four = Book('Мастер и Маргарита', 'Булгаков', 500, 4)
book_five = Book('Ревизор', 'Гоголь', 900, 5)

book_two.reserved = True

for book in [book_one, book_two, book_three, book_four, book_five]:
    print(book)


class Textbook(Book):
    def __init__(self, book_name, author, number_pages, ISBN, subject, class_level, has_tasks):
        super().__init__(book_name, author, number_pages, ISBN)
        self.subject = subject
        self.class_level = class_level
        self.has_tasks = has_tasks

    def __str__(self):
        reserved_status = ', зарезервирована' if self.reserved else ''
        return (f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.number_pages}, предмет: {self.subject}, '
                f'класс: {self.class_level}'
                f'{reserved_status}')


textbook1 = Textbook('Алгебра', 'Иванов', 200, 6, 'Математика', 9, True)
textbook2 = Textbook('Геометрия', 'Петров', 250, 7, 'Математика', 10, True)
textbook3 = Textbook('История', 'Сидоров', 300, 8, 'История', 8, False)

textbook2.reserved = True

for textbook in [textbook1, textbook2, textbook3]:
    print(textbook)
