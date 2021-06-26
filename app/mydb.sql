-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 26-06-2021 a las 21:47:20
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mydb`
--
CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `mydb`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `languages`
--

DROP TABLE IF EXISTS `languages`;
CREATE TABLE IF NOT EXISTS `languages` (
  `IdLanguages` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Pic_url` varchar(45) DEFAULT NULL,
  `Desc` varchar(45) NOT NULL,
  `Example` varchar(45) NOT NULL,
  PRIMARY KEY (`IdLanguages`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `languages`
--

INSERT INTO `languages` (`IdLanguages`, `Name`, `Pic_url`, `Desc`, `Example`) VALUES
(1, 'Python', 'x', 'X', 'x');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rec`
--

DROP TABLE IF EXISTS `rec`;
CREATE TABLE IF NOT EXISTS `rec` (
  `IdRec` int(11) NOT NULL AUTO_INCREMENT,
  `Difficulty` varchar(45) NOT NULL,
  `Title` varchar(45) NOT NULL,
  `Id_Topic` int(11) NOT NULL,
  PRIMARY KEY (`IdRec`,`Id_Topic`),
  KEY `fk_Rec_Topic1_idx` (`Id_Topic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `topic`
--

DROP TABLE IF EXISTS `topic`;
CREATE TABLE IF NOT EXISTS `topic` (
  `idTopic` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Pic_url` varchar(45) DEFAULT NULL,
  `Id_Languages` int(11) NOT NULL,
  PRIMARY KEY (`idTopic`,`Id_Languages`),
  KEY `fk_Topic_Languages_idx` (`Id_Languages`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `url`
--

DROP TABLE IF EXISTS `url`;
CREATE TABLE IF NOT EXISTS `url` (
  `IdUrl` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Url` varchar(45) NOT NULL,
  `Id_Rec` int(11) NOT NULL,
  PRIMARY KEY (`IdUrl`,`Id_Rec`),
  KEY `fk_Url_Rec1_idx` (`Id_Rec`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `videos`
--

DROP TABLE IF EXISTS `videos`;
CREATE TABLE IF NOT EXISTS `videos` (
  `IdVideos` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Url` varchar(45) NOT NULL,
  `Id_Rec` int(11) NOT NULL,
  PRIMARY KEY (`IdVideos`,`Id_Rec`),
  KEY `fk_Videos_Rec1_idx` (`Id_Rec`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visited`
--

DROP TABLE IF EXISTS `visited`;
CREATE TABLE IF NOT EXISTS `visited` (
  `IdRec` int(11) NOT NULL AUTO_INCREMENT,
  `Id_Topic` int(11) NOT NULL,
  `User_Username` varchar(20) NOT NULL,
  PRIMARY KEY (`IdRec`,`Id_Topic`,`User_Username`),
  KEY `fk_Rec_has_User_User1_idx` (`User_Username`),
  KEY `fk_Rec_has_User_Rec1_idx` (`IdRec`,`Id_Topic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `rec`
--
ALTER TABLE `rec`
  ADD CONSTRAINT `fk_Rec_Topic1` FOREIGN KEY (`Id_Topic`) REFERENCES `topic` (`idTopic`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `topic`
--
ALTER TABLE `topic`
  ADD CONSTRAINT `fk_Topic_Languages` FOREIGN KEY (`Id_Languages`) REFERENCES `languages` (`IdLanguages`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `url`
--
ALTER TABLE `url`
  ADD CONSTRAINT `fk_Url_Rec1` FOREIGN KEY (`Id_Rec`) REFERENCES `rec` (`IdRec`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `videos`
--
ALTER TABLE `videos`
  ADD CONSTRAINT `fk_Videos_Rec1` FOREIGN KEY (`Id_Rec`) REFERENCES `rec` (`IdRec`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `visited`
--
ALTER TABLE `visited`
  ADD CONSTRAINT `fk_Rec_has_User_Rec1` FOREIGN KEY (`IdRec`,`Id_Topic`) REFERENCES `rec` (`IdRec`, `Id_Topic`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Rec_has_User_User1` FOREIGN KEY (`User_Username`) REFERENCES `user` (`Username`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
