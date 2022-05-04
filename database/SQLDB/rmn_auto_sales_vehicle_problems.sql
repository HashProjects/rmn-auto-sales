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
-- Table structure for table `vehicle_problems`
--

DROP TABLE IF EXISTS `vehicle_problems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle_problems` (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_id` int NOT NULL,
  `problem_id` int NOT NULL,
  `problem_description` varchar(200) NOT NULL,
  `estimated_repair_cost` double NOT NULL,
  `actual_repair_cost` double DEFAULT NULL,
  PRIMARY KEY (`purchase_id`,`vehicle_id`,`problem_id`),
  KEY `fk_vehicle_id_idx` (`vehicle_id`),
  CONSTRAINT `fk` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`vehicle_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_purchase_id` FOREIGN KEY (`purchase_id`) REFERENCES `purchase` (`purchase_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle_purchase` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle_problems`
--

LOCK TABLES `vehicle_problems` WRITE;
/*!40000 ALTER TABLE `vehicle_problems` DISABLE KEYS */;
INSERT INTO `vehicle_problems` VALUES (20,57,0,'Cracked Windshield',30,NULL),(20,58,0,'Dirty Oil',46,NULL),(21,59,0,'Broken Tail Light',48,NULL),(21,60,0,'Cracked Windshield',61,NULL),(22,61,0,'Cracked Windshield',45,50),(22,62,0,'Broken Tail Light',33,NULL),(23,63,0,'Broken Tail Light',60,NULL),(23,64,0,'Flat Tire',77,NULL),(24,65,0,'Broken Tail Light',85,NULL),(24,66,0,'Broken Tail Light',44,NULL),(25,67,2,'Low Transmission Fluid',99,NULL),(25,68,3,'Broken Tail Light',66,NULL),(27,70,1,'Broken Tail Light',41,NULL),(27,70,2,'Dirty Oil',55,NULL),(27,71,1,'Flat Tire',78,NULL),(27,71,2,'Broken Tail Light',54,NULL),(27,71,3,'Flat Tire',34,NULL),(28,72,1,'Broken Tail Light',28,NULL),(28,72,2,'Dirty Oil',65,NULL),(28,73,1,'Cracked Windshield',64,NULL),(28,73,2,'Dirty Oil',76,NULL),(28,73,3,'Broken Tail Light',87,NULL),(29,74,1,'Low Transmission Fluid',75,NULL),(29,74,2,'Flat Tire',91,NULL),(29,75,1,'Cracked Windshield',98,NULL),(29,75,2,'Low Transmission Fluid',42,NULL),(29,75,3,'Dirty Oil',67,NULL),(30,76,1,'Flat Tire',41,NULL),(30,76,2,'Dirty Oil',79,NULL),(30,77,1,'Cracked Windshield',48,NULL),(30,77,2,'Flat Tire',43,NULL),(30,77,3,'Broken Tail Light',96,NULL),(31,78,1,'Broken Tail Light',46,NULL),(31,78,2,'Cracked Windshield',46,NULL),(31,79,1,'Dirty Oil',74,NULL),(31,79,2,'Broken Tail Light',97,NULL),(31,79,3,'Broken Tail Light',47,NULL),(32,80,1,'Broken Tail Light',69,NULL),(32,80,2,'Cracked Windshield',55,NULL),(32,81,1,'Dirty Oil',40,NULL),(32,81,2,'Cracked Windshield',75,100),(32,81,3,'Dirty Oil',42,41),(37,91,1,'Broken Tail Light',93,NULL),(37,91,2,'Dirty Oil',59,NULL),(37,92,1,'Flat Tire',89,NULL),(37,92,2,'Cracked Windshield',26,NULL),(37,92,3,'Low Transmission Fluid',26,NULL),(38,93,1,'Low Transmission Fluid',49,NULL),(38,93,2,'Low Transmission Fluid',43,NULL),(38,94,1,'Broken Tail Light',87,NULL),(38,94,2,'Dirty Oil',66,NULL),(38,94,3,'Cracked Windshield',80,NULL),(39,95,1,'Low Transmission Fluid',81,NULL),(39,95,2,'Dirty Oil',54,NULL),(39,96,1,'Low Transmission Fluid',52,NULL),(39,96,2,'Dirty Oil',77,NULL),(39,96,3,'Low Transmission Fluid',47,NULL),(43,99,1,'Cracked Windshield',69,NULL),(43,99,2,'Broken Tail Light',93,NULL),(43,99,3,'Dirty Oil',35,NULL),(43,99,4,'Low Transmission Fluid',40,NULL),(44,100,1,'Cracked Windshield',50,NULL),(44,100,2,'Low Transmission Fluid',43,NULL),(44,100,3,'Flat Tire',28,NULL),(44,100,4,'Dirty Oil',29,NULL),(44,101,1,'Cracked Windshield',70,NULL),(44,101,2,'Low Transmission Fluid',47,NULL),(44,101,3,'Broken Tail Light',76,NULL),(44,101,4,'Dirty Oil',95,NULL),(45,102,1,'Cracked Windshield',67,NULL),(46,103,1,'Dirty Oil',99,NULL),(46,103,2,'Low Transmission Fluid',38,NULL),(46,103,3,'Cracked Windshield',91,NULL),(46,103,4,'Broken Tail Light',43,NULL),(46,103,5,'Flat Tire',78,NULL),(47,104,1,'Low Transmission Fluid',83,NULL),(47,104,2,'Cracked Windshield',81,NULL),(47,104,3,'Dirty Oil',76,NULL),(47,104,4,'Flat Tire',92,NULL),(47,104,5,'Broken Tail Light',45,NULL),(48,105,1,'Broken Tail Light',81,NULL),(48,105,2,'Cracked Windshield',50,NULL),(48,105,3,'Flat Tire',98,NULL),(48,105,4,'Dirty Oil',29,NULL),(49,106,1,'Low Transmission Fluid',81,NULL),(49,106,2,'Flat Tire',82,NULL),(49,106,3,'Broken Tail Light',96,NULL),(49,106,4,'Dirty Oil',33,NULL),(49,106,5,'Cracked Windshield',26,NULL),(50,107,1,'Cracked Windshield',65,NULL),(50,107,2,'Low Transmission Fluid',32,NULL),(50,107,3,'Broken Tail Light',80,NULL),(50,107,4,'Flat Tire',76,NULL),(50,107,5,'Dirty Oil',72,NULL),(51,108,1,'Broken Tail Light',41,NULL),(51,108,2,'Low Transmission Fluid',78,NULL),(51,108,3,'Dirty Oil',62,NULL),(51,108,4,'Flat Tire',43,NULL),(51,108,5,'Cracked Windshield',64,NULL),(52,109,1,'Low Transmission Fluid',42,NULL),(52,109,2,'Dirty Oil',77,NULL),(52,109,3,'Broken Tail Light',51,NULL),(53,110,1,'Low Transmission Fluid',42,NULL),(53,110,2,'Dirty Oil',77,NULL),(53,110,3,'Broken Tail Light',51,NULL),(54,111,1,'Dirty Oil',91,NULL),(54,111,2,'Flat Tire',61,NULL),(54,111,3,'Cracked Windshield',41,NULL),(54,111,4,'Low Transmission Fluid',32,NULL),(54,111,5,'Broken Tail Light',81,NULL),(55,112,1,'Cracked Windshield',39,NULL),(55,112,2,'Broken Tail Light',69,NULL),(55,112,3,'Low Transmission Fluid',64,NULL),(55,112,4,'Dirty Oil',32,NULL),(56,113,1,'Flat Tire',53,NULL),(56,113,2,'Dirty Oil',88,NULL),(57,114,1,'Flat Tire',32,NULL),(58,115,1,'Dirty Oil',69,NULL),(58,115,2,'Flat Tire',34,NULL),(58,115,3,'Broken Tail Light',69,NULL),(59,116,1,'Cracked Windshield',28,NULL),(59,116,2,'Flat Tire',29,NULL),(59,116,3,'Dirty Oil',48,NULL),(60,117,1,'Flat Tire',83,NULL),(61,118,1,'Flat Tire',83,NULL),(61,119,1,'Broken Tail Light',32,NULL),(61,119,2,'Dirty Oil',91,NULL),(61,119,3,'Flat Tire',81,NULL),(61,119,4,'Cracked Windshield',41,NULL),(62,120,1,'Cracked Windshield',89,NULL),(63,121,1,'Flat Tire',93,NULL),(63,121,2,'Cracked Windshield',99,NULL),(63,121,3,'Dirty Oil',55,NULL),(63,121,4,'Low Transmission Fluid',52,NULL),(63,121,5,'Broken Tail Light',72,NULL),(64,122,1,'Cracked Windshield',73,100),(64,122,2,'Dirty Oil',36,40),(64,122,3,'Low Transmission Fluid',62,65),(65,125,1,'Dirty Oil',34,50),(65,125,2,'Cracked Windshield',58,100),(65,125,3,'Broken Tail Light',26,50),(65,126,1,'Flat Tire',61,NULL),(65,126,2,'Cracked Windshield',76,NULL),(65,126,3,'Dirty Oil',49,NULL),(65,126,4,'Low Transmission Fluid',75,NULL),(67,129,1,'Low Transmission Fluid',88,NULL),(67,129,2,'Broken Tail Light',31,NULL),(67,129,3,'Cracked Windshield',58,NULL),(67,129,4,'Flat Tire',36,NULL),(67,130,1,'Flat Tire',63,100),(67,130,2,'Cracked Windshield',57,1),(67,130,3,'Dirty Oil',32,1),(67,131,1,'Low Transmission Fluid',53,100),(67,131,2,'Dirty Oil',53,100),(67,131,3,'Broken Tail Light',67,100),(68,133,1,'Dirty Oil',31,35),(68,133,2,'Low Transmission Fluid',54,58),(68,134,1,'Dirty Oil',68,50),(68,134,2,'Broken Tail Light',25,30),(68,134,3,'Broken Tail Light',85,100),(69,135,1,'Flat Tire',95,NULL),(69,135,2,'Dirty Oil',92,NULL),(69,135,3,'Broken Tail Light',43,NULL),(69,135,4,'Low Transmission Fluid',97,NULL),(69,135,5,'Cracked Windshield',84,NULL),(70,136,1,'Low Transmission Fluid',72,NULL),(70,136,2,'Flat Tire',88,NULL),(70,136,3,'Dirty Oil',53,NULL),(70,137,1,'Broken Tail Light',87,100),(71,138,1,'Cracked Windshield',96,NULL),(71,138,2,'Dirty Oil',99,NULL),(71,138,3,'Low Transmission Fluid',52,NULL),(71,138,4,'Flat Tire',61,NULL),(71,138,5,'Broken Tail Light',43,NULL),(72,139,1,'Cracked Windshield',96,100),(72,139,2,'Dirty Oil',99,100),(72,139,3,'Low Transmission Fluid',52,53),(72,139,4,'Flat Tire',61,65),(72,139,5,'Broken Tail Light',43,43),(72,140,1,'Cracked Windshield',97,500),(72,140,2,'Low Transmission Fluid',96,56),(72,140,3,'Flat Tire',96,56),(73,141,1,'Broken Tail Light',82,1),(73,141,2,'Low Transmission Fluid',27,1),(73,141,3,'Flat Tire',39,1),(73,141,4,'Dirty Oil',62,1),(73,141,5,'Cracked Windshield',51,1),(74,142,1,'Flat Tire',53,NULL),(75,143,1,'Cracked Windshield',51,NULL),(75,143,2,'Low Transmission Fluid',81,NULL),(75,144,1,'Dirty Oil',48,NULL),(75,144,2,'Broken Tail Light',50,NULL),(75,144,3,'Low Transmission Fluid',75,NULL),(76,145,1,'Low Transmission Fluid',41,NULL),(76,145,2,'Dirty Oil',90,NULL),(76,146,1,'Low Transmission Fluid',92,NULL),(76,146,2,'Broken Tail Light',87,NULL),(76,146,3,'Low Transmission Fluid',31,NULL),(77,147,1,'Flat Tire',79,NULL),(77,147,2,'Broken Tail Light',28,NULL),(77,147,3,'Dirty Oil',82,NULL),(77,147,4,'Cracked Windshield',63,NULL),(78,148,1,'Flat Tire',42,NULL),(78,148,2,'Broken Tail Light',78,NULL),(78,148,3,'Low Transmission Fluid',65,NULL),(78,148,4,'Dirty Oil',76,NULL),(79,149,1,'Broken Tail Light',57,NULL),(79,149,2,'Cracked Windshield',53,NULL),(79,149,3,'Low Transmission Fluid',84,NULL),(79,149,4,'Dirty Oil',56,NULL),(79,150,1,'Low Transmission Fluid',81,NULL),(79,150,2,'Cracked Windshield',88,NULL),(79,150,3,'Flat Tire',100,NULL),(80,151,1,'Cracked Windshield',65,NULL),(80,151,2,'Broken Tail Light',37,NULL),(80,151,3,'Dirty Oil',71,NULL),(80,151,4,'Flat Tire',67,NULL),(80,151,5,'Low Transmission Fluid',72,NULL),(81,152,1,'Broken Tail Light',91,NULL),(81,152,2,'Low Transmission Fluid',97,NULL),(81,152,3,'Flat Tire',45,NULL),(82,153,1,'Broken Tail Light',76,NULL),(82,153,2,'Flat Tire',40,NULL),(83,154,1,'Flat Tire',43,NULL),(83,154,2,'Dirty Oil',77,NULL),(83,154,3,'Low Transmission Fluid',25,NULL),(84,155,1,'Cracked Windshield',49,NULL),(84,155,2,'Dirty Oil',51,NULL),(84,155,3,'Broken Tail Light',38,NULL),(85,156,1,'Low Transmission Fluid',31,NULL),(86,157,1,'Flat Tire',92,NULL),(87,158,1,'Low Transmission Fluid',30,NULL),(87,158,2,'Dirty Oil',48,NULL),(87,158,3,'Flat Tire',47,NULL),(87,158,4,'Broken Tail Light',89,NULL),(87,159,1,'Dirty Oil',59,75),(87,159,2,'Low Transmission Fluid',35,150),(87,159,3,'Broken Tail Light',61,150),(88,160,1,'Low Transmission Fluid',92,NULL),(88,160,2,'Broken Tail Light',60,NULL),(88,160,3,'Dirty Oil',66,NULL),(88,160,4,'Flat Tire',93,NULL);
/*!40000 ALTER TABLE `vehicle_problems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04  9:28:18
