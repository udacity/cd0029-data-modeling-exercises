# Lesson 3: Data Modeling for Document Stores

## Video Summary

We just learned how document databases handle flexible, semi-structured data and how they differ from traditional relational databases.

### Lesson Overview

Sometimes it makes sense to break the rigid forms of relational data and allow a more flexible schema. Imagine you run a fruit business that grows fruit in custom containers—some pears are tall and thin, some are wide and flat, others are completely unique shapes. Not every order has the same attributes: some fruits have special dimensions, others have unusual weights, and some have pricing rules that only apply to one order. This is the kind of situation that led to the creation of NoSQL databases.

In this lesson, we covered:
- How document databases work and how to query them
- How CRUD operations differ from relational databases
- Data modeling in NoSQL systems, including **embedding** and **referencing**
- Consistency, validation, and **ACID guarantees** in a NoSQL context
- Common NoSQL challenges and how **cloud-managed services** can help reduce operational burden

### What We Covered

**The NoSQL Philosophy and Motivation**

NoSQL stands for "not only SQL"—it was never about replacing relational databases, just complementing them. "NoSQL" is an umbrella term for databases that trade rigid schemas for flexibility, including document stores, key-value stores, and column-oriented databases. In this lesson we focus especially on **document databases**, where each record can have its own structure.

Document databases emerged from a simple problem: sometimes the real world refuses to fit neatly into rigid tables. Relational databases expect every row to follow the same structure and every column to have a well-defined type. That's powerful—until your data doesn't behave that way. The core idea behind document databases is the shift from fixed tables to flexible objects: some include dozens of fields, some include only a few, and some contain nested structures whose shape changes over time.

Many organizations eventually run into cases where:
- They are working with **fast-evolving data**
- The data itself has an **unstructured nature**
- They are **unsure of what data** they need to collect

This has been increasingly common as the web, mobile apps, and event-driven systems produce unstructured or semi-structured data—often in **JSON format**.

**JSON** (JavaScript Object Notation) took off because it was easy for JavaScript to read and write, and then spread far beyond JavaScript. Today, nearly every major language—Python (`dict`), Java (`HashMap`), C# (`Dictionary`), C++ (`unordered_map`), Go (`map`)—has a native JSON-like structure. JSON has become a universal language for web APIs, logs, events, and configuration files.

At the same time, businesses needed systems that could stay online as their schema changed—no downtime, no waiting for a DBA to run a migration, no strict table structures getting in the way. These pressures led to a new type of database that stores entire documents, not rows.

**The Rise of Startups**: Another major force was the rise of startups over the past twenty years. These companies work in rapid, iterative cycles with shifting requirements and high uncertainty. A rigid relational schema can slow that pace, while a flexible document model lets teams adjust their data structures as quickly as their product evolves. And this isn't only a startup story—even inside the largest tech companies, individual teams frequently operate with the same kind of agility and incomplete information.

**NoSQL vs. JSON in SQL**: Modern relational databases like PostgreSQL let you store flexible data using JSON columns. That can be a great solution when only part of your data is hard to model. NoSQL databases are best when **most or all** of the data is difficult to structure into rigid tabular models. In practice, teams have several options:
- Store flexible fields inside a relational database using JSON columns (partial flexibility + structure)
- Move that data entirely into a NoSQL system (full flexibility)
- Use **polyglot persistence**, combining multiple database types based on the job each one does best

**Document Database Fundamentals**

MongoDB is the best-known document database. Its founders imagined a system where every record looks like a JSON object—not just one column in one table. Internally, MongoDB stores data as **BSON** (Binary JSON) for efficiency, but to developers and applications, it behaves just like JSON. This alignment with modern software stacks made MongoDB take off.

**Terminology translation:**
- Collection = Table
- Document = Row
- Field = Column

You can still index fields, query subsets of data, and enforce some validation rules—many concepts line up with relational databases.

