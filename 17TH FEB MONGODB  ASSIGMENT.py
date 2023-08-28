#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>
Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use
MongoDB over SQL databases?MongoDB is a widely used open-source NoSQL database management system. It falls under the category of document-oriented databases, which store and manage data in a format similar to JSON (BSON), allowing for flexibility in data structures and schemas. MongoDB is designed to handle large amounts of unstructured or semi-structured data and offers features like horizontal scalability, high availability, and fast querying.

Non-relational databases, often referred to as NoSQL databases, are databases that do not rely on the traditional tabular structure of rows and columns found in relational databases. Instead, they offer flexible ways to store and retrieve data, making them suitable for scenarios where data formats are diverse or unpredictable. NoSQL databases can be categorized into various types, including document-oriented, key-value, column-family, and graph databases.

In scenarios where data structures are complex or evolving, and where performance, scalability, and agility are priorities, MongoDB might be preferred over traditional SQL databases. Here are some scenarios where MongoDB is a good fit:

Flexible Schema: When your application's data model is evolving or contains varying attributes for different records, MongoDB's schema-less design allows you to store documents with different structures in the same collection.

Large Volumes of Unstructured Data: MongoDB excels when dealing with large amounts of unstructured or semi-structured data, such as social media posts, logs, user-generated content, and sensor data.

Dynamic Queries: If your application requires ad hoc querying with varying attributes and conditions, MongoDB's dynamic queries can accommodate these without needing to define complex joins or indexes.

Agile Development: In fast-paced development environments, where requirements change frequently, MongoDB's flexibility makes it easier to adapt to changing data structures without major schema alterations.

Scalability: MongoDB's sharding capability allows for horizontal scaling, distributing data across multiple servers or clusters to handle large amounts of data and high read/write workloads.

Real-Time Analytics: When dealing with real-time analytics or event tracking, MongoDB's ability to quickly ingest and process data can be advantageous.

Prototyping and Startups: For new projects or startups with limited resources and uncertain requirements, MongoDB can speed up development by allowing iterations without strict schema definitions.

However, there are scenarios where traditional SQL databases might be more appropriate, such as when data relationships are well-defined, transactions are critical, and complex joins are necessary. In summary, MongoDB is preferred over SQL databases in scenarios involving evolving data structures, unstructured data, flexible querying, and the need for horizontal scalability.Q2. State and Explain the features of MongoDB.MongoDB is a popular NoSQL database management system that offers a range of features designed to meet the needs of modern applications. Here are some key features of MongoDB:

Schema-less Design:
MongoDB uses a flexible schema, which means that each document in a collection can have a different structure. This is particularly useful for applications that evolve over time or deal with heterogeneous data.

JSON-like Documents:
MongoDB stores data in a format similar to JSON (BSON), making it easy to work with for developers. Documents can contain nested arrays and subdocuments, allowing for rich and complex data structures.

High Performance:
MongoDB provides high-performance data storage and retrieval due to its efficient indexing, automatic sharding (partitioning data across multiple servers), and support for in-memory storage.

Scalability:
MongoDB is designed to scale horizontally, allowing you to distribute your data across multiple servers and clusters to handle growing workloads. This is particularly valuable for applications with high read/write demands.

Ad Hoc Queries:
MongoDB supports powerful ad hoc queries, allowing you to perform complex queries on your data without needing to predefine specific indexes or structures.

Indexing:
MongoDB supports various types of indexes, including compound indexes, geospatial indexes, and text indexes, which improve query performance and enable advanced querying capabilities.

Aggregation Framework:
MongoDB's Aggregation Framework provides powerful tools for performing data transformations, filtering, grouping, and computation, allowing you to process and analyze data within the database.

Full-text Search:
MongoDB includes a built-in text search feature that supports text indexing and searching across multiple fields for relevant documents.

Flexible Data Model:
The document-oriented nature of MongoDB makes it well-suited for handling diverse types of data, including structured, semi-structured, and unstructured data.

Automatic Failover:
MongoDB provides automatic failover and high availability through replica sets. If a primary node goes down, a secondary node can automatically take over as the new primary.

Ease of Use:
MongoDB's intuitive API and query language make it relatively easy to learn and use. Its JSON-like documents also simplify the data mapping process for developers.

