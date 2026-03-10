# Lesson 2: Data Modeling for Relational Databases

## Video Summary

We just learned how to properly design relational database schemas to avoid data problems and support different workload patterns.

### Lesson Overview

You've written SQL before. You've joined tables. You've queried data and made sense of it. But relational databases have a lot more going on under the surface than most people realize. In this lesson, we peeled back the layers of the relational model, looked at the problems it solves (and the ones it doesn't), and learned how to structure data so it behaves the way our applications expect. Key topics include **ACID** properties, **normalization**, and **referential integrity**.

### What We Covered

**The Relational Data Model**

The relational data model organizes values into relations—what we usually call tables—made up of rows and columns. Each row represents a record or "unit of observation", each column represents an attribute of that record, and a table focuses on one kind of entity (items, customers, purchases, etc.).

To work reliably across many users and many queries, relational systems use **keys** to identify and connect rows:
- A **primary key (PK)** uniquely identifies each record in a table, preventing duplication and avoiding confusion when different users want to retrieve specific rows.
- A **foreign key (FK)** links one table to another by referencing the primary key in the related table, enforcing relationships and enabling JOINs.

These key constraints are part of the design introduced by **Edgar Codd**, who invented the relational model while working at IBM in the 1970s. Oracle quickly adopted an estimation of the relational model in their early SQL systems and brought many of Codd's ideas into the mainstream. Today, when someone mentions a "database", they're usually talking about a system that follows Codd's model. Codd also coined the term "OLAP"—online analytical processing—in the 1990s.

**Relational Rules**

Relational models impose rules to prevent inconsistent or misleading operations:

- **No implicit conversions**: If you try to add the integer `5` plus the string `"10"`, PostgreSQL intentionally errors out (`ERROR: invalid input syntax for type integer`). Many programming languages—like JavaScript (`"510"`) or certain dialects of BASIC (`15`)—will quietly try to combine those values, producing confusing results. Relational databases don't allow this.
- **Distinct column names**: Each attribute/column must have a distinct name to avoid confusion when working with and retrieving data.
- **Consistent column types**: Every value in a column must be the same type. For example, `unit_price` cannot be the string "one dollar and fifty cents", and you cannot mix hexadecimal or binary numbers alongside decimal numbers, as this would result in incorrect mathematical operations.

**ACID: The Four Guarantees**

In practice, we describe the reliability of relational databases using the ACID framework:

**Consistency** - Consistency means that any operation on the database cannot violate the database's constraints. If an operation would break a rule related to keys, types, or any other metadata, the database rejects it. This connects directly to the relational rules above.

**Atomicity** - Operations are bundled together as a transaction and are all-or-nothing. Suppose you are writing a new record: you add the name "watermelons" but before you can add the price, there is a power outage or network interruption. You're stuck with half a row and no clear next step—do you update it? Insert a new one? Either choice can result in errors, duplication, or failures. Atomicity prevents this "in-between" state: a transaction is either completed in its entirety or not applied at all.

**Isolation** - In a real system, many users and pieces of software may read and write data at the same time. If one user reads a row while another is updating it, or both try to update the same record, the database needs a predictable way to handle the conflict. Isolation guarantees that even when transactions run in parallel, they behave as if they happened one at a time, in sequence.

**Durability** - Once a transaction is committed, its changes are permanent. We achieve this by writing data to some kind of permanent storage system such as a hard disk—not in RAM or "volatile memory". RAM needs continuous power, but a disk doesn't have that limitation. Of course, there are limits (data centers can be damaged by floods, natural disasters, etc.), but under normal failure conditions, the data will persist.

ACID properties provide a strong safety net—transactions stay whole, rules stay intact, and committed data persists. Still, no system is perfect. Some quirks and corner cases still slip through, which was known all the way back when the relational model was created.

**When Things Go Wrong: CRUD Anomalies**