To illustrate the comparison, the lesson showed a financial transactions example—the same data modeled as relational DDL (with `CREATE TABLE Accounts` and `CREATE TABLE Transactions`) and then as MongoDB JSON-like documents. Both approaches work; they're just two different ways of modeling the same domain. But this is where the paths diverge: relational tables expect every row to share the same columns, and schema changes require migrations. Document databases are built on the opposite assumption: different documents might have different fields, and the structure can evolve over time.

**Application Logging Example**: The lesson used an online fruit store to demonstrate this flexibility. A purchase event captures item, price, currency, and quantity in its "payload" field. A login event needs entirely different details—browser and authentication method. As the business grows, the security team might ask for a "number of attempts" field. In a relational database, adding this field requires a migration that updates every row—even rows that have nothing to do with failed attempts. In a document database, you simply start including the field when it's relevant. No schema change. No downtime. No refactoring.

**The Analogy**: If a relational database is a rigid grid of rows and columns, a document database is more like a pile of pages. Each page can contain whatever fields make sense for the thing it represents. One page might include browser details; another might list purchased items; another might record fraud-detection signals that didn't even exist last month. What keeps the pile usable is that each piece of information is stored as a **key-value pair**. Documents in the same collection don't need to match—they evolve as your system evolves.

The key advantage: **flexible schemas**. We can add new fields to some documents without touching others. No schema migrations, no downtime, no rebuilding half our application just to add one new piece of information.

**Document Stores vs Key-Value Stores**

Key-value systems like Redis don't organize fields into documents—all they have is the key and the corresponding data. They're very fast for simple lookups but don't support sorting or filtering like document stores do. If a document store is a pile of pages, a key-value store is like a long scroll with bullet points.

Document stores sit in the **middle ground**: more flexible than relational tables, more structured than pure key-value systems.

**CRUD Operations with MQL**

