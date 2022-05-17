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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_phone` varchar(45) NOT NULL,
  `customer_last_name` varchar(45) NOT NULL,
  `customer_first_name` varchar(45) NOT NULL,
  `customer_address` varchar(45) NOT NULL,
  `customer_city` varchar(45) NOT NULL,
  `customer_state` varchar(45) NOT NULL,
  `customer_zip` int NOT NULL,
  `customer_gender` varchar(10) NOT NULL,
  `customer_dob` varchar(45) NOT NULL,
  `customer_taxpayer_id` varchar(45) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (2,'835-233-6883N14','Harris','Donald','53941 Martin Luther King Jr Lane','Newport Beach','Florida',10000,'Male','4-13-1970','226-31-3603'),(30,'525-695-7761','Newsome','Joe','41897 Kent Road','Orange','Florida',10000,'Female','5-5-1997','818-57-6307'),(39,'835-233-6883N14','Harris','Donald','53941 Martin Luther King Jr Lane','Newport Beach','Florida',10000,'Male','4-13-1970','226-31-3603'),(45,'479-256-3327','Harris','Sammy','71214 Mockingbird Street','Orange','Fountain Valley',10000,'Male','10-19-1996','521-25-4933'),(51,'952-953-5083','Johnson','Ted','72426 Wayne Street Road','Orange','Fountain Valley',10000,'Male','5-30-1989','814-13-4661'),(53,'980-118-6439','Nyugen','Fredrick','30373 Martin Luther King Jr Street','Garden Grove','Florida',10000,'Male','5-24-1983','827-25-3237'),(54,'102-631-1498','Holden','James','33406 Kent Street','Garden Grove','California',10000,'Female','11-24-2000','453-17-3259'),(55,'781-299-5377','Burton','Amos','10439 Kent Lane','Fountain Valley','California',10000,'Male','6-14-1987','770-59-2611'),(56,'357-634-5083','Bush','Gavin','92705 Kent Blvd','Garden Grove','Nevada',10000,'Male','10-18-1985','843-37-1050'),(57,'334-983-5840','Newsome','Mohit','2595 Wayne Street Lane','Fullerton','California',10000,'Male','4-16-1992','925-11-9527'),(58,'263-794-8267','Nyugen','Donald','31030 Wayne Street Blvd','Garden Grove','Nevada',10000,'Male','3-18-1984','216-45-9772'),(59,'118-470-2226','Biden','Eric','3494 Wayne Street Blvd','Irvine','Fountain Valley',10000,'Female','11-26-1971','130-84-6544');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
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
