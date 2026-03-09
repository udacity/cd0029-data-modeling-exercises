# All Tasks — Data Modeling Course

## Lesson 1

### Exercise 1: Identifying Data, Information, and Knowledge

- **Task 1:** Fill in the blank (after GROUP BY) in the first query to start extracting survey data
- **Task 2:** Modify the initial query to filter for results where Country is 'United States of America' and YearsCodingExp is between 5 and 10 years.
- **Task 3:** Modify the query by replacing blanks with the correct conditional statements for the CASE expression, and the WHERE clause to bucket years of experience
- **Task 4:** Modify the query by replacing blanks as part of the last piece of the WHERE clause. This should allow us to only see Rust users appear in the  results. Do the same afterwards, but for C++ users.
- **Task 5:** Fill in the blanks as part of the last piece of the WHERE clause to have only Rust users AND C++ users appear in the results.
- **Task 6:** Fill in the blanks as part of the last piece of the WHERE clause to have both PostgreSQL users OR MongoDB users appear in the filter.
- **Standout:** Think of what some of the potential pitfalls of this analysis are. We believe we found some patterns we know to be true, but how could we have erred in coming to these conclusions? 

### Exercise 2: Data, Metadata, Query Engines

- **Task 1:** Fill in the blank column names after the CREATE OR REPLACE TABLE portion of the DuckDB SQL statement to configure our initial table which aligns with the information provided.
- **Task 2:** Fill in the blank rows after the INSERT INTO ... VALUES portion of the DuckDB SQL statement to insert data which aligns with the table provided.
- **Task 3:** Fill in the blanks after the CREATE TABLE ... portion of the SQL statement, to create columns in PostgreSQL which aligns (in terms of type and name) with the data provided.
- **Task 4:** Fill in the blank rows after the INSERT INTO ... VALUES portion of the PostgreSQL statement to insert data which aligns with the table provided.
- **Task 5:** Alter the columns in both DuckDB and PostgreSQL using the appropriate DDL to add customer ID as a blank column — and then re-run the selected queries.
- **Task 6:** Add the following records and then run the query to see newly inserted data.
- **Task 7:** Add the following records and then run the query to see newly inserted data.
- **Task 8:** Calculate the average price across the files.
- **Task 9:** Let's query the metadata information table in PostgreSQL, that was stored there by DuckLake. Select table_name, and table_schema columns.

### Exercise 3: OLTP-OLAP Use Cases

- **Task 1:** Select 'query' from tpch_queries table. See what does it contains.
- **Task 2:** Import TPCH_QUERY_STRING from the utils library we've prepared.
- **Task 3:** Explain: why is DuckDB so much faster than Postgres for analytical reads that involve large aggregations over many elements, and Postgres is better at fetching/writing individual rows?

### Exercise 4: Structured and Unstructured Data

- **Task 1:** Complete the code below to lookup previousJobs if they were full time
- **Task 2:** Update services to also include Data Engineering

### Exercise 5: Visualizing a Graph with Python

- **Task 1:** Let's remove Helen from the graph. You can use the graph.remove(node_number) code. Remember the node number Helen was assigned.
- **Task 2:** Add a relationship between Emily and Grace and adjust the create_social_graph function.
- **Task 3:** Remove Charlie from the graph.

---

## Lesson 2

### Exercise 1: Testing Transactions in PostgreSQL

- **Task 1:** Create a table Customers with column customer_id, full_name, and email. The column types should be VARCHAR. Set primary the key.
- **Task 2:** Try to insert Charlie Brown into the table, with customer_id 3. Use the format Values(customer_id, full_name) for the actual record.
- **Task 3:** Try to insert Eve Davis into the table, with customer_id 4, and email alice@example.com. Use the format Values(customer_id, full_name, email) for the actual record.
- **Task 4:** Try to set the balance of customer with account_id 101 to -50. Complete the query below.
- **Task 5:** Set the addition and subtraction values of the balance query to balance - 5000 and balance + 5000.
- **Task 6:** Commit the transaction using conn1.commit(). Close the connection and the cursor using the .close() functionality.
- **Task 7:** Open another connection called new_conn, and set the cursor to new_conn.cursor().

### Exercise 2: Creating Anomalies

