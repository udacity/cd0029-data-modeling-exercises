# Lesson 4: Data Modeling for Graph Databases

## Video Summary

We just learned how graph databases represent and query relationship-focused data more efficiently than traditional databases.

### Lesson Overview

In this lesson we explored a database technology that's been around for decades but only recently became the basis for the first new database query language standard since SQL. In 2024, the International Organization for Standardization released **GQL** (Graph Query Language)—reflecting that graph databases have matured from niche tools into a core part of modern data systems.

Unlike systems that center on rows, documents, or key-value pairs, graph databases treat **connections between entities as first-class data**. They're built for questions like: Who is connected to whom? How are these entities connected? What paths or patterns exist across a network?

Graph databases fall under the broader **NoSQL** umbrella. Like other non-relational systems, they trade rigid schemas and traditional SQL joins for flexibility and performance. But unlike other NoSQL systems, they **store relationships directly** rather than computing them on the fly.

This lesson covered:
- Graph database **history and motivation**
- Representing data using **nodes, relationships, and properties**
- Querying data using **Cypher and GQL**
- **CRUD operations** in graph databases
- **DDL, ACID guarantees**, and data modeling principles
- Graph database **challenges** and **cloud providers**

### What We Covered

**Motivation for Graph Databases: The Seven Bridges of Königsberg**

We started with a puzzle from eighteenth-century Prussia. The **Seven Bridges of Königsberg** problem asks: could someone walk through the city and cross each bridge once—and only once? Mathematician **Leonhard Euler** recognized that brute-forcing all 5,000+ possible sequences was impractical. Instead, he asked: what information actually matters?

Euler realized that the city's exact street layout, distances, and geography were noise, not signal. The only thing that mattered was the **land masses** (nodes) and the **bridges** (edges) between them. He proved that for a valid path, a maximum of two nodes (start and end) can have an odd number of edges. Since all four land masses in Königsberg had an odd number of bridges, no such walk exists.

More importantly than solving the puzzle, Euler devised an entirely new way to think about problems by modeling data as a graph. These graph abstractions—stripping away irrelevant details and focusing on structure—are the foundation of modern graph databases.

**Graphs Are Everywhere**

Bridges aren't the only things modeled this way. The internet is a graph of computers that connect to each other. The World Wide Web is a graph of websites that link to one another. The difference now is that we've built specialized software that focuses primarily on graph data.

**Neo4j and the ECM Origin Story**

Neo4j was created by a team building an **enterprise content management (ECM)** system in the early 2000s—a system for storing, organizing, and retrieving large amounts of interconnected content (documents, pages, metadata, permissions, versions, and references). Think Microsoft SharePoint.

The relational database they were using was slow and limiting for this kind of data. Simple questions like "What documents reference this one?" or "How is this piece of content connected to everything else?" required **complex joins** and didn't scale well as relationships became deeper and more numerous. So instead of forcing this data into relational tables, they built a new kind of database. In 2007, the Neo4j CEO coined the term **"graph database"** and began marketing it to other tech companies.

Today, Neo4j is a production-ready graph database with **full ACID guarantees**, a query language designed specifically for traversing relationships, and performance optimized for deeply connected data. All major cloud providers—AWS, Azure, Google Cloud—now offer managed graph database services.

**Graph Database Applications**

Graph databases are widely used for problems where connections are the primary thing you care about:
- **Social and communication networks**
- **Fraud detection and transaction analysis**
- **Recommendation systems**
- **Access control or network topology**

**Knowledge Graphs and AI**

Graph databases are central to **knowledge graphs**—systems that store entities and the relationships between them so that information can be interpreted in context. Historically, knowledge graphs have been valuable for information retrieval tasks like search engines and recommendation systems.

What's changed recently is the rise of AI. Large language models (LLMs) make knowledge far more accessible because you can ask questions in plain language—like "Which customers are most affected by recent price changes?" or "What products are most strongly associated with churn?" To answer those questions accurately using your actual data (not just general training or hallucinations), AI systems increasingly rely on techniques like **GraphRAG** or agent-based approaches that query a graph database behind the scenes.

Euler showed that the way you model relationships determines what you can learn—and that idea now underpins knowledge graphs and modern AI systems.

**How Graph Databases Work**

Instead of organizing information into tables or collections, a graph database stores three core components:
- **Nodes**: Entities like people, products, or documents
- **Relationships**: How those entities are connected
- **Properties**: Data about both nodes and relationships

