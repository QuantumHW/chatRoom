-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: chat
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mid` varchar(45) DEFAULT NULL COMMENT '消息所属用户',
  `time` varchar(45) DEFAULT NULL COMMENT '消息发出的时间',
  `content` varchar(1000) DEFAULT NULL COMMENT '消息具体内容',
  PRIMARY KEY (`id`),
  KEY `FK_messages_users` (`mid`),
  CONSTRAINT `FK_messages_users` FOREIGN KEY (`mid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用于存储所有的消息记录，包含消息序号、消息所属用户、时间、类型、内容';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (8,'hw','2022-04-18 11:47:08','大家好\n'),(9,'lulu','2022-04-18 11:47:20','你好\n'),(10,'hw','2022-04-18 11:48:19','社会主义核心价值观是社会主义核心价值体系的内核，体现社会主义核心价值体系的根本性质和基本特征，反映社会主义核心价值体系的丰富内涵和实践要求，是社会主义核心价值体系的高度凝练和集中表达\n'),(11,'lulu','2022-04-18 11:48:34','党的十八大提出，倡导富强、民主、文明、和谐，倡导自由、平等、公正、法治，倡导爱国、敬业、诚信、友善，积极培育和践行社会主义核心价值观\n'),(12,'lulu','2022-04-18 11:48:42','新中国的建立，确立了以社会主义基本政治制度、基本经济制度的确立和以马克思主义为指导思想的社会主义意识形态，为社会主义核心价值体系建设奠定了政治前提、物质基础和文化条件\n'),(13,'hw','2022-04-18 11:49:05','高举中国特色社会主义伟大旗帜，以邓小平理论、“三个代表”重要思想、科学发展观为指导，深入学习贯彻党的十八大精神和习近平同志系列讲话精神，紧紧围绕坚持和发展中国特色社会主义这一主题，紧紧围绕实现中华民族伟大复兴中国梦这一目标，紧紧围绕“三个倡导”这一基本内容，注重宣传教育、示范引领、实践养成相统一，注重政策保障、制度规范、法律约束相衔接，使社会主义核心价值观融入人们生产生活和精神世界，激励全体人民为夺取中国特色社会主义新胜利而不懈奋斗。\n'),(14,'hw','2022-04-18 11:54:23','bb**'),(15,'lulu','2022-04-18 12:19:29','@robot 天津的天气如何@@天津:周一 04月18日,多云转晴 东风转西南风,最低气温12度，最高气温21度。'),(16,'hw','2022-04-18 12:37:24','@robot 达州的天气呢@@达州:周一 04月18日,阴 持续无风向,最低气温12度，最高气温21度。'),(17,'hw','2022-04-18 20:23:14','@robot 全世界最帅的人是谁@@人品好，心地善良的男人都很帅呢。');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uid_UNIQUE` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用于存储所有用户的账号及密码';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('hw','e10adc3949ba59abbe56e057f20f883e'),('hw2','e10adc3949ba59abbe56e057f20f883e'),('lulu','e10adc3949ba59abbe56e057f20f883e'),('quantumcloud','e10adc3949ba59abbe56e057f20f883e'),('test','e10adc3949ba59abbe56e057f20f883e');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-18 20:34:45
