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

mysql> use world
Database changed
mysql> select * from city where District="Karnataka" and Population > 250000
    -> ;
+------+---------------+-------------+-----------+------------+
| ID   | Name          | CountryCode | District  | Population |
+------+---------------+-------------+-----------+------------+
| 1030 | Bangalore     | IND         | Karnataka |    2660088 |
| 1060 | Hubli-Dharwad | IND         | Karnataka |     648298 |
| 1074 | Mysore        | IND         | Karnataka |     480692 |
| 1102 | Belgaum       | IND         | Karnataka |     326399 |
| 1108 | Gulbarga      | IND         | Karnataka |     304099 |
| 1116 | Mangalore     | IND         | Karnataka |     273304 |
| 1119 | Davangere     | IND         | Karnataka |     266082 |
+------+---------------+-------------+-----------+------------+
7 rows in set (0.66 sec)

mysql> select * from city where IN('Karnataka', 'Madhya Pradesh', 'Goa');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'IN('Karnataka', 'Madhya Pradesh', 'Goa')' at line 1

mysql> select * from city where DISTRICT IN('Karnataka', 'Madhya Pradesh', 'Goa');
+------+-----------------+-------------+----------------+------------+
| ID   | Name            | CountryCode | District       | Population |
+------+-----------------+-------------+----------------+------------+
| 1030 | Bangalore       | IND         | Karnataka      |    2660088 |
| 1037 | Indore          | IND         | Madhya Pradesh |    1091674 |
| 1038 | Bhopal          | IND         | Madhya Pradesh |    1062771 |
| 1053 | Jabalpur        | IND         | Madhya Pradesh |     741927 |
| 1057 | Gwalior         | IND         | Madhya Pradesh |     690765 |
| 1060 | Hubli-Dharwad   | IND         | Karnataka      |     648298 |
| 1074 | Mysore          | IND         | Karnataka      |     480692 |
| 1097 | Ujjain          | IND         | Madhya Pradesh |     362266 |
| 1102 | Belgaum         | IND         | Karnataka      |     326399 |
| 1108 | Gulbarga        | IND         | Karnataka      |     304099 |
| 1116 | Mangalore       | IND         | Karnataka      |     273304 |
| 1119 | Davangere       | IND         | Karnataka      |     266082 |
| 1122 | Bellary         | IND         | Karnataka      |     245391 |
| 1156 | Sagar           | IND         | Madhya Pradesh |     195346 |
| 1161 | Bijapur         | IND         | Karnataka      |     186939 |
| 1165 | Ratlam          | IND         | Madhya Pradesh |     183375 |
| 1170 | Shimoga         | IND         | Karnataka      |     179258 |
| 1180 | Burhanpur       | IND         | Madhya Pradesh |     172710 |
| 1186 | Dewas           | IND         | Madhya Pradesh |     164364 |
| 1187 | Murwara (Katni) | IND         | Madhya Pradesh |     163431 |
| 1193 | Raichur         | IND         | Karnataka      |     157551 |
| 1196 | Satna           | IND         | Madhya Pradesh |     156630 |
| 1215 | Morena          | IND         | Madhya Pradesh |     147124 |
| 1219 | Khandwa         | IND         | Madhya Pradesh |     145133 |
| 1227 | Timkur          | IND         | Karnataka      |     138903 |
| 1237 | Gadag Betigeri  | IND         | Karnataka      |     134051 |
| 1247 | Rewa            | IND         | Madhya Pradesh |     128981 |
| 1275 | Mandya          | IND         | Karnataka      |     120265 |
| 1297 | Bhind           | IND         | Madhya Pradesh |     109755 |
| 1303 | Shivapuri       | IND         | Madhya Pradesh |     108277 |
| 1304 | Bidar           | IND         | Karnataka      |     108016 |
| 1329 | Guna            | IND         | Madhya Pradesh |     100490 |
| 1342 | Hospet          | IND         | Karnataka      |      96322 |
| 1346 | Mandasor        | IND         | Madhya Pradesh |      95758 |
| 1347 | Damoh           | IND         | Madhya Pradesh |      95661 |
| 1352 | Chhindwara      | IND         | Madhya Pradesh |      93731 |
| 1356 | Vidisha         | IND         | Madhya Pradesh |      92917 |
| 1359 | Hassan          | IND         | Karnataka      |      90803 |
+------+-----------------+-------------+----------------+------------+
38 rows in set (0.00 sec)

