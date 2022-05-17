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
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale` (
  `sale_id` int NOT NULL AUTO_INCREMENT,
  `sale_date` datetime NOT NULL,
  `total_due` double NOT NULL,
  `down_payment` double NOT NULL,
  `financed_amount` double NOT NULL,
  `employee_commission` double NOT NULL,
  `vehicle_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`sale_id`,`customer_id`,`vehicle_id`),
  KEY `fk_vehicle_id_idx` (`vehicle_id`),
  KEY `fk_employee_id_idx` (`employee_id`),
  KEY `fk_sale_2_idx` (`customer_id`),
  CONSTRAINT `fk_sale_1` FOREIGN KEY (`employee_id`) REFERENCES `sales_people` (`salesperson_id`),
  CONSTRAINT `fk_sale_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `fk_sale_3` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES (37,'2022-05-02 00:00:00',8000,5000,3000,1000,134,51,6),(39,'2022-05-03 00:00:00',9000,5000,4000,1000,159,53,7),(40,'2022-05-04 00:00:00',8000,5000,3000,1000,161,54,6),(41,'2022-05-04 00:00:00',8000,5000,3000,1000,162,55,5),(42,'2022-05-13 00:00:00',8000,5000,3000,1000,163,56,7),(43,'2022-05-17 00:00:00',12000,8000,4000,1000,114,57,3),(44,'2022-05-17 00:00:00',9000,7000,2000,1000,116,58,4),(45,'2022-05-17 00:00:00',13000,10000,3000,1000,121,59,6);
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-17 14:30:42
