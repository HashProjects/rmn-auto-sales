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
-- Table structure for table `employment`
--

DROP TABLE IF EXISTS `employment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employment` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `employment_id` int NOT NULL,
  `employer` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  `supervisor` varchar(45) NOT NULL,
  `supervisor_phone` varchar(16) NOT NULL,
  `employer_address` varchar(100) NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  PRIMARY KEY (`customer_id`,`employment_id`),
  CONSTRAINT `fk_employment_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employment`
--

LOCK TABLES `employment` WRITE;
/*!40000 ALTER TABLE `employment` DISABLE KEYS */;
INSERT INTO `employment` VALUES (30,1,'Home Depot','Teacher','Biden, Joe','799-70-5229','9452 Kent Lane Fullerton, Florida 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(30,2,'Lowes','Teacher','Smith, Gavin','941-27-4504','8748 Mockingbird Lane Garden Grove, California 10000','2018-09-15 00:00:00','2029-04-15 00:00:00'),(51,1,'Home Depot','Janitor','Trump, Loan','990-90-6367','14857 Kent Blvd Newport Beach, California 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(53,1,'Josephine Crab Shack','Janitor','Smith, Gavin','762-65-8704','70083 Wayne Street Street Fountain Valley, Texas 10000','2021-04-15 00:00:00','2029-04-15 00:00:00'),(54,1,'Avery Denison','Engineers','Smith, Brandon','448-97-2803','31965 Mockingbird Road Fountain Valley, Fountain Valley 10000','2021-04-15 00:00:00','2029-04-15 00:00:00'),(55,1,'Home Depot','Manager','Bannon, Brandon','673-66-6114','20413 Martin Luther King Jr Blvd Orange, Florida 10000','2018-09-15 00:00:00','2029-04-15 00:00:00'),(56,1,'Home Depot','Engineer','Bannon, Lizet','434-45-1186','29367 Martin Luther King Jr Street Newport Beach, Nevada 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(56,2,'Lowes','Janitor','Nyugen, Kammy','192-99-4598','14157 Wayne Street Blvd Newport Beach, Fountain Valley 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(57,1,'3M','Teacher','Benden, Loan','971-13-1037','27631 Martin Luther King Jr Lane Garden Grove, Texas 10000','2021-04-15 00:00:00','2015-04-20 00:00:00'),(58,1,'Josephine Crab Shack','Teacher','Nyugen, Brandon','105-21-2329','31032 Kent Street Garden Grove, Texas 10000','2020-04-20 00:00:00','2029-04-15 00:00:00'),(59,1,'Avery Denison','Teacher','Bannon, Don','562-49-9111','73628 Wayne Street Road Fountain Valley, Florida 10000','2020-04-20 00:00:00','2015-09-15 00:00:00');
/*!40000 ALTER TABLE `employment` ENABLE KEYS */;
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
