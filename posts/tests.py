from django.test import TestCase
from django.urls import reverse
from .forms import NoteForm
from .models import Note

class NoteModelTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test note", content="Remember to test the app.", author="Test Author"
        )

    def test_note_has_expected_fields(self):
        self.assertEqual(self.note.title, "Test note")
        self.assertEqual(self.note.content, "Remember to test the app.")
        self.assertEqual(self.note.author, "Test Author")

    def test_string_representation_is_title(self):
        self.assertEqual(str(self.note), "Test note")

    def test_created_and_updated_timestamps_are_set(self):
        self.assertIsNotNone(self.note.created_at)
        self.assertIsNotNone(self.note.updated_at)

class NoteViewTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test note", content="Test content", author="Sam"
        )

    def test_note_list_returns_200_and_shows_note(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test note")

    def test_note_detail_returns_200_and_shows_content(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test content")

    def test_create_note_with_valid_data(self):
        response = self.client.post(reverse("note_create"), {
            "title": "New note", "content": "Created by test", "author": "Alex"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="New note").exists())

    def test_create_note_rejects_blank_content(self):
        response = self.client.post(reverse("note_create"), {
            "title": "Invalid note", "content": "   ", "author": "Alex"
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.filter(title="Invalid note").exists())

    def test_update_note(self):
        response = self.client.post(reverse("note_update", args=[self.note.pk]), {
            "title": "Updated title", "content": "Updated content", "author": "Sam"
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated title")

    def test_delete_requires_post_confirmation(self):
        response = self.client.get(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(pk=self.note.pk).exists())

    def test_delete_note(self):
        response = self.client.post(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())

    def test_missing_note_returns_404(self):
        response = self.client.get(reverse("note_detail", args=[99999]))
        self.assertEqual(response.status_code, 404)

class NoteFormTests(TestCase):
    def test_form_is_invalid_without_title(self):
        form = NoteForm(data={"title": " ", "content": "Some content", "author": "Me"})
        self.assertFalse(form.is_valid())

    def test_form_accepts_valid_data(self):
        form = NoteForm(data={"title": "Title", "content": "Content", "author": "Me"})
        self.assertTrue(form.is_valid())
