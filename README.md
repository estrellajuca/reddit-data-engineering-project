<h1>Reddit Batch Pipeline using Airflow and Amazon Web Services</h1>


<h2>Description</h2>
In this project, I developed a data pipeline solution to extract, transform, and load (ETL) Reddit data into an Amazon Redshift data warehouse. By leveraging a combination of tools and services, including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift, the pipeline ensures efficient and scalable data processing.

The pipeline is designed to extract data from Reddit using its API, store the raw data in an S3 bucket through Airflow, transform the data using AWS Glue and Amazon Athena, and finally load the transformed data into Amazon Redshift for analytics and querying. This setup allows for seamless data ingestion, transformation, and analysis, making it an ideal solution for handling large-scale Reddit data.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Airflow</b>
- <b>Docker</b>
- <b>AWS Glue</b>
- <b>AWS S3</b>
- <b>AWS Athena</b>
- <b>AWS Redshift</b>

<h2>Project walk-through:</h2>

<h3>Pipeline Flow:</h3>
<img src="https://i.imgur.com/nLKI0ui.png" height="80%" width="80%" />
<br />
<br />


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