Compared to relational SQL databases, the workflow is similar in spirit—but the syntax, data model, and mindset are quite different. We walked through each CRUD operation using MongoDB as the primary example, with comparisons to Amazon DynamoDB and Firestore (Google's document database inside Firebase). These examples use Python libraries, but the JavaScript libraries are very similar.

**Create**: You take a Python dictionary and send it to the database. Each system uses a different verb—MongoDB uses `insert_one`, DynamoDB uses `put_item`, Firestore uses `add`—but they all mean "store this document."

**Read**: You specify a filter (sometimes called a query or key condition) and each system gives you back matching documents. MongoDB and DynamoDB let you use a Python dictionary as your filter expression; Firestore has a slightly different syntax using `where("email", "==", ...)`.

MongoDB uses operators that start with a dollar sign (`$`) to tell the system "this is an instruction, not data"—this is part of **MQL** (MongoDB Query Language):

- **$set**: Change or add a field
- **$unset**: Remove a field
- **$push**: Append to an array

**Update**: This is one of the biggest differences from SQL. MongoDB doesn't rewrite the whole row—MQL operators surgically update only what you specify. You first give MongoDB a filter to find the right document, then use `$set` to change just one field without touching the rest. DynamoDB requires an "update expression" and uses a colon (`:`) to indicate placeholder values—the goal is to distinguish between keywords and data. Firestore uses the double-equals syntax to locate the record, then calls the update method—it doesn't use special operators for simple updates.

**Delete**: MongoDB and DynamoDB are fairly similar for deletion. The main difference is that MongoDB can delete based on any filter, while DynamoDB can only delete based on the item's primary key. Firestore uses its double-equals syntax to find the document, then calls the delete method.

**Comparison with Other Document Stores:**
- **DynamoDB**: Uses colons (`:`) for placeholder values; can only delete by primary key
- **Firestore**: Uses double equals (`==`) for filtering; doesn't use `$` or `:` for simple updates

**Aggregation Pipelines: ETL in MongoDB**

At some point, you'll want to ask bigger questions: How much did we sell last year? What's the average sale value by month and category? How do sales change over time?

**Handling Data Relationships**: In relational databases, you would join tables using SQL. Document databases take a different approach—DynamoDB and Firestore don't support joins at all (your application must fetch related data manually). MongoDB is the exception, offering a join-like capability through the `$lookup` stage inside an **aggregation pipeline**.

An aggregation pipeline is an Extract, Transform, Load (ETL) framework that MongoDB provides for performing advanced data analysis and manipulation on collections. It processes documents through a sequence of stages—filtering, reshaping, grouping, sorting, or joining.

**Key stages we practiced:**

**$lookup** - Performs an operation similar to a LEFT OUTER JOIN between two collections. In the lesson example, it enriches each "order" document by attaching matching documents from "customers". Important note: unlike optimized SQL joins, MongoDB's `$lookup` is **more expensive**—it's powerful but not something to rely on for every query.

**$match** - Filters documents. The lesson example kept only sales in the 2025 calendar year using `$gte` (greater than or equal to) and `$lt` (less than) operators.

**$group** - Groups matching documents by specified fields (e.g., year, month, product category) and computes aggregations: total sales (`$sum`), average sale value (`$avg`), and number of sales (`$sum: 1`, which counts documents).

**$sort** - Orders results (e.g., by year, then month, then product category).

Put together, these stages—filter, group, summarize, and sort—let MongoDB answer questions that would normally take a multi-clause SQL query.

**Managing Document Database Structure Without DDL**

Once you're comfortable with CRUD and standard aggregation queries, the next question is: "How do I change the structure of my data over time?"

In relational databases, that's handled by DDL statements like `CREATE TABLE` and `ALTER TABLE`. In document databases, there usually isn't a separate DDL layer.

**CREATE TABLE equivalent**: In document databases, the equivalent is simply inserting your first documents. The shape of those initial documents becomes the de facto structure of the collection. Structure is introduced by what you write, not by a separate command.

**ALTER TABLE equivalent**: In relational databases, `ALTER TABLE` applies to all existing rows at once—often requiring backfilling values, setting defaults, or handling NULLs. In document databases, you achieve the same effect by updating the documents themselves. This can be a gradual process—there's no single moment when the entire collection must change shape.

The same MongoDB operators used for updates—`$set`, `$unset`, and `$rename`—can be used to **reshape** documents:
- `update_one` targets a single document; `update_many` targets all documents matching a filter
- `$set` can add a new field to every matching document
- `$unset` can drop a field you no longer want
- `$rename` can migrate an old field name to a new one

You're not redefining a table—you're modifying the stored documents directly.

**Avoiding Migrations Altogether**: Document databases offer another option that doesn't exist in relational systems—you can just start inserting new documents with the new structure, even while older documents still have the old shape. This is very common in real systems, but the flexibility shifts responsibility onto your application code. Your code needs to handle missing fields, optional values, and multiple document shapes.

Key takeaways for schema evolution:
- **CRUD is your schema migration tool** in document databases
- Document shape **evolves gradually**, not through rigid DDL steps
- Applications must handle **mixed versions** of documents during migrations
- There's no single migration file—structure changes can be ongoing, partial, and spread out over time
- You must be intentional about **tracking changes**, **testing assumptions**, and keeping application logic in sync with the data

That tension—between speed and control, flexibility and discipline—is at the core of data modeling for document databases.

**Document Database Normalization: Embedding vs. Referencing**

In relational databases, OLTP systems tend to be normalized (even to 2NF or 3NF) to prevent CRUD anomalies, while OLAP systems often use denormalized structures like star schemas to make reads fast. **Document databases flip that pattern**: because joins are expensive in most document systems, the most efficient OLTP design is usually **more denormalized**, not less.

**Embedding** means putting related data inside the parent document so the most common read or write happens in a single operation. It's conceptually similar to the "one big table" pattern in analytical relational databases, but optimized for transactional workloads.

**When to embed** (customer-addresses example): In a relational system, you'd create a separate addresses table linked by a foreign key. In a document database, the natural choice is to embed addresses directly into the customer document. Reads, writes, and updates all happen in one place—no join, no second query. Addresses don't change often (a customer might update their home address once a year—or never), and whenever you care about addresses, you're already looking up the customer. As MongoDB's documentation puts it: *"In general… prefer embedding by default… when data is usually accessed together."*

**When NOT to embed** (product-prices example): If your store updates prices regularly (daily sales, seasonal adjustments, discounts), embedding the current price inside every order would create massive duplication and increased chances of CRUD anomalies. Instead, MongoDB encourages storing a canonical "source of truth" in a separate collection and **referencing** it. Three different orders can all reference the same product ID, keeping the price in one place so updates require only a single change.

**Challenging situations**: If you need to represent complicated many-to-many relationships across large datasets, or if the related entity is frequently queried on its own, referencing may be better—even for data that seems embeddable. For example, if you often query for a list of addresses independently, your application performs best with a separate address collection linked by reference.

**ACID Guarantees in NoSQL Systems**

Even in NoSQL systems, ACID guarantees still matter. But unlike relational systems, NoSQL systems often **implement** those guarantees differently, **scope** them differently, or **make them optional**.

The lesson compared four system types side by side:

**Atomicity** (operation is complete or fails entirely):
- **Relational DBs**: Atomic at the transaction level (multiple statements, rows, tables)
- **MongoDB**: Atomic at the **document level** by default. If an operation modifies multiple fields or embedded documents inside a single document, all changes are applied or none are. This is why document modeling matters—you group related data by embedding so it can be updated atomically. MongoDB also supports optional multi-document transactions.
- **DynamoDB**: Atomic at the **item level**, with optional transactional APIs for multiple items
- **Cassandra**: Atomic at the **partition level**, allowing it to remain highly available and horizontally scalable

**Consistency** (what readers see after a write):
- NoSQL joins are expensive, limited, or unavailable—so denormalization and duplication are far more common by design
- If the same data appears in multiple documents, the **database does not automatically keep copies in sync**. Deciding how and when duplicated data stays consistent is now the **developer's responsibility**
- As MongoDB states: *"If you duplicate data in your schema, you must decide how to keep duplicated data consistent across multiple collections."*
- Even without duplication, inconsistency can creep in when documents meant to be analyzed together don't share the same structure or data types
- **Schema validation**: MongoDB allows documents in the same collection to have different shapes by default, but provides optional schema validation using the **JSON Schema standard** (supported by Python, JS, Java). Validation rules can cover: required fields, data types, value ranges and patterns, array size constraints, and inter-field dependencies. You can customize whether failures produce errors (reject) or warnings (accept with logging), and whether validation applies to all documents, new docs only, or conforming docs only
- **DynamoDB** does not support schema validation—structure is enforced almost entirely in application code, and access patterns are controlled through primary keys
- **Cassandra** uses a table-like model with a defined schema, but deliberately relaxes constraints to support high write throughput, horizontal scaling, and availability

**Isolation** (what happens with concurrent operations):
- **Relational DBs**: Isolated at the transaction level
- **MongoDB**: Isolated at the **document level** by default. Also supports explicit multi-document transactions with **snapshot isolation** (data read from a "personal snapshot"; conflicting updates cancel the transaction)
- **DynamoDB**: Offers conditional writes to prevent conflicting updates
- **Cassandra**: Accepts weaker isolation guarantees to maintain high availability

**Durability** (committed data survives failures):
- **MongoDB**: Writes data to disk and keeps copies on multiple machines. Can scale horizontally by default (unlike PostgreSQL, which requires add-ons). Includes replication (same data on multiple nodes) and sharding (data distributed across machines). Durability is tunable—you can decide whether a write must be written to disk, replicated to other nodes, or simply accepted quickly
- **DynamoDB**: Durability built into the service—data automatically replicated across multiple availability zones. Developers don't manage disks or replicas directly
- **Cassandra**: Achieves durability through replication and commit logging across a cluster. You can tune how many nodes must acknowledge a write before it's considered successful

Across NoSQL systems, ACID guarantees still apply, but **where** they apply and **how much responsibility** shifts to the developer changes significantly.

**Principles for Data Modeling with Document Databases**

With all this freedom, the lesson provided a structured framework for making modeling decisions:

**1) Focus on the application you're building:**
- What queries do your pages or services need to run?
- Which pieces of data are central to those queries?
- How often is different data written, updated, or read?
- How much data are you operating on overall?

