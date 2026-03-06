# Lesson 3: Data Modeling for Document Stores and NoSQL — Quizzes

---

### **Quiz 1: NoSQL and MongoDB Fundamentals**

**Question 1:** A development team's data model changes frequently as the product evolves — new fields are added weekly, and some documents have attributes others don't. Which database paradigm is designed for this kind of flexibility?
- A) A strictly normalized relational database
- B) A document store (NoSQL)
- C) A graph database
- D) A spreadsheet

**Answer:** B) A document store (NoSQL) — where schemas are flexible and fields can vary between documents
**Explanation:** The lesson explains that document databases are "built on the opposite assumption: different documents might have different fields, and the structure can evolve over time." As the lesson notes, "businesses needed systems that could stay online as their schema changed. No downtime. No waiting for a DBA to run a migration. No strict table structures getting in the way."

Feedback:
- A) A strictly normalized relational database requires schema changes (ALTER TABLE, migrations) to add new fields — exactly the kind of friction this team wants to avoid.
- C) Graph databases excel at relationship traversal, but the scenario describes frequently changing field structures, not relationship-heavy data.
- D) Spreadsheets can be flexible, but they aren't databases — they lack query engines, concurrency control, indexing, and scaling capabilities.

---

**Question 2:** MongoDB stores data internally as BSON. How does this relate to what developers interact with?
- A) Developers must write raw binary code
- B) BSON is binary JSON 
- C) BSON is completely unrelated to JSON
- D) Developers must convert BSON manually before reading data

**Answer:** B) BSON is binary JSON — MongoDB stores it as binary for efficiency, but developers interact with it as standard JSON
**Explanation:** "Internally, MongoDB stores data as BSON—binary JSON—for efficiency, but to developers and applications, it behaves just like JSON." This gives the best of both worlds: efficient storage and a developer-friendly interface.

Feedback:
- A) Developers interact with standard JSON syntax, not raw binary code. MongoDB handles the BSON conversion transparently.
- C) BSON is directly derived from JSON — it's the binary-encoded representation of JSON documents, specifically designed for JSON-like data.
- D) The conversion between JSON and BSON is handled automatically by MongoDB and its drivers. Developers never need to convert manually.

---

**Question 3:** A relational database developer is learning MongoDB. They're used to "tables," "rows," and "columns." Match each relational database term to its MongoDB equivalent.

Column A:
1. Table
2. Row
3. Column

Column B:
A. Collection
B. Document
C. Field

**Answer:** 1→A, 2→B, 3→C
**Explanation:** The lesson provides this mapping: "A 'collection' is roughly like a 'table'. A 'document' is roughly like a 'row'. Fields within a document behave a lot like columns." While the analogy isn't perfect (documents can have nested structures and variable fields), it helps relational developers build mental models.

Feedback:
- 1→A: A collection groups related documents together, similar to how a table groups related rows. Both serve as the organizational container for a set of records.
- 2→B: A document is one record (a JSON/BSON object with key-value pairs), similar to how a row is one record in a relational table.
- 3→C: A field is a key within a document, similar to how a column is a named attribute in a table’s row.

---

**Question 4:** A security team wants to add a "login_attempts" field to user records, but only for users who have failed a login. In a relational database, you'd ALTER the table and add a nullable column. What's different in a document database?
- A) You can't add new fields at all
- B) You simply include the field in relevant documents 
- C) You must delete and recreate the entire collection
- D) You need to create a new collection for users with failed logins

**Answer:** B) You simply include the field in relevant documents — no schema change, no migration, no downtime
**Explanation:** The lesson uses a similar example: "In a document database, you simply start including the field when it's relevant. No schema change. No downtime. No refactoring half the application just to add one new piece of information." Documents in the same collection can have different fields.

Feedback:
- A) Document databases are specifically designed for flexible schemas — adding fields to individual documents is a core capability.
- C) There's no need to recreate a collection to add a field. Documents within a collection are schema-independent.
- D) Creating a separate collection would fragment your user data unnecessarily. The flexibility of document stores means one collection can hold documents with varying fields.

---

**Question 5:** A developer says: "Redis and MongoDB are basically the same since they're both NoSQL." Why is this incorrect?
- A) Redis is a relational database
- B) Redis is a key-value store (simple lookups only); MongoDB is a document store that supports sorting, filtering, and complex queries on fields
- C) They use the same query language
- D) MongoDB doesn't support NoSQL operations

