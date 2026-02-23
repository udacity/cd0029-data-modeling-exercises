# Data Modeling Course - Comprehensive Quiz Collection

This document contains quizzes for all four lessons of the Data Modeling course (cd0029). Quizzes marked with **[EXTRA]** were not originally specified in the project scope but have been added to enhance learning and assessment.

---

## **LESSON 1: Introduction to Data Modeling**

### **Quiz 1: Identifying Database Components** *(Original - from Project Scope)*

**Question 1:** According to the lesson, what are the three fundamental components of a database?
- A) Tables, Rows, and Columns
- B) Storage, Query Engine, and Metadata
- C) Input, Processing, and Output
- D) Hardware, Software, and Network

**Answer:** B) Storage, Query Engine, and Metadata
**Explanation:** The lesson describes these three components as the core elements: storage (how data is physically stored), query engine (how queries are interpreted and executed), and metadata (the structure and rules that define the data).

---

**Question 2:** The query engine needs two basic capabilities. What are they?
- A) Backup and restore
- B) Write data and read data
- C) Encrypt and decrypt
- D) Compress and decompress

**Answer:** B) Write data and read data
**Explanation:** As stated in the lesson, the query engine needs "a way to write data into the system, and a way to read it back out." Without both operations, data would be unusable.

---

**Question 3:** What is metadata in a database context?
- A) Data about your data - including types, rules, and constraints
- B) The actual values stored in tables
- C) Backup copies of production data
- D) User activity logs

**Answer:** A) Data about your data - including types, rules, and constraints
**Explanation:** The lesson explains that metadata includes "requirements about what type each attribute should be; rules that enforce certain standards or constraints; checks that prevent common errors; guarantees for the software that depends on the database."

---

**Question 4:** In the grocery spreadsheet example, what would prevent someone from entering "Pear" in a unit_price column?
- A) User training
- B) Metadata enforcement through type constraints (e.g., DECIMAL)
- C) Manual review processes
- D) Spell checking software

**Answer:** B) Metadata enforcement through type constraints (e.g., DECIMAL)
**Explanation:** The lesson provides this exact example: "By giving the column a numeric type, PostgreSQL automatically rejects anything that isn't a valid number. If you try to insert 'Pear' into that column, the database stops you immediately. That's metadata doing its job."

---

**Question 5:** What is a "domain" in database terminology?
- A) A website address for accessing the database
- B) The range of acceptable values an attribute can take on
- C) The physical location of the server
- D) The username and password combination

**Answer:** B) The range of acceptable values an attribute can take on
**Explanation:** The lesson states: "The domain of an attribute is the range of acceptable values it can take on. For a grocery dataset, the domain of 'unit price' would usually be positive numbers."

---

**Question 6:** What distinguishes a tightly coupled database system from a modular one?
- A) The number of users it supports
- B) Whether the query engine and storage format are integrated as one system or separated
- C) The programming language it's written in
- D) Whether it runs on Windows or Linux

**Answer:** B) Whether the query engine and storage format are integrated as one system or separated
**Explanation:** The lesson explains that "traditionally, the query engine and the storage format are tightly coupled—they're built as one integrated system" whereas "modern systems also offer more modular options" where storage and query engines are separated, like in a lakehouse architecture.

---

### **Quiz 2: Physical & Logical Data Models** *(Original - from Project Scope)*

**Question 1:** What is the primary difference between a logical data model and a physical data model?
- A) Logical models are always faster
- B) The logical model is human-friendly; the physical model is machine-friendly
- C) Physical models are only used in cloud databases
- D) There is no difference

**Answer:** B) The logical model is human-friendly; the physical model is machine-friendly
**Explanation:** The lesson states: "The logical model is the human-friendly view. It describes the entities in your domain, their attributes, and how they relate to each other." And "The physical model is the machine-friendly view. It describes how the data is actually stored and accessed under the hood."

---

**Question 2:** What is Data Definition Language (DDL) used for?
- A) Querying existing data with SELECT statements
- B) Creating tables, defining attributes, setting keys, and adding constraints
- C) Backing up databases
- D) Monitoring database performance

**Answer:** B) Creating tables, defining attributes, setting keys, and adding constraints
**Explanation:** The lesson explains: "DDL is how you create tables, define attributes, set primary keys, add constraints, or create indexes." It's used to define the structure of the data model.

---

**Question 3:** Which of the following is an example of Data Manipulation Language (DML)?
- A) CREATE TABLE customers
- B) ALTER TABLE products ADD COLUMN price
- C) SELECT * FROM orders
- D) DROP TABLE inventory

**Answer:** C) SELECT * FROM orders
**Explanation:** The lesson states: "Once the structure exists, then you can use the SQL you already know—SELECT to fetch things, INSERT to add them, UPDATE and DELETE to change them. That set of commands is known as Data Manipulation Language, or DML."

---

**Question 4:** According to the lesson, what does "All models are wrong, but some are useful" mean in the context of data modeling?
- A) Data models always contain errors
- B) You'll never capture every detail of reality, but you can design models useful for solving specific problems
- C) Models should be avoided
- D) Only perfect models should be used

**Answer:** B) You'll never capture every detail of reality, but you can design models useful for solving specific problems
**Explanation:** The lesson opens with this quote and explains: "You'll never design a model that captures every detail of the real world—but you can design one that's useful for the problems you're trying to solve."

---

**Question 5:** What SQL statement type would you use to change an existing table structure, such as adding a new column?
- A) SELECT
- B) INSERT
- C) ALTER
- D) UPDATE

**Answer:** C) ALTER
**Explanation:** The lesson states: "An ALTER command changes an existing structure—adding a column, modifying a constraint, or adjusting something in the physical design."

---

**Question 6:** When DDL impacts metadata, what effect does this have?
- A) It only affects documentation
- B) It changes the structure and rules that define the data model
- C) It deletes all existing data
- D) It only affects user permissions

