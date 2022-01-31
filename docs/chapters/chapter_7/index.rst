.. _CTEAM:

Configuring a Team Environment
==============================

This section outlines the installation and configuration of |cyTriage| Team, 
which is a client-server deployment with one server and one or more clients. 
Only one instance of |cyTriage| can run on a system at a time, so this means you will need at least two computers. 

Architecture
------------

There are three components of a |cyTriage| Team cluster:

* |cyTriage| Server: Where the processing and analysis occurs. This contains the REST API used by clients and other integrations. 
* |cyTriage| Clients: Runs on examiner systems and interacts with the |cyTriage| Server.
* Database: Where the collected data is stored. There are a few options for this:
   + SQLite databases on the same host as the |cyTriage| Server
   + PostgreSQL server running on the same host as the |cyTriage| Server
   + PostgreSQL server on its own dedicated host 

.. figure:: /_static/img/chapter_7/7_1.jpg
    :figclass: align-center
    :class: no-scaled-link

    |cyTriage| *Team cluster*

There are several factors to take into account when deciding where the database should reside:

* SQLite: This is the easiest to deploy (it is all embedded), but will be more limited with respect to performance when datasets get large. It is certainly sufficient for evaluation purposes though or small investigations. There is no data migration path from SQLite to PostgreSQL.  
* PostgreSQL on the same host as the |cyTriage| Server: This minimizes the number of hosts to maintain, but is not always optimal based on other applications and because PostgreSQL is faster on Linux. 
* PostgreSQL on its own host: This gives you flexibility to optimize the environment, but may not be needed for average case sizes. You can also use managed PostgreSQL services from cloud providers if you are running in the cloud.  The `Cyber Triage website <https://cybertriage.com>`_ has several blog posts about which services worked best. 
  
Testing PostgreSQL Speed
^^^^^^^^^^^^^^^^^^^^^^^^

When choosing between running PostgreSQL on its own server versus running alongside |cyTriage|, you can measure the PostgreSQL performance using **pgbench**.  
We have found this is much more reliable than focusing on hardware specs.  
We recommend that your PostgreSQL installation is able to get **at least 4250 transactions per second (TPS)**.

You can start by installing PostgreSQL on the same server as |cyTriage| (as outlined below). 
You can then use the following commands to measure the TPS.  
If they are too slow, then you can consider setting up a dedicated server. 

1. Setup the test by running the following. It will prompt you for the superuser password you entered during the installation.
    .. code-block:: powershell

        C:\Program Files\PostgreSQL\13\bin\pgbench -U postgres -i -s 50 postgres
    
2. Run the test: 
    .. code-block:: powershell

        C:\Program Files\PostgreSQL\13\bin\pgbench -U postgres -c 5 -j 2 -t 1000 postgres

.. note:: The final values may change in between runs, so you might want to run it a few times. 

Software Requirements
---------------------


* `Cyber Triage <https://www.cybertriage.com/download-eval/>`_ MSI installer.
* `PSExec 2.2 <https://download.sysinternals.com/files/PSTools.zip>`_ (or newer) if you want to push the collection tool to remote hosts over the network.
* Download `PostgreSQL 13 <https://www.postgresql.org/download/>`_ if you are going to use PostgreSQL instead of SQLite
  
Hardware Requirements
---------------------

* **Team Server**: 64-bit version of Windows Server 2012 or newer, 16GB+ of RAM, 4+ cores, and 250GB+ of free hard drive space.
* **Team Client**: 64-bit version of Windows 7 or newer, 8GB+ of RAM, 4+ cores, and 50GB+ of free hard drive space. 
* Optional Separate PostgreSQL Server: 16GB+ of RAM, 4+ cores, and 250GB+ of free hard drive space. Either Linux or Windows.
  
We recommend using SSD storage for best performance. 

Installing and Configuring PostgreSQL
-------------------------------------

If you are going to use PostgreSQL, then the following sections outline its installation and configuration on Windows. 

PostgreSQL Installation
^^^^^^^^^^^^^^^^^^^^^^^

PostgreSQL can be installed in a variety of ways, including with installers, package managers, or containers such as Docker. |br|
The easiest method for most |cyTriage| users will be to use a `PostgreSQL windows installer <https://www.postgresql.org/download/windows/>`_ and choose the default settings. 
You do not need to use StackBuilder if it prompts you to. |br|

.. note::

    * Data Folder: The default is inside of the PostgreSQL installation folder.
    * Superuser Password: You'll need this to configure the database.

At the end of the Windows installer process, PostgreSQL will be running as a service as the **Network Service** account.

If you wanted to test the PostgreSQL speed as outlined in `Section 7.1.1 <#testing-postgreSQL-speed>`_, you can do that now before doing further configuration. 

