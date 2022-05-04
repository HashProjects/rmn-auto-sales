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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employment`
--

LOCK TABLES `employment` WRITE;
/*!40000 ALTER TABLE `employment` DISABLE KEYS */;
INSERT INTO `employment` VALUES (2,1,'Home Depot','Janitor','Harris, Kamala','869-94-6737','65397 Kent Road Placentia, Nevada 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(3,2,'3M','Janitor','Nyugen, Joe','825-16-8668','76362 Kent Road Garden Grove, California 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(4,1,'Home Depot','Professor','Smith, Loan','654-72-7357','10610 Mockingbird Road Orange, California 10000','2018-09-15 00:00:00','2029-04-15 00:00:00'),(5,2,'Home Depot','Janitor','Newsome, Mohit','339-53-3259','65933 Martin Luther King Jr Blvd Placentia, Fountain Valley 10000','2020-04-20 00:00:00','2029-04-15 00:00:00'),(6,1,'Lowes','Teacher','Trump, Ted','962-99-1975','56638 Mockingbird Road Anaheim, Texas 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(7,2,'Avery Denison','Janitor','Newsome, Gavin','467-38-9686','69898 Wayne Street Blvd Orange, California 10000','2018-09-15 00:00:00','2015-09-15 00:00:00'),(8,1,'Josephine Crab Shack','Teacher','Smith, Eric','186-36-2724','68148 Wayne Street Lane Orange, Florida 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(9,2,'Avery Denison','Engineer','Nyugen, Donald','575-66-3138','8248 Mockingbird Road Anaheim, Fountain Valley 10000','2021-04-15 00:00:00','2015-04-20 00:00:00'),(10,1,'Josephine Crab Shack','Teacher','Biden, Sammy','694-96-7823','15359 Martin Luther King Jr Lane Placentia, Texas 10000','2018-09-15 00:00:00','2029-04-15 00:00:00'),(11,2,'3M','Janitor','Nyugen, Kamala','211-40-7495','15800 Kent Street Fountain Valley, Nevada 10000','2018-09-15 00:00:00','2015-09-15 00:00:00'),(12,1,'Avery Denison','Professor','Johnson, Ted','563-53-4477','49022 Mockingbird Street Irvine, Florida 10000','2018-09-15 00:00:00','2015-09-15 00:00:00'),(13,2,'Avery Denison','Teacher','Nyugen, Gavin','597-75-6144','62119 Mockingbird Blvd Newport Beach, Texas 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(14,1,'Home Depot','Professor','Harris, Joe','337-90-5684','64952 Kent Blvd Irvine, Nevada 10000','2020-04-20 00:00:00','2029-04-15 00:00:00'),(15,2,'Home Depot','Janitor','Newsome, Donald','884-35-3518','80016 Kent Lane Orange, Fountain Valley 10000','2021-04-15 00:00:00','2029-04-15 00:00:00'),(16,1,'Josephine Crab Shack','Engineer','Newsome, Ted','484-15-2115','70818 Martin Luther King Jr Blvd Irvine, Fountain Valley 10000','2020-04-20 00:00:00','2015-04-20 00:00:00'),(17,2,'Home Depot','Teacher','Nyugen, Loan','829-68-2884','41811 Kent Lane Fullerton, Florida 10000','2020-04-20 00:00:00','2029-04-15 00:00:00'),(18,1,'Avery Denison','Teacher','Newsome, Mohit','573-27-6179','77105 Martin Luther King Jr Blvd Fullerton, Nevada 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(19,2,'Lowes','Janitor','Nyugen, Loan','795-24-4539','8538 Wayne Street Street Placentia, Nevada 10000','2021-04-15 00:00:00','2015-04-20 00:00:00'),(28,1,'Josephine Crab Shack','Janitor','Biden, Gavin','241-88-2699','57258 Mockingbird Road Orange, Texas 10000','2021-04-15 00:00:00','2015-04-20 00:00:00'),(28,2,'Avery Denison','Engineer','Newsome, Mohit','343-59-4413','16993 Wayne Street Blvd Fountain Valley, Florida 10000','2021-04-15 00:00:00','2015-04-20 00:00:00'),(29,1,'Lowes','Engineer','Biden, Eric','831-15-6016','66617 Wayne Street Street Orange, California 10000','2018-09-15 00:00:00','2015-09-15 00:00:00'),(29,2,'Josephine Crab Shack','Engineer','Trump, Eric','137-61-1459','48078 Martin Luther King Jr Blvd Fullerton, Texas 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(30,1,'Home Depot','Teacher','Biden, Joe','799-70-5229','9452 Kent Lane Fullerton, Florida 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(30,2,'Lowes','Teacher','Smith, Gavin','941-27-4504','8748 Mockingbird Lane Garden Grove, California 10000','2018-09-15 00:00:00','2029-04-15 00:00:00'),(32,1,'Lowes','Janitor','Nyugen, Ted','935-90-4988','72014 Mockingbird Street Irvine, Florida 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(33,1,'Josephine Crab Shack','Professor','Smith, Kamala','781-62-6358','77952 Mockingbird Street Fountain Valley, Texas 10000','2020-04-20 00:00:00','2015-04-20 00:00:00'),(35,1,'Josephine Crab Shack','Professor','Harris, Eric','931-24-3696','79492 Kent Street Newport Beach, Nevada 10000','2018-09-15 00:00:00','2015-09-15 00:00:00'),(36,1,'Lowes','Teacher','Nyugen, Ted','555-56-6944','77628 Kent Street Orange, Nevada 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(37,1,'Home Depot','Professor','Harris, Eric','774-20-6466','4483 Mockingbird Lane Newport Beach, Texas 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(38,1,'Josephine Crab Shack','Janitor','Newsome, Kamala','851-57-2700','26461 Martin Luther King Jr Lane Placentia, California 10000','2018-09-15 00:00:00','2029-04-15 00:00:00'),(39,1,'Lowes','Teacher','Biden, Donald','232-60-9723','47052 Kent Street Newport Beach, California 10000','2020-04-20 00:00:00','2015-04-20 00:00:00'),(40,1,'Lowes','Teacher','Biden, Donald','232-60-9723','47052 Kent Street Newport Beach, California 10000','2020-04-20 00:00:00','2015-04-20 00:00:00'),(41,1,'Josephine Crab Shack','Engineer','Johnson, Gavin','560-68-3573','43639 Kent Blvd Fullerton, California 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(42,1,'3M','Professor','Newsome, Joe','183-97-4696','64887 Mockingbird Street Anaheim, Nevada 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(43,1,'Lowes','Teacher','Johnson, Gavin','486-10-6972','53141 Martin Luther King Jr Street Fullerton, Texas 10000','2021-04-15 00:00:00','2015-04-20 00:00:00'),(43,2,'Josephine Crab Shack','Janitor','Trump, Mohit','384-76-7232','73845 Martin Luther King Jr Lane Fullerton, Texas 10000','2021-04-15 00:00:00','2029-04-15 00:00:00'),(44,1,'Avery Denison','Janitor','Harris, Donald','428-76-2263','5056 Kent Blvd Fullerton, Nevada 10000','2020-04-20 00:00:00','2029-04-15 00:00:00'),(44,2,'Home Depot','Professor','Newsome, Sammy','621-36-3344','4472 Wayne Street Road Fullerton, Texas 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(46,1,'3M','Professor','Johnson, Sammy','964-76-2467','88987 Martin Luther King Jr Blvd Orange, Nevada 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(47,1,'Avery Denison','Janitor','Harris, Ted','289-23-4762','7236 Mockingbird Road Fullerton, Nevada 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(48,1,'Josephine Crab Shack','Engineer','Johnson, Sammy','512-73-6113','10657 Mockingbird Street Irvine, Texas 10000','2020-04-20 00:00:00','2015-04-20 00:00:00'),(48,2,'3M','Engineer','Newsome, Lizet','439-44-4748','1690 Wayne Street Road Fountain Valley, California 10000','2020-04-20 00:00:00','2029-04-15 00:00:00'),(49,1,'3M','Engineer','Harris, Mohit','637-82-7240','35932 Wayne Street Street Garden Grove, Florida 10000','2021-04-15 00:00:00','2029-04-15 00:00:00'),(50,1,'Lowes','Engineer','Nyugen, Loan','674-23-6973','85261 Martin Luther King Jr Road Placentia, Nevada 10000','2021-04-15 00:00:00','2015-09-15 00:00:00'),(50,2,'Home Depot','Janitor','Newsome, Loan','229-25-9109','68919 Mockingbird Lane Fountain Valley, Nevada 10000','2020-04-20 00:00:00','2015-04-20 00:00:00'),(51,1,'Home Depot','Janitor','Trump, Loan','990-90-6367','14857 Kent Blvd Newport Beach, California 10000','2020-04-20 00:00:00','2015-09-15 00:00:00'),(52,1,'Lowes','Teacher','Smith, Mohit','636-95-7288','48569 Martin Luther King Jr Street Fountain Valley, Florida 10000','2018-09-15 00:00:00','2015-04-20 00:00:00'),(53,1,'Josephine Crab Shack','Janitor','Smith, Gavin','762-65-8704','70083 Wayne Street Street Fountain Valley, Texas 10000','2021-04-15 00:00:00','2029-04-15 00:00:00');
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

-- Dump completed on 2022-05-04  9:28:18
