class ThreadData:
    __shared_data = {
        'name': 'thread_1',
        'raw_data': {},
        'id': 1,
    }
    def __init__(self):
        self.__dict__ = self.__shared_data

th1 = ThreadData()
th2 = ThreadData()
print(th1.id)
th2.id = 3
print(th1.id)