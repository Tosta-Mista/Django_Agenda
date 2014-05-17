# -*- coding: utf-8 -*-
from django.test import TestCase, Client


class StatusTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_public(self):
        urls = [{'url':'/accounts/login/',
                 'template':'registration/login.html',
                 'status':200},
                {'url':'/accounts/logout/',
                 'template':'registration/login.html',
                 'status':302},
                {'url':'/accounts/profile/',
                 'template':'registration/login.html',
                 'status':302},
                ]
        for elem in urls:
            response = self.client.get(elem['url'])
            self.assertEqual(response.status_code, elem['status'])
            response = self.client.get(elem['url'], follow=True)
            self.assertEqual(response.template.name, elem['template'])

    def test_create_user(self):
        response = self.client.post('/user/create_account/', {
            'username':'john',
            'password1':'trytoguess',
            'password2':'trytoguess',
            }, follow=True)
        self.assertEqual(response.template.name, 'user/succes.html')
        user = User.objects.get(username="john")
        self.assertEqual(user.username, "john")

    def test_login(self):
        self.test_create_user()
        response = self.client.post('/accounts/login/',{
            'username':'john',
            'password':'trytoguess'
            }, follow=True)
        self.assertEqual(response.template.name, 'registration/profile.html')