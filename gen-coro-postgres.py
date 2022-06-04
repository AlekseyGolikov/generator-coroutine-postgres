

from time import sleep
from psycopg2 import connect
from psycopg2 import Error

def reader():
        s = ' '
        with open('input.txt', 'r') as f:
            while s != '':
                s = f.readline().replace('\n','')
                id, title, price = s.split()
                yield id, title, price

# class wrapper:
#     def __init__(self, coroutine):
#         self.coro = coroutine()
#     def __enter__(self):
#         self.coro.__next__()
#         return self.coro
#     def __exit__(self, type, value, traceback):
#         self.coro.close()
#         if value is None: return True
#         else: return False
#     def send(self, *args):
#         return self.coro.send(*args)

def writer():
    try:
        while True:
            item = (yield)

            try:
                with connect(user='selectel',
                            password='selectel',
                            host='127.0.0.1',
                            port='5432',
                            database='selectel') as conn:
                    with conn.cursor() as cursor:
                        insert_query = "INSERT INTO products (id, title, price) VALUES (%s, %s, %s)"
                        cursor.execute(insert_query, item)
                        print(item)
                    conn.commit()
            except Error as ex:
                print(ex)
    except GeneratorExit:
        pass

if __name__ == "__main__":

    try:
        gen = reader()
        c = writer()
        c.__next__()
        while True:
            item = gen.__next__()
            # with wrapper(writer) as coro:
            #     coro.send(item)
            # id, title, price = int(item[0]), item[1], float(item[2])
            c.send(item)
            sleep(1)
    except Exception:
        pass
    