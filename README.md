## gen-coro-postgres.py - передача данных из текстового файла в БД PostgreSQL с использованием генератора и сопрограммы

---

commit 1: функция чтения реализована на основе генератора, 
функция записи в базу на основе корутины

commit 2: функция записи реализована на основе класса-обертки

input.txt:  
> 1 apple 100.23  
> 2 tomatos 200.43  
> 3 potatos 300.65  

PostgreSQL:

> selectel=# SELECT * FROM products;  
 id |   title    | price  
----+------------+--------  
  1 | apple      | 100.23  
  2 | tomatos    | 200.43  
  3 | potatos    | 300.65  
