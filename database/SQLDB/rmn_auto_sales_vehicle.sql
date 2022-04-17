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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'2323423234','Lexus','Ct200h','2016','Silver',33882,'Excellent','Hatchback','Black',8000,8999,0),(2,'973249872333','Honda','Accord','2015','Black',85000,'Good','Sedan','Brown',7000,8000,0),(3,'348923978','Chevy','Astro','2000','Maroon',200200,'Fair','Van','Black',2000,2500,0),(13,'39974628N21','Ford','Car','2011','Red',10000,'Fair','Coupe','9800',8100,0,0),(14,'157540514N12','Infinity','Car','2017','Red',10000,'Excellent','Truck','8900',7600,0,0),(15,'107948906N24','Toyota','Car','2019','Red',10000,'Excellent','Sedan','7100',5500,0,0),(16,'141811345N28','Toyota','Car','2018','Red',10000,'Fair','Van','10000',10200,0,0),(17,'27339171N24','Toyota','Car','2012','Red',10000,'Excellent','Van','7300',8900,0,0),(18,'124960196N14','Toyota','Car','2018','Red',10000,'Excellent','Coupe','8300',10500,0,0),(19,'23727033N24','Infinity','Car','2015','Red',10000,'Fair','Van','5600',6300,0,0),(20,'4686972N19','GCM','Car','2021','Red',10000,'Good','Truck','4900',5800,0,0),(21,'68837661N21','Ford','Car','2014','Red',10000,'Fair','Van','5300',6700,0,0),(22,'167615233N21','Infinity','Car','2020','Red',10000,'Good','Coupe','4900',7700,0,0),(23,'174136733N16','Infinity','Car','2011','Red',10000,'Excellent','Sedan','5900',7000,0,0),(24,'92891912N0','Infinity','Car','2017','Red',10000,'Fair','Coupe','4400',9700,0,0),(25,'17221351N23','Toyota','Car','2016','Red',10000,'Good','Coupe','7600',7200,0,0),(26,'149849330N30','Toyota','Car','2016','Red',10000,'Fair','Sedan','4000',7200,0,0),(27,'137180661N29','Toyota','Car','2014','Red',10000,'Fair','Coupe','4200',8500,0,0);
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

-- Dump completed on 2022-04-16 23:30:50
