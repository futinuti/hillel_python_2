import sqlite3
import os


def execute_query(query_sql: str) -> list:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def get_firstname_from_customers() -> None:
    '''
    Функция получения всех firstname из таблицы customers
    '''
    query_sql = '''
        SELECT firstname
          FROM customers;
    '''
    result = set()
    quantity = []
    names = execute_query(query_sql)

    for i in names:
        if names.count(i) > 1:
            result.add(i)
    for j in result:
        counter = 0
        for i in names:
            if j == i:
                counter +=1
        quantity.append(j[0])
        quantity.append(counter)
    print(quantity)

get_firstname_from_customers()