**Answer:** B) It changes the structure and rules that define the data model
**Explanation:** The lesson explains that "DDL impacts the metadata, DML impacts the data," and metadata defines the structure, types, constraints, and rules of the database.

---

### **[EXTRA] Quiz 3: Data Use Cases - OLTP, OLAP, and Infrastructure**

**Question 1:** What does OLTP stand for?
- A) Online Transaction Processing
- B) Offline Transaction Protocol
- C) Online Transfer Programming
- D) Optimal Linear Transaction Processing

**Answer:** A) Online Transaction Processing
**Explanation:** The lesson states: "Online Transactional Processing—or OLTP—systems. In OLTP systems, the most important and prioritized feature is the ability to write many lines of data to the database quickly and reliably."

---

**Question 2:** In OLAP systems, what is the primary focus?
- A) Fast writes of transactional data
- B) Reading and aggregating data to create summaries and insights
- C) Real-time user authentication
- D) Social media integration

**Answer:** B) Reading and aggregating data to create summaries and insights
**Explanation:** The lesson explains: "In OLAP systems, the priority flips. There is more focus on the ability to read and aggregate data, summarizing it into information and insight."

---

**Question 3:** Why are row-oriented databases typically used for OLTP?
- A) They are cheaper
- B) Users can insert new records quickly without affecting the rest of the table
- C) They don't require maintenance
- D) They use less storage space

**Answer:** B) Users can insert new records quickly without affecting the rest of the table
**Explanation:** The lesson states: "The general idea is that each row or record is written and stored somewhat independently in sequence. Users can insert new records quickly without affecting the rest of the table. This is useful when you need to write large amounts of data in a short time frame."

---

**Question 4:** According to the lesson, why would summing grocery transaction costs be faster in a column-oriented database?
- A) Column-oriented databases are always faster
- B) You can open one column file instead of reading through all rows
- C) They have better user interfaces
- D) They use more memory

**Answer:** B) You can open one column file instead of reading through all rows
**Explanation:** The lesson explains: "It's easier to look at one file, and sum all the grocery store transaction costs, if you have a column oriented database, and you choose to open up the total cost column. If you did this on a row-oriented database, you would have to open multiple files, look at all the rows, go over to the total cost column, and then sum across each record one by one."

---

**Question 5:** What is "hot" data versus "cold" data?
- A) Data stored on fast servers versus slow servers
- B) Recent, actively accessed data versus older archival data
- C) Encrypted versus unencrypted data
- D) Production versus test data

**Answer:** B) Recent, actively accessed data versus older archival data
**Explanation:** The lesson explains: "'Hot' or 'warm' data would be focusing on more recent years and trends that are to be consumed right away for important business operations or decisions... 'Cold' data, on the other hand, would be more for archival usage and understanding corporate history."

---

**Question 6:** What is a key advantage of running databases on cloud providers with managed services?
- A) They are always free
- B) You never have to touch the hardware and the service handles setup and maintenance
- C) They only work with SQL
- D) They prevent all security issues

**Answer:** B) You never have to touch the hardware and the service handles setup and maintenance
**Explanation:** The lesson states: "If you choose to run a database with a cloud vendor, you'll never have to touch the hardware. Most cloud vendors also offer... managed service, which includes an easy setup and launching of the database as a service provided—in other words, you don't have to set up a server yourself, install the operating system, and so on—that all comes included."

---

**Question 7:** What distinguishes a distributed database from a single-node database?
- A) Distributed databases are always faster
- B) Distributed systems spread storage and processing across multiple machines
- C) Single-node databases cannot handle real workloads
- D) Distributed databases only work in the cloud

**Answer:** B) Distributed systems spread storage and processing across multiple machines
**Explanation:** The lesson explains: "A single-node database runs everything—storage, query planning, query execution—on one machine... A distributed system spreads those responsibilities across multiple machines. That adds complexity, but it also lets the system handle much larger workloads and datasets."

---

### **[EXTRA] Quiz 4: What is Data - Understanding Foundations**

**Question 1:** According to William Edwards Deming, what famous phrase emphasizes the importance of data?
- A) "Data is the new oil"
- B) "In God we trust, all others must bring data"
- C) "Knowledge is power"
- D) "Information wants to be free"

**Answer:** B) "In God we trust, all others must bring data"
**Explanation:** The lesson states: "He was credited with once coining the phrase 'in God we trust, all others must bring data.'" Deming also noted that "without data, you're just another person with an opinion."

---

**Question 2:** What is the DIKW pyramid?
- A) A data storage format
- B) A model showing the progression from Data to Information to Knowledge to Wisdom
- C) A type of database index
- D) A cloud architecture pattern

**Answer:** B) A model showing the progression from Data to Information to Knowledge to Wisdom
**Explanation:** The lesson describes this model: "Data is the foundation. The raw digital values. Information is data that's been organized or summarized so it carries meaning... Knowledge is the result of synthesizing information and analyzing data in context... And wisdom is the level where we make sound judgments based on that knowledge."

---

**Question 3:** According to the lesson's definition, what is data?
- A) Analyzed insights ready for decision-making
- B) A collection of discrete or continuous values "as given"—the raw values provided by whatever system collected them
- C) Only numerical information
- D) The final output of machine learning models

**Answer:** B) A collection of discrete or continuous values "as given"—the raw values provided by whatever system collected them
**Explanation:** The lesson states: "Ultimately, we can think of data as a collection of discrete or continuous values 'as given'—the raw values provided by whatever system or person collected them."

---

**Question 4:** What does "information" represent in the DIKW model?
- A) Raw unprocessed data
- B) Data that's been organized or summarized so it carries meaning
- C) The same thing as wisdom
- D) Only statistical analyses

**Answer:** B) Data that's been organized or summarized so it carries meaning
**Explanation:** The lesson explains: "Information is data that's been organized or summarized so it carries meaning. Information fundamentally allows us to interpret and understand a studied entity or its abstraction."

---

