import os


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')
