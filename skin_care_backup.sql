-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: skin_care
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add Token',8,'add_tokenproxy'),(30,'Can change Token',8,'change_tokenproxy'),(31,'Can delete Token',8,'delete_tokenproxy'),(32,'Can view Token',8,'view_tokenproxy'),(33,'Can add product',9,'add_product'),(34,'Can change product',9,'change_product'),(35,'Can delete product',9,'delete_product'),(36,'Can view product',9,'view_product'),(37,'Can add category',10,'add_category'),(38,'Can change category',10,'change_category'),(39,'Can delete category',10,'delete_category'),(40,'Can view category',10,'view_category'),(41,'Can add quiz',11,'add_quiz'),(42,'Can change quiz',11,'change_quiz'),(43,'Can delete quiz',11,'delete_quiz'),(44,'Can view quiz',11,'view_quiz'),(45,'Can add comments',12,'add_comments'),(46,'Can change comments',12,'change_comments'),(47,'Can delete comments',12,'delete_comments'),(48,'Can view comments',12,'view_comments'),(49,'Can add cart item',13,'add_cartitem'),(50,'Can change cart item',13,'change_cartitem'),(51,'Can delete cart item',13,'delete_cartitem'),(52,'Can view cart item',13,'view_cartitem'),(53,'Can add cart',14,'add_cart'),(54,'Can change cart',14,'change_cart'),(55,'Can delete cart',14,'delete_cart'),(56,'Can view cart',14,'view_cart'),(57,'Can add ratings',15,'add_ratings'),(58,'Can change ratings',15,'change_ratings'),(59,'Can delete ratings',15,'delete_ratings'),(60,'Can view ratings',15,'view_ratings'),(61,'Can add routine',16,'add_routine'),(62,'Can change routine',16,'change_routine'),(63,'Can delete routine',16,'delete_routine'),(64,'Can view routine',16,'view_routine'),(65,'Can add browsing hisrory',17,'add_browsinghisrory'),(66,'Can change browsing hisrory',17,'change_browsinghisrory'),(67,'Can delete browsing hisrory',17,'delete_browsinghisrory'),(68,'Can view browsing hisrory',17,'view_browsinghisrory'),(69,'Can add browsing history',18,'add_browsinghistory'),(70,'Can change browsing history',18,'change_browsinghistory'),(71,'Can delete browsing history',18,'delete_browsinghistory'),(72,'Can view browsing history',18,'view_browsinghistory');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('d9023dff6393731df7e4795c75a63e36a64b189c','2025-07-22 07:32:52.033828',3);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `browsing_history_browsinghistory`
--

DROP TABLE IF EXISTS `browsing_history_browsinghistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `browsing_history_browsinghistory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `interaction_type` varchar(20) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `browsing_history_bro_product_id_84e52838_fk_products_` (`product_id`),
  KEY `browsing_history_bro_user_id_5fa8bc63_fk_users_cus` (`user_id`),
  CONSTRAINT `browsing_history_bro_product_id_84e52838_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `browsing_history_bro_user_id_5fa8bc63_fk_users_cus` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browsing_history_browsinghistory`
--

