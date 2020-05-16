from django.test import TestCase

from News.models import Notes
from django.contrib.auth.models import User

class NotesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testUser = User.objects.create_user(username = 'testUser1', password = 'qweqweqwe123')
        Notes.objects.create(title = 'Test note title', text = 'Some text for testing this note right now.', author = testUser)

    def test_note_title_label(self):
        note = Notes.objects.get(id = 1)
        field_label = note._meta.get_field('title').verbose_name
        self.assertEqual(field_label, "заголовок")

    def  test_note_title_max_length(self):
        note = Notes.objects.get(id = 1)
        max_length = note._meta.get_field('title').max_length
        self.assertEquals(max_length,  50)

    def test_note_str_(self):
        note = Notes.objects.get(id = 1)
        exmpl = note.title
        self.assertEquals(exmpl, str(note))

    def test_note_get_absolute_url(self):
        note = Notes.objects.get(id = 1)
        self.assertEquals(note.get_absolute_url(), '/news/note/1')