mysql> select * from city where district="karnataka" and population BETWEEN 250000 and 300000;
+------+-----------+-------------+-----------+------------+
| ID   | Name      | CountryCode | District  | Population |
+------+-----------+-------------+-----------+------------+
| 1116 | Mangalore | IND         | Karnataka |     273304 |
| 1119 | Davangere | IND         | Karnataka |     266082 |
+------+-----------+-------------+-----------+------------+
2 rows in set (0.02 sec)

mysql> select * from city where Name like '%re' and District="Karnataka";
+------+-----------+-------------+-----------+------------+
| ID   | Name      | CountryCode | District  | Population |
+------+-----------+-------------+-----------+------------+
| 1030 | Bangalore | IND         | Karnataka |    2660088 |
| 1074 | Mysore    | IND         | Karnataka |     480692 |
| 1116 | Mangalore | IND         | Karnataka |     273304 |
| 1119 | Davangere | IND         | Karnataka |     266082 |
+------+-----------+-------------+-----------+------------+
4 rows in set (0.01 sec)

mysql> select * from city where Name like 'M%' and District="Karnataka";
+------+-----------+-------------+-----------+------------+
| ID   | Name      | CountryCode | District  | Population |
+------+-----------+-------------+-----------+------------+
| 1074 | Mysore    | IND         | Karnataka |     480692 |
| 1116 | Mangalore | IND         | Karnataka |     273304 |
| 1275 | Mandya    | IND         | Karnataka |     120265 |
+------+-----------+-------------+-----------+------------+
3 rows in set (0.00 sec)

mysql> select * from city where Name like '%ng%' and District="Karnataka";
+------+-----------+-------------+-----------+------------+
| ID   | Name      | CountryCode | District  | Population |
+------+-----------+-------------+-----------+------------+
| 1030 | Bangalore | IND         | Karnataka |    2660088 |
| 1116 | Mangalore | IND         | Karnataka |     273304 |
| 1119 | Davangere | IND         | Karnataka |     266082 |
+------+-----------+-------------+-----------+------------+
3 rows in set (0.00 sec)

mysql> select * from city where district='Karnataka' ORDER BY name
    -> ;
+------+----------------+-------------+-----------+------------+
| ID   | Name           | CountryCode | District  | Population |
+------+----------------+-------------+-----------+------------+
| 1030 | Bangalore      | IND         | Karnataka |    2660088 |
| 1102 | Belgaum        | IND         | Karnataka |     326399 |
| 1122 | Bellary        | IND         | Karnataka |     245391 |
| 1304 | Bidar          | IND         | Karnataka |     108016 |
| 1161 | Bijapur        | IND         | Karnataka |     186939 |
| 1119 | Davangere      | IND         | Karnataka |     266082 |
| 1237 | Gadag Betigeri | IND         | Karnataka |     134051 |
| 1108 | Gulbarga       | IND         | Karnataka |     304099 |
| 1359 | Hassan         | IND         | Karnataka |      90803 |
| 1342 | Hospet         | IND         | Karnataka |      96322 |
| 1060 | Hubli-Dharwad  | IND         | Karnataka |     648298 |
| 1275 | Mandya         | IND         | Karnataka |     120265 |
| 1116 | Mangalore      | IND         | Karnataka |     273304 |
| 1074 | Mysore         | IND         | Karnataka |     480692 |
| 1193 | Raichur        | IND         | Karnataka |     157551 |
| 1170 | Shimoga        | IND         | Karnataka |     179258 |
| 1227 | Timkur         | IND         | Karnataka |     138903 |
+------+----------------+-------------+-----------+------------+
17 rows in set (0.04 sec)

mysql> select * from city where district='Karnataka' ORDER BY Name DESC
    -> ;
