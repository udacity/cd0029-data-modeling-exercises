# Lesson 2: Data Modeling for Relational Databases — Quizzes

---

### **Quiz 1: ACID Properties and Transactions**

**Question 1:** A bank transfer moves $500 from Account A to Account B. The system debits Account A but crashes before crediting Account B. When the system recovers, the debit is rolled back. Which ACID property ensured this?
- A) Consistency
- B) Isolation
- C) Atomicity
- D) Durability

**Answer:** C) Atomicity
**Explanation:** "Atomicity guarantees that a transaction is either completed in its entirety or not applied at all." The bank transfer is one logical operation — both the debit and credit must happen together or neither should happen. The lesson's watermelon example illustrates the same concept: a partial insert is rolled back after a power outage.

Feedback:
- A) Consistency ensures database constraints aren't violated (e.g., NOT NULL, foreign keys). It doesn't govern whether partial transactions are rolled back.
- B) Isolation ensures concurrent transactions don't interfere with each other. This scenario involves a crash during a single transaction, not two competing ones.
- D) Durability ensures committed data survives failures. Here the transaction never committed — atomicity is what ensures the incomplete transaction is rolled back.

---

**Question 2:** A developer tries to insert a row with a NULL value into a NOT NULL column. The database rejects the operation. Which ACID property is this an example of?
- A) Durability
- B) Atomicity
- C) Isolation
- D) Consistency

**Answer:** D) Consistency
**Explanation:** "Consistency means that any operation on the database cannot violate the database's constraints. If an operation would break a rule related to keys, types, or any other metadata, the database rejects it." The NOT NULL constraint is a database rule, and consistency ensures it's never violated.

Feedback:
- A) Durability ensures committed data persists through crashes. This scenario is about rejecting invalid data before it's stored, not preserving committed data.
- B) Atomicity is about all-or-nothing transactions. A single insert of an invalid value is rejected by a constraint check, not by transaction rollback logic.
- C) Isolation manages concurrent access between transactions. This is a single operation violating a constraint — no concurrency is involved.

---

**Question 3:** Two users simultaneously update the same product's price. User A sets it to $10, User B sets it to $12. The database ensures each transaction behaves as if it ran alone, so no partial or corrupted state results. Which ACID property guarantees this?
- A) Atomicity
- B) Durability
- C) Consistency
- D) Isolation

**Answer:** D) Isolation
**Explanation:** "Isolation guarantees that even when transactions run in parallel, they behave as if they happened one at a time, in sequence... isolation prevents one transaction from interfering with another." Without isolation, the two concurrent updates could produce a corrupted or mixed state.

Feedback:
- A) Atomicity ensures each transaction individually completes fully or not at all. It doesn't address the interaction between two simultaneous transactions.
- B) Durability ensures committed data survives failures. Both transactions here succeed — the issue is preventing them from corrupting each other during execution.
- C) Consistency ensures constraints are met. Both $10 and $12 are valid prices — the issue is preventing a mixed/corrupted state from concurrent access, which is isolation's job.

---

**Question 4:** After a transaction commits successfully, a power failure hits the server. When the server restarts, the committed data is still intact. Why?
- A) Because the database kept the data in RAM
- B) Because the data was written to persistent storage (disk), not volatile memory
- C) Because the database has a query optimizer
- D) Because isolation prevented the power failure from affecting data

**Answer:** B) Because the data was written to persistent storage (disk), not volatile memory
**Explanation:** "We achieve this by writing the data to some kind of permanent storage system, such as a hard disk—and not in RAM or 'volatile memory'. RAM needs continuous power, but a disk doesn't have that limitation." This is the Durability guarantee.

Feedback:
- A) RAM is volatile memory — it loses all data when power is lost. If committed data were only in RAM, a power failure would destroy it.
- C) The query optimizer improves query performance. It has no role in ensuring data survives hardware failures.
- D) Isolation manages concurrent transaction access. It doesn't protect data from physical events like power failures — that's durability through persistent storage.

---

**Question 5:** A consultant reviews a company's tech stack and sees they use a NoSQL database that doesn't guarantee all four ACID properties. When might this trade-off be acceptable?
- A) Never — all databases must be fully ACID-compliant
- B) When the use case prioritizes other aspects over transactional guarantees (e.g., logging, caching)
- C) Only when using graph databases
- D) When the data is stored in the cloud

