# Data Engineering Nanodegree

Instructors: 
- Amanda Moran, Ben Goldberg, Sameh El-Ansary, Olli Iivonen, David Drummond, Judit Lantos, and Juno Lee. 
- For biographical information, see [BIO.md][1]  

Offered By: [udacity.com][2]

## Introduction
This repo contains projects and exercises for the five-course Data Engineering Nanodegree program offered through Udacity. 

Feel free to use the material for reference purposes or if you get stuck. However, I would encourage you to try to complete all projects and exercises yourself, so that you can maximize your learning and enjoyment of the program.

## Udacity Description
#### About this Nanodegree
Data Engineering is the foundation for the new world of Big Data. This nanodegree will enable you to build production-ready data infrastructure, an essential skill for advancing your data career.

#### Overview
Learn to design data models, build data warehouses and data lakes, automate data pipelines, and work with massive datasets. At the end of the program, you’ll combine your new skills by completing a capstone project.

Students should have intermediate SQL and Python programming skills.

Educational Objectives: Students will learn to:
- Create user-friendly relational and NoSQL data models
- Create scalable and efficient data warehouses
- Work efficiently with massive datasets
- Build and interact with a cloud-based data lake
- Automate and monitor data pipelines
- Develop proficiency in Spark, Airflow, and AWS tools

## Topics Covered
**Course 1: Data Modeling:**  
- Data Modeling (What, Why, Who), Relational Databases (RMDBS, NoSQL, Normal Forms, Fact & Dimension Tables), Data Models (Star & Snowflake Schemas), Non-relational Databases.
- PostgreSQL, Apache Cassandra.

**Course 2: Cloud Data Warehouses:**  
- Data Warehouses (Operations, Technology, Dimensional Modeling, ETL, Architecture, OLAP Cubes), Cloud Computing (Definition, Ecosystem).
- AWS (EC2, S3, Redshift, VPC, IAM).

**Course 3: Spark and Data Lakes:**  
- Big Data (Hardware, Definition, Hadoop, MapReduce), Functional Programming, Data (Format, Distributed Storage), Data Lakes.
- Apache Spark (Environment, Data Wrangling, Debugging, Optimization), AWS EMR, AWS Spark Cluster.

**Course 4: Automatic Data Pipelines:**  
- Data Pipelines (Definition, Data Validation, DAGs), Data Quality (Data Lineage, Data Pipeline Schedules, Data Partitioning), Production Data Pipelines (SubDAGs, Monitoring).
- Apache Airflow.

**Course 5: Capstone Project:**  
- Scope Project, Gather Data, Explore and Assess Data, Define Data Model, Run ETL to Model the Data, Project Write-up.

For further information on topics and technologies covered, see [TOPICS.md][3].

## Syllabus

### Course 1: Data Modeling
In this course, you’ll learn to create relational and NoSQL data models to fit the diverse needs of data consumers. You’ll understand the differences between different data models, and how to choose the appropriate data model for a given situation. You’ll also build fluency in PostgreSQL and Apache Cassandra.

**Lesson 1: Introduction to Data Modeling.** 
- Outcomes:
  - Understand the purpose of data modeling
  - Identify the strengths and weaknesses of different types of databases and data storage techniques
  - Create a table in Postgres and Apache Cassandra
- Exercises:
  - [1-creating-a-table-with-postgres][5]
  - [2-creating-a-table-with-cassandra][6]

**Lesson 2: Relational Data Models.** 
- Outcomes:
  - Understand when to use a relational database
  - Understand the difference between OLAP and OLTP databases
  - Create normalized data tables
  - Implement denormalized schemas (e.g. STAR, Snowflake)
- Exercises:
  - [1-creating-normalized-tables][7]
  - [2-creating-denormalized-tables][8]
  - [3-creating-fact-and-dimension-tables-with-star-schema][9] 

**Lesson 3: NoSQL Data Models.** 
- Outcomes:
  - Understand when to use NoSQL databases and how they differ from relational databases
  - Select the appropriate primary key and clustering columns for a given use case
  - Create a NoSQL database in Apache Cassandra
- Exercises:
  - [1-three-queries-three-tables][10]
  - [2-primary-key][11]
  - [3-clustering-column][12] 
  
**Course Project: Data Modeling with Postgres.**
- In this project, you’ll model user activity data for a music streaming app called Sparkify. You’ll create a relational database and ETL pipeline designed to optimize queries for understanding what songs users are listening to. In PostgreSQL you will also define Fact and Dimension tables and insert data into your new tables.
- Project Solution: [Data Modeling with Postgress][39]