Even with ACID guarantees, relational databases can still run into problems—especially when the structure of the data model doesn't match the reality of the domain. These issues are called **anomalies**, and they show up during the four basic operations a database performs: **C**reate, **R**ead, **U**pdate, and **D**elete (often shortened to **CRUD**). Each operation has its own failure modes when the underlying data model isn't structured correctly.

We used a table that simulated inventory at a grocery store. An example of such a table is below:

| name       | type   | price |
|-----------|--------|-------|
| watermelon|        | $5    |
| onion     | red    | $1    |
| onion     | yellow | $1    |
| onion     | green  | $1    |

Consider the types of problems we came across:

**Create (Insert) Anomaly** - Suppose we want to insert a new row for "watermelons", but the store management hasn't yet decided on the price. If our table requires every column to have a value, we can't insert this row without making up the missing information. Setting the price to `NULL` technically works, but it isn't always ideal and can make later queries harder to interpret. A create anomaly appears when the structure forces us to supply information we don't actually have yet.

**Read Anomaly** - Queries become ambiguous when our data structure isn't clear. If the table includes a "type" column for onions—red, yellow, green—a query for "the price of onions" might return several rows, and we could potentially double-count or misinterpret the results.

**Update Anomaly** - Read and update anomalies often appear together because they stem from ambiguity in the data. If someone says "update the price of onions", which row should change? All types? Just one? It's unclear. We have to update multiple separate rows and hope we don't miss any. If we forget one, the data becomes inconsistent.

**Delete Anomaly** - Imagine the table includes a column specifying where onions are sold. If onions are temporarily unavailable in a certain location, we might delete the onion rows entirely. But doing that would also erase information we care about—like the unit prices. Then, when we get new shipments, we won't know the price! A deletion anomaly means we can't delete a row without unintentionally erasing other valuable information.

These examples highlight why **the structure matters as much as the data itself**. Even with ACID guarantees keeping operations safe and consistent, a poorly-designed table can still produce confusing, contradictory, or incomplete results.

**Normalization: Fixing the Problems**

When a table structure creates confusion—whether during inserts, updates, or deletes—one way to address those issues is through **normalization**. Normalization is the process of organizing tables into standard structures called **normal forms** so that the data model reflects the domain cleanly and avoids common anomalies.

These normal forms come from Edgar Codd's 1971 paper, *"Further Normalization of the Data Base Relational Model"*. While the paper contains many abstract Greek-letter formulas, the forms are still useful today. We walk through them one level at a time:

**1NF (First Normal Form)** - Each cell in a table should contain a **single value**. Not a list, not a nested table, and not multiple pieces of information packed together.

For example, imagine the current unit price of apples is $2.00, and next week it goes up to $3.00. You'd like to remember the previous price. The easiest approach might be putting both values in the same cell—like typing `"$3 (current), $2 (last week)"` or storing a JSON list of dates and prices. Technically that "works", but it breaks 1NF:
- Filtering becomes harder: you can't just say `WHERE unit_price > 2.50`—you have to dig into JSON, extract values, and interpret them
- Indexes are much harder to build and use when data is buried inside JSON keys and values
- Constraints become weaker: it's easy to enforce `CHECK (unit_price > 0)` on a numeric column, but much harder inside a JSON structure
- Each row carries repeated structure (the JSON blob repeats "date" + "price" over and over)

The normalized solution: **create a separate Price History table** with one row per price change. The Item table keeps a single current price, and the Price History table tracks how it has changed over time. Now we can apply filters and constraints using simple SQL, and join from Item to Price History using a foreign key.

**2NF (Second Normal Form)** - Achieve 1NF first, then eliminate **partial dependencies**. The first ingredient is clearly defining the primary key:
- **Natural keys**: Keys with business meaning (like product name). Sometimes called a "natural key" as it's fairly intuitive.
- **Composite keys**: When a single column can't uniquely identify a row (e.g., different types of onions all share the same name), we use a combination of columns—a composite primary key (e.g., name + type). The primary key is the formal way of answering: "Which attributes make this record one-of-a-kind?"
- **Partial dependencies**: Once the primary key is defined, 2NF asks: do all other columns depend on the **entire** primary key—and not just part of it?