**Answer:** B) When the use case prioritizes other aspects over transactional guarantees (e.g., logging, caching)
**Explanation:** ACID properties are essential for transactional workloads (banking, inventory), but some use cases like logging, caching, or specific high-throughput analytics can tolerate relaxed guarantees in exchange for performance and scalability. The course emphasizes polyglot persistence — different problems call for different database characteristics.

Feedback:
- A) This is too rigid. Many successful systems (caching layers, event logs, high throughput analytics pipelines) operate without full ACID compliance because their use cases don't require it.
- C) Graph databases can be ACID-compliant (Neo4j is). The trade-off depends on the use case, not the database category.
- D) Cloud vs. on-premise is an infrastructure choice that doesn't determine whether ACID properties are needed. The decision depends on the workload characteristics.

---

---

### **Quiz 2: CRUD Anomalies**

**Question 1:** You have a single table storing both product information and store inventory. You want to add a new product ("dragon fruit") to your catalog, but the product hasn't been stocked in any store yet — and the table requires a store ID. What type of anomaly is this?
- A) Read anomaly
- B) Update anomaly
- C) Insert (Create) anomaly
- D) Delete anomaly

**Answer:** C) Insert (Create) anomaly
**Explanation:** "A create anomaly appears when the structure of the table forces you to supply information you don't actually have yet." You can't insert dragon fruit without a store ID, even though the product exists independently. This is the same pattern as the lesson's watermelon example where the price isn't yet known.

Feedback:
- A) A read anomaly involves ambiguous or inconsistent results when reading data. This scenario is about being unable to insert data at all.
- B) An update anomaly occurs when the same fact stored in multiple places leads to inconsistent updates. This scenario is about inserting new data, not modifying existing data.
- D) A delete anomaly occurs when removing a row unintentionally destroys other valuable information. This scenario involves adding data, not removing it.

---

**Question 2:** Your grocery table has three rows for onions (red, yellow, green), each with a `price` column. Management announces a price increase for all onions. You update only the "red onion" row and forget the others. What anomaly occurred?
- A) Insert anomaly
- B) Delete anomaly
- C) Update anomaly 
- D) Read anomaly 

**Answer:** C) Update anomaly — the same logical fact (onion price) is stored in multiple places
**Explanation:** "If someone says 'update the price of onions', which row should change? All types? Just one? It's unclear... These are read and update anomalies: situations where the table technically contains the right data, but the structure makes everyday operations ambiguous or inconsistent." The root cause is redundancy — the same fact is stored across multiple rows.

Feedback:
- A) An insert anomaly prevents adding data without supplying unrelated information. This scenario is about modifying existing data inconsistently.
- B) A delete anomaly involves losing information when rows are removed. No rows are being deleted here — the problem is inconsistent modification.
- D) The query may return wrong results as a *consequence* of the update anomaly, but the root cause is the redundant storage that made the inconsistent update possible in the first place.

---

**Question 3:** A store temporarily stops carrying onions, so you delete all onion rows. Later, when onions return, you realize you've also lost the unit prices. What type of anomaly is this?
- A) Insert anomaly
- B) Update anomaly
- C) Read anomaly
- D) Delete anomaly

**Answer:** D) Delete anomaly — removing rows unintentionally erased other valuable information
**Explanation:** "A deletion anomaly means that you can't delete a row without unintentionally erasing other valuable information." The price data was coupled with the inventory data in the same table, so deleting inventory also destroyed pricing information.

Feedback:
- A) An insert anomaly prevents adding new data without supplying unrelated required fields. This scenario is about losing data through deletion, not being unable to insert.
- B) An update anomaly involves inconsistent modifications to redundant data. No data is being updated here — it's being deleted.
- C) A read anomaly involves ambiguous query results. The issue here is data loss from deletion, not confusing read results.

---

**Question 4:** A colleague argues: "We just need to be more careful when updating data — training will fix these problems." Why is this not a reliable solution to CRUD anomalies?
- A) Training is too expensive
- B) Anomalies are structural problems in the data model, not human errors — they can't be solved by being more careful
- C) Databases don't allow training
- D) Only managers need training, not developers