**Course Project: Data Modeling with Apache Cassandra.**
- In these projects, you’ll model user activity data for a music streaming app called Sparkify. You’ll create a database and ETL pipeline, in both Postgres and Apache Cassandra, designed to optimize queries for understanding what songs users are listening to. For PostgreSQL, you will also define Fact and Dimension tables and insert data into your new tables. For Apache Cassandra, you will model your data so you can run specific queries provided by the analytics team at Sparkify.
- Project Solution: [Data Modeling with Apache Cassandra][40]

### Course 2: Cloud Data Warehouses
In this course, you’ll learn to create cloud-based data warehouses. You’ll sharpen your data warehousing skills, deepen your understanding of data infrastructure, and be introduced to data engineering on the cloud using Amazon Web Services (AWS).

**Lesson 1: Introduction to the Data Warehouses.** 
- Outcomes:
  - Understand Data Warehousing architecture
  - Run an ETL process to denormalize a database (3NF to Star) 
  - Create an OLAP cube from facts and dimensions
  - Compare columnar vs. row oriented approaches
- Exercises:
  - [1-schemas][13]
  - [2-OLAP-cube][14]
  - [3-columnar-vs-row-storage][15]

**Lesson 2: Introduction to the Cloud with AWS.** 
- Outcomes:
  - Understand cloud computing
  - Create an AWS account and understand their services 
  - Set up Amazon S3, IAM, VPC, EC2, RDS PostgreSQ

**Lesson 3: Implementing Data Warehouses on AWS.** 
- Outcomes:
  - Identify components of the Redshift architecture
  - Run ETL process to extract data from S3 into Redshift
  - Set up AWS infrastructure using Infrastructure as Code (IaC)
  - Design an optimized table by selecting the appropriate distribution style and sorting key
- Exercises:
  - [2-iac][16]
  - [3-parallel-ETL][17]
  - [4-table-design][18]
  
**Course Project: Build a Cloud Data Warehouse.**
- In this project, you are tasked with building an ELT pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.
- Project Solution: [Build a Cloud Data Warehouse][41]

### Course 3: Spark and Data Lakes
In this course, you will learn more about the big data ecosystem and how to use Spark to work with massive datasets. You’ll also learn about how to store big data in a data lake and query it with Spark.

**Lesson 1: The Power of Spark.** 
- Outcomes:
  - Understand the big data ecosystem
  - Understand when to use Spark and when not to use it

**Lesson 2: Data Wrangling with Spark.** 
- Outcomes:
  - Manipulate data with SparkSQL and Spark Dataframes 
  - Use Spark for ETL purposes
- Exercises:
  - [1-procedural-vs-functional-in-python][19]
  - [2-spark-maps-and-lazy-evaluation][20]
  - [3-data-inputs-and-outputs][21]
  - [4-data-wrangling][22]
  - [6-dataframe-quiz][23]
  - [7-data-wrangling-sql][24]
  - [9-spark-sql-quiz][25]

**Lesson 3: Debugging and Optimization.** 
- Outcomes:
  - Troubleshoot common errors and optimize their code using the Spark WebUI

**Lesson 4: Introduction to Data Lakes.** 
- Outcomes:
  - Understand the purpose and evolution of data lakes
  - Implement data lakes on Amazon S3, EMR, Athena, and Amazon Glue
  - Use Spark to run ELT processes and analytics on data of diverse sources, structures, and vintages
  - Understand the components and issues of data lakes
- Exercises:
  - [1-schema-on-read][26]
  - [2-advanced-analytics-NLP][27]
  - [3-data-lake-on-S3][28]

**Course Project: Build a Data Lake.**
- In this project, you’ll build an ETL pipeline for a data lake. The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in the app. You will load data from S3, process the data into analytics tables using Spark, and load them back into S3. You’ll deploy this Spark process on a cluster using AWS.
- Project Solution: [Build a Data Lake][42]

### Course 4: Automatic Data Pipelines
In this course, you’ll learn to schedule, automate, and monitor data pipelines using Apache Airflow. You’ll learn to run data quality checks, track data lineage, and work with data pipelines in production.

**Lesson 1: Data Pipelines.** 
- Outcomes:
  - Create data pipelines with Apache Airflow 
  - Set up task dependencies
  - Create data connections using hooks
- Exercises:
  - [1-airflow-DAGs][29]
  - [2-run-the-schedules][30]
  - [3-task-dependencies][31]
  - [4-connections-and-hooks][32]
  - [5-context-and-templating][33]
  - [6-build-the-S3-to-redshift-DAG][34]  
  
**Lesson 2: Data Quality.** 
- Outcomes:
  - Track data lineage
  - Set up data pipeline schedules
  - Partition data to optimize pipelines 
  - Write tests to ensure data quality
  - Backfill data
- Exercises:
  - [1-data-lineage-in-airflow][35]
  - [2-schedules-and-backfills-in-airflow][36]
  - [3-data-partitioning][37]
  - [4-data-quality][38]