PostgreSQL Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

There are several settings that must be changed from the default installation. 
After you have made these changes, you should reboot the system for them to all take effect.

Create Database User
++++++++++++++++++++

A special user will need to be created for the |cyTriage| Server to access the database. We'll use the name ``cyber_triage``. 

1. From a Windows Command Prompt run:
  
    .. code-block:: powershell

       C:\Program Files\PostgreSQL\13\bin\psql -U postgres postgres
        
2. You will be prompted for the superuser password you entered during the installation.
   
3. You will next get a ``postgres=#`` prompt. To create the user enter the following code below and replace ``ChangeMeASAP`` with a real password. |br| Ensure you record the password because you will need to enter it into the |cyTriage| server.
   
    .. code-block:: SQL

       CREATE ROLE cyber_triage PASSWORD 'ChangeMeASAP' CREATEDB LOGIN;

4. Type ``\q`` to exit prompt.
   
Basic Configuration Changes
+++++++++++++++++++++++++++

There are several settings that we suggest making to improve performance and enable logging to make debugging problems easier. 

.. note:: 
  
  These are all oriented around a Windows installation and a Linux deployment have other settings that will make it more optimal.

Open the following file in a text editor:

.. code-block:: powershell

   C:\Program Files\PostgreSQL\13\data\postgresql.conf