**Answer:** B) Redis is a key-value store (simple lookups only); MongoDB is a document store that supports sorting, filtering, and complex queries on fields
**Explanation:** "Key-value systems like Redis don't organize fields into documents. All they have is the key and the corresponding data. They're very fast for simple lookups, but don't support sorting or filtering like document stores do." The NoSQL label covers a wide range of very different database types.

Feedback:
- A) Redis is not relational — it's a NoSQL key-value store. But being "NoSQL" doesn't make it the same as MongoDB.
- C) Redis and MongoDB use completely different query interfaces. Redis uses simple commands (GET, SET), while MongoDB uses MQL with operators like `$match`, `$set`, etc.
- D) MongoDB is one of the most widely used NoSQL databases with full CRUD and aggregation support.

---

**Question 6:** The lesson describes several forces that drove the creation of document databases. Which of the following were driving forces behind the creation of document databases? (Select all that apply)
- A) Businesses needed systems that could evolve without downtime or rigid schema migrations
- B) Web, mobile, and event-driven systems produced unstructured or semi-structured data
- C) Developers wanted simpler syntax than SQL
- D) NoSQL databases were created to fully replace relational databases

**Answer:** A, B
**Explanation:** The lesson states: "businesses needed systems that could stay online as their schema changed. No downtime. No waiting for a DBA to run a migration. No strict table structures getting in the way. These pressures led to a new type of database—one that stores entire documents, not rows." It also notes that "the web, mobile apps, and event-driven systems produce unstructured or semi-structured data—often in JSON format."

Feedback:
- A) ✅ The lesson explicitly describes the need for systems that "could stay online as their schema changed. No downtime. No waiting for a DBA to run a migration."
- B) ✅ The lesson notes that "the web, mobile apps, and event-driven systems produce unstructured or semi-structured data—often in JSON format" as a key driver.
- C) Syntax convenience was not the driving force. The lesson emphasizes operational flexibility, schema evolution, and the ability to handle unstructured and semi-structured data at scale.
- D) The lesson clarifies that NoSQL stands for "not only SQL"—it refers to non-relational databases that complement, not replace, relational ones.

---

---

### **Quiz 2: CRUD Operations in Document Databases**

**Question 1:** In MongoDB, what does the `$` prefix signify in operators like `$set`, `$unset`, and `$push`?
- A) A variable reference
- B) It tells MongoDB "what follows is an instruction, not data" — it distinguishes operators from field values
- C) A comment marker
- D) A currency symbol for monetary fields

**Answer:** B) It tells MongoDB "what follows is an instruction, not data" — it distinguishes operators from field values
**Explanation:** "The dollar sign tells MongoDB: 'What follows is an instruction, not data.'" This convention prevents ambiguity between operators and actual data values in update commands.

Feedback:
- A) `$` in MongoDB is not a variable reference (as it might be in other languages you may hav seen). It's a reserved prefix for MongoDB operators and expressions.
- C) Comments in MongoDB use `//` or are not part of the query syntax. The `$` prefix signals operators, not comments.
- D) The `$` has no relationship to currency. It's a syntactic convention for distinguishing operators from data field names and values.

---

**Question 2:** You want to change a user's email address in MongoDB without touching any other fields. Which operator would you use?
- A) `$push` — to append the new email
- B) `$set` — to update only the specified field
- C) `$unset` — to remove and re-add the field
- D) `$pull` — to extract the email

**Answer:** B) `$set` — to update only the specified field
**Explanation:** The lesson describes `$set` as used "to change or add a field." Critically, "MongoDB doesn't rewrite the whole row—MQL operators surgically update only what you specify." So `$set: { email: "new@example.com" }` changes just the email field.

Feedback:
- A) `$push` appends a value to an array field. It doesn't replace an existing scalar value like an email address.
- C) `$unset` removes a field entirely. Using it to "remove and re-add" would be a two-step workaround when `$set` does the job in one operation.
- D) `$pull` removes a specific value from an array. It's not used for updating scalar field values.

---

**Question 3:** How does MongoDB's approach to updates differ fundamentally from SQL's UPDATE?
- A) MongoDB is always slower
- B) MongoDB operators surgically update only specified fields without rewriting the entire document; SQL rewrites the whole row
- C) SQL can update fields; MongoDB cannot
- D) There is no difference