**Lesson 3: Production Data Pipelines.** 
- Outcomes:
  - Build reusable and maintainable pipelines 
  - Build your own Apache Airflow plugins
  - Implement subDAGs
  - Set up task boundaries
  - Monitor data pipelines
  
**Course Project: Data Pipelines with Airflow.**
- In this project, you’ll continue your work on the music streaming company’s data infrastructure by creating and automating a set of data pipelines. You’ll configure and schedule data pipelines with Airflow and monitor and debug production pipelines.
- Project Solution: [Data Pipelines with Airflow][43]

### Course 5: Capstone Project
Combine what you’ve learned throughout the program to build your own data engineering portfolio project.

**Course Project: Data Engineering Capstone.**
- The purpose of the data engineering capstone project is to give you a chance to combine what you’ve learned throughout the program. This project will be an important part of your portfolio that will help you achieve your data engineering-related career goals.
- In this project, you’ll define the scope of the project and the data you’ll be working with. We’ll provide guidelines, suggestions, tips, and resources to help you be successful, but your project will be unique to you. You’ll gather data from several different data sources; transform, combine, and summarize it; and create a clean database for others to analyze.
- Project Solution: [Data Engineering Capstone][44]

## License
This project is licensed under the MIT License. See [LICENSE][4] for details.

## Milestones
- 2020-11-16: Completed 5-course Nanodegree program.

[//]: # (Links Section)
[1]:https://github.com/robstraker/data-engineering-nanodegree-udacity/blob/master/BIO.md
[2]:https://www.udacity.com
[3]:https://github.com/robstraker/data-engineering-nanodegree-udacity/blob/master/TOPICS.md
[4]:https://github.com/robstraker/data-engineering-nanodegree-udacity/blob/master/LICENSE

[//]: # (Links to Exercise Solutions)
[5]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-1-exercises/1-creating-a-table-with-postgres.ipynb
[6]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-1-exercises/2-creating-a-table-with-cassandra.ipynb
[7]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-2-exercises/1-creating-normalized-tables.ipynb
[8]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-2-exercises/2-creating-denormalized-tables.ipynb
[9]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-2-exercises/3-creating-fact-and-dimension-tables-with-star-schema.ipynb
[10]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-3-exercises/1-three-queries-three-tables.ipynb
[11]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-3-exercises/2-primary-key.ipynb
[12]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/lesson-3-exercises/3-clustering-column.ipynb
[13]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/lesson-1-exercises/1-schemas.ipynb
[14]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/lesson-1-exercises/2-OLAP-cubes.ipynb
[15]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/lesson-1-exercises/3-columnar-vs-row-storage.ipynb
[16]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/lesson-3-exercises/2-iac.ipynb
[17]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/lesson-3-exercises/3-parallel-ETL.ipynb
[18]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/lesson-3-exercises/4-table-design.ipynb
[19]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/1-procedural-vs-functional-in-python.ipynb
[20]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/2-spark-maps-and-lazy-evaluation.ipynb
[21]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/3-data-inputs-and-outputs.ipynb
[22]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/4-data-wrangling.ipynb
[23]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/6-dataframe-quiz-solution.ipynb
[24]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/7-data-wrangling-sql.ipynb
[25]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-2-exercises/9-spark-sql-quiz-solution.ipynb
[26]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-4-exercises/1-schema-on-read.ipynb
[27]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-4-exercises/2-advanced-analytics-NLP.ipynb
[28]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/lesson-4-exercises/3-data-lake-on-S3.ipynb
[29]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-1-exercises/1-airflow-DAGs.py
[30]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-1-exercises/2-run-the-schedules.py
[31]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-1-exercises/3-task-dependencies.py
[32]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-1-exercises/4-connections-and-hooks.py
[33]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-1-exercises/5-context-and-templating.py
[34]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-1-exercises/6-build-the-S3-to-redshift-DAG.py
[35]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-2-exercises/1-data-lineage-in-airflow.py
[36]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-2-exercises/2-schedules-and-backfills-in-airflow.py
[37]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-2-exercises/3-data-partitioning.py
[38]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/lesson-2-exercises/4-data-quality.py

[//]: # (Links to Project Solutions)
[39]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/project-data-modeling-with-postgres
[40]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-1-data-modeling/project-data-modeling-with-apache-cassandra
[41]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-2-cloud-data-warehouses/project-build-a-cloud-data-warehouse
[42]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-3-spark-and-data-lakes/project-build-a-data-lake
[43]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-4-automatic-data-pipelines/project-data-pipelines-with-airflow
[44]:https://github.com/robstraker/data-engineering-nanodegree-udacity/tree/master/course-5-capstone-project/project-data-engineering-capstone