**Answer:** B) Anomalies are structural problems in the data model, not human errors — they can't be solved by being more careful
**Explanation:** CRUD anomalies arise from how the table is designed, not from user mistakes. Even a perfectly careful team will face ambiguity when the structure makes it unclear which of three onion rows to update. The solution is normalization — restructuring the tables to eliminate the root cause.

Feedback:
- A) Cost is not the primary issue. Even free training wouldn't fix structural problems in the data model.
- C) "Databases don't allow training" doesn't make sense as a reason - it's not even true, there are plenty of courses about databases. You're in one right now! The real issue is that no amount of user behavior change can fix a poorly structured table.
- D) Both managers and developers interact with data, but the anomaly exists regardless of who performs the operation. The table's structure is the problem.

---

**Question 5:** What is the general purpose of normalization in the context of database CRUD anomalies?
- A) Making all numbers positive
- B) Organizing tables into standard structures (normal forms) so that each fact is stored once and anomalies are avoided
- C) Deleting redundant databases
- D) Converting all text to uppercase

**Answer:** B) Organizing tables into standard structures (normal forms) so that each fact is stored once and anomalies are avoided
**Explanation:** The lesson defines normalization as "the process of organizing tables into standard structures called normal forms so that the data model reflects the domain cleanly and avoids common anomalies." By storing each fact in exactly one place, insert, update, and delete anomalies are eliminated.

Feedback:
- A) "Making all numbers positive" describes a mathematical operation, not a database design process. Normalization refers to organizing table structures in this context.
- C) Normalization reorganizes tables within a database — it doesn't involve deleting entire databases.
- D) Text case conversion is a data formatting concern, so it doesn't make sense in this context. Normalization is about structural organization to eliminate redundancy and anomalies here.

---

---

### **Quiz 3: Normalization Forms**

**Question 1:** A products table has a column called `price_history` that stores a JSON array like `[4.99, 5.49, 5.99]` in a single cell. Which normal form does this violate, and why?
- A) 2NF — there's a partial dependency
- B) 3NF — there's a transitive dependency
- C) 1NF — each cell should contain a single atomic value, not a list
- D) It doesn't violate any normal form

**Answer:** C) 1NF — each cell should contain a single atomic value, not a list
**Explanation:** First Normal Form "says that each cell in a table should contain a single value. Not a list, not a nested table, and not multiple pieces of information packed together." The lesson uses exactly this example — storing price history as JSON in one cell violates 1NF.

Feedback:
- A) 2NF addresses partial dependencies on a composite primary key. The issue here is a non-atomic value in a cell, which is a 1NF violation.
- B) 3NF addresses transitive dependencies between non-key columns. Storing a list in a single cell is a more fundamental problem addressed by 1NF.
- D) A JSON array containing multiple values in one cell violates 1NF's requirement for atomic (single) values per cell.

---

**Question 2:** You have a composite primary key of (store_id, item_name) on an inventory table. The `unit_price` column depends only on the item_name, not on which store carries it. Which normal form does this violate?
- A) 1NF
- B) 2NF
- C) 3NF
- D) No violation

**Answer:** B) 2NF — non-key columns must depend on the *entire* primary key, not just part of it
**Explanation:** "Second normal form also asks: do all of the other columns in the table depend on the entire primary key—and not just part of it?" If `unit_price` depends only on `item_name` (part of the composite key), it's a partial dependency — a 2NF violation. The fix is to move `unit_price` to a separate items table keyed on `item_name`.

Feedback:
- A) 1NF requires atomic values in each cell. The values here are atomic — the problem is which key they depend on, which is a 2NF concern.
- C) 3NF addresses dependencies between non-key columns. Here the dependency is between a non-key column and *part* of the primary key, which is a 2NF issue.
- D) There is a violation — `unit_price` depending on only part of the composite key is the textbook definition of a partial dependency (2NF violation).

---

**Question 3:** A price history table has columns: (item_id, date, base_price, on_sale, sale_price). The `sale_price` is always calculated as `base_price * 0.9` when `on_sale` is true. Why is this a 3NF violation?
- A) The table has too many columns
- B) `sale_price` depends on `base_price` and `on_sale` (non-key columns), creating a transitive dependency
- C) The primary key is wrong
- D) The table isn't in 1NF

**Answer:** B) `sale_price` depends on `base_price` and `on_sale` (non-key columns), creating a transitive dependency
**Explanation:** "3NF adds one more rule: No non-key column should depend on another non-key column." The lesson identifies `sale_price` depending on `base_price` and `on_sale` as "a transitive dependency, not a direct fact based on the item and date. That's a 3NF problem." The solution: store promotion rules separately and calculate `sale_price` on the fly.