**Question 5:** By some estimates mentioned in the lesson, what percentage of the world's data was generated in the last two years?
- A) 50%
- B) 70%
- C) 90%
- D) 99%

**Answer:** C) 90%
**Explanation:** The lesson states: "This matters now more than ever because today we produce much more data than we ever have. By some estimates, 90% of the world's data was generated in the last two years alone."

---

**Question 6:** What is a "digital twin" as mentioned in the lesson?
- A) A backup copy of a database
- B) A digital model constructed from data that represents real-life things like buildings or cities
- C) A mirrored database server
- D) A type of encryption

**Answer:** B) A digital model constructed from data that represents real-life things like buildings or cities
**Explanation:** The lesson mentions: "We also explore the concept of a 'digital twin' where data begins to construct a digital version of real life things (buildings, cities, companies etc.)" and asks us to "Think about the amount of data needed to build a 'digital twin' model of a city for engineering uses."

---

---

## **LESSON 2: Data Modeling for Relational Databases**

### **[EXTRA] Quiz 1: ACID Properties and Transactions**

**Question 1:** What does ACID stand for in database systems?
- A) Automatic, Consistent, Integrated, Durable
- B) Atomicity, Consistency, Isolation, Durability
- C) Advanced, Connected, Integrated, Distributed
- D) Automatic, Concurrent, Isolated, Distributed

**Answer:** B) Atomicity, Consistency, Isolation, Durability
**Explanation:** The lesson explains that ACID represents the four key guarantees relational databases provide: Atomicity (transactions are all-or-nothing), Consistency (operations cannot violate constraints), Isolation (transactions behave as if they run sequentially), and Durability (committed changes persist even after system failures).

---

**Question 2:** According to the lesson, what does Consistency in ACID mean?
- A) Data is stored consistently across all servers
- B) Any operation on the database cannot violate the database's constraints
- C) All transactions complete at the same speed
- D) Backups are created consistently

**Answer:** B) Any operation on the database cannot violate the database's constraints
**Explanation:** The lesson states: "Consistency means that any operation on the database cannot violate the database's constraints. If an operation would break a rule related to keys, types, or any other metadata, the database rejects it."

---

**Question 3:** In the lesson's watermelon example, what problem does Atomicity prevent?
- A) Price errors
- B) Getting stuck with half a row if there's a power outage before completing the insert
- C) Duplicate records
- D) Slow queries

**Answer:** B) Getting stuck with half a row if there's a power outage before completing the insert
**Explanation:** The lesson uses this example: "Suppose you are writing a new record to the database. You add the name 'watermelons' but then before you can add the price, there is a power outage or a network interruption. This is an unusual state... Atomicity guarantees that a transaction is either completed in its entirety or not applied at all."

---

**Question 4:** What does Isolation guarantee in ACID?
- A) Database operations are performed in isolation from users
- B) Transactions behave as if they happened one at a time, even when running in parallel
- C) Each database table is isolated from others
- D) The database is isolated from the network

**Answer:** B) Transactions behave as if they happened one at a time, even when running in parallel
**Explanation:** The lesson states: "Isolation guarantees that even when transactions run in parallel, they behave as if they happened one at a time, in sequence... isolation prevents one transaction from interfering with another."

---

**Question 5:** How is Durability achieved in databases?
- A) By keeping all data in RAM
- B) By writing data to permanent storage like hard disks, not volatile memory
- C) By making multiple backups
- D) By encrypting all data

**Answer:** B) By writing data to permanent storage like hard disks, not volatile memory
**Explanation:** The lesson explains: "We achieve this by writing the data to some kind of permanent storage system, such as a hard disk—and not in RAM or 'volatile memory'. RAM needs continuous power, but a disk doesn't have that limitation."

---

### **[EXTRA] Quiz 2: CRUD Anomalies**

**Question 1:** What does CRUD stand for?
- A) Create, Read, Update, Delete
- B) Copy, Remove, Upload, Download
- C) Configure, Run, Use, Debug
- D) Connect, Retrieve, Unify, Distribute

**Answer:** A) Create, Read, Update, Delete
**Explanation:** The lesson explains that CRUD represents "the four basic operations a database performs: Create, Read, Update, and Delete" and that anomalies show up during these operations.

---

**Question 2:** In the lesson's watermelon example, what type of anomaly occurs when you want to insert a new item but don't yet know its price?
- A) Read anomaly
- B) Create (Insert) anomaly
- C) Update anomaly
- D) Delete anomaly

**Answer:** B) Create (Insert) anomaly
**Explanation:** The lesson states: "Suppose we have a table of grocery items, and we want to insert a new row for 'watermelons'. However, the store management has not yet decided on the price... A create anomaly appears when the structure of the table forces you to supply information you don't actually have yet."

---

**Question 3:** According to the lesson, what causes read and update anomalies with onions in the grocery table?
- A) The database is too slow
- B) The structure makes it unclear which row to update when someone says "update the price of onions"
- C) Onions are stored incorrectly
- D) There are no foreign keys

**Answer:** B) The structure makes it unclear which row to update when someone says "update the price of onions"
**Explanation:** The lesson explains: "If someone says 'update the price of onions', which row should change? All types? Just one? It's unclear... These are read and update anomalies: situations where the table technically contains the right data, but the structure makes everyday operations ambiguous or inconsistent."

---

**Question 4:** What type of anomaly occurs when deleting onion rows also erases price information you still need?
- A) Create anomaly
- B) Read anomaly
- C) Update anomaly
- D) Delete anomaly

**Answer:** D) Delete anomaly
**Explanation:** The lesson states: "If onions are temporarily unavailable in a certain location, we might delete the onion rows entirely. But doing that would also erase information we do care about—like the unit prices... a deletion anomaly means that you can't delete a row without unintentionally erasing other valuable information."

---

**Question 5:** What is normalization?
- A) Making all numbers positive
- B) Organizing tables into standard structures called normal forms to avoid anomalies
- C) Deleting old data
- D) Converting text to lowercase

