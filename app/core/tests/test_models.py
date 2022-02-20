from core import models
from django.test import TestCase
from django.contrib.auth import  get_user_model

def sample_user(email="test@test.com", password="testtest"):
    """create a user"""
    return get_user_model().objects.create_user(email, password)

def sample_recipe(user):
    return models.Recipe.objects.create(
            user = user,
            name = 'lepa hrana',
            text = 'Steak and mushroom sauce',
            price = 2.45
        )

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@stefan.com'
        password = 'stefan123'
        
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        '''Test the email for a new user is nnormalized'''

        email =  'test@STEFAN.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def  test_new_user_invalid_email(self):
        """Test creating user with mo email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)