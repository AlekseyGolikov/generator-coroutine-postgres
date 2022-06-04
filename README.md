## gen-coro-postgres.py - transmit notes from text file into bd PostgreSQL

---

commit 1: функция чтения реализована на основе генератора, 
функция записи в базу на основе корутины

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
