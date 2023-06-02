from sqlalchemy.exc import IntegrityError


class UserExist(IntegrityError):
    pass
