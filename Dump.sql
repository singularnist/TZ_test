-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: new_test
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `adminuser`
--

DROP TABLE IF EXISTS `adminuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adminuser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adminuser`
--

LOCK TABLES `adminuser` WRITE;
/*!40000 ALTER TABLE `adminuser` DISABLE KEYS */;
INSERT INTO `adminuser` VALUES (1,'admin','admin'),(2,'test','test');
/*!40000 ALTER TABLE `adminuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,'Київ'),(2,'Вінниця'),(3,'Хмельницький'),(4,'Варшава'),(5,'Краків'),(6,'Вроцлав'),(7,'Берлін '),(8,'Мюнхен '),(9,'Гамбург '),(10,'Рим '),(11,'Флоренція '),(12,'Венеція ');
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `id` int NOT NULL AUTO_INCREMENT,
  `country` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'Україна'),(2,'Польща'),(3,'Німетччина'),(4,'Італія');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery`
--

DROP TABLE IF EXISTS `delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `country_id` int NOT NULL,
  `city_id` int NOT NULL,
  `street_id` int NOT NULL,
  `house` varchar(10) NOT NULL,
  `number` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `weight` decimal(10,2) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `stat` varchar(255) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `country_id` (`country_id`),
  KEY `city_id` (`city_id`),
  KEY `street_id` (`street_id`),
  CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`),
  CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`),
  CONSTRAINT `delivery_ibfk_3` FOREIGN KEY (`street_id`) REFERENCES `street` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery`
--

LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES (76,9,3,8,17,'1111','+380982630537','Улянівський','Сергій','Подушка 6','Білий',60.00,60,'виконано','2023-07-24 17:11:02'),(77,9,3,8,17,'1111','+380982630537','Улянівський','Сергій','Подушка 6','Білий',60.00,60,'Обробляється','2023-07-24 17:12:38'),(78,9,3,8,17,'1111','+380982630537','Улянівський','Сергій','Подушка 6','Білий',60.00,60,'Виконується','2023-07-24 17:16:19'),(79,9,3,8,17,'1111','+380982630537','Улянівський','Сергій','Подушка 6','Білий',60.00,60,'Обробляється','2023-07-24 17:22:40'),(80,1234,3,2,18,'98','+380982630537','Улянівський','Сергій','Подушка 5','Жовтий',50.00,50,'Виконано','2023-07-24 19:43:50'),(81,1234,3,2,18,'98','+380982630537','Улянівський','Сергій','Подушка 5','Жовтий',50.00,50,'Обробляється','2023-07-24 19:49:07'),(82,1234,3,2,18,'98','+380982630537','Улянівський','Сергій','Подушка 5','Жовтий',50.00,50,'Виконано','2023-07-24 19:49:46'),(83,1234,3,2,18,'98','+380982630537','Улянівський','Сергій','Подушка 5','Жовтий',50.00,50,'Виконується','2023-07-24 19:53:14'),(84,10000,3,2,18,'98','+380982630537','Улянівський','Сергій','Подушка 5','Жовтий',50.00,50,'Виконується','2023-07-24 19:57:13'),(85,10000,3,2,18,'98','+380982630537','Улянівський','Сергій','Подушка 5','Жовтий',50.00,50,'Обробляється','2023-07-24 19:59:21');
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `weight` decimal(10,2) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Подушка 1',10.00,'Червоний',10.00,'2023-07-06 08:17:16'),(2,'Подушка 2',20.00,'Чорний',20.00,'2023-07-06 08:17:47'),(3,'Подушка 3',30.00,'Зелений',30.00,'2023-07-06 08:18:11'),(4,'Подушка 4',40.00,'Синій',40.00,'2023-07-06 08:18:29'),(5,'Подушка 5',50.00,'Жовтий',50.00,'2023-07-06 08:18:42'),(6,'Подушка 6',60.00,'Білий',60.00,'2023-07-06 08:19:01');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `street`
--

DROP TABLE IF EXISTS `street`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `street` (
  `id` int NOT NULL AUTO_INCREMENT,
  `street` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `street`
--

LOCK TABLES `street` WRITE;
/*!40000 ALTER TABLE `street` DISABLE KEYS */;
INSERT INTO `street` VALUES (1,'Проспект Юності'),(2,'Келецька'),(3,'Космонавтів'),(4,'Зарічанська '),(5,'Проспект Миру'),(6,'Панаса Мирного'),(7,'Новий Світ'),(8,'Ударова'),(9,'Краківське Предмістя'),(10,'Ринкова площа'),(11,'Вулиця Флорянська'),(12,'Вулиця Головна'),(13,'Казимежа Великого'),(14,'Святого Мартина'),(15,'Казимирська '),(16,'Під липами'),(17,'Курфюрстендамм '),(18,'Фрідріхштрассе '),(19,'Марієнплац '),(20,'Фрезенплац '),(21,'Людвігштрассе '),(22,'Йоханнес-Брамс-Плац'),(23,'Мьо-дамм-Галлері'),(24,'Рейпербан'),(25,'Віа дель Корсо'),(26,'Плата ді Спанья'),(27,'Віа Венето'),(28,'Віа де\' Торнабоні'),(29,'Понте Веккьо '),(30,'Піацца дельла Сіґнорія'),(31,'Ріва деглі Шьявоні '),(32,'Понте Ріальто'),(33,'Піацца Сан Марко ');
/*!40000 ALTER TABLE `street` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-24 23:32:48
