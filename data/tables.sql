-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: ca_scc_courts
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.4

--
-- Table structure for table `court_appearances`
--

DROP TABLE IF EXISTS `court_appearances`;
CREATE TABLE `court_appearances` (
  `pk` int NOT NULL,
  `dept_pk` int DEFAULT NULL,
  `case_number` varchar(31) DEFAULT NULL,
  `case_id` int DEFAULT NULL,
  `parties` varchar(2048) DEFAULT NULL,
  `parties_lc` varchar(2048) DEFAULT NULL,
  `scheduled_time` varchar(31) DEFAULT NULL,
  `created` bigint DEFAULT NULL,
  `uuid` char(36) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  KEY `scheduled_time` (`scheduled_time`),
  KEY `case_number` (`case_number`),
  KEY `parties` (`parties`(64)),
  KEY `dept_pk` (`dept_pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `court_calendar_depts`
--

DROP TABLE IF EXISTS `court_calendar_depts`;
CREATE TABLE `court_calendar_depts` (
  `pk` int NOT NULL,
  `calendar_pk` int DEFAULT NULL,
  `display_date` varchar(20) DEFAULT NULL,
  `department` varchar(8) DEFAULT NULL,
  `created` bigint DEFAULT NULL,
  PRIMARY KEY (`pk`),
  KEY `display_date` (`display_date`),
  KEY `calendar_pk` (`calendar_pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Table structure for table `court_calendars`
--

DROP TABLE IF EXISTS `court_calendars`;
CREATE TABLE `court_calendars` (
  `pk` int NOT NULL,
  `county_pk` int DEFAULT NULL,
  `name` varchar(31) DEFAULT NULL,
  `abbreviation` char(3) DEFAULT NULL,
  `cal_speak` varchar(31) DEFAULT NULL,
  `created` bigint DEFAULT NULL,
  PRIMARY KEY (`pk`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `court_counties`
--

DROP TABLE IF EXISTS `court_counties`;
CREATE TABLE `court_counties` (
  `pk` int NOT NULL,
  `name` varchar(63) DEFAULT NULL,
  PRIMARY KEY (`pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `notify_reservations`
--

DROP TABLE IF EXISTS `notify_reservations`;
CREATE TABLE `notify_reservations` (
  `pk` int NOT NULL,
  `appearance_uuid` varchar(36) DEFAULT NULL,
  `email_addr` varchar(255) DEFAULT NULL,
  `phone_num` varchar(31) DEFAULT NULL,
  `created` bigint DEFAULT NULL,
  `deleted` bigint DEFAULT NULL,
  PRIMARY KEY (`pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump completed on 2023-08-03 14:27:18
