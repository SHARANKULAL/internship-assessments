-- =========================================================================
-- SSMS T-SQL Script to Create Database, Tables with PRIMARY KEYs and Insert Raw DQA Data
-- =========================================================================

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'edtech_dqa')
BEGIN
    CREATE DATABASE [edtech_dqa];
END
GO

USE [edtech_dqa];
GO

IF OBJECT_ID('learners', 'U') IS NOT NULL DROP TABLE [learners];
CREATE TABLE [learners] (
    [learner_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [first_name] VARCHAR(MAX),
    [last_name] VARCHAR(MAX),
    [email] VARCHAR(MAX),
    [date_of_birth] VARCHAR(MAX),
    [enrollment_date] VARCHAR(MAX),
    [cohort_id] VARCHAR(MAX),
    [status] VARCHAR(MAX),
    [phone] VARCHAR(MAX)
);
GO

-- Inserting data into learners
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0001')
    INSERT INTO [learners] VALUES ('L0001', 'Raj', 'Patel', 'raj.patel1@edu.com', '1990-07-24', '2024-01-30', 'C003', 'Active', '+91-7958682846');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0002')
    INSERT INTO [learners] VALUES ('L0002', 'Vikram', 'Bansal', 'vikram.bansal2@edu.com', '1992-04-19', '2023-11-24', 'C006', 'Active', '+91-9536146025');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0003')
    INSERT INTO [learners] VALUES ('L0003', 'Pooja', 'Sharma', NULL, '1990-09-02', '2022-04-06', 'C002', 'Active', '+91-9170484433');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0004')
    INSERT INTO [learners] VALUES ('L0004', 'Nisha', 'Sharma', 'nisha.sharma4@edu.com', '2002-08-03', '2022-07-23', 'C006', 'active', '+91-7946785248');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0005')
    INSERT INTO [learners] VALUES ('L0005', 'Amit', 'Reddy', 'amit.reddy5@edu.com', '1996-03-28', '2024-04-08', 'C007', 'Active', '+91-7685731524');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0006')
    INSERT INTO [learners] VALUES ('L0006', 'Deepak', 'Joshi', 'deepak.joshi6@edu.com', '1997-08-19', '2022-10-12', 'C002', 'Active', '+91-8445662585');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0004')
    INSERT INTO [learners] VALUES ('L0004', 'Sneha', 'Patel', 'sneha.patel7@edu.com', '1998-07-10', '2022-04-10', 'C003', 'active', '+91-9592983555');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0008')
    INSERT INTO [learners] VALUES ('L0008', 'Arjun', 'Malhotra', 'arjun.malhotra8@edu.com', '1990-12-22', '2024-01-18', 'C004', 'Active', '+91-8625792787');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0009')
    INSERT INTO [learners] VALUES ('L0009', 'Rahul', 'Iyer', 'rahul.iyer9@edu.com', '1996-07-29', '2024-04-29', 'C006', 'active', '+91-9479708607');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0010')
    INSERT INTO [learners] VALUES ('L0010', 'Rohan', 'Bansal', 'rohan.bansal10@edu.com', '1991-07-24', '2022-02-16', 'C006', 'Active', '+91-8242911821');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0011')
    INSERT INTO [learners] VALUES ('L0011', 'Rahul', 'Kapoor', 'rahul.kapoor11@edu.com', '1995-03-23', '2022-04-14', 'C004', 'active', '+91-8947382419');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0012')
    INSERT INTO [learners] VALUES ('L0012', 'Raj', 'Kapoor', 'invalidemail.format', '1998-03-08', '2022-06-16', 'C003', 'active', '+91-7899825838');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0013')
    INSERT INTO [learners] VALUES ('L0013', 'Sunita', 'Kumar', 'sunita.kumar13@edu.com', '2005-09-28', '2023-12-01', 'C006', 'Active', '+91-9616197747');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0014')
    INSERT INTO [learners] VALUES ('L0014', 'Raj', 'Gupta', 'raj.gupta14@edu.com', '2001-12-24', '2024-01-17', 'C002', 'Active', '+91-8985392498');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0015')
    INSERT INTO [learners] VALUES ('L0015', 'Suresh', 'Kumar', 'suresh.kumar15@edu.com', '2004-05-09', '2023-12-06', 'C005', 'Active', '+91-9940395823');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0016')
    INSERT INTO [learners] VALUES ('L0016', 'Kiran', 'Kapoor', 'kiran.kapoor16@edu.com', '1991-04-04', '2022-08-23', 'C007', 'Active', '+91-8354860540');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0017')
    INSERT INTO [learners] VALUES ('L0017', 'Suresh', 'Kumar', 'suresh.kumar17@edu.com', '1991-06-27', '2022-08-05', 'C005', 'active', '+91-7913224047');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0018')
    INSERT INTO [learners] VALUES ('L0018', 'Raj', 'Nair', 'raj.nair18@edu.com', '2030-05-12', '2023-10-21', 'C004', 'Active', '+91-8137651678');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0019')
    INSERT INTO [learners] VALUES ('L0019', 'Vikram', 'Singh', 'vikram.singh19@edu.com', '2002-08-04', '2023-07-06', 'C003', 'active', '+91-9506254832');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0020')
    INSERT INTO [learners] VALUES ('L0020', 'Suresh', 'Mehta', 'suresh.mehta20@edu.com', '1994-12-02', '2022-05-22', 'C005', 'active', '+91-7390452952');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0021')
    INSERT INTO [learners] VALUES ('L0021', 'Manoj', 'Sharma', 'manoj.sharma21@edu.com', '1992-06-17', '2022-06-06', 'C006', 'Active', '+91-9922644564');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0022')
    INSERT INTO [learners] VALUES ('L0022', NULL, 'Reddy', 'pooja.reddy22@edu.com', '1991-06-05', '2023-01-30', 'C004', 'active', '+91-9272528809');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0023')
    INSERT INTO [learners] VALUES ('L0023', 'Arjun', 'Iyer', 'arjun.iyer23@edu.com', '1990-04-05', '2023-11-28', 'C006', 'Active', '+91-9927923735');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0024')
    INSERT INTO [learners] VALUES ('L0024', 'Prakash', 'Iyer', 'prakash.iyer24@edu.com', '1995-12-26', '2024-02-27', 'C006', 'active', '+91-7479112937');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0025')
    INSERT INTO [learners] VALUES ('L0025', 'Divya', 'Joshi', 'divya.joshi25@edu.com', '1993-07-19', '2023-04-10', 'C001', 'active', '+91-9150000991');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0026')
    INSERT INTO [learners] VALUES ('L0026', 'Manoj', 'Gupta', 'manoj.gupta26@edu.com', '2001-05-21', '2022-04-19', 'C007', 'active', '+91-9744267175');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0027')
    INSERT INTO [learners] VALUES ('L0027', 'Sanjay', 'Reddy', 'sanjay.reddy27@edu.com', '1994-06-18', '2022-06-06', 'C003', 'Active', '+91-9316615266');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0028')
    INSERT INTO [learners] VALUES ('L0028', 'Manoj', 'Pandey', 'manoj.pandey28@edu.com', '2001-11-23', '2022-01-01', 'C005', 'active', '+91-9098545541');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0029')
    INSERT INTO [learners] VALUES ('L0029', 'Aarav', 'Patel', 'aarav.patel29@edu.com', '1998-02-21', '2024-05-01', 'C007', 'active', '+91-8028439863');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0030')
    INSERT INTO [learners] VALUES ('L0030', 'Priya', 'Singh', 'priya.singh30@edu.com', '2002-09-22', '2022-03-22', 'C001', 'ACTIVE', '+91-7297265480');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0031')
    INSERT INTO [learners] VALUES ('L0031', 'Manoj', 'Iyer', 'manoj.iyer31@edu.com', '1992-10-27', '2022-05-12', 'C006', 'active', '+91-9361388464');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0032')
    INSERT INTO [learners] VALUES ('L0032', 'Ananya', 'Kumar', 'ananya.kumar32@edu.com', '2001-11-01', '2023-09-14', 'C004', 'Active', '+91-9316259067');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0033')
    INSERT INTO [learners] VALUES ('L0033', 'Manoj', 'Bansal', 'manoj.bansal33@edu.com', '2005-06-22', '2022-07-25', 'C006', 'active', '+91-8713658874');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0034')
    INSERT INTO [learners] VALUES ('L0034', 'Sunita', 'Verma', 'sunita.verma34@edu.com', '1998-05-18', '2023-03-25', 'C005', 'active', '+91-7519709079');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0015')
    INSERT INTO [learners] VALUES ('L0015', 'Suresh', 'Kumar', 'suresh.kumar15@edu.com', '2004-05-09', '2023-12-06', 'C005', 'Active', '+91-9940395823');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0036')
    INSERT INTO [learners] VALUES ('L0036', 'Neha', 'Sharma', 'neha.sharma36@edu.com', '1991-08-05', '2023-12-26', 'C006', 'Active', '+91-7983297492');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0037')
    INSERT INTO [learners] VALUES ('L0037', 'Rahul', 'Pandey', 'rahul.pandey37@edu.com', '1990-09-15', '2024-05-30', 'C003', 'Active', '+91-9208283728');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0038')
    INSERT INTO [learners] VALUES ('L0038', 'Neha', 'Kumar', 'neha.kumar38@edu.com', '2005-01-02', '2023-05-13', 'C002', 'Active', '+91-9452611418');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0039')
    INSERT INTO [learners] VALUES ('L0039', 'Ajay', 'Nair', 'ajay.nair39@edu.com', '1995-06-14', '2024-03-14', 'C004', 'active', '+91-7817804383');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0040')
    INSERT INTO [learners] VALUES ('L0040', 'Sneha', 'Patel', 'sneha.patel40@edu.com', '2004-10-12', '2023-03-18', 'C003', 'active', 'CALL-ME');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0041')
    INSERT INTO [learners] VALUES ('L0041', 'Amit', 'Kapoor', 'amit.kapoor41@edu.com', '1991-03-20', '2023-11-21', 'C006', 'Active', '+91-7260329455');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0042')
    INSERT INTO [learners] VALUES ('L0042', 'Suresh', 'Bansal', 'suresh.bansal42@edu.com', '1997-08-11', '2024-03-30', 'C007', 'Active', '+91-8067970820');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0043')
    INSERT INTO [learners] VALUES ('L0043', 'Rohan', 'Singh', 'rohan.singh43@edu.com', '2002-01-11', '2023-04-05', 'C002', 'active', '+91-7788075126');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0044')
    INSERT INTO [learners] VALUES ('L0044', 'Arjun', 'Nair', 'arjun.nair44@edu.com', '1995-08-09', '2022-03-19', 'C004', 'Active', '+91-7217275224');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0045')
    INSERT INTO [learners] VALUES ('L0045', 'Raj', 'Iyer', 'raj.iyer45@edu.com', '1990-05-01', '2019-03-01', 'C007', 'Active', '+91-7714300770');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0046')
    INSERT INTO [learners] VALUES ('L0046', 'Pooja', 'Nair', 'pooja.nair46@edu.com', '2000-10-18', '2022-08-07', 'C007', 'active', '+91-7251837136');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0047')
    INSERT INTO [learners] VALUES ('L0047', 'Ananya', 'Joshi', 'ananya.joshi47@edu.com', '1990-01-18', '2023-02-04', 'C003', 'active', '+91-8225136114');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0048')
    INSERT INTO [learners] VALUES ('L0048', 'Pooja', 'Bansal', 'deepak.joshi6@edu.com', '2002-06-19', '2023-11-09', 'C006', 'active', '+91-7664847319');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0049')
    INSERT INTO [learners] VALUES ('L0049', 'Rohan', 'Kumar', 'rohan.kumar49@edu.com', '1994-11-19', '2022-03-01', 'C005', 'Active', '+91-8346922426');
IF NOT EXISTS (SELECT 1 FROM [learners] WHERE [learner_id] = 'L0050')
    INSERT INTO [learners] VALUES ('L0050', 'Priya', 'Sharma', 'priya.sharma50@edu.com', '2003-02-07', '2023-05-04', 'C005', 'Active', '+91-7244295904');
GO

IF OBJECT_ID('courses', 'U') IS NOT NULL DROP TABLE [courses];
CREATE TABLE [courses] (
    [course_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [course_title] VARCHAR(MAX),
    [category] VARCHAR(MAX),
    [instructor_id] VARCHAR(MAX),
    [duration_hours] VARCHAR(MAX),
    [start_date] VARCHAR(MAX),
    [end_date] VARCHAR(MAX),
    [status] VARCHAR(MAX),
    [price] VARCHAR(MAX)
);
GO

-- Inserting data into courses
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0001')
    INSERT INTO [courses] VALUES ('CRS0001', 'Course in Marketing - Level 1', 'Web Dev', 'I002', '96', '2022-03-11', '2022-06-09', 'published', '2077.98');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0002')
    INSERT INTO [courses] VALUES ('CRS0002', 'Course in Marketing - Level 1', 'Marketing', 'I010', '25', '2022-03-25', '2022-08-09', 'Draft', '6252.05');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0003')
    INSERT INTO [courses] VALUES ('CRS0003', 'Course in Marketing - Level 2', 'Business', 'I004', '105', '2022-11-18', '2023-02-17', 'published', '4561.07');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0004')
    INSERT INTO [courses] VALUES ('CRS0004', 'Course in Cloud - Level 3', 'Business', 'I008', '60', '2022-03-16', '2022-04-17', 'published', '6589.43');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0005')
    INSERT INTO [courses] VALUES ('CRS0005', NULL, 'Data Science', 'I009', '47', '2022-09-29', '2022-12-01', 'published', '8926.78');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0006')
    INSERT INTO [courses] VALUES ('CRS0006', 'Course in Web Dev - Level 2', 'Business', 'I003', '76', '2022-11-06', '2023-04-20', 'Published', '7009.77');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0007')
    INSERT INTO [courses] VALUES ('CRS0007', 'Course in Marketing - Level 2', 'Cloud', 'I002', '37', '2022-09-28', '2022-11-26', 'Published', '7680.75');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0008')
    INSERT INTO [courses] VALUES ('CRS0008', 'Course in Web Dev - Level 2', 'Business', 'I010', '-5', '2022-12-18', '2023-03-10', 'Draft', '6707.14');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0009')
    INSERT INTO [courses] VALUES ('CRS0009', 'Course in Business - Level 3', 'Design', 'I005', '26', '2022-04-05', '2022-08-21', 'published', '1395.78');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0010')
    INSERT INTO [courses] VALUES ('CRS0010', 'Course in Business - Level 1', 'Cloud', 'I005', '40', '2023-03-29', '2023-09-16', 'Draft', '4848.18');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0011')
    INSERT INTO [courses] VALUES ('CRS0011', 'Course in Data Science - Level 1', 'Data Science', 'I003', '89', '2022-02-06', '2021-01-01', 'Draft', '5971.73');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0012')
    INSERT INTO [courses] VALUES ('CRS0012', 'Course in Design - Level 1', 'Data Science', 'I005', '66', '2022-02-10', '2022-06-11', 'Published', '7137.6');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0013')
    INSERT INTO [courses] VALUES ('CRS0013', 'Course in Cloud - Level 1', 'Business', 'I009', '72', '2022-06-08', '2022-09-06', 'Published', '9784.85');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0014')
    INSERT INTO [courses] VALUES ('CRS0014', 'Course in Web Dev - Level 2', 'Data Science', NULL, '114', '2022-12-07', '2023-04-21', 'Draft', '8775.58');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0015')
    INSERT INTO [courses] VALUES ('CRS0015', 'Course in Web Dev - Level 2', 'Web Dev', 'I002', '68', '2022-02-09', '2022-07-09', 'Published', '2795.16');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0016')
    INSERT INTO [courses] VALUES ('CRS0016', 'Course in Design - Level 2', 'Business', 'I004', '48', '2022-01-25', '2022-04-14', 'published', '3953.36');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0017')
    INSERT INTO [courses] VALUES ('CRS0017', 'Course in Data Science - Level 2', 'Business', 'I009', '71', '2022-12-06', '2023-01-12', 'Published', '-100.0');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0018')
    INSERT INTO [courses] VALUES ('CRS0018', 'Course in Business - Level 1', 'Marketing', 'I005', '24', '2022-04-22', '2022-09-10', 'published', '7555.91');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0019')
    INSERT INTO [courses] VALUES ('CRS0019', 'Course in Business - Level 2', 'Marketing', 'I009', '34', '2023-01-30', '2023-07-26', 'publihsed', '3291.5');
IF NOT EXISTS (SELECT 1 FROM [courses] WHERE [course_id] = 'CRS0020')
    INSERT INTO [courses] VALUES ('CRS0020', 'Course in Cloud - Level 2', 'Data Science', 'I009', '0', '2022-07-21', '2022-11-21', 'published', '1628.76');
GO

IF OBJECT_ID('assessments', 'U') IS NOT NULL DROP TABLE [assessments];
CREATE TABLE [assessments] (
    [assessment_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [course_id] VARCHAR(MAX),
    [assessment_type] VARCHAR(MAX),
    [max_score] VARCHAR(MAX),
    [passing_score] VARCHAR(MAX),
    [due_date] VARCHAR(MAX),
    [created_date] VARCHAR(MAX)
);
GO

-- Inserting data into assessments
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0001')
    INSERT INTO [assessments] VALUES ('ASS0001', 'CRS0015', 'Project', '100', '50', '2022-11-05', '2022-10-06');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0002')
    INSERT INTO [assessments] VALUES ('ASS0002', 'CRS0006', 'Final Exam', '100', '50', '2023-08-10', '2023-07-24');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0003')
    INSERT INTO [assessments] VALUES ('ASS0003', 'CRS0009', 'Project', '50', '25', '2023-01-03', '2022-12-14');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0004')
    INSERT INTO [assessments] VALUES ('ASS0004', 'CRS0015', 'Midterm', '50', '25', '2023-04-24', '2023-04-05');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0005')
    INSERT INTO [assessments] VALUES ('ASS0005', 'CRS0012', 'Quiz', '100', '50', '2023-04-03', '2023-03-21');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0006')
    INSERT INTO [assessments] VALUES ('ASS0006', 'CRS0009', 'Final Exam', '0', '50', '2023-10-11', '2023-09-20');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0007')
    INSERT INTO [assessments] VALUES ('ASS0007', 'CRS0010', 'Assignment', '100', '50', '2022-12-19', '2022-11-21');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0008')
    INSERT INTO [assessments] VALUES ('ASS0008', 'CRS0002', 'Project', '100', '50', '2022-09-18', '2022-09-04');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0009')
    INSERT INTO [assessments] VALUES ('ASS0009', 'CRS0015', 'Project', '50', '25', '2023-01-01', '2022-12-21');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0010')
    INSERT INTO [assessments] VALUES ('ASS0010', 'CRS0001', 'Quiz', '50', '60', '2023-10-26', '2023-09-30');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0011')
    INSERT INTO [assessments] VALUES ('ASS0011', 'CRS0018', 'Quiz', '100', '50', '2023-08-26', '2023-07-30');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0012')
    INSERT INTO [assessments] VALUES ('ASS0012', 'CRS0013', 'Assignment', '100', '50', '2023-11-08', '2023-10-20');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0013')
    INSERT INTO [assessments] VALUES ('ASS0013', 'CRS0004', 'Assignment', '50', '25', '2022-10-08', '2022-09-18');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0014')
    INSERT INTO [assessments] VALUES ('ASS0014', 'CRS0004', 'Assignment', '100', '50', '2021-01-01', '2022-07-22');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0015')
    INSERT INTO [assessments] VALUES ('ASS0015', 'CRS0004', 'Quiz', '100', '50', '2022-11-05', '2022-10-15');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0016')
    INSERT INTO [assessments] VALUES ('ASS0016', 'CRS0015', 'Final Exam', '100', '50', '2023-09-23', '2023-08-28');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0017')
    INSERT INTO [assessments] VALUES ('ASS0017', 'CRS0016', 'Final Exam', '100', '50', '2023-09-12', '2023-08-31');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0018')
    INSERT INTO [assessments] VALUES ('ASS0018', 'CRS0016', NULL, '100', '50', '2023-03-07', '2023-02-21');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0019')
    INSERT INTO [assessments] VALUES ('ASS0019', 'CRS0015', 'Project', '100', '50', '2023-02-15', '2023-01-31');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0020')
    INSERT INTO [assessments] VALUES ('ASS0020', 'CRS0010', 'Quiz', '100', '50', '2023-02-11', '2023-01-27');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0021')
    INSERT INTO [assessments] VALUES ('ASS0021', 'CRS0007', 'Project', '50', '25', '2022-10-31', '2022-10-20');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0022')
    INSERT INTO [assessments] VALUES ('ASS0022', 'CRS9999', 'Midterm', '50', '25', '2023-01-15', '2023-01-06');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0023')
    INSERT INTO [assessments] VALUES ('ASS0023', 'CRS0009', 'Midterm', '100', '50', '2023-10-11', '2023-09-21');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0024')
    INSERT INTO [assessments] VALUES ('ASS0024', 'CRS0001', 'Assignment', '100', '50', '2023-07-29', '2023-07-04');
IF NOT EXISTS (SELECT 1 FROM [assessments] WHERE [assessment_id] = 'ASS0011')
    INSERT INTO [assessments] VALUES ('ASS0011', 'CRS0016', 'Quiz', '100', '50', '2023-10-09', '2023-10-02');
GO

IF OBJECT_ID('course_enrollments', 'U') IS NOT NULL DROP TABLE [course_enrollments];
CREATE TABLE [course_enrollments] (
    [enrollment_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [learner_id] VARCHAR(MAX),
    [course_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [enrollment_date] VARCHAR(MAX),
    [completion_date] VARCHAR(MAX),
    [grade] VARCHAR(MAX),
    [status] VARCHAR(MAX)
);
GO

-- Inserting data into course_enrollments
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0001', 'L0024', 'CRS0006', '2023-04-04', '2023-09-20', '97', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0016')
    INSERT INTO [course_enrollments] VALUES ('ENR0002', 'L0037', 'CRS0016', '2023-09-11', '2024-02-20', '78', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0004')
    INSERT INTO [course_enrollments] VALUES ('ENR0003', 'L0033', 'CRS0004', '2022-12-05', '2023-03-30', '71', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0007')
    INSERT INTO [course_enrollments] VALUES ('ENR0004', 'L9999', 'CRS0007', '2023-04-19', '2023-09-18', '50', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0013')
    INSERT INTO [course_enrollments] VALUES ('ENR0005', 'L0010', 'CRS0013', '2023-08-29', '2023-10-31', '98', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0013')
    INSERT INTO [course_enrollments] VALUES ('ENR0006', 'L0040', 'CRS0013', '2022-03-28', '2022-06-06', '81', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0007', 'L0010', 'CRS0010', '2022-09-03', '2022-11-08', '56', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0004')
    INSERT INTO [course_enrollments] VALUES ('ENR0008', 'L0022', 'CRS0004', '2023-06-09', '2023-09-18', '61', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS9998')
    INSERT INTO [course_enrollments] VALUES ('ENR0009', 'L0019', 'CRS9998', '2023-05-06', '2023-08-06', '93', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0001')
    INSERT INTO [course_enrollments] VALUES ('ENR0010', 'L0032', 'CRS0001', '2023-09-04', '2023-11-09', '100', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0015')
    INSERT INTO [course_enrollments] VALUES ('ENR0011', 'L0016', 'CRS0015', '2022-05-10', '2022-10-16', '81', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0004')
    INSERT INTO [course_enrollments] VALUES ('ENR0012', 'L0002', 'CRS0004', '2022-09-21', '2023-03-07', '41', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0004')
    INSERT INTO [course_enrollments] VALUES ('ENR0013', 'L0011', 'CRS0004', '2022-07-08', '2022-11-05', '82', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0004')
    INSERT INTO [course_enrollments] VALUES ('ENR0014', 'L0039', 'CRS0004', '2023-06-20', '2023-11-16', '56', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0013')
    INSERT INTO [course_enrollments] VALUES ('ENR0015', 'L0012', 'CRS0013', '2023-11-12', '2020-01-01', '85', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0016', 'L0012', 'CRS0006', '2022-06-19', '2022-10-31', '41', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0015')
    INSERT INTO [course_enrollments] VALUES ('ENR0017', 'L0039', 'CRS0015', '2023-03-20', '2023-07-08', '100', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0018', 'L0014', 'CRS0002', '2023-10-28', '2024-03-24', '93', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0019', 'L0017', 'CRS0002', '2023-01-03', '2023-06-20', '83', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0018')
    INSERT INTO [course_enrollments] VALUES ('ENR0006', 'L0009', 'CRS0018', '2023-10-01', '2024-03-09', '42', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0009')
    INSERT INTO [course_enrollments] VALUES ('ENR0021', 'L0037', 'CRS0009', '2023-03-15', '2023-05-22', '72', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0001')
    INSERT INTO [course_enrollments] VALUES ('ENR0022', 'L0023', 'CRS0001', '2023-05-05', '2023-10-17', '71', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0007')
    INSERT INTO [course_enrollments] VALUES ('ENR0023', 'L0029', 'CRS0007', '2023-12-11', '2024-06-02', '93', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0003')
    INSERT INTO [course_enrollments] VALUES ('ENR0024', 'L0048', 'CRS0003', '2023-05-20', '2023-08-10', '86', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0025', 'L0044', 'CRS0006', '2023-11-21', '2024-05-02', '150', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0026', 'L0032', 'CRS0010', '2023-05-21', '2023-11-02', '86', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0007')
    INSERT INTO [course_enrollments] VALUES ('ENR0027', 'L0019', 'CRS0007', '2022-11-07', '2023-04-22', '99', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0028', 'L0019', 'CRS0010', '2022-11-05', '2023-04-10', '69', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0015')
    INSERT INTO [course_enrollments] VALUES ('ENR0029', 'L0042', 'CRS0015', '2023-03-24', '2023-07-05', '41', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0003')
    INSERT INTO [course_enrollments] VALUES ('ENR0030', 'L0022', 'CRS0003', '2023-07-13', '2023-10-08', '62', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0031', 'L0023', 'CRS0006', NULL, '2024-03-29', '96', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0001')
    INSERT INTO [course_enrollments] VALUES ('ENR0032', 'L0038', 'CRS0001', '2023-08-12', '2023-11-04', '45', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0009')
    INSERT INTO [course_enrollments] VALUES ('ENR0033', 'L0049', 'CRS0009', '2023-07-14', '2023-11-22', '88', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0034', 'L0047', 'CRS0010', '2023-12-22', '2024-05-21', '71', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0035', 'L0002', 'CRS0002', '2022-12-27', '2023-03-25', '65', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0036', 'L0017', 'CRS0006', '2023-10-17', '2024-02-01', '70', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0007')
    INSERT INTO [course_enrollments] VALUES ('ENR0037', 'L0036', 'CRS0007', '2023-05-10', '2023-10-12', '75', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0016')
    INSERT INTO [course_enrollments] VALUES ('ENR0038', 'L0024', 'CRS0016', '2023-06-08', '2023-09-10', '59', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0039', 'L0016', 'CRS0002', '2022-09-14', '2022-12-23', '47', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0018')
    INSERT INTO [course_enrollments] VALUES ('ENR0040', 'L0037', 'CRS0018', '2022-09-06', '2022-11-29', '53', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0041', 'L0032', 'CRS0006', '2023-10-25', '2024-03-30', '73', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0042', 'L0020', 'CRS0002', '2022-09-15', '2022-12-21', '54', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0043', 'L0013', 'CRS0006', '2022-03-15', '2022-08-12', '74', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0001')
    INSERT INTO [course_enrollments] VALUES ('ENR0044', 'L0019', 'CRS0001', '2022-04-25', '2022-09-02', '58', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0015')
    INSERT INTO [course_enrollments] VALUES ('ENR0045', 'L0010', 'CRS0015', '2023-07-16', '2023-09-27', '95', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0046', 'L0039', 'CRS0006', '2023-06-24', '2023-10-23', '-5', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0001')
    INSERT INTO [course_enrollments] VALUES ('ENR0047', 'L0013', 'CRS0001', '2022-11-14', '2023-05-13', '95', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0048', 'L0009', 'CRS0002', '2023-04-15', '2023-08-15', '44', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0015')
    INSERT INTO [course_enrollments] VALUES ('ENR0049', 'L0043', 'CRS0015', '2022-04-24', '2022-07-12', '49', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0050', 'L0021', 'CRS0002', '2022-11-10', '2023-01-24', '75', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0013')
    INSERT INTO [course_enrollments] VALUES ('ENR0051', 'L0041', 'CRS0013', '2023-11-24', '2024-02-20', '89', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0052', 'L0026', 'CRS0010', '2023-05-28', '2023-09-03', '95', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0053', 'L0029', 'CRS0006', '2023-10-04', '2024-02-20', '43', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0054', 'L0050', 'CRS0002', '2022-09-29', '2023-02-16', '53', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0055', 'L0045', 'CRS0002', '2022-08-08', '2022-11-06', '51', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0003')
    INSERT INTO [course_enrollments] VALUES ('ENR0056', 'L0005', 'CRS0003', '2022-03-03', '2022-06-23', '68', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0057', 'L0041', 'CRS0010', '2022-12-24', '2023-02-26', '54', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0058', 'L0048', 'CRS0006', '2023-06-08', '2023-08-16', '83', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0018')
    INSERT INTO [course_enrollments] VALUES ('ENR0059', 'L0018', 'CRS0018', '2023-12-01', '2024-04-14', '82', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0002')
    INSERT INTO [course_enrollments] VALUES ('ENR0060', 'L0029', 'CRS0002', '2023-09-09', '2023-12-06', '81', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0009')
    INSERT INTO [course_enrollments] VALUES ('ENR0021', 'L0037', 'CRS0009', '2023-03-15', '2023-05-22', '72', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0016')
    INSERT INTO [course_enrollments] VALUES ('ENR0062', 'L0041', 'CRS0016', '2023-10-04', '2024-03-29', '58', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0063', 'L0009', 'CRS0010', '2023-01-06', '2023-06-04', '65', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0012')
    INSERT INTO [course_enrollments] VALUES ('ENR0064', 'L0034', 'CRS0012', '2023-07-19', '2023-11-12', '45', 'Dropped');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0009')
    INSERT INTO [course_enrollments] VALUES ('ENR0065', 'L0003', 'CRS0009', '2023-01-25', '2023-06-11', '56', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0004')
    INSERT INTO [course_enrollments] VALUES ('ENR0066', 'L0006', 'CRS0004', '2023-10-11', '2024-02-23', '100', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0006')
    INSERT INTO [course_enrollments] VALUES ('ENR0067', 'L0046', 'CRS0006', '2023-10-12', '2023-12-16', '88', 'Enrolled');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0012')
    INSERT INTO [course_enrollments] VALUES ('ENR0068', 'L0032', 'CRS0012', '2023-12-28', '2024-04-22', '98', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0013')
    INSERT INTO [course_enrollments] VALUES ('ENR0069', 'L0013', 'CRS0013', '2023-05-21', '2023-10-09', '92', 'Completed');
IF NOT EXISTS (SELECT 1 FROM [course_enrollments] WHERE [course_id] = 'CRS0010')
    INSERT INTO [course_enrollments] VALUES ('ENR0070', 'L0006', 'CRS0010', '2023-02-20', '2023-06-12', '61', 'Completed');
GO

IF OBJECT_ID('transactions', 'U') IS NOT NULL DROP TABLE [transactions];
CREATE TABLE [transactions] (
    [transaction_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [learner_id] VARCHAR(MAX),
    [course_id] VARCHAR(MAX),
    [amount] VARCHAR(MAX),
    [payment_method] VARCHAR(MAX),
    [transaction_date] VARCHAR(MAX),
    [status] VARCHAR(MAX),
    [currency] VARCHAR(MAX)
);
GO

-- Inserting data into transactions
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00001')
    INSERT INTO [transactions] VALUES ('TXN00001', 'L0045', 'CRS0002', '8718.6', 'UPI', '2023-02-26', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00002')
    INSERT INTO [transactions] VALUES ('TXN00002', 'L0033', 'CRS0006', '6962.25', 'Net Banking', '2024-02-18', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00003')
    INSERT INTO [transactions] VALUES ('TXN00003', 'L0003', 'CRS0010', '1791.54', 'UPI', '2022-11-28', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00004')
    INSERT INTO [transactions] VALUES ('TXN00004', 'L0027', 'CRS0012', '8423.34', 'Credit Card', '2023-11-05', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00005')
    INSERT INTO [transactions] VALUES ('TXN00005', 'L0031', 'CRS0009', '-500.0', 'Wallet', '2023-01-06', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00006')
    INSERT INTO [transactions] VALUES ('TXN00006', 'L0033', 'CRS0015', '4977.37', 'Credit Card', '2022-07-28', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00007')
    INSERT INTO [transactions] VALUES ('TXN00007', 'L0038', 'CRS0003', '9348.05', 'Net Banking', '2023-12-17', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00008')
    INSERT INTO [transactions] VALUES ('TXN00008', 'L0009', 'CRS0001', '9757.32', 'Wallet', '2022-09-03', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00009')
    INSERT INTO [transactions] VALUES ('TXN00009', 'L0012', 'CRS0006', '5956.55', 'Wallet', '2023-02-22', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00003')
    INSERT INTO [transactions] VALUES ('TXN00003', 'L0016', 'CRS0002', '5152.03', 'Credit Card', '2023-10-26', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00011')
    INSERT INTO [transactions] VALUES ('TXN00011', 'L0033', 'CRS0016', '3625.75', 'UPI', '2023-03-02', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00012')
    INSERT INTO [transactions] VALUES ('TXN00012', 'L0032', 'CRS0004', '5110.08', 'Debit Card', '2023-01-28', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00013')
    INSERT INTO [transactions] VALUES ('TXN00013', 'L0041', 'CRS0012', '7715.63', 'Debit Card', '2022-03-13', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00014')
    INSERT INTO [transactions] VALUES ('TXN00014', 'L0028', 'CRS0007', '9407.24', 'Wallet', '2022-10-01', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00015')
    INSERT INTO [transactions] VALUES ('TXN00015', 'L0020', 'CRS0016', '3686.0', 'Wallet', '2023-08-17', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00016')
    INSERT INTO [transactions] VALUES ('TXN00016', 'L0033', 'CRS0003', '5017.93', NULL, '2022-12-20', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00017')
    INSERT INTO [transactions] VALUES ('TXN00017', 'L0038', 'CRS0018', '5889.87', 'Net Banking', '2022-11-26', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00018')
    INSERT INTO [transactions] VALUES ('TXN00018', 'L0047', 'CRS0004', '6145.18', 'Debit Card', '2023-02-25', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00019')
    INSERT INTO [transactions] VALUES ('TXN00019', 'L0022', 'CRS0016', '5255.79', 'Net Banking', '2023-01-31', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00020')
    INSERT INTO [transactions] VALUES ('TXN00020', 'L0044', 'CRS0003', '5456.96', 'Credit Card', '2022-05-10', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00021')
    INSERT INTO [transactions] VALUES ('TXN00021', 'L0040', 'CRS0007', '8826.3', 'Net Banking', '2022-04-13', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00022')
    INSERT INTO [transactions] VALUES ('TXN00022', 'L9997', 'CRS0001', '7500.99', 'Net Banking', '2023-11-02', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00023')
    INSERT INTO [transactions] VALUES ('TXN00023', 'L0005', 'CRS0010', '8032.73', 'UPI', '2022-12-13', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00024')
    INSERT INTO [transactions] VALUES ('TXN00024', 'L0047', 'CRS0009', '6847.53', 'UPI', '2023-11-22', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00025')
    INSERT INTO [transactions] VALUES ('TXN00025', 'L0026', 'CRS0007', '6640.19', 'Net Banking', '2023-07-09', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00026')
    INSERT INTO [transactions] VALUES ('TXN00026', 'L0042', 'CRS0002', '3111.93', 'UPI', '2022-08-21', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00027')
    INSERT INTO [transactions] VALUES ('TXN00027', 'L0006', 'CRS0009', '9804.04', 'Credit Card', '2023-03-31', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00028')
    INSERT INTO [transactions] VALUES ('TXN00028', 'L0047', 'CRS0006', '9129.82', 'Credit Card', '2022-11-29', 'COMPELTED', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00029')
    INSERT INTO [transactions] VALUES ('TXN00029', 'L0020', 'CRS0007', '4372.57', 'Debit Card', '2022-09-08', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00030')
    INSERT INTO [transactions] VALUES ('TXN00030', 'L0028', 'CRS0013', '7135.2', 'Debit Card', '2022-06-24', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00031')
    INSERT INTO [transactions] VALUES ('TXN00031', 'L0006', 'CRS0013', '8836.56', 'Wallet', '2023-12-01', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00032')
    INSERT INTO [transactions] VALUES ('TXN00032', 'L0033', 'CRS0013', '2287.06', 'Net Banking', '2023-10-16', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00033')
    INSERT INTO [transactions] VALUES ('TXN00033', 'L0031', 'CRS0006', '7000.57', 'Net Banking', NULL, 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00034')
    INSERT INTO [transactions] VALUES ('TXN00034', 'L0037', 'CRS0003', '1663.76', 'UPI', '2023-08-25', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00035')
    INSERT INTO [transactions] VALUES ('TXN00035', 'L0043', 'CRS0009', '7211.82', 'Net Banking', '2022-11-06', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00036')
    INSERT INTO [transactions] VALUES ('TXN00036', 'L0026', 'CRS0010', '1958.88', 'Net Banking', '2023-08-09', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00037')
    INSERT INTO [transactions] VALUES ('TXN00037', 'L0039', 'CRS0006', '9933.23', 'UPI', '2022-01-23', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00038')
    INSERT INTO [transactions] VALUES ('TXN00038', 'L0027', 'CRS0006', '1071.88', 'Credit Card', '2023-09-13', 'Refunded', 'us');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00039')
    INSERT INTO [transactions] VALUES ('TXN00039', 'L0033', 'CRS0006', '7980.67', 'Debit Card', '2023-09-14', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00040')
    INSERT INTO [transactions] VALUES ('TXN00040', 'L0016', 'CRS0015', '2710.19', 'UPI', '2023-11-26', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00041')
    INSERT INTO [transactions] VALUES ('TXN00041', 'L0045', 'CRS0015', '8544.03', 'Credit Card', '2023-10-05', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00042')
    INSERT INTO [transactions] VALUES ('TXN00042', 'L0003', 'CRS0006', '8096.49', 'Credit Card', '2023-08-17', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00043')
    INSERT INTO [transactions] VALUES ('TXN00043', 'L0049', 'CRS0003', '1810.2', 'UPI', '2022-12-01', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00044')
    INSERT INTO [transactions] VALUES ('TXN00044', 'L0028', 'CRS0003', '2806.15', 'Wallet', '2023-01-10', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00045')
    INSERT INTO [transactions] VALUES ('TXN00045', 'L0034', 'CRS0006', '0.0', 'UPI', '2023-05-09', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00046')
    INSERT INTO [transactions] VALUES ('TXN00046', 'L0050', 'CRS0007', '8237.09', 'Net Banking', '2022-03-19', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00047')
    INSERT INTO [transactions] VALUES ('TXN00047', 'L0016', 'CRS0015', '7516.95', 'Net Banking', '2023-07-25', 'Failed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00048')
    INSERT INTO [transactions] VALUES ('TXN00048', 'L0006', 'CRS0018', '4550.17', 'UPI', '2023-07-04', 'Completed', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00004')
    INSERT INTO [transactions] VALUES ('TXN00004', 'L0027', 'CRS0012', '8423.34', 'Credit Card', '2023-11-05', 'Refunded', 'INR');
IF NOT EXISTS (SELECT 1 FROM [transactions] WHERE [transaction_id] = 'TXN00050')
    INSERT INTO [transactions] VALUES ('TXN00050', 'L0043', 'CRS0007', '9999999.0', 'Debit Card', '2023-04-28', 'Completed', 'INR');
GO

IF OBJECT_ID('academic_calendar', 'U') IS NOT NULL DROP TABLE [academic_calendar];
CREATE TABLE [academic_calendar] (
    [calendar_id] VARCHAR(255) NOT NULL PRIMARY KEY,
    [term_name] VARCHAR(MAX),
    [academic_year] VARCHAR(MAX),
    [start_date] VARCHAR(MAX),
    [end_date] VARCHAR(MAX),
    [is_active] VARCHAR(MAX),
    [holidays] VARCHAR(MAX)
);
GO

-- Inserting data into academic_calendar
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL001')
    INSERT INTO [academic_calendar] VALUES ('CAL001', 'Semester 1 - 2022', '2021-2022', '2022-01-10', '2022-05-31', 'Yes', '2022-01-26,2022-04-15');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL002')
    INSERT INTO [academic_calendar] VALUES ('CAL002', 'Semester 2 - 2022', '2021-2022', '2022-07-01', '2022-11-30', 'No', '2022-08-15,2022-10-02');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL003')
    INSERT INTO [academic_calendar] VALUES ('CAL003', 'Semester 1 - 2023', '2022-2023', '2023-06-15', '2023-01-10', 'No', '2023-01-26');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL004')
    INSERT INTO [academic_calendar] VALUES ('CAL004', 'Semester 2 - 2023', '2022-2023', '2023-07-01', '2023-11-30', 'Yes', '2023-08-15');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL005')
    INSERT INTO [academic_calendar] VALUES ('CAL005', 'Semester 1 - 2024', '2023-2024', '2023-10-15', '2024-03-31', 'Yes', '2024-01-26');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL006')
    INSERT INTO [academic_calendar] VALUES ('CAL006', 'Semester 2 - 2024', '2023-2024', '2024-07-01', '2024-11-30', 'No', '2024-08-15');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL007')
    INSERT INTO [academic_calendar] VALUES ('CAL007', NULL, '2024-2025', '2025-01-10', '2025-05-31', 'Yes', '2025-01-26');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL001')
    INSERT INTO [academic_calendar] VALUES ('CAL001', 'Semester 1 - 2025', '2024-2025', '2025-07-01', '2025-11-30', 'No', '2025-08-15');
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL009')
    INSERT INTO [academic_calendar] VALUES ('CAL009', 'Summer Intensive', '2023-2024', '2024-04-01', '2024-04-30', 'Yes', NULL);
IF NOT EXISTS (SELECT 1 FROM [academic_calendar] WHERE [calendar_id] = 'CAL010')
    INSERT INTO [academic_calendar] VALUES ('CAL010', 'Workshop Series', '2024-2025', NULL, '2025-02-28', 'Yes', NULL);
GO

