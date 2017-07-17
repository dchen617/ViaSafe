-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: ViaSafe
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.19-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `locationid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `longitude` decimal(12,8) DEFAULT NULL,
  `latitude` decimal(12,8) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `cityid` int(11) NOT NULL,
  `countryid` int(11) NOT NULL,
  `stateid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`locationid`),
  KEY `locations_cityid_0d35d963_fk_cities_cityid` (`cityid`),
  KEY `locations_countryid_288b16ed_fk_countries_countryid` (`countryid`),
  KEY `locations_stateid_3f60ae8f_fk_states_stateid` (`stateid`),
  KEY `locations_userid_d92420e4_fk_users_userid` (`userid`),
  CONSTRAINT `locations_cityid_0d35d963_fk_cities_cityid` FOREIGN KEY (`cityid`) REFERENCES `cities` (`cityid`),
  CONSTRAINT `locations_countryid_288b16ed_fk_countries_countryid` FOREIGN KEY (`countryid`) REFERENCES `countries` (`countryid`),
  CONSTRAINT `locations_stateid_3f60ae8f_fk_states_stateid` FOREIGN KEY (`stateid`) REFERENCES `states` (`stateid`),
  CONSTRAINT `locations_userid_d92420e4_fk_users_userid` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (3,'Murder in Dallas','Hi',32.77000000,96.79000000,NULL,2,3,3,1),(4,'Murder in Houston','Hi2',32.76000000,96.79600000,NULL,2,3,3,1),(5,'Stabbing in Downtown Houston','Unlucky guy',29.76000000,95.37000000,NULL,3,3,3,1),(6,'Stabbing on 3rd','http://www.nbcsandiego.com/news/national-international/Cosmo-DiNardo-Sean-Kratz-Bucks-County-Missing-Men-Pennsylvania-Murder-Charges-Bensalem-Philadelphia-Solebury-Township-434695573.html',-117.12040090,32.72013890,'3415 Beech St, San Diego, CA 92102, USA',11,3,6,1),(7,'Robbery by the Harbor','8pm',-117.11149640,32.66332090,'1930-1998 Cleveland Ave, National City, CA 91950, USA',12,8,10,1),(8,'Car Window smashed','Late last night someone smashed the window of a car parked in the Viasat parking lot',-117.27053200,33.12825420,'2505-2509 Palomar Airport Rd, Carlsbad, CA 92011, USA',10,7,9,1),(9,'My bag was stolen','I accidentally left my car unlocked and someone went into it last night. Lock your cars people!',-117.27122790,33.12285420,'2200-2234 Corte De La Pina, Carlsbad, CA 92011, USA',10,7,9,1),(10,'Black Van Terrorizing the Street','Reckless driver usually on weekends around 5pm just cruises around',-117.25869110,33.12556700,'2601 Town Garden Rd, Carlsbad, CA 92009, USA',6,3,6,1),(11,'Avoid the park at night','There are groups of teenagers wondering around at night during the weekdays.',-117.26698940,33.12676900,'6155 El Camino Real, Carlsbad, CA 92009, USA',8,6,8,1),(12,'Car ran a red light','8pm',-117.25079530,33.12702630,'6241 El Fuerte St, Carlsbad, CA 92009, USA',6,3,6,1),(13,'Dangerous place','stay away',-117.25247670,33.12340300,'6324-6328 Montecito Dr, Carlsbad, CA 92009, USA',6,3,6,1);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-17  9:23:30
