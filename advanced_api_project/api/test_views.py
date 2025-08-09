from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Comprehensive testing for Book API endpoints (CRUD)
class BookAPITestBase(APITestCase):
    def setUp(self):
        # Create test user and authenticate via token
        self.user = User.objects.create_user(username='reader1', password='securepass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a sample author
        self.author = Author.objects.create(name='K.L. Marks')


class BookListEndpointTest(BookAPITestBase):
    def setUp(self):
        super().setUp()
        # Create sample book
        self.book = Book.objects.create(
            title='Shadows in Light',
            publication_year=2022,
            author=self.author
        )
        self.url = reverse('book-list')  # URL to list all books

    def test_can_list_books(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


class BookCreationTest(BookAPITestBase):
    def setUp(self):
        super().setUp()
        self.url = reverse('book-list')
        self.new_book = {
            'title': 'Beyond the Skies',
            'publication_year': 2024,
            'author': self.author.id
        }

    def test_can_create_book(self):
        response = self.client.post(self.url, self.new_book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().title, 'Beyond the Skies')


class BookDetailFetchTest(BookAPITestBase):
    def setUp(self):
        super().setUp()
        self.book = Book.objects.create(
            title='The Last Voyage',
            publication_year=2020,
            author=self.author
        )
        self.url = reverse('book-detail', args=[self.book.pk])

    def test_can_retrieve_single_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Last Voyage')
        self.assertEqual(response.data['publication_year'], 2020)


class BookUpdateTest(BookAPITestBase):
    def setUp(self):
        super().setUp()
        self.book = Book.objects.create(
            title='Lost Horizons',
            publication_year=2019,
            author=self.author
        )
        self.url = reverse('book-detail', args=[self.book.pk])
        self.updated_data = {
            'title': 'Lost Horizons - Revised',
            'publication_year': 2020,
            'author': self.author.id
        }

    def test_can_update_book(self):
        response = self.client.put(self.url, self.updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, 'Lost Horizons - Revised')


class BookDeletionTest(BookAPITestBase):
    def setUp(self):
        super().setUp()
        self.book = Book.objects.create(
            title='Silent Words',
            publication_year=2021,
            author=self.author
        )
        self.url = reverse('book-detail', args=[self.book.pk])

    def test_can_delete_book(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)