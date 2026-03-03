# Lesson 3: Data Modeling for Document Stores and NoSQL — Quizzes

---

### **Quiz 1: NoSQL and MongoDB Fundamentals**

**Question 1:** A development team's data model changes frequently as the product evolves — new fields are added weekly, and some documents have attributes others don't. Which database paradigm is designed for this kind of flexibility?
- A) A strictly normalized relational database
- B) A document store (NoSQL) — where schemas are flexible and fields can vary between documents
- C) A graph database
- D) A spreadsheet

**Answer:** B) A document store (NoSQL) — where schemas are flexible and fields can vary between documents
**Explanation:** The lesson explains that NoSQL databases were created because the idea was "to create databases that didn't force everything into a strict, predefined schema." In a document database, "if you want to add a note, leave a field blank, or tack on a new attribute you didn't plan for, you just do it. No schema changes, migrations, or table redesigns."

Feedback:
- A) A strictly normalized relational database requires schema changes (ALTER TABLE, migrations) to add new fields — exactly the kind of friction this team wants to avoid.
- C) Graph databases excel at relationship traversal, but the scenario describes frequently changing field structures, not relationship-heavy data.
- D) Spreadsheets can be flexible, but they aren't databases — they lack query engines, concurrency control, indexing, and scaling capabilities.

---

**Question 2:** MongoDB stores data internally as BSON. How does this relate to what developers interact with?
- A) Developers must write raw binary code
- B) BSON is binary JSON — MongoDB stores it as binary for efficiency, but developers interact with it as standard JSON
- C) BSON is completely unrelated to JSON
- D) Developers must convert BSON manually before reading data

**Answer:** B) BSON is binary JSON — MongoDB stores it as binary for efficiency, but developers interact with it as standard JSON
**Explanation:** "Internally, MongoDB stores data as BSON—binary JSON—for efficiency, but to developers and applications, it behaves just like JSON." This gives the best of both worlds: efficient storage and a developer-friendly interface.

Feedback:
- A) Developers interact with standard JSON syntax, not raw binary code. MongoDB handles the BSON conversion transparently.
- C) BSON is directly derived from JSON — it's the binary-encoded representation of JSON documents, specifically designed for JSON-like data.
- D) The conversion between JSON and BSON is handled automatically by MongoDB and its drivers. Developers never need to convert manually.

---

**Question 3:** A relational database developer is learning MongoDB. They're used to "tables," "rows," and "columns." What are the MongoDB equivalents?
- A) Graphs, nodes, edges
- B) Collections, documents, fields
- C) Buckets, objects, attributes
- D) Schemas, records, keys

**Answer:** B) Collections, documents, fields
**Explanation:** The lesson provides this mapping: "A 'collection' is roughly like a 'table'. A 'document' is roughly like a 'row'. Fields within a document behave a lot like columns." While the analogy isn't perfect (documents can have nested structures and variable fields), it helps relational developers build mental models.

Feedback:
- A) Graphs, nodes, and edges are the building blocks of graph databases (like Neo4j), not document stores like MongoDB.
- C) "Buckets, objects, attributes" is not standard MongoDB terminology. MongoDB uses collections, documents, and fields.
- D) "Schemas, records, keys" doesn't map to MongoDB's structure. MongoDB collections don't enforce schemas, and "records" isn't the preferred MongoDB term.

---

**Question 4:** A security team wants to add a "login_attempts" field to user records, but only for users who have failed a login. In a relational database, you'd ALTER the table and add a nullable column. What's different in a document database?
- A) You can't add new fields at all
- B) You simply include the field in relevant documents — no schema change, no migration, no downtime
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

**Question 6:** MongoDB was born from an ad platform handling 400,000 ads per second. DynamoDB was built to survive Amazon's holiday traffic spikes. Cassandra powered Facebook's inbox search. What common theme drove the creation of these NoSQL databases?
- A) They were all built for small-scale applications
- B) Each was designed to handle massive scale and workloads that traditional relational schemas couldn't accommodate efficiently
- C) They all replaced SQL entirely
- D) They were all created by the same company

**Answer:** B) Each was designed to handle massive scale and workloads that traditional relational schemas couldn't accommodate efficiently
**Explanation:** The lesson mentions these origin stories to highlight that NoSQL databases were purpose-built for extreme scale. "The principle was, to build a platform that could handle large volumes of unstructured data." Each system emerged from a real-world problem where traditional approaches hit their limits.