**Answer:** B) MongoDB operators surgically update only specified fields without rewriting the entire document; SQL engines usually rewrite the whole row
**Explanation:** "This is one of the biggest differences from SQL. MongoDB doesn't rewrite the whole row—MQL operators surgically update only what you specify." This targeted approach can be more efficient for documents with many fields when only one needs to change.

Feedback:
- A) Speed depends on the workload and implementation. MongoDB's surgical updates can actually be faster for targeted field changes on large documents.
- C) Both SQL and MongoDB can update fields. The difference is in *how* — MongoDB targets specific fields while SQL engines usually replace the entire row.
- D) There is a significant architectural difference in how updates are processed, as the lesson explicitly highlights.

---

**Question 4:** You need to delete all orders from 2023 in MongoDB. A colleague says: "You can filter on any field." If you tried the same thing in DynamoDB, what limitation would you hit?
- A) DynamoDB doesn't support deletion
- B) DynamoDB can only delete by primary key, not by arbitrary filters
- C) DynamoDB deletes are identical to MongoDB
- D) DynamoDB deletes entire collections at once

**Answer:** B) DynamoDB can only delete by primary key, not by arbitrary filters
**Explanation:** "MongoDB can delete based on any filter, while DynamoDB can only delete based on the item's primary key." This is a significant architectural difference — in DynamoDB, you'd need to first query for matching items' keys, then delete each individually.

Feedback:
- A) DynamoDB does support deletion — but only by specifying the item's primary key, not by arbitrary field filters.
- C) They are not identical. MongoDB supports filter-based deletion on any field; DynamoDB requires the primary key for each delete operation.
- D) DynamoDB deletes individual items by key, not entire tables/collections at once. There's no bulk "delete by filter" operation.

---

**Question 5:** A developer is comparing MongoDB, DynamoDB, and Firestore syntax for locating records. MongoDB uses `$` operators, DynamoDB uses `:` for placeholders, and Firestore uses `==`. What underlying design problem are all three solving?
- A) Encryption
- B) Separating query instructions from data values so the database can distinguish commands from content
- C) Data compression
- D) User authentication

**Answer:** B) Separating query instructions from data values so the database can distinguish commands from content
**Explanation:** Each document store needs a way to tell the database "this is an operator" versus "this is a data value." MongoDB uses `$`, DynamoDB uses `:` placeholders, and Firestore uses `==`. Different syntax, same fundamental need to prevent ambiguity between instructions and data.

Feedback:
- A) Encryption protects data confidentiality. The different syntax conventions are about query parsing, not security.
- C) Data compression reduces storage size. Query operator syntax has nothing to do with compression.
- D) User authentication verifies identity. Query syntax conventions separate operators from data values, which is a parsing concern, not a security one.

---

---

### **Quiz 3: MongoDB Aggregation Pipelines**

**Question 1:** A product manager wants to see monthly revenue broken down by product category for the past year. In MongoDB, which feature would you use to build this multi-step analysis?
- A) A simple find() query
- B) An aggregation pipeline — a sequence of stages that filter, reshape, group, and sort documents
- C) A map-Reduce function
- D) A manual export to spreadsheet

**Answer:** B) An aggregation pipeline — a sequence of stages that filter, reshape, group, and sort documents
**Explanation:** "An aggregation pipeline is an Extract, Transform, Load framework that MongoDB provides for performing advanced data analysis and manipulation on collections. It processes documents through a sequence of stages—filtering, reshaping, grouping, sorting, or joining."

Feedback:
- A) A simple `find()` query can filter and return documents, but it can't group, aggregate, reshape, or compute metrics like monthly revenue breakdowns.
- C) `map-Reduce` is an older MongoDB feature for data processing. Aggregation pipelines are the modern, preferred approach — more flexible, better optimized, and easier to compose.
- D) Exporting to a spreadsheet moves analysis outside the database, defeating the purpose of using MongoDB's built-in capabilities for performant in-database processing.

---

**Question 2:** You need to enrich each order document with matching customer information from a separate collection. Match each aggregation pipeline stage to the SQL operation it is most similar to.

Column A:
1. `$group`
2. `$lookup`
3. `$match`
4. `$sort`

Column B:
A. GROUP BY
B. LEFT OUTER JOIN
C. WHERE
D. ORDER BY

**Answer:** 1→A, 2→B, 3→C, 4→D
**Explanation:** "The 'lookup' stage performs an operation similar to a left outer join between two collections." Each aggregation stage has a direct SQL analog: `$group` groups documents by a key (GROUP BY), `$lookup` joins data from another collection (LEFT OUTER JOIN), `$match` filters documents (WHERE), and `$sort` orders results (ORDER BY).

