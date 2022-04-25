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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'789-851-5134N4','Harris','Donald','33546 Mockingbird Road','Irvine','Fountain Valley',10000,'Male','13-28-1992','933-88-8319'),(2,'835-233-6883N14','Harris','Donald','53941 Martin Luther King Jr Lane','Newport Beach','Florida',10000,'Male','4-13-1970','226-31-3603'),(3,'247-852-3109','Smith','Donald','54351 Martin Luther King Jr Lane','Orange','California',10000,'Male','8-9-1972','725-23-2490'),(4,'254-194-6217','Harris','Mohit','16992 Martin Luther King Jr Road','Fullerton','Texas',10000,'Female','5-10-1998','102-21-5760'),(5,'804-842-4352','Harris','Kamala','45519 Wayne Street Street','Newport Beach','Nevada',10000,'Male','3-30-1972','538-93-1065'),(6,'234-786-8740','Trump','Loan','78082 Mockingbird Lane','Irvine','Fountain Valley',10000,'Female','3-26-1977','467-72-1014'),(7,'779-866-6385','Smith','Loan','19522 Wayne Street Lane','Irvine','Florida',10000,'Female','3-9-1994','443-20-8218'),(8,'871-482-1944','Harris','Ted','91329 Wayne Street Street','Fountain Valley','Nevada',10000,'Male','5-19-1988','495-56-5038'),(9,'432-502-6409','Nyugen','Kamala','94994 Martin Luther King Jr Street','Placentia','Texas',10000,'Female','1-8-1990','930-46-9491'),(10,'500-266-2041','Newsome','Kamala','96422 Martin Luther King Jr Lane','Orange','Fountain Valley',10000,'Female','1-24-1999','721-99-9752'),(11,'205-209-5101','Smith','Sammy','18645 Martin Luther King Jr Street','Irvine','Nevada',10000,'Female','1-23-1990','441-63-9351'),(12,'936-929-4512','Johnson','Loan','49967 Mockingbird Lane','Irvine','California',10000,'Female','7-29-1974','280-49-3866'),(13,'457-552-8813','Newsome','Loan','92748 Martin Luther King Jr Lane','Orange','Texas',10000,'Male','10-2-1987','687-78-5871'),(14,'141-299-1246','Newsome','Eric','16991 Wayne Street Road','Placentia','Fountain Valley',10000,'Male','2-31-1971','876-14-6154'),(15,'663-881-7673','Nyugen','Mohit','6699 Martin Luther King Jr Street','Irvine','Texas',10000,'Male','6-16-1987','751-43-8280'),(16,'794-113-6247','Newsome','Kamala','23028 Wayne Street Blvd','Orange','Fountain Valley',10000,'Male','6-22-1977','959-85-5222'),(17,'893-935-4678','Biden','Ted','23977 Mockingbird Lane','Fullerton','Fountain Valley',10000,'Male','8-20-1989','153-59-1326'),(18,'640-791-1007','Trump','Joe','44780 Mockingbird Blvd','Orange','California',10000,'Male','8-13-1975','690-68-7699'),(19,'919-986-1725','Nyugen','Donald','92964 Wayne Street Road','Irvine','Fountain Valley',10000,'Female','12-24-1976','163-10-8646'),(20,'301-360-7555','Biden','Mohit','14976 Mockingbird Blvd','Garden Grove','Florida',10000,'Female','3-20-1987','162-61-3664'),(21,'862-248-5781','Johnson','Ted','50423 Kent Road','Orange','Nevada',10000,'Male','13-9-1982','650-60-2619'),(22,'912-824-4340','Trump','Eric','14661 Kent Blvd','Newport Beach','Fountain Valley',10000,'Male','13-24-1981','546-11-6242'),(23,'200-956-7688','Smith','Mohit','53395 Mockingbird Road','Placentia','Nevada',10000,'Female','8-1-1981','647-86-8980'),(24,'869-613-2866','Smith','Loan','67853 Martin Luther King Jr Blvd','Garden Grove','Texas',10000,'Female','5-31-2000','960-41-9173'),(25,'983-135-3215','Nyugen','Eric','25532 Mockingbird Lane','Irvine','California',10000,'Female','6-10-1978','365-70-4227'),(26,'900-232-5623','Johnson','Mohit','79374 Mockingbird Lane','Orange','Nevada',10000,'Male','11-6-1976','768-69-1044'),(28,'875-833-5199','Trump','Kamala','99736 Mockingbird Blvd','Fullerton','Texas',10000,'Male','7-19-2000','611-21-8068'),(29,'225-257-2960','Trump','Donald','26382 Wayne Street Road','Irvine','California',10000,'Female','8-27-1986','872-74-9680'),(30,'525-695-7761','Newsome','Joe','41897 Kent Road','Orange','Florida',10000,'Female','5-5-1997','818-57-6307');
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

-- Dump completed on 2022-04-24 21:01:27
