-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2020 at 06:59 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
CREATE DATABASE `corona`;
USE `corona`;
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Username`, `Password`) VALUES
('aditi.acharya', '2121'),
('suyog.ahuja', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `patient_data`
--

CREATE TABLE `patient_data` (
  `P_id` int(50) NOT NULL,
  `Fname` varchar(50) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `Fever` varchar(50) NOT NULL,
  `BodyPain` varchar(50) NOT NULL,
  `Age` varchar(50) NOT NULL,
  `Runnynose` varchar(50) NOT NULL,
  `DiffBreathing` varchar(50) NOT NULL,
  `Travel` varchar(50) NOT NULL,
  `Result` varchar(50) NOT NULL,
  `State` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_data`
--

INSERT INTO `patient_data` (`P_id`, `Fname`, `Lname`, `Fever`, `BodyPain`, `Age`, `Runnynose`, `DiffBreathing`, `Travel`, `Result`, `State`) VALUES
(1, 'suyog', 'ahuja', '102', '1', '23', '1', '-1', '1', 'POSITIVE', 'MH'),
(2, 'aditi', 'acharya', '98', '0', '90', '0', '0', '0', 'NEGATIVE', 'GJ'),
(3, 'deepika', 'ahuja', '99', '0', '20', '1', '1', '1', 'NEGATIVE', 'AP'),
(4, 'ankita', 'acharya', '101', '1', '20', '1', '-1', '1', 'POSITIVE', 'MP'),
(5, 'kamal', 'punjabi', '103', '1', '45', '0', '1', '1', 'POSITIVE', 'JK'),
(6, 'simran', 'ahuja', '103', '0', '32', '0', '-1', '1', 'POSITIVE', 'DL'),
(7, 'yash', 'katariya', '100', '0', '23', '0', '-1', '0', 'POSITIVE', 'GA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Username`);

--
-- Indexes for table `patient_data`
--
ALTER TABLE `patient_data`
  ADD PRIMARY KEY (`P_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patient_data`
--
ALTER TABLE `patient_data`
  MODIFY `P_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
