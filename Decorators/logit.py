import logging
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def logit(func):
    def inner(*args):
        logging.info(f"Arguments {args} were successfully logged)")
        return None
    return inner

@logit
def some_func(name, age):
    return None

some_func('Daniel', 16)