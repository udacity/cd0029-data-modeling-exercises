# Lesson 1: Introduction to Data Modeling

## Video Summary

We've reviewed the importance and scale of data consumption in modern applications. We also reviewed how the appetite for data continues to grow at rates unheard of for everyday technology products. Consider the lessons example that Amazon S3 stores more than 350 trillion files (of all kinds!) and processes over 100 million requests every second. 

However, despite the importance of data, we know that it is not formless. The reality is that although data powers and drives almost every aspect of most modern software, data, unlike liquid fuel in an engine, must be molded, then given shape to be useful! 


### What We Covered

**The Big Picture: Polyglot Persistence**

This sets the stage for understanding why we need different, scalable, database technologies. As a result, we now know that modern applications must use multiple types of databases to solve different problems, as data is processed, molded, modeled, and consumed differently across them. 

The key concept here is **polyglot persistence**—no single database fits every problem. Real-world applications combine relational databases, document stores, and graph databases, each handling what it does best. 
 
In this course, we'll work with:
- **Relational databases** (PostgreSQL and AWS RDS) - focusing on keys, indexes, constraints, and normalization
- **Document stores** (MongoDB and AWS DynamoDB) - handling semi-structured and evolving data
- **Graph databases** (Neo4j and Amazon Neptune) - using Cypher and GQL, the first new database language standard since SQL in 1987

**Understanding Data: The DIKW Pyramid**

In this lesson, we learned how to define data itself. The Merriam Webster Dictionary offers two definitions, but for this course, we're focused on the second one: data is information in digital form that can be transmitted or processed. Think of it as raw values—measurements, statistics, observations—provided "as given" by whatever system or person collected them.

The **DIKW Framework** (Data → Information → Knowledge → Wisdom) helps us understand data's role:
- **Data** is the foundation—raw digital values
- **Information** is data that's been organized or summarized to carry meaning
- **Knowledge** comes from synthesizing information and analyzing data in context
- **Wisdom** is where we make sound judgments based on that knowledge

Data modeling gives raw data structure so it reflects real things and supports what we're trying to accomplish. As William Edwards Deming said: "without data, you're just another person with an opinion."

We also learned about the "5 Vs" of modern data: volume, velocity, variety, veracity, and value. 
- **Volume** refers to the fact that we are now producing more data than ever before in history. By some estimates, 90% of the world's data was generated in just the last two years.
- **Variety** refers to the different types of data we are generating - consider we now generate video, images, and text in addition to just numerical measurements. 
- **Veracity** is the trustworthiness, accuracy, and reliability of data within systems. Given how "noisy" data has become in recent times, and the fact that data generating sources have increased in number, it is not always clear what the "source of truth" is. 
- **Velocity** is the speed at which data is gathered. We are now gathering data faster than in the past with real time systems, sensors and telemetry in many modern products, and so on.

**The Three Parts of a Database**

Every database has three core components we need to understand:

1. **Storage Layer** - How data is physically stored (spreadsheets, files, tables, documents, graphs)
2. **Query Engine** - How we write and read data (SQL, MQL, Cypher, etc.)
3. **Metadata** - Data about our data (types, constraints, rules)

**Different Storage Structures**

We saw how data can be organized in different ways depending on what we need to do:
- **Tables** (relational): Rows and columns, like a spreadsheet. Each row is a record, each column is an attribute.
- **Lists** (document stores): Simple collections where items don't all need the same fields. NoSQL databases often work this way.
- **Graphs**: Nodes connected by relationships. Perfect for questions like "what products do customers buy together?"

**Query Engines: Reading and Writing**

Every query engine needs two capabilities: writing data into the system and reading it back out. Different databases use different commands, but it's always about adding something and asking for something.

Some systems are **tightly coupled**—the query engine and storage are built together (like PostgreSQL). Others are **modular**—the storage layer is separate from the query engine (like lakehouse architectures).

**Metadata Keeps Us Honest**

Metadata sits between storage and the query engine, tracking the rules about our data:
- **Type enforcement**: PostgreSQL rejects `"abc"` if we declared a column as `unit_price DECIMAL`
- **Domain constraints**: We can add rules like `CHECK (price > 0)` to prevent invalid values
- **Error prevention**: Catches mistakes before they corrupt our data
- **Performance optimization**: Helps the database run queries faster

**OLTP vs OLAP: Different Workloads, Different Designs**

