# Lesson 4: Data Modeling for Graph Databases — Quizzes

---

### **Quiz 1: Graph Database Fundamentals**

**Question 1:** You're modeling an e-commerce system where the most valuable insight is: "Customers who bought X also bought Y." Which database paradigm is purpose-built for this kind of relationship query?
- A) A column-oriented data warehouse
- B) A document store
- C) A graph database
- D) A flat file

**Answer:** C) A graph database — designed to traverse relationships between entities efficiently
**Explanation:** The lesson states that "graph databases treat connections between entities as first-class data" and are "widely used for problems where connections are the primary thing you care about, such as: social and communication networks, fraud detection and transaction analysis, recommendation systems." A recommendation like "bought X also bought Y" is a classic relationship traversal.

Feedback:
- A) Column-oriented data warehouses are optimized for aggregating large volumes of metrics (sums, averages). They aren't designed for traversing connections between entities.
- B) Document stores excel at flexible schemas and nested data, but traversing multi-hop relationships (customer → purchase → product → other customers) isn't their strength.
- D) Flat files have no query engine, indexing, or relationship traversal capability. They can't efficiently answer relationship-based questions at scale.

---

**Question 2:** Match each graph database building block to its description.

Column A:
1. Nodes
2. Edges (Relationships)
3. Properties

Column B:
A. Entities like people, products, or documents
B. Connections that describe how entities are related
C. Attributes/data stored on both nodes and relationships

**Answer:** 1→A, 2→B, 3→C
**Explanation:** The lesson states: "a graph database stores three core components: Nodes, which represent entities—like people, products, or documents. Relationships, which represent how those entities are connected. And properties, which store data about both nodes and relationships."

Feedback:
- 1→A: Nodes are the fundamental entities in a graph — the "things" being modeled (people, products, documents, etc.).
- 2→B: Edges (relationships) are the connections between nodes, describing how entities relate to each other (e.g., ACTED_IN, FRIENDS_WITH).
- 3→C: Properties are key-value pairs that store data on both nodes (e.g., a person's name) and relationships (e.g., a role in a movie).

---

**Question 3:** A fraud detection team needs to find accounts that share addresses, phone numbers, and transaction patterns across multiple hops. In a relational database, this requires many self-JOINs. Why is a graph database more suitable?
- A) Graph databases are always faster for all queries
- B) In a graph, traversing relationships follows direct pointers — no scanning tables to match keys — making multi-hop queries natural and efficient
- C) Relational databases can't store address data
- D) Graph databases don't require any queries

**Answer:** B) In a graph, traversing relationships follows direct pointers — no scanning tables to match keys — making multi-hop queries natural and efficient
**Explanation:** The lesson explains that "Each node and relationship stores direct references—essentially pointers—to its properties. And nodes and relationships also store references to each other. Because of this layout, the database does not need to search tables or perform joins in order to discover connections." For multi-hop relationship queries (fraud rings, social networks), graphs are fundamentally more efficient.

Feedback:
- A) Graph databases are not always faster for *all* queries. They excel specifically at relationship traversal. Aggregate calculations across millions of rows may be faster in columnar databases.
- C) Relational databases can store any kind of data, including addresses. The issue is that traversing multi-hop relationships requires expensive self-JOINs in SQL.
- D) Graph databases absolutely require queries (in Cypher, Gremlin, SPARQL, etc.). The advantage is that relationship traversal queries are more natural and efficient, not that queries are unnecessary.

---

**Question 4:** Graph theory was formalized in 1736 when a mathematician proved that a famous problem had no solution. Who was the mathematician, and what was the problem?
- A) Alan Turing and the Halting Problem
- B) Leonhard Euler and the Seven Bridges of Königsberg
- C) Isaac Newton and the Three-Body Problem
- D) Ada Lovelace and the Bernoulli Numbers