Each node and relationship stores **direct references (pointers)** to its properties and to each other. Because of this layout, the database does not need to search tables or perform joins to discover connections—the connections are already there.

**Comparing Database Components:**

| Graph DB | Relational DB | MongoDB |
|---|---|---|
| Node | Row | Document |
| Property | Column | Field |
| Label | Table | Collection |
| Relationship | JOIN (using keys) | Embedding or $lookup |

Labels are just classifications that describe characteristics of nodes—a single node can have multiple labels, and labels don't determine physical storage. But **relationships** are where graph databases are fundamentally different: they are **first-class data objects**, stored directly with direction, type, and their own properties. A relationship isn't something the database needs to compute—it's something the database already knows.

**Anatomy of Graph Databases**

Under the hood, graph databases follow the same broad structure as other databases: they store data on disk, maintain metadata, and provide a query engine. The difference is what they're **optimized to query**:
- **Relational DBs**: Combine tables using JOINs
- **Document DBs**: Retrieve and filter documents
- **Graph DBs**: Traverse relationships

Because relationships are stored directly, graph databases need a query language designed to express **patterns of connections**, not just filters over rows or documents.

**Querying: Cypher and GQL**

In SQL, finding Alice's friends requires joining a People table to a Relationships table and back, with WHERE filters. In a graph query, the syntax mirrors the shape of the graph itself:

```
MATCH (person:Person {name: 'Alice'})
      -[:FRIENDS_WITH]->
      (friend:Person)
RETURN friend.name
```

- **Nodes** appear in parentheses—like a visual representation of the graph
- **Arrows** represent relationships with their type
- The query says: find Alice, follow her FRIENDS_WITH relationships, return those people's names

This pattern-based style comes from **Cypher**, the query language originally developed by Neo4j, designed to be readable and visual. More recently, this approach has been standardized as **GQL**—the first new database language standard from ISO since SQL itself (released in 2024). Vendors like Neo4j, Microsoft, and Google have been actively aligning their graph query engines with GQL.

**CRUD in Graph Databases**

To illustrate CRUD, we built a grocery store chatbot scenario where a customer asks "What fruits should I add to my cart?"—a recommendation problem solved by direct graph traversal rather than computation-heavy queries.

**Read** — Start at the customer node, follow relationships to categories the customer likes, filter to fruits that are in stock, and return their names. Key clauses:
- `MATCH` specifies the pattern to search for
- `WHERE` adds filters based on properties or labels
- `RETURN` defines what to include in the result
- `DISTINCT`, `ORDER BY`, and `LIMIT` work just like in SQL

Graph queries are also more **interpretable**: a GraphRAG system can traverse the query path to explain its reasoning ("Because you like citrus fruits and we currently have oranges and lemons in stock, I'd recommend those today").

**Create** — Creating data means creating nodes, relationships, or both. `CREATE` is the Cypher keyword; `INSERT` is the GQL equivalent. One syntax difference: when applying multiple labels, Cypher allows colons or ampersands (`Fruit:Organic` or `Fruit&Organic`), while GQL only supports ampersands.

**Update** — Use `MATCH` to find nodes or relationships, then `SET` to modify properties or `MERGE` to modify relationships. Conceptually similar to `UPDATE…WHERE` in SQL, but matching happens through graph patterns, not table filters.

**Delete** — Use `MATCH` followed by `DELETE`. Two common cases: deleting relationships only (keeping nodes intact), or deleting nodes with `DETACH DELETE` which also removes attached relationships. Most graph databases won't let you delete a node that still has relationships—forcing you to be explicit about structural removal.

Graph databases support **full CRUD**, not just reads—which is a big reason why GQL emerged as a true database standard rather than just a query layer.

**DDL in Graph Databases**

Like many NoSQL systems, graph databases use a **flexible data model**. Nodes and relationships can have properties added, changed, or removed at any time, and different nodes of the same type don't need to share the same structure. Structure emerges as data is created and updated.

There's no `ALTER TABLE`-style command to change structure. Instead:
- `CREATE` adds new nodes or relationships
- `MATCH + SET` updates properties
- `MATCH + DELETE` removes nodes or relationships

Structure changes happen through **regular graph operations**, not a separate schema migration step.

That said, the emerging **GQL standard** brings more explicit schema support. With GQL, you can choose to define graph schemas—including node types, relationship types, and constraints—or continue working in a schema-optional way. Vendor implementations vary: Google Cloud Spanner, for example, uses keywords like `KEY`, `PROPERTIES`, `SOURCE`, and `DESTINATION` rather than arrows and brackets, but the underlying structure being described is the same.

