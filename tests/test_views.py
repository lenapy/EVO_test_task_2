from django.test import TestCase, Client
from django.urls import reverse
from django import forms

from test_app.forms import AddNameForm, DeleteNameForm


class TestAddName(TestCase):
    def test_add_name_form_not_valid(self):
        AddNameForm(data={})
        self.assertRaises(forms.ValidationError)

    def test_add_name_form_not_valid_short_name(self):
        AddNameForm(data={'name': 'te'})
        self.assertRaises(forms.ValidationError)

    def test_add_name_form_not_valid_name_already_exist(self):
        add_name()
        AddNameForm(data={'name': 'test_name'})
        self.assertRaises(forms.ValidationError)

    def test_add_name_form_valid(self):
        form = AddNameForm(data={'name': 'test_name'})
        self.assertTrue(form.is_valid())

    def test_success_add(self):
        response = add_name()
        self.assertEqual(response.status_code, 200)


def add_name():
    c = Client()
    return c.post(reverse('name:add'),
                  data={'name': 'test_name'})


class TestDeleteName(TestCase):

    def test_del_name_form_not_valid_name_not_added(self):
        DeleteNameForm(data={'name': 'test_name'})
        self.assertRaises(forms.ValidationError)

    def test_del_name_form_not_valid_short_name(self):
        DeleteNameForm(data={'name': 'te'})
        self.assertRaises(forms.ValidationError)

    def test_delete_name_form_valid(self):
        add_name()
        form = DeleteNameForm(data={'name': 'test_name'})
        self.assertTrue(form.is_valid())

    def test_success_delete(self):
        add_name()
        response = delete_name()
        self.assertEqual(response.status_code, 200)


def delete_name():
    c = Client()
    return c.post(reverse('name:del'),
                  data={'name': 'test_name'})


class TestGetRandomNames(TestCase):

    def test_show_names_success(self):
        for i in range(5):
            add_name()
        c = Client()
        response = c.get(reverse('name:get_random_names'))
        self.assertEqual(response.status_code, 200)
