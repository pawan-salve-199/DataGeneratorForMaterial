
--drop database ConstructionMaterialProject
if DB_ID('ConstructionMaterialProject') is null create database ConstructionMaterialProject;

use ADFPrectice
use ConstructionMaterialProject;


CREATE TABLE Suppliers (
    SupplierID INTEGER  IDENTITY(1,1) PRIMARY KEY,
    SupplierName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255),
    Phone VARCHAR(25),
    Email VARCHAR(255)a
);

CREATE TABLE Materials (
    MaterialID INTEGER IDENTITY(1,1) PRIMARY KEY,
    MaterialName VARCHAR(255) NOT NULL,
    Description TEXT,
    UnitPrice DECIMAL(10, 2) NOT NULL,
	Unit varchar(255),
	CategoryID varchar(255)
);

CREATE TABLE Cities (
    CityID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    CityName VARCHAR(255) NOT NULL,
    Country VARCHAR(255)
);

CREATE TABLE SupplierMaterials (
    SupplierID INTEGER,
    MaterialID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

CREATE TABLE Customers (
    CustomerID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255),
    Phone VARCHAR(30),
    Email VARCHAR(255),
    CityID INTEGER,
    FOREIGN KEY (CityID) REFERENCES Cities(CityID)
);


CREATE TABLE Orders (
    OrderID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    CustomerID INTEGER,
    MaterialID INTEGER,
    Quantity INTEGER,
    OrderDate datetime,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);


CREATE TABLE Projects (
    ProjectID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    ProjectName VARCHAR(255) NOT NULL,
    StartDate datetime,
    EndDate datetime,
    CityID INTEGER,
    FOREIGN KEY (CityID) REFERENCES Cities(CityID)
);

CREATE TABLE ProjectMaterials (
    ProjectID INTEGER,
    MaterialID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

CREATE TABLE MaterialCategories (
    CategoryID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL
);

CREATE TABLE SupplierCertifications (
    CertificationID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    CertificationName VARCHAR(255) NOT NULL
);

CREATE TABLE SupplierCertificationMapping (
    SupplierID INTEGER,
    CertificationID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (CertificationID) REFERENCES SupplierCertifications(CertificationID)
);

CREATE TABLE Transactions (
    TransactionID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    SupplierID INTEGER,
    MaterialID INTEGER,
    CityID INTEGER,
    Quantity INTEGER,
    TransactionDate datetime,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
    FOREIGN KEY (CityID) REFERENCES Cities(CityID)
);


CREATE TABLE Inventory (
    InventoryID  INTEGER IDENTITY(1,1) PRIMARY KEY,
    MaterialID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);





use ConstructionMaterialProject

select * from MaterialCategories
select * from Materials
select * from SupplierCertifications
select * from Suppliers
select * from SupplierMaterials
select * from Customers
select * from Orders
select * from Transactions

select * from sys.tables;

CREATE TABLE [dbo].[controltable](
	[Source_System_Name] [nvarchar](255) NULL,
	[Source_Object_Type] [nvarchar](255) NULL,
	[Source_Object_Schema] [nvarchar](255) NULL,
	[Source_Object_Name] [nvarchar](255) NULL,
	[Source_File_Location] [nvarchar](255) NULL,
	[Target_Location] [nvarchar](255) NULL,
	[Target_Object_Name] [nvarchar](255) NULL,
	[File_Format] [nvarchar](255) NULL,
	[Partition_Column] [nvarchar](255) NULL,
	[Load_Type] [nvarchar](255) NULL,
	[Watermark_Column] [nvarchar](255) NULL,
	[Creation_Time] [datetime] NULL,
	[Indicator] [float] NULL,
	[watermark_value] [nvarchar](100) NULL);

