# Lesson 3: Data Modeling for Document Stores

## Video Summary

We just learned how document databases handle flexible, semi-structured data and how they differ from traditional relational databases.

### What We Covered

**The NoSQL Philosophy**

We learned that NoSQL stands for "not only SQL"—it was never about replacing relational databases, just complementing them. NoSQL databases were designed for scenarios where strict, predefined schemas don't fit.

MongoDB (short for "humongous database") was built to handle large volumes of unstructured data that changes frequently. It grew out of a real-world need—an ad platform serving 400,000 ads per second.

**Document Database Fundamentals**

MongoDB stores data internally as **BSON** (binary JSON) for efficiency, but it looks and behaves like JSON to developers.

**Terminology translation:**
- Collection = Table
- Document = Row
- Field = Column

The key advantage: **flexible schemas**. We can add new fields to some documents without touching others. No schema migrations, no downtime, no rebuilding half our application just to add one new piece of information.

**Document Stores vs Key-Value Stores**

We learned the distinction: Key-value systems like Redis only have keys and corresponding data—very fast for simple lookups but no sorting or filtering. Document stores organize data into fields within documents, supporting complex queries and aggregations.

**CRUD Operations with MQL**

MongoDB uses operators that start with a dollar sign (`$`) to tell the system "this is an instruction, not data":

- **$set**: Change or add a field
- **$unset**: Remove a field
- **$push**: Append to an array

This is fundamentally different from SQL. MongoDB doesn't rewrite whole rows—it surgically updates only what we specify.

**Comparison with Other Document Stores:**
- **DynamoDB**: Uses colons (`:`) for placeholder values
- **Firestore**: Uses double equals (`==`) for filtering
- **DynamoDB limitation**: Can only delete by primary key, while MongoDB can delete based on any filter

**Aggregation Pipelines: ETL in MongoDB**

We learned about MongoDB's built-in framework for Extract, Transform, Load operations. An aggregation pipeline processes documents through multiple stages—filtering, reshaping, grouping, sorting, and even joining.

**Key stages we practiced:**

**$lookup** - Similar to SQL's LEFT OUTER JOIN. Enriches documents by matching and attaching related documents from another collection. Important note: Unlike optimized SQL joins, MongoDB's `$lookup` is more expensive. Use it when needed, but it's not something to rely on for every query.

**$group** - Groups documents and computes aggregations. When we see `$sum: 1`, we're counting documents (treating each one as 1). Supports various aggregation functions like sum, average, min, max.

**Scaling with MongoDB Atlas**

We explored MongoDB's managed service (Platform-as-a-Service):

**MongoDB Atlas** handles the infrastructure so we don't manage servers. It provides automatic backups, monitoring, and easy setup.

**Scaling strategies:**
- **Scaling up**: Choose higher tiers with more CPU cores and RAM
- **Sharding**: MongoDB's term for horizontal scaling—splitting data across multiple machines to handle growth beyond what one machine can manage

**DynamoDB vs MongoDB Atlas**

We learned the architectural difference: DynamoDB is deeply integrated into AWS at the infrastructure level, while MongoDB Atlas runs on virtual machines. This gives DynamoDB more seamless scaling within the AWS ecosystem.

**DynamoDB's capacity model** uses read and write capacity units—think of them like arcade tokens. We spend a specific number of units for each operation.
