from django.test import TestCase

from News.models import Notes
from django.contrib.auth.models import User

class UserNotesTestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testusername', password='qweqwer123')
        for i in range(10):
            Notes.objects.create(title = 'cool note №{}'.format(i), text = 'cool text for text note №{}'.format(i), author = test_user)
        
    def test_view_exist(self):
        resp = self.client.get('mynotes/')
        self.assertEquals(resp.status_code, 200)

    def test_view_correct_template(self):
        resp = self.client.get('mynotes/')
        self.assertTemplateUsed(resp, 'News/list_notes_user.html')