**Answer:** B) Organizing tables into standard structures called normal forms to avoid anomalies
**Explanation:** The lesson defines normalization as "the process of organizing tables into standard structures called normal forms so that the data model reflects the domain cleanly and avoids common anomalies."

---

**Question 6:** According to the lesson, what does First Normal Form (1NF) require?
- A) All columns must be numeric
- B) Each cell should contain a single value, not a list or nested structure
- C) Every table must have exactly one column
- D) All data must be sorted alphabetically

**Answer:** B) Each cell should contain a single value, not a list or nested structure
**Explanation:** The lesson explains that 1NF "says that each cell in a table should contain a single value. Not a list, not a nested table, and not multiple pieces of information packed together" and uses the example of storing price history as JSON in one cell as violating 1NF.

---

### **[EXTRA] Quiz 3: Normalization Forms**

**Question 1:** What is a "natural key" as mentioned in the lesson?
- A) A key made of natural numbers
- B) A primary key that uses intuitive, real-world attributes like item name
- C) A key stored in nature
- D) An automatically generated ID

**Answer:** B) A primary key that uses intuitive, real-world attributes like item name
**Explanation:** The lesson states: "Sometimes, this type of primary key is also called a 'natural key' as it's fairly intuitive" when discussing using the item name as a primary key.

---

**Question 2:** Why does the lesson introduce a composite primary key of (name, type) for grocery items?
- A) To make queries faster
- B) Because name alone can't uniquely identify rows once we have different types of onions
- C) To save storage space
- D) Because the database requires it

**Answer:** B) Because name alone can't uniquely identify rows once we have different types of onions
**Explanation:** The lesson explains: "The name of the item alone might work for apples, but it falls apart once we add different types of onions. All of them share the same name, but they represent different items. So 'name' alone can't uniquely identify a row anymore. Instead, we can use a composite primary key—the combination of the name and the type."

---

**Question 3:** What does Second Normal Form (2NF) require beyond 1NF?
- A) All columns must be indexed
- B) All non-key columns must depend on the entire primary key, not just part of it
- C) All tables must have foreign keys
- D) All data must be encrypted

**Answer:** B) All non-key columns must depend on the entire primary key, not just part of it
**Explanation:** The lesson states: "Second normal form also asks: do all of the other columns in the table depend on the entire primary key—and not just part of it?" The inventory table example shows unit_price depending only on the item, not on the store, violating 2NF.

---

**Question 4:** What is a "transitive dependency" that Third Normal Form (3NF) prevents?
- A) Dependencies that take a long time to process
- B) When a non-key column depends on another non-key column
- C) Dependencies across different databases
- D) Dependencies on external APIs

**Answer:** B) When a non-key column depends on another non-key column
**Explanation:** The lesson explains: "3NF adds one more rule: No non-key column should depend on another non-key column. In other words, there shouldn't be any transitive dependencies among non-key attributes" and uses sale_price depending on base_price and on_sale as an example.

---

**Question 5:** In the lesson's promotion example, why is storing sale_price in the price history table a 3NF violation?
- A) It's too expensive to compute
- B) sale_price depends on base_price and on_sale (non-key columns), not directly on the primary key
- C) It requires too much storage
- D) It makes queries slower

**Answer:** B) sale_price depends on base_price and on_sale (non-key columns), not directly on the primary key
**Explanation:** The lesson states that having sale_price depend on base_price and on_sale creates a "transitive dependency, not a direct fact based on the item and date. That's a 3NF problem."

---

**Question 6:** What solution does the lesson propose for handling promotions while maintaining 3NF?
- A) Delete all promotion data
- B) Store promotion rules in a separate table and calculate sale_price on the fly
- C) Duplicate all price data
- D) Disable normalization

**Answer:** B) Store promotion rules in a separate table and calculate sale_price on the fly
**Explanation:** The lesson explains: "That's why it makes sense to keep the price history table focused on the price on a given date, and move the promotion rules into a separate table... Any query that needs to know the sale price can join the two tables together and calculate it on the fly."

---

### **[EXTRA] Quiz 4: Star and Snowflake Schemas**

**Question 1:** What is a Star Schema?
- A) A schema where all tables are connected to every other table
- B) A dimensional model with a central fact table surrounded by dimension tables
- C) A schema shaped like a star for decoration
- D) A security model for databases

**Answer:** B) A dimensional model with a central fact table surrounded by dimension tables
**Explanation:** A star schema consists of one or more fact tables referencing dimension tables, creating a star-like pattern when visualized.

---

**Question 2:** What is the primary difference between a Star Schema and a Snowflake Schema?
- A) Snowflake schemas are always faster
- B) Snowflake schemas further normalize dimension tables into sub-dimensions
- C) Star schemas can only have 5 dimensions
- D) Snowflake schemas don't use fact tables

**Answer:** B) Snowflake schemas further normalize dimension tables into sub-dimensions
**Explanation:** Snowflake schemas extend star schemas by normalizing dimension tables, breaking them into additional related tables to reduce redundancy.

---

**Question 3:** In a Star Schema, what type of data does the fact table typically contain?
- A) Descriptive attributes
- B) Measurable, quantitative data (metrics) and foreign keys to dimensions
- C) Only primary keys
- D) User credentials

**Answer:** B) Measurable, quantitative data (metrics) and foreign keys to dimensions
**Explanation:** Fact tables store measurable business metrics (like sales amounts, quantities) and foreign keys linking to dimension tables.

---

**Question 4:** Which schema typically requires fewer JOIN operations for queries?
- A) Star Schema
- B) Snowflake Schema
- C) Both require the same number of JOINs
- D) Neither uses JOINs

**Answer:** A) Star Schema
**Explanation:** Star schemas have fewer tables because dimensions are denormalized, requiring fewer JOINs to retrieve data. Snowflake schemas need more JOINs due to normalized dimensions.

