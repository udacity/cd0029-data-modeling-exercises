# Lesson 1: Introduction to Data Modeling — Quizzes

---

### **Quiz 1: What is Data — Understanding Foundations**

**Question 1:** A retail company collects transaction timestamps, product IDs, and purchase amounts from its point-of-sale system. A manager asks: "Which product categories are trending this quarter?" At what level of the DIKW pyramid does the manager's question sit?
- A) Data — it's just asking for raw values
- B) Information — it's asking for organized summaries of raw values
- C) Knowledge — it requires analysis and context beyond simple aggregation
- D) Wisdom — it requires contextual judgment

**Answer:** C) Knowledge — it requires analysis and context beyond simple aggregation
**Explanation:** "Trending" requires synthesizing information over time, comparing periods, and interpreting what the patterns mean. The DIKW pyramid describes Knowledge as "the result of synthesizing information and analyzing data in context, combining belief with fact and justification." The raw transactions are data, a summary of sales per category is information, but identifying *trends* requires contextual analysis — that's knowledge.

Feedback:
- A) Data is the raw values themselves (timestamps, IDs, amounts) — the manager isn't asking for raw values, they're asking for interpreted patterns.
- B) Information would be an organized summary like "total sales per category" — but "trending" goes further, requiring comparison over time and interpretation.
- D) Wisdom involves applying knowledge with judgment to make decisions (e.g., "should we invest more in trending categories?"). The question asks what's trending, not what to do about it.

---

**Question 2:** A data engineer tells you: "By some estimates, 90% of the world's data was generated in the last two years alone." Which of the following best explains why this statistic matters for data modeling?
- A) It means older data is no longer useful, and we should abandon or delete older data
- B) The volume, velocity, and variety of data demand intentional structure with schema changes and evolution in mind so systems remains usable
- C) It proves that relational databases are obsolete, and we should move to NoSQL databases
- D) It means all data should be stored in the cloud, in order to make sure data storage can scale

**Answer:** B) The volume, velocity, and variety of data demand intentional structure with schema changes and evolution in mind so systems remains usable
**Explanation:** The lesson stresses that "data modeling means giving raw data some structure, so it actually reflects the real things we're studying." As data volume explodes, the need for good models increases — without structure, data becomes noise. The 5 Vs (volume, velocity, variety, veracity, value) are mentioned as characteristics of modern data challenges.

Feedback:
- A) Older data can still be extremely valuable, although it is not as often used — think about historical trends, compliance records, and training datasets. All rely on past data.
- C) Relational databases remain widely used and highly effective for many workloads. The statistic highlights the need for good modeling, not the obsolescence of any particular technology.
- D) Where data is stored (cloud vs. on-premise) is an infrastructure decision, not a data modeling one. The statistic speaks to the need for structure, not storage location.

---

**Question 3:** Your team is building a simulation of a factory floor, using sensor data to optimize machine placement and airflow. This digital representation is an example of:
- A) An OLAP cube
- B) A data warehouse
- C) A digital twin
- D) A query engine

**Answer:** C) A digital twin
**Explanation:** The concept of a "digital twin" is a digital model constructed from data that represents real-life things like buildings or cities. A factory floor simulation built on sensor data is a textbook example. 

Feedback:
- A) An OLAP cube is a multidimensional data structure for analytical queries, not a simulation of a physical environment.
- B) A data warehouse stores historical data for analysis — it's a data repository, not a real-time simulation of physical objects.
- D) A query engine is a component that interprets and executes queries against stored data, not a digital representation of a real-world system.

---

**Question 4:** A colleague says: "We have a spreadsheet of customer emails, but it doesn't tell us anything useful." According to the DIKW model, what step is missing?
- A) Collecting more emails and identifiable information
- B) Organizing and summarizing the data so it carries meaning
- C) Deleting the spreadsheet and starting over
- D) Converting the spreadsheet to a database to store and query more information

**Answer:** B) Organizing and summarizing the data so it carries meaning — moving from Data to Information
**Explanation:** Raw email addresses are Data — discrete values. The lesson defines Information as "data that's been organized or summarized so it carries meaning." The colleague needs to move up the pyramid: segment customers, find patterns, or link emails to purchase behavior to transform data into information.