Feedback:
- 1→A: `$group` aggregates documents by a specified key, producing one output document per group — directly analogous to SQL's GROUP BY clause.
- 2→B: `$lookup` enriches documents by pulling in matching documents from another collection — the lesson explicitly compares it to a LEFT OUTER JOIN.
- 3→C: `$match` filters documents based on criteria, passing only matching documents to the next stage — equivalent to SQL's WHERE clause.
- 4→D: `$sort` orders the result set by specified fields — equivalent to SQL's ORDER BY clause.

---

**Question 3:** A developer proposes using `$lookup` extensively throughout the application to join collections together, similar to how they'd use JOINs in PostgreSQL. Why might this be problematic?
- A) `$lookup` doesn't exist in MongoDB
- B) Unlike optimized SQL joins, `$lookup` is more expensive — it's powerful but not something to rely on for every query
- C) `$lookup` only works on a single collection
- D) There's no issue — `$lookup` and SQL JOINs perform identically

**Answer:** B) Unlike optimized SQL joins, `$lookup` is more expensive — it's powerful but not something to rely on for every query
**Explanation:** The lesson warns: it's powerful—but not free. Unlike optimized SQL joins, MongoDB's 'lookup' is more expensive. It's powerful, but not something you rely on for every query. Document databases are designed to minimize the need for joins by embedding related data — heavy `$lookup` use may indicate a modeling problem.

Feedback:
- A) `$lookup` absolutely exists in MongoDB and is a core aggregation pipeline stage for cross-collection operations.
- C) `$lookup` works across two collections — that's its primary purpose. It joins a "from" collection to the current pipeline's collection.
- D) There is a meaningful performance difference. SQL databases have decades of JOIN optimization (indexes, hash joins, merge joins), while `$lookup` in MongoDB is less optimized by design.

---

**Question 4:** In a MongoDB aggregation pipeline, you see `$sum: 1` inside a `$group` stage. What does this compute?
- A) The sum of all field values
- B) A count of documents in each group (each document contributes 1 to the total)
- C) The literal number 1 stored in each group
- D) The sum of all numeric fields

**Answer:** B) A count of documents in each group (each document contributes 1 to the total)
**Explanation:** The lesson states: "'sum colon one', which counts documents." Each document adds 1 to the running total, effectively counting how many documents belong to each group — similar to SQL's COUNT(*).

Feedback:
- A) `$sum: 1` adds 1 per document, not the value of any field. To sum a field's values, you'd use `$sum: "$fieldName"` instead.
- C) `$sum: 1` produces a running count as an accumulator across documents in a group, not a static literal value stored once.
- D) `$sum: 1` doesn't reference any fields — it simply adds 1 for each document encountered, resulting in a count.

---

**Question 5:** You're designing a MongoDB data pipeline that needs to: (1) filter orders from 2024, (2) join customer data, (3) group by region, and (4) sort by total revenue. How would you structure this?
- A) Four separate queries run independently
- B) A single aggregation pipeline with stages: `$match` → `$lookup` → `$group` → `$sort`
- C) A single find() query with multiple parameters
- D) Export to CSV and process in a spreadsheet

**Answer:** B) A single aggregation pipeline with stages: `$match` → `$lookup` → `$group` → `$sort`
**Explanation:** Aggregation pipelines process documents through a sequence of stages. Each stage transforms the data and passes it to the next. The order matters: filter first ($match) to reduce the dataset, enrich with customer data ($lookup), then aggregate ($group), and finally order the results ($sort).

Feedback:
- A) Running four separate queries loses the ability to chain transformations. Each stage depends on the output of the previous one, so they must be in a single pipeline.
- C) `find()` can filter and project but can't group, aggregate, join collections, or sort by computed values. This analysis requires pipeline stages.
- D) Exporting to CSV and processing externally is inefficient and defeats the purpose of MongoDB's built-in aggregation framework.

---

---

### **Quiz 4: MongoDB Atlas and Cloud NoSQL**

**Question 1:** A team currently runs MongoDB on their own servers. They find that managing infrastructure, replication, backups, and patching takes significant effort. Which of the following does MongoDB Atlas provide? (Select all that apply)
- A) A fully managed MongoDB experience
- B) Replication, sharding, backups, and monitoring
- C) Deployment across multiple cloud providers (AWS, GCP, Azure)
- D) A relational database wrapper around MongoDB

