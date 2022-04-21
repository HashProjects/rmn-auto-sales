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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle_problems`
--

LOCK TABLES `vehicle_problems` WRITE;
/*!40000 ALTER TABLE `vehicle_problems` DISABLE KEYS */;
INSERT INTO `vehicle_problems` VALUES (20,57,0,'Cracked Windshield',30,NULL),(20,58,0,'Dirty Oil',46,NULL),(21,59,0,'Broken Tail Light',48,NULL),(21,60,0,'Cracked Windshield',61,NULL),(22,61,0,'Cracked Windshield',45,NULL),(22,62,0,'Broken Tail Light',33,NULL),(23,63,0,'Broken Tail Light',60,NULL),(23,64,0,'Flat Tire',77,NULL),(24,65,0,'Broken Tail Light',85,NULL),(24,66,0,'Broken Tail Light',44,NULL),(25,67,2,'Low Transmission Fluid',99,NULL),(25,68,3,'Broken Tail Light',66,NULL),(27,70,1,'Broken Tail Light',41,NULL),(27,70,2,'Dirty Oil',55,NULL),(27,71,1,'Flat Tire',78,NULL),(27,71,2,'Broken Tail Light',54,NULL),(27,71,3,'Flat Tire',34,NULL),(28,72,1,'Broken Tail Light',28,NULL),(28,72,2,'Dirty Oil',65,NULL),(28,73,1,'Cracked Windshield',64,NULL),(28,73,2,'Dirty Oil',76,NULL),(28,73,3,'Broken Tail Light',87,NULL),(29,74,1,'Low Transmission Fluid',75,NULL),(29,74,2,'Flat Tire',91,NULL),(29,75,1,'Cracked Windshield',98,NULL),(29,75,2,'Low Transmission Fluid',42,NULL),(29,75,3,'Dirty Oil',67,NULL),(30,76,1,'Flat Tire',41,NULL),(30,76,2,'Dirty Oil',79,NULL),(30,77,1,'Cracked Windshield',48,NULL),(30,77,2,'Flat Tire',43,NULL),(30,77,3,'Broken Tail Light',96,NULL),(31,78,1,'Broken Tail Light',46,NULL),(31,78,2,'Cracked Windshield',46,NULL),(31,79,1,'Dirty Oil',74,NULL),(31,79,2,'Broken Tail Light',97,NULL),(31,79,3,'Broken Tail Light',47,NULL);
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

-- Dump completed on 2022-04-21 11:17:33
