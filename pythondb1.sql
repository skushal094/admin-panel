-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 21, 2019 at 12:02 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythondb1`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(10) NOT NULL,
  `date` date NOT NULL,
  `if_attended` int(3) NOT NULL,
  `sub_id` int(5) NOT NULL,
  `teacher_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `studenttable`
--

CREATE TABLE `studenttable` (
  `id` int(11) NOT NULL,
  `fname` text NOT NULL,
  `lname` text NOT NULL,
  `age` int(3) NOT NULL,
  `is_active` int(1) NOT NULL DEFAULT '1',
  `is_deleted` int(1) NOT NULL DEFAULT '0' COMMENT 'value 0 if deleted',
  `class_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studenttable`
--

INSERT INTO `studenttable` (`id`, `fname`, `lname`, `age`, `is_active`, `is_deleted`, `class_id`) VALUES
(1, 'Kushal', 'Shah', 20, 1, 0, 1),
(2, 'Ridham', 'Shah', 20, 1, 0, 1),
(3, 'Ayush', 'Shah', 18, 1, 0, 1),
(4, 'Nisarg', 'Pethani', 20, 1, 0, 1),
(5, 'John', 'Wick', 38, 0, 0, 1),
(6, 'John', 'Doe', 50, 0, 0, 1),
(9, 'Samyak', 'Gandhi', 78, 1, 1, 1),
(10, 'Karan', 'Johar', 40, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_class`
--

CREATE TABLE `tb_class` (
  `class_id` int(5) NOT NULL,
  `name` varchar(20) NOT NULL,
  `sem_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_class`
--

INSERT INTO `tb_class` (`class_id`, `name`, `sem_id`) VALUES
(1, 'CE-19', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_re_teaches`
--

CREATE TABLE `tb_re_teaches` (
  `teacher_id` int(5) NOT NULL,
  `sub_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tb_sem`
--

CREATE TABLE `tb_sem` (
  `sem_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_sem`
--

INSERT INTO `tb_sem` (`sem_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_subjects`
--

CREATE TABLE `tb_subjects` (
  `sub_id` int(5) NOT NULL,
  `name` text NOT NULL,
  `sem_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tb_teachers`
--

CREATE TABLE `tb_teachers` (
  `teacher_id` int(5) NOT NULL,
  `name` text NOT NULL,
  `salary` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD KEY `id` (`id`),
  ADD KEY `sub_id` (`sub_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `studenttable`
--
ALTER TABLE `studenttable`
  ADD PRIMARY KEY (`id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `tb_class`
--
ALTER TABLE `tb_class`
  ADD PRIMARY KEY (`class_id`),
  ADD KEY `sem_id` (`sem_id`);

--
-- Indexes for table `tb_re_teaches`
--
ALTER TABLE `tb_re_teaches`
  ADD KEY `sub_id` (`sub_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `tb_sem`
--
ALTER TABLE `tb_sem`
  ADD PRIMARY KEY (`sem_id`);

--
-- Indexes for table `tb_subjects`
--
ALTER TABLE `tb_subjects`
  ADD PRIMARY KEY (`sub_id`),
  ADD KEY `sem_id` (`sem_id`);

--
-- Indexes for table `tb_teachers`
--
ALTER TABLE `tb_teachers`
  ADD PRIMARY KEY (`teacher_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `studenttable`
--
ALTER TABLE `studenttable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tb_class`
--
ALTER TABLE `tb_class`
  MODIFY `class_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_sem`
--
ALTER TABLE `tb_sem`
  MODIFY `sem_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_subjects`
--
ALTER TABLE `tb_subjects`
  MODIFY `sub_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_teachers`
--
ALTER TABLE `tb_teachers`
  MODIFY `teacher_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`id`) REFERENCES `studenttable` (`id`),
  ADD CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`sub_id`) REFERENCES `tb_subjects` (`sub_id`),
  ADD CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`teacher_id`) REFERENCES `tb_teachers` (`teacher_id`);

--
-- Constraints for table `studenttable`
--
ALTER TABLE `studenttable`
  ADD CONSTRAINT `studenttable_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `tb_class` (`class_id`);

--
-- Constraints for table `tb_class`
--
ALTER TABLE `tb_class`
  ADD CONSTRAINT `tb_class_ibfk_1` FOREIGN KEY (`sem_id`) REFERENCES `tb_sem` (`sem_id`);

--
-- Constraints for table `tb_re_teaches`
--
ALTER TABLE `tb_re_teaches`
  ADD CONSTRAINT `tb_re_teaches_ibfk_1` FOREIGN KEY (`sub_id`) REFERENCES `tb_subjects` (`sub_id`),
  ADD CONSTRAINT `tb_re_teaches_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `tb_teachers` (`teacher_id`);

--
-- Constraints for table `tb_subjects`
--
ALTER TABLE `tb_subjects`
  ADD CONSTRAINT `tb_subjects_ibfk_1` FOREIGN KEY (`sem_id`) REFERENCES `tb_sem` (`sem_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
