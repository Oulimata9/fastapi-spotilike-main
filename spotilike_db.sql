-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 17 jan. 2024 à 00:07
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `spotilike_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `album`
--

DROP TABLE IF EXISTS `album`;
CREATE TABLE IF NOT EXISTS `album` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Titre` varchar(255) NOT NULL,
  `Pochette` longblob,
  `Date_sortie` date DEFAULT NULL,
  `Artiste_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Artiste_ID` (`Artiste_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `artiste`
--

DROP TABLE IF EXISTS `artiste`;
CREATE TABLE IF NOT EXISTS `artiste` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nom_artiste` varchar(255) NOT NULL,
  `Avatar` longblob,
  `Biographie` text,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `genre`
--

DROP TABLE IF EXISTS `genre`;
CREATE TABLE IF NOT EXISTS `genre` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Titre` varchar(255) NOT NULL,
  `Description` text,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `morceau`
--

DROP TABLE IF EXISTS `morceau`;
CREATE TABLE IF NOT EXISTS `morceau` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Titre` varchar(255) NOT NULL,
  `Duree` time DEFAULT NULL,
  `Artiste_ID` int DEFAULT NULL,
  `Genre_ID` int DEFAULT NULL,
  `Album_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Artiste_ID` (`Artiste_ID`),
  KEY `Genre_ID` (`Genre_ID`),
  KEY `Album_ID` (`Album_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nom_utilisateur` varchar(255) NOT NULL,
  `Mot_de_passe` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