Feedback:
- A) The number of columns in a table doesn't determine normalization violations. 3NF is about dependency relationships between columns, not column count.
- C) The composite primary key (item_id, date) is appropriate for a price history table. The problem is the transitive dependency among non-key columns.
- D) The table can be in 1NF (atomic values) and still violate 3NF. Normal forms are cumulative — a table can satisfy lower forms while violating higher ones.

---

**Question 4:** Why might a team use the item name as a "natural key" instead of a system-generated numeric ID?
- A) Natural keys are always faster to query
- B) They use intuitive, real-world attributes that are meaningful to humans, making the data easier to understand
- C) Databases require natural keys
- D) Numeric IDs are not supported by relational databases

**Answer:** B) They use intuitive, real-world attributes that are meaningful to humans, making the data easier to understand
**Explanation:** The lesson notes: "Sometimes, this type of primary key is also called a 'natural key' as it's fairly intuitive." Natural keys use domain-relevant attributes (like product names or email addresses). The trade-off is that natural keys can change or have duplicates — which is why composite keys or surrogate keys are sometimes preferred.

Feedback:
- A) Natural keys are not always faster — string comparisons are typically slower than integer comparisons. The advantage is readability and meaning, not performance.
- C) Databases don't require natural keys. Surrogate keys (auto-incrementing integers, UUIDs) are widely used and often preferred for performance.
- D) Numeric IDs are fully supported and commonly used in relational databases. They're often generated automatically via sequences or auto-increment.

---

**Question 5:** After normalizing a grocery table into separate `items`, `inventory`, and `price_history` tables, a developer complains that queries now require JOINs and are more complex. Is this a valid concern?
- A) No — normalized tables always perform better
- B) Yes — normalization trades some read query complexity for data integrity and reduced anomalies, which is usually worth it for OLTP
- C) No — JOINs have zero performance cost
- D) Yes — you should never normalize data

**Answer:** B) Yes — normalization trades some read query complexity for data integrity and reduced anomalies, which is usually worth it for OLTP
**Explanation:** Normalization eliminates redundancy and anomalies, but it does introduce JOINs. This is a deliberate trade-off: write-heavy OLTP systems benefit from normalization (reduced update anomalies, smaller writes), while read-heavy OLAP systems sometimes denormalize for query performance — this is exactly why star and snowflake schemas exist.

Feedback:
- A) Normalized tables don't always perform better — JOINs add overhead, and read-heavy OLAP workloads may be slower with heavily normalized schemas.
- C) JOINs are not free — they require the database to match and combine rows from multiple tables, which has real computational cost, especially on large datasets.
- D) Normalization is a well-established best practice for transactional databases. "Never normalize" would lead to rampant redundancy and anomalies.

---

**Question 6:** A team proposes storing promotion rules in a separate table and calculating sale prices by joining tables at query time, rather than storing the calculated value. Which normal form principle does this approach satisfy?
- A) 1NF — it ensures atomic values
- B) 2NF — it removes partial dependencies
- C) 3NF — it removes the transitive dependency by not storing a derived value
- D) None — this is about performance, not normalization

**Answer:** C) 3NF — it removes the transitive dependency by not storing a derived value
**Explanation:** The lesson proposes exactly this approach: "keep the price history table focused on the price on a given date, and move the promotion rules into a separate table... Any query that needs to know the sale price can join the two tables together and calculate it on the fly." This eliminates the transitive dependency where `sale_price` depended on other non-key columns.

Feedback:
- A) 1NF ensures atomic values in each cell. Separating tables doesn't address atomicity — it addresses a dependency between non-key columns.
- B) 2NF removes partial dependencies on composite keys. This scenario involves a transitive dependency between non-key columns, which is a 3NF concern.
- D) This is directly about normalization. Removing a derived column that depends on other non-key columns is the textbook 3NF fix.

---

---

### **Quiz 4: Star and Snowflake Schemas**

**Question 1:** A retail company wants to analyze sales by product, store, date, and customer demographics. An architect proposes a central `fact_sales` table surrounded by `dim_product`, `dim_store`, `dim_date`, and `dim_customer` tables. What is this design pattern called?
- A) Third Normal Form
- B) Star Schema
- C) Entity-Relationship Diagram
- D) Graph Database