The key takeaway: graph databases **don't require DDL**—but modern standards like GQL give you the option to introduce it when structure and validation matter.

**ACID Guarantees in Graph Databases**

Many graph databases, including Neo4j, offer ACID compliance—but these guarantees are applied at different scopes compared to relational systems.

**Atomicity** — The most common atomic unit is a single query or update. Creating a node with all its properties, creating a relationship, or updating multiple properties in one statement all happen atomically. Neo4j also supports **explicit multi-step transactions**, but many graph workloads are designed so that related data can be updated safely in one operation.

**Consistency** — Graph databases default to flexibility, similar to document databases. They allow nodes with missing properties, relationships without metadata, and properties that vary across nodes with the same label. Unless you explicitly enforce **constraints**, the database accepts that data. This means consistency becomes a **design decision**, not a default guarantee. The same CRUD anomalies from other NoSQL systems can occur:
- **Insert anomalies**: Creating a node before all properties are known
- **Update anomalies**: Duplicated data across nodes not automatically kept in sync
- **Delete anomalies**: Removing a node may erase important context like historical pricing or supply-chain relationships

Neo4j provides optional **constraints**—rules enforced at write time (uniqueness, required properties)—that reject invalid writes so bad data never lands in the graph.

**Isolation** — Individual updates to nodes and relationships are isolated by default. Concurrent updates are handled safely and conflicting writes won't partially corrupt the graph. Explicit transactions provide **snapshot-style isolation**: each transaction works against a consistent view, and conflicts cause the transaction to fail rather than silently overwrite data.

**Durability** — Provided through writing data to disk, replicating data across machines, and coordinating writes across a cluster. Neo4j supports clusters with primary and secondary (replica) servers. If a machine fails, another node takes over—data remains available and intact. Graph databases also support **horizontal scaling**: data can be split across machines, reads served from replicas, and writes coordinated to maintain consistency.

**Graph Database Modeling Principles**

With all this flexibility, the lesson provided a structured framework:

**1) Focus on the application you're building.** Write down the key questions the system needs to answer. What nodes are those questions about? What properties do you need? What relationships connect them?

**2) Prioritize representative queries.** In SQL, lookup time is proportional to table size. In graph databases, it's proportional to **traversal length**—the number of relationship links you follow. So you want the most common paths to be efficient.

**3) Evaluate denormalization vs. normalization.** In graph databases, normalization means introducing additional nodes and relationships instead of repeating properties. Denormalization means collapsing information into node or relationship properties.

*Favor denormalization when:*
- Keeping info together simplifies the model and reasoning
- Data is always accessed together
- Data is usually updated together
- Further normalization would significantly increase hops for common traversals

*Favor normalization when:*
- Relationships have high or growing cardinality
- Information would be duplicated across many nodes
- A node or relationship makes sense on its own and is queried independently

**Intermediate nodes** are useful when relationships carry a lot of information. Instead of packing properties onto an edge, you can model the concept (e.g., "Shipment Status" or "Batch") as its own node with its own connections. This is especially valuable when the intermediate data can be shared or queried independently.

**4) Determine consistency and validation needs.** Validation can be specified at the GQL schema level (declared up front) or through database constraints (enforced at runtime). You decide how much structure to enforce and where—validation is part of your data modeling responsibility.

**Graph Database Challenges**

Graph databases aren't perfect. In this video, we reviewed some of those challenges that they come with. 

**OLTP vs. OLAP** — Graph databases are designed primarily for **OLTP-style workloads**: fast reads and writes of individual nodes and relationships, and efficient traversal along graph paths. Full graph scans for analytics can be expensive and slow. To address this, vendors offer separate analytics tools (Neo4j Graph Data Science, Neo4j Graph Analytics) that add optimized algorithms and parallel processing—similar to a data warehouse for SQL.

**Narrow Scope** — Graph databases emerged to solve a specific problem: modeling and querying relationships efficiently when connections matter more than individual records. They excel at social networks, recommendation engines, fraud detection, and knowledge graphs. But not everything is a graph problem—if data is highly structured and tabular, relationships are shallow, or complexity lives in properties rather than connections, a relational or document database may be the better choice. This is why many teams practice **polyglot persistence**, introducing a graph database only when relationship-heavy queries become central.