+------+----------------+-------------+-----------+------------+
| ID   | Name           | CountryCode | District  | Population |
+------+----------------+-------------+-----------+------------+
| 1227 | Timkur         | IND         | Karnataka |     138903 |
| 1170 | Shimoga        | IND         | Karnataka |     179258 |
| 1193 | Raichur        | IND         | Karnataka |     157551 |
| 1074 | Mysore         | IND         | Karnataka |     480692 |
| 1116 | Mangalore      | IND         | Karnataka |     273304 |
| 1275 | Mandya         | IND         | Karnataka |     120265 |
| 1060 | Hubli-Dharwad  | IND         | Karnataka |     648298 |
| 1342 | Hospet         | IND         | Karnataka |      96322 |
| 1359 | Hassan         | IND         | Karnataka |      90803 |
| 1108 | Gulbarga       | IND         | Karnataka |     304099 |
| 1237 | Gadag Betigeri | IND         | Karnataka |     134051 |
| 1119 | Davangere      | IND         | Karnataka |     266082 |
| 1161 | Bijapur        | IND         | Karnataka |     186939 |
| 1304 | Bidar          | IND         | Karnataka |     108016 |
| 1122 | Bellary        | IND         | Karnataka |     245391 |
| 1102 | Belgaum        | IND         | Karnataka |     326399 |
| 1030 | Bangalore      | IND         | Karnataka |    2660088 |
+------+----------------+-------------+-----------+------------+
17 rows in set (0.00 sec)

mysql> select * from city where district='Karnataka' ORDER BY Population ASC;
+------+----------------+-------------+-----------+------------+
| ID   | Name           | CountryCode | District  | Population |
+------+----------------+-------------+-----------+------------+
| 1359 | Hassan         | IND         | Karnataka |      90803 |
| 1342 | Hospet         | IND         | Karnataka |      96322 |
| 1304 | Bidar          | IND         | Karnataka |     108016 |
| 1275 | Mandya         | IND         | Karnataka |     120265 |
| 1237 | Gadag Betigeri | IND         | Karnataka |     134051 |
| 1227 | Timkur         | IND         | Karnataka |     138903 |
| 1193 | Raichur        | IND         | Karnataka |     157551 |
| 1170 | Shimoga        | IND         | Karnataka |     179258 |
| 1161 | Bijapur        | IND         | Karnataka |     186939 |
| 1122 | Bellary        | IND         | Karnataka |     245391 |
| 1119 | Davangere      | IND         | Karnataka |     266082 |
| 1116 | Mangalore      | IND         | Karnataka |     273304 |
| 1108 | Gulbarga       | IND         | Karnataka |     304099 |
| 1102 | Belgaum        | IND         | Karnataka |     326399 |
| 1074 | Mysore         | IND         | Karnataka |     480692 |
| 1060 | Hubli-Dharwad  | IND         | Karnataka |     648298 |
| 1030 | Bangalore      | IND         | Karnataka |    2660088 |
+------+----------------+-------------+-----------+------------+
17 rows in set (0.00 sec)

mysql> select Name, CountryCode from city where District='Karnataka';
+----------------+-------------+
| Name           | CountryCode |
+----------------+-------------+
| Bangalore      | IND         |
| Hubli-Dharwad  | IND         |
| Mysore         | IND         |
| Belgaum        | IND         |
| Gulbarga       | IND         |
| Mangalore      | IND         |
| Davangere      | IND         |
| Bellary        | IND         |
| Bijapur        | IND         |
| Shimoga        | IND         |
| Raichur        | IND         |
| Timkur         | IND         |
| Gadag Betigeri | IND         |
| Mandya         | IND         |
| Bidar          | IND         |
| Hospet         | IND         |
| Hassan         | IND         |
+----------------+-------------+
17 rows in set (0.00 sec)

mysql> select count(*) from city where District='Karnataka';
+----------+
| count(*) |
+----------+
|       17 |
+----------+
1 row in set (0.14 sec)

mysql> select max(Population) from city where District='Karnataka';
+-----------------+
| max(Population) |
+-----------------+
|         2660088 |
+-----------------+
1 row in set (0.06 sec)

mysql> select min(Population) from city where District='Karnataka';
+-----------------+
| min(Population) |
+-----------------+
|           90803 |
+-----------------+
1 row in set (0.03 sec)

