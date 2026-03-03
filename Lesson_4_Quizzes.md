# Lesson 4: Data Modeling for Graph Databases — Quizzes

---

### **Quiz 1: Graph Database Fundamentals**

**Question 1:** You're modeling an e-commerce system where the most valuable insight is: "Customers who bought X also bought Y." Which database paradigm is purpose-built for this kind of relationship query?
- A) A column-oriented data warehouse
- B) A document store
- C) A graph database — designed to traverse relationships between entities efficiently
- D) A flat file

**Answer:** C) A graph database — designed to traverse relationships between entities efficiently
**Explanation:** "A classic example is an e-commerce recommendation: 'Customers who bought X also bought Y.'" The lesson explains that graph databases excel when "the most important part of your data isn't the individual items—it's the relationships between them."

Feedback:
- A) Column-oriented data warehouses are optimized for aggregating large volumes of metrics (sums, averages). They aren't designed for traversing connections between entities.
- B) Document stores excel at flexible schemas and nested data, but traversing multi-hop relationships (customer → purchase → product → other customers) isn't their strength.
- D) Flat files have no query engine, indexing, or relationship traversal capability. They can't efficiently answer relationship-based questions at scale.

---

**Question 2:** What are the three building blocks of a graph database?
- A) Tables, rows, columns
- B) Nodes (entities), edges (relationships), and properties (attributes)
- C) Documents, collections, fields
- D) Keys, values, indexes

**Answer:** B) Nodes (entities), edges (relationships), and properties (attributes)
**Explanation:** "A graph database represents data using three things: nodes, edges, and properties. Nodes are entities—people, products, places. Edges are the connections between them... Properties are attributes—names, dates, types."

Feedback:
- A) Tables, rows, and columns are the building blocks of relational databases, not graph databases.
- C) Documents, collections, and fields are the building blocks of document stores like MongoDB.
- D) Keys, values, and indexes describe key-value stores (like Redis) and general database indexing concepts, not graph-specific structures.

---

**Question 3:** A fraud detection team needs to find accounts that share addresses, phone numbers, and transaction patterns across multiple hops. In a relational database, this requires many self-JOINs. Why is a graph database more suitable?
- A) Graph databases are always faster for all queries
- B) In a graph, traversing relationships follows direct pointers — no scanning tables to match keys — making multi-hop queries natural and efficient
- C) Relational databases can't store address data
- D) Graph databases don't require any queries

**Answer:** B) In a graph, traversing relationships follows direct pointers — no scanning tables to match keys — making multi-hop queries natural and efficient
**Explanation:** "In a graph, when you traverse a relationship, you're following a direct pointer or address. You don't scan all possible records to match conditions. In SQL, a JOIN typically involves scanning indexes or tables to match keys." For multi-hop relationship queries (fraud rings, social networks), graphs are fundamentally more efficient.

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
**Explanation:** "The insight came from Leonhard Euler in 1736, who formalized what we now call the 'Seven Bridges of Königsberg problem'... Euler proved there was no route that crossed each bridge exactly once." This work laid the foundation for graph theory as a mathematical discipline.

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
**Explanation:** "In 2024, 'GQL'—Graph Query Language—was voted in as the new ISO standard for querying graphs, similar to how SQL is the standard for relational databases." This is a historic milestone — 37 years between the SQL standard and GQL.

Feedback:
- A) GraphQL is a Facebook-created API query language for web services, not a database query language or ISO standard for graph databases.
- C) Cypher is Neo4j's proprietary query language. While influential, it's not an ISO standard. openCypher is the open-source version, and GQL drew from it.
- D) SPARQL is a W3C standard for querying RDF/semantic data, not a general graph database standard. GQL is the new ISO standard for property graphs.

---

**Question 6:** A consultant is evaluating database options for a new system that needs to handle recommendation engines, social network analysis, and supply-chain modeling. All three require traversing complex relationships. Which type of database systems should they evaluate?
- A) Only relational databases like PostgreSQL
- B) Graph databases such as Neo4j, Amazon Neptune, or Azure Cosmos DB
- C) Only key-value stores like Redis
- D) Only document stores like MongoDB

**Answer:** B) Graph databases such as Neo4j, Amazon Neptune, or Azure Cosmos DB
**Explanation:** The lesson lists "recommendation systems, fraud detection, supply-chain modeling, social networks" as graph database use cases and mentions "Example graph systems include Neo4j, Amazon Neptune, Google Spanner Graph, and Azure Cosmos DB." All three requirements are classic graph workloads.

