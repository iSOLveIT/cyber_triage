.. _UPGRADE:

Upgrading from v2 to v3
=======================

Version 3 of |cyTriage| introduced a new backend database type and schema. 
This is a backward incompatible change and this section outlines how to make the upgrade and what is retained.

Here are some key concepts:

* You will not be able to access data in |cyTriage| 3 (v3) that was created in |cyTriage| 2 (v2). 
* No v2 data is deleted, it is just not in the v3 database. 
* You can install v3 alongside v2, but only one version can be run at a time. This will allow you to access old data. 
* Your basic configuration settings from v2 will be used by v3. 
* The collection tool schema changed. The |cyTriage| v3 UI cannot import v2 collection tool data. 
    
Standard
--------

If you have |cyTriage| Standard, then you can simply install |cyTriage| 3 and start using it with no other configuration changes. 

Team
----

You have a couple of decisions to make when using the new Team version:

1. Retaining Access to v2 Data: If you want clients to be able to access older data, then you should get a new host for the v3 |cyTriage| Server. If you do not need access, then you can stop the v2 |cyTriage| Server and start v3 instead.
2. Database Type: With v3, you have a choice of SQLite or PostgreSQL. Choosing between them is outlined in :ref:`Section 7.1 <CTEAM>`. 
 
For each client, you'll need to:

* Configure them to use the new **Server Password**.
* Change the server address if you have a new host for the v3 Server. 