**Answer:** A, B, C
**Explanation:** The lesson describes MongoDB Atlas as "the official cloud service from the developers of MongoDB" that "provides a fully managed MongoDB experience, including replication, sharding, backups, and monitoring." It also notes that "Atlas also lets you deploy to several cloud infrastructure vendors, such as AWS, Google Cloud Platform, or Azure."

Feedback:
- A) ✅ Atlas is "the official cloud service from the developers of MongoDB" providing a "fully managed MongoDB experience."
- B) ✅ The lesson explicitly states Atlas includes "replication, sharding, backups, and monitoring" as managed features.
- C) ✅ The lesson notes Atlas "lets you deploy to several cloud infrastructure vendors, such as AWS, Google Cloud Platform, or Azure."
- D) Atlas runs MongoDB natively — it's not a relational wrapper. It provides the full MongoDB document model and query capabilities.

---

**Question 2:** Your MongoDB Atlas cluster needs to handle varying workloads without constant manual intervention. According to the lesson, how does Atlas help manage changing resource demands?
- A) By requiring manual capacity planning for every workload change
- B) By autoscaling compute and storage based on usage patterns
- C) By deleting old data automatically when storage is full
- D) By limiting the number of concurrent queries

**Answer:** B) By autoscaling compute and storage based on usage patterns
**Explanation:** The lesson states that with Atlas, "you can autoscale your cluster's compute and storage based on usage patterns, so you don't have to constantly guess at the right instance sizes or worry about running out of capacity."

Feedback:
- A) Atlas specifically reduces the need for manual capacity planning. The lesson highlights that autoscaling means you "don't have to constantly guess at the right instance sizes."
- C) Atlas autoscales resources — it doesn't delete data to free space. Storage scaling is handled automatically based on demand patterns.
- D) Atlas handles workload scaling, not query throttling. Autoscaling adjusts compute and storage resources to match actual usage, not limit it.

---

**Question 3:** A single MongoDB server is hitting its storage and throughput limits. You need to distribute data across multiple machines. What is this called in MongoDB?
- A) Replication
- B) Sharding 
- C) Indexing
- D) Aggregation

**Answer:** B) Sharding — splitting data across multiple machines to scale horizontally
**Explanation:** Sharding is the term MongoDB uses for splitting your data across multiple machines to scale horizontally. Sharding addresses one machine's limits by distributing the data across multiple machines. This is horizontal scaling — adding more machines rather than making one bigger.

Feedback:
- A) Replication creates copies of data for redundancy and read scaling, but each replica holds the full dataset. It doesn't distribute data across machines to overcome storage limits.
- C) Indexing speeds up queries by creating lookup structures, but it doesn't address fundamental storage or throughput limits of a single machine.
- D) Aggregation is a query framework for data analysis. It doesn't distribute data across machines or scale the database infrastructure.

---

**Question 4:** A solutions architect is comparing MongoDB Atlas and Amazon DynamoDB for a new project. Based on the lesson, what is a key difference between these two services?
- A) They are identical in architecture and capabilities
- B) Atlas can deploy across multiple cloud providers (AWS, GCP, Azure), while DynamoDB offers a serverless integrated AWS experience with more constrained access patterns but extremely low operational overhead
- C) DynamoDB supports all MongoDB features
- D) Atlas only runs on AWS

**Answer:** B) Atlas can deploy across multiple cloud providers (AWS, GCP, Azure), while DynamoDB offers a serverless AWS experience with more constrained access patterns but extremely low operational overhead
**Explanation:** The lesson describes Atlas as letting you "deploy to several cloud infrastructure vendors, such as AWS, Google Cloud Platform, or Azure." For DynamoDB, the lesson notes it "offers a 'serverless' experience—you don't manage instances or clusters at all" and "makes different tradeoffs than MongoDB: access patterns are more constrained, but operational overhead is extremely low."

Feedback:
- A) They have fundamentally different architectures and deployment models. Atlas is multi-cloud with managed clusters; DynamoDB is AWS-only and serverless. Their access patterns and tradeoffs differ significantly.
- C) DynamoDB makes different tradeoffs than MongoDB — access patterns are more constrained. They are distinct database services with different capabilities and query models.
- D) Atlas explicitly supports multiple cloud providers — AWS, Google Cloud Platform, and Azure — as stated in the lesson.

---