Feedback:
- A) Relational databases can model relationships via JOINs, but multi-hop traversals across recommendations, social networks, and supply chains become prohibitively expensive with self-JOINs.
- C) Key-value stores like Redis are optimized for simple lookups by key, not for traversing complex relationship patterns across multiple entity types.
- D) Document stores like MongoDB handle flexible data well but aren't optimized for the multi-hop relationship traversals that recommendation engines and social networks require.

---

---

### **Quiz 2: Neo4j and Cypher Queries**

**Question 1:** In Cypher, the query `MATCH (p:Person)-[:ACTED_IN]->(m:Movie) RETURN p.name, m.title` uses two types of syntax. What do the parentheses `()` and the square brackets with arrow `-[]->` represent?
- A) Parentheses = properties; brackets = functions
- B) Parentheses = nodes; square brackets with arrows = relationships (edges) with direction
- C) Parentheses = tables; brackets = columns
- D) Parentheses = collections; brackets = documents

**Answer:** B) Parentheses = nodes; square brackets with arrows = relationships (edges) with direction
**Explanation:** "In Cypher, you use parentheses to represent nodes" and "square brackets with arrows represent edges. The arrow direction shows which way the relationship goes." So `(p:Person)` is a Person node, and `-[:ACTED_IN]->` is a directed "ACTED_IN" relationship.

Feedback:
- A) Properties are stored *inside* nodes and relationships, not represented by parentheses. Parentheses denote nodes; brackets denote relationships.
- C) Cypher doesn't use tables or columns. It's a graph query language where parentheses represent nodes and brackets represent edges.
- D) Collections and documents are MongoDB concepts. Cypher uses parentheses for nodes and brackets for relationships in a graph model.

---

**Question 2:** You want to find all movies that a specific actor appeared in. Which Cypher clause describes the pattern you're looking for?
- A) CREATE — to make new nodes
- B) MATCH — to describe a pattern to find in the graph
- C) DELETE — to remove matching nodes
- D) MERGE — to create or find

**Answer:** B) MATCH — to describe a pattern to find in the graph
**Explanation:** "'Match' describes a pattern we're looking for... in plain English: find a person node that's connected to a movie node through an 'acted in' relationship." MATCH is the primary read operation in Cypher — you describe what the relationship pattern looks like, and Neo4j finds all matches.

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
**Explanation:** "'Return' specifies what to give back. We could return the node itself, specific properties like name and title, or even counts and aggregations." RETURN is analogous to the SELECT clause in SQL — it controls the shape of the result set.

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
**Explanation:** "'Merge' is like 'create or find.' If the pattern already exists, Merge doesn't create a duplicate. Otherwise, it creates it." This is essential for data loading scenarios where you want idempotent operations that avoid duplicates.

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
**Explanation:** "Cypher reads almost like plain English. You can describe patterns you're looking for, and Neo4j will find matching structures in the graph." The visual pattern syntax (`()-[]->()`) is designed to be intuitive, especially for relationship-heavy queries.

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
**Explanation:** "Creating data uses the 'create' command." In Cypher, CREATE can make individual nodes, nodes with properties, and relationships between nodes — all in a single statement using the same parentheses-and-brackets pattern syntax.

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
**Explanation:** "AWS Neptune is the managed graph database service from Amazon. It's similar to how RDS provides managed relational databases." Neptune "handles the provisioning, backups, replication, and point-in-time recovery. You don't manage servers. You simply connect and query the graph."

Feedback:
- A) Neptune is not self-hosted or open-source. It's a fully managed AWS service. You don't install or maintain any database servers.
- C) Neptune is a full graph database engine, not just a visualization tool. It stores, indexes, and queries graph data. Visualization is handled by separate tools.
- D) Neptune doesn't replace Neo4j's query language. In fact, it supports openCypher (similar to Neo4j's Cypher), along with Gremlin and SPARQL.

---

**Question 2:** Neptune supports multiple query languages for different use cases. Which languages are available?
- A) Only SQL
- B) Gremlin, SPARQL, and openCypher
- C) Only MQL (MongoDB Query Language)
- D) Only Python

**Answer:** B) Gremlin, SPARQL, and openCypher
**Explanation:** "Neptune supports multiple query languages. The two main ones are Gremlin and SPARQL" and "Neptune also supports 'openCypher', which is similar to the Cypher language." This multi-language support makes Neptune flexible across different graph use cases.

