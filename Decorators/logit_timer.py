import time
import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def logit(func):
    def inner(*args):
        logging.info(f"Function {func.__name__} were successfully logged)")
        return None
    return inner

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        if not hasattr(func, 'alltime'):
            func.alltime = 0
        func.alltime += elapsed_time

        print(f"{func.__name__} выполнялась {elapsed_time:.6f} секунд")
        print(f"Суммарное время вызовов {func.__name__}: {func.alltime:.6f} секунд")

        return result

    return wrapper


class ExampleClass:
    @timer
    @logit
    def some_method(self):
        time.sleep(1)
        return "Завершено"

@timer
def test_function():
    time.sleep(2)
    return "Готово"


if __name__ == "__main__":
    ex = ExampleClass()
    ex.some_method()
    ex.some_method()

    test_function()
    test_function()