For example, imagine an Inventory table tracking which products are available at which stores. The composite primary key is (store_name, item_name, item_type). Quantity depends on the store and the item—every value is different. But `unit_price` is set at the corporate level: it depends on the item, but **not** the store. So we have multiple copies of the same price. If the price changes, we'd need to update it in multiple places—and if we forget one, the data becomes inconsistent. The fix: since unit_price is already recorded in the Price History table, we remove it from the Inventory table. Now we comply with 2NF.

**3NF (Third Normal Form)** - Achieve 2NF first, then eliminate **transitive dependencies**. The rule: no non-key column should depend on another non-key column.

For example, suppose the marketing team wants to distinguish between regular and sale prices. We might replace `unit_price` with three columns: `base_price` (the regular price), `on_sale` (a boolean flag), and `sale_price` (the discounted price). But `sale_price` depends on `base_price` and `on_sale` plus whatever discount rule we're using—it's a transitive dependency, not a direct fact based on the item and date.

Imagine the store runs a "10% off all apples in February" promotion. If we model that directly in the price history table, we'd have to set `on_sale = TRUE` and compute a `sale_price` for every single date in February where apples appear. If the promotion dates or discount change, we'd have to update many rows. If the store repeats the promotion next year, we duplicate the pattern.

The 3NF solution: keep the **Price History** table focused on the base price on a given date, and move the promotion rules into a separate **Promotion** table. This table stores the type of discount, the amount, the dates, promo codes, and other details. Any query needing the sale price can join the two tables and calculate it on the fly.

**Referential Integrity**

After applying normal forms, we've eliminated most common anomalies. But there's still an inconsistency that normalization alone can't prevent. Imagine the company decides to stop selling red onions due to a supply chain issue. If we delete the red onion rows from the Items table but forget to delete the matching rows from Inventory, the database now contains inventory information for a product that no longer exists—the tables are out of sync with reality.

Many relational databases provide **referential integrity** features to prevent this. For example, PostgreSQL supports **cascading deletes**: when a product is removed from the Items table, any related rows in Inventory (and Promotions, Price History, etc.) are automatically removed as well.

With all of these controls, we'll eliminate all but the rarest edge cases in our systems.

**Benefits of Normalization**

Normalization has benefits across the physical and logical levels:

*Physical level:*
- **No duplication**: We avoid storing the same information twice. In row-oriented systems like PostgreSQL, redundant values add storage costs and slow down updates.
- **Fewer update errors**: Using keys correctly, especially composite keys when the data truly requires them, prevents inconsistencies.
- **Indexes on keys**: Primary keys and foreign keys often come with automatically-created indexes, speeding up point-lookups and routine transactional queries.
- **Efficient OLTP writes**: These properties make normalization especially well-suited for OLTP systems, where correctness, efficiency, and many small updates matter.

*Logical level:*
- **Clear dependencies**: Normalization helps us clearly see what depends on what in the domain.
- **Well-defined keys**: Choosing the right primary keys forces us to define each entity unambiguously.
- **Entity-relationship diagrams (ERDs)**: Drawing an ERD helps reveal how the tables relate and how information flows through the system.

Normalization gives structure to the places that need it most—where clarity, consistency, and reliable updates matter. Generally speaking, when we reach 3NF, we can eliminate many of the anomalies we covered in the lesson (although edge cases and other detailed nuances exist).

**Designing for Analytics: Star and Snowflake Schemas**

When designing data models, there are times when full normalization is exactly what you want—especially in systems that handle frequent inserts, updates, and deletes. But **not all systems prioritize writing**. Some focus almost entirely on reading and analyzing data—these are the OLAP applications.

**Facts and Dimensions**