Feedback:
- A) SQL is for relational databases. Neptune is a graph database and uses graph-specific query languages (Gremlin, SPARQL, openCypher).
- C) MQL (MongoDB Query Language) is for document stores, not graph databases. Neptune has no connection to MongoDB's query language.
- D) Python is a general-purpose programming language, not a graph query language. You can use Python *drivers* to connect to Neptune, but the queries themselves are in Gremlin, SPARQL, or openCypher.

---

**Question 3:** A developer describes Gremlin as a "step-by-step" approach to querying graphs. What kind of language is Gremlin?
- A) A declarative language — you describe what you want
- B) A graph traversal language — you describe how to traverse the graph step by step, following edges and filtering nodes
- C) A data definition language
- D) A markup language

**Answer:** B) A graph traversal language — you describe how to traverse the graph step by step, following edges and filtering nodes
**Explanation:** "Gremlin is a graph traversal language. You describe how to traverse the graph—step by step—following edges and filtering nodes." Unlike Cypher (which is more declarative — "find this pattern"), Gremlin is imperative — "start here, go to this edge, filter by this property."

Feedback:
- A) Declarative languages describe *what* you want (like SQL or Cypher). Gremlin is imperative/procedural — you describe *how* to traverse the graph step by step.
- C) A data definition language (DDL) defines schemas (CREATE TABLE, ALTER TABLE). Gremlin is for querying and traversing graph data, not defining schemas.
- D) A markup language (like HTML or XML) structures documents for display or data exchange. Gremlin is a query/traversal language for graph databases.

---

**Question 4:** A knowledge graph stores facts as triples like "Alice knows Bob" (subject, predicate, object). Which data format and query language are designed specifically for this kind of semantic data?
- A) JSON and MQL
- B) RDF (Resource Description Framework) and SPARQL
- C) CSV and SQL
- D) BSON and Gremlin

**Answer:** B) RDF (Resource Description Framework) and SPARQL
**Explanation:** "RDF stands for 'Resource Description Framework.' It's a format for representing data as 'triples': a subject, a predicate, and an object... for example: 'Alice, knows, Bob.'" SPARQL is "used for querying 'semantic data'" in RDF format. Together they form the backbone of semantic web and knowledge graph applications.

Feedback:
- A) JSON and MQL are used with document stores like MongoDB. They don't natively represent semantic triples (subject-predicate-object).
- C) CSV and SQL are for flat/tabular and relational data. They lack the semantic triple structure that RDF provides for knowledge graphs.
- D) BSON is MongoDB's binary JSON format, and Gremlin is a traversal language for property graphs. Neither is designed for semantic/triple-based data.

---

**Question 5:** A consultant is advising a company that already uses AWS heavily (S3, Lambda, RDS). They need a graph database for their new recommendation engine. Why might Neptune be a natural fit compared to a standalone Neo4j deployment?
- A) Neptune is always cheaper
- B) Neptune is an AWS-native managed service that integrates seamlessly with the existing AWS ecosystem — backups, security, networking all work with familiar AWS tools
- C) Neo4j can't handle recommendation queries
- D) Neptune uses a completely different data model than Neo4j

**Answer:** B) Neptune is an AWS-native managed service that integrates seamlessly with the existing AWS ecosystem — backups, security, networking all work with familiar AWS tools
**Explanation:** For teams already invested in AWS, Neptune offers the managed service benefits ("you don't manage servers") combined with native AWS integration — IAM for security, VPC for networking, CloudWatch for monitoring — reducing operational overhead compared to managing a separate Neo4j deployment.

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
**Explanation:** This query involves traversing relationships across multiple entity types (people → companies, people → cities, people → restaurants). The lesson emphasizes that graph databases are designed for exactly this: "Sometimes the most important part of your data isn't the individual items—it's the relationships between them." Multi-hop pattern discovery is a core strength of graph databases.

Feedback:
- A) Key-value stores are optimized for simple lookups by a single key. They can't traverse relationships between people, companies, cities, and restaurants.
- B) Column-oriented data warehouses excel at aggregating large volumes of metrics, not at discovering multi-hop relationship patterns between entities.
- D) Flat files have no query engine or relationship traversal capability. Discovering multi-hop patterns across four entity types would require custom code and be extremely inefficient.
