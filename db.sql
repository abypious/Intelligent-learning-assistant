/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.27 : Database - autism
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`autism` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `autism`;

/*Table structure for table `experts` */

DROP TABLE IF EXISTS `experts`;

CREATE TABLE `experts` (
  `exp_id` int NOT NULL AUTO_INCREMENT,
  `exp_name` varchar(20) NOT NULL,
  `experience` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `login_id` int DEFAULT NULL,
  PRIMARY KEY (`exp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `experts` */

insert  into `experts`(`exp_id`,`exp_name`,`experience`,`gender`,`place`,`phone`,`email`,`login_id`) values 
(12,'Anuraj','3yr','male','KOZHIKODE',9876540000,'anuraj@gmail.com',14);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_b_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `parent_f_b` text,
  `f_b_date` date NOT NULL,
  PRIMARY KEY (`f_b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`f_b_id`,`user_id`,`parent_f_b`,`f_b_date`) values 
(3,13,'doing good','1972-04-01'),
(5,13,'dtsiakajfnfxufjeiox','2022-01-17'),
(6,13,'dtsiakajfnfxufjeiox','2022-01-17'),
(7,13,'hello friend','2022-01-17'),
(8,13,'juy','2022-01-17'),
(9,13,'okkk','2022-01-18'),
(10,26,'okk','2022-01-19');

/*Table structure for table `guidance` */

DROP TABLE IF EXISTS `guidance`;

CREATE TABLE `guidance` (
  `g_id` int NOT NULL AUTO_INCREMENT,
  `report_id` int NOT NULL,
  `exp_id` int NOT NULL,
  `g_info` text NOT NULL,
  PRIMARY KEY (`g_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `guidance` */

insert  into `guidance`(`g_id`,`report_id`,`exp_id`,`g_info`) values 
(1,1,7,'gfcdqe'),
(2,1,7,'ewlrnewiofhewiofj'),
(3,2,14,'ok'),
(4,2,14,'hiiiiiiiiiiiiiiiiii'),
(5,2,14,'okkkkkkkkkkkkkkkkk'),
(6,4,14,'okkk'),
(7,3,14,'will chk');

/*Table structure for table `intraction` */

DROP TABLE IF EXISTS `intraction`;

CREATE TABLE `intraction` (
  `intr_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` varchar(11) NOT NULL,
  `exp_id` int NOT NULL,
  `intr_date` varchar(45) NOT NULL,
  `intr_time` varchar(54) NOT NULL,
  PRIMARY KEY (`intr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `intraction` */

insert  into `intraction`(`intr_id`,`user_id`,`questions`,`exp_id`,`intr_date`,`intr_time`) values 
(1,13,'whaatis 1+1',7,'2021-09-24','06:33:13'),
(6,26,'okkkk',14,'2022-01-19','16:48:33');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`user_id`,`user_name`,`password`,`user_type`) values 
(1,'jebin','autism','admin'),
(13,'joe','Joe12345','student'),
(14,'anu','Anu12345','expert'),
(20,'qwerty123','qwerty123','student'),
(24,'qwerty1234','qwerty1234','student'),
(26,'siva','qwerty56','student');

/*Table structure for table `medical_report` */

DROP TABLE IF EXISTS `medical_report`;

CREATE TABLE `medical_report` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `report_info` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `exp_id` int NOT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `medical_report` */

insert  into `medical_report`(`report_id`,`user_id`,`report_info`,`exp_id`) values 
(1,13,'milo.jpg',7),
(2,13,'storage_emulated_0_DCIM_Camera_IMG_20220117_173552.jpg',14),
(3,26,'storage_emulated_0_Android_data_cn.wps.moffice_eng_.cache_KingsoftOffice_file_download_0f1ba24c-5665-4658-8ead-3bc76538100e_com.whatsapp.provider.media_3570-Article_Text-5660-1-10-20200122_1.pdf',14),
(4,26,'storage_emulated_0_DCIM_Camera_IMG_20220119_153034.jpg',14);

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `parent_id` int NOT NULL AUTO_INCREMENT,
  `login_id` int DEFAULT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `contact` bigint DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`parent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `parent` */

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file` text NOT NULL,
  `mat_type` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`id`,`file`,`mat_type`) values 
(1,'1.mp4','music'),
(2,'2.mp4','audio'),
(3,'3.mp4','video');

/*Table structure for table `response` */

DROP TABLE IF EXISTS `response`;

CREATE TABLE `response` (
  `res_id` int NOT NULL AUTO_INCREMENT,
  `intr_id` int NOT NULL,
  `res_info` text NOT NULL,
  `res_date` varchar(43) NOT NULL,
  `res_time` varchar(43) NOT NULL,
  PRIMARY KEY (`res_id`,`intr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `response` */

insert  into `response`(`res_id`,`intr_id`,`res_info`,`res_date`,`res_time`) values 
(1,1,'okkkkkkkkk','2021-09-24','13:07:06'),
(2,6,'willl','2022-01-19','16:50:08');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `std_id` int NOT NULL AUTO_INCREMENT,
  `std_name` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `phone_no` bigint NOT NULL,
  `description` text NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`std_id`,`std_name`,`dob`,`place`,`gender`,`phone_no`,`description`,`user_id`) values 
(1,'Joe','8/5/2001','calicut','male',9961525401,'abcdefg\r\n',13),
(2,'siva','12/12/2000','Calicut','Male',6958362547,'description',26);

/*Table structure for table `study_materials` */

DROP TABLE IF EXISTS `study_materials`;

CREATE TABLE `study_materials` (
  `std_mat_id` int NOT NULL AUTO_INCREMENT,
  `std_mat_info` varchar(500) NOT NULL,
  `up_date` varchar(44) NOT NULL,
  `exp_id` varchar(11) NOT NULL,
  `mat_type` varchar(50) NOT NULL,
  PRIMARY KEY (`std_mat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `study_materials` */

insert  into `study_materials`(`std_mat_id`,`std_mat_info`,`up_date`,`exp_id`,`mat_type`) values 
(1,'ADMINHOME.html','2021-09-23','12','text'),
(2,'ADD_GUIDANCE.html','2021-09-24','16','video'),
(4,'ADDTIPS.html','2021-09-24','16','video'),
(5,'ADD_EXPERTS.html','2021-09-24','14','video'),
(6,'volley.jar','2022-01-15','16','text'),
(7,'ICRITO48877.2020.9197805.pdf','2022-01-19','14','text');

/*Table structure for table `tips` */

DROP TABLE IF EXISTS `tips`;

CREATE TABLE `tips` (
  `tips_id` int NOT NULL AUTO_INCREMENT,
  `tips_info` text,
  `exp_id` int NOT NULL,
  PRIMARY KEY (`tips_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `tips` */

insert  into `tips`(`tips_id`,`tips_info`,`exp_id`) values 
(9,'SGDHDH',12),
(10,'FGGGDRZ',12),
(11,'SALMAN',12),
(12,'newwwww',7),
(13,'',7),
(14,'wkadhuiufh',7),
(15,'Follow the prescribed medicine',7),
(16,'sasa',14);

/*Table structure for table `video_frame` */

DROP TABLE IF EXISTS `video_frame`;

CREATE TABLE `video_frame` (
  `v_f_id` int NOT NULL AUTO_INCREMENT,
  `id` int NOT NULL,
  `ratio` float DEFAULT NULL,
  `std_id` int NOT NULL,
  PRIMARY KEY (`v_f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `video_frame` */

insert  into `video_frame`(`v_f_id`,`id`,`ratio`,`std_id`) values 
(1,1,1,1),
(2,2,0.833333,1),
(3,3,1,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
