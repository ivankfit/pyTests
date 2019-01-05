import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    #programmers use DRY method..>>>> Don't Repeat Yourself by using setUp and tearDown methods

    def setUp(self): #this runs first before any test runs
        print('setUp')
        #use self.emp_1 to make emp_1 and 2 instance attributes
        self.emp_1 = Employee('tweheyo', 'ivan', 50000)
        self.emp_2 = Employee('ahebwa', 'chris', 40000)

    def tearDown(self): #this is used to clean up all the test done eg to delete database done tests to create space for more
        print('teardown\n')

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'tweheyoivan@gmail.com')
        self.assertEqual(self.emp_2.email, 'ahebwachris@gmail.com')

        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.email, 'johnivan@gmail.com')
        self.assertEqual(self.emp_2.email, 'janechris@gmail.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'tweheyo ivan')
        self.assertEqual(self.emp_2.fullname, 'ahebwa chris')

        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.fullname, 'john ivan')
        self.assertEqual(self.emp_2.fullname, 'jane chris')

    # TODO

    # def test_if_name_is_already_taken(self):
    #     self.emp_1 = Employee('Tweheyo', 'Ivan', 50000)
    #     self.emp_2 = Employee('John', 'Amanya', 20000)

    #     with self.assertRaises(ValueError):
    #       Employee.test_fullname('Tweheyo', 'Ivan')
    #     #self.assertEqual(self.emp_2.fullname, 'John Amanya')

    def test_apply_raise(self):

        self.emp_1.apply_raise
        self.emp_2.apply_raise

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 42000)

    def test_monthly_schedule(self): #only used when accessing urls
        #test function to store our information incase the website is down the function shouldnot fail
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/ivan/May')
            self.assertEqual(schedule, 'Success')

            #test a failed response
             mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/chris/June')
            self.assertEqual(schedule, 'Bad Response!')




if __name__ == '__main__':
    unittest.main()