**Answer:** B) Star Schema
**Explanation:** A star schema consists of one or more central fact tables (containing measurable metrics and foreign keys) surrounded by dimension tables (containing descriptive attributes). The star-like pattern emerges from the fact table at the center connected to each dimension.

Feedback:
- A) Third Normal Form is a normalization standard for reducing redundancy in OLTP databases. Star schema dimnension tables are intentionally denormalized sometimes for OLAP analytical queries.
- C) An Entity-Relationship Diagram is a visual modeling tool that shows entities and their relationships. It's a diagram technique, not a schema design pattern.
- D) A graph database stores data as nodes and edges. The design described here — fact and dimension tables — is a relational schema pattern for analytics.

---

**Question 2:** In a star schema, the `fact_sales` table contains `sale_amount`, `quantity`, and foreign keys to dimension tables. What kind of data belongs in the fact table versus the dimension tables?
- A) Fact tables store descriptions; dimension tables store numbers
- B) Fact tables store measurable, quantitative metrics; dimension tables store descriptive attributes for filtering and grouping
- C) Both store the same types of data
- D) Fact tables store only primary keys

**Answer:** B) Fact tables store measurable, quantitative metrics; dimension tables store descriptive attributes for filtering and grouping
**Explanation:** Fact tables hold business metrics (sales amounts, quantities, costs) and foreign keys linking to dimensions. Dimension tables hold attributes you filter or group by (product names, store locations, date components, customer demographics).

Feedback:
- A) This reverses the roles. Fact tables store numeric metrics; dimension tables store the descriptive context used for filtering and grouping.
- C) Fact and dimension tables serve fundamentally different purposes — metrics vs. descriptive attributes. Conflating them defeats the purpose of the star schema design.
- D) Fact tables store metrics and foreign keys, not just primary keys. The foreign keys link to dimension tables, but the metrics (sale_amount, quantity) are the core content.

---

**Question 3:** The `dim_product` table contains a `product_category` field alongside product name, description, and price. A colleague suggests extracting `product_category` into its own `dim_category` table. What does this transformation create?
- A) A simpler star schema
- B) A snowflake schema — where dimension tables are further normalized into sub-dimensions
- C) A denormalized table
- D) An OLTP schema

**Answer:** B) A snowflake schema — where dimension tables are further normalized into sub-dimensions
**Explanation:** Snowflake schemas extend star schemas by normalizing dimension tables into additional related tables. Extracting the category into its own table reduces redundancy (e.g., "Electronics" stored once instead of repeated per product) but adds a JOIN.

Feedback:
- A) Extracting sub-dimensions makes the schema more complex, not simpler. A star schema keeps all dimension attributes in one table per dimension.
- C) Extracting a field into a separate table is normalization (reducing redundancy), the opposite of denormalization.
- D) An OLTP schema is optimized for transactional writes. Star and snowflake schemas are OLAP patterns designed for analytical reads.

---

**Question 4:** An analyst runs a query that joins the fact table to four dimension tables. In which schema design would this query typically need *fewer* total JOINs?
- A) Snowflake schema — because it has more tables, there are fewer JOINs per query
- B) Star schema — because dimensions are denormalized, so fewer tables need to be joined
- C) Both require exactly the same number of JOINs
- D) Neither schema uses JOINs

**Answer:** B) Star schema — because dimensions are denormalized, so fewer tables need to be joined
**Explanation:** Star schemas keep dimensions denormalized (all attributes in one table per dimension), so queries only JOIN fact-to-dimension. Snowflake schemas split dimensions into sub-tables, requiring additional JOINs (e.g., product → category → department).

Feedback:
- A) More tables means more JOINs, not fewer. Snowflake schemas require additional JOINs to traverse the normalized dimension hierarchy.
- C) They don't require the same number — snowflake schemas add extra JOINs for each normalized sub-dimension table.
- D) Both schemas rely heavily on JOINs to connect fact tables to dimension tables. JOINs are fundamental to how star and snowflake schemas work.

---

**Question 5:** When would a snowflake schema be preferred over a star schema?
- A) When query simplicity is the only priority
- B) When reducing data redundancy and storage costs matters more than minimizing JOINs
- C) When the database doesn't support JOINs
- D) When there are no dimension tables

