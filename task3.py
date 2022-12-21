# 3. Применить написанный логгер к приложению из любого предыдущего д/з.
from datetime import datetime
import requests
from pprint import pprint

def logger(old_function):
    def new_function(*args, **kwargs):
        time = datetime.now()
        name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('main.log2', 'a', encoding='utf-8') as f:
            f.write(f'Date/time: {time}\n'
                    f'Name: {name}\n'
                    f'Arguments: {args} и {kwargs}\n'
                    f'Result: {result}\n'
            )
        return result
    return new_function

@logger
def question_tag_python():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1664323200&order=desc&max=1664496000&order=desc&sort=activity&tagged=Python&site=stackoverflow"
    response = requests.get(url)
    response.raise_for_status()
    result = response.json()
    return result

if __name__ == '__main__':
    question_tag_python()