Feedback:
- A) Collecting more raw emails just adds more data — it doesn't make the existing data more meaningful or useful.
- C) Deleting data doesn't solve the problem of extracting meaning — it eliminates the raw material you need to work with.
- D) Converting to a database changes the storage format and will allow you to store more emails, but doesn't inherently organize or summarize the data into something meaningful.

---

**Question 5:** William Edwards Deming said: "Without data, you're just another person with an opinion", highlighting the importance of using data to make decisions. Which of the following scenarios best illustrates data-driven decision making?
- A) A CEO decides to enter a new market based on a competitor's opinion alone
- B) A product team uses A/B test results to choose between two UI designs
- C) A manager copies a colleague's database schema without reviewing it
- D) A developer chooses a programming language for their company based on personal preference

**Answer:** B) A product team uses A/B test results to choose between two UI designs
**Explanation:** Deming's quote emphasizes basing decisions on evidence rather than intuition. Option B is the only scenario where a decision is grounded in collected data. The others rely on opinion, imitation, or preference — exactly what Deming cautioned against.

Feedback:
- A) A single opinion is not collected data — basing market entry on this alone is opinion-driven. 
- C) Copying a schema without reviewing it is imitation, not data-driven decision-making. The colleague's schema may not fit your domain. It may not even have any data or records in it yet!
- D) Personal preference for a programming language is exactly the kind of opinion-based decision Deming warned against.

---

---

### **Quiz 2: Identifying Database Components**

**Question 1:** A new team member asks you to explain what a database actually does at the most fundamental level. Which of the following captures the three core components?
- A) Tables, Rows, and Columns
- B) Storage, Query Engine, and Metadata
- C) Input, Processing, and Output
- D) Hardware, Software, and Network

**Answer:** B) Storage, Query Engine, and Metadata

**Explanation:** The lesson describes these three pieces as the core of any database: "how the data is stored, how your queries are interpreted and executed, and how to track the structure and rules that define the data. Those three pieces—storage, query engine, and metadata—shape everything you see from the outside."

Feedback:
- A) Not all databases use tables, rows, and columns — document stores and graph databases use different structures.
- C) Input/Processing/Output describes a general computing model, not specifically what a database manages internally.
- D) These are infrastructure components the database runs *on*, not what the database itself is composed of.

---

**Question 2:** Imagine you build a system that can accept data but provides no way to retrieve it. What fundamental capability is missing from the query engine?
- A) Encryption
- B) The ability to read data back out
- C) Backup functionality
- D) Compression

**Answer:** B) The ability to read data back out

**Explanation:** The query engine needs "a way to write data into the system, and a way to read it back out." A system that only accepts data is essentially a black hole — you can never extract insights. Both write and read operations are the minimum requirements for a useful query engine.

Feedback:
- A) Encryption protects data but isn't a core query engine operation.
- C) Backups are important for disaster recovery but aren't part of the basic read/write contract.
- D) Compression is an optimization, not a fundamental capability.

---

**Question 3:** A developer tries to insert the text "Pear" into a `unit_price DECIMAL` column in PostgreSQL. The database rejects the operation. Which database component enforced this rule?
- A) The query engine's optimizer
- B) The storage layer's file system
- C) Metadata and type constraints
- D) The application code

**Answer:** C) Metadata — specifically, type constraints

**Explanation:** Recall from our lesson - by giving the column a type - in this case numeric - PostgreSQL automatically rejects anything that isn't a valid number. If you try to insert 'Pear' into that column, the database stops you immediately. Metadata includes type constraints, domain rules, and other structural definitions that protect the integrity of data.

Feedback:
- A) The optimizer decides *how* to execute queries efficiently, not whether data is valid.
- B) The storage layer holds data but doesn't enforce type rules.
- D) The application code *should* validate data, but the database's metadata is the last line of defense.

---

