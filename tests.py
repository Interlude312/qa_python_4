import pytest
from main import BooksCollector


class TestBooksCollector:

    # Проверка начального состояния словаря книг
    def test_initial_state_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    # Проверка начального состояния списка избранного
    def test_initial_state_favorites_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    # Проверка добавления книги — она появляется в словаре с пустым жанром
    def test_add_new_book_added_book_has_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_book_genre('Азбука') == ''

    # Проверка, что книга с корректным названием добавляется
    def test_add_new_book_valid_name_added(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert len(collector.get_books_genre()) == 1

    # Проверка, что книга с пустым названием не добавляется
    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # Проверка, что книга с названием длиннее 40 символов не добавляется
    def test_add_new_book_too_long_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука' * 10)
        assert len(collector.get_books_genre()) == 0

    # Установка жанра из допустимого списка
    def test_set_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.get_book_genre('Азбука') == 'Ужасы'

    # Установка жанра не из списка — жанр остаётся пустым
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'FFFFFF')
        assert collector.get_book_genre('Азбука') == ''

    # Получение жанра книги
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.get_book_genre('Азбука') == 'Ужасы'

    # Получение книг с определённым жанром
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        books = ['Азбука', 'Алгебра', 'Маленький принц']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')
        
        collector.add_new_book('Ну погоди')
        collector.set_book_genre('Ну погоди', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Ужасы') == books

    # Получение словаря books_genre
    def test_get_books_genre_returns_dict_with_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_books_genre() == {'Азбука': ''}

    # Книги для детей — только без возрастного рейтинга
    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']

    # Добавление книги в избранное
    def test_add_book_in_favorites_adds_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == ['Азбука']

    # Удаление книги из избранного
    def test_delete_book_from_favorites_removes_from_list(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        collector.delete_book_from_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == []

    # Получение списка избранных книг
    def test_get_list_of_favorites_books_returns_all_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_new_book('Алгебра')
        collector.add_book_in_favorites('Азбука')
        collector.add_book_in_favorites('Алгебра')
        assert collector.get_list_of_favorites_books() == ['Азбука', 'Алгебра']