LOCK TABLES `browsing_history_browsinghistory` WRITE;
/*!40000 ALTER TABLE `browsing_history_browsinghistory` DISABLE KEYS */;
INSERT INTO `browsing_history_browsinghistory` VALUES (127,'view','2025-09-08 23:52:44.269310',1,1),(128,'view','2025-09-08 23:53:09.296763',1,1),(129,'view','2025-09-08 23:59:31.278674',5,1),(130,'view','2025-09-08 23:59:54.813835',16,1),(131,'view','2025-09-09 00:00:05.886678',1,1),(132,'view','2025-09-09 00:02:51.059501',17,1),(133,'cart','2025-09-09 00:03:00.872670',17,1),(134,'view','2025-09-09 00:03:13.939294',17,1),(135,'rating','2025-09-09 00:03:15.822565',17,1),(136,'view','2025-09-09 00:03:47.887469',17,1),(137,'view','2025-09-09 00:11:26.764765',14,1),(138,'view','2025-09-09 00:28:27.777210',4,1),(139,'view','2025-09-09 00:28:28.514104',4,1),(140,'view','2025-09-09 00:32:46.370055',15,1),(141,'view','2025-09-09 00:33:34.554047',14,1),(142,'view','2025-09-09 00:33:58.184913',14,1),(143,'view','2025-09-09 00:38:21.216351',14,1),(144,'view','2025-09-09 00:42:22.315734',1,1),(145,'view','2025-09-09 00:42:50.933893',14,1),(146,'view','2025-09-09 00:42:55.016471',17,1),(147,'view','2025-09-09 00:43:10.090693',10,1),(148,'view','2025-09-09 00:43:22.737734',4,1),(149,'view','2025-09-09 00:43:41.078196',3,1),(150,'view','2025-09-09 00:43:45.081845',5,1),(151,'view','2025-09-09 00:44:07.944791',15,1),(152,'view','2025-09-09 00:44:33.838623',16,1),(153,'view','2025-09-09 00:44:38.254235',4,1),(154,'view','2025-09-09 00:45:33.935452',11,1),(155,'view','2025-09-09 01:38:12.107184',16,1),(156,'view','2025-09-09 01:38:24.277712',16,1),(157,'cart','2025-09-09 01:38:25.575395',16,1);
/*!40000 ALTER TABLE `browsing_history_browsinghistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts_cart`
--

DROP TABLE IF EXISTS `carts_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carts_cart_user_id_bd0756c7_fk_users_customuser_id` (`user_id`),
  CONSTRAINT `carts_cart_user_id_bd0756c7_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts_cart`
--

LOCK TABLES `carts_cart` WRITE;
/*!40000 ALTER TABLE `carts_cart` DISABLE KEYS */;
INSERT INTO `carts_cart` VALUES (1,'2025-07-28 08:46:41.726725','2025-07-28 08:46:41.726784',1);
/*!40000 ALTER TABLE `carts_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts_cartitem`
--

DROP TABLE IF EXISTS `carts_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `cart_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `carts_cartitem_cart_id_product_id_883bacdf_uniq` (`cart_id`,`product_id`),
  KEY `carts_cartitem_product_id_acd010e4_fk_products_product_id` (`product_id`),
  CONSTRAINT `carts_cartitem_cart_id_9cb0a756_fk_carts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `carts_cart` (`id`),
  CONSTRAINT `carts_cartitem_product_id_acd010e4_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `carts_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts_cartitem`
--

LOCK TABLES `carts_cartitem` WRITE;
/*!40000 ALTER TABLE `carts_cartitem` DISABLE KEYS */;
INSERT INTO `carts_cartitem` VALUES (68,1,1,1),(69,1,1,2),(70,1,1,17),(71,1,1,16);
/*!40000 ALTER TABLE `carts_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-07-22 06:55:45.586560','2','mohammad',1,'[{\"added\": {}}]',6,1),(2,'2025-07-22 06:55:56.681194','2','mohammad',2,'[]',6,1),(3,'2025-07-22 07:04:48.230980','2','mohammad',2,'[{\"changed\": {\"fields\": [\"User type\", \"Last login\"]}}]',6,1),(4,'2025-07-24 07:20:33.260438','1','abc',1,'[{\"added\": {}}]',9,1),(5,'2025-07-24 07:59:10.226411','2','idvsoi',1,'[{\"added\": {}}]',9,1),(6,'2025-07-24 08:02:51.200969','3','gfgff',1,'[{\"added\": {}}]',9,1),(7,'2025-07-24 08:03:53.981968','4','ghty,mmgm',1,'[{\"added\": {}}]',9,1),(8,'2025-07-24 08:42:37.682456','5','mohammdjfisif',1,'[{\"added\": {}}]',9,1),(9,'2025-07-24 08:42:54.583709','6','faas',1,'[{\"added\": {}}]',9,1),(10,'2025-07-24 08:53:26.688343','7','gggg',1,'[{\"added\": {}}]',9,1),(11,'2025-07-24 09:11:37.114697','6','faas',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',9,1),(12,'2025-07-24 09:12:47.279097','1','abc',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',9,1),(13,'2025-07-26 08:48:22.941109','3','shahin_eshg_abadi',2,'[{\"changed\": {\"fields\": [\"Skin type\", \"Concern\", \"Preferences\", \"Created at\"]}}]',6,1),(14,'2025-07-26 10:05:28.446961','7','gggg',2,'[{\"changed\": {\"fields\": [\"Skin type\", \"Concern targeted\", \"Preferences\", \"Ingredient\", \"Rating\"]}}]',9,1),(15,'2025-07-27 06:30:19.858780','1','hydarting facial',1,'[{\"added\": {}}]',9,1),(16,'2025-07-27 06:30:31.226575','1','hydarting facial',2,'[]',9,1),(17,'2025-07-27 06:32:24.745634','2','foaming facial',1,'[{\"added\": {}}]',9,1),(18,'2025-07-27 06:34:07.064203','3','calm and restore oat',1,'[{\"added\": {}}]',9,1),(19,'2025-07-27 06:36:33.706949','4','Rosehip cream',1,'[{\"added\": {}}]',9,1),(20,'2025-07-27 06:39:16.502433','5','one-step facial',1,'[{\"added\": {}}]',9,1),(21,'2025-07-27 06:43:05.047756','6','Glow tonic',1,'[{\"added\": {}}]',9,1),(22,'2025-07-27 06:43:17.269761','4','Rosehip cream',2,'[{\"changed\": {\"fields\": [\"Ingredient\"]}}]',9,1),(23,'2025-07-27 06:44:43.257408','7','hydrating toner',1,'[{\"added\": {}}]',9,1),(24,'2025-07-27 06:47:29.609515','8','Galactomyces',1,'[{\"added\": {}}]',9,1),(25,'2025-07-27 06:50:51.694504','9','Hyalu B5',1,'[{\"added\": {}}]',9,1),(26,'2025-07-27 06:53:07.037773','10','super serum 5in1',1,'[{\"added\": {}}]',9,1),(27,'2025-07-27 06:55:42.781645','11','5 the serum',1,'[{\"added\": {}}]',9,1),(28,'2025-07-27 06:59:49.888794','12','daily motion',1,'[{\"added\": {}}]',9,1),(29,'2025-07-27 07:02:13.911591','13','lotion',1,'[{\"added\": {}}]',9,1),(30,'2025-07-27 07:04:33.944709','14','daily motion',1,'[{\"added\": {}}]',9,1),(31,'2025-07-27 07:06:55.567087','15','lotion',1,'[{\"added\": {}}]',9,1),(32,'2025-07-27 22:01:05.192288','1','admin - 2025-07-27 22:01:05.187281+00:00',1,'[{\"added\": {}}]',12,1),(33,'2025-07-27 22:01:18.935021','2','mohammad - 2025-07-27 22:01:18.932533+00:00',1,'[{\"added\": {}}]',12,1),(34,'2025-07-27 22:01:35.258801','3','shahin_eshg_abadi - 2025-07-27 22:01:35.256004+00:00',1,'[{\"added\": {}}]',12,1),(35,'2025-07-27 22:01:53.187515','4','shahin_eshg_abadi - 2025-07-27 22:01:53.185215+00:00',1,'[{\"added\": {}}]',12,1),(36,'2025-07-28 06:35:49.650821','1','hydarting facial',1,'[{\"added\": {}}]',9,1),(37,'2025-07-28 06:36:03.390218','1','mohammad - 2025-07-28 06:36:03.388867+00:00',1,'[{\"added\": {}}]',12,1),(38,'2025-07-29 06:09:28.999164','1','hydarting facial',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',9,1),(39,'2025-07-29 16:47:47.726763','2','hydarting facial',1,'[{\"added\": {}}]',9,1),(40,'2025-07-29 16:50:16.759106','3','Rosehip cream',1,'[{\"added\": {}}]',9,1),(41,'2025-07-29 16:51:55.857475','4','lotion',1,'[{\"added\": {}}]',9,1),(42,'2025-07-29 16:54:10.503299','5','body lotion',1,'[{\"added\": {}}]',9,1),(43,'2025-07-29 17:01:01.369898','6','Hydra Boost Toner',1,'[{\"added\": {}}]',9,1),(44,'2025-07-29 17:03:07.131810','7','Glow Deep Essence',1,'[{\"added\": {}}]',9,1),(45,'2025-07-29 17:07:10.749747','8','Advanced Snail 96 Mucin Power Essence',1,'[{\"added\": {}}]',9,1),(46,'2025-07-29 17:09:38.072215','9','Niacinamide 10% + Zinc 1%',1,'[{\"added\": {}}]',9,1),(47,'2025-07-29 17:12:44.666290','10','Vitamin C Suspension 23% + HA Spheres',1,'[{\"added\": {}}]',9,1),(48,'2025-07-29 17:16:08.535569','11','Propolis Light Ampoule',1,'[{\"added\": {}}]',9,1),(49,'2025-07-29 17:19:19.747106','12','Moisture Surge 100H Auto-Replenishing Hydrator',1,'[{\"added\": {}}]',9,1),(50,'2025-07-29 17:19:37.106150','12','Moisture Surge 100H Auto-Replenishing Hydrator',2,'[{\"changed\": {\"fields\": [\"Stock\", \"Rating\"]}}]',9,1),(51,'2025-07-29 17:22:26.893392','13','Ceramidin Cream',1,'[{\"added\": {}}]',9,1),(52,'2025-07-29 17:25:12.395009','14','Water Bank Blue Hyaluronic Cream',1,'[{\"added\": {}}]',9,1),(53,'2025-07-29 17:27:44.012595','15','Cica Cream Intense',1,'[{\"added\": {}}]',9,1),(54,'2025-08-03 15:25:07.797195','16','dsfghjjhgfdd',1,'[{\"added\": {}}]',9,1),(55,'2025-09-09 00:02:35.984727','17','kerem',1,'[{\"added\": {}}]',9,1),(56,'2025-09-09 01:31:03.844090','18','nnnn',1,'[{\"added\": {}}]',9,1),(57,'2025-09-09 01:32:09.678615','19','sunscren best',1,'[{\"added\": {}}]',9,1),(58,'2025-09-09 01:32:53.287280','20','sunkissyyyy',1,'[{\"added\": {}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(7,'authtoken','token'),(8,'authtoken','tokenproxy'),(17,'browsing_history','browsinghisrory'),(18,'browsing_history','browsinghistory'),(14,'carts','cart'),(13,'carts','cartitem'),(4,'contenttypes','contenttype'),(10,'products','category'),(12,'products','comments'),(9,'products','product'),(15,'products','ratings'),(11,'quiz','quiz'),(16,'routins','routine'),(5,'sessions','session'),(6,'users','customuser');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-07-22 06:09:59.292311'),(2,'contenttypes','0002_remove_content_type_name','2025-07-22 06:09:59.362781'),(3,'auth','0001_initial','2025-07-22 06:09:59.555881'),(4,'auth','0002_alter_permission_name_max_length','2025-07-22 06:09:59.601344'),(5,'auth','0003_alter_user_email_max_length','2025-07-22 06:09:59.606346'),(6,'auth','0004_alter_user_username_opts','2025-07-22 06:09:59.609671'),(7,'auth','0005_alter_user_last_login_null','2025-07-22 06:09:59.613158'),(8,'auth','0006_require_contenttypes_0002','2025-07-22 06:09:59.614703'),(9,'auth','0007_alter_validators_add_error_messages','2025-07-22 06:09:59.617808'),(10,'auth','0008_alter_user_username_max_length','2025-07-22 06:09:59.621698'),(11,'auth','0009_alter_user_last_name_max_length','2025-07-22 06:09:59.625914'),(12,'auth','0010_alter_group_name_max_length','2025-07-22 06:09:59.635741'),(13,'auth','0011_update_proxy_permissions','2025-07-22 06:09:59.639919'),(14,'auth','0012_alter_user_first_name_max_length','2025-07-22 06:09:59.643127'),(15,'users','0001_initial','2025-07-22 06:09:59.845858'),(16,'admin','0001_initial','2025-07-22 06:09:59.936884'),(17,'admin','0002_logentry_remove_auto_add','2025-07-22 06:09:59.941669'),(18,'admin','0003_logentry_add_action_flag_choices','2025-07-22 06:09:59.945787'),(19,'sessions','0001_initial','2025-07-22 06:09:59.968251'),(20,'authtoken','0001_initial','2025-07-22 07:32:10.409344'),(21,'authtoken','0002_auto_20160226_1747','2025-07-22 07:32:10.421951'),(22,'authtoken','0003_tokenproxy','2025-07-22 07:32:10.424356'),(23,'authtoken','0004_alter_tokenproxy_options','2025-07-22 07:32:10.427300'),(27,'users','0002_customuser_profile_image','2025-07-24 09:34:51.623029'),(28,'users','0003_customuser_skin_type','2025-07-26 07:23:37.021428'),(29,'users','0004_alter_customuser_skin_type','2025-07-26 07:25:10.480273'),(30,'users','0005_customuser_concern_customuser_created_at_and_more','2025-07-26 08:44:12.356772'),(37,'quiz','0001_initial','2025-07-27 08:13:11.758605'),(39,'products','0001_initial','2025-07-28 06:33:15.490361'),(40,'carts','0001_initial','2025-07-28 08:46:20.620819'),(41,'products','0002_product_tags_alter_product_concern_targeted_and_more','2025-07-29 06:07:54.155018'),(42,'quiz','0002_remove_quiz_concern_targeted_remove_quiz_preferences_and_more','2025-07-29 07:33:06.071439'),(43,'products','0003_ratings','2025-07-30 06:32:19.917327'),(44,'routins','0001_initial','2025-07-30 07:40:42.198006'),(45,'quiz','0003_quiz_concern_targeted_quiz_preferences_and_more','2025-07-30 08:08:26.035660'),(46,'users','0006_alter_customuser_skin_type','2025-08-05 14:09:26.609306'),(47,'users','0007_alter_customuser_concern_and_more','2025-08-05 14:31:35.582638'),(48,'browsing_history','0001_initial','2025-09-08 15:44:42.580330'),(49,'browsing_history','0002_browsinghistory_delete_browsinghisrory','2025-09-08 17:03:59.048852');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7dll6txyhffgz635x1zoigwz39fyjv5i','.eJxVjEEOwiAURO_C2hDw8wFduu8ZCPBBqgaS0q6Md5cmXehmMpk3M2_m_LYWt_W0uJnYlUl2-s2Cj89Ud0APX--Nx1bXZQ58r_CDdj41Sq_b0f07KL6XsUaBwYIV2mRMcCZAIKvt0KwvJuThjRSkI0ifAU1UKmoShKCkNCayzxe3fzbH:1uvYVB:XCCHVl_NMQc0KTuDaBc-CPp868ZxWGaixPLJhpjd-hs','2025-09-22 09:49:33.362834'),('gq0xtfrbqo1zbwkbs15ievlloa85pxk3','.eJxVjEEOwiAQRe_C2hAq0BaX7j0DGYYZqRpISrsy3t2SdNFu_3vvf4WHdUl-rTT7KYqbMOJy3ALgm3ID8QX5WSSWvMxTkE2RO63yUSJ97rt7OkhQU6udA2cMKRztwDAykVbBMkey3FvcMESm0OGAlsgw6o6dviL2vBVK_P4gTzl4:1ujgca:mWCzenwxjYY7XD0oy_NGL4OYpvPwS1V0Ree6vpPSj7I','2025-08-20 16:04:08.320136'),('jiqswlqce47gcccgs1w4hf95ubgvkmdl','.eJxVjEEOwiAURO_C2hDw8wFduu8ZCPBBqgaS0q6Md5cmXehmMpk3M2_m_LYWt_W0uJnYlUl2-s2Cj89Ud0APX--Nx1bXZQ58r_CDdj41Sq_b0f07KL6XsUaBwYIV2mRMcCZAIKvt0KwvJuThjRSkI0ifAU1UKmoShKCkNCayzxe3fzbH:1ugH49:SEqfj-quAuDRVIM-4orV_0qjyycaSiRc63yExQA3Csc','2025-08-11 06:10:29.356924'),('l9ljncj1mbvsa9yo161w3yxi8mpiwmjw','.eJxVjEEOwiAURO_C2hDw8wFduu8ZCPBBqgaS0q6Md5cmXehmMpk3M2_m_LYWt_W0uJnYlUl2-s2Cj89Ud0APX--Nx1bXZQ58r_CDdj41Sq_b0f07KL6XsUaBwYIV2mRMcCZAIKvt0KwvJuThjRSkI0ifAU1UKmoShKCkNCayzxe3fzbH:1uvjku:xMcwcSWHWtkHBcPCf7W8uUkKeYP5vsF19MGg7A-Q7qw','2025-09-22 21:50:32.530276'),('nxj1x3vup5q34iz3xpsze4hyhwpdqecd','.eJxVjEEOwiAURO_C2hDw8wFduu8ZCPBBqgaS0q6Md5cmXehmMpk3M2_m_LYWt_W0uJnYlUl2-s2Cj89Ud0APX--Nx1bXZQ58r_CDdj41Sq_b0f07KL6XsUaBwYIV2mRMcCZAIKvt0KwvJuThjRSkI0ifAU1UKmoShKCkNCayzxe3fzbH:1ujJAG:iQS3iY7oiwg64znSMGSD1PVtJPGkDiRPWariH1BOj94','2025-08-19 15:01:20.302016');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_comments`
--

DROP TABLE IF EXISTS `products_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_comments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_comments_user_id_fb5d2a2b_fk_users_customuser_id` (`user_id`),
  KEY `products_comments_product_id_1fd03457_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_comments_product_id_1fd03457_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_comments_user_id_fb5d2a2b_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_comments`
--

LOCK TABLES `products_comments` WRITE;
/*!40000 ALTER TABLE `products_comments` DISABLE KEYS */;
INSERT INTO `products_comments` VALUES (1,'ridammmmmmmmmmmmmmmmm','2025-07-28 06:36:03.388867',2,1),(2,'aliee','2025-07-28 07:04:04.046598',1,1),(3,'aliee','2025-07-28 07:04:08.352477',1,1),(4,'aliee','2025-07-28 07:06:30.098216',1,1),(5,'mkk','2025-07-28 07:06:58.073187',1,1),(6,'re','2025-07-28 07:16:42.273905',1,1),(7,'sdaf','2025-07-28 07:16:46.725395',1,1),(8,'sdaf','2025-07-28 07:16:47.450577',1,1),(9,'ksldcks','2025-07-28 07:16:54.340590',1,1),(10,'ksldcks','2025-07-28 07:16:54.949236',1,1),(11,'ksldcks','2025-07-28 07:17:03.934192',1,1),(12,'ksldcks','2025-07-28 07:17:04.176192',1,1),(13,'ksldcks','2025-07-28 07:17:04.385049',1,1),(14,'asf','2025-07-28 07:17:37.604156',1,1),(15,'asf','2025-07-28 07:17:44.860779',1,1),(16,'malkcm','2025-07-28 07:18:00.373628',1,1),(17,'sal,','2025-07-28 07:23:16.275099',1,1),(18,'salmaa rrididd','2025-07-28 07:24:52.067021',1,1),(19,'ئخا','2025-07-28 08:35:44.263677',1,1),(20,'slayyyyy','2025-07-29 17:52:13.058281',1,5),(21,'fireeee???','2025-07-29 17:52:31.108775',1,5),(22,'great init ??','2025-07-29 17:52:50.615930',1,5),(23,'kefaklnkaf','2025-07-30 05:56:38.433522',1,1),(24,'salam','2025-07-30 06:56:55.907574',1,12),(25,'man ridam to in product','2025-07-30 07:04:07.673402',4,12),(26,'ایلیا دو صفر','2025-08-01 00:59:26.553420',1,1),(27,'ودف واقعااااااااااا','2025-08-06 15:17:03.913419',1,11),(28,'افتضاح','2025-09-08 23:53:09.254961',1,1),(29,'kheily bade','2025-09-09 00:03:13.876506',1,17);
/*!40000 ALTER TABLE `products_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category` varchar(50) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `stock` int unsigned NOT NULL,
  `skin_type` varchar(30) NOT NULL,
  `concern_targeted` varchar(93) NOT NULL,
  `preferences` varchar(142) NOT NULL,
  `ingredient` varchar(406) NOT NULL,
  `rating` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `tags` varchar(761) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `products_product_chk_1` CHECK ((`stock` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (1,'hydarting facial','',5656.00,'cleanser','CearVe','products/download_QGCZX0M.jpeg',8,'dry,sensitive','dullness,redness,uneven_tone,puffiness','paraben_free,dermatologist_tested,sulfate_free','salicylic_acid,lactic_acid,azelaic_acid,licorice_extract',4,'2025-07-28 06:35:49.649968','hydarting-facial','Toner-Essence,Moisturizer,Mask,combination,wrinkles,uneven_tone,cruelty_free,dermatologist_tested,squalane,mandelic_acid,licorice_extract,zinc_oxide,green_tea_extract,caffeine,peptides,dimethicone'),(2,'hydarting facial','something to use',0.38,'cleanser','CearVe','products/download_BBqnCry.jpeg',16,'oily','wrinkles,redness,puffiness','cruelty_free,paraben_free,sulfate_free','panthenol,glycolic_acid,arbutin,kojic_acid,niacinamide,green_tea_extract,argan_oil,caffeine',1,'2025-07-29 16:47:47.712775','hydarting-facial-1','cleanser,oily,wrinkles,redness,puffiness,cruelty_free,paraben_free,sulfate_free,panthenol,glycolic_acid,arbutin,kojic_acid,niacinamide,green_tea_extract,argan_oil,caffeine'),(3,'Rosehip cream','for cream',75.26,'cleanser','trilogy','products/images_1_e2YzxlX.jpeg',42,'dry,sensitive','acne,dark_spots,pores','vegan,non_comedogenic','hyaluronic_acid,aloe_vera,glycolic_acid,lactic_acid',1,'2025-07-29 16:50:16.752960','rosehip-cream','cleanser,dry,sensitive,acne,dark_spots,pores,vegan,non_comedogenic,hyaluronic_acid,aloe_vera,glycolic_acid,lactic_acid'),(4,'lotion','lotion for face',12.50,'Toner-Essence','Aveeno','products/51NnCUOvL_Dfe3f29._UF10001000_QL80_.jpg',10,'combination','uneven_tone,blackheads,puffiness','eco_friendly,natural_ingredients','green_tea_extract,vitamin_e,rosehip_oil,argan_oil,tea_tree_oil',1,'2025-07-29 16:51:55.852361','lotion','Toner-Essence,dry,uneven_tone,blackheads,puffiness,eco_friendly,natural_ingredients,green_tea_extract,vitamin_e,rosehip_oil,argan_oil,tea_tree_oil'),(5,'body lotion','for all bodies',32.80,'Toner-Essence','trilogy','products/images_1_zhM9fQT.jpeg',0,'dry','uneven_tone,blackheads','fragrance_free,alcohol_free,cruelty_free','caffeine,collagen,dimethicone,mica,iron_oxides',1,'2025-07-29 16:54:10.499058','body-lotion','Toner-Essence,dry,uneven_tone,blackheads,fragrance_free,alcohol_free,cruelty_free,caffeine,collagen,dimethicone,mica,iron_oxides'),(6,'Hydra Boost Toner','Lightweight hydrating toner with hyaluronic acid',420000.00,'Toner-Essence','Neutrogena','products/images_1_79ppJuW.jpeg',0,'dry,sensitive','dullness','fragrance_free,alcohol_free','hyaluronic_acid,glycerin,panthenol',1,'2025-07-29 17:01:01.367960','hydra-boost-toner','Toner-Essence,dry,sensitive,dullness,fragrance_free,alcohol_free,hyaluronic_acid,glycerin,panthenol'),(7,'Glow Deep Essence','Brightening essence with arbutin and niacinamide',580000.00,'Toner-Essence','Cosrx','',89,'dry,oily,combination,sensitive','dark_spots,uneven_tone','cruelty_free,vegan','arbutin,niacinamide',1,'2025-07-29 17:03:07.129537','glow-deep-essence','dry,oily,combination,sensitive,dark_spots,uneven_tone,cruelty_free,vegan,arbutin,niacinamide'),(8,'Advanced Snail 96 Mucin Power Essence','Healing and repairing essence with snail mucin',750000.00,'Serum-Treatments','Cosrx','products/download_1_sD6B3kZ.jpeg',0,'dry,sensitive','acne,redness','cruelty_free','panthenol',1,'2025-07-29 17:07:10.747674','advanced-snail-96-mucin-power-essence','Serum-Treatments,dry,sensitive,acne,redness,cruelty_free,panthenol'),(9,'Niacinamide 10% + Zinc 1%','Brightening and oil-controlling serum',520000.00,'Serum-Treatments','The Ordinary','',0,'oily,combination','dark_spots','alcohol_free','niacinamide,zinc_oxide',1,'2025-07-29 17:09:38.067664','niacinamide-10-zinc-1','Serum-Treatments,oily,combination,dark_spots,alcohol_free,niacinamide,zinc_oxide'),(10,'Vitamin C Suspension 23% + HA Spheres','Antioxidant serum for brightening and firming.',520000.00,'Serum-Treatments','The Ordinary','products/images.avif',53,'dry','uneven_tone','fragrance_free','squalane',1,'2025-07-29 17:12:44.664181','vitamin-c-suspension-23-ha-spheres','Serum-Treatments,dry,uneven_tone,fragrance_free,squalane'),(11,'Propolis Light Ampoule','Nourishing ampoule with 83% propolis extract.',690000.00,'Serum-Treatments','Cosrx','products/download_2.jpeg',11,'dry,sensitive','','fragrance_free','panthenol',4,'2025-07-29 17:16:08.531178','propolis-light-ampoule','dry,sensitive,fragrance_free,panthenol'),(12,'Moisture Surge 100H Auto-Replenishing Hydrator','Oil-free gel cream that provides deep hydration for 100 hours.',1400000.00,'Moisturizer','Clinique','products/download_3.jpeg',82,'dry,oily,combination,sensitive','dullness','fragrance_free','hyaluronic_acid,aloe_vera,caffeine',3.2,'2025-07-29 17:19:19.744878','moisture-surge-100h-auto-replenishing-hydrator','Moisturizer,dry,oily,combination,sensitive,dullness,fragrance_free,hyaluronic_acid,aloe_vera,caffeine'),(13,'Ceramidin Cream','Strengthens skin barrier and locks in moisture',1300000.00,'Moisturizer','Dr. Jart','',26,'dry,sensitive','redness','fragrance_free','panthenol',2.36,'2025-07-29 17:22:26.890634','ceramidin-cream','Moisturizer,dry,sensitive,redness,fragrance_free,panthenol'),(14,'Water Bank Blue Hyaluronic Cream','Hydrating cream with blue hyaluronic acid for moisture retention.',1150000.00,'Moisturizer','Laneige','products/download_5.jpeg',41,'dry,combination','','','hyaluronic_acid',4,'2025-07-29 17:25:12.392716','water-bank-blue-hyaluronic-cream','Moisturizer,dry,combination,hyaluronic_acid'),(15,'Cica Cream Intense','Intensive soothing repair cream for damaged skin.',1600000.00,'Moisturizer','La Roche-Posay','products/download_6.jpeg',15,'dry,sensitive','redness','fragrance_free','panthenol,zinc_oxide',1.5,'2025-07-29 17:27:44.009611','cica-cream-intense','Moisturizer,dry,sensitive,redness,fragrance_free,panthenol,zinc_oxide'),(16,'dsfghjjhgfdd','ertygbfvfa\r\ndbngfhjmfchxbgf\r\nsgfxncghfmn fg\r\nzsfdbfghdjmf \r\nasrgsbhxdfn',1233.00,'cleanser','sb','',65,'oily','pores,uneven_tone','paraben_free','glycerin',1,'2025-08-03 15:25:07.788757','dsfghjjhgfdd','Exfoliator'),(17,'kerem','for any time',12.50,'Sunscreen','mmd','products/Screenshot_2025-09-06_134040.png',83132,'dry,combination,sensitive','wrinkles,redness,uneven_tone,puffiness','cruelty_free,paraben_free,dermatologist_tested,sulfate_free','glycerin,squalane,aloe_vera,lactic_acid,mandelic_acid,vitamin_c,kojic_acid,niacinamide,zinc_oxide,green_tea_extract,vitamin_e,rosehip_oil,argan_oil,caffeine,retinol,retinaldehyde,peptides,collagen,iron_oxides',1,'2025-09-09 00:02:35.981992','kerem','Sunscreen,Eye-Care,acne,wrinkles,blackheads,fragrance_free,sulfate_free,natural_ingredients,glycerin,azelaic_acid,vitamin_c,niacinamide'),(18,'nnnn','kdchlkdshkhsdlch',1.00,'Sunscreen','Cetaphil','',8,'combination','dullness,pores','vegan,dermatologist_tested','mandelic_acid,licorice_extract,titanium_dioxide,centella_asiatica',1,'2025-09-09 01:31:03.835901','nnnn','Moisturizer,wrinkles,blackheads,cruelty_free'),(19,'sunscren best','recover every 3 hours',78000.00,'Sunscreen','beest','',12,'combination','redness,uneven_tone','vegan,non_comedogenic,sulfate_free','lactic_acid,vitamin_c,titanium_dioxide,centella_asiatica,chamomile_extract',1,'2025-09-09 01:32:09.675011','sunscren-best','Exfoliator,Eye-Care,sensitive,alcohol_free,paraben_free,arbutin,titanium_dioxide,chamomile_extract,bakuchiol'),(20,'sunkissyyyy','best for hot and sunny days',8996666.00,'Sunscreen','Cosrx','',87,'sensitive','dark_spots','non_comedogenic','squalane',1,'2025-09-09 01:32:53.284901','sunkissyyyy','redness,fragrance_free,dermatologist_tested,kojic_acid,tea_tree_oil');
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_ratings`
--

DROP TABLE IF EXISTS `products_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_ratings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `score` smallint unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_ratings_product_id_77f614d8_fk_products_product_id` (`product_id`),
  KEY `products_ratings_user_id_5dffc608_fk_users_customuser_id` (`user_id`),
  CONSTRAINT `products_ratings_product_id_77f614d8_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_ratings_user_id_5dffc608_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `products_ratings_chk_1` CHECK ((`score` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_ratings`
--

LOCK TABLES `products_ratings` WRITE;
/*!40000 ALTER TABLE `products_ratings` DISABLE KEYS */;
INSERT INTO `products_ratings` VALUES (1,4,'2025-07-30 06:57:03.391327',12,1),(2,1,'2025-07-30 07:03:00.399888',12,3),(3,5,'2025-07-30 07:03:48.355103',12,4),(4,3,'2025-08-01 00:57:54.190612',1,1),(5,4,'2025-09-08 18:29:45.270697',4,1),(6,1,'2025-09-08 18:39:42.964866',2,1),(7,4,'2025-09-08 21:12:48.944907',9,1),(8,4,'2025-09-08 21:31:27.651262',3,1),(9,5,'2025-09-08 22:37:13.532598',16,1),(10,1,'2025-09-09 00:03:15.815549',17,1);
/*!40000 ALTER TABLE `products_ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz_quiz`
--

DROP TABLE IF EXISTS `quiz_quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz_quiz` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `user_id_id` bigint NOT NULL,
  `tags` varchar(267) NOT NULL,
  `concern_targeted` varchar(93) NOT NULL,
  `preferences` varchar(142) NOT NULL,
  `skin_type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quiz_quiz_user_id_id_131a0d99_fk_users_customuser_id` (`user_id_id`),
  CONSTRAINT `quiz_quiz_user_id_id_131a0d99_fk_users_customuser_id` FOREIGN KEY (`user_id_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz_quiz`
--

LOCK TABLES `quiz_quiz` WRITE;
/*!40000 ALTER TABLE `quiz_quiz` DISABLE KEYS */;
INSERT INTO `quiz_quiz` VALUES (1,'2025-07-29 07:33:37.846202',1,'','','',''),(2,'2025-07-30 09:05:21.826098',1,'','','',''),(3,'2025-07-30 09:14:38.657683',1,'dry','','','dry'),(4,'2025-07-30 09:15:01.868981',1,'combination','','','combination'),(5,'2025-08-01 00:55:17.359487',1,'dry','','','dry'),(6,'2025-08-03 11:38:15.447032',1,'dry','','','dry'),(7,'2025-08-05 15:12:28.486108',1,'combination','','','combination'),(8,'2025-08-06 14:56:06.885304',1,'dry','','','dry'),(9,'2025-08-06 15:05:15.244904',1,'dry','','','dry'),(10,'2025-08-06 15:14:24.680590',1,'dry','','','dry'),(11,'2025-08-06 15:18:33.524634',3,'oily','','','oily'),(12,'2025-08-06 15:34:06.237879',3,'dry','','','dry'),(13,'2025-08-06 15:38:24.395868',3,'dry','','','dry'),(14,'2025-08-06 15:39:09.823883',3,'dry','','','dry'),(15,'2025-08-06 15:40:39.749955',1,'oily','','','oily'),(16,'2025-08-06 15:41:33.973645',1,'dry','','','dry'),(17,'2025-08-06 15:57:14.302139',1,'dry','','','dry'),(18,'2025-08-06 15:57:52.895376',1,'dry','','','dry'),(19,'2025-08-06 15:58:23.011901',1,'dry','','','dry'),(20,'2025-09-08 23:56:01.508471',1,'combination','','','combination');
/*!40000 ALTER TABLE `quiz_quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routins_routine`
--

DROP TABLE IF EXISTS `routins_routine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routins_routine` (
  `routine_id` char(32) NOT NULL,
  `plan_name` varchar(255) NOT NULL,
  `steps` json NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`routine_id`),
  KEY `routins_routine_user_id_58e9ca7c_fk_users_customuser_id` (`user_id`),
  CONSTRAINT `routins_routine_user_id_58e9ca7c_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routins_routine`
--

LOCK TABLES `routins_routine` WRITE;
/*!40000 ALTER TABLE `routins_routine` DISABLE KEYS */;
INSERT INTO `routins_routine` VALUES ('08aa7ab0bf1041db9c7d8f1ce8a6a3d5','Full Plan','[{\"step_name\": \"Serum-Treatments\", \"product_id\": 11}]','2025-08-06 15:05:15.285744',1),('0edf7b82495741408353092290233449','Full Plan','[{\"step_name\": \"Serum-Treatments\", \"product_id\": 11}]','2025-08-06 15:18:33.571635',3),('13b5ffc97e34457d952df21a92ede502','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 1}, {\"step_name\": \"Toner-Essence\", \"product_id\": 5}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:57:52.926961',1),('3c3b0b0615044a9ea78676dd03759a27','Full Plan','[{\"step_name\": \"Serum-Treatments\", \"product_id\": 11}]','2025-08-06 15:14:24.713047',1),('444c1246b32c487bb2f97840082be7b0','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 1}, {\"step_name\": \"Toner-Essence\", \"product_id\": 5}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:57:14.338332',1),('871274652ea540588656398b64d8908f','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 1}, {\"step_name\": \"Toner-Essence\", \"product_id\": 5}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:38:24.430282',3),('ad53ff5487654c8f8296b33453884597','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 2}, {\"step_name\": \"Toner-Essence\", \"product_id\": 7}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 12}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:40:39.779445',1),('c6ef7d9b8e5245259d97fb056840457f','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 1}, {\"step_name\": \"Toner-Essence\", \"product_id\": 5}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:39:09.853525',3),('d02ff3c0c7e1436cadd230fc4709132f','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 1}, {\"step_name\": \"Toner-Essence\", \"product_id\": 5}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:58:23.041196',1),('d205aead00d54a3fa805c288e4c433d9','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": null}, {\"step_name\": \"Toner-Essence\", \"product_id\": 4}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-09-08 23:56:01.633132',1),('e12fc3ff2d774103997b2449726c58cf','Full Plan','[{\"step_name\": \"Cleanser\", \"product_id\": 1}, {\"step_name\": \"Toner-Essence\", \"product_id\": 5}, {\"step_name\": \"Serum-Treatments\", \"product_id\": 11}, {\"step_name\": \"Moisturizer\", \"product_id\": 14}, {\"step_name\": \"Sunscreen\", \"product_id\": null}, {\"step_name\": \"Exfoliator\", \"product_id\": null}, {\"step_name\": \"Eye-Care\", \"product_id\": null}, {\"step_name\": \"Mask\", \"product_id\": null}]','2025-08-06 15:41:34.022353',1);
/*!40000 ALTER TABLE `routins_routine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser`
--

DROP TABLE IF EXISTS `users_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `profile_image` varchar(100) DEFAULT NULL,
  `skin_type` varchar(29) NOT NULL,
  `concern` varchar(93) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `device_type` varchar(50) DEFAULT NULL,
  `preferences` varchar(142) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser`
--

LOCK TABLES `users_customuser` WRITE;
/*!40000 ALTER TABLE `users_customuser` DISABLE KEYS */;
INSERT INTO `users_customuser` VALUES (1,'pbkdf2_sha256$1000000$FzqZwfkjYhbKMPSBlOY0Vy$A8iLn+ReXpHx6+uJPzS8MflVFaWaWyjPOnplwN962Mc=','2025-09-08 21:50:32.522064',1,'admin','mohammad shahin reza','shamonry','cir@gmail.com',1,1,'2025-07-22 06:29:56.688376','buyer','profile_images/admin.png','dry,sensitive','redness,pores,uneven_tone,blackheads','2025-07-26 08:44:12.233277','desktop','dermatologist_tested,eco_friendly,sulfate_free,natural_ingredients'),(2,'pbkdf2_sha256$1000000$p6IQvbV4ll7m1xnyq7i1XV$N4cMFnoFygaafB26DtLD9eUbFsrXIs/7bjSLM6iRxf4=','2025-07-22 07:04:45.000000',0,'mohammad','','','mohammaddelavar1384@gmail.com',0,1,'2025-07-22 06:55:44.000000','buyer',NULL,'oily','','2025-07-26 08:44:12.233277',NULL,''),(3,'pbkdf2_sha256$1000000$KDIGYBVC10PN8wCSA5XPOE$N0FcmZqTG5n1Eq6N5PqhXxQ4g8rhy58qNMA4F64dgOs=','2025-08-06 15:18:11.541027',0,'shahin_eshg_abadi','shahin','shaporzade','shahin@gmail.com',0,1,'2025-07-22 07:21:23.000000','buyer','profile_images/Screenshot_1_i5qxCQW.png','sensitive','dark_spots,redness','2025-07-26 08:48:13.000000','desktop','fragrance_free,alcohol_free,cruelty_free'),(4,'pbkdf2_sha256$1000000$FThzvgMghZh63fdozXiTuB$FZBcyf+a7YS10ovbcHxWLKDiLTOmF1OlcDYZauGWQTM=','2025-08-06 16:04:08.312569',0,'mohammad_reza','mohammadreza','mehri','mehry@gmail.com',0,1,'2025-07-22 07:24:47.847026','seller',NULL,'oily','','2025-07-26 08:44:12.233277',NULL,'');
/*!40000 ALTER TABLE `users_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_groups`
--

DROP TABLE IF EXISTS `users_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_groups`
--

LOCK TABLES `users_customuser_groups` WRITE;
/*!40000 ALTER TABLE `users_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_user_permissions`
--

DROP TABLE IF EXISTS `users_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_user_permissions`
--

LOCK TABLES `users_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-09  5:21:56