**2) Identify relationships:** Just as in relational databases, identify one-to-one, one-to-many, and many-to-many relationships. Ask whether certain data naturally contains others or can exist independently.

**3) Evaluate denormalization (embedding) vs. normalization (referencing):**

*Favor embedding when:*
- Keeping related data together makes the model **simpler**
- One piece of data clearly **"has" or "contains"** another
- Data is almost always **read together** (query atomicity)
- Related fields tend to be **updated at the same time**
- Multiple pieces of data should be **archived or deleted together**

*Favor referencing when:*
- **High cardinality**: A product might be associated with thousands of orders, or a user might generate an unbounded stream of events. When the number of related items can grow large, embedding becomes risky—slow to read, slow to update, expensive to move
- **Data duplication**: If embedding would require copying the same information into many records and keeping copies in sync would be error-prone
- **Record size and growth**: If denormalized data would create records that are expensive to store or could grow without clear bounds
- **Write patterns**: If different parts of data are written at different times in write-heavy workloads
- **Individuality**: If the "child" data makes sense on its own, outside the context of the "parent"

**4) Determine consistency and validation needs:** Some fields may need strict formats for regulatory, financial, or safety-critical reasons (strong validation with clear errors). Other data like logs or event streams may benefit from lighter checks. If data formats are very consistent, stronger validation catches bugs early. If structure is likely to evolve, more flexible validation reduces friction.

