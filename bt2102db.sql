DROP SCHEMA IF EXISTS `bt2102db`;

CREATE DATABASE `bt2102db`;
USE `bt2102db`;

-- create librarymembers table
DROP TABLE IF EXISTS `librarymembers`;

CREATE TABLE `librarymembers` (
  `member_id` varchar(6) NOT NULL,
  `name` varchar(45) NOT NULL,
  `faculty` varchar(11) NOT NULL,
  `phone_number` int(8) NOT NULL,
  `email_address` varchar(45) NOT NULL,
  `payment_amount` int(3) NOT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- insert data in librarymembers
INSERT INTO `librarymembers`(`member_id`, `name`, `faculty`, `phone_number`, `email_address`, `payment_amount`, `payment_date`) VALUES
('A101A', 'Hermione Granger', 'Science', 33336663, 'flying@als.edu', 0, NULL),
('A201B', 'Sherlock Holmes', 'Law', 44327676, 'elementarydrw@als.edu', 0, NULL),
('A301C', 'Tintin', 'Engineering', 14358788, 'luvmilu@als.edu', 0, NULL),
('A401D', 'Prinche Hamlet', 'FASS', 16091609, 'tobeornot@als.edu', 0, NULL),
('A5101E', 'Willy Wonka', 'FASS', 19701970, 'choco1@als.edu', 0, NULL),
('A601F', 'Holly Golightly', 'Business', 55548008, 'diamond@als.edu', 0, NULL),
('A701G', 'Raskolnikov', 'Law', 18661866, 'oneaxe@als.edu', 0, NULL),
('A801H', 'Patrick Bateman', 'Business', 38548544, 'mice@als.edu', 0, NULL),
('A901I', 'Captain Ahab', 'Science', 18511851, 'wwhale@als.edu', 0, NULL);

-- create authors table
DROP TABLE IF EXISTS `authors`;

CREATE TABLE `authors` (
  `accession_no` varchar(13) NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`accession_no`, `name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- insert data into authors
INSERT INTO `authors`(`accession_no`, `name`) VALUES

('A01', 'George Orwell'),
('A02', 'Gabriel Garcia Marquez'),
('A03', 'Aldous Huxley'),
('A04', 'Fyodor Dostoevsky'),
('A05', 'C.S. Lewis'),
('A06', 'Mary Shelley'),
('A07', 'John Steinbeck'),
('A08', 'Mark Twain'),
('A09', 'Charles Dickens'),
('A10', 'Joseph Heller'),
('A11', 'Homer'),
('A12', 'Victor Hugo'),
('A13', 'James Joyce'), 
('A14', 'Vladimir Nabokov'),
('A15', 'Ayn Rand'),
('A16', 'Patrick Suskind'),
('A17', 'Franz Kafka'),
('A18', 'Bret Easton Ellis'),
('A19', 'Rene Goscinny'),
('A19', 'Albert Uderzo'),
('A20', 'Ray Bradbury'),
('A21', 'Isaac Asimov'),
('A22', 'Karl Marx'),
('A22', 'Friedrich Engels'),
('A23', 'Thomas Paine'),
('A24', 'Niccolo Machiavelli'),
('A25', 'Adam Smith'),
('A26', 'Miguel de Cervantes Saavedra'),
('A27', 'Simone de Beauvoir'),
('A28', 'Immanuel Kant'),
('A29', 'Charles Darwin'),
('A30', 'Isaac Newton'),
('A31', 'Milan Kundera'),
('A32', 'Sun Tzu'),
('A33', 'Jorge Luis Borges'), 
('A34', 'Gabriel Garcia Marquez'),
('A35', 'Juan Rulfo'), 
('A36', 'Octavio Paz'),
('A37', 'Pablo Neruda'), 
('A38', 'Richard Feynman'), 
('A39', 'Stephen Hawking'), 
('A40', 'Carl Sagan'), 
('A41', 'Silvanus P. Thompson'),
('A41', 'Martin Gardner'),
('A42', 'Enrico Fermi'), 
('A43', 'Alexander Hamilton'),
('A43', 'James Madison'),
('A43', 'John Jay'),
('A44', 'C. B. Macpherson'),
('A45', 'Karl Popper'),
('A46', 'Howard Zinn'), 
('A47', 'William Golding'),
('A48', 'George Orwell'), 
('A49', 'Ernest Hemingway'), 
('A50', 'Luo Guanzhong');

-- create bookdetails table
DROP TABLE IF EXISTS `librarybooks`;

CREATE TABLE `librarybooks` (
  `accession_no` varchar(3) NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `title` varchar(100) NOT NULL,
  `publisher` varchar(45) NOT NULL,
  `publication_year` int(4) NOT NULL,
  PRIMARY KEY (`accession_no`),
  CONSTRAINT `librarybooks_ibfk_1` FOREIGN KEY (`accession_no`) REFERENCES `authors` (`accession_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- insert data into librarybooks
INSERT INTO `librarybooks`(`accession_no`,`isbn`, `title`, `publisher`, `publication_year`) VALUES

('A01','9790000000001', 'A 1984 Story', 'Intra S.r.l.s.', 2021),
('A02','9790000000002', '100 anos de soledad', 'Vintage Espanol', 2017),
('A03','9790000000003', 'Brave New World', 'Harper Perennial', 2006),
('A04','9790000000004', 'Crime and Punishment', 'Penguin', 2002),
('A05','9790000000005',"The Lion, The Witch and The Wardrobe", 'Harper Collins',2002),
('A06','9790000000006','Frankenstein',"Reader's Library Classics",2021),
('A07','9790000000007','The Grapes of Wrath', 'Penguin Classics',2006),
('A08','9790000000008', 'The Adventures of Huckleberry Finn', 'SeaWolf Press', 2021),
('A09','9790000000009', 'Great Expectations', 'Penguin Classics',2002),
('A10','9790000000010', 'Catch-22', 'Simon & Schuster',2011),
('A11','9790000000011', 'The Iliad', 'Penguin Classics',1998),
('A12','9790000000012', 'Les Miserables', 'Signet',2013),
('A13','9790000000013', 'Ulysses', 'Vintage',1990),
('A14','9790000000014', 'Lolita', 'Vintage',1989),
('A15','9790000000015', 'Atlas Shrugged', 'Dutton',2005),
('A16','9790000000016','Perfume','Vintage',2001),
('A17','9790000000017','The Metamorphosis','12th Media Services',2017),
('A18','9790000000018','American Psycho', 'ROBERT LAFFONT',2019),
('A19','9790000000019', 'Asterix the Gaul','Papercutz',2020),
('A20','9790000000020','Fahrenheit 451','Simon & Schuster',2012),
('A21','9790000000021','Foundation','Bantam Spectra Books',1991),
('A22','9790000000022','The Communist Manifesto','Penguin Classics',2002),
('A23','9790000000023',"Rights of Man, Common Sense, and Other Political Writings",'Oxford University Press',2009),
('A24','9790000000024','The Prince','Independently published',2019),
('A25','9790000000025','The Wealth of Nations','Royal Classics',2021),
('A26','9790000000026','Don Quijote','Ecco',2005),
('A27','9790000000027','The Second Sex','Vintage',2011),
('A28','9790000000028','Critique of Pure Reason','Cambridge University Press',1999),
('A29','9790000000029','On The Origin of Species','Signet',2003),
('A30','9790000000030','Philosophae Naturalis Principia Mathematica','University of California Press',2016),
('A31','9790000000031','The Unbearable Lightness of Being','Harper Perennial Modern Classics',2009),
('A32','9790000000032','The Art of War','LSC Communications',2007),
('A33','9790000000033','Ficciones','Penguin Books',1999),
('A34','9790000000034','El Amor en Los Tiempos del Colera','Vintage',2007),
('A35','9790000000035','Pedro Paramo','Grove Press',1994),
('A36','9790000000036','The Labyrinth of Solitude','Penguin Books',2008),
('A37','9790000000037','Twenty Love Poems and a Song of Despair','Penguin Classics',2006),
('A38','9790000000038','QED: The Strange Theory of Light and Matter','Princeton University Press',2014),
('A39','9790000000039','A Brief History of Time','Bantam',1996),
('A40','9790000000040','Cosmos','Ballantine Books',2013),
('A41','9790000000041','Calculus Made Easy','St Martins Pr',1970),
('A42','9790000000042','Notes on Thermodynamics and Statistics','University of Chicago Press',1988),
('A43','9790000000043','The Federalist','Coventry House Publishing',2015),
('A44','9790000000044','Second Treatise of Government',"Hackett Publishing Company, Inc.",1980),
('A45','9790000000045','The Open Society and Its Enemies','Princeton University Press',2020),
('A46','9790000000046', "A People's History of the United States", 'Harper Perennial Modern Classics',2015),
('A47','9790000000047','Lord of the Flies','Penguin Books',2003),
('A48','9790000000048','Animal farm','Wisehouse Classics',2021),
('A49','9790000000049', 'The Old Man and the Sea', 'Scribner', 1995),
('A50','9790000000050', 'Romance of the Three Kingdoms', 'Penguin Books', 2018);

-- create borrowedbooks table
DROP TABLE IF EXISTS `borrowedbooks`;

CREATE TABLE `borrowedbooks` (
  `accession_no` varchar(3) NOT NULL,
  `member_id` varchar(6) NOT NULL,
  `borrow_date` date NOT NULL,
  PRIMARY KEY (`accession_no`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `borrowedbooks_ibfk_1` FOREIGN KEY (`accession_no`) REFERENCES `librarybooks` (`accession_no`),
  CONSTRAINT `borrowedbooks_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `librarymembers` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- create reservedbooks table
DROP TABLE IF EXISTS `reservedbooks`;

CREATE TABLE `reservedbooks` (
  `accession_no` varchar(3) NOT NULL,
  `member_id` varchar(6) NOT NULL,
  `reserve_date` date NOT NULL,
  PRIMARY KEY (`accession_no`,`member_id`),
  CONSTRAINT `reservedbooks_ibfk_1` FOREIGN KEY (`accession_no`) REFERENCES `librarybooks` (`accession_no`),
  CONSTRAINT `reservedbooks_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `librarymembers` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