**Answer:** B) Leonhard Euler and the Seven Bridges of Königsberg
**Explanation:** The lesson describes how "mathematician Leonhard Euler recognized that this approach quickly becomes impractical" for the Seven Bridges of Königsberg problem, and instead represented it as a graph "where the land masses are 'nodes' and the bridges are 'edges'." Euler proved there was no valid path, laying the foundation for graph theory as a mathematical discipline.

Feedback:
- A) Alan Turing's Halting Problem (1936) is about computability theory, not graph theory. It asks whether a program can determine if another program will halt.
- C) The Three-Body Problem is a physics/celestial mechanics problem about predicting the motion of three gravitational bodies, unrelated to graph theory.
- D) Ada Lovelace wrote the first algorithm (for Bernoulli numbers) but didn't formalize graph theory. Euler's bridge problem predates her work by over a century.

---

**Question 5:** In 2024, a new ISO standard was published for graph databases — the first new database language standard since SQL in 1987. What is it called?
- A) GraphQL
- B) GQL (Graph Query Language)
- C) Neo4j Standard Language
- D) SPARQL 2.0

**Answer:** B) GQL (Graph Query Language)
**Explanation:** The lesson states: "In 2024, the International Organization for Standardization released GQL, the Graph Query Language." It further notes: "It's the first new database language standard from ISO since SQL itself." This is a historic milestone — 37 years between the SQL standard and GQL.

Feedback:
- A) GraphQL is a Facebook-created API query language for web services, not a database query language or ISO standard for graph databases.
- C) Cypher is Neo4j's proprietary query language. While influential, it's not an ISO standard. openCypher is the open-source version, and GQL drew from it.
- D) SPARQL is a W3C standard for querying RDF/semantic data, not a general graph database standard. GQL is the new ISO standard for property graphs.

---

**Question 6:** A consultant is evaluating database options for a new system. Which of the following are use cases where graph databases excel? (Select all that apply)
- A) Recommendation engines
- B) Social network analysis
- C) Fraud detection
- D) Simple key-value lookups

**Answer:** A, B, C
**Explanation:** The lesson states that "graph databases are widely used for problems where connections are the primary thing you care about, such as: social and communication networks, fraud detection and transaction analysis, recommendation systems, and access control or network topology." It also notes: "All major cloud providers—AWS, Azure, Google Cloud—now offer managed graph database services."

Feedback:
- A) ✅ Recommendation engines ("customers who bought X also bought Y") rely on traversing purchase and preference relationships — a core graph database strength.
- B) ✅ Social network analysis involves traversing connections between people (friends, followers, groups) — exactly the multi-hop relationship patterns graphs are built for.
- C) ✅ Fraud detection requires discovering shared addresses, phone numbers, and transaction patterns across multiple hops — graphs handle this naturally through direct pointer traversal.
- D) Simple key-value lookups (get a value by its key) are the domain of key-value stores like Redis, not graph databases. No relationship traversal is needed.

---

---

### **Quiz 2: Neo4j and Cypher Queries**

**Question 1:** In Cypher, the query `MATCH (p:Person)-[:ACTED_IN]->(m:Movie) RETURN p.name, m.title` uses two types of syntax. Match each syntax element to what it represents.

Column A:
1. Parentheses `()`
2. Square brackets with arrow `-[]->`

Column B:
A. Nodes
B. Relationships (edges) with direction

**Answer:** 1→A, 2→B
**Explanation:** The lesson explains that "Nodes appear in parentheses, almost like a visual representation of the graph itself. Labels like 'Person' describe the type of node. The arrow represents a relationship." So `(p:Person)` is a Person node, and `-[:ACTED_IN]->` is a directed "ACTED_IN" relationship.

Feedback:
- 1→A: Parentheses wrap nodes in Cypher — `(p:Person)` declares a node variable `p` with label `Person`. The visual shape of parentheses mirrors the circular representation of nodes in graph diagrams.
- 2→B: Square brackets with arrows represent directed relationships — `-[:ACTED_IN]->` describes the relationship type and direction between two nodes.

---

