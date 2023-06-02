import time
from logs.log_conf import LogCrud
from painless.utils import clear_screen
from sqlalchemy.exc import IntegrityError
from crud_user.model import Student, session
from painless.helper.enum import RegexPatternEnum, Emoji
from painless.helper.validator import validate_date


logging = LogCrud.log_establish()


class Crud:
    def __init__(self, action: str):
        """
        Initializes an instance of the Crud class.

        Args:
            action (str): The action to perform (e.g., 'create', 'update',
                'read', 'delete').
        """
        self.action = action

    def create_user(self) -> None:
        """
        Creates a new user based on user input.

        This method prompts the user to enter information for creating a new
            student.
        It validates the input fields to ensure they are valid.
        If the action is 'create', it creates a new student object and saves
            it to the database.
        """
        if self.action == 'create':
            clear_screen()
            print(f"Registration form {Emoji.STUDENT}")
            first_name = input("\n\nPlease enter first name: ")
            last_name = input("Please enter last name: ")
            student_number = input("Please enter student number [10 digit]: ")
            gender = input("Please enter gender [Male - Female]: ")
            date_of_birth = input("Please enter date of birth (YYYY-MM-DD): ")
            educational_level = input("Please enter educational level->\n[High School|College|Bachelor|Master|PhD]: ")# noqa
            registration_date = input("Please enter registration date (YYYY-MM-DD): ")# noqa
            graduation_date = input("Please enter graduation date (YYYY-MM-DD): ")# noqa
            address = input("Please enter address: ")
            phone_number = input("Please enter phone number: ")

            if (
                validate_date(first_name, RegexPatternEnum.NAME) and
                validate_date(last_name, RegexPatternEnum.NAME) and
                validate_date(student_number, RegexPatternEnum.STUDENT_NUMBER) and# noqa
                validate_date(gender, RegexPatternEnum.GENDER) and
                validate_date(date_of_birth, RegexPatternEnum.DATE) and
                validate_date(educational_level, RegexPatternEnum.EDUCATIONAL_LEVEL) and # noqa
                validate_date(registration_date, RegexPatternEnum.DATE) and
                validate_date(graduation_date, RegexPatternEnum.DATE) and
                validate_date(phone_number, RegexPatternEnum.IRAN_PHONE_NUMBER)
            ):
                student = Student(
                    first_name=first_name,
                    last_name=last_name,
                    student_number=student_number,
                    gender=gender,
                    date_of_birth=date_of_birth,
                    educational_level=educational_level,
                    registration_date=registration_date,
                    graduation_date=graduation_date,
                    address=address,
                    phone_number=phone_number
                )
                try:
                    session.add(student)
                    session.commit()
                    logging.info('Student data saved successfully.')
                    time.sleep(1.5)
                except IntegrityError:
                    session.rollback()
                    logging.error('Error: Duplicate student number.')
                    time.sleep(1.5)
            else:
                print("\n\nInvalid input. Please try again.")
                time.sleep(2)

    def update_user(self) -> None:
        """
        Updates a user based on user input.

        This method prompts the user to enter the student number of the user
            to update.
        It queries the database for the student with the provided student
            number.
        If the student is found, it allows the user to update various fields.
        The user can enter new values for each field, or leave them empty to
            keep the current values.
        After updating the fields, it commits the changes to the database and
            logs a success message.
        """
        if self.action == 'update':
            student_number = input("\nWhich user do you want to update? Please enter their student number: ")# noqa
            clear_screen()
            # Query the student you want to update
            student = session.query(Student).filter_by(student_number=student_number).first()# noqa

            if not student:
                logging.error('Student not found.')
                time.sleep(1.5)
                session.close()
                return

            fields = [
                ('first_name', "Enter new first name (leave empty to keep current value): "),# noqa
                ('last_name', "Enter new last name (leave empty to keep current value): "),# noqa
                ('student_number', "Enter new student number (leave empty to keep current value): "),# noqa
                ('gender', "Enter new gender (leave empty to keep current value): "),# noqa
                ('date_of_birth', "Enter new date of birth (YYYY-MM-DD, leave empty to keep current value): "),# noqa
                ('educational_level', "Enter new educational level (leave empty to keep current value): "),# noqa
                ('registration_date', "Enter new registration date (YYYY-MM-DD, leave empty to keep current value): "),# noqa
                ('graduation_date', "Enter new graduation date (YYYY-MM-DD, leave empty to keep current value): "),# noqa
                ('address', "Enter new address (leave empty to keep current value): "),# noqa
                ('phone_number', "Enter new phone number (leave empty to keep current value): ")# noqa
            ]
            i = 0
            for field, message in fields:
                new_value = input(message)
                if field in ['first_name', 'last_name'] and validate_date(new_value, RegexPatternEnum.NAME):
                    setattr(student, field, new_value)
                    logging.info(f'this {field} updated successfully.')
                    time.sleep(1.5)
                    i += 1
                elif field in ['registration_date', 'graduation_date', 'date_of_birth'] and validate_date(new_value, RegexPatternEnum.DATE):
                    setattr(student, field, new_value)
                    logging.info(f'this {field} updated successfully.')
                    time.sleep(1.5)
                    i += 1
                elif field == 'student_number' and validate_date(new_value, RegexPatternEnum.STUDENT_NUMBER):
                    setattr(student, field, new_value)
                    logging.info(f'this {field} updated successfully.')
                    time.sleep(1.5)
                    i += 1
                elif field == 'gender' and validate_date(new_value, RegexPatternEnum.GENDER):
                    setattr(student, field, new_value)
                    logging.info(f'this {field} updated successfully.')
                    time.sleep(1.5)
                    i += 1
                elif field == 'educational_level' and validate_date(new_value, RegexPatternEnum.EDUCATIONAL_LEVEL):
                    setattr(student, field, new_value)
                    logging.info(f'this {field} updated successfully.')
                    time.sleep(1.5)
                    i += 1
                elif field == 'phone_number' and validate_date(new_value, RegexPatternEnum.IRAN_PHONE_NUMBER):
                    logging.info(f'this {field} updated successfully.')
                    time.sleep(1.5)
                    setattr(student, field, new_value)
                    i += 1

            if i != 0:
                session.commit()
                session.close()
            else:
                logging.info('nothing updated')

    def read_user(self) -> None:
        """
        Reads and displays information of a user based on user input.

        This method prompts the user to enter the student number of the user
            to retrieve information.
        It queries the database for the student with the provided student
            number.
        If the student is found, it calls the 'display_student_info' method to
            print the student's information.
        If no student is found, it logs an error message.
        """
        if self.action == 'read':
            student_number = input("Enter student number: ")
            clear_screen()
            student = session.query(Student).filter_by(student_number=student_number).first()# noqa

            if student:
                self.display_student_info(student)
            else:
                logging.error("No student found with the provided student number.")# noqa
                time.sleep(1.5)
            session.close()

    def display_student_info(self, student: Student) -> None:
        """
        Displays the information of a student.

        Args:
            student: The student object whose information needs to be
                displayed.
        """
        info = {
            "ID": student.id,
            "First Name": student.first_name,
            "Last Name": student.last_name,
            "Student Number": student.student_number,
            "Gender": student.gender,
            "Date of Birth": student.date_of_birth,
            "Educational Level": student.educational_level,
            "Registration Date": student.registration_date,
            "Graduation Date": student.graduation_date,
            "Address": student.address,
            "Phone Number": student.phone_number
        }

        for key, value in info.items():
            print(f"{key}: {value}")
        return_to_menu:str = input('\n\nPlease Enter to return to menu !') # noqa

    def delete_user(self) -> None:
        """
        Deletes a user based on user input.

        This method prompts the user to enter the student number of the user
            to delete.
        It queries the database for the student with the provided student
            number.
        If the student is found, it deletes the student from the database.
        If no student is found, it logs an error message.
        """
        if self.action == 'delete':
            # Prompt the user to enter the student ID to delete
            student_number = input("Enter student number: ")
            clear_screen()
            # Query the student by ID
            student = session.query(Student).filter_by(student_number=student_number).first() # noqa

            if student:
                # Student with the provided ID found, delete the student
                session.delete(student)
                session.commit()
                logging.info("Student deleted successfully.")
                time.sleep(1.5)
            else:
                # Student with the provided ID not found
                logging.error("No student found with the provided Student number.")# noqa
                time.sleep(1.5)
            # Close the session
                session.close()

    def help_user(self) -> None:
        if self.action == 'help':
            clear_screen()
            print("========================================================================================") # noqa E501
            print('''for enroll student use this command
                    Create : create student
                    Read : Read data of student base on student_number
                    Update : update data of student base on student_number
                    Delete : Delete data of student base on student_number
                    ''')
            return_to_menu:str = input('\n\nPlease enter to return to menu !') # noqa
