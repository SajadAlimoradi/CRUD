import time
from crud_user.control.crud import Crud
from painless.utils import banner, clear_screen
from pyfiglet import Figlet
from termcolor import colored
from logs.log_conf import LogCrud

clear_screen()
start_message: Figlet = Figlet(font='standard', width=110)
logging: LogCrud = LogCrud.log_establish()


def view() -> None:
    banner()
    print(colored(start_message.renderText('Welcome to CRUDE v0.1.0 '), 'green')) # noqa
    time.sleep(3)
    actions: dict[str, str] = {
        'create': 'create_user',
        'read': 'read_user',
        'update': 'update_user',
        'delete': 'delete_user',
        'help': 'help_user',
    }

    while True:
        clear_screen()
        print(colored(start_message.renderText('C R U D'), 'blue'))
        print(colored(start_message.renderText('------'), 'red'))
        action: str = input('\nWhat do you want to do? [ Create - Read - Update - Delete - Help]  \n ').lower() # noqa
        data_input: Crud = Crud(action)

        if action in actions:
            method_name: str = actions[action]
            method = getattr(data_input, method_name)
            method()
        else:
            logging.error('Invalid action. Please try again.')

        time.sleep(1.5)
