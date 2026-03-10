# Lesson 1: Introduction to Data Modeling

## Video Summary

We've reviewed the importance and scale of data consumption in modern applications. We also reviewed how the appetite for data continues to grow at rates unheard of for everyday technology products. Consider the lesson's example that Amazon S3 stores more than 350 trillion files (of all kinds!) and processes over 100 million requests every second—if you managed to stack 350 trillion sheets of paper, you could reach the moon!

However, despite the importance of data, we know that it is not formless. The reality is that although data powers and drives almost every aspect of most modern software, data, unlike liquid fuel in an engine, must be molded, then given shape to be useful! And while cloud providers like AWS, Azure, and Google Cloud make handling data at scale look effortless, the underlying engineering is anything but easy.

### Meet Your Instructor

The course instructor is **Koosha Totonchi**, a senior data engineer and former Googler. His background spans diverse industries—governments, fast-moving technology startups that grew to IPO, large financial institutions, nonprofits, and tech enterprises. Across all of them, one consistent challenge has always been structuring datasets to be usable in the analytics engines these organizations depend on. Whether the datasets were about people, employees, customers, business operations, or abstract concepts—data modeling impacted everything.

### What We Covered

**The Big Picture: Polyglot Persistence**

The context we covered here sets the stage for understanding why we need different, scalable, database technologies. As a result, we now know that modern applications must use multiple types of databases to solve different problems, as data is processed, molded, modeled, and consumed differently across them. 

The key concept here is **polyglot persistence**—no single database fits every problem. Real-world applications combine relational databases, document stores, and graph databases, each handling what it does best. Relational databases, document stores, and graph databases often work side by side, each with different strengths, physical layouts, query engines, and modeling patterns.
 
In this course, we'll work with:
- **Relational databases** (PostgreSQL and AWS RDS) - focusing on keys, indexes, constraints, and normalization
- **Document stores** (MongoDB and AWS DynamoDB) - handling semi-structured data, document validation, and flexible schemas
- **Graph databases** (Neo4j and Amazon Neptune) - modeling nodes, relationships, and paths using Cypher and GQL, the first new ISO database language standard since SQL in 1987

**Understanding Data: The DIKW Pyramid**

In this lesson, we learned how to define data itself. Data is something we hear about daily across multiple industries—it impacts everything from search engines and business operations to scientific research. Data has often been called the "new oil" because it fuels all kinds of innovative AI tools and products which automate or accelerate decision making.

The Merriam Webster Dictionary offers two definitions of data, but for this course, we're focused on the second one: **data is information in digital form that can be transmitted or processed**. Think of it as a collection of discrete or continuous values "as given"—the raw values provided by whatever system or person collected them.

The **DIKW Framework** (Data → Information → Knowledge → Wisdom), a philosophy going back to 1927 in corporate addresses by Dow Jones and Company editors, helps us understand data's role when we understand it with this definition:

- **Data** is the foundation—raw digital values
- **Information** is data that's been organized or summarized so it carries meaning, fundamentally allowing us to interpret and understand a studied entity or its abstraction
- **Knowledge** is the result of synthesizing information and analyzing data in context, combining belief with fact and justification
- **Wisdom** is the level where we make sound judgments based on that knowledge

Data modeling sits right at this intersection—giving raw data structure so it reflects real things and supports whatever we're trying to accomplish, enabling us to move higher on the pyramid.

**The Scope of Modern Data**

The scope of data usage and gathering today is broader than ever. By some estimates, **90% of the world's data was generated in the last two years alone**. The systems that make use of data are also largely automated:
- **Recommendation engines** power Netflix, Amazon, Shopify, Google Search, Maps, YouTube, and more
- **Large language models** can write emails, answer questions, and retrieve information
- **Predictive maintenance** systems at GE and Siemens use telemetry data to predict when maintenance should be performed
- **Sports analytics** organizations use data to discover new talented athletes
- **Decision science** helps understand the effectiveness of business or organizational decisions across every sector

Think about the amount of data needed to build a **digital twin** model of a city for engineering—you would need images, videos, survey data, satellite images, bylaw documents, and more.

However, **more isn't always better**. Raw data at this scale is hard to work with. Before it can become meaningful information, it needs to be refined, cleaned, validated, and—most importantly—structured. And like any resource, it needs infrastructure to manage it effectively. That infrastructure determines whether a search engine can rank results quickly, whether an AI model can learn meaningful patterns, and whether an operations team can spot a shift in quality.

