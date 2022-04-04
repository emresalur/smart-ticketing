from django.test import TestCase
# 
# Create your tests here.
# create test class
from smart import models


class SmartTest(TestCase):

    def setUp(self):
        '''
        Equivalent to the initialization operation, it will be executed once before the test case test_xxx is executed

        Features: This function will be executed once before each test case is executed
        '''
        print('start test SmartTest modles!!!')





    def tearDown(self):
        '''
        Will be executed once after the test case test_xxx is executed

        Features: It will be executed once after each test case is executed
        '''
        print('>>>>test end start test sMartTest modles!!!')


    # Define a test function The naming format of the test function is test+function name
    def test_smart(self):
        print('Generating MainRequest entity object')


        print(' MainRequest The entity object module is stored successfully and the test passes, The number of objects in the MainRequest table is queried as：'+str(len(models.MainRequest.objects.all().values())))

