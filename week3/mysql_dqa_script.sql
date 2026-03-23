-- =========================================================================================
-- EdTech Data Quality Assessment (DQA) - MySQL Workbench Script
-- This script contains all SQL commands to:
--   1. Create the Database and Tables
--   2. Detect Data Quality Issues (SELECT queries)
--   3. Clean the Data (UPDATE / DELETE queries)
-- =========================================================================================

-- -----------------------------------------------------------------------------------------
-- PART 1: SETUP DATABASE & TABLES
-- -----------------------------------------------------------------------------------------

CREATE DATABASE IF NOT EXISTS edtech_dqa;
USE edtech_dqa;

-- Note: In MySQL Workbench, you will right-click on the 'edtech_dqa' schema,
-- select "Table Data Import Wizard", and import the 6 raw CSV files from 'dataset/raw/'.
-- The import will create tables matching the CSV names (e.g., 'learners', 'transactions').
-- Wait until you have imported ALL 6 CSV files before running Part 2 and Part 3.

-- -----------------------------------------------------------------------------------------
-- PART 2: DQA ASSESSMENT (FINDING THE ISSUES)
-- Run these SELECT queries to "find" the bad data.
-- -----------------------------------------------------------------------------------------

-- 1. LEARNERS
SELECT '--- LEARNERS ISSUES ---' AS Info;

-- Find duplicate learner_id
SELECT learner_id, COUNT(*) as Count FROM learners GROUP BY learner_id HAVING COUNT(*) > 1;

-- Find missing or invalid emails
SELECT learner_id, email FROM learners 
WHERE email IS NULL OR email = '' OR email NOT LIKE '%@%.%';

-- Find future Date of Birth
SELECT learner_id, date_of_birth FROM learners WHERE date_of_birth > CURDATE();

-- Find inconsistent status casing
SELECT learner_id, status FROM learners WHERE status NOT IN ('Active', 'Inactive', 'Pending');


-- 2. COURSES
SELECT '--- COURSES ISSUES ---' AS Info;

-- Find missing Course Titles
SELECT course_id, course_title FROM courses WHERE course_title IS NULL OR course_title = '';

-- Find negative duration or price
SELECT course_id, duration_hours, price FROM courses WHERE duration_hours <= 0 OR price < 0;

-- Find illogical dates (end before start)
SELECT course_id, start_date, end_date FROM courses WHERE end_date < start_date;


-- 3. TRANSACTIONS
SELECT '--- TRANSACTIONS ISSUES ---' AS Info;

-- Find negative amounts
SELECT transaction_id, amount FROM transactions WHERE amount < 0;

-- Find invalid currency codes
SELECT transaction_id, currency FROM transactions WHERE currency NOT IN ('INR', 'USD', 'EUR', 'GBP', 'AED');

-- Find Orphan Transactions (learner_id does not exist in learners table)
SELECT t.transaction_id, t.learner_id 
FROM transactions t 
LEFT JOIN learners l ON t.learner_id = l.learner_id 
WHERE l.learner_id IS NULL;


-- 4. ACADEMIC CALENDAR
SELECT '--- CALENDAR ISSUES ---' AS Info;

-- Find illogical term dates
SELECT calendar_id, start_date, end_date FROM academic_calendar WHERE end_date < start_date;


-- -----------------------------------------------------------------------------------------
-- PART 3: DATA CLEANING (FIXING THE ISSUES)
-- Run these UPDATE and DELETE queries to clean the data permanently in the database.
-- -----------------------------------------------------------------------------------------
SELECT '--- STARTING DATA CLEANING ---' AS Info;

-- 1. CLEAN LEARNERS
-- Fix missing emails using a placeholder
UPDATE learners 
SET email = CONCAT(LOWER(learner_id), '@unknown.com') 
WHERE email IS NULL OR email = '';

-- Fix future DOB by setting to NULL
UPDATE learners 
SET date_of_birth = NULL 
WHERE date_of_birth > CURDATE();

-- Standardize Status to Title Case
UPDATE learners SET status = 'Active' WHERE LOWER(status) = 'active';
UPDATE learners SET status = 'Inactive' WHERE LOWER(status) = 'inactive';
UPDATE learners SET status = 'Pending' WHERE LOWER(status) = 'pending';


-- 2. CLEAN COURSES
-- Fix negative durations and prices
UPDATE courses SET duration_hours = 1 WHERE duration_hours <= 0;
UPDATE courses SET price = 0 WHERE price < 0;

-- Fix swapped dates
UPDATE courses 
SET start_date = @temp := start_date, 
    start_date = end_date, 
    end_date = @temp 
WHERE end_date < start_date;


-- 3. CLEAN TRANSACTIONS
-- Set negative amounts to 0 and flag as Refunded
UPDATE transactions 
SET amount = 0, status = 'Refunded' 
WHERE amount < 0;

-- Standardize US currency to USD
UPDATE transactions 
SET currency = 'USD' 
WHERE LOWER(currency) IN ('us', 'united states');

-- Fix missing payment methods
UPDATE transactions 
SET payment_method = 'Unknown' 
WHERE payment_method IS NULL OR payment_method = '';

-- Remove Orphan Transactions (Referential Integrity Fix)
DELETE FROM transactions 
WHERE learner_id NOT IN (SELECT learner_id FROM learners);


-- 4. DEDUPLICATION (Example for Course Enrollments)
-- In MySQL, removing duplicates while keeping the first row requires a self-join delete
DELETE t1 FROM course_enrollments t1
INNER JOIN course_enrollments t2 
WHERE t1.enrollment_id = t2.enrollment_id AND t1.id > t2.id; -- Assumes an auto-increment 'id' primary key exists


SELECT '--- DATA CLEANING COMPLETE ---' AS Info;
-- Now your data is perfectly clean in MySQL!
