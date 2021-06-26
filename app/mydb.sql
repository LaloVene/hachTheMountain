DROP TABLE IF EXISTS languages;
CREATE TABLE IF NOT EXISTS languages (
  IdLanguages INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Name varchar(45) NOT NULL,
  Pic_url varchar(45) DEFAULT NULL,
  Desc varchar(45) NOT NULL,
  Example varchar(45) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla rec
--

DROP TABLE IF EXISTS rec;
CREATE TABLE IF NOT EXISTS rec (
  IdRec INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Difficulty varchar(45) NOT NULL,
  Title varchar(45) NOT NULL,
  Id_Topic int(11) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla topic
--

DROP TABLE IF EXISTS topic;
CREATE TABLE IF NOT EXISTS topic (
  idTopic INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Name varchar(45) DEFAULT NULL,
  Pic_url varchar(45) DEFAULT NULL,
  Id_Languages int(11) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla url
--

DROP TABLE IF EXISTS url;
CREATE TABLE IF NOT EXISTS url (
  IdUrl INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Name varchar(45) NOT NULL,
  Url varchar(45) NOT NULL,
  Id_Rec int(11) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla user
--

DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user (
  Username varchar(20) NOT NULL PRIMARY KEY,
  Password varchar(45) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla videos
--

DROP TABLE IF EXISTS videos;
CREATE TABLE IF NOT EXISTS videos (
  IdVideos INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Name varchar(45) NOT NULL,
  Url varchar(45) NOT NULL,
  Id_Rec int(11) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla visited
--

DROP TABLE IF EXISTS visited;
CREATE TABLE IF NOT EXISTS visited (
  IdRec INTEGER NOT NULL,
  Id_Topic int(11) NOT NULL,
  User_Username VARCHAR(45) NOT NULL
);
