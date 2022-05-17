
drop table employee_info;
create table employee_info (
id serial primary key,
fname varchar(50) not NULL,
lname varchar(50) not NULL,
erole varchar(50)
);

insert into employee_info values (1, 'Larry', 'King', 'department employee');
insert into employee_info values (2, 'Jerry', 'Jenkins', 'department supervisor');
insert into employee_info values (3, 'Billy', 'Bob', 'department head');
insert into employee_info values (4, 'Mister', 'Cord', 'benco');
insert into employee_info values (5, 'Izzi', 'Saucy', 'department employee');
insert into employee_info values (default, 'Izzi', 'Saucy', 'department employee');
insert into employee_info values (50, 'Selenium', 'Test', 'department employee');
insert into employee_info values (51, 'Selenium', 'Test', 'department employee');
insert into employee_info values (52, 'Presentation', 'Test', 'department employee');


update employee_info set fname = 'Larry' where id = 1;
select * from employee_info;



drop table form;
create table form (
id serial primary key,
fname varchar(50),
lname varchar(50),
event_date varchar(50),
event_time varchar(50),
location varchar(50),
description varchar(50),
cost INT,
grading_format varchar(50),
type_of_event varchar(50),
employee_id serial references employee_info(id),
passing_cutoff varchar(50) default 'C',
urgent varchar(50) default 'No',
final_grade varchar(50),
work_just varchar(50),
add_info varchar(50) default null,
reject_form varchar(50) default 'No',
deny_reason varchar(50) default null,
dsup_approval varchar(50) default 'No',
dhead_approval varchar(50) default 'No',
benco_approval varchar(50) default 'No'
);

insert into form values (default, 'Larry', 'King', '03/23/2022', '08:00AM', 'Texas', 'University Course', 
7500, 'txt', 'university course', 1, default, default, 'B', 'Advance knowledge', default, default, default, default, default, default);

insert into form values (default, 'Izzi', 'Saucy', '04/12/2022', '09:00AM', 'Texas', 'College Course', 
6200, 'txt', 'college course', 5, default, default, 'A', 'Benefit Work Role', default, default, default, default, default, default);


select * from form;
select * from form where employee_id = 1;




drop table login;
create table login (
id serial primary key,
username varchar(50) not null,
password varchar(50) not null
);

insert into login values (1, 'LKing', 'password');
insert into login values (2, 'JJenkins', 'password');
insert into login values (3, 'BBob', 'password');
insert into login values (4, 'MCord', 'password');

select * from login;


--drop table login;
--create table login (
--id serial primary key,
--e_id int references employee_info(id),
--username varchar(50) not null,
--password varchar(50) not null
--);