For analytics, management doesn't need to know the structure of our product tables or how we enforce keys and constraints. Instead, they want to understand business performance: **what sold**, **when it sold**, and **for how much**. These are **facts**—events that actually happened, like a sale or an order. They're concrete, historical, and central to most analytical questions.

Facts become more meaningful when paired with **dimensions**, which describe the context around them: the product that was sold, the customer who bought it, the store where it happened, or the date. A **fact table** is usually large and contains foreign keys into dimension tables. The **dimension tables** are smaller and hold descriptive attributes (think of how many types of products are sold vs. how many product sales occur).

The **TPC-H** benchmarking dataset for OLAP-focused, columnar databases uses this pattern: sales, orders, and shipments form the core fact tables, with dimensions for parts, suppliers, customers, nations, and regions.

**Star Schema** - When the fact table sits at the center and the dimension tables surround it, we call the structure a **star schema**. In a grocery example, a star schema might place **sales** at the center, with dimensions for **products**, **customers**, **stores**, and **time**. Analysts can join them to answer questions like "How much of product X did customer Y buy last month?" Star schemas intentionally **relax normalization**—the focus is on fast, intuitive reading, so denormalizing a bit can make queries dramatically easier.

**Snowflake Schema** - A normalized version of the star schema where dimension tables are broken down further into sub-dimensions. More storage efficient but requires more joins for queries.

We also learned that in many instances, tables are joined to create reports for specific use cases, graphs, or views.

**Schema Evolution**

Schemas don't stay frozen. As a business grows, the data it needs to capture can change—sometimes slowly, sometimes overnight. Imagine a grocery database that initially tracks products, prices, and sales. Then the company decides it needs to store the **country of origin** for each item. That means new columns, maybe a new table, and new foreign keys in the analytics tables that reference it.

Changes like these require **DDL**—commands such as `CREATE TABLE` and `ALTER TABLE`. In practice, DDL changes are often grouped into **migrations**, which are planned adjustments to the structure of the database. Running a migration usually requires administrative permissions, so someone like a **database administrator (DBA)** or a senior engineer has to apply the change carefully.

Things get even more complicated when new information touches **primary keys**. If a key changes, the database may need to drop constraints, recreate them, and update all related tables.

Now imagine an even faster-moving scenario: the company releases a mobile grocery-ordering app. Suddenly, we're collecting data we didn't anticipate—device information, click paths, delivery preferences, app events—and we may not yet know which of these fields will matter long-term.

This situation—where the shape of the data changes as new requirements appear—is called **schema evolution**. Different organizations experience it differently:
- **Fast-moving startups** may evolve their schemas constantly.
- **Highly-regulated institutions** may change theirs rarely and cautiously.

Schema evolution can create friction, especially if every structural change requires a new migration and a DBA's time. And sometimes the data itself is **inherently unstructured**—two events of the same type may contain different fields, or new attributes may appear unexpectedly. In cases like this, it can be practical—at least temporarily—to relax the strict normalization rules we've been following. In other words, this is the rare situation where we might intentionally "do what Edgar Codd told us not to do": break normal form, accept variability, and allow the schema to evolve as the system learns what data actually matters.

**Relational Database Model Challenges**

Relational databases give us structure, clarity, and strong guarantees—but they also come with tradeoffs, especially when the real world doesn't fit neatly into tables.

*Unstructured Data* — One challenge appears the moment we need to store information that doesn't have a fixed shape. For example, imagine we want to track which webpage a sale came from on our app. Sometimes there's one source, sometimes several, sometimes it's a search engine, and sometimes it's something entirely new we haven't seen before. A traditional table with rigid columns isn't built for that level of variability.

*JSON and JSONB Columns* — Systems like PostgreSQL allow a column to store **JSON** or **JSONB** data. Instead of adding new columns every time the data changes, we can store a flexible document right inside the cell. It's a powerful way to capture semi-structured or evolving information—things like user preferences, configuration settings, clickstream data, or product attributes that change over time. PostgreSQL includes operators and functions specifically for querying JSON data, so we still get the benefits of SQL with more flexibility.

