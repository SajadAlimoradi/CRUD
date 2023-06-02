import unittest
from unittest.mock import patch
from crud_user.control.crud import Crud
from crud_user.model import Student, session


class CrudTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # Prepare the database with a sample student
        student = Student(
            first_name='John',
            last_name='Doe',
            student_number='1231231239',
            gender='Male',
            date_of_birth='1990-01-01',
            educational_level='Bachelor',
            registration_date='2021-01-01',
            graduation_date='2025-01-01',
            address='Sample Address',
            phone_number='09181234578'
        )
        session.add(student)
        session.commit()

    def tearDown(self) -> None:
        # Clean up the database after each test
        session.query(Student).delete()
        session.commit()

    @patch('builtins.input')
    def test_create_user(self, mock_input) -> None:
        # Retrieve the created student from the database
        created_student = session.query(Student).filter_by(student_number='1231231239').first()  # noqa

        # Add assertions to check if the student was created correctly
        self.assertIsNotNone(created_student)
        self.assertEqual(created_student.first_name, 'John')
        self.assertEqual(created_student.last_name, 'Doe')
        self.assertEqual(created_student.gender, 'Male')
        self.assertEqual(created_student.date_of_birth.isoformat(), '1990-01-01')  # noqa
        self.assertEqual(created_student.educational_level, 'Bachelor')
        self.assertEqual(created_student.registration_date.isoformat(), '2021-01-01')  # noqa
        self.assertEqual(created_student.graduation_date.isoformat(), '2025-01-01')  # noqa
        self.assertEqual(created_student.address, 'Sample Address')
        self.assertEqual(created_student.phone_number, '09181234578')

    @patch('builtins.input')
    def test_update_user(self, mock_input) -> None:
        mock_input.side_effect = [
            '1231231239',  # Enter student number to update
            '',  # Leave first name empty
            'Updated Last Name',  # Enter updated last name
            '',  # Leave student number empty
            'Female',  # Enter updated gender
            '',  # Leave date of birth empty
            'master',  # Enter updated educational level
            '',  # Leave registration date empty
            '2026-01-01',  # Enter updated graduation date
            '',  # Enter updated address
            ''  # Leave phone number empty
        ]

        crud = Crud('update')
        crud.update_user()

        # Retrieve the updated student from the database
        updated_student = session.query(Student).filter_by(student_number='1231231239').first()  # noqa

        # Add assertions to check if the student was updated correctly
        self.assertIsNotNone(updated_student)
        self.assertEqual(updated_student.first_name, 'John')  # First name should remain unchanged  # noqa
        self.assertEqual(updated_student.last_name, 'Updated Last Name')
        self.assertEqual(updated_student.gender, 'Female')
        self.assertEqual(updated_student.date_of_birth.isoformat(), '1990-01-01')  # Date of birth should remain unchanged  # noqa
        self.assertEqual(updated_student.educational_level, 'master')
        self.assertEqual(updated_student.registration_date.isoformat(), '2021-01-01')  # Registration date should remain unchanged  # noqa
        self.assertEqual(updated_student.graduation_date.isoformat(), '2026-01-01')  # noqa
        self.assertEqual(updated_student.address, 'Sample Address')
        self.assertEqual(updated_student.phone_number, '09181234578')

    @patch('builtins.input')
    def test_delete_user_found(self, mock_input) -> None:
        mock_input.return_value = '1231231239'

        crud = Crud('delete')
        crud.delete_user()

        # Add assertions to check if the user was deleted from the database
        deleted_student = session.query(Student).filter_by(student_number='1231231239').first()  # noqa
        self.assertIsNone(deleted_student)

    @patch('builtins.input')
    def test_delete_user_not_found(self, mock_input) -> None:
        mock_input.return_value = '9999999999'

        crud = Crud('delete')
        crud.delete_user()


if __name__ == '__main__':
    unittest.main()
