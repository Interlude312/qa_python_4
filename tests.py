import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_initial_state_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_initial_state_favorites_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book_added_book_has_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_book_genre('Азбука') == ''

    def test_add_new_book_valid_name_added(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_too_long_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука' * 10)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.get_book_genre('Азбука') == 'Ужасы'

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'FFFFFF')
        assert collector.get_book_genre('Азбука') == ''

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')
        assert collector.get_book_genre('Азбука') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        books = ['Азбука', 'Алгебра', 'Маленький принц']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')
        
        collector.add_new_book('Ну погоди')
        collector.set_book_genre('Ну погоди', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Ужасы') == books

    def test_get_books_genre_returns_dict_with_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        assert collector.get_books_genre() == {'Азбука': ''}

    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']

    def test_add_book_in_favorites_adds_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == ['Азбука']

    def test_delete_book_from_favorites_removes_from_list(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_book_in_favorites('Азбука')
        collector.delete_book_from_favorites('Азбука')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_all_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.add_new_book('Алгебра')
        collector.add_book_in_favorites('Азбука')
        collector.add_book_in_favorites('Алгебра')
        assert collector.get_list_of_favorites_books() == ['Азбука', 'Алгебра']