**Integration Challenges** — Many dashboards, BI tools, and visualization platforms are designed around tables and star schemas. These tools may struggle to connect directly to graph databases or require custom transformations. Not all application libraries integrate cleanly with graph databases either.

**Operational Challenges** — Running a graph database means managing servers, storage, networking, replication, and sometimes sharding. That complexity grows as systems scale—which is why managed cloud offerings have become increasingly popular.

**Cloud Providers for Graph Databases**

In this video, we cover examples of cloud vendors that help host graph databases as a service.

**Neo4j Aura** — The fully managed cloud service from Neo4j's creators. Handles infrastructure provisioning, upgrades and patching, backups and replication, and scaling. You connect to a graph database endpoint and start querying. Aura also offers a dedicated **Graph Analytics** service for OLAP workloads, and integrates with AWS, GCP, and Azure.

**Amazon Neptune** — A fully managed graph database within the AWS ecosystem. Supports multiple graph models and query languages, including property graphs (Cypher, Gremlin) and RDF-style graphs (SPARQL). Handles infrastructure, high availability, backups, and integration with AWS tools. **Neptune Analytics** provides a serverless engine for large-scale graph analytics workloads.

**Other Providers** — Oracle provides graph capabilities as part of its database offerings with its own query languages and tooling. These systems don't follow the GQL standard but are optimized for specific enterprise and analytics use cases.

Graph databases are no longer niche or experimental. Major cloud providers now offer managed graph services, each with different trade-offs around query language support, scalability, and ecosystem integration.

---

### Lesson Review

Graph databases represent a fundamentally different way of thinking about data. Instead of organizing information into tables or documents, they store **nodes**, **relationships**, and **properties**—with connections treated as first-class citizens rather than something reconstructed at query time through joins.

This idea traces back to Euler's insight in 1736: strip away the noise, focus on structure, and the right answers emerge. That same principle now powers knowledge graphs, recommendation engines, fraud detection systems, and the AI applications built on top of them through techniques like **GraphRAG**.

We queried graphs using **Cypher** and learned that the syntax is designed to mirror the shape of the data itself—nodes in parentheses, relationships as arrows, patterns matched directly. The **GQL standard** (ISO, 2024) formalizes this approach as the first new database language since SQL, and vendors are actively aligning with it.

Graph databases are **schema-flexible by default**. Structure emerges through the data you write, not through DDL migrations. But modern standards like GQL and tools like Neo4j constraints give you the option to introduce validation when it matters. **ACID guarantees** apply—atomicity at the operation level, snapshot-style isolation for explicit transactions, durability through replication and clustering—but consistency is a design decision, not an automatic guarantee.

The central modeling question is how much to **normalize** (more nodes and relationships, less duplication) versus **denormalize** (fewer hops, simpler traversals). The answer depends on your application's most common queries, because graph performance scales with **traversal length**, not table size.

Graph databases are optimized for **OLTP** workloads. Full graph scans for analytics require separate tooling. And not every problem is a graph problem—if relationships are shallow or data is primarily tabular, relational or document databases may be simpler and equally effective. **Managed cloud services** like Neo4j Aura and Amazon Neptune handle the operational burden, letting you focus on modeling and querying.

Key takeaways:

- Graph databases store **nodes, relationships, and properties**—connections are first-class data, not computed via joins
- **Cypher** uses a visual, pattern-based syntax; **GQL** (2024) standardizes this as the first new ISO database language since SQL
- Graph performance depends on **traversal length**, not table size—design your most common paths to be short
- Graph databases are **schema-flexible by default**; structure evolves through regular CRUD operations, not DDL migrations
- **ACID guarantees** exist but are scoped differently—atomicity at the operation level, consistency as a design decision with optional constraints
- **CRUD anomalies** (insert, update, delete) can occur just like in other NoSQL systems—less database enforcement means more application responsibility
- **Normalization** in graphs means more nodes and relationships; **denormalization** means fewer hops and simpler traversals—choose based on query patterns
- **Intermediate nodes** (e.g., batches, shipments) are useful when relationships carry significant data or need to be shared across the graph
- Graph databases are designed for **OLTP**; analytics require separate tooling like Neo4j Graph Data Science or Neptune Analytics
- Not everything is a graph problem—graph databases add the most value when **connections matter more than individual records**
- **Managed cloud services** (Neo4j Aura, Amazon Neptune) handle infrastructure, scaling, and replication so you can focus on data modeling
- **Polyglot persistence**—combining relational, document, and graph databases—is increasingly common as systems grow more complex
