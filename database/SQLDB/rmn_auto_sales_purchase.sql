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
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase` (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `purchase_date` datetime NOT NULL,
  `seller_id` int NOT NULL,
  `auction` tinyint NOT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `fk_seller_id_idx` (`seller_id`),
  CONSTRAINT `fk_seller_id` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (5,'2022-04-19 00:00:00',1,0),(6,'2022-04-19 00:00:00',1,0),(7,'2022-04-19 00:00:00',1,0),(8,'2022-04-19 00:00:00',1,0),(9,'2022-04-19 00:00:00',1,0),(10,'2022-04-19 00:00:00',1,0),(11,'2022-04-19 00:00:00',1,0),(12,'2022-04-19 00:00:00',1,0),(13,'2022-04-19 00:00:00',1,0),(14,'2022-04-19 00:00:00',1,0),(15,'2022-04-19 00:00:00',1,0),(16,'2022-04-19 00:00:00',1,0),(20,'2022-04-19 00:00:00',1,0),(21,'2022-04-19 00:00:00',1,0),(22,'2022-04-19 00:00:00',1,0),(23,'2022-04-19 00:00:00',1,0),(24,'2022-04-19 00:00:00',1,0),(25,'2022-04-19 00:00:00',1,0),(27,'2022-04-19 00:00:00',1,0),(28,'2022-04-19 00:00:00',1,0),(29,'2022-04-19 00:00:00',1,0),(30,'2022-04-19 00:00:00',1,0),(31,'2022-04-19 00:00:00',1,0),(32,'2022-04-19 00:00:00',1,0),(37,'2022-04-19 00:00:00',1,0),(38,'2022-04-19 00:00:00',1,0),(39,'2022-04-19 00:00:00',1,0),(43,'2022-04-28 00:00:00',1,0),(44,'2022-04-28 00:00:00',1,0),(45,'2022-04-28 00:00:00',1,0),(46,'2022-04-28 00:00:00',1,0),(47,'2022-04-28 00:00:00',1,0),(48,'2022-04-28 00:00:00',1,0),(49,'2022-04-28 00:00:00',1,0),(50,'2022-04-28 00:00:00',1,0),(51,'2022-04-28 00:00:00',1,0),(52,'2022-04-28 00:00:00',1,0),(53,'2022-04-28 00:00:00',1,0),(54,'2022-04-28 00:00:00',1,0),(55,'2022-04-29 00:00:00',1,0),(56,'2022-04-29 00:00:00',1,0),(57,'2022-04-29 00:00:00',1,0),(58,'2022-04-29 00:00:00',1,0),(59,'2022-04-29 00:00:00',1,0),(60,'2022-04-29 00:00:00',1,0),(61,'2022-04-29 00:00:00',1,0),(62,'2022-04-29 00:00:00',1,0),(63,'2022-04-29 00:00:00',1,0),(64,'2022-04-29 00:00:00',1,0),(65,'2022-04-30 00:00:00',1,0),(67,'2022-04-30 00:00:00',1,0),(68,'2022-04-19 00:00:00',1,0),(69,'2022-05-02 00:00:00',1,0),(70,'2022-05-02 00:00:00',1,0),(71,'2022-05-02 00:00:00',1,0),(72,'2022-05-02 00:00:00',1,0),(73,'2022-05-02 00:00:00',1,0),(74,'2022-05-02 00:00:00',1,0),(75,'2022-04-19 00:00:00',1,0),(76,'2022-04-19 00:00:00',1,0),(77,'2022-05-02 00:00:00',1,0),(78,'2022-05-02 00:00:00',1,0),(79,'2022-05-03 00:00:00',1,0),(80,'2022-05-03 00:00:00',1,0),(81,'2022-05-03 00:00:00',1,0),(82,'2022-05-03 00:00:00',1,0),(83,'2022-05-03 00:00:00',1,0),(84,'2022-05-03 00:00:00',1,0),(85,'2022-05-03 00:00:00',1,0),(86,'2022-05-03 00:00:00',1,0),(87,'2022-05-03 00:00:00',1,0),(88,'2022-05-03 00:00:00',3,0),(89,'2022-05-04 00:00:00',3,0),(90,'2022-05-04 00:00:00',3,0),(91,'2022-05-04 00:00:00',3,0),(92,'2022-05-13 00:00:00',3,0);
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
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