The following settings should be changed or uncommented (by removing the leading ``#``):

* Edit the maximum number of connections:
    .. code-block:: text

        max_connections = 200 

* Increase the value of the buffer setting:
    .. code-block:: text

        shared_buffers = 512MB

* Enable huge_pages by uncommenting this line:
    .. code-block:: text

        huge_pages = try

* Uncomment the following performance-oriented lines and change the default values:
    .. code-block:: text

        temp_buffers = 80MB
        shared_memory_type = windows
        fsync = off
        synchronous_commit = off

* Uncomment and change the effective cache size based on the amount of RAM available. We recommend the value be 50% of the total RAM.
    
    .. code-block:: text

        effective_cache_size = 16GB 

* Uncomment the following log-oriented lines and change the default values:
    .. code-block:: text

        log_min_duration_statement = 300
        log_lock_waits = on

This file also allows you to restrict access to the database from other hosts. 

* If PostgreSQL is on the same host as the |cyTriage| server, then edit the ``listen_address`` line to the following:
    .. code-block:: text

        listen_addresses = 'localhost'

* If PostgreSQL is on a different host, then confirm that the line is:
    .. code-block:: text

        listen_addresses = '*'

Windows Service Settings
++++++++++++++++++++++++

If you are running PostgreSQL on a Windows system, we recommend that you also enable the **Lock Pages in Memory** setting for the Windows user that the service will be running as. 
By default, this is the Network Service account.

1. Open the **Local Group Policy Editor**
2. Navigate to **Local Computer Policy -> Windows Settings -> Security Settings -> Local Policies -> User Rights Assignment**
3. Select the **Local pages in memory** item and double click on it.
   
.. figure:: /_static/img/chapter_7/7_2.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Local Group Policy Editor*

4. Add the user that the PostgreSQL service will be running as (i.e. Network Service)

Dedicated PostgreSQL Server Changes
+++++++++++++++++++++++++++++++++++

If you are running PostgreSQL Server on a system different from the |cyTriage| server, you'll need to make an additional change.

Open the following in a text editor:

.. code-block:: powershell

    C:\Program Files\PostgreSQL\13\data\pg_hba.conf

Add a rule to the bottom similar to:

.. code-block:: text

    host all cyber_triage 10.10.10.10/32 scram-sha-256

Update the above rule based on:

* IP Address of the |cyTriage| Server
* The ``password_encryption`` value in the **postgresql.conf** file. 

Restart The Host
++++++++++++++++

After all the above configuration changes, restart the computer so that the service and database settings take effect. 

Configuring The Cyber Triage Server
-----------------------------------

The |cyTriage| server will need to be running whenever you want to use any of the |cyTriage| clients to create or open sessions. 
It will be receiving the network connections from the various collection tools and will be performing all of the automated analysis.

The installation steps for the server (and client) start the same way as the standard version, which are outlined in :ref:`Section 1.3 <SI>`. 
Namely, to launch the ``.msi`` installer and choose the default options. 

When prompted for a license, choose the license file that you received that has **_server** in the name. 

When |cyTriage| is open:

1. Open the Options panel and choose the **Deployment Mode** tab. Change the mode to **Team - Server**. If you do not have this option, then you did not supply a Team license key.

.. figure:: /_static/img/chapter_7/7_3.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Options (Deployment Mode Tab)*

2. In the **Server Password** section, press the **Change Password** button and pick a password that clients will use to connect to the server. You will need the new password when you configure each client, so write it down somewhere safe or make sure you remember it. 
   
3. In the **Database Setting** section, either keep it as SQLite or enter in the PostgreSQL information by pressing the **View Database Settings** button. Use ``localhost`` as the host if you are running the server on the same system as the server.

.. figure:: /_static/img/chapter_7/7_4.jpg
    :figclass: align-center
    :class: no-scaled-link

    *PostgreSQL Database Settings*

4. Press OK and it will restart |cyTriage|. 
5. When it restarts, your host firewall software may ask permission to open ports. These are required for the server to operate. 
6. After it restarts, the |cyTriage| interface will only allow you to go to the options panel or extract the collection tool. You cannot create or open sessions directly on the server. 

Configuring the Cyber Triage Clients
------------------------------------

|cyTriage| clients can be installed on any analysis system. 
The responder will use the client to create and open sessions. 

To configure each |cyTriage| client:

1. Install |cyTriage| using the same MSI as you used for the Server.
2. Supply the same appropriate client license key.
3. Open the Options panel using the button in the upper right and choose the **Deployment Mode** tab.
4. Choose **Team - Client**. 
    .. figure:: /_static/img/chapter_7/7_5.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Options (Deployment Mode Tab)*

5. Enter the hostname or IP address of the server and the Server Password that you configured on the Server. Press the **Test Connection** button to ensure that the client can connect to the Server. 
6. Press OK and |cyTriage| will restart. 


Team General Information
------------------------

This section outlines general information for using |cyTriage| Team:

* Any client can open any session, even if it did not create the session.
* Some functionality is currently more limited in a client-server deployment, such as the ability to cancel collections and malware analysis. 


Team REST API SSL Certificate
-----------------------------

The Team Server will have a REST API on **port 9443** that you can use to integrate |cyTriage| with your SIEM or orchestration system. 
By default, it will use a self-signed certificate, but you can also use your own instead. 

Send an email to `support@cybertriage.com <mailto:support@cybertriage.com>`_ for instructions. 

Configuring the Server to Run as a Service
------------------------------------------

You can also run the Team Server as a Windows service, which ensures that it runs when the computer starts and does not require a user to be always logged in. 

Limitations
^^^^^^^^^^^

* You need to run the service as a user account because the user must login to configure the Server. 
* To make changes to the Server, you will need to stop the service, launch |cyTriage| as a user to make changes via the Options panel, close |cyTriage|, and then start the service back up again. 

Installation Instructions 
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Stop any existing |cyTriage| services by opening a command prompt (with Admin priveledges) and running:
    .. code-block:: powershell
    
        <Previous_CT_Location>\cybertriage\service\svcmgr.bat uninstall

2. Install and configure the Server using the steps outlined in `Section 7.5 <#configuring-the-cyber-triage-server>`_. Also configure settings such as NSRL and Yara. 
   
3. After the server is configured, close the application. Ensure that you do the configuration while logged in under the account that the service will run as. Otherwise, the configuration settings will not be available to the service. 
   
4. In a Admin command prompt, change to the new |cyTriage| folder
    .. code-block:: powershell
    
        cd C:\Program Files\Cyber Triage-3.0.0\cybertriage\service

5. Install the service by running: 
    .. code-block:: powershell
    
        svcmgr.bat install

6. Launch the |cyTriage| Service Manager from the command prompt by typing:
    .. code-block:: powershell
    
        CyberTriageServicew.exe

7. Go to the Logon screen to change the user account that the service should run as. This should be the same user account that was used to configure |cyTriage|. 
    .. figure:: /_static/img/chapter_7/7_6.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Team Server Log On Screen*

8. Press Apply.
9. Either restart the server so that the service starts or press **Start** on the General Tab. 

Verifying The Service
^^^^^^^^^^^^^^^^^^^^^

You can get basic status of the service by pointing a web browser at: https://SERVER_HOST_NAME:9443/api/admin/service-status 

Making Changes to Service
^^^^^^^^^^^^^^^^^^^^^^^^^

To make configuration changes, you will need to stop the service, launch |cyTriage|, make your changes, close the application, and then start the service again. 

Changing Team Port Numbers
--------------------------

It is possible, but not typical, to change the port numbers used by various services within |cyTriage| Team.  
Namely, the ports used by the REST API and Active MQ (which is used to broadcast events). 

* Open up ``%appdata%\cybertriage\config\config.yml`` on the |cyTriage| Server machine
* Edit the port number for **restApiPort** or **activeMQPort** and save the file
* Follow the same process to update the port on each of the |cyTriage| client machines. 

