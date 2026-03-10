# Lesson 2: Data Modeling for Relational Databases

## Video Summary

We just learned how to properly design relational database schemas to avoid data problems and support different workload patterns.

### What We Covered

**ACID: The Four Guarantees**

We learned why relational databases are considered reliable—they guarantee ACID properties:

**Atomicity** - Transactions are all-or-nothing. If we start adding a record and the power goes out before we finish, the database acts as if it never happened. No partial data corruption.

**Consistency** - Every operation must respect our database's constraints. If we defined a column as NOT NULL or set up a foreign key, the database enforces those rules automatically.

**Isolation** - Concurrent users don't interfere with each other. If two people modify the same data simultaneously, each sees a consistent view and the database coordinates the changes properly.

**Durability** - Once a transaction commits, it's permanent, even if the system crashes. The database writes to persistent storage, so power loss won't erase our committed data.

**When Things Go Wrong: CRUD Anomalies**

We worked through a grocery store example to understand data anomalies—problems that happen when our schema isn't well-designed:

```
| name       | type   | price |
|-----------|--------|-------|
| watermelon|        | $5    |
| onion     | red    | $1    |
| onion     | yellow | $1    |
| onion     | green  | $1    |
```

**Insert Anomaly** - We can't add a new product type without having all required information filled in.

**Read Anomaly** - Queries become ambiguous when our data structure isn't clear. Which onion did someone buy?

**Update Anomaly** - Changing one logical fact requires updating multiple rows. Want to change the price of all onions? We have to update three separate rows and hope we don't miss any.

**Delete Anomaly** - Deleting records can accidentally lose information we wanted to keep.

**Normalization: Fixing the Problems**

We learned a systematic approach to eliminating these anomalies through normalization:

**1NF (First Normal Form)** - Every field contains atomic values. No arrays, no nested structures. Each cell holds exactly one value.

**2NF (Second Normal Form)** - Achieve 1NF first, then eliminate partial dependencies. We need to understand:
- **Natural keys**: Keys with business meaning (like product name + type)
- **Composite keys**: Keys made of multiple columns working together
- **Partial dependencies**: When a non-key column depends on only part of a composite key (this is what we're eliminating)

**3NF (Third Normal Form)** - Achieve 2NF first, then eliminate transitive dependencies. If `sale_price` is calculated from `base_price` and `on_sale` status, that's a transitive dependency—one non-key column depending on another non-key column through the primary key.

**Designing for Analytics: Star and Snowflake Schemas**

We learned that OLAP systems use different design patterns than OLTP:

**Star Schema** - A central fact table surrounded by dimension tables. It's denormalized on purpose—optimized for fast aggregations and analysis rather than avoiding redundancy.

**Snowflake Schema** - A normalized version of the star schema where dimension tables are broken down further. More storage efficient but requires more joins for queries.

**Managed Databases with AWS RDS**

We explored managed relational database services:

**AWS RDS** provides PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server as Platform-as-a-Service. Instead of installing and maintaining databases ourselves, AWS handles:
- Automated backups
- Software patching
- Monitoring and alerts
- Scaling options

Our applications connect to RDS exactly like connecting to any other database—we just don't manage the underlying infrastructure.