**5) Fill in remaining details:** Decide how records are identified, which fields must be unique, and how different pieces of data are named and typed.

**NoSQL Data Model Challenges**

NoSQL databases give you freedom, but that freedom comes with challenges:

**CRUD Anomalies in NoSQL:**
- **Create anomalies**: You can insert records even if fields are missing or incomplete. The database won't stop the operation unless you've configured validation. Your application must handle those cases.
- **Update anomalies**: When structure is flexible, it's easier to end up with multiple records that look similar but aren't quite the same. Updating the "right" document requires careful filtering.
- **Delete anomalies**: The database won't automatically clean up related information. There's no equivalent of relational constraints + cascading deletes—this is handled in application logic.

The core principle: **less database enforcement = more application responsibility**.

**Validation is a design decision, not a missing feature**. You can choose to enforce schemas, data types, and required fields—or deliberately avoid them to stay flexible. You decide how strict to be, and that decision affects how many anomalies your application must handle.

**Integration can be challenging**: Many analytics, reporting, and visualization tools are designed around tabular data, star schemas, or relational joins. Some work well with denormalized NoSQL data; others don't. Understanding your broader stack is part of using NoSQL effectively.

**Cloud Providers for NoSQL Databases**

Running any database in production requires hosting on hardware, managing operating systems, handling scaling, applying patches, and ensuring backups. With NoSQL systems, this can be even more demanding because many structural guarantees are optional or application-driven.

Managed NoSQL services handle: provisioning and scaling infrastructure, replication and high availability, backups/patching/upgrades, and integration with security, monitoring, and analytics tools.

**MongoDB Atlas** — The official cloud service from MongoDB's developers. Provides fully managed MongoDB with replication, sharding, backups, and monitoring. Autoscales compute and storage based on usage patterns. Deploys to AWS, Google Cloud, or Azure, allowing co-location with the rest of your infrastructure.

**Amazon DocumentDB** — A fully managed document database compatible with MongoDB APIs. Offers a MongoDB-style document model while AWS handles infrastructure, scaling, backups, and maintenance. Integrates tightly with AWS services like IAM, Glue, and Kinesis. You can often migrate or develop with existing MongoDB tools.

**Amazon DynamoDB** — A fully managed document and key-value service offering a "serverless" experience—no instances or clusters to manage. Automatically scales capacity with pay-per-request billing. Access patterns are more constrained than MongoDB, but operational overhead is extremely low.