We also learned about the key characteristics of modern "big data":
- **Volume** refers to the massive quantity of data we are now producing—more than ever before in history.
- **Velocity** is the massive speed at which data is gathered, with real-time systems, sensors, and telemetry in many modern products.
- **Variety** refers to the different types of data we are generating—videos, images, documents, pictures, spreadsheets, and more—not just facts and figures gathered by hand.
- **Veracity** is the uncertainty and unstructured nature of data. Given how "noisy" data has become, and the fact that data-generating sources have increased in number, it is not always clear what the "source of truth" is.

**The Three Parts of a Database**

In this lesson, we learned that every database has three core components we need to understand:

1. **Storage Layer** - How data is physically stored (spreadsheets, files, tables, documents, graphs)
2. **Query Engine** - How we write and read data (SQL, MQL, Cypher, etc.)
3. **Metadata** - Data about our data (types, constraints, rules)

**Different Storage Structures**

We saw how data can be organized in different ways depending on what we need to do—and the grocery analogy helps illustrate the differences:
- **Tables** (relational): Rows and columns, like a spreadsheet. Each row is a record, each column is an attribute. When most people picture a database, this is exactly what they're imagining: a relational system with rows as individual records and columns as attributes. Useful for analyzing how much you've spent on groceries.
- **Lists/Documents** (document stores): Simple collections where items don't all need the same fields. NoSQL databases often work this way. Like a grocery list—you wouldn't want a large table with lots of columns and rows just to remember what to buy. You'd want something more like a simple, flexible list.
- **Graphs**: Nodes connected by relationships. Perfect for questions like "when I buy spinach, do I also buy tomatoes?"—a visual relationship between items, a completely different kind of structure.

**Query Engines: Reading and Writing**

We also saw how every query engine needs two capabilities: writing data into the system and reading it back out. Different databases use different commands, but it's always about adding something and asking for something.

Traditionally, the query engine and the storage format are **tightly coupled**—built as one integrated system:
- **PostgreSQL** = relational storage + SQL engine
- **MongoDB** = document storage + MQL engine
- **Neo4j** = graph storage + Cypher engine

These tightly coupled systems are simple to understand and reliable to operate because all the parts assume the same data format. You get predictable performance, predictable behavior, and fewer moving pieces to debug.

Modern systems also offer more **modular** alternatives. A **lakehouse**, for example, separates the storage layer from the query engine entirely: one component holds the files, and another reads those files and runs the queries. Tightly coupled systems still make perfect sense when you want a well-defined model and predictable behavior. Modular systems make sense when you want flexibility in how data is stored or when multiple engines need to read the same files.

**Metadata Keeps Us Honest**

Metadata sits between storage and the query engine, tracking the rules about our data:
- **Type enforcement**: PostgreSQL rejects `"abc"` if we declared a column as `unit_price DECIMAL`
- **Domain constraints**: We can add rules like `CHECK (price > 0)` to prevent invalid values
- **Error prevention**: Catches mistakes before they corrupt our data
- **Performance optimization**: Helps the database run queries faster

**OLTP vs OLAP: Different Workloads, Different Designs**

In this lesson, we learned about two fundamental patterns for how databases are used:

**OLTP (Online Transactional Processing)** - Optimized for writing lots of data quickly and reliably. Think: recording sales, processing orders, updating accounts. Uses **row-oriented** databases like PostgreSQL or MySQL where each record is stored independently in sequence. Adding a new record is simple—you just append it to the end.

**OLAP (Online Analytical Processing)** - Optimized for reading and aggregating data to create insights. Think: generating reports, analyzing trends, business intelligence. Uses **column-oriented** databases like Amazon Redshift or Google BigQuery. Although the reality is more nuanced, think of each column as belonging to a separate piece of a file—it's easier to open one file and sum all the transaction costs. If you did this on a row-oriented database, you would have to open multiple files, look at all the rows, go to the total cost column, and then sum across each record one by one. The drawback is that writing a new line to a column-oriented system requires opening all columns and writing the next value into each.

In many organizations, these two types of systems **work together**: data often arrives first in an OLTP system and then gets transformed and loaded into an OLAP system for reporting and analysis. Most modern data pipelines follow this pattern.

We also reviewed **hot versus cold data**