**Question 4:** You define a column as `unit_price DECIMAL CHECK (unit_price > 0)` in a relational database. A user tries to insert a price of -5. What happens, and why?
- A) The database stores it but flags it as a warning
- B) The database rejects the insert because it violates the domain constraint
- C) The database automatically converts it to a positive number
- D) The insert succeeds because DECIMAL allows negative numbers

**Answer:** B) The database rejects the insert because it violates the domain constraint

**Explanation:** The lesson defines "the domain of an attribute" as "the range of acceptable values it can take on" and shows this exact pattern: adding a CHECK constraint to restrict `unit_price` to positive values. The database enforces this as part of its checks against metadata, rejecting any value outside the permitted domain.

Feedback:
- A) Relational databases enforce constraints strictly — they reject violations outright rather than storing invalid data with warnings.
- C) Generally, relational databases don't silently transform data to satisfy constraints. Automatic conversion would violate the principle that the database preserves exactly what you insert.
- D) The DECIMAL type does allow negative numbers, but the CHECK constraint explicitly restricts the domain to positive values. The type and the constraint work together.

---

**Question 5:** A lakehouse architecture separates the storage layer from the query engine. Which of the following is a practical benefit of this modular approach?
- A) The query engine can read data stored in multiple formats without redesigning storage
- B) It eliminates the need for metadata entirely
- C) It makes the database run on a single machine only
- D) It forces all data into a strict relational schema

**Answer:** A) The query engine can read data stored in multiple formats without redesigning storage

**Explanation:** The lesson contrasts tightly coupled systems (where "the query engine and the storage format are tightly coupled—they're built as one integrated system") with modular lakehouse architectures where "one component holds the files, and another reads those files and runs the queries." This separation means you can change or add query engines without modifying the underlying storage.

Feedback:
- B) Metadata is still essential — you need schema definitions, data types, and governance rules regardless of architecture. Separation of storage and compute doesn't eliminate metadata.
- C) The opposite is true in many cases (especially when using cloud tools) — decoupling enables distributed systems where storage and compute can scale independently across multiple machines.
- D) A lakehouse architecture supports multiple data formats (Parquet, JSON, CSV, etc.), not just strict relational schemas. That flexibility is one of its key advantages.

---

**Question 6:** Your organization stores data in a graph database, a relational database, and an object store. This approach is an example of:
- A) Normalization
- B) Polyglot persistence
- C) Cloud migration
- D) Data deduplication

**Answer:** B) Polyglot persistence

**Explanation:** The course introduces polyglot persistence as "the idea that no single database fits every problem, and that real applications combine multiple technologies. Relational databases, document stores, and graph databases often work side by side." Using multiple specialized databases together is the definition of polyglot persistence.

Feedback:
- A) Normalization is the process of structuring tables to reduce redundancy within a single relational database — it doesn't describe using multiple database types.
- C) Cloud migration refers to moving systems from on-premise to cloud infrastructure. Using multiple database types is a design choice, not a migration strategy.
- D) Data deduplication removes duplicate copies of data. The scenario describes using different databases for different purposes, not eliminating duplicates.

---

---

### **Quiz 3: Data Use Cases - OLTP, OLAP, and Infrastructure**

**Question 1:** A grocery chain needs a database for its point-of-sale system, processing thousands of checkout transactions per second. Which workload pattern best describes this use case?
- A) OLAP — because the system reads and aggregates sales data
- B) OLTP — because the priority is writing many records quickly and reliably
- C) Batch processing — because transactions are processed overnight
- D) Cold storage — because transaction data is archival

**Answer:** B) OLTP — because the priority is writing many records quickly and reliably
**Explanation:** "In OLTP systems, the most important and prioritized feature is the ability to write many lines of data to the database quickly and reliably." A point-of-sale system generating checkout records in real-time is a classic OLTP workload.

Feedback:
- A) OLAP focuses on reading and aggregating large volumes of historical data for analysis — the point-of-sale system's priority is writing transactions, not running analytical reports.
- C) Batch processing handles data in scheduled bulk jobs. Checkout transactions happen in real-time and must be recorded immediately, not queued for overnight processing.
- D) Cold storage is for archival data that's rarely accessed. Active transaction data from a running POS system is "hot" and must be written and read immediately.

