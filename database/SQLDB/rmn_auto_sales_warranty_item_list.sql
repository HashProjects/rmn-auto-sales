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
-- Table structure for table `warranty_item_list`
--

DROP TABLE IF EXISTS `warranty_item_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warranty_item_list` (
  `item_id` int NOT NULL,
  `warranty_sale_id` int NOT NULL,
  `warranty_id` int NOT NULL,
  PRIMARY KEY (`item_id`,`warranty_sale_id`,`warranty_id`),
  KEY `fk_item_id_idx` (`item_id`) /*!80000 INVISIBLE */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranty_item_list`
--

LOCK TABLES `warranty_item_list` WRITE;
/*!40000 ALTER TABLE `warranty_item_list` DISABLE KEYS */;
INSERT INTO `warranty_item_list` VALUES (1,17,11),(1,18,12),(1,59,55),(2,59,55),(3,7,2),(3,8,3),(3,25,19),(3,29,23),(3,32,26),(3,35,29),(3,36,30),(3,38,32),(3,40,34),(3,45,39),(3,47,41),(3,52,48),(3,53,49),(3,55,51),(3,56,52),(3,66,62),(3,67,63),(4,42,36),(4,43,37),(4,44,38),(4,48,42),(4,54,50),(5,13,8),(5,24,18),(5,27,21),(5,30,24),(5,66,62),(6,67,64),(7,11,6),(7,12,7),(7,14,9),(8,9,4),(8,10,5),(8,15,10),(8,23,17),(8,26,20),(8,37,31),(60,61,57),(61,61,57),(62,62,58),(63,62,58),(64,63,59),(65,63,59);
/*!40000 ALTER TABLE `warranty_item_list` ENABLE KEYS */;
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
