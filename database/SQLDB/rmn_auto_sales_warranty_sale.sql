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
  PRIMARY KEY (`warranty_sale_id`,`vehicle_id`,`customer_id`,`salesperson_id`),
  KEY `fk_salesperson_id_idx` (`salesperson_id`) /*!80000 INVISIBLE */,
  KEY `fk_warranty_sale_1_idx` (`customer_id`),
  KEY `fk_warranty_sale_2_idx` (`vehicle_id`),
  CONSTRAINT `fk_warranty_sale_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `fk_warranty_sale_2` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`vehicle_id`),
  CONSTRAINT `fk_warranty_sale_3` FOREIGN KEY (`salesperson_id`) REFERENCES `sales_people` (`salesperson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranty_sale`
--

LOCK TABLES `warranty_sale` WRITE;
/*!40000 ALTER TABLE `warranty_sale` DISABLE KEYS */;
INSERT INTO `warranty_sale` VALUES (1,21,3,'None','2022-04-22 00:00:00',1000,100,2),(2,67,19,'None','2022-04-22 00:00:00',1000,100,3),(3,32,16,'None','2022-04-22 00:00:00',1000,100,3),(4,17,22,'None','2022-04-22 00:00:00',1000,100,7),(7,1,28,'None','2022-04-22 00:00:00',1000,100,6),(8,33,6,'None','2022-04-22 00:00:00',1000,100,2),(9,71,19,'None','2022-04-22 00:00:00',1000,100,2),(10,16,20,'None','2022-04-22 00:00:00',1000,100,4),(11,49,24,'None','2022-04-22 00:00:00',1000,100,6),(12,71,6,'None','2022-04-22 00:00:00',1000,100,5),(13,62,3,'None','2022-04-22 00:00:00',1000,100,5),(14,38,18,'None','2022-04-22 00:00:00',1000,100,7),(15,57,21,'None','2022-04-22 00:00:00',1000,100,3),(17,1,36,'','2022-04-29 00:00:00',0,0,3),(18,1,40,'','2022-04-29 00:00:00',0,0,4),(23,109,3,'None','2022-04-22 00:00:00',1000,100,4),(24,13,8,'None','2022-04-22 00:00:00',1000,100,7),(25,109,2,'None','2022-04-22 00:00:00',1000,100,4),(26,14,19,'None','2022-04-22 00:00:00',1000,100,6),(27,121,38,'None','2022-04-22 00:00:00',1000,100,6),(29,1,39,'','2022-04-29 00:00:00',0,0,3),(30,2,35,'','2022-04-29 00:00:00',0,0,3),(32,1,40,'','2022-04-29 00:00:00',0,0,3),(35,1,40,'','2022-04-29 00:00:00',0,0,4),(36,1,39,'','2022-04-29 00:00:00',0,0,4),(37,1,40,'','2022-04-29 00:00:00',0,0,3),(38,1,40,'','2022-04-29 00:00:00',0,0,4),(40,1,36,'','2022-04-29 00:00:00',0,0,2),(42,1,36,'','2022-04-29 00:00:00',0,0,2),(43,1,39,'','2022-04-29 00:00:00',0,0,3),(44,1,36,'','2022-04-29 00:00:00',0,0,2),(45,1,36,'','2022-04-29 00:00:00',0,0,3),(46,1,36,'','2022-04-29 00:00:00',0,0,2),(47,1,36,'','2022-04-29 00:00:00',0,0,2),(48,1,39,'None','2022-04-30 00:00:00',0,0,2),(49,1,39,'None','2022-04-30 00:00:00',1000,41.666666666666664,3),(52,1,39,'None','2022-04-30 00:00:00',1000,41.666666666666664,4),(53,1,39,'None','2022-04-30 00:00:00',1000,41.666666666666664,2),(54,1,36,'None','2022-05-01 00:00:00',1000,41.666666666666664,3),(55,141,48,'None','2022-05-02 00:00:00',1000,41.67,3),(56,133,50,'None','2022-05-02 00:00:00',1000,41.67,3),(59,134,51,'None','2022-05-02 00:00:00',1000,41.67,3),(61,134,51,'None','2022-05-02 00:00:00',1000,41.67,5),(62,134,51,'None','2022-05-02 00:00:00',1000,41.67,2),(63,134,51,'None','2022-05-02 00:00:00',1000,41.67,3),(66,134,51,'None','2022-05-02 00:00:00',1000,41.67,2);
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

-- Dump completed on 2022-05-02 17:31:54