---

**Question 2:** A data analyst wants to calculate the average transaction total across all stores for the past quarter. They're using a column-oriented database. Why is this faster than using a row-oriented database for this query?
- A) Column-oriented databases have better user interfaces
- B) You can read just the transaction total column without scanning unrelated fields in each row
- C) Column-oriented databases use less memory overall
- D) Row-oriented databases can't perform arithmetic operations

**Answer:** B) You can read just the transaction total column without scanning unrelated fields in each row
**Explanation:** The lesson explains: "It's easier to look at one file, and sum all the grocery store transaction costs, if you have a column oriented database, and you choose to open up the total cost column. If you did this on a row-oriented database, you would have to open multiple files, look at all the rows, go over to the total cost column, and then sum across each record one by one."

Feedback:
- A) User interfaces are application-layer concerns and have nothing to do with how data is physically stored or scanned.
- C) Column-oriented databases may actually use more memory for write-heavy workloads. The advantage is in read efficiency for aggregations, not total memory usage.
- D) Row-oriented databases can absolutely perform arithmetic — the issue is that they must scan all fields in each row to reach the one column needed, which is slower for aggregation queries.

---

**Question 3:** A financial services company needs two systems: one for real-time trade execution and another for end-of-month regulatory reporting across millions of records. Match each use case to the most appropriate system architecture.

Column A:
1. Real-time trade execution
2. End-of-month regulatory reporting across millions of records

Column B:
A. Column-oriented OLAP system
B. Row-oriented OLTP system

**Answer:** 1→B, 2→A
**Explanation:** The lesson distinguishes between OLTP workloads (fast writes, row-oriented) and OLAP workloads (aggregate reads, column-oriented). Real-time trading is a write-heavy OLTP workload, so it maps to a row-oriented OLTP system (B). Regulatory reporting across millions of records is a read/aggregation-heavy OLAP workload, so it maps to a column-oriented OLAP system (A). Different problems call for different database architectures.

Feedback:
- 1→B: Real-time trade execution requires fast, reliable writes — the defining characteristic of OLTP. OLAP systems are optimized for reads and would struggle with the low-latency write demands of live trading.
- 2→A: Regulatory reporting across millions of records requires scanning and aggregating large volumes — the strength of column-oriented OLAP systems. A row-oriented system would be inefficient for this scale of analytical reporting.

---

**Question 4:** You're advising a startup that processes recent user activity data in real-time but also needs to retain seven years of historical data for compliance. Which of the following correctly describe the data tiers in this scenario? (Select all that apply)
- A) Recent user activity is "hot" or "warm" data
- B) Historical compliance data is "cold" data
- C) Both are "hot" data since the company owns all of it
- D) The distinction between hot and cold data only applies to cloud storage

**Answer:** A, B
**Explanation:** The lesson defines "'hot' or 'warm' data" as "focusing on more recent years and trends that are to be consumed right away for important business operations" and "'cold' data" as "more for archival usage and understanding corporate history." Both A and B correctly describe the startup's two tiers.

Feedback:
- A) ✅ Recent user activity processed in real-time is "hot" or "warm" data — it's actively consumed for important business operations.
- B) ✅ Seven years of historical compliance data is "cold" data — it's archival, rarely accessed, and retained for regulatory purposes.
- C) Ownership doesn't determine data temperature. The key factor is how frequently and urgently the data is accessed, not who owns it.
- D) Hot/cold distinctions apply to any storage environment — on-premise, cloud, or hybrid. It's about access patterns and recency, not infrastructure.

---

**Question 5:** Your team is debating whether to self-host a PostgreSQL database on-premise or use AWS RDS. Which of the following are advantages of using a cloud managed service like AWS RDS? (Select all that apply)
- A) You never have to touch the hardware
- B) Setup, maintenance, and patching are handled for you
- C) It prevents all security vulnerabilities automatically
- D) Cloud databases don't require any monitoring

