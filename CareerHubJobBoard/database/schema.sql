
IF DB_ID('JobBoardDB') IS NOT NULL
BEGIN
    ALTER DATABASE JobBoardDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE JobBoardDB;
END


CREATE DATABASE JobBoardDB;

USE JobBoardDB;


CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY IDENTITY(1,1),
    CompanyName VARCHAR(255) NOT NULL,
    Location VARCHAR(255) NOT NULL
);


CREATE TABLE Applicants (
    ApplicantID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone VARCHAR(20) NOT NULL,
    Resume VARCHAR(255) NOT NULL
);


CREATE TABLE JobListings (
    JobListingID INT PRIMARY KEY IDENTITY(1,1),
    CompanyID INT,
    JobTitle VARCHAR(255) NOT NULL,
    JobDescription TEXT NOT NULL,
    JobLocation VARCHAR(255) NOT NULL,
    Salary DECIMAL(18, 2) NOT NULL CHECK (Salary >= 0),
    JobType VARCHAR(50) NOT NULL,
    PostedDate DATETIME NOT NULL DEFAULT GETDATE(),
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);


CREATE TABLE JobApplications (
    ApplicationID INT PRIMARY KEY IDENTITY(1,1),
    JobListingID INT,
    ApplicantID INT,
    ApplicationDate DATETIME NOT NULL DEFAULT GETDATE(),
    CoverLetter TEXT NOT NULL,
    FOREIGN KEY (JobListingID) REFERENCES JobListings(JobListingID),
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
);


CREATE INDEX IDX_CompanyID ON JobListings(CompanyID);
CREATE INDEX IDX_JobListingID ON JobApplications(JobListingID);
CREATE INDEX IDX_ApplicantID ON JobApplications(ApplicantID);

SELECT * FROM JobListings;

SELECT * FROM Companies;


SELECT * FROM JobApplications;


SELECT * FROM Applicants;


SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'JobListings';

SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'JobListings';


SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Companies';


SELECT jl.JobListingID, jl.JobTitle, jl.Salary, jl.CompanyID, c.CompanyName, c.Location
FROM JobListings jl
LEFT JOIN Companies c ON jl.CompanyID = c.CompanyID


SELECT * FROM INFORMATION_SCHEMA.TABLES;

