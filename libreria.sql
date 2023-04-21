-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2023 at 08:39 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `libreria`
--

-- --------------------------------------------------------

--
-- Table structure for table `bibliotecario`
--

CREATE TABLE `bibliotecario` (
  `ID_bibliotecario` int(11) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `carrello_bibliotecario`
--

CREATE TABLE `carrello_bibliotecario` (
  `ID_libro` int(11) NOT NULL,
  `quantita` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `carrello_cliente`
--

CREATE TABLE `carrello_cliente` (
  `ID_cliente` int(11) NOT NULL,
  `ID_libro` int(11) NOT NULL,
  `quantita` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `ID_cliente` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cognome` varchar(255) NOT NULL,
  `indirizzo` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`ID_cliente`, `nome`, `cognome`, `indirizzo`, `email`, `password`) VALUES
(1, 'Francesco', 'Sabot', 'Via Forum Julii, 11 Ruda UD', 'francesco.sabot@gmail.com', 'pescopesco04');

-- --------------------------------------------------------

--
-- Table structure for table `libro`
--

CREATE TABLE `libro` (
  `ID_libro` int(11) NOT NULL,
  `titolo` varchar(255) NOT NULL,
  `autore` varchar(255) DEFAULT NULL,
  `ISBN` varchar(255) DEFAULT NULL,
  `prezzo` decimal(6,2) NOT NULL,
  `copie_magazzino` int(11) NOT NULL,
  `copie_noleggiate` int(11) NOT NULL,
  `riserva_noleggio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `libro`
--

INSERT INTO `libro` (`ID_libro`, `titolo`, `autore`, `ISBN`, `prezzo`, `copie_magazzino`, `copie_noleggiate`, `riserva_noleggio`) VALUES
(1, 'Rosso Malpelo', 'Verga', '9877', '15.00', 5, 0, 2),
(2, 'ciao', 'Verga', '112312321', '20.00', 7, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `noleggio`
--

CREATE TABLE `noleggio` (
  `ID_noleggio` int(11) NOT NULL,
  `data_fine` date NOT NULL,
  `ID_cliente` int(11) NOT NULL,
  `ID_libro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `noleggio`
--

INSERT INTO `noleggio` (`ID_noleggio`, `data_fine`, `ID_cliente`, `ID_libro`) VALUES
(1, '2023-03-31', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `prenotazione`
--

CREATE TABLE `prenotazione` (
  `ID_cliente` int(11) NOT NULL,
  `ID_libro` int(11) NOT NULL,
  `data_richiesta` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bibliotecario`
--
ALTER TABLE `bibliotecario`
  ADD PRIMARY KEY (`ID_bibliotecario`);

--
-- Indexes for table `carrello_bibliotecario`
--
ALTER TABLE `carrello_bibliotecario`
  ADD PRIMARY KEY (`ID_libro`);

--
-- Indexes for table `carrello_cliente`
--
ALTER TABLE `carrello_cliente`
  ADD PRIMARY KEY (`ID_cliente`,`ID_libro`),
  ADD KEY `ID_libro` (`ID_libro`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`ID_cliente`);

--
-- Indexes for table `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`ID_libro`);

--
-- Indexes for table `noleggio`
--
ALTER TABLE `noleggio`
  ADD PRIMARY KEY (`ID_noleggio`),
  ADD KEY `ID_cliente` (`ID_cliente`),
  ADD KEY `ID_libro` (`ID_libro`);

--
-- Indexes for table `prenotazione`
--
ALTER TABLE `prenotazione`
  ADD PRIMARY KEY (`ID_cliente`,`ID_libro`),
  ADD KEY `ID_libro` (`ID_libro`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bibliotecario`
--
ALTER TABLE `bibliotecario`
  MODIFY `ID_bibliotecario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cliente`
--
ALTER TABLE `cliente`
  MODIFY `ID_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `libro`
--
ALTER TABLE `libro`
  MODIFY `ID_libro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `noleggio`
--
ALTER TABLE `noleggio`
  MODIFY `ID_noleggio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `carrello_bibliotecario`
--
ALTER TABLE `carrello_bibliotecario`
  ADD CONSTRAINT `carrello_bibliotecario_ibfk_1` FOREIGN KEY (`ID_libro`) REFERENCES `libro` (`ID_libro`);

--
-- Constraints for table `carrello_cliente`
--
ALTER TABLE `carrello_cliente`
  ADD CONSTRAINT `carrello_cliente_ibfk_1` FOREIGN KEY (`ID_cliente`) REFERENCES `cliente` (`ID_cliente`),
  ADD CONSTRAINT `carrello_cliente_ibfk_2` FOREIGN KEY (`ID_libro`) REFERENCES `libro` (`ID_libro`);

--
-- Constraints for table `noleggio`
--
ALTER TABLE `noleggio`
  ADD CONSTRAINT `noleggio_ibfk_1` FOREIGN KEY (`ID_cliente`) REFERENCES `cliente` (`ID_cliente`),
  ADD CONSTRAINT `noleggio_ibfk_2` FOREIGN KEY (`ID_libro`) REFERENCES `libro` (`ID_libro`);

--
-- Constraints for table `prenotazione`
--
ALTER TABLE `prenotazione`
  ADD CONSTRAINT `prenotazione_ibfk_1` FOREIGN KEY (`ID_cliente`) REFERENCES `cliente` (`ID_cliente`),
  ADD CONSTRAINT `prenotazione_ibfk_2` FOREIGN KEY (`ID_libro`) REFERENCES `libro` (`ID_libro`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
