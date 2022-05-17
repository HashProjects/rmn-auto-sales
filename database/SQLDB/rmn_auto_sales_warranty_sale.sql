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
-- Table structure for table `warranty_sale`
--

DROP TABLE IF EXISTS `warranty_sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warranty_sale` (
  `warranty_sale_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `co_signer_name` varchar(45) NOT NULL,
  `warranty_sale_date` datetime NOT NULL,
  `total_cost` double NOT NULL,
  `monthly_cost` double NOT NULL,
  `salesperson_id` int NOT NULL,
  PRIMARY KEY (`warranty_sale_id`),
  KEY `fk_salesperson_id_idx` (`salesperson_id`) /*!80000 INVISIBLE */,
  KEY `fk_warranty_sale_1_idx` (`customer_id`),
  KEY `fk_warranty_sale_2_idx` (`vehicle_id`),
  CONSTRAINT `fk_warranty_sale_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `fk_warranty_sale_2` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`vehicle_id`),
  CONSTRAINT `fk_warranty_sale_3` FOREIGN KEY (`salesperson_id`) REFERENCES `sales_people` (`salesperson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranty_sale`
--

LOCK TABLES `warranty_sale` WRITE;
/*!40000 ALTER TABLE `warranty_sale` DISABLE KEYS */;
INSERT INTO `warranty_sale` VALUES (53,1,39,'None','2022-04-30 00:00:00',1000,41.666666666666664,2),(68,161,54,'None','2022-05-04 00:00:00',1100,61.11,7),(69,162,55,'None','2022-05-04 00:00:00',2000,111.11,2),(70,162,55,'None','2022-05-04 00:00:00',2000,111.11,2),(71,162,55,'None','2022-05-04 00:00:00',2000,111.11,2),(72,162,55,'None','2022-05-04 00:00:00',2000,111.11,7),(73,162,55,'None','2022-05-04 00:00:00',2000,111.11,7),(74,163,56,'None','2022-05-13 00:00:00',1100,61.11,2);
/*!40000 ALTER TABLE `warranty_sale` ENABLE KEYS */;
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