**Amazon Keyspaces** — For wide-column NoSQL workloads with very high throughput and predictable access patterns. A fully managed Cassandra-compatible service supporting the familiar Cassandra Query Language (CQL) and existing drivers, while AWS handles replication, scaling, and availability.

All of these services remove the operational burden—but they **do not remove** the need to understand how your data is modeled, how consistency is handled, how duplication and updates are managed, and how your application interacts with the database.

---

### Lesson Review

Document databases emerged from a real need: not all data fits neatly into rigid tables. When the shape of your data is uncertain, evolving quickly, or inherently variable, a flexible document model—built around **JSON-like objects** rather than fixed rows and columns—lets teams move faster without waiting for schema migrations or DBA approval.

We explored how **MongoDB**, **DynamoDB**, and **Firestore** each handle the core **CRUD** operations. The verbs differ (`insert_one`, `put_item`, `add`), but the pattern is the same: store a document, query by filter, update specific fields with surgical operators like `$set` and `$unset`, and delete by key or filter. MongoDB stands out with its **aggregation pipelines**—a built-in ETL framework using stages like `$lookup`, `$match`, `$group`, and `$sort`—that let you answer analytical questions without leaving the database.

Unlike relational systems, document databases don't have a separate DDL layer. Structure is introduced by the documents you write, not by `CREATE TABLE` or `ALTER TABLE`. Schema evolution happens gradually—new documents can include new fields while older documents keep their original shape. This is powerful, but it shifts responsibility onto your application code to handle **mixed document versions**, missing fields, and optional values.

The central modeling decision in document databases is **embedding vs. referencing**. Embedding keeps related data together for fast, atomic reads and writes—ideal when data is accessed together and doesn't change often (like customer addresses). Referencing stores data separately and links it by ID—better when data changes frequently, has high cardinality, or needs to exist independently (like product prices referenced by many orders). This flips the relational pattern: in document databases, the most efficient OLTP design is usually **more denormalized**, not less.

**ACID guarantees** still exist in NoSQL, but they're scoped differently. Atomicity typically applies at the **document level** (MongoDB) or **item level** (DynamoDB), not across multi-table transactions by default. Consistency becomes the **developer's responsibility** when data is duplicated across documents. Isolation and durability are tunable—you choose how strict to be based on your application's needs.

With all this flexibility comes responsibility. There are **no cascading deletes**, no automatic referential integrity, and no guarantee that every document follows the same structure unless you configure **schema validation**. The core principle: less database enforcement means more application responsibility. Good NoSQL data models start from **application access patterns**, update frequency, and scale requirements—not from entity-relationship diagrams.

Finally, **managed cloud services** like MongoDB Atlas, Amazon DocumentDB, DynamoDB, and Amazon Keyspaces handle the operational burden of provisioning, scaling, replication, and backups. But they don't remove the need to understand how your data is modeled, how consistency is handled, and how your application interacts with the database.

Together, these ideas equip you to choose when a document database is the right fit—and how to model, query, and manage data within one effectively.

Key takeaways:
- Document and NoSQL databases **store and retrieve data very differently** from relational systems, even though they still support familiar CRUD operations
- Instead of rigid schemas enforced up front, NoSQL systems allow **flexible document structures** where different records in the same collection may look different
- Because joins are limited or expensive, data modeling often involves **deliberate denormalization** (embedding related data) rather than strict normal forms
- That flexibility means **you, not the database**, are responsible for handling many classic data issues: update anomalies, missing values, duplicated data, and consistency trade-offs
- **ACID guarantees still exist** in NoSQL systems, but they are scoped differently—often at the document or item level—and may be optional or configurable
- When choosing a NoSQL database (MongoDB, DynamoDB, Firestore, Cassandra), **read the documentation** to understand available options—certain aggregations or validations may or may not be available
- There is **no one "correct" NoSQL data model**. Good designs start from application access patterns, update frequency, and scale requirements
- **Managed cloud services** can handle infrastructure, scaling, replication, and backups, letting teams focus on modeling and using data effectively