**Question 2:** You want to find all movies that a specific actor appeared in. Which Cypher clause describes the pattern you're looking for?
- A) CREATE — to make new nodes
- B) MATCH — to describe a pattern to find in the graph
- C) DELETE — to remove matching nodes
- D) MERGE — to create or find

**Answer:** B) MATCH — to describe a pattern to find in the graph
**Explanation:** The lesson states: "MATCH lets you specify the pattern to search for." MATCH is the primary read operation in Cypher — you describe what the relationship pattern looks like, and the database finds all matches.

Feedback:
- A) CREATE makes new nodes and relationships — it's a write operation, not a query for finding existing patterns.
- C) DELETE removes nodes and relationships from the graph. It doesn't search for patterns.
- D) MERGE creates a pattern only if it doesn't already exist. While it can "find," it's primarily used for idempotent writes, not pure read queries.

---

**Question 3:** After a MATCH clause finds results, what does the RETURN clause do?
- A) Deletes the matched data
- B) Specifies what to give back — node properties, counts, aggregations, or the nodes themselves
- C) Creates backups of matched data
- D) Validates the match results

**Answer:** B) Specifies what to give back — node properties, counts, aggregations, or the nodes themselves
**Explanation:** The lesson states: "RETURN defines the parts of the pattern—nodes, relationships, or properties—that should be included in the result." RETURN is analogous to the SELECT clause in SQL — it controls the shape of the result set.

Feedback:
- A) RETURN is a read operation that outputs results. It doesn't delete or modify any data in the graph.
- C) RETURN provides query results to the caller. Backups are a database administration concern handled by different tools entirely.
- D) RETURN doesn't validate results — it specifies which parts of the matched data to include in the output.

---

**Question 4:** You're loading data into Neo4j. Some records may already exist (e.g., an actor node might already be in the graph from a previous import). You want to create the node only if it doesn't already exist. Which command should you use?
- A) CREATE — which always creates a new node
- B) MATCH — which only reads
- C) MERGE — which creates only if the pattern doesn't already exist
- D) DELETE — which removes existing nodes first

**Answer:** C) MERGE — which creates only if the pattern doesn't already exist
**Explanation:** The lesson introduces CREATE as "the keyword to create new data" and separately presents MERGE in the context of updates, where it's used to add relationships or nodes only when needed. Unlike CREATE — which always creates new elements — MERGE avoids duplicates by first checking whether the pattern already exists, making it essential for data loading scenarios with potential re-imports.

Feedback:
- A) CREATE always creates a new node, even if an identical one exists. Running it twice would create duplicates, which is exactly what you want to avoid during re-imports.
- B) MATCH only reads — it finds existing patterns but can't create new ones. If the node doesn't exist yet, MATCH returns nothing.
- D) DELETE removes nodes. Deleting existing nodes before re-creating them is destructive and risks losing relationships and properties.

---

**Question 5:** How does Cypher's readability compare to SQL? Consider this query: `MATCH (p:Person)-[:FRIENDS_WITH]->(f:Person) WHERE p.name = "Alice" RETURN f.name`
- A) Cypher is unreadable and requires special training
- B) Cypher reads almost like plain English — "find a person named Alice, follow FRIENDS_WITH relationships, return the friends' names"
- C) Cypher and SQL are syntactically identical
- D) Cypher can only be used through a GUI, not written as text

**Answer:** B) Cypher reads almost like plain English — "find a person named Alice, follow FRIENDS_WITH relationships, return the friends' names"
**Explanation:** The lesson states: "Cypher was designed to be readable and visual—so that the query mirrors the shape of the graph you're searching." The visual pattern syntax (`()-[]->()`) is designed to be intuitive, especially for relationship-heavy queries.

