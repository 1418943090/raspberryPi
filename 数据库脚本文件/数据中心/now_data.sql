
create table now_data(

    id int(11) NOT NULL AUTO_INCREMENT,
    sensor_id varchar(20) primary key not null,
    type varchar(20),
    name varchar(20),
    value varchar(10),
    isComplex int ,  #0不是复合传感器 1 是复合传感器
    sensor_type varchar(20),
    net_type varchar(20)
);


CREATE TABLE `sensor_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `net_type` varchar(255) DEFAULT NULL,
  `sensor_id` varchar(255) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `value` decimal(19,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
)


create table current_mode_name(
 name varchar(20) primary key not null,

);

create table equ(
   id varchar(10) primary key not null,
   net_type varchar(20)
);

create table sensor(
   id varchar(10) primary key not null,
   sensor_type varchar(10),
   net_type varchar(20)

);

create table node_information(
    name  varchar(20) primary key not null,
    style varchar(20),
    status varchar(5)
);

#####################情景模式#################################################
create table scene_mode_name(
   name varchar(50) primary key,
   equ varchar(200)
);


create table current_scene(
   name varchar(20) primary key not null
);

###################定时中心#############################################

create table set_name(

  name varchar(20) primary key not null,
  status varchar(5)
);

create table timing(
     equ_name   varchar(500),
     date       varchar(5),
     shour      varchar(5),
     sminute    varchar(5),
     ehour      varchar(5),
     eminute    varchar(5),
     type       int,
     days       varchar(20),
     name       varchar(50)

);



#########智能中心#################################################
create table smart(
    name    varchar(50) primary key ,
    sensor  varchar(20),
    compare varchar(10),
    value   varchar(10),
    operate varchar(10),
    equ     varchar(500),
    status  varchar(10)
);






