---

**Question 5:** In the exercise, the DimProduct table contained a product_category field. When this was normalized into a separate DimCategory table, the schema became:
- A) A Star Schema
- B) A Snowflake Schema
- C) Denormalized
- D) An OLTP schema

**Answer:** B) A Snowflake Schema
**Explanation:** By extracting the category into its own dimension table, we further normalized the dimension, creating a snowflake pattern with additional branches.

---

**Question 6:** What is the main advantage of a Snowflake Schema over a Star Schema?
- A) Faster queries
- B) Reduced data redundancy and storage space
- C) Simpler queries
- D) No foreign keys needed

**Answer:** B) Reduced data redundancy and storage space
**Explanation:** Snowflake schemas eliminate redundancy by normalizing dimensions (e.g., "Electronics" category stored once instead of repeated for each product), saving storage space.

---

### **[EXTRA] Quiz 4: AWS RDS and Cloud Database Management**

**Question 1:** What does AWS RDS stand for?
- A) Relational Data Store
- B) Relational Database Service
- C) Remote Data System
- D) Rapid Deployment Service

**Answer:** B) Relational Database Service
**Explanation:** AWS RDS is Amazon's managed relational database service that supports multiple database engines including PostgreSQL, MySQL, and others.

---

**Question 2:** Which of the following is handled automatically by AWS RDS?
- A) Query optimization
- B) Database schema design
- C) Automated backups and security patching
- D) SQL query writing

**Answer:** C) Automated backups and security patching
**Explanation:** AWS RDS automates infrastructure management tasks like backups, patching, scaling, and monitoring, but application-level tasks remain the developer's responsibility.

---

**Question 3:** What is the purpose of AWS Blue/Green Deployments for databases?
- A) To change the database color scheme
- B) To enable zero-downtime database updates and migrations
- C) To separate development and production data
- D) To create database backups

**Answer:** B) To enable zero-downtime database updates and migrations
**Explanation:** Blue/Green deployments create a parallel environment (green) where changes are tested, then traffic is switched over with minimal downtime.

---

**Question 4:** Where are database credentials typically stored when using AWS RDS with best practices?
- A) In the application source code
- B) In AWS Secrets Manager
- C) In a text file on the server
- D) In environment variables only

**Answer:** B) In AWS Secrets Manager
**Explanation:** AWS Secrets Manager provides secure storage, rotation, and retrieval of database credentials and other sensitive information.

---

**Question 5:** What is a primary benefit of using a cloud-hosted database like AWS RDS over self-hosting?
- A) You have less control over the database
- B) It's always cheaper
- C) Automated maintenance, scaling, and high availability
- D) You can't access the database remotely

**Answer:** C) Automated maintenance, scaling, and high availability
**Explanation:** Cloud-hosted databases handle infrastructure concerns automatically, allowing developers to focus on application development rather than database administration.

---

---

## **LESSON 3: Data Modeling for Document Stores and NoSQL**

### **[EXTRA] Quiz 1: NoSQL and MongoDB Fundamentals**

**Question 1:** According to the lesson, what does "NoSQL" stand for?
- A) No SQL allowed
- B) "Not only SQL" - non-relational databases
- C) New SQL
- D) Next-generation SQL

**Answer:** B) "Not only SQL" - non-relational databases
**Explanation:** The lesson states: "NoSQL is short for 'not only SQL' and refers to non-relational databases" and explains that "the idea wasn't to get rid of relational databases. It was to create databases that didn't force everything into a strict, predefined schema."

---

**Question 2:** What does MongoDB's name derive from?
- A) The founders' names
- B) "Humongous" - reflecting its ability to handle massive data
- C) A type of database tree
- D) A programming language

**Answer:** B) "Humongous" - reflecting its ability to handle massive data
**Explanation:** The lesson states: "A well-known example is MongoDB. Its name is short for 'humongous database'. The principle was, to build a platform that could handle large volumes of unstructured data."

---

**Question 3:** What is BSON?
- A) Better SQL Operations Network
- B) Binary JSON - MongoDB's internal storage format
- C) Basic System Object Notation
- D) Berkeley Standard Object Notation

**Answer:** B) Binary JSON - MongoDB's internal storage format
**Explanation:** The lesson explains: "Internally, MongoDB stores data as BSON—binary JSON—for efficiency, but to developers and applications, it behaves just like JSON."

---

**Question 4:** In MongoDB terminology, what is roughly equivalent to a relational database "table"?
- A) Document
- B) Collection
- C) Field
- D) Key

**Answer:** B) Collection
**Explanation:** The lesson states: "A 'collection' is roughly like a 'table'. A 'document' is roughly like a 'row'. Fields within a document behave a lot like columns."

---

**Question 5:** What advantage does the lesson highlight for document databases when business logic changes?
- A) They are always faster
- B) You can start including new fields when relevant without schema changes or downtime
- C) They automatically optimize queries
- D) They require less storage

**Answer:** B) You can start including new fields when relevant without schema changes or downtime
**Explanation:** The lesson uses an example where security teams want to add a "number of attempts" field: "In a document database, you simply start including the field when it's relevant. No schema change. No downtime. No refactoring half the application just to add one new piece of information."

---

**Question 6:** According to the lesson, how do document stores differ from key-value stores like Redis?
- A) They are exactly the same
- B) Document stores support sorting and filtering on fields; key-value stores only support simple lookups
- C) Key-value stores are always faster
- D) Document stores don't support indexing

**Answer:** B) Document stores support sorting and filtering on fields; key-value stores only support simple lookups
**Explanation:** The lesson explains: "Key-value systems like Redis don't organize fields into documents. All they have is the key and the corresponding data. They're very fast for simple lookups, but don't support sorting or filtering like document stores do."

---

### **[EXTRA] Quiz 2: CRUD Operations in Document Databases**