- **Hot/Warm data**: Recent, frequently accessed, needed for immediate business operations. Hot data tends to flow into OLTP in the form of writes.
- **Cold data**: Archival, historical, used for long-term analysis, complex models, and AI/ML training. Cold data tends to accumulate in OLAP systems, although the majority of OLAP use cases still focus on reading "warm" data so the most recent trends can be studied.
- The distinction helps teams **control cost and performance** without treating all data the same.

**Deployment Options**

In production, database software runs on a server (when practicing, it might be a file-based or in-memory database like SQLite or DuckDB). We explored different ways to run databases:
- **On-premise** vs **Cloud**: On-premise means you handle all maintenance (software updates, security patches, OS dependencies) and deal with hardware yourself. Cloud means you never touch the hardware—services are provided by AWS, Azure, Google Cloud, or other vendors.
- **Managed** vs **Self-managed**: Cloud vendors offer both options. A managed service provides easy setup—you just click start and fill out the configuration. Self-managed means launching a server image yourself and installing everything from scratch. The choice depends on your team and project.
- **Single-node** vs **Distributed**: A single-node database runs storage, query planning, and execution on one machine—simpler to operate and easier to reason about. A distributed system spreads those responsibilities across multiple machines, adding complexity but handling much larger workloads. Cloud providers offer distributed databases as managed services, taking care of cluster-level details.

In distributed systems, the query engine must plan how work is split across machines, where to send each piece, and how to combine results. You can influence this behavior through partitioning rules, indexing choices, and table organization.

An important thing to remember: **even if you didn't choose the system, you still need to understand it**. In many teams, decisions about OLTP vs. OLAP, cloud vs. on-prem, or single-node vs. distributed are made by architects, platform teams, or cloud administrators—and may have been locked in years ago. Understanding databases work helps you drop into a project quickly, ask better questions, and make more informed contributions.

**Why NoSQL Exists**

In this video, we discovered why document databases were invented. Traditional relational databases force everything into strict, predefined schemas with rows and columns. But not all data fits neatly into tables, and sometimes data structures change faster than we can redesign our schema.

**NoSQL** stands for "not only SQL"—the goal wasn't to replace relational databases but to complement them.

**MongoDB** (short for "humongous database") was designed to handle large volumes of unstructured data that changes constantly. We can add fields, leave blanks, or modify the structure without schema migrations or table redesigns. It grew out of an ad platform serving 400,000 ads per second.

Other NoSQL databases emerged from similar real-world pressures:
- **DynamoDB**: Built to handle Amazon's holiday shopping traffic spikes
- **Cassandra**: Created at Facebook for inbox search across hundreds of millions of users

These databases use new query languages designed for flexible data. MQL (MongoDB Query Language) works with documents for example, instead of rows and columns.

**When Relationships Matter Most**

We learned about graph databases, based on graph structures, which are built for situations where the relationships between things are just as important—or more important—than the things themselves.

Questions like "who owns which vehicle?", "which products are bought together?", "which people are connected to each other?", or "which ideas link together inside your notes app?" are perfect for graphs in general, and graph databases by extension.

Graph databases are less common than relational or NoSQL systems, but their popularity has been growing—especially as companies build **knowledge bases** to support AI systems, **recommendation engines**, and **semantic search engines**.

The math behind graphs goes back to 1736 when Leonhard Euler solved the "Seven Bridges of Königsberg" problem, proving no route existed that crossed each bridge exactly once.

**Graph Structure**

Graphs have three components:
- **Nodes**: The entities (people, products, places)
- **Edges**: The connections between them (relationships)
- **Properties**: Attributes on nodes and edges (names, dates, types)

We also reviewed **why graphs are fast for relationships**

In a relational database, joining tables means scanning indexes or matching keys—it gets slower as data grows. In a graph database, we follow direct pointers from one node to another. This makes graph databases perfect for:
- Recommendation systems ("customers who bought X also bought Y")
- Fraud detection (finding patterns across connected accounts)
- Social networks (friend-of-friend queries)
- Supply chain modeling

**GQL: The New Standard**

In 2024, GQL (Graph Query Language) became the first new ISO database language standard since SQL in 1987. This growth in standardization reflects the increasing importance of graph databases in the modern data landscape. Systems include Neo4j, Amazon Neptune, Google Spanner Graph, and Azure Cosmos DB. They don't replace relational or document databases—they sit alongside them, with systems using graphs when the connections themselves carry most of the meaning.

**Data Models: Logical vs Physical**

