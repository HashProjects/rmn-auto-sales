-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: rmn_auto_sales
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.21.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `vehicle_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_vin` varchar(17) NOT NULL,
  `vehicle_make` varchar(45) NOT NULL,
  `vehicle_model` varchar(45) NOT NULL,
  `vehicle_year` varchar(45) NOT NULL,
  `vehicle_color` varchar(45) NOT NULL,
  `vehicle_miles` double NOT NULL,
  `vehicle_condition` varchar(45) NOT NULL,
  `vehicle_style` varchar(45) NOT NULL,
  `vehicle_interior_color` varchar(45) NOT NULL,
  `vehicle_list_price` double NOT NULL,
  `vehicle_sale_price` double NOT NULL,
  `vehicle_sold` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'2323423234','Lexus','Ct200h','2016','Silver',33882,'Excellent','Hatchback','Black',8000,8999,0),(2,'973249872333','Honda','Accord','2015','Black',85000,'Good','Sedan','Brown',7000,8000,1),(3,'348923978','Chevy','Astro','2000','Maroon',200200,'Fair','Van','Black',2000,2500,0),(13,'39974628N21','Ford','Car','2011','Red',10000,'Fair','Coupe','9800',8100,0,0),(14,'157540514N12','Infinity','Car','2017','Red',10000,'Excellent','Truck','8900',7600,0,0),(15,'107948906N24','Toyota','Car','2019','Red',10000,'Excellent','Sedan','7100',5500,0,0),(16,'141811345N28','Toyota','Car','2018','Red',10000,'Fair','Van','10000',10200,0,0),(17,'27339171N24','Toyota','Car','2012','Red',10000,'Excellent','Van','7300',8900,0,0),(18,'124960196N14','Toyota','Car','2018','Red',10000,'Excellent','Coupe','8300',10500,0,0),(19,'23727033N24','Infinity','Car','2015','Red',10000,'Fair','Van','5600',6300,0,1),(20,'4686972N19','GCM','Car','2021','Red',10000,'Good','Truck','4900',5800,0,0),(21,'68837661N21','Ford','Car','2014','Red',10000,'Fair','Van','5300',6700,0,0),(22,'167615233N21','Infinity','Car','2020','Red',10000,'Good','Coupe','4900',7700,0,0),(23,'174136733N16','Infinity','Car','2011','Red',10000,'Excellent','Sedan','5900',7000,0,0),(24,'92891912N0','Infinity','Car','2017','Red',10000,'Fair','Coupe','4400',9700,0,0),(25,'17221351N23','Toyota','Car','2016','Red',10000,'Good','Coupe','7600',7200,0,0),(26,'149849330N30','Toyota','Car','2016','Red',10000,'Fair','Sedan','4000',7200,0,0),(27,'137180661N29','Toyota','Car','2014','Red',10000,'Fair','Coupe','4200',8500,0,0),(30,'3719296N28','Ford','Car','2020','Black',10000,'Fair','Van','4600',8000,0,1),(31,'128022334N25','GMC','Car','2018','Blue',10000,'Excellent','Sedan','6400',8800,0,0),(32,'31319914N16','Ford','Car','2018','Black',10000,'Excellent','Sedan','9200',6000,0,0),(33,'135465738N27','Chevy','Car','2017','Red',10000,'Excellent','Sedan','8900',10700,0,0),(34,'140094370N18','GMC','Car','2015','Red',10000,'Excellent','Truck','9800',9000,0,0),(35,'137103065N8','Toyota','Car','2011','Silver',10000,'Fair','Truck','9000',9300,0,0),(36,'114943814N26','Chevy','Car','2019','Blue',10000,'Good','Coupe','4800',6600,0,0),(37,'160208732N19','Toyota','Car','2019','Blue',10000,'Fair','Van','6100',10300,0,0),(38,'44278207N25','Honda','Car','2015','Silver',10000,'Fair','Sedan','7100',5800,0,0),(39,'713354N22','Toyota','Car','2011','Blue',10000,'Good','Truck','6000',6200,0,1),(40,'29694983N20','Infinity','Car','2018','Blue',10000,'Good','Truck','4500',6500,0,1),(41,'60346730N29','GMC','Car','2021','Silver',10000,'Fair','Coupe','4400',6400,0,0),(42,'42265315N17','Toyota','Car','2012','Blue',10000,'Fair','Truck','7800',10300,0,1),(43,'33854470N3','GMC','Car','2011','Blue',10000,'Fair','Coupe','9600',9200,0,0),(44,'131848325N10','Honda','Car','2015','Silver',10000,'Excellent','Van','4000',8100,0,0),(45,'31941114N18','GMC','Car','2017','Red',10000,'Good','Truck','6300',6900,0,0),(46,'85843377N2','Chevy','Car','2014','Silver',10000,'Excellent','Truck','5000',8400,0,0),(47,'153800678N12','GMC','Car','2014','Red',10000,'Fair','Sedan','7800',9800,0,0),(48,'79930124N28','Honda','Car','2018','Blue',10000,'Excellent','Truck','9900',8200,0,1),(49,'85005275N17','Ford','Car','2017','White',10000,'Fair','Coupe','9700',5200,0,0),(50,'158439168N13','Honda','Car','2017','Blue',10000,'Good','Coupe','9400',6900,0,0),(51,'33375556N5','Infinity','Car','2015','Blue',10000,'Good','Van','9900',6500,0,0),(52,'45361614N4','GMC','Car','2010','Blue',10000,'Good','Van','7400',6300,0,0),(53,'127809556N22','Ford','Car','2020','Black',10000,'Excellent','Sedan','5800',6800,0,0),(57,'144277238N8','Ford','Car','2017','White',10000,'Good','Truck','9500',5400,0,0),(58,'123538491N9','GMC','Car','2020','White',10000,'Excellent','Van','6900',6900,0,1),(59,'70495457N10','GMC','Car','2022','Silver',10000,'Good','Sedan','4300',9400,0,0),(60,'22917785N27','Honda','Car','2022','Red',10000,'Good','Sedan','5400',8700,0,0),(61,'91266180N20','Chevy','Car','2014','Blue',10000,'Fair','Van','7900',7900,0,0),(62,'46296175N2','Ford','Car','2016','Red',10000,'Fair','Truck','7400',5800,0,0),(63,'19106140N29','Infinity','Car','2010','Black',10000,'Fair','Sedan','7300',8500,0,1),(64,'175119133N25','Toyota','Car','2011','Red',10000,'Fair','Coupe','8300',6100,0,0),(65,'17612253N6','Toyota','Car','2022','Silver',10000,'Excellent','Sedan','9200',8600,0,0),(66,'95085011N3','GMC','Car','2018','White',10000,'Excellent','Van','6600',9500,0,0),(67,'71999429N1','Toyota','Car','2013','Red',10000,'Excellent','Van','6500',7900,0,0),(68,'4248325N0','GMC','Car','2022','Blue',10000,'Excellent','Coupe','5800',7000,0,0),(70,'130535741N30','GMC','Car','2018','White',10000,'Good','Coupe','8500',6300,0,0),(71,'115861074N17','Ford','Car','2016','Blue',10000,'Fair','Van','8300',7000,0,0),(72,'76694011N17','Toyota','Car','2013','Silver',10000,'Good','Van','9400',9400,0,0),(73,'173014693N18','GMC','Car','2010','White',10000,'Good','Van','7800',6400,0,0),(74,'14775838N11','Chevy','Car','2011','Blue',10000,'Excellent','Truck','7400',10000,0,0),(75,'129891539N20','Toyota','Car','2012','Silver',10000,'Good','Coupe','9400',9600,0,1),(76,'123237785N0','Honda','Car','2010','Red',10000,'Fair','Truck','8500',9600,0,0),(77,'148154718N18','Ford','Car','2017','Blue',10000,'Excellent','Van','5800',10600,0,0),(78,'911873N6','Honda','Car','2019','Silver',10000,'Fair','Truck','7000',5800,0,0),(79,'31575701N5','Ford','Car','2015','Blue',10000,'Excellent','Truck','8400',5400,0,1);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-21 11:17:33