Feedback:
- A) The opposite is true — each was built specifically because small-scale solutions couldn't handle the volume (400K ads/sec, holiday spikes, billions of inbox messages).
- C) None of these databases "replaced SQL entirely." SQL databases remain widely used alongside NoSQL. These tools serve different use cases.
- D) MongoDB was created by 10gen, DynamoDB by Amazon, and Cassandra by Facebook. They were built by different companies facing different scale challenges.

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
- A) `$` in MongoDB is not a variable reference (as it might be in shell scripting or PHP). It's a reserved prefix for MongoDB operators and expressions.
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

**Answer:** B) MongoDB operators surgically update only specified fields without rewriting the entire document; SQL rewrites the whole row
**Explanation:** "This is one of the biggest differences from SQL. MongoDB doesn't rewrite the whole row—MQL operators surgically update only what you specify." This targeted approach can be more efficient for documents with many fields when only one needs to change.

Feedback:
- A) Speed depends on the workload and implementation. MongoDB's surgical updates can actually be faster for targeted field changes on large documents.
- C) Both SQL and MongoDB can update fields. The difference is in *how* — MongoDB targets specific fields while SQL conceptually replaces the entire row.
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
- C) A mapReduce function
- D) A manual export to spreadsheet

**Answer:** B) An aggregation pipeline — a sequence of stages that filter, reshape, group, and sort documents
**Explanation:** "An aggregation pipeline is an Extract, Transform, Load framework that MongoDB provides for performing advanced data analysis and manipulation on collections. It processes documents through a sequence of stages—filtering, reshaping, grouping, sorting, or joining."

Feedback:
- A) A simple `find()` query can filter and return documents, but it can't group, aggregate, reshape, or compute metrics like monthly revenue breakdowns.
- C) `mapReduce` is an older MongoDB feature for data processing. Aggregation pipelines are the modern, preferred approach — more flexible, better optimized, and easier to compose.
- D) Exporting to a spreadsheet moves analysis outside the database, defeating the purpose of using MongoDB's built-in capabilities for performant in-database processing.

---

**Question 2:** You need to enrich each order document with matching customer information from a separate collection. Which aggregation pipeline stage performs this, and what SQL operation is it similar to?
- A) `$group` — similar to GROUP BY
- B) `$lookup` — similar to a LEFT OUTER JOIN
- C) `$match` — similar to WHERE
- D) `$sort` — similar to ORDER BY

**Answer:** B) `$lookup` — similar to a LEFT OUTER JOIN
**Explanation:** "The 'lookup' stage performs an operation similar to a left outer join between two collections. In this example, it enriches each 'order' document by attaching matching documents from 'customers'."

Feedback:
- A) `$group` aggregates documents by a key (like SQL's GROUP BY). It doesn't join data from separate collections.
- C) `$match` filters documents within a single collection (like SQL's WHERE). It can't pull in data from another collection.
- D) `$sort` orders results (like SQL's ORDER BY). It operates on existing fields and doesn't introduce data from other collections.

---

**Question 3:** A developer proposes using `$lookup` extensively throughout the application to join collections together, similar to how they'd use JOINs in PostgreSQL. Why might this be problematic?
- A) `$lookup` doesn't exist in MongoDB
- B) Unlike optimized SQL joins, `$lookup` is more expensive — it's powerful but not something to rely on for every query
- C) `$lookup` only works on a single collection
- D) There's no issue — `$lookup` and SQL JOINs perform identically

**Answer:** B) Unlike optimized SQL joins, `$lookup` is more expensive — it's powerful but not something to rely on for every query
**Explanation:** The lesson warns: "It's powerful—but not free. Unlike optimized SQL joins, MongoDB's 'lookup' is more expensive. It's powerful, but not something you rely on for every query." Document databases are designed to minimize the need for joins by embedding related data — heavy `$lookup` use may indicate a modeling problem.

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

**Question 1:** A team currently runs MongoDB locally. They want to move to a managed service where infrastructure, backups, and patching are handled automatically. What type of cloud service is MongoDB Atlas?
- A) IaaS (Infrastructure as a Service) — you manage virtual machines
- B) PaaS (Platform as a Service) — a fully managed database where you don't manage underlying infrastructure
- C) SaaS (Software as a Service) — a desktop application
- D) A self-hosted solution

**Answer:** B) PaaS (Platform as a Service) — a fully managed database where you don't manage underlying infrastructure
**Explanation:** "MongoDB Atlas is the managed version of MongoDB... PaaS stands for Platform as a Service. It means you're renting a fully managed database, not just bare computing hardware."