**Answer:** A, B
**Explanation:** The lesson states: "If you choose to run a database with a cloud vendor, you'll never have to touch the hardware." Most cloud vendors offer managed services, which includes an easy setup and launching of the database as a service provided—in other words, you don't have to set up a server yourself, install the operating system, and so on—that all comes included.

Feedback:
- A) ✅ The lesson explicitly states you'll "never have to touch the hardware" when using a cloud vendor.
- B) ✅ Cloud managed services handle setup, maintenance, and patching — you don't have to install the operating system, configure the server, or manage updates yourself.
- C) Cloud services improve security posture through patching and managed infrastructure, but they don't prevent all vulnerabilities automatically. Security is a shared responsibility.
- D) Cloud databases still require monitoring for performance, costs, and security. The cloud provider handles infrastructure-level concerns, but application-level monitoring remains your responsibility.

---

**Question 6:** A single-node database running on one machine is reaching its capacity limits as your dataset grows. What architectural change does the lesson describe for handling much larger workloads?
- A) Buying a larger monitor
- B) Moving to a distributed system that spreads storage and processing across multiple machines
- C) Deleting old data to free up space
- D) Switching from SQL to NoSQL

**Answer:** B) Moving to a distributed system that spreads storage and processing across multiple machines
**Explanation:** A single-node database runs everything—storage, query planning, query execution—on one machine... A distributed system spreads those responsibilities across multiple machines. That adds complexity, but it also lets the system handle much larger workloads and datasets.

Feedback:
- A) A larger monitor has no impact on database capacity or performance — it's a display device, not a computing resource.
- C) Deleting old data is a short-term workaround that sacrifices valuable information. The lesson describes scaling the system's architecture, not reducing its data.
- D) Switching from SQL to NoSQL doesn't inherently solve capacity limits. Both paradigms can be single-node or distributed — the key change is moving from single-node to distributed architecture.

---

---

### **Quiz 4: Physical & Logical Data Models**

**Question 1:** A business analyst draws a diagram showing "Customer," "Order," and "Product" as boxes with lines showing relationships between them. A database engineer then translates this into PostgreSQL table definitions with column types and indexes. Match each role to the type of data model they created.

Column A:
1. Business analyst (entity/relationship diagram with boxes and lines)
2. Database engineer (PostgreSQL table definitions with column types and indexes)

Column B:
A. Logical model
B. Physical model

**Answer:** 1→A, 2→B

**Explanation:** As per our lesson, the logical model is the human-friendly view. It describes the entities in your domain, their attributes, and how they relate to each other. The analyst's diagram is a logical model. The physical model is the machine-friendly view. It describes how the data is actually stored and accessed under the hood. The engineer's PostgreSQL definitions with types and indexes is closer to the physical model.

Feedback:
- 1→A: The analyst's diagram shows entities and relationships at a conceptual level — no storage details like data types, indexes, or disk layout. This is the defining characteristic of a logical model.
- 2→B: The engineer's PostgreSQL DDL specifies implementation details (column types, indexes, constraints) — the machine-friendly view that describes how data is actually stored. This is the physical model.

---

**Question 2:** You need to add a `loyalty_tier` column to an existing `customers` table. Which SQL category and command would you use?
- A) DML — INSERT
- B) DML — UPDATE
- C) DDL — ALTER
- D) DDL — SELECT

**Answer:** C) DDL — ALTER

**Explanation:** The lesson explains that DDL (Data Definition Language) is "how you create tables, define attributes, set primary keys, add constraints, or create indexes" and that "an ALTER command changes an existing structure—adding a column, modifying a constraint, or adjusting something in the physical design." Adding a column changes the table's structure, not its data, so that's DDL.

Feedback:
- A) INSERT adds data rows, not structural changes to the table. That's DML.
- B) UPDATE modifies existing data values, not the table's structure. That's DML.
- D) SELECT retrieves data and is DML. There's no DDL SELECT.

---

**Question 3:** A developer runs `SELECT * FROM orders WHERE total > 100`. Which SQL category does this belong to, and what does it affect?
- A) DDL — it changes the structure of the orders table
- B) DML — it reads data from the orders table
- C) DDL — it creates a new filtered table
- D) DML — it deletes rows below 100