mysql> select * from city where District='Karnataka' Order by Population DESC LIMIT 1;
+------+-----------+-------------+-----------+------------+
| ID   | Name      | CountryCode | District  | Population |
+------+-----------+-------------+-----------+------------+
| 1030 | Bangalore | IND         | Karnataka |    2660088 |
+------+-----------+-------------+-----------+------------+

mysql> select AVG(Population) from city where District="Karnataka";
+-----------------+
| AVG(Population) |
+-----------------+
|     377438.8824 |
+-----------------+
1 row in set (0.12 sec)

mysql> select contient, Count(*) as Total_Contries from Country Group By Continent;
ERROR 1054 (42S22): Unknown column 'contient' in 'field list'
mysql> select continent, Count(*) as Total_Contries from Country Group By Continent;
+---------------+----------------+
| continent     | Total_Contries |
+---------------+----------------+
| North America |             37 |
| Asia          |             51 |
| Africa        |             58 |
| Europe        |             46 |
| South America |             14 |
| Oceania       |             28 |
| Antarctica    |              5 |
+---------------+----------------+
7 rows in set (0.10 sec)


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
8 rows in set (0.17 sec)

mysql> Describe test2;
ERROR 1046 (3D000): No database selected
mysql> use test2;
Database changed
mysql> show tables;
+-----------------+
| Tables_in_test2 |
+-----------------+
| users           |
| users1          |
+-----------------+
2 rows in set (0.00 sec)

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
5 rows in set (0.03 sec)