Feedback:
- A) IaaS provides raw virtual machines that you manage yourself (OS, patches, database installation). Atlas handles all of that for you, making it PaaS.
- C) SaaS is end-user software (like Gmail or Salesforce). Atlas is a platform for developers to build on, not a consumer application.
- D) Atlas is the managed cloud version of MongoDB — it's the opposite of self-hosted, with infrastructure managed by MongoDB Inc.

---

**Question 2:** Your MongoDB Atlas workload is growing and queries are slowing down. The database runs on a single tier with limited CPU and RAM. What does "scaling up" mean in this context?
- A) Adding more collections
- B) Moving to a higher tier with more CPU cores and RAM so each request gets more resources
- C) Deleting old data
- D) Adding more developers

**Answer:** B) Moving to a higher tier with more CPU cores and RAM so each request gets more resources
**Explanation:** "Scaling up means choosing a higher tier—more CPU cores and more RAM—so each request gets more resources." This is vertical scaling — making one machine more powerful.

Feedback:
- A) Adding more collections doesn't increase compute resources. Collections are logical groupings of documents, not a way to add CPU or memory.
- C) Deleting old data frees storage but doesn't address CPU or RAM bottlenecks. Slow queries need more compute resources, not just free space.
- D) Adding more developers doesn't improve database performance. Scaling up means increasing the hardware resources available to the database.

---

**Question 3:** A single MongoDB server is hitting its storage and throughput limits. You need to distribute data across multiple machines. What is this called in MongoDB?
- A) Replication
- B) Sharding — splitting data across multiple machines to scale horizontally
- C) Indexing
- D) Aggregation

**Answer:** B) Sharding — splitting data across multiple machines to scale horizontally
**Explanation:** "Sharding is the term MongoDB uses for splitting your data across multiple machines to scale horizontally.... Sharding addresses one machine's limits by distributing the data across multiple machines." This is horizontal scaling — adding more machines rather than making one bigger.

Feedback:
- A) Replication creates copies of data for redundancy and read scaling, but each replica holds the full dataset. It doesn't distribute data across machines to overcome storage limits.
- C) Indexing speeds up queries by creating lookup structures, but it doesn't address fundamental storage or throughput limits of a single machine.
- D) Aggregation is a query framework for data analysis. It doesn't distribute data across machines or scale the database infrastructure.

---

**Question 4:** A solutions architect is comparing MongoDB Atlas and AWS DynamoDB for a new project on AWS. What architectural difference should they consider?
- A) They're architecturally identical
- B) DynamoDB is built into AWS natively and scales seamlessly within the ecosystem; MongoDB Atlas runs on virtual machines and operates more independently
- C) MongoDB Atlas is always faster
- D) DynamoDB doesn't support NoSQL workloads

**Answer:** B) DynamoDB is built into AWS natively and scales seamlessly within the ecosystem; MongoDB Atlas runs on virtual machines and operates more independently
**Explanation:** "DynamoDB is built into AWS at a deeper level. MongoDB Atlas runs on virtual machines. In contrast, DynamoDB is more like AWS's own service that doesn't rely on those virtual machines in the same way." This affects scaling behavior, pricing models, and integration with other AWS services.

Feedback:
- A) They have fundamentally different architectures. DynamoDB is AWS-native serverless; Atlas runs on provisioned VMs. This impacts scaling, pricing, and integration.
- C) Performance depends on the workload, configuration, and access patterns. Neither is categorically faster — they excel at different things.
- D) DynamoDB is a NoSQL key-value/document store. Both Atlas and DynamoDB support NoSQL workloads, just with different architectures.

---

**Question 5:** DynamoDB uses "capacity units" to meter usage. What analogy does the lesson use to explain this concept, and what does it mean practically?
- A) Like buying gas — you pay per gallon stored
- B) Like tokens at an arcade — you spend read/write capacity units each time you interact with data
- C) Like electricity — you pay a flat monthly rate
- D) Like a subscription — unlimited usage for a fixed price

**Answer:** B) Like tokens at an arcade — you spend read/write capacity units each time you interact with data
**Explanation:** "Think of capacity like tokens at an arcade. You spend a specific number to use a machine. In DynamoDB, you spend read capacity units and write capacity units every time you interact with data." This pay-per-interaction model requires capacity planning to avoid throttling.

Feedback:
- A) DynamoDB charges per read/write operation (capacity units), not per volume of data stored. Storage is billed separately.
- C) DynamoDB's provisioned capacity mode charges based on throughput capacity reserved, not a flat rate regardless of usage. On-demand mode charges per request.
- D) DynamoDB is usage-based, not unlimited. Exceeding provisioned capacity results in throttling. You must plan capacity or use on-demand mode.
