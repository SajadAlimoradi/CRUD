from crud_user.model import Student, session
from logs.log_conf import LogCrud
import re
import time

logging = LogCrud.log_establish()


def student_number_checker(student: Student) -> None:
    """
    Checks if a student with the same student number already exists in the
        database.
    If not, saves the student data to the database.

    Args:
        student (Student): The student object to be checked and saved.
    """
    exists = session.query(Student).filter_by(student_number=student.student_number).first() # noqa

    if exists:
        logging.error('This student number already exists.')
        time.sleep(1.5)
    else:
        session.add(student)
        session.commit()
        logging.info('Student data saved successfully.')
        time.sleep(1.5)


def validate_date(date_string: str, regex_pattern: str) -> bool:
    pattern = regex_pattern
    if re.match(pattern, date_string):
        return True
    else:
        return False