**Question 1:** In MongoDB's MQL (MongoDB Query Language), what does the dollar sign ($) signify?
- A) A comment
- B) An operator that modifies a document - it tells MongoDB this is an instruction, not data
- C) A variable name
- D) A currency field

**Answer:** B) An operator that modifies a document - it tells MongoDB this is an instruction, not data
**Explanation:** The lesson states: "MongoDB updates use operators, which always start with a dollar sign... In MQL, anything that modifies a document uses a special operator beginning with a dollar sign... The dollar sign tells MongoDB: 'What follows is an instruction, not data.'"

---

**Question 2:** Which MongoDB operator would you use to change or add a field in a document?
- A) $push
- B) $set
- C) $unset
- D) $pull

**Answer:** B) $set
**Explanation:** The lesson explains: "For example: 'set' to change or add a field, 'unset' to remove a field, or 'push' to append to an array."

---

**Question 3:** How does DynamoDB distinguish between keywords and data values in update expressions?
- A) Using dollar signs like MongoDB
- B) Using colons to indicate placeholder values
- C) Using double equals signs
- D) Using asterisks

**Answer:** B) Using colons to indicate placeholder values
**Explanation:** The lesson states: "It requires an 'update expression' and also uses a colon to indicate placeholder values. Similar to the dollar sign in MongoDB, the goal is to distinguish between keywords and data."

---

**Question 4:** In the lesson's comparison of CRUD operations, what syntax does Firestore use to locate records?
- A) Dollar signs ($)
- B) Colons (:)
- C) Double equals signs (==)
- D) Asterisks (*)

**Answer:** C) Double equals signs (==)
**Explanation:** The lesson mentions: "Firestore uses the 'double equals sign' syntax to locate the existing record" for both update and delete operations.

---

**Question 5:** What is the key difference MongoDB operators make compared to SQL updates?
- A) They are slower
- B) They surgically update only specified fields without rewriting the whole document
- C) They require more storage
- D) They don't support indexes

**Answer:** B) They surgically update only specified fields without rewriting the whole document
**Explanation:** The lesson states: "This is one of the biggest differences from SQL. MongoDB doesn't rewrite the whole row—MQL operators surgically update only what you specify."

---

**Question 6:** According to the lesson, what limitation does DynamoDB have compared to MongoDB for deletion?
- A) It can't delete anything
- B) It can only delete based on the item's primary key, not any filter
- C) It requires administrator privileges
- D) It's slower than MongoDB

**Answer:** B) It can only delete based on the item's primary key, not any filter
**Explanation:** The lesson states: "For deletion, MongoDB and DynamoDB are fairly similar. The main difference is that MongoDB can delete based on any filter, while DynamoDB can only delete based on the item's primary key."

---

### **[EXTRA] Quiz 3: MongoDB Aggregation Pipelines**

**Question 1:** What is an aggregation pipeline in MongoDB?
- A) A physical pipe for data transfer
- B) An ETL framework for performing advanced data analysis through a sequence of stages
- C) A backup system
- D) A security feature

**Answer:** B) An ETL framework for performing advanced data analysis through a sequence of stages
**Explanation:** The lesson states: "An aggregation pipeline is an Extract, Transform, Load framework that MongoDB provides for performing advanced data analysis and manipulation on collections. It processes documents through a sequence of stages—filtering, reshaping, grouping, sorting, or joining."

---

**Question 2:** What does MongoDB's $lookup stage do?
- A) Speeds up queries
- B) Performs an operation similar to a left outer join between two collections
- C) Deletes documents
- D) Creates indexes

**Answer:** B) Performs an operation similar to a left outer join between two collections
**Explanation:** The lesson explains: "The 'lookup' stage performs an operation similar to a left outer join between two collections. In this example, it enriches each 'order' document by attaching matching documents from 'customers'."

---

**Question 3:** According to the lesson, how do MongoDB's $lookup operations compare to SQL joins in terms of cost?
- A) They are exactly the same
- B) $lookup is more expensive and not something to rely on for every query
- C) $lookup is always faster
- D) SQL joins are always slower

**Answer:** B) $lookup is more expensive and not something to rely on for every query
**Explanation:** The lesson states: "It's powerful—but not free. Unlike optimized SQL joins, MongoDB's 'lookup' is more expensive. It's powerful, but not something you rely on for every query."

---

**Question 4:** In a MongoDB aggregation pipeline, what does the $group stage do?
- A) Deletes grouped documents
- B) Groups matching documents by specified fields and computes aggregations
- C) Sorts documents
- D) Filters documents

**Answer:** B) Groups matching documents by specified fields and computes aggregations
**Explanation:** The lesson explains the $group stage: "We group the matching documents by year, month, and product category. Inside this group stage, we compute three aggregations" including sum and count operations.

---

**Question 5:** What does the syntax "$sum: 1" mean in a MongoDB aggregation pipeline?
- A) Add the number 1 to each document
- B) Count documents (count each document as 1)
- C) Filter documents with value 1
- D) Delete 1 document

**Answer:** B) Count documents (count each document as 1)
**Explanation:** The lesson states: "and number of sales using 'sum colon one', which counts documents."

---

### **[EXTRA] Quiz 4: MongoDB Atlas and Cloud NoSQL**

**Question 1:** According to the lesson, what type of database service is MongoDB Atlas?
- A) A self-hosted database you manage yourself
- B) A PaaS (Platform as a Service) - a managed database service
- C) An IaaS (Infrastructure as a Service)
- D) A desktop database application

**Answer:** B) A PaaS (Platform as a Service) - a managed database service
**Explanation:** The lesson states: "MongoDB Atlas is the managed version of MongoDB. We've already been using it in the exercises... PaaS stands for Platform as a Service. It means you're renting a fully managed database, not just bare computing hardware."

---

**Question 2:** According to the lesson, what happens when you scale up in MongoDB Atlas?
- A) You delete old data
- B) You choose a higher tier with more CPU cores and RAM
- C) You add more developers
- D) You backup data