Feedback:
- A) Cypher is widely regarded as one of the most readable query languages. Its ASCII-art pattern syntax (`()-[]->()`) visually represents the graph structure being queried.
- C) Cypher and SQL have very different syntax. SQL uses SELECT/FROM/JOIN/WHERE; Cypher uses MATCH/WHERE/RETURN with visual pattern syntax.
- D) Cypher is a text-based query language that can be written in any text editor, terminal, or application code — it's not limited to a GUI.

---

**Question 6:** A developer comfortable with SQL asks: "In SQL I use INSERT to add data. What's the Cypher equivalent to create new nodes and relationships?"
- A) INSERT
- B) ADD
- C) CREATE
- D) PUSH

**Answer:** C) CREATE
**Explanation:** The lesson states: "In Cypher, the keyword to create new data is CREATE." CREATE can make individual nodes, nodes with properties, and relationships between nodes — all in a single statement using the same parentheses-and-brackets pattern syntax.

Feedback:
- A) INSERT is a SQL command. Cypher doesn't use INSERT — it uses CREATE for adding new nodes and relationships.
- B) ADD is not a Cypher command. Cypher uses CREATE for new data and SET for adding properties to existing nodes.
- D) PUSH is not a Cypher command. It's used in some other contexts (like MongoDB's `$push` for arrays), but not in graph query languages.

---

---

### **Quiz 3: AWS Neptune and Graph Query Languages**

**Question 1:** AWS Neptune is to graph databases as AWS RDS is to relational databases. What does Neptune provide?
- A) A self-hosted open-source graph database
- B) A managed graph database service — handling provisioning, backups, replication, and recovery automatically
- C) A graph visualization tool only
- D) A replacement for Neo4j's query language

**Answer:** B) A managed graph database service — handling provisioning, backups, replication, and recovery automatically
**Explanation:** The lesson describes Neptune as "a fully managed graph database service within the AWS ecosystem." It notes that "Neptune handles infrastructure management, high availability, backups, and integration with AWS tools for security, monitoring, and data ingestion."

Feedback:
- A) Neptune is not self-hosted or open-source. It's a fully managed AWS service. You don't install or maintain any database servers.
- C) Neptune is a full graph database engine, not just a visualization tool. It stores, indexes, and queries graph data. Visualization is handled by separate tools.
- D) Neptune doesn't replace Neo4j's query language. It supports languages like Cypher and Gremlin, as well as SPARQL for RDF-style graphs.

---

**Question 2:** Neptune supports multiple query languages for different use cases. Which of the following query languages does Neptune support? (Select all that apply)
- A) Gremlin
- B) SPARQL
- C) openCypher
- D) SQL
- E) MQL (MongoDB Query Language)

**Answer:** A, B, C
**Explanation:** The lesson states that Neptune supports "multiple graph models and query languages, including property graphs queried with languages like Cypher and Gremlin, as well as RDF-style graphs queried with SPARQL." This multi-language support makes Neptune flexible across different graph use cases.

Feedback:
- A) ✅ Gremlin is a graph traversal language supported by Neptune for querying property graphs.
- B) ✅ SPARQL is supported by Neptune for querying RDF-style graphs.
- C) ✅ openCypher is supported by Neptune as an additional language for querying property graphs.
- D) SQL is for relational databases. Neptune is a graph database and uses graph-specific query languages.
- E) MQL (MongoDB Query Language) is for document stores, not graph databases. Neptune has no connection to MongoDB's query language.

---

**Question 3:** Neptune supports two different graph data models. Match each graph data model to the query languages used with it.

Column A:
1. Property graphs
2. RDF-style graphs

Column B:
A. Cypher and Gremlin
B. SPARQL

**Answer:** 1→A, 2→B
**Explanation:** The lesson states that Neptune supports "multiple graph models and query languages, including property graphs queried with languages like Cypher and Gremlin, as well as RDF-style graphs queried with SPARQL." This distinction reflects two different graph data models, each with its own query language ecosystem.

Feedback:
- 1→A: Property graphs store data as nodes, relationships, and properties. They are queried using Cypher (a pattern-matching language) and Gremlin (a traversal-based language).
- 2→B: RDF (Resource Description Framework) graphs store data as subject-predicate-object triples. SPARQL is the standard query language for this model.

