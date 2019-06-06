-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: github_hawk_eye
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contributor_org_rel`
--

DROP TABLE IF EXISTS `contributor_org_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `contributor_org_rel` (
  `ContributorID` int(11) NOT NULL,
  `OrgID` int(11) NOT NULL,
  PRIMARY KEY (`ContributorID`,`OrgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `contributormodel`
--

DROP TABLE IF EXISTS `contributormodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `contributormodel` (
  `id` int(11) NOT NULL,
  `login` char(128) NOT NULL,
  `name` char(128) DEFAULT NULL,
  `collaborators` int(11) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `email` char(128) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `following` int(11) DEFAULT NULL,
  `hireable` tinyint(1) DEFAULT NULL,
  `location` mediumtext,
  `site_admin` tinyint(1) DEFAULT NULL,
  `type` char(128) DEFAULT NULL,
  `private_gists` int(11) DEFAULT NULL,
  `public_gists` int(11) DEFAULT NULL,
  `public_repos` int(11) DEFAULT NULL,
  `total_private_repos` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lastqueryconfig`
--

DROP TABLE IF EXISTS `lastqueryconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lastqueryconfig` (
  `id` int(11) NOT NULL,
  `startIdx` int(11) NOT NULL,
  `steps` int(11) NOT NULL,
  `endIdx` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orgmodel`
--

DROP TABLE IF EXISTS `orgmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `orgmodel` (
  `id` int(11) NOT NULL,
  `login` char(128) NOT NULL,
  `name` char(128) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `email` char(128) DEFAULT NULL,
  `billing_email` char(128) DEFAULT NULL,
  `type` char(128) DEFAULT NULL,
  `location` mediumtext,
  `blog` mediumtext,
  `collaborators` int(11) DEFAULT NULL,
  `disk_usage` int(11) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `following` int(11) DEFAULT NULL,
  `private_gists` int(11) DEFAULT NULL,
  `public_gists` int(11) DEFAULT NULL,
  `public_repos` int(11) DEFAULT NULL,
  `total_private_repos` int(11) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `owner_org_rel`
--

DROP TABLE IF EXISTS `owner_org_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `owner_org_rel` (
  `OwnerID` int(11) NOT NULL,
  `OrgID` int(11) NOT NULL,
  PRIMARY KEY (`OwnerID`,`OrgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ownermodel`
--

DROP TABLE IF EXISTS `ownermodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ownermodel` (
  `id` int(11) NOT NULL,
  `login` char(128) NOT NULL,
  `name` char(128) DEFAULT NULL,
  `collaborators` int(11) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `email` char(128) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `following` int(11) DEFAULT NULL,
  `hireable` tinyint(1) DEFAULT NULL,
  `location` mediumtext,
  `site_admin` tinyint(1) DEFAULT NULL,
  `type` char(128) DEFAULT NULL,
  `private_gists` int(11) DEFAULT NULL,
  `public_gists` int(11) DEFAULT NULL,
  `public_repos` int(11) DEFAULT NULL,
  `total_private_repos` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `repo_contributor_rel`
--

DROP TABLE IF EXISTS `repo_contributor_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `repo_contributor_rel` (
  `RepoID` int(11) NOT NULL,
  `ContributorID` int(11) NOT NULL,
  PRIMARY KEY (`RepoID`,`ContributorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `repo_org_rel`
--

DROP TABLE IF EXISTS `repo_org_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `repo_org_rel` (
  `RepoID` int(11) NOT NULL,
  `OrgID` int(11) NOT NULL,
  PRIMARY KEY (`RepoID`,`OrgID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `repo_owner_rel`
--

DROP TABLE IF EXISTS `repo_owner_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `repo_owner_rel` (
  `RepoID` int(11) NOT NULL,
  `OwnerID` int(11) NOT NULL,
  PRIMARY KEY (`RepoID`,`OwnerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `repositoriesmodel`
--

DROP TABLE IF EXISTS `repositoriesmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `repositoriesmodel` (
  `id` int(11) NOT NULL,
  `name` char(128) NOT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `subscribers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `language` char(64) DEFAULT NULL,
  `full_name` mediumtext,
  `forks_count` int(11) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `description` mediumtext,
  `network_count` int(11) DEFAULT NULL,
  `open_issues_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-06 10:14:56
