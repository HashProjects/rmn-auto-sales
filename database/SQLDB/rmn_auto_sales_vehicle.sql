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
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `vehicle_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_vin` varchar(17) NOT NULL,
  `vehicle_make` varchar(45) NOT NULL,
  `vehicle_model` varchar(45) NOT NULL,
  `vehicle_year` varchar(45) NOT NULL,
  `vehicle_color` varchar(45) NOT NULL,
  `vehicle_miles` double NOT NULL,
  `vehicle_condition` varchar(45) NOT NULL,
  `vehicle_style` varchar(45) NOT NULL,
  `vehicle_interior_color` varchar(45) NOT NULL,
  `vehicle_list_price` double NOT NULL,
  `vehicle_sale_price` double NOT NULL,
  `vehicle_sold` tinyint(1) NOT NULL DEFAULT '0',
  `vehicle_repaired` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'2323423234','Lexus','Ct200h','2016','Silver',33882,'Excellent','Hatchback','Black',8000,8999,1,0),(2,'973249872333','Honda','Accord','2015','Black',85000,'Good','Sedan','Brown',7000,8000,1,0),(3,'348923978','Chevy','Astro','2000','Maroon',200200,'Fair','Van','Black',2000,2500,1,0),(13,'39974628N21','Ford','Car','2011','Red',10000,'Fair','Coupe','9800',8100,0,0,0),(14,'157540514N12','Infinity','Car','2017','Red',10000,'Excellent','Truck','8900',7600,0,0,0),(15,'107948906N24','Toyota','Car','2019','Red',10000,'Excellent','Sedan','7100',5500,0,0,0),(16,'141811345N28','Toyota','Car','2018','Red',10000,'Fair','Van','10000',10200,0,0,0),(17,'27339171N24','Toyota','Car','2012','Red',10000,'Excellent','Van','7300',8900,0,1,0),(18,'124960196N14','Toyota','Car','2018','Red',10000,'Excellent','Coupe','8300',10500,0,0,0),(19,'23727033N24','Infinity','Car','2015','Red',10000,'Fair','Van','5600',6300,0,1,0),(20,'4686972N19','GCM','Car','2021','Red',10000,'Good','Truck','4900',5800,0,0,0),(21,'68837661N21','Ford','Car','2014','Red',10000,'Fair','Van','5300',6700,0,0,0),(22,'167615233N21','Infinity','Car','2020','Red',10000,'Good','Coupe','4900',7700,0,0,0),(23,'174136733N16','Infinity','Car','2011','Red',10000,'Excellent','Sedan','5900',7000,0,0,0),(24,'92891912N0','Infinity','Car','2017','Red',10000,'Fair','Coupe','4400',9700,0,0,0),(25,'17221351N23','Toyota','Car','2016','Red',10000,'Good','Coupe','7600',7200,0,0,0),(26,'149849330N30','Toyota','Car','2016','Red',10000,'Fair','Sedan','4000',7200,0,0,0),(27,'137180661N29','Toyota','Car','2014','Red',10000,'Fair','Coupe','4200',8500,0,0,0),(30,'3719296N28','Ford','Car','2020','Black',10000,'Fair','Van','4600',8000,0,1,0),(31,'128022334N25','GMC','Car','2018','Blue',10000,'Excellent','Sedan','6400',8800,0,0,0),(32,'31319914N16','Ford','Car','2018','Black',10000,'Excellent','Sedan','9200',6000,0,0,0),(33,'135465738N27','Chevy','Car','2017','Red',10000,'Excellent','Sedan','8900',10700,0,0,0),(34,'140094370N18','GMC','Car','2015','Red',10000,'Excellent','Truck','9800',9000,0,0,0),(35,'137103065N8','Toyota','Car','2011','Silver',10000,'Fair','Truck','9000',9300,0,0,0),(36,'114943814N26','Chevy','Car','2019','Blue',10000,'Good','Coupe','4800',6600,0,0,0),(37,'160208732N19','Toyota','Car','2019','Blue',10000,'Fair','Van','6100',10300,0,0,0),(38,'44278207N25','Honda','Car','2015','Silver',10000,'Fair','Sedan','7100',5800,0,0,0),(39,'713354N22','Toyota','Car','2011','Blue',10000,'Good','Truck','6000',6200,0,1,0),(40,'29694983N20','Infinity','Car','2018','Blue',10000,'Good','Truck','4500',6500,0,1,0),(41,'60346730N29','GMC','Car','2021','Silver',10000,'Fair','Coupe','4400',6400,0,0,0),(42,'42265315N17','Toyota','Car','2012','Blue',10000,'Fair','Truck','7800',10300,0,1,0),(43,'33854470N3','GMC','Car','2011','Blue',10000,'Fair','Coupe','9600',9200,0,0,0),(44,'131848325N10','Honda','Car','2015','Silver',10000,'Excellent','Van','4000',8100,0,0,0),(45,'31941114N18','GMC','Car','2017','Red',10000,'Good','Truck','6300',6900,0,1,0),(46,'85843377N2','Chevy','Car','2014','Silver',10000,'Excellent','Truck','5000',8400,0,0,0),(47,'153800678N12','GMC','Car','2014','Red',10000,'Fair','Sedan','7800',9800,0,0,0),(48,'79930124N28','Honda','Car','2018','Blue',10000,'Excellent','Truck','9900',8200,0,1,0),(49,'85005275N17','Ford','Car','2017','White',10000,'Fair','Coupe','9700',5200,0,0,0),(50,'158439168N13','Honda','Car','2017','Blue',10000,'Good','Coupe','9400',6900,0,0,0),(51,'33375556N5','Infinity','Car','2015','Blue',10000,'Good','Van','9900',6500,0,0,0),(52,'45361614N4','GMC','Car','2010','Blue',10000,'Good','Van','7400',6300,0,0,0),(53,'127809556N22','Ford','Car','2020','Black',10000,'Excellent','Sedan','5800',6800,0,0,0),(57,'144277238N8','Ford','Car','2017','White',10000,'Good','Truck','9500',5400,0,0,0),(58,'123538491N9','GMC','Car','2020','White',10000,'Excellent','Van','6900',6900,0,1,0),(59,'70495457N10','GMC','Car','2022','Silver',10000,'Good','Sedan','4300',9400,0,0,0),(60,'22917785N27','Honda','Car','2022','Red',10000,'Good','Sedan','5400',8700,0,0,0),(61,'91266180N20','Chevy','Car','2014','Blue',10000,'Fair','Van','7900',7900,0,0,0),(62,'46296175N2','Ford','Car','2016','Red',10000,'Fair','Truck','7400',5800,0,0,0),(63,'19106140N29','Infinity','Car','2010','Black',10000,'Fair','Sedan','7300',8500,0,1,0),(64,'175119133N25','Toyota','Car','2011','Red',10000,'Fair','Coupe','8300',6100,0,0,0),(65,'17612253N6','Toyota','Car','2022','Silver',10000,'Excellent','Sedan','9200',8600,0,0,0),(66,'95085011N3','GMC','Car','2018','White',10000,'Excellent','Van','6600',9500,0,0,0),(67,'71999429N1','Toyota','Car','2013','Red',10000,'Excellent','Van','6500',7900,0,0,0),(68,'4248325N0','GMC','Car','2022','Blue',10000,'Excellent','Coupe','5800',7000,0,0,0),(70,'130535741N30','GMC','Car','2018','White',10000,'Good','Coupe','8500',6300,0,0,0),(71,'115861074N17','Ford','Car','2016','Blue',10000,'Fair','Van','8300',7000,0,0,0),(72,'76694011N17','Toyota','Car','2013','Silver',10000,'Good','Van','9400',9400,0,0,0),(73,'173014693N18','GMC','Car','2010','White',10000,'Good','Van','7800',6400,0,0,0),(74,'14775838N11','Chevy','Car','2011','Blue',10000,'Excellent','Truck','7400',10000,0,0,0),(75,'129891539N20','Toyota','Car','2012','Silver',10000,'Good','Coupe','9400',9600,0,1,0),(76,'123237785N0','Honda','Car','2010','Red',10000,'Fair','Truck','8500',9600,0,0,0),(77,'148154718N18','Ford','Car','2017','Blue',10000,'Excellent','Van','5800',10600,0,0,0),(78,'911873N6','Honda','Car','2019','Silver',10000,'Fair','Truck','7000',5800,0,0,0),(79,'31575701N5','Ford','Car','2015','Blue',10000,'Excellent','Truck','8400',5400,0,1,0),(80,'167306995N4','Chevy','Car','2015','Blue',10000,'Good','Truck','5200',6500,0,0,0),(81,'75265382N26','Honda','Car','2020','Red',10000,'Excellent','Coupe','6400',8900,0,0,0),(82,'118074005N8','Ford','Car','2015','Red',10000,'Excellent','Coupe','7500',7800,0,1,1),(83,'147215274N6','Toyota','Car','2016','Red',10000,'Excellent','Truck','6200',10400,0,1,1),(84,'53011816N25','GCM','Car','2014','Red',10000,'Excellent','Sedan','6100',8500,0,1,1),(85,'35693523N22','Toyota','Car','2017','Red',10000,'Fair','Sedan','4000',9300,0,1,1),(86,'67813035N22','Toyota','Car','2022','Red',10000,'Good','Coupe','4100',7200,0,1,1),(87,'110072684N7','Toyota','Car','2010','Red',10000,'Good','Coupe','7900',8800,0,1,1),(88,'82874430N21','GCM','Car','2017','Red',10000,'Good','Coupe','6700',8900,0,1,1),(89,'108110809N6','GCM','Car','2013','Red',10000,'Fair','Sedan','4300',6500,0,1,1),(90,'73885750N24','Infinity','Car','2016','Red',10000,'Good','Truck','8400',6400,0,1,1),(91,'135734126N27','Toyota','Corolla','2015','White',10000,'Excellent','Sedan','8300',6100,9100,0,0),(92,'32177049N14','Lexus','LX','2010','Silver',10000,'Good','Coupe','9000',8600,8800,0,0),(93,'78777941N30','Toyota','Yaris','2019','Silver',10000,'Good','Truck','7900',9600,7700,0,0),(94,'119583065N28','Toyota','Camry','2019','Silver',10000,'Excellent','Coupe','7500',10400,9700,0,0),(95,'64435077N14','Honda','Civic','2014','Blue',10000,'Good','Truck','7600',5600,8200,0,0),(96,'21620747N2','Toyota','Sienna','2016','Red',10000,'Good','Truck','5700',8600,7600,0,0),(99,'10356749N26','Toyota','Corolla','2010','Silver',10000,'Good','Van','6100',5900,5200,0,0),(100,'87365024N23','Lexus','LX','2013','Black',10000,'Excellent','Van','5800',7500,8700,0,0),(101,'84091172N27','Lexus','Ct200h','2019','White',10000,'Excellent','Truck','7300',9300,6300,0,0),(102,'137470617N6','Toyota','Camry','2011','Silver',10000,'Excellent','Van','4900',9700,7600,0,0),(103,'17676416N2','Toyota','Tacoma','2012','Silver',10000,'Excellent','Coupe','6300',7400,6200,0,0),(104,'84409614N24','Toyota','Sienna','2021','Silver',10000,'Excellent','Coupe','6100',6000,9600,0,0),(105,'11166668N26','Honda','Accord','2018','Red',10000,'Fair','Van','8400',5700,6500,0,0),(106,'159570163N6','Toyota','Tacoma','2022','Blue',10000,'Excellent','Truck','7400',8800,5600,0,0),(107,'30186690N28','Honda','CR-V','2017','White',10000,'Fair','Truck','5300',9900,10900,0,0),(108,'10960403N16','Honda','Accord','2022','Silver',10000,'Good','Coupe','7400',11000,7200,0,0),(109,'107287867N17','Toyota','Camry','2017','Black',10000,'Good','Sedan','6400',5100,10800,0,0),(110,'107287867N17','Toyota','Camry','2017','Black',10000,'Good','Sedan','6400',5100,10800,0,0),(111,'143331912N19','Toyota','Yaris','2018','White',10000,'Excellent','Coupe','4800',9100,9500,0,0),(112,'37538335N2','Lexus','Ct200h','2018','White',10000,'Fair','Coupe','4400',6800,5000,0,0),(113,'112272253N29','Toyota','Corolla','2012','White',10000,'Fair','Van','4900',8100,11000,0,0),(114,'61816444N14','Toyota','Camry','2016','Red',10000,'Excellent','Van','5700',10400,6300,0,0),(115,'119780626N27','Toyota','Venza','2021','White',10000,'Good','Van','6100',10700,6000,0,0),(116,'97710594N13','Honda','Accord','2015','Black',10000,'Excellent','Sedan','9500',5100,10400,0,0),(117,'58590630N27','Honda','Civic','2015','Black',10000,'Excellent','Van','4000',8000,5400,0,0),(118,'58590630N27','Honda','Civic','2015','Black',10000,'Excellent','Van','4000',8000,5400,0,0),(119,'125375364N16','Honda','HR-V','2013','White',10000,'Excellent','Van','6300',7400,6600,0,0),(120,'13208947N2','Lexus','LX','2017','Black',10000,'Good','Truck','9200',9000,5500,0,0),(121,'47075569N22','Toyota','RAV4','2017','Silver',10000,'Fair','Truck','9700',7400,5700,0,0),(122,'39271225N0','Toyota','RAV4','2011','Red',10000,'Good','Van','5100',9600,6400,1,1),(123,'71393114N25','GCM','Car','2021','Red',10000,'Excellent','Sedan','5300',9400,0,1,1),(124,'1781616N14','Ford','Car','2022','Red',10000,'Fair','Truck','6800',10900,0,1,1),(125,'105286481N8','Toyota','Corolla','2011','White',10000,'Good','Sedan','10000',6600,10300,1,1),(126,'85152405N0','Toyota','Yaris','2019','Black',10000,'Fair','Sedan','9600',7600,10700,0,0),(129,'46520793N28','Honda','Civic','2013','Blue',10000,'Excellent','Van','7100',6900,7400,0,0),(130,'31400336N2','Honda','CR-V','2020','White',10000,'Excellent','Truck','5500',10300,11000,1,1),(131,'96659206N10','Toyota','Camry','2016','Blue',10000,'Excellent','Sedan','5400',7800,10200,1,1),(132,'93349382N26','Infinity','Car','2012','Red',10000,'Good','Truck','8300',5500,0,1,1),(133,'49077677N4','Honda','HR-V','2021','Red',10000,'Excellent','Van','4300',10300,7800,1,1),(134,'68396360N6','Lexus','LX','2014','Black',10000,'Excellent','Coupe','9500',7300,5900,1,1),(135,'8840386N15','Toyota','Venza','2018','Silver',10000,'Excellent','Coupe','5300',7700,9600,0,0),(136,'137676218N28','Honda','Accord','2014','Black',10000,'Excellent','Van','Brown',8300,7800,0,0),(137,'174972483N24','Honda','Civic','2022','Blue',10000,'Fair','Van','Black',7100,5600,0,1),(138,'1511577N2','Chevy','Blazer','2010','Silver',10000,'Excellent','Sedan','Gray',6700,9100,0,0),(139,'1511577N2','Chevy','Blazer','2010','Silver',10000,'Excellent','Sedan','Gray',6700,9100,1,1),(140,'147181559N28','Lexus','LX','2019','Silver',10000,'Excellent','Van','Gray',6000,9900,1,1),(141,'100798723N12','Ford','Mustang','2015','Blue',10000,'Good','Truck','Brown',4600,8600,1,1),(142,'52984369N14','Toyota','RAV4','2019','Blue',10000,'Good','Truck','Black',9800,10400,0,0),(143,'159366764N23','Honda','Accord','2017','Red',10000,'Excellent','Sedan','Brown',5700,8600,1,0),(144,'1814106N11','Infinity','Q30','2012','Black',10000,'Fair','Coupe','Gray',10000,6200,1,0),(145,'77637172N0','Honda','CR-V','2014','Red',10000,'Good','Sedan','Gray',6300,10000,1,0),(146,'121231388N7','Lexus','Ct200h','2011','Blue',10000,'Good','Van','Brown',4900,5100,1,0),(147,'22772727N24','Honda','Civic','2021','Silver',10000,'Good','Van','Black',4800,10600,0,0),(148,'61739987N3','Lexus','LX','2021','White',10000,'Fair','Van','Black',8200,7200,0,0);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
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