**Answer:** B) DML — it reads data from the orders table

**Explanation:** "SELECT to fetch things, INSERT to add them, UPDATE and DELETE to change them. That set of commands is known as Data Manipulation Language, or DML." A SELECT reads and returns data — it doesn't modify structure (DDL) or delete anything.

Feedback:
- A) SELECT doesn't change the structure of any table — it only reads existing data. Structural changes use DDL commands like CREATE, ALTER, or DROP.
- C) SELECT doesn't create new tables. It returns a result set, which is a temporary view of data, not a new persistent object.
- D) The WHERE clause filters which rows are returned in the results — it doesn't delete rows from the table. DELETE is a separate DML command.

---

**Question 4:** The quote "All models are wrong, but some are useful" is often cited in data modeling. Which of the following best captures its meaning in practice?
- A) You should avoid building data models because they'll always be flawed
- B) A model doesn't need to capture every detail of reality — it just needs to serve the problems you're solving
- C) Only mathematically perfect models should be deployed
- D) Data models are temporary and should be rebuilt from scratch frequently

**Answer:** B) A model doesn't need to capture every detail of reality — it just needs to serve the problems you're solving

**Explanation:** The lesson opens with this quote and explains: "You'll never design a model that captures every detail of the real world—but you can design one that's useful for the problems you're trying to solve." Pragmatic data modeling accepts trade-offs while focusing on fitness for purpose.

Feedback:
- A) The quote says models are *useful* despite being imperfect. It's an argument for building models pragmatically, not avoiding them entirely.
- C) "All models are wrong" directly denies the existence of mathematically perfect models. The point is that usefulness matters more than completeness.
- D) Models should evolve as requirements change, but the quote doesn't advocate constant rebuilding — it advocates building models that are good enough for the task at hand.

---

**Question 5:** In a team meeting, someone says: "DDL changes the metadata; DML changes the data." Give an example that illustrates this distinction.
- A) CREATE TABLE creates data; SELECT reads metadata
- B) ALTER TABLE ADD COLUMN changes metadata (table structure); INSERT INTO adds data (row values)
- C) DROP TABLE deletes data; UPDATE changes metadata
- D) Both DDL and DML affect only the data

**Answer:** B) ALTER TABLE ADD COLUMN changes metadata (table structure); INSERT INTO adds data (row values)

**Explanation:** The lesson states "DDL impacts the metadata, DML impacts the data." ALTER TABLE modifies the table's structure and rules (metadata). INSERT INTO adds actual row values (data). This is the fundamental split between the two SQL categories.

Feedback:
- A) CREATE TABLE is DDL (it creates structure/metadata), not data. SELECT is DML that reads data, not metadata.
- C) DROP TABLE is DDL that removes the structure (and its data). UPDATE is DML that changes data values, not metadata.
- D) DDL and DML target different layers — DDL affects structure/metadata, DML affects the actual stored data. They are fundamentally different.

---

**Question 6:** Your application evolves over time, and the database schema needs to change with it (e.g., adding columns, changing constraints). What practice does the lesson describe for managing these changes systematically?
- A) Manually editing the database each time
- B) Packaging schema changes as migrations — small, versioned updates that evolve the schema over time
- C) Deleting and recreating the database for every change
- D) Avoiding schema changes entirely

**Answer:** B) Packaging schema changes as migrations — small, versioned updates that evolve the schema over time

**Explanation:** The lesson describes: "In many systems, especially in application development, these kinds of changes are packaged as a *migration*—a small, versioned update that evolves the database schema over time." Migrations enable controlled, traceable schema evolution.

Feedback:
- A) Manual edits are error-prone, untracked, and hard to reproduce across environments. Migrations provide version control and repeatability.
- C) Deleting and recreating the database destroys all existing data. Migrations preserve data while evolving the structure incrementally.
- D) Avoiding schema changes is impractical — applications evolve, and the database must evolve with them. Migrations make that evolution manageable.
