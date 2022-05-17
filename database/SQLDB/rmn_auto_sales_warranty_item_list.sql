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
  KEY `fk_warranty_item_list_1_idx` (`warranty_id`),
  CONSTRAINT `fk_warranty_item_list_1` FOREIGN KEY (`warranty_id`) REFERENCES `warranty` (`warranty_id`),
  CONSTRAINT `fk_warranty_item_list_2` FOREIGN KEY (`item_id`) REFERENCES `warranty_item` (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranty_item_list`
--

LOCK TABLES `warranty_item_list` WRITE;
/*!40000 ALTER TABLE `warranty_item_list` DISABLE KEYS */;
INSERT INTO `warranty_item_list` VALUES (3,53,49),(3,68,65),(4,68,65),(7,68,66),(3,69,67),(4,69,68),(3,70,69),(4,70,70),(3,71,71),(4,71,72),(3,72,73),(4,72,74),(3,73,75),(4,73,76),(3,74,77),(5,74,78);
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

-- Dump completed on 2022-05-17 14:30:43
