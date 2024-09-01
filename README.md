<h1>Reddit Batch Pipeline using Airflow and Amazon Web Services</h1>


<h2>Description</h2>
In this project, I developed a data pipeline solution to extract, transform, and load (ETL) Reddit data into an Amazon Redshift data warehouse. By leveraging a combination of tools and services, including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift, the pipeline ensures efficient and scalable data processing.

The pipeline is designed to extract data from Reddit using its API, store the raw data in an S3 bucket through Airflow, transform the data using AWS Glue and Amazon Athena, and finally load the transformed data into Amazon Redshift for analytics and querying. This setup allows for seamless data ingestion, transformation, and analysis, making it an ideal solution for handling large-scale Reddit data.
<br />


<h2>Tools and Services</h2>

- <b>Python</b> 
- <b>Airflow</b>
- <b>Docker</b>
- <b>AWS Glue</b>
- <b>AWS S3</b>
- <b>AWS Athena</b>
- <b>AWS Redshift</b>

<h2>Project walk-through:</h2>

<h3>Pipeline Flow:</h3>
<br>
<img src="https://i.imgur.com/nLKI0ui.png" height="80%" width="80%" />
<br />

<h3>System Setup</h3> 

1. Clone the repository.
   ```bash
    git clone https://github.com/estrellajuca/reddit-data-engineering-project.git
   ```
2. Create a virtual environment.
   ```bash
    python3 -m venv venv
   ```
3. Activate the virtual environment.
   ```bash
    source venv/bin/activate
   ```
4. Install the dependencies.
   ```bash
    pip install -r requirements.txt
   ```
5. Rename the configuration file and the credentials to the file.
   ```bash
    mv config/config.conf.example config/config.conf
   ```
6. Starting the containers
   ```bash
    docker-compose up -d
   ```
7. Launch the Airflow web UI.
   ```bash
    open http://localhost:8080
   ```
<br>
<h3>Steps</h3>
<p align="center">
Create a docker image that will contain the airflow services <br/>
<br>

<img src="https://i.imgur.com/WtwLjFA.png" height="80%" width="80%" />
<br />
<br />
Create the Airflow dags and run them <br/>

<img src="https://i.imgur.com/dg0vBw7.png" height="80%" width="80%" />
<br />
<br />
Create the S3 bucket and its folders <br/>

<img src="https://i.imgur.com/w4e8kiu.png" height="80%" width="80%" />
<br />
<br />
Create an ETL job in Glue <br/>

<img src="https://i.imgur.com/siuDMRR.png" height="80%" width="80%" />
<br />
<br />
Create a crawler in Glue for the schema ceation <br/>

<img src="https://i.imgur.com/mtziRCn.png" height="80%" width="80%" />
<br />
<br />
Connect the database to Redshift and perfom some queries  <br/>

<img src="https://i.imgur.com/cRpboF7.png" height="80%" width="80%" />
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
