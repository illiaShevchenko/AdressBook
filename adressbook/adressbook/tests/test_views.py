from django.test import TestCase

from homepage.models import Person
from django.urls import reverse


class PersonListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        persons_num = 5
        for author_num in range(persons_num):
            Person.objects.create(name='TestName %s' % author_num,
                                surname = 'TestSurname %s' % author_num,
                                phone = '099123456%s' % author_num,
                                )

    def test_view_url_accessible_by_name_list(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_delete_id(self):
        resp = self.client.post(reverse('delete_id', kwargs = {'id':2}))
        self.assertEqual(resp.status_code, 302)

    def test_view_url_accessible_by_name_add(self):
        resp = self.client.get(reverse('add'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_home(self):
        resp = self.client.get(reverse('wellcome'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_add_id(self):
        resp = self.client.get(reverse('add_id', kwargs = {'id':4}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_list(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'homepage/wrapper.html', 'homepage/list.html')