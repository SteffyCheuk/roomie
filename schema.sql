drop table if exists users;
create table users (
  id integer primary key autoincrement,
  first_name text not null,
  middle_name text,
  last_name text not null,  
  dob date not null,
  group integer not null,
  alias text not null
)

drop table if exists groups;
create table groups (
  id integer primary key autoincrement,
  name text not null
)

drop table if exists members;
create table members (
  id integer primary key autoincrement,
  group_id integer not null,
  user_id integer not null
)

drop table if exists lists;
create table lists (
  id integer primary key autoincrement,
  group_id integer,
  name text not null,
  description text 
)

drop table if exists list_items;
create table list_items (
  id integer primary key autoincrement,
  list_id integer not null,
  name text not null,
  unit text not null,
  quantity text not null,
)

drop table if exists messages;
create table messages (
  id integer primary key autoincrement,
  group_id integer not null,
  user_id integer not null,
  created_at integer not null,
  message text not null
)