Cross-Platform Compatibility:
MongoDB supports multiple platforms and programming languages, making it versatile for building applications across different technologies.

Community and Enterprise Editions:
MongoDB offers both a free and open-source Community Edition and a paid Enterprise Edition with additional features, support, and security options.

Security Features:
MongoDB provides features like access control, authentication, encryption, and auditing to help secure your data and comply with regulatory requirements.

Backup and Restore:
MongoDB supports backup and restore mechanisms to ensure data reliability and recovery in case of data loss or disasters.

In summary, MongoDB's features cater to the demands of modern applications, offering flexibility, scalability, high performance, and ease of use while supporting various types of data and use cases.Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.To connect MongoDB to Python, you can use the pymongo library, which provides a Python driver for MongoDB. Here's how you can connect to MongoDB, create a database, and create a collection using Python:

Install the pymongo library (if you haven't already) using the following command:

pip install pymongo
Create a Python script with the following code to connect to MongoDB, create a database, and create a collection:
from pymongo import MongoClient

# Connect to the MongoDB server (default host and port)
client = MongoClient("mongodb://localhost:27017/")

# Access or create a database named "mydatabase"
db = client.mydatabase

# Create a collection named "mycollection" in the "mydatabase" database
collection = db.mycollection

print("Connected to MongoDB")
Replace "mongodb://localhost:27017/" with the appropriate connection string if your MongoDB server is running on a different host or port.

Save the script with a .py extension (e.g., mongodb_connection.py), and then run it using a Python interpreter. Make sure your MongoDB server is running before you execute the script.

When you run the script, it will:

Connect to the MongoDB server.
Access or create a database named "mydatabase".
Create a collection named "mycollection" within the "mydatabase" database.
Print "Connected to MongoDB" to indicate that the connection and database/collection creation were successful.
After running the script, you'll have a MongoDB database named "mydatabase" with a collection named "mycollection" ready to be used for data storage and retrieval.Q4. Using the database and the collection created in question number 3, write a code to insert one record,
and insert many records. Use the find() and find_one() methods to print the inserted record.Certainly! Based on the context of your previous question, let's assume we have a MongoDB database named "mydatabase" and a collection named "mycollection". Here's how you can insert records using the insert_one() and insert_many() methods, and then retrieve and print the inserted records using the find() and find_one() methods:
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the "mydatabase" database
db = client.mydatabase

# Access the "mycollection" collection
collection = db.mycollection

# Insert one record
record1 = {"name": "Alice", "age": 25, "city": "New York"}
inserted_record1 = collection.insert_one(record1)
print("Inserted ID (One record):", inserted_record1.inserted_id)

# Insert many records
records_to_insert = [
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"},
    {"name": "David", "age": 22, "city": "Houston"}
]
inserted_records = collection.insert_many(records_to_insert)
print("Inserted IDs (Many records):", inserted_records.inserted_ids)

# Find and print the inserted records
print("\nInserted Record (find_one()):")
inserted_record = collection.find_one({"name": "Alice"})
print(inserted_record)

print("\nInserted Records (find()):")
all_inserted_records = collection.find()
for record in all_inserted_records:
    print(record)
In this example:

We establish a connection to the MongoDB server and access the "mydatabase" database and the "mycollection" collection.
We use the insert_one() method to insert a single record into the collection and print the inserted ID.
We use the insert_many() method to insert multiple records into the collection and print the inserted IDs.
We use the find_one() method to retrieve and print the first inserted record that matches the specified query.
We use the find() method to retrieve and print all inserted records in the collection.
Please make sure you have the pymongo library installed in your Python environment to execute this code.Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to
demonstrate this.n MongoDB, the find() method is used to query a collection and retrieve documents that match a specified set of criteria. This method allows you to retrieve documents based on filters, projections, and other query options. Here's how you can use the find() method:
Syntax:
db.collection.find(query, projection);
collection: The name of the collection you want to query.
query: An optional document that specifies the criteria for selecting documents. It acts as a filter.
projection: An optional document that specifies which fields to include or exclude from the returned documents.
Here's a simple example to demonstrate how to use the find() method in MongoDB:

Suppose we have a collection named "students" with documents representing students' information, and each document has fields "name", "age", and "grade". We want to retrieve the names of students who are older than 18 and are in grade 12.
// Sample data in the "students" collection
db.students.insertMany([
  { name: "Alice", age: 17, grade: 11 },
  { name: "Bob", age: 19, grade: 12 },
  { name: "Charlie", age: 20, grade: 12 },
  { name: "David", age: 16, grade: 10 }
]);

// Query using the find() method
const query = { age: { $gt: 18 }, grade: 12 };
const projection = { _id: 0, name: 1 };

const result = db.students.find(query, projection);

// Print the results
result.forEach(student => {
  print(`Name: ${student.name}`);
});
In this example, we first insert sample data into the "students" collection. Then, we use the find() method to query the collection. The query parameter specifies the criteria for selecting documents: students who are older than 18 and are in grade 12. The projection parameter specifies that only the "name" field should be included in the returned documents. The output will display the names of students who meet the specified criteria.

Keep in mind that the find() method returns a cursor, which you can iterate through to access the retrieved documents.Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.In MongoDB, the sort() method is used to arrange the documents in a specified order within a result set. It allows you to retrieve documents from a collection in a specific order based on one or more fields. The sort() method takes one or more fields as arguments and specifies whether the sorting should be in ascending (default) or descending order.

Here's the basic syntax of the sort() method in MongoDB:
db.collection.find().sort({ field1: 1, field2: -1 })
collection: The name of the collection you're querying.
find(): The query operation used to retrieve documents from the collection.
sort(): The method used to specify the sorting criteria.
{ field1: 1, field2: -1 }: A document specifying the fields to sort by and the sorting order. In this example, field1 is sorted in ascending order (1), and field2 is sorted in descending order (-1).
Here's an example to demonstrate sorting in MongoDB:

Suppose we have a collection named "books" with documents representing books, and each document has fields "title", "author", and "published_year". We want to retrieve the books sorted by their published year in descending order, and for books with the same published year, we want to sort them alphabetically by the author's name
// Sample data in the "books" collection
db.books.insertMany([
  { title: "Book A", author: "Author X", published_year: 2020 },
  { title: "Book B", author: "Author Y", published_year: 2022 },
  { title: "Book C", author: "Author Z", published_year: 2021 },
  { title: "Book D", author: "Author Y", published_year: 2021 }
]);

// Query with sorting
const sortedBooks = db.books.find().sort({ published_year: -1, author: 1 });

// Display the sorted results
sortedBooks.forEach(book => {
  print(`Title: ${book.title}, Author: ${book.author}, Published Year: ${book.published_year}`);
});
In this example, the sort() method is used to first sort the documents based on the "published_year" field in descending order (-1). For documents with the same published year, they are then sorted by the "author" field in ascending order (1). The output will display the sorted books according to the specified criteria.Q7. Explain why delete_one(), delete_many(), and drop() is used.delete_one(), delete_many(), and drop() are methods commonly used in databases, especially with MongoDB, a popular NoSQL database. These methods are used for managing and manipulating data within a collection. Let's break down each method:

delete_one():
This method is used to delete a single document that matches a specified filter from a collection. In MongoDB, a document is analogous to a row in a relational database. The delete_one() method takes a filter as its argument, which specifies the criteria for matching the document to be deleted. If multiple documents match the filter, only the first matching document is deleted.
Example usage:
db.collection.delete_one({"field": "value"})
delete_many():
This method is used to delete multiple documents that match a specified filter from a collection. It works similarly to delete_one(), but it can delete multiple documents at once. This method is useful when you want to delete a subset of documents that meet certain criteria.
Example usage:
db.collection.delete_many({"field": "value"})
drop():
The drop() method is used to completely remove an entire collection from the database. It essentially deletes the entire structure, including all the documents and indexes within that collection. This method is typically used when you want to remove a collection entirely, and you're not concerned about preserving any of the data within it.

Example usage:
db.collection.drop()
In summary:

delete_one() and delete_many() are used to selectively remove documents from a collection based on a specified filter.
drop() is used to completely delete a collection from the database, including all of its documents and indexes.
It's important to use these methods carefully, especially drop(), as they can result in data loss that might be difficult to recover. Always make sure to have proper backups and confirm your actions before executing these methods, especially in production environments.
# #  <P style="color:GREEN"> Thank You ,That's All </p>
