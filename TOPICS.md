# Data Engineering Nanodegree Topics

## Topics for Course 1: Data Modeling
Introduction to Data Modeling:
- Data Modeling: Definition, Importance, Practitioners.
- Relational Databases: ACID, Table Creation, PostgreSQL, NoSQL, Apache Cassandra. 

Relational Data Models:
- Relational Databases: OLAP, OLTP, Normal Forms, Normalized Tables, Denormalization, Fact and Dimension Tables, Upsert.
- Data Models: Star Schemas, Snowflake Schemas.

NoSQL Data Models:
- Non-Relational Databases: Distributed Databases, CAP Theorem, Denormalization, CQL, Primary Key, Clustering Columns, WHERE Clause.

## Topics for Course 2: Cloud Data Warehouses
Introduction to Data Warehouses:
- Data Warehouses: Business Perspective, Operational/Analytics Processes, Technical Perspective, Dimensional Modeling, ETL, DWH Architecture, OLAP Cubes, DWH Storage Technology.

Introduction to Cloud Computing and AWS:
- Cloud Computing: Definition, Cloud Infrastructure Ecosystem.
- AWS: Computing (EC2), Storage (S3), Data Warehouse (Redshift), Private Cloud (VPC), Account Setup, IAM, Security Group, PostgreSQL RDS.

Implementing Data Warehouses on AWS:
- Data Warehouses: Scalable Storage, Ingesting at Scale, Infastructure as Code, ETL Strategies (SQL, Redshift, Parallel), Design (Distribution Style, Sorting Key, Table Design), Query Optimization.

## Topics for Course 3: Spark and Data Lakes
The Power of Spark:
- Introduction: Big Data, Four Key Hardware Components, Central Processing Unit: CPU, Memory: RAM, Storage: SSD/Magnetic Disk, Network: LAN/Internet.
- Big Data: Definition (Small, Medium, Big), Distributed Computing, Hadoop Ecosystem, MapReduce, Spark Cluster, Spark Use Cases.

Data Wrangling with Spark:
- Functional Programming: Definition, Purpose, Functional vs. Procedural Programming, Imperative vs. Declarative Programming, Maps and Lambda Functions.
- Data: Formats, Distributed Data Stores.
- Spark: Environment (SparkSession), Read/Write Data, Data Wrangling, APIs, RDDs.

Setting up Spark Clusters with AWS:
- Spark Clusters: Local vs. Standalone, AWS Spark Cluster, Spark UI, AWS CLI, EMR Cluster, Test Port Forwarding, Spark Scripts, Store/Retrieve Data, Read/Write to S3, HDFS vs. S3, Read/Write to HDFS.

Debugging and Optimization:
- Debugging: Difficulty, Code Errors, Data Errors, Accumulators, Spark Broadcast Variables.
- Optimization: Code Optimization, Data Skewness, Optimizing for Data Skewness, Insufficient Resources, Inefficient Queries.

Introduction to Data Lakes:
- Data Lakes: Purpose, Big Data Effects (Schema-on-Read, Advanced Analytics), Implementation, Data Lake vs. Data Warehouse, AWS Options (EMR: HDFS+Spark, EMR: S3+Spark, Athena: S3+Serverless), Issues.

## Topics for Course 4: Automatic Data Pipelines
Data Pipelines:
- Data Pipelines: Definition, Data Validation, DAGs, Apache Airflow (DAGs, Runtime Architecture, Run the Schedules, Operators and Tasks, Task Dependencies, Connections and Hooks, Context and Templating).

Data Quality:
- Data Quality: Data Lineage, Data Quality Requirements, Airflow (Data Lineage, Data Pipeline Schedules and Backfills, Updating DAGs, Data Partitioning).

Production Data Pipelines:
- Production Data Pipelines: Airflow (Operator Plugins, Hooks and Contrib, Task Boundaries, Refactoring a DAG, SubDAGs, Monitoring, Building a Full DAG, Building a Full Pipeline).

## Topics for Course 5: Capstone Project
Data Engineering Capstone Project:
- Scope Project, Gather Data, Explore and Assess Data, Define Data Model, Run ETL to Model the Data, Project Write-up.

## Technologies
General Tools and Libraries:
- NumPy (Array Computing Library)
- Pandas (Data Analysis Library)

Databases:
- PostgreSQL (Open Source Relational DBMS)
- Apache Cassandra (Open Source NoSQL DB)

Infastructure Tools:
- AWS EC2 (Cloud Computing Services: "Elastic Compute Cloud")
- AWS S3 (Cloud Storage Services: "Simple Storage Service")
- AWS Redshift (Cloud Data Warehouse Services)
- AWS EMR (Cloud Big Data Services: "Elastic MapReduce")
- Apache Spark (Open Source Big Data Analytics Framework)
- Apache Airflow (Open Source Workflow Management Platform)

Programming Languages:
- Python (Data Types, Operators, Data Structures, Control Flow, Functions, Scripting, Iterators, Generators)
- SQL (Basics, Joins, Aggregations, Subqueries, Temporary Tables, Data Cleaning, Window Functions, Advanced Joins, Performance Tuning)
- Unix Shell (Basic Commands, Directory Navigation, Parameters and Options, File Organization, Downloading Files, Viewing Files, Searching and Pipes, Shell/Environment Variables, Startup Files)