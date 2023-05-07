# SQL Query
## Create Table
```
CREATE TABLE students(
sid int NOT NULL,
name varchar(255),
course varchar(255),

PRIMARY KEY (sid)
);
```

## insert values with columns names
```
INSERT INTO students(sid,name,course)
VALUES (1,'Hamza','AI')
```

```
INSERT INTO students(sid,,course)
VALUES (1,'AI')
```

## insert values without columns names
```
INSERT INTO students
VALUES (2,'Hamza','AI')
```

# Insert mutlitple values 
```
insert into students
values 
(4,'A','Blockchain'),
(5,'C','AI'),
(6,'D','AI')
```

# DML 
* Select Query
```
SELECT * FROM students
```

* select perticular columns from table
```
SELECT course,sid,name FROM students

```

# apply filter
```
select * from students
WHERE
course = 'AI' 
and sid >= 5


select * from students
WHERE
course = 'AI' 
or course = 'Blockchain'


```

# in operator
```
select * from students
WHERE
course IN ('AI' ,'Blockchain')


```


# all query
```
CREATE TABLE students(
sid int NOT NULL,
name varchar(255),
course varchar(255),

PRIMARY KEY (sid)
);

INSERT INTO students(sid,name,course)
VALUES (1,'Hamza','AI')

INSERT INTO students 
values (2,'Yaseer','Blockchain')



INSERT INTO students(sid,name,course)
VALUES (1,'Hamza','AI')



INSERT INTO students(sid,course)
VALUES (3,'AI')


insert into students
values (4,'A','Blockchain'),
(5,'C','AI'),(6,'D','AI')


SELECT * FROM students


SELECT course,sid,name FROM students

select sid as student_id, name, course FROM students


select * from students
WHERE
sid IN (1,3,5)

UPDATE students 
set
name = 'Ali'
where 
sid = 3

delete  from students 
WHERE 
sid = 6


alter TABLE students 
add 
father_name varchar(255)





```