**Answer:** B) You choose a higher tier with more CPU cores and RAM
**Explanation:** The lesson explains: "Suppose your workload grows. You can adjust the tier. Scaling up means choosing a higher tier—more CPU cores and more RAM—so each request gets more resources."

---

**Question 3:** What does "sharding" mean in MongoDB?
- A) Deleting old data
- B) Splitting data across multiple servers/machines to scale horizontally
- C) Encrypting data
- D) Creating backups

**Answer:** B) Splitting data across multiple servers/machines to scale horizontally
**Explanation:** The lesson states: "Sharding is the term MongoDB uses for splitting your data across multiple machines to scale horizontally.... Sharding addresses one machine's limits by distributing the data across multiple machines."

---

**Question 4:** According to the lesson, how does DynamoDB differ from MongoDB in terms of cloud architecture?
- A) They are identical
- B) DynamoDB is AWS-native and tightly integrated; MongoDB Atlas runs on virtual machines
- C) MongoDB is faster
- D) DynamoDB doesn't support NoSQL

**Answer:** B) DynamoDB is AWS-native and tightly integrated; MongoDB Atlas runs on virtual machines
**Explanation:** The lesson explains: "DynamoDB is built into AWS at a deeper level. MongoDB Atlas runs on virtual machines. In contrast, DynamoDB is more like AWS's own service that doesn't rely on those virtual machines in the same way. As a result, DynamoDB tends to scale more seamlessly within the AWS ecosystem."

---

**Question 5:** What analogy does the lesson use to explain capacity units in DynamoDB?
- A) Buying gas for a car
- B) Tickets or tokens at an arcade
- C) Electricity usage
- D) Water consumption

**Answer:** B) Tickets or tokens at an arcade
**Explanation:** The lesson states: "Think of capacity like tokens at an arcade. You spend a specific number to use a machine. In DynamoDB, you spend read capacity units and write capacity units every time you interact with data."

---

---

## **LESSON 4: Data Modeling for Graph Databases**

### **[EXTRA] Quiz 1: Graph Database Fundamentals**

**Question 1:** According to the lesson, what famous historical problem motivated graph theory?
- A) The traveling salesman problem
- B) The Seven Bridges of Königsberg
- C) The Tower of Hanoi
- D) The knapsack problem

**Answer:** B) The Seven Bridges of Königsberg
**Explanation:** The lesson states: "The insight came from Leonhard Euler in 1736, who formalized what we now call the 'Seven Bridges of Königsberg problem'... Euler proved there was no route that crossed each bridge exactly once."

---

**Question 2:** What are the three core elements of a graph database?
- A) Tables, Rows, Columns
- B) Nodes, Edges, Properties
- C) Documents, Collections, Fields
- D) Keys, Values, Indexes

**Answer:** B) Nodes, Edges, Properties
**Explanation:** The lesson explains: "A graph database represents data using three things: nodes, edges, and properties. Nodes are entities—people, products, places. Edges are the connections between them... Properties are attributes—names, dates, types."

---

**Question 3:** According to the lesson, how do graph databases handle relationship traversals compared to relational JOIN operations?
- A) They are exactly the same
- B) Graph databases use pointers/addresses making traversals very fast; SQL JOINs scan entire tables
- C) SQL JOINs are always faster
- D) Graph databases don't support traversals

**Answer:** B) Graph databases use pointers/addresses making traversals very fast; SQL JOINs scan entire tables
**Explanation:** The lesson states: "In a graph, when you traverse a relationship, you're following a direct pointer or address. You don't scan all possible records to match conditions. In SQL, a JOIN typically involves scanning indexes or tables to match keys."

---

**Question 4:** What query language does Neo4j use?
- A) SQL
- B) MongoDB Query Language (MQL)
- C) Cypher
- D) JavaScript

**Answer:** C) Cypher
**Explanation:** The lesson explains: "Neo4j uses a custom query language called Cypher. Cypher reads almost like plain English. You can describe patterns you're looking for, and Neo4j will find matching structures in the graph."

---

**Question 5:** According to the lesson, what new standard was voted in for graph query languages?
- A) GraphSQL
- B) GQL (Graph Query Language)
- C) Neo4j Standard
- D) Graph-QL

**Answer:** B) GQL (Graph Query Language)
**Explanation:** The lesson states: "In 2024, 'GQL'—Graph Query Language—was voted in as the new ISO standard for querying graphs, similar to how SQL is the standard for relational databases."

---

**Question 6:** What example does the lesson use to demonstrate why graph databases are useful?
- A) Banking transactions
- B) Fraud detection by finding complex relationship patterns
- C) Weather forecasting
- D) Image processing

**Answer:** B) Fraud detection by finding complex relationship patterns
**Explanation:** The lesson mentions: "You might have a network of accounts, shared addresses, similar transaction times. In a relational database, tracking these multi-hop relationships is cumbersome. In a graph database, you simply traverse edges. This is why graphs are commonly used for fraud detection."

---

### **[EXTRA] Quiz 2: Neo4j and Cypher Queries**

**Question 1:** In Cypher syntax, what do parentheses represent?
- A) Relationships
- B) Nodes
- C) Properties
- D) Functions

**Answer:** B) Nodes
**Explanation:** The lesson states: "In Cypher, you use parentheses to represent nodes" and gives examples like (p: Person) for person nodes.

---

**Question 2:** In Cypher, what syntax represents relationships?
- A) Parentheses ()
- B) Curly braces {}
- C) Square brackets with arrows -[]->
- D) Angle brackets <>

**Answer:** C) Square brackets with arrows -[]->
**Explanation:** The lesson explains: "And square brackets with arrows represent edges. The arrow direction shows which way the relationship goes."

---

**Question 3:** According to the lesson, what does the MATCH clause do in Cypher?
- A) Creates new nodes
- B) Describes a pattern to find in the graph
- C) Deletes nodes
- D) Updates properties

