# Project Log Analysis

## Description
The project's main purpose is to extract newspaper site data from [Udacity SQL download file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
and analyze various tables in order to answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Setup
Prior to running a program, you need to install or setup the following items:
1. Install Python
2. Install VirturalBox
3. Install Vagrant
4. Clone [project-log-analysis repository](https://github.com/nvictor7/project-log-analysis.git), then place it inside vagrant directory
5. Download [SQL file of newspaper site](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) <br />
Unzip the file, then place it inside project-log-analysis folder

## Run Program
1. Open terminal, `cd` to project-log-analysis folder
2. Run `vagrant up` to start virtual machine
3. Run `vagrant ssh` to log on
4. Change current working directory to `cd /vagrant/project-log-analysis`
5. Load news paper site data in the terminal using `psql -d news -f newsdata.sql`
6. Create three views using PSQL view commands below
7. Exit PSQL mode using CONTROL + D keys
6. Last, run `python log-analysis.py`

#### PSQL View Commands
```
CREATE VIEW request_total AS
SELECT DATE(time) AS date, COUNT(*) AS num
FROM log
GROUP BY date
ORDER BY num DESC;
```

```
CREATE VIEW error_requests AS
SELECT DATE(time) AS date, COUNT(*) AS num
FROM log 
WHERE  status != '200 OK'
GROUP BY date
ORDER BY num DESC;
```

```
CREATE VIEW error_percentage AS
SELECT request_total.date,
((error_requests.num * 100.0) / request_total.num) AS error_perc
FROM request_total, error_requests
WHERE request_total.date = error_requests.date;
```

## Output
Once executing `python log-analysis.py`, here are the following output:
```MOST POPULAR THREE ARTICLES OF ALL TIME
1.Candidate is jerk, alleges rival - 338647 views
2.Bears love berries, alleges bear - 253801 views
3.Bad things gone, say good people - 170098 views

MOST POPULAR ARTICLE AUTHORS OF ALL TIME
1.Ursula La Multa - 507594 views
2.Rudolf von Treppenwitz - 423457 views
3.Anonymous Contributor - 170098 views
4.Markoff Chaney - 84557 views

DAYS HAVE MORE THAN 1% OF REQUESTS LEAD TO ERRORS
2016-07-17 - 2.26 % errors```
