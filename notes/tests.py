from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteTests(TestCase):
    """Tests for note ownership, access, and auth."""

    def setUp(self):
        """Create two users, each with one note."""
        self.user_a = User.objects.create_user(
            username="user_a", password="pass12345"
        )
        self.user_b = User.objects.create_user(
            username="user_b", password="pass12345"
        )
        self.note_a = Note.objects.create(
            user=self.user_a, content="Note A content"
        )
        self.note_b = Note.objects.create(
            user=self.user_b, content="Note B content"
        )

    def test_create_note_sets_owner(self):
        """Creating a note while logged in as A sets owner to A."""
        self.client.login(username="user_a", password="pass12345")
        self.client.post(
            reverse("note_create"), {"content": "New note"}
        )
        new_note = Note.objects.get(content="New note")
        self.assertEqual(new_note.user, self.user_a)

    def test_list_shows_only_own_notes(self):
        """List view shows A's note, not B's."""
        self.client.login(username="user_a", password="pass12345")
        response = self.client.get(reverse("note_list"))
        self.assertContains(response, "Note A content")
        self.assertNotContains(response, "Note B content")

    def test_detail_returns_own_note(self):
        """A can view A's own note."""
        self.client.login(username="user_a", password="pass12345")
        url = reverse("note_detail", args=[self.note_a.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_other_users_note_404(self):
        """A viewing B's note by URL gets 404."""
        self.client.login(username="user_a", password="pass12345")
        url = reverse("note_detail", args=[self.note_b.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_update_own_note(self):
        """A can edit A's own note."""
        self.client.login(username="user_a", password="pass12345")
        url = reverse("note_update", args=[self.note_a.pk])
        self.client.post(url, {"content": "Edited content"})
        self.note_a.refresh_from_db()
        self.assertEqual(self.note_a.content, "Edited content")

    def test_delete_own_note(self):
        """A can delete A's own note."""
        self.client.login(username="user_a", password="pass12345")
        url = reverse("note_delete", args=[self.note_a.pk])
        self.client.post(url)
        exists = Note.objects.filter(pk=self.note_a.pk).exists()
        self.assertFalse(exists)

    def test_logged_out_redirected(self):
        """Logged-out user is redirected from list and create."""
        list_response = self.client.get(reverse("note_list"))
        self.assertEqual(list_response.status_code, 302)
        self.assertIn("/accounts/login/", list_response.url)

        create_response = self.client.get(reverse("note_create"))
        self.assertEqual(create_response.status_code, 302)
        self.assertIn("/accounts/login/", create_response.url)