But this approach has limits:
- JSONB values can't grow indefinitely; each cell still has a maximum size
- Queries can be slower, especially with deeply nested data
- There's no built-in guarantee that every JSON document follows the same structure—without careful validation, we can end up with missing fields, mismatched types, or inconsistent naming conventions, all of which make analysis harder and queries more error-prone

*Scaling Challenges* — PostgreSQL is fundamentally a **single-node system**. We can scale vertically (better hardware, more memory, faster disks), but it won't automatically spread data across multiple machines. **Horizontal scaling** requires additional tools or extensions—fortunately, PostgreSQL's open-source nature means many such extensions exist, including fully open-source distributed options like **Citus**, which let Postgres run across many machines.

Another practical challenge is that PostgreSQL is still software running on a server. That server needs an operating system, security patches, hardware monitoring, network configuration, backups, and failover planning—all of which require time and expertise. Cloud providers help relieve this burden with managed services.

**Managed Databases with AWS RDS**

We explored managed relational database services:

**AWS RDS** provides PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server as Platform-as-a-Service. Instead of installing and maintaining databases ourselves, AWS handles:
- Automated backups
- Software patching
- Monitoring and alerts
- Scaling options

Our applications connect to RDS exactly like connecting to any other database—we just don't manage the underlying infrastructure.

---

### Lesson Review

Relational databases are built on a clear, structured way of organizing data into tables. They enforce **ACID** guarantees—Atomicity, Consistency, Isolation, and Durability—that keep data reliable even when many users and systems are reading and writing at the same time.

We saw that relational tables can still run into problems. **CRUD anomalies**—issues with inserts, reads, updates, and deletes—often happen when the structure of the data doesn't match the realities of the domain.

That's where **normalization** comes in. By bringing tables into **first**, **second**, and **third normal form**, we reduce duplication, remove hidden dependencies, and prevent many of these anomalies before they occur. Keys, foreign keys, and clear relationships all support this structure.

But normalization isn't the only approach. When the goal is fast, large-scale analytics, we often shift toward **star schemas**, **snowflake schemas**, or even one-big-table designs. These deliberately trade some write-side structure for simpler, faster reads.

Relational systems aren't limited to fixed columns anymore, either. PostgreSQL's **JSON** and **JSONB** types give us options for semi-structured data, especially when schemas evolve quickly—though with trade-offs around validation, consistency, and performance.

Finally, running a relational database involves more than just modeling tables. **Self-hosting** requires managing servers, storage, networking, and updates. Cloud platforms like **Amazon RDS** can take on that operational burden, letting you focus on your schema, your queries, and the data itself.

Together, these ideas give you the foundation for designing and working with relational models—from cleanly normalized OLTP systems to analytical structures designed for scale.

Key takeaways: 

- Relational databases organize data into **tables** with rows, columns, primary keys, and foreign keys
- **ACID** guarantees (Atomicity, Consistency, Isolation, Durability) keep data reliable across concurrent reads and writes
- **CRUD anomalies** (Create, Read, Update, Delete) arise when table structure doesn't match the domain
- **Normalization** (1NF, 2NF, 3NF) eliminates duplication, partial dependencies, and transitive dependencies
- **Referential integrity** and cascading deletes prevent orphaned records across related tables
- **Star schemas** and **snowflake schemas** trade normalization for faster analytical reads
- **OLAP databases** (Redshift, BigQuery, Snowflake, DuckDB) use column-oriented storage for analytics at scale
- **Schema evolution** introduces friction—DDL migrations, DBA coordination, and key changes complicate structural updates
- **JSON/JSONB columns** in PostgreSQL offer flexibility for semi-structured data, with trade-offs in query performance and validation
- PostgreSQL is a **single-node system**; horizontal scaling requires extensions like **Citus**
- **Managed services** like AWS RDS handle infrastructure, backups, patching, and scaling so you can focus on data modeling