In this lesson, we learned about two fundamental patterns for how databases are used:

**OLTP (Online Transactional Processing)** - Optimized for writing lots of data quickly and reliably. Think: recording sales, processing orders, updating accounts. Uses **row-oriented** databases like PostgreSQL or MySQL where each record is stored independently.

**OLAP (Online Analytical Processing)** - Optimized for reading and aggregating data to create insights. Think: generating reports, analyzing trends, business intelligence. Uses **column-oriented** databases like Amazon Redshift or Google BigQuery where it's faster to sum up values across millions of rows.

**Hot vs Cold Data**

- **Hot/Warm data**: Recent, frequently accessed, needed for immediate business operations
- **Cold data**: Archival, historical, used for long-term analysis and compliance

**Deployment Options**

We explored different ways to run databases:
- **On-premise** vs **Cloud**: Local hardware we control vs rented infrastructure
- **Managed** vs **Self-managed**: Database-as-a-service (easy setup, automatic backups) vs installing and maintaining everything ourselves
- **Single-node** vs **Distributed**: One machine doing everything vs spreading workload across multiple machines

**Why NoSQL Exists**

We discovered why document databases were invented. Traditional relational databases force everything into strict, predefined schemas with rows and columns. But not all data fits neatly into tables, and sometimes data structures change faster than we can redesign our schema.

**NoSQL** stands for "not only SQL"—the goal wasn't to replace relational databases but to complement them.

**MongoDB** (short for "humongous database") was designed to handle large volumes of unstructured data that changes constantly. We can add fields, leave blanks, or modify the structure without schema migrations or table redesigns. It grew out of an ad platform serving 400,000 ads per second.

Other NoSQL databases emerged from similar real-world pressures:
- **DynamoDB**: Built to handle Amazon's holiday shopping traffic spikes
- **Cassandra**: Created at Facebook for inbox search across hundreds of millions of users

These databases use new query languages designed for flexible data. MQL (MongoDB Query Language) works with documents instead of rows and columns.

**When Relationships Matter Most**

We learned about graph databases, which are built for situations where the relationships between things are just as important—or more important—than the things themselves.

Questions like "who owns which vehicle?", "which products are bought together?", or "which people are connected to each other?" are perfect for graph databases.

The math behind graphs goes back to 1736 when Leonhard Euler solved the "Seven Bridges of Königsberg" problem, proving no route existed that crossed each bridge exactly once.

**Graph Structure**

Graphs have three components:
- **Nodes**: The entities (people, products, places)
- **Edges**: The connections between them (relationships)
- **Properties**: Attributes on nodes and edges (names, dates, types)

**Why Graphs Are Fast for Relationships**

In a relational database, joining tables means scanning indexes or matching keys—it gets slower as data grows. In a graph database, we follow direct pointers from one node to another. This makes graph databases perfect for:
- Recommendation systems ("customers who bought X also bought Y")
- Fraud detection (finding patterns across connected accounts)
- Social networks (friend-of-friend queries)
- Supply chain modeling

**GQL: The New Standard**

In 2024, GQL (Graph Query Language) became the first new ISO database language standard since SQL in 1987. Systems include Neo4j, Amazon Neptune, Google Spanner Graph, and Azure Cosmos DB.

**Data Models: Logical vs Physical**

We learned what a data model actually is: an abstract design that organizes entities, their attributes, and relationships. Without clear structure, we get confused records, contradictions, and data that's hard to work with.

**Two Levels of Abstraction**

- **Logical model**: The human view. Describes what exists in our domain and how things relate (Items have names and prices; TransactionLines connect Items to Purchases).
- **Physical model**: The machine view. Describes how data is actually stored and accessed (row-oriented tables, column-oriented files, document collections).

**DDL vs DML**

We learned two categories of database commands:

**DDL (Data Definition Language)** - Changes the structure:
- `CREATE`: Sets up a new table, index, or constraint
- `ALTER`: Modifies existing structure (add columns, change constraints)
- `DROP`: Removes structure

DDL affects our metadata and is often packaged as **migrations**—versioned updates that evolve our schema over time.

**DML (Data Manipulation Language)** - Changes the data:
- `SELECT`: Fetch data
- `INSERT`: Add new records
- `UPDATE`: Modify existing records
- `DELETE`: Remove records

The practice of data modeling means aligning our logical layer with reality and our physical layer with the use case we're solving.