---

**Question 4:** A team running an operational graph database on Neptune needs to perform large-scale analytics across the entire graph. According to the lesson, what does AWS offer to address this?
- A) Running analytics directly on the operational Neptune instance with no performance impact
- B) Neptune Analytics — a serverless analytics engine designed for large-scale graph analytics workloads
- C) Exporting the graph to a relational database for analysis
- D) There is no solution — graph databases cannot perform analytics

**Answer:** B) Neptune Analytics — a serverless analytics engine designed for large-scale graph analytics workloads
**Explanation:** The lesson describes "Neptune Analytics, a serverless analytics engine. It's designed for running large-scale graph analytics workloads that would be expensive or impractical to run directly on an operational graph database."

Feedback:
- A) Running heavy analytics on an operational database can degrade transactional performance. Neptune Analytics exists specifically to offload these workloads to a dedicated engine.
- C) Exporting to a relational database would lose the graph structure and relationships that make graph analytics valuable. Neptune Analytics keeps the data in graph form.
- D) Graph analytics is very much possible — the lesson describes dedicated analytics offerings from both Neptune (Neptune Analytics) and Neo4j (Aura Graph Analytics).

---

**Question 5:** A consultant is advising a company that already uses AWS heavily (S3, Lambda, RDS). They need a graph database for their new recommendation engine. Why might Neptune be a natural fit compared to a standalone Neo4j deployment?
- A) Neptune is always cheaper
- B) Neptune is an AWS-native managed service that integrates seamlessly with the existing AWS ecosystem — backups, security, networking all work with familiar AWS tools
- C) Neo4j can't handle recommendation queries
- D) Neptune uses a completely different data model than Neo4j

**Answer:** B) Neptune is an AWS-native managed service that integrates seamlessly with the existing AWS ecosystem — backups, security, networking all work with familiar AWS tools
**Explanation:** The lesson describes Neptune as handling "infrastructure management, high availability, backups, and integration with AWS tools for security, monitoring, and data ingestion." For teams already invested in AWS, this native integration reduces operational overhead compared to managing a separate graph database deployment.

Feedback:
- A) Neptune isn't always cheaper. Costs depend on usage patterns, instance sizes, and workloads. The main advantage here is ecosystem integration and reduced operational burden, not cost.
- C) Neo4j can absolutely handle recommendation queries — it's one of its core use cases. The advantage of Neptune is AWS ecosystem integration, not capability differences.
- D) Neptune actually supports openCypher (similar to Neo4j's Cypher) alongside Gremlin and SPARQL. The data model (property graphs) is shared; the advantage is managed infrastructure.

---

**Question 6:** You need to model the following scenario: "People who work at the same company and live in the same city often eat at the same restaurants." Which database paradigm is best suited for discovering these multi-hop relationship patterns?
- A) A key-value store
- B) A column-oriented data warehouse
- C) A graph database — where traversing multi-hop relationships between people, companies, cities, and restaurants is a natural operation
- D) A flat file

**Answer:** C) A graph database — where traversing multi-hop relationships between people, companies, cities, and restaurants is a natural operation
**Explanation:** This query involves traversing relationships across multiple entity types (people → companies, people → cities, people → restaurants). The lesson emphasizes that "graph databases treat connections between entities as first-class data" and are built for questions like "Who is connected to whom? How are these entities connected? and What paths or patterns exist across a network?" Multi-hop pattern discovery is a core strength of graph databases.

Feedback:
- A) Key-value stores are optimized for simple lookups by a single key. They can't traverse relationships between people, companies, cities, and restaurants.
- B) Column-oriented data warehouses excel at aggregating large volumes of metrics, not at discovering multi-hop relationship patterns between entities.
- D) Flat files have no query engine or relationship traversal capability. Discovering multi-hop patterns across four entity types would require custom code and be extremely inefficient.