- **Task 1:** Alice has a new email address, 'alice.new@example.com'. We need to update her customer record. Use 'SET email = alice.new@example.com'.
- **Task 2:** Fill in the Delete statement WHERE clause for Bob's account.
- **Task 3:** Normalize the schema below. Fill in the query with customer_id and full_name.

### Exercise 3: Modeling Data for OLAP Use Cases

- **Task 1:** For the FactSales table, add the quantity (integer) column into the create table statement.
- **Task 2:** Create and Populate DimCategory by filling in the blanks in the SQL query.
- **Task 3:** Fill in the blanks below to alter the old DimProduct table to reference the DimCategory table.
- **Task 4:** Write the Report Query. Fill in the blanks to join all the tables on the correct conditions.

### Exercise 4: Dealing with Flexible Data

- **Task 1:** Update the Alter Table statement to add the column source as a varchar.
- **Task 2:** Update the query statement to extract source from the misc_sale_metadata JSON column.
- **Task 3:** Update the query to aggregate the number of sales from each source.
- **Task 4:** Update the WHERE clause in order to find sales coming from Google Search.

### Exercise 5: Launching AWS RDS Postgres

- **Task 1:** In the cells provided, replace the placeholder values with your actual AWS credentials.
- **Task 2:** Go ahead and name the database. You can use the syntax db_name = "…".
- **Task 3:** As part of the exercise, let's create a very simple query.
- **Task 4:** Cleanup all resources!

---

## Lesson 3

### Exercise 1: Querying MongoDB

- **Task 1:** Using MongoDB, find orders over $100.
- **Task 2:** Write the equivalent query in PostgreSQL and execute it without any joins.
- **Task 3:** Write a join between PostgreSQL Customers and Orders tables; select all orders. Run the cell. Do the same for MongoDB.
- **Task 4:** Fill in the $group stage of the query below.
- **Task 5:** MongoDB Aggregation with Mixed Data Types — complete the aggregation to calculate total_spent by customer.
- **Task 6:** Insert the following values into our equivalent PostgreSQL table.

### Exercise 2: Creating Collections and NoSQL Data Modeling

- **Task 1:** Add the seller name as "name": "ArtistStudio123" in listing 1002.
- **Task 2:** Add a new bid into the collection, with the bidder_name "MuseumBuyer".
- **Task 3:** Query the fields for a seller that goes by "TimepieceCollector".
- **Task 4:** Find listings between 1000 and 5000 dollars.
- **Task 5:** Increment view counts for the item with listing ID 1001.
- **Task 6:** Create diverse listings for the marketplace (at least 3 new listings with completely different product categories).

### Exercise 3: NoSQL on AWS

- **Task 1:** In the cell below, replace the placeholder values with your actual AWS credentials.
- **Task 2:** Query anything you want across each of the databases!
- **Task 3:** Cleanup all resources!

---

## Lesson 4

### Exercise 1: Getting Started With Neo4j

- **Task 1:** Find all products purchased by a specific customer (Alice, C001).
- **Task 2:** Find customers who have purchased the same product (Laptop, P001).
- **Task 3:** Find products rated 5 stars.
- **Task 4:** Find customers with similar purchase history (multi-hop relationship from Alice).

### Exercise 2: Creating and Populating Graphs in Neo4j

- **Task 1:** Create a simple graph model (denormalized approach with Customers, Products, PURCHASED and RATED relationships).
- **Task 2:** Create an enhanced, normalized model with Category and CustomerSegment hub nodes.
- **Task 3:** Query by Category Hub — find all products in a category and their average rating.
- **Task 4:** Customer Segment Analysis — find the purchasing patterns of different customer segments.
- **Task 5:** Product Affinity (Products Bought Together) — find products frequently purchased together using the Order intermediate node pattern.
- **Task 6:** Customer Lifetime Value — calculate total spending and order count per customer.
- **Task 7:** Supplier Performance Analysis — analyze supplier performance using the refactored graph.

### Exercise 3: Graph Databases on AWS

- **Task 1:** In the cell below, replace the placeholder values with your actual AWS credentials.
- **Task 2:** Choose a name for your Neptune cluster.
- **Task 3:** Review and run the Gremlin query examples below.
- **Task 4:** Run the openCypher query examples below.
- **Task 5:** Cleanup all resources!