In this video introducing the purpose and heart of data modeling, we learned what a data model actually is: an abstract design that organizes entities, their attributes, and relationships. It represents our understanding of reality before any data is even gathered. Without clear structure, we get confused records, contradictions, and data that's hard to work with. There are two primary model layers we are interested in.

As George Box famously said: *"All models are wrong, but some are useful."* Data modeling works the same way—you'll never design a model that captures every detail of the real world, but you can design one that's useful for the problems you're trying to solve.

**Data Architecture: Choosing a System**

Before creating any tables or defining any keys, someone—maybe you, maybe a platform team—has to choose which database system is running underneath. A relational engine like PostgreSQL, a document store like MongoDB, a graph database like Neo4j—each supports different physical layouts and shapes of data. Each type has benefits and drawbacks:
- **Relational databases** give strong structure and clear relationships, but altering that structure can be costly. Columns must have standard types defined ahead of time.
- **Document stores** give flexibility for semi-structured or evolving data, but that flexibility can make it harder to filter or aggregate consistently. There's more you have to handle on your own compared to relational setups. You also have to handle anomalies on your own entirely. More on that later. 
- **Graph databases** let you traverse connected entities efficiently, but they're more specialized and primarily make sense when relationships are the primary area of interest.

The lines between database types are also blurring—PostgreSQL, for example, keeps getting better at handling JSON, so even within a relational engine, you might mix tabular structures with semi-structured attributes.

**Two Levels of Abstraction**

- **Logical model**: The human-friendly view. Describes what exists in our domain and how things relate (Items have names and prices; TransactionLines connect Items to Purchases).
- **Physical model**: The machine-friendly view. Describes how data is actually stored and accessed (row-oriented tables, column-oriented files, document collections).

**DDL vs DML**

We learned two categories of database commands for working with data and data models:

**DDL (Data Definition Language)** - Changes the structure:
- `CREATE`: Sets up a new table, index, or constraint
- `ALTER`: Modifies existing structure (add columns, change constraints)
- `DROP`: Removes structure

DDL affects our metadata and is often packaged as **migrations**—versioned updates that evolve our schema over time. For example, PostgreSQL lets you add a JSON column for semi-structured attributes via `ALTER TABLE item ADD COLUMN attributes JSON;`.

Some DDL decisions shape the **logical model** (naming entities and defining their domains), while others influence the **physical model** (choosing indexes, distribution keys, or sort keys). Most real DDL affects both layers at once, because the structure you design is the bridge between how humans see the data and how the machine organizes it.

**DML (Data Manipulation Language)** - Changes the data:
- `SELECT`: Fetch data
- `INSERT`: Add new records
- `UPDATE`: Modify existing records
- `DELETE`: Remove records

DDL impacts the metadata; DML impacts the data.

**DDL Beyond Relational Databases**

The DDL/DML distinction is most commonly used in SQL relational databases, but similar concepts apply elsewhere:
- **Graph databases** have Cypher or GQL DDL commands to define nodes, relationships, and constraints
- **Document stores** have some commands analogous to DDL (defining collections, validation rules, indexes), but schemas are not as rigid and don't work the same way as table structures in relational databases

The practice of data modeling means aligning our logical layer with reality and our physical layer with the use case we're solving.

---

### Lesson Review

You came into this course already knowing how to write SQL. But the SQL you've written before—`SELECT`, `INSERT`, `UPDATE`, `DELETE`—is DML. It works at the information level, querying existing structures to extract patterns and answer questions. Now you've opened up the hood on everything underneath those queries.

Key takeaways:
- **Databases** are the backbone of data-driven systems and come in several forms: relational (structured tables), document stores (semi-structured data), and graph databases (relationship-focused)
- **Storage formats** vary—the same table you see on the surface may actually be stored as rows, columns, documents, or nodes and edges underneath
- **OLTP** prioritizes simultaneous writes; **OLAP** prioritizes large batch reads
- Organizations distinguish between **hot data** (quick access) and **cold data** (cheaper storage)
- Databases may run **on-premises or in the cloud**, as **managed or self-managed**, on **a single node or distributed** across many machines
- **Metadata** acts as guardrails—enforcing types, constraints, and domain rules to keep data valid
- A **data model** is a structured representation connecting human understanding (logical) with machine storage and retrieval (physical)
- Data models are created using **DDL** (`CREATE`, `ALTER`, `DROP`), and data is manipulated using **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- Together—storage formats, query engines, system architecture, metadata, logical and physical models, DDL and DML—give you a full mental model of what's happening underneath a query