mysql> update users1 SET user_name="Bavya" where user = 2;
Query OK, 1 row affected (0.13 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from users1;
+------+-----------+------------------+----------+-----------+
| user | user_name | email            | password | create_at |
+------+-----------+------------------+----------+-----------+
|    1 | sachin    | sachin@gmail.com | dgr677   | NULL      |
|    2 | Bavya     | kavya@gmail.com  | sa6788   | NULL      |
|    3 | ravi      | ravi@gmail.com   | dgr677   | NULL      |
|    4 | neethu    | neethu@gmail.com | d888hh7  | NULL      |
|    5 | anitha    | anitha@gmail.com | ui997    | NULL      |
+------+-----------+------------------+----------+-----------+
5 rows in set (0.00 sec)

mysql> show tables;
+-----------------+
| Tables_in_test2 |
+-----------------+
| users           |
| users1          |
+-----------------+
2 rows in set (0.00 sec)

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
5 rows in set (0.03 sec)

mysql> update users1 SET user_name="Bavya" where user = 2;
Query OK, 1 row affected (0.13 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from users1;
+------+-----------+------------------+----------+-----------+
| user | user_name | email            | password | create_at |
+------+-----------+------------------+----------+-----------+
|    1 | sachin    | sachin@gmail.com | dgr677   | NULL      |
|    2 | Bavya     | kavya@gmail.com  | sa6788   | NULL      |
|    3 | ravi      | ravi@gmail.com   | dgr677   | NULL      |
|    4 | neethu    | neethu@gmail.com | d888hh7  | NULL      |
|    5 | anitha    | anitha@gmail.com | ui997    | NULL      |
+------+-----------+------------------+----------+-----------+
5 rows in set (0.00 sec)

mysql> Alter table users1 rename to Employee;
Query OK, 0 rows affected (0.31 sec)

mysql> show tables;
+-----------------+
| Tables_in_test2 |
+-----------------+
| employee        |
| users           |
+-----------------+
2 rows in set (0.00 sec)

mysql> alter table Employee Add Phone_number varchar(15);
Query OK, 0 rows affected (0.31 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe users;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| user_id    | int          | YES  |     | NULL    |       |
| user_name  | varchar(100) | YES  |     | NULL    |       |
| email      | varchar(255) | YES  |     | NULL    |       |
| password   | varchar(255) | YES  |     | NULL    |       |
| created_at | timestamp    | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
5 rows in set (0.08 sec)

mysql> Truncate Table users;
Query OK, 0 rows affected (0.34 sec)

mysql> select * from users;
Empty set (0.00 sec)


mysql> select * from Employee;
+------+-----------+------------------+----------+-----------+--------------+
| user | user_name | email            | password | create_at | Phone_number |
+------+-----------+------------------+----------+-----------+--------------+
|    1 | sachin    | sachin@gmail.com | dgr677   | NULL      | NULL         |
|    2 | Bavya     | kavya@gmail.com  | sa6788   | NULL      | NULL         |
|    3 | ravi      | ravi@gmail.com   | dgr677   | NULL      | NULL         |
|    4 | neethu    | neethu@gmail.com | d888hh7  | NULL      | NULL         |
|    5 | anitha    | anitha@gmail.com | ui997    | NULL      | NULL         |
+------+-----------+------------------+----------+-----------+--------------+
5 rows in set (0.00 sec)

mysql> delete from Employee where email="ravi@gmail.com";
Query OK, 1 row affected (0.08 sec)

mysql> select * from Employee;
+------+-----------+------------------+----------+-----------+--------------+
| user | user_name | email            | password | create_at | Phone_number |
+------+-----------+------------------+----------+-----------+--------------+
|    1 | sachin    | sachin@gmail.com | dgr677   | NULL      | NULL         |
|    2 | Bavya     | kavya@gmail.com  | sa6788   | NULL      | NULL         |
|    4 | neethu    | neethu@gmail.com | d888hh7  | NULL      | NULL         |
|    5 | anitha    | anitha@gmail.com | ui997    | NULL      | NULL         |
+------+-----------+------------------+----------+-----------+--------------+
4 rows in set (0.00 sec)


mysql> create table User(
    -> user_id INT AUTO_INCREMENT PRIMARY KEY,
    -> user_name VARCHAR(100) NOT NULL,
    -> email VARCHAR(100) NOT NULL UNIQUE,
    -> password VARCHAR(255) NOT NULL,
    -> created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.27 sec)

mysql> describe User;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| user_id    | int          | NO   | PRI | NULL              | auto_increment    |
| user_name  | varchar(100) | NO   |     | NULL              |                   |
| email      | varchar(100) | NO   | UNI | NULL              |                   |
| password   | varchar(255) | NO   |     | NULL              |                   |
| created_at | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)




mysql> create table User(
    -> user_id INT AUTO_INCREMENT PRIMARY KEY,
    -> user_name VARCHAR(100) NOT NULL,
    -> email VARCHAR(100) NOT NULL UNIQUE,
    -> password VARCHAR(255) NOT NULL,
    -> created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.27 sec)

mysql> describe User;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| user_id    | int          | NO   | PRI | NULL              | auto_increment    |
| user_name  | varchar(100) | NO   |     | NULL              |                   |
| email      | varchar(100) | NO   | UNI | NULL              |                   |
| password   | varchar(255) | NO   |     | NULL              |                   |
| created_at | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)

 
mysql> insert into User (user_name, email, password) values("Rahul", "rahul@gmail.com", "12ft4");
Query OK, 1 row affected (0.14 sec)

mysql> insert into User (user_name, email, password) values("Rahul", "rahul@gmail.com", "12ft4");
ERROR 1062 (23000): Duplicate entry 'rahul@gmail.com' for key 'user.email'

mysql> insert into User (user_name, email, password) values("Rahul", "rahul2@gmail.com", "12ft4");
Query OK, 1 row affected (0.07 sec)

mysql> insert into User (user_name, email, password) values("kiran", "kiran2@gmail.com", "88ft4");
Query OK, 1 row affected (0.07 sec)

mysql> select * from User;
+---------+-----------+------------------+----------+---------------------+
| user_id | user_name | email            | password | created_at          |
+---------+-----------+------------------+----------+---------------------+
|       1 | Rahul     | rahul@gmail.com  | 12ft4    | 2025-11-22 20:30:59 |
|       3 | Rahul     | rahul2@gmail.com | 12ft4    | 2025-11-22 20:32:34 |
|       4 | kiran     | kiran2@gmail.com | 88ft4    | 2025-11-22 20:33:04 |
+---------+-----------+------------------+----------+---------------------+
3 rows in set (0.00 sec)