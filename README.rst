processlog - Process Logging in Redshift with python
===================================================

| 1.Overview_
| 2.Installation_
| 3.Usages-Guidelines_
| 4.Examples_
| 5.Support_
| 6.References_ 

1.Overview
==========
**processlog** is prepared to capture logs of Python's ETL tasks in Redshift Processlog table.

processlog is purley implemented in Python.

2.Installation
==============
| **To install the library, use below command**
|    $ pip install processlog

.. note::

    During the installation of package please verify that all the required dependencies installed successfully, if not try to install them one by one.

3.Usages-Guidelines
===================
| This python library need a configured input file which will include list of datasource details.File should be in below format:-

 +---------+-------------+------------+--------+------------+------------+------------------+-------------+-----------------+
 |**conid**|**host**     |**dbname**  |**port**|**username**|**password**|**datasourcetype**|**conString**|**PythonLibrary**|
 +---------+-------------+------------+--------+------------+------------+------------------+-------------+-----------------+
 |1        |127.0.0.1    |employee    |5433    |livexyz     |live@123    |Redshift          |NA           |psycopg2         |
 +---------+-------------+------------+--------+------------+------------+------------------+-------------+-----------------+

| Once file is prepared with all available datasource connection details, follow the below steps to get connect to respective datasource and insert into processlog.

| **Step 1:** Load  connection details *.csv* file into pandas dataframe             
|             >> import processlog

| **Step 2:** Pass query with respective Parameters
|             >> file='D:/python/datasource.csv'
|                connid=1
|                table='development.processlog_karan'
|                logtimestamp='2019-01-01' (with or without timestamp)
|                etl_runid=-1
|                loglevel=1
|                processname='test'
|                processstage='test'
|                processsubstage='test'
|                logmessage='insert'
|                recordcount=100
|                logerror='test'
|             >> processlog.logging(file,connid,table,logtimestamp,etl_runid,loglevel,processname,processstage,processsubstage,logmessage,recordcount,logerror)

.. note::

    01. Use the same header name which is provided in sample file format for more help a user can use **p.config_df_sample()** command to see structure of sample configuration file format.
    

4.Examples
==========
| *Package Used:*
| Eg. processlog.logging(file,connid,table,logtimestamp,etl_runid,loglevel,processname,processstage,processsubstage,logmessage,recordcount,logerror)




5.Support
==========
 +--------------------+------------------------------------+
 |**Operating System**|Linux/OSX/Windows                   |
 +--------------------+------------------------------------+
 |**Python Version**  |2/2.7/3/3.2/3.3/3.4/3.5/3.7 etc.    |
 +--------------------+------------------------------------+ 


7.References
============
| Many thanks to the developers of dependent packages. Please use the below links to get deeper knowledge about required packages:-

| **PSYCOPG2:** https://pypi.org/project/psycopg2/
| **DBCONNECT:** https://pypi.org/project/dsconnect/