**Answer:** B) When reducing data redundancy and storage costs matters more than minimizing JOINs
**Explanation:** Snowflake schemas eliminate redundancy in dimension tables (e.g., category names stored once rather than repeated per product). The trade-off is more JOINs for queries. This is valuable when storage efficiency and data consistency are priorities.

Feedback:
- A) If query simplicity is the only priority, a star schema is better — it has fewer JOINs and simpler queries. Snowflake schemas add query complexity.
- C) Both star and snowflake schemas rely on JOINs. If a database didn't support JOINs, neither schema would work.
- D) Both star and snowflake schemas are built around dimension tables. Without dimensions, you'd have just a flat fact table with no filtering or grouping context.

---

---

### **Quiz 5: AWS RDS and Cloud Database Management**

**Question 1:** A startup needs to run PostgreSQL in production. They're comparing self-hosting on a server in the office vs. using AWS RDS. Which best describes what RDS provides?
- A) A desktop application for writing SQL
- B) A managed relational database service that handles provisioning, backups, patching, and scaling
- C) A free PostgreSQL license
- D) An open-source replacement for PostgreSQL

**Answer:** B) A managed relational database service that handles provisioning, backups, patching, and scaling
**Explanation:** AWS RDS automates infrastructure management — backups, security patches, scaling, and monitoring — so the team can focus on their application rather than database administration.

Feedback:
- A) RDS is a cloud service, not a desktop application. You interact with it through the AWS console, CLI, or APIs, and connect via standard database clients.
- C) PostgreSQL is already open-source and free to use. RDS provides managed infrastructure on top of PostgreSQL, not a license.
- D) RDS runs PostgreSQL (and other engines) as a managed service — it doesn't replace PostgreSQL, it hosts and manages it for you.

---

**Question 2:** An operations team wants to push a major database version upgrade without downtime. AWS offers a feature where a parallel environment is set up, tested, and traffic is switched over seamlessly. What is this called?
- A) Hot/Cold migration
- B) Blue/Green Deployment
- C) Sharding
- D) Normalization

**Answer:** B) Blue/Green Deployment
**Explanation:** Blue/Green deployments create a parallel "green" environment where changes are tested, while the "blue" environment continues serving traffic. Once validated, traffic switches to the green environment with minimal or zero downtime.

Feedback:
- A) Hot/cold migration refers to data temperature tiers or moving workloads between active and archival systems — it's not a zero-downtime deployment strategy.
- C) Sharding distributes data across multiple machines for horizontal scaling. It doesn't address zero-downtime version upgrades.
- D) Normalization is a database design technique for reducing redundancy. It has nothing to do with deployment or upgrade strategies.

---

**Question 3:** Following security best practices, where should database credentials be stored when connecting an application to AWS RDS?
- A) Hard-coded in the application source code
- B) In a secure service like AWS Secrets Manager
- C) In a shared spreadsheet accessible to the team
- D) In the database itself as a table row

**Answer:** B) In a secure service like AWS Secrets Manager
**Explanation:** AWS Secrets Manager provides secure storage, rotation, and retrieval of credentials. Hard-coding credentials in source code or sharing them in documents creates security vulnerabilities.

Feedback:
- A) Hard-coded credentials in source code are visible to anyone with repository access and are a major security risk. They can't be rotated without code changes.
- C) Spreadsheets lack encryption, access controls, and audit trails. Sharing credentials this way exposes them to anyone with file access.
- D) Storing credentials inside the database creates a circular dependency and exposes them to anyone who can query the table.

---

**Question 4:** Which of the following database engines does AWS RDS support?
- A) Only PostgreSQL
- B) PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server among others
- C) Only NoSQL databases
- D) Only MongoDB

**Answer:** B) PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server among others
**Explanation:** RDS supports multiple relational database engines, giving teams flexibility to choose the engine that best fits their needs while still benefiting from managed infrastructure.

Feedback:
- A) RDS supports many engines beyond PostgreSQL, including MySQL, MariaDB, Oracle, and SQL Server.
- C) RDS is specifically for relational databases. AWS offers separate services for NoSQL (DynamoDB, DocumentDB, etc.).
- D) MongoDB is a document database, not a relational one. AWS offers DocumentDB (with MongoDB compatibility) as a separate service, not through RDS.
