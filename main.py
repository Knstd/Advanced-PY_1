from datetime import datetime as dt
from colorama import Fore
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(f'{Fore.GREEN}Hello! Today is {dt.now().date()}')
    calculate_salary()
    get_employees()
