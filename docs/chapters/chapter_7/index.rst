.. _CTEAM:

Configuring a Team Environment
==============================

Architecture
------------

Testing PostgreSQL Speed
^^^^^^^^^^^^^^^^^^^^^^^^

Software Requirements
---------------------

Hardware Requirements
---------------------

Installing and Configuring PostgreSQL
-------------------------------------

If you are going to use PostgreSQL, then the following sections outline its installation and configuration on Windows. 

PostgreSQL Installation
^^^^^^^^^^^^^^^^^^^^^^^

PostgreSQL can be installed in a variety of ways, including with installers, package managers, or containers such as Docker. |br|
The easiest method for most |cyTriage| users will be to use a `PostgreSQL windows installer <https://www.postgresql.org/download/windows/>`_ and choose the default settings. 
You do not need to use StackBuilder if it prompts you to. |br|

Take note of:

* Data Folder: The default is inside of the PostgreSQL installation folder.
* Superuser Password: You'll need this to configure the database.

At the end of the Windows installer process, PostgreSQL will be running as a service as the **Network Service** account.

If you wanted to test the PostgreSQL speed as outlined in `Testing PostgreSQL Speed`_, you can do that now before doing further configuration. 

PostgreSQL Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

There are several settings that must be changed from the default installation. 
After you have made these changes, you should reboot the system for them to all take effect.

Create Database User
++++++++++++++++++++

A special user will need to be created for the |cyTriage| Server to access the database. We'll use the name ``cyber_triage``. 

1. From a Windows Command Prompt run:
   
    .. code-block:: powershell

       "C:\Program Files\PostgreSQL\13\bin\psql" -U postgres postgres
        
2. You will be prompted for the superuser password you entered during the installation.
   
3. You will next get a ``postgres=#`` prompt. To create the user enter the following code below and replace ``ChangeMeASAP`` with a real password. |br| Ensure you record the password because you will need to enter it into the |cyTriage| server.
   
    .. code-block:: SQL

      CREATE ROLE cyber_triage PASSWORD 'ChangeMeASAP' CREATEDB LOGIN;

4. Type ``\q`` to exit prompt.
   
    
