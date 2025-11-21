C:\Users\ADMIN>mysql -u root -p
Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.44 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
| test2              |
| world              |
+--------------------+
7 rows in set (0.25 sec)

mysql> create database test3;
Query OK, 1 row affected (0.18 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
| test2              |
| test3              |
| world              |
+--------------------+
8 rows in set (0.00 sec)

mysql> use test;
Database changed
mysql> show tables;
Empty set (0.12 sec)

mysql> use test2;
Database changed
mysql> show tables;
+-----------------+
| Tables_in_test2 |
+-----------------+
| users           |
+-----------------+
1 row in set (0.00 sec)

mysql> create table users1(
    -> user int, user_name varchar(200),
    -> email varchar (200),
    -> password varchar(200),
    -> create_at timestamp);
Query OK, 0 rows affected (0.38 sec)

mysql> show tables
    -> ;
+-----------------+
| Tables_in_test2 |
+-----------------+
| users           |
| users1          |
+-----------------+
2 rows in set (0.00 sec)

mysql> insert into users1 (user, user_name, email, password) values (1, "sachin", "sachin@gmail.com", "dgr677");
Query OK, 1 row affected (0.14 sec)

mysql> insert into users1 (user, user_name, email, password) values (2, "kavya", "kavya@gmail.com", "sa6788");
Query OK, 1 row affected (0.05 sec)

mysql> insert into users1 (user, user_name, email, password) values (3, "ravi", "ravi@gmail.com", "dgr677");
Query OK, 1 row affected (0.08 sec)

mysql> insert into users1 (user, user_name, email, password) values (4, "neethu", "neethu@gmail.com", "d888hh7");
Query OK, 1 row affected (0.13 sec)

mysql> insert into users1 (user, user_name, email, password) values (5, "anitha", "anitha@gmail.com", "ui997");
Query OK, 1 row affected (0.06 sec)

mysql> select * from users1;
+------+-----------+------------------+----------+-----------+
| user | user_name | email            | password | create_at |
+------+-----------+------------------+----------+-----------+
|    1 | sachin    | sachin@gmail.com | dgr677   | NULL      |
|    2 | kavya     | kavya@gmail.com  | sa6788   | NULL      |
|    3 | ravi      | ravi@gmail.com   | dgr677   | NULL      |
|    4 | neethu    | neethu@gmail.com | d888hh7  | NULL      |
|    5 | anitha    | anitha@gmail.com | ui997    | NULL      |
+------+-----------+------------------+----------+-----------+
5 rows in set (0.00 sec)

mysql> DESCRIBE users1;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| user      | int          | YES  |     | NULL    |       |
| user_name | varchar(200) | YES  |     | NULL    |       |
| email     | varchar(200) | YES  |     | NULL    |       |
| password  | varchar(200) | YES  |     | NULL    |       |
| create_at | timestamp    | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
5 rows in set (0.06 sec)

C:\Users\ADMIN\Downloads\world-db\world-db>mysql -uroot -p < world.sql
Enter password: ********

mysql> use world;
Database changed

mysql> show tables;
+-----------------+
| Tables_in_world |
+-----------------+
| city            |
| country         |
| countrylanguage |
+-----------------+
3 rows in set (0.00 sec)

mysql> describe city;
+-------------+----------+------+-----+---------+----------------+
| Field       | Type     | Null | Key | Default | Extra          |
+-------------+----------+------+-----+---------+----------------+
| ID          | int      | NO   | PRI | NULL    | auto_increment |
| Name        | char(35) | NO   |     |         |                |
| CountryCode | char(3)  | NO   | MUL |         |                |
| District    | char(20) | NO   |     |         |                |
| Population  | int      | NO   |     | 0       |                |
+-------------+----------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> select * from city CountryCode="IND";
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '="IND"' at line 1
mysql> select * from city where CountryCode="IND";
+------+--------------------------------+-------------+-------------------+------------+
| ID   | Name                           | CountryCode | District          | Population |
+------+--------------------------------+-------------+-------------------+------------+
| 1024 | Mumbai (Bombay)                | IND         | Maharashtra       |   10500000 |
| 1025 | Delhi                          | IND         | Delhi             |    7206704 |
| 1026 | Calcutta [Kolkata]             | IND         | West Bengali      |    4399819 |
| 1027 | Chennai (Madras)               | IND         | Tamil Nadu        |    3841396 |
| 1028 | Hyderabad                      | IND         | Andhra Pradesh    |    2964638 |
| 1029 | Ahmedabad                      | IND         | Gujarat           |    2876710 |
| 1030 | Bangalore                      | IND         | Karnataka         |    2660088 |
| 1031 | Kanpur                         | IND         | Uttar Pradesh     |    1874409 |
| 1032 | Nagpur                         | IND         | Maharashtra       |    1624752 |
| 1033 | Lucknow                        | IND         | Uttar Pradesh     |    1619115 |
| 1034 | Pune                           | IND         | Maharashtra       |    1566651 |
| 1035 | Surat                          | IND         | Gujarat           |    1498817 |

mysql> select * from city where district = 'karnataka';
+------+----------------+-------------+-----------+------------+
| ID   | Name           | CountryCode | District  | Population |
+------+----------------+-------------+-----------+------------+
| 1030 | Bangalore      | IND         | Karnataka |    2660088 |
| 1060 | Hubli-Dharwad  | IND         | Karnataka |     648298 |
| 1074 | Mysore         | IND         | Karnataka |     480692 |
| 1102 | Belgaum        | IND         | Karnataka |     326399 |
| 1108 | Gulbarga       | IND         | Karnataka |     304099 |
| 1116 | Mangalore      | IND         | Karnataka |     273304 |
| 1119 | Davangere      | IND         | Karnataka |     266082 |
| 1122 | Bellary        | IND         | Karnataka |     245391 |
| 1161 | Bijapur        | IND         | Karnataka |     186939 |
| 1170 | Shimoga        | IND         | Karnataka |     179258 |
| 1193 | Raichur        | IND         | Karnataka |     157551 |
| 1227 | Timkur         | IND         | Karnataka |     138903 |
| 1237 | Gadag Betigeri | IND         | Karnataka |     134051 |
| 1275 | Mandya         | IND         | Karnataka |     120265 |
| 1304 | Bidar          | IND         | Karnataka |     108016 |
| 1342 | Hospet         | IND         | Karnataka |      96322 |
| 1359 | Hassan         | IND         | Karnataka |      90803 |
+------+----------------+-------------+-----------+------------+
17 rows in set (0.02 sec)

mysql> select * from city where CountryCode = "IND" limit 4;
+------+--------------------+-------------+--------------+------------+
| ID   | Name               | CountryCode | District     | Population |
+------+--------------------+-------------+--------------+------------+
| 1024 | Mumbai (Bombay)    | IND         | Maharashtra  |   10500000 |
| 1025 | Delhi              | IND         | Delhi        |    7206704 |
| 1026 | Calcutta [Kolkata] | IND         | West Bengali |    4399819 |
| 1027 | Chennai (Madras)   | IND         | Tamil Nadu   |    3841396 |
+------+--------------------+-------------+--------------+------------+
4 rows in set (0.00 sec)