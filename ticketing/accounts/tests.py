from django.test import TestCase
# Zejin.Deng
# Create your tests here.
# creat test class
from accounts import models


class AccoutsTest(TestCase):

    def setUp(self):
        '''
        Equivalent to the initialization operation, it will be executed once before the test case test_xxx is executed

        Features: This function will be executed once before each test case is executed
        '''
        print('start testing Accouts part!!!')


    def tearDown(self):
        '''
        Will be executed once after the test case test_xxx is executed

         Features: It will be executed once after each test case is executed
        '''
        print('>>>>Test end Accouts part!!! Test passed')


    # Define a test function The naming format of the test function is test+function name
    def test_accoutsTest(self):
        print('Generating UserProfile entity')
        models.UserProfile.objects.create(mpassword='123',email="123",is_active=False,have_active=False)
        print("UserProfile entity created successfully")
        print("Querying the test database for test data")
        print(models.UserProfile.objects.all().values())