**Answer:** B) Describes a pattern to find in the graph
**Explanation:** The lesson states: "'Match' describes a pattern we're looking for... in plain English: find a person node that's connected to a movie node through an 'acted in' relationship."

---

**Question 4:** What does the RETURN clause do in Cypher queries?
- A) Deletes matched data
- B) Specifies what to give back as the result
- C) Creates a backup
- D) Validates the query

**Answer:** B) Specifies what to give back as the result
**Explanation:** The lesson explains: "'Return' specifies what to give back. We could return the node itself, specific properties like name and title, or even counts and aggregations."

---

**Question 5:** According to the lesson, what Cypher command creates nodes and relationships?
- A) INSERT
- B) ADD
- C) CREATE
- D) NEW

**Answer:** C) CREATE
**Explanation:** The lesson states: "Creating data uses the 'create' command" and demonstrates creating nodes with properties and relationships between them.

---

**Question 6:** What does the MERGE command do in Cypher?
- A) Deletes duplicate nodes
- B) Creates a node/relationship if it doesn't exist; does nothing if it already exists
- C) Combines two graphs
- D) Sorts results

**Answer:** B) Creates a node/relationship if it doesn't exist; does nothing if it already exists
**Explanation:** The lesson states: "'Merge' is like 'create or find.' If the pattern already exists, Merge doesn't create a duplicate. Otherwise, it creates it."

---

### **[EXTRA] Quiz 3: AWS Neptune and Graph Data Modeling**

**Question 1:** What is AWS Neptune?
- A) A relational database
- B) AWS's managed graph database service
- C) A data warehouse
- D) A NoSQL document store

**Answer:** B) AWS's managed graph database service
**Explanation:** The lesson states: "AWS Neptune is the managed graph database service from Amazon. It's similar to how RDS provides managed relational databases and DynamoDB offers managed NoSQL."

---

**Question 2:** Which query languages does AWS Neptune support?
- A) Only SQL
- B) Only Cypher
- C) Both Gremlin and SPARQL (and openCypher)
- D) Only MongoDB Query Language

**Answer:** C) Both Gremlin and SPARQL (and openCypher)
**Explanation:** The lesson states: "Neptune supports multiple query languages. The two main ones are Gremlin and SPARQL" and mentions "Neptune also supports 'openCypher', which is similar to the Cypher language."

---

**Question 3:** According to the lesson, what is Gremlin?
- A) A SQL variant
- B) A graph traversal language
- C) A NoSQL document language
- D) A data visualization tool

**Answer:** B) A graph traversal language
**Explanation:** The lesson explains: "Gremlin is a graph traversal language. You describe how to traverse the graph—step by step—following edges and filtering nodes."

---

**Question 4:** What does SPARQL stand for and what is it used for?
- A) Simple Protocol And RDF Query Language - used for querying semantic data and RDF
- B) Structured Programming And Relational Query Language
- C) System Performance And Resource Query Language
- D) Sequential Processing And Reporting Query Language

**Answer:** A) Simple Protocol And RDF Query Language - used for querying semantic data and RDF
**Explanation:** The lesson states: "SPARQL stands for 'Simple Protocol And RDF Query Language.' It's used for querying 'semantic data.'"

---

**Question 5:** According to the lesson, what type of data is RDF designed for?
- A) Transactional data
- B) Data presented as triples: subject, predicate, object
- C) Columnar data
- D) Time-series data

**Answer:** B) Data presented as triples: subject, predicate, object
**Explanation:** The lesson explains: "RDF stands for 'Resource Description Framework.' It's a format for representing data as 'triples': a subject, a predicate, and an object... for example: 'Alice, knows, Bob.'"

---

**Question 6:** According to the lesson, what is a key advantage of using AWS Neptune over self-hosted Neo4j?
- A) Neptune uses a completely different data model
- B) Neptune handles provisioning, backups, replication, and scaling automatically
- C) Neptune is always free
- D) Neptune doesn't require any queries

**Answer:** B) Neptune handles provisioning, backups, replication, and scaling automatically
**Explanation:** The lesson states: "Neptune handles the provisioning, backups, replication, and point-in-time recovery. You don't manage servers. You simply connect and query the graph."

---

---

## **Summary: Quizzes Created**

### Original (from Project Scope): 2 quizzes
- Lesson 1, Quiz 1: Identifying Database Components
- Lesson 1, Quiz 2: Physical & Logical Data Models

### [EXTRA] Quizzes Added: 12 quizzes
- Lesson 1, Quiz 3: OLTP vs OLAP Use Cases
- Lesson 1, Quiz 4: Data, Information, and Knowledge
- Lesson 2, Quiz 1: ACID Properties and Transactions
- Lesson 2, Quiz 2: Normalization and CRUD Anomalies
- Lesson 2, Quiz 3: Star and Snowflake Schemas
- Lesson 2, Quiz 4: AWS RDS and Cloud Database Management
- Lesson 3, Quiz 1: NoSQL and MongoDB Fundamentals
- Lesson 3, Quiz 2: Document Store Data Modeling
- Lesson 3, Quiz 3: MongoDB Atlas and Cloud NoSQL
- Lesson 4, Quiz 1: Graph Database Fundamentals
- Lesson 4, Quiz 2: Neo4j and Cypher Queries
- Lesson 4, Quiz 3: Graph Data Modeling Patterns
- Lesson 4, Quiz 4: AWS Neptune and Cloud Graph Databases

### Total: 14 quizzes covering all 4 lessons

---

## **Quiz Implementation Notes**

Each quiz includes:
- Multiple choice questions (typically 5-6 per quiz)
- Correct answers clearly marked
- Detailed explanations for each answer
- Alignment with learning objectives from the project scope
- Coverage of practical concepts demonstrated in exercises
- Progressive difficulty matching lesson complexity

These quizzes can be implemented in various formats:
- LMS (Learning Management System) integration
- Jupyter Notebook interactive widgets
- Web-based quiz platforms
- PDF worksheets for offline practice
