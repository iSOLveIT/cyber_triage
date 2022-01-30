.. _ASD:

Analyzing The Session Data
==========================

<<<<<<< HEAD
Once you have added data to |cyTriage| from one of the collection methods previously listed, then analysis begins.  
Your goal during this process is to review the data to make a conclusion about if the system is compromised and how badly.  
|cyTriage| will help you as much as possible.
=======
Once you have added data to Cyber Triage from one of the collection methods previously listed, then analysis begins.  
Your goal during this process is to review the data to make a conclusion about if the system is compromised and how badly.  
Cyber Triage will help you as much as possible.
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

Threat Scores
-------------

<<<<<<< HEAD
As data comes in from the remote host, file, or disk image, |cyTriage| will start to analyze it and assign a score: 

* **Bad**: The item is believed to be bad because several malware scanners thought so, it is on a bad list, the user manually identified it, or some other low false positive-based approach.
* **Suspicious**: The item has characteristics that make it anomalous or similar to what is seen during an attack. The approaches used to identify these items have false positives and |cyTriage| is going to need you to make the final decision.
=======
As data comes in from the remote host, file, or disk image, Cyber Triage will start to analyze it and assign a score: 

* **Bad**: The item is believed to be bad because several malware scanners thought so, it is on a bad list, the user manually identified it, or some other low false positive-based approach.
* **Suspicious**: The item has characteristics that make it anomalous or similar to what is seen during an attack. The approaches used to identify these items have false positives and Cyber Triage is going to need you to make the final decision.
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
* **Good**: The item was part of a hash database of known items, part of a Good List, or the user manually identified it as good. This score is for items that are OK and not associated with an attack. 
* **Unknown**: No score was assigned to the item. 
  
Your main responsibility is to confirm the **Bad** items and decide on the **Suspicious** items. 
You can also review the other items.

Interface Overview and Workflow
-------------------------------

<<<<<<< HEAD
When |cyTriage| starts, you'll see the Dashboard that displays the number of Bad and Suspicious items, 
=======
When Cyber Triage starts, you'll see the Dashboard that displays the number of Bad and Suspicious items, 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
the number of background tasks, and other general session information. 

.. figure:: /_static/img/chapter_3/3_1.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Dashboard Interface*

As you can see from the interface, there are three sections: 

* The left-hand side menu allows you to navigate between the dashboard and the various data types that were collected. 
* The middle part displays the selected data type
* The right-hand side displays a timeline of the items that have a Bad score. 
  
The middle section for non-dashboard selections has a table on top and a set of tabs on the bottom. 
The table shows the items of the selected data type and the bottom shows details that are related to a selected item. 

.. figure:: /_static/img/chapter_3/3_2.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Bad Items*

As you navigate around the UI investigating the endpoint, you can use the arrows in the upper left to go back in your history. 
This is useful when you see something suspicious, click around to investigate it, and then want to go back to your original place to continue your review. 

.. figure:: /_static/img/chapter_3/3_3.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Backward and Forward Arrows*

Marking an Item as Good, Bad, or Suspicious
-------------------------------------------

When you select an item in the table, you can choose to change its score in the area below. 

.. figure:: /_static/img/chapter_3/3_4.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Change Score*

* Bad: Use this score if you know the item is related to an incident and want it to be reported on.
* Suspicious: Use this score if you want to make sure you review it again in the future. This can be used as a bookmark for your workflow.
<<<<<<< HEAD
* Good: Use this score if |cyTriage| marked and item as Good or Suspicious and you want to override that score because you know it is not related to an incident. 
=======
* Good: Use this score if Cyber Triage marked and item as Good or Suspicious and you want to override that score because you know it is not related to an incident. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
  
If the item is initially Suspicious, you can change the score to Bad if it is in fact bad or mark it as Good if it was a false positive. 
Changing a Suspicious item to Good or Bad will decrease the number of suspicious items listed on the dashboard and the counters on the left-hand menu. 

You can use the **Add Comment** button to store a comment for the file. 
This will get included in the final report and be visible to future investigations that come across the same item.   

Keyboard Shortcuts
^^^^^^^^^^^^^^^^^^

If you would rather not use the mouse and prefer keyboard shortcuts, you can also apply scores as follows: 

.. table::
   :align: center
   :width: 100%
   :class: align-center
   :widths: auto

   +----------------------------------------------+--------------------------------------------+
   | .. centered:: Keyboard Shortcuts                                                          |
   +==============================================+============================================+
   | **Keys**                                     | **Meaning**                                |
   +----------------------------------------------+--------------------------------------------+
   | SHIFT + B                                    | Bad                                        |
   +----------------------------------------------+--------------------------------------------+  
   | SHIFT + S                                    | Suspicious                                 |
   +----------------------------------------------+--------------------------------------------+   
   | SHIFT + G                                    | Good                                       |
   +----------------------------------------------+--------------------------------------------+   
   | SHIFT + U                                    | Unknown                                    |
   +----------------------------------------------+--------------------------------------------+   
   | SHIFT + C                                    | Add Comment                                |
   +----------------------------------------------+--------------------------------------------+  
   | CTRL + Z                                     | Undo                                       |
   +----------------------------------------------+--------------------------------------------+


Marking Related Items as Suspicious
-----------------------------------

<<<<<<< HEAD
When you change the score of an item to Bad or Suspicious, |cyTriage| will identify other items that are related and allow you to mark any as suspicious. 
=======
When you change the score of an item to Bad or Suspicious, Cyber Triage will identify other items that are related and allow you to mark any as suspicious. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
The idea is that you may find these other items interesting and you should follow up on them.  
You will get a dialog such as this:

.. figure:: /_static/img/chapter_3/3_5.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Recommended Threats*

In this example, we marked an active connection as **Bad** and it recommended that we also mark the process, file, and user as Suspicious. 
You can also choose to directly mark an item as Bad. 

Viewing Bad Items
-----------------

Items with a **Bad** score are found in the **Bad Items** menu, as shown in the previous section. 
These items were found from automated analysis or manually identified as bad. 
The rows in this table are grouped (typically by path) and have columns for: 

* **Type**: What type of item was found to be a threat. 
* **Description**: High level description of the item
* **Malware**: Indicates if an executable has been scanned by the external analysis service.
* **New**: threats seen for the first time on this host have an asterisk icon.
* **Seen Before**: List of other hosts that contain this threat item in the Incident or among all hosts in the database. 
  
**What Should You Do**: You should review the data here and confirm that it is indeed bad in your environment.
A program that gets flagged as malicious could be normal in your environment. 
If it is, mark it as **Good** and consider adding it to a Global Good List. 

Analysis Techniques
-------------------

<<<<<<< HEAD
There are a variety of analysis techniques that |cyTriage| uses to identify suspicious data. 
=======
There are a variety of analysis techniques that Cyber Triage uses to identify suspicious data. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
This section outlines some that you may encounter the most. These are not used in the free Lite mode. 

Executable Analysis
^^^^^^^^^^^^^^^^^^^

<<<<<<< HEAD
As previously described in :ref:`Section 2 <CDRH>`, |cyTriage| uses ReversingLabs to analyze executables for malware.  
If you configured the session to upload file content and/or MD5 values, then |cyTriage| will know the malware results from many scanners. 
=======
As previously described in :ref:`Section 2 <CDRH>`, Cyber Triage uses ReversingLabs to analyze executables for malware.  
If you configured the session to upload file content and/or MD5 values, then Cyber Triage will know the malware results from many scanners. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

Scores are assigned based on ReversingLabs's proprietary algorithms that combine results from many scanning engines as well as their own techniques. 

You can get the malware details by going to the **File** tab at the bottom and choosing **Scan Results**. 

Yara Signatures
^^^^^^^^^^^^^^^

Yara signatures are a way that malware researchers share signatures about malicious files. 
<<<<<<< HEAD
|cyTriage| can use a set of rules to analyze the collected files. Files that match a rule will be scored as **Bad**. 

|cyTriage| uses **libyara 3.8.1**. Documentation can be found at: 
=======
Cyber Triage can use a set of rules to analyze the collected files. Files that match a rule will be scored as **Bad**. 

Cyber Triage uses **libyara 3.8.1**. Documentation can be found at: 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
`<https://yara.readthedocs.io/en/v3.8.1/>`_

Adding Yara Files
+++++++++++++++++

To include Yara signatures in the analysis, you need to copy them into a specific folder. 
You can find that folder by going to the Options panel. 

.. figure:: /_static/img/chapter_3/3_6.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Options Panel*

The default path is ``%localappdata%\cybertriage\config\yara_rules``. 
<<<<<<< HEAD
However, this location is can be changed by changing the data folder location in the |cyTriage| options panel. 

|cyTriage| will not search sub directories for Yara files. 
=======
However, this location is can be changed by changing the data folder location in the Cyber Triage options panel. 

Cyber Triage will not search sub directories for Yara files. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
If you would like to organize your Yara rules with sub directories, then you'll need to have a Yara file in the root directory that uses an include statements to refer to the other files. 

.. note::
   
   You will not be able to import the entire **Yara Rules** GitHub repository. 
   This repository has links between its ``.yar`` files and causes many false positives. 
   You should copy in only the rules that you are searching for. 

Scanning Files
++++++++++++++

<<<<<<< HEAD
Each time a session is ingested or a Yara rescan is initiated |cyTriage| will take all ``.yar`` files in the above folder and compile them into a single compiled Yara file. 

|cyTriage| will use that rule against each file that has not already been marked as Bad by malware scanning. 

If a rule matches a file, then the rule name will be specified in the |cyTriage| score. 
=======
Each time a session is ingested or a Yara rescan is initiated Cyber Triage will take all ``.yar`` files in the above folder and compile them into a single compiled Yara file. 

Cyber Triage will use that rule against each file that has not already been marked as Bad by malware scanning. 

If a rule matches a file, then the rule name will be specified in the Cyber Triage score. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

Memory Images
+++++++++++++

If you import a memory image, the same Yara rules will be used by the ``yarascan`` Volatility module.  
Documentation to the **yarascan Volatility module** can be found here:
`<https://github.com/volatilityfoundation/volatility/wiki/Command-Reference-Mal#yarascan>`_

File Location in Team Deployment
++++++++++++++++++++++++++++++++

When running in a Team environment, processing happens in different locations depending on the type of data you are adding. 

* The Yara rules on the Server will be used for all types of collections except for Memory Images. 
* The Yara rules on the Client will be used for Memory Images.  Volatility is run on the client system and the results are sent to the system for processing. 

Bad Lists
^^^^^^^^^

<<<<<<< HEAD
|cyTriage| ships with some basic programs and file names on its default Bad List that will cause files to be marked as **Bad**. 
=======
Cyber Triage ships with some basic programs and file names on its default Bad List that will cause files to be marked as **Bad**. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
You can expand this list based on your threat intelligence. See :ref:`Section 5.1 <ADT>` for details. 

Country Resolution
^^^^^^^^^^^^^^^^^^

IP addresses and host names will be resolved to a country using **GeoLite2 data** created by `MaxMind <http://www.maxmind.com/>`_. 
There should either be a column in each relevant table with this data or it is available in the **Hosts** tab at the bottom of the screen. 

Dynamic DNS
^^^^^^^^^^^

<<<<<<< HEAD
|cyTriage| will mark hostnames as suspicious if they are part of a dynamic DNS setup, which can be used by malware to avoid network-based detection. 
If a hostname uses dynamic DNS, then it will be marked as Suspicious. 

|cyTriage| ships with a set of Dynamic DNS providers that it will detect. 
=======
Cyber Triage will mark hostnames as suspicious if they are part of a dynamic DNS setup, which can be used by malware to avoid network-based detection. 
If a hostname uses dynamic DNS, then it will be marked as Suspicious. 

Cyber Triage ships with a set of Dynamic DNS providers that it will detect. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
You can add more providers by going to **Options**, **Dynamic DNS**.
The domains hosted by dynamic DNS providers are detected using the DNS server for the domain. 
To add a provider, you add the DNS server names.

.. figure:: /_static/img/chapter_3/3_7.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Dynamic DNS providers*

Ransomware
^^^^^^^^^^

<<<<<<< HEAD
|cyTriage| has several ransomware-specific detection techniques. 
=======
Cyber Triage has several ransomware-specific detection techniques. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
Ransomware incidents are much like any other incident where attackers laterally move through an environment, but the difference is on their final action (where they encrypt the data instead of just stealing it). 

The ransomware-specific techniques include:

* Detection of ransomware notes based on known naming patterns
* Detection of possible ransomware notes based on heuristics
* Detection of data recovery techniques disabling, such as Volume Shadow and Microsoft Backup
  
<<<<<<< HEAD
|cyTriage| focuses on making sure you quickly determine when the encryption started so that you can work backwards to determine how ransomware was deployed.  

|cyTriage| does not have decryption features.
=======
Cyber Triage focuses on making sure you quickly determine when the encryption started so that you can work backwards to determine how ransomware was deployed.  

Cyber Triage does not have decryption features.
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

Data Types
----------

<<<<<<< HEAD
We will not review the types of data that |cyTriage| collected. 
=======
We will not review the types of data that Cyber Triage collected. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
The data types on the left hand side are organized by user-oriented data and malware-oriented data. 

Accounts
^^^^^^^^

The Accounts menu item shows local and domain user accounts and their login activity. 

.. note::
   
   Not all data will be available for all users in this view because some data exists only for local accounts and other data is from logs that roll over. 

.. figure:: /_static/img/chapter_3/3_8.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Accounts Interface*

**What Should You Do**: Review the accounts to identify those with an abnormal naming convention, 
in appropriate permissions, or creation times that are similar to the incident timing. 

Logins
^^^^^^

This menu item shows the remote and local interactive logins to and from the system. 
You should review this data to look for sessions with suspicious locations or users. 
Remote logins are used to move laterally within corporate environments. 

.. figure:: /_static/img/chapter_3/3_9.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Logins Interface*

The rows in this table are grouped by the remote host and have columns for local and remote users (when it is known), times, and information about the remote host. 

For each remote host, you can use the bottom tabs to identify when the connection happened, details about the user, etc.

**What Should You Do**: Review this data to look for suspicious hosts, users, and times. 
<<<<<<< HEAD
|cyTriage| may mark some of them as being suspicious and you should review those and others to identify them as Good or Bad. 
=======
Cyber Triage may mark some of them as being suspicious and you should review those and others to identify them as Good or Bad. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

Observed Actions
++++++++++++++++

<<<<<<< HEAD
As |cyTriage| is parsing data from the target system, it keeps track of how various user accounts were used.  
=======
As Cyber Triage is parsing data from the target system, it keeps track of how various user accounts were used.  
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
You can then filter based on those **Observed Actions**

.. figure:: /_static/img/chapter_3/3_10.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Filter Observed Actions*

<<<<<<< HEAD
* Interactive Login or Program Run: |cyTriage| found evidence that the user had a local or remote interactive login with the system or launched a program (locally or remotely) on the system. 
* File or Service Access: |cyTriage| found evidence that the user interacted with a file or service on the system. Examples include accessing a file share or owning a file that got copied to the system. 
=======
* Interactive Login or Program Run: Cyber Triage found evidence that the user had a local or remote interactive login with the system or launched a program (locally or remotely) on the system. 
* File or Service Access: Cyber Triage found evidence that the user interacted with a file or service on the system. Examples include accessing a file share or owning a file that got copied to the system. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69
* Referenced: There was a reference to the user on the system, perhaps in an event log or registry, but no evidence was found of them doing anything on this specific system. Examples include accounts that were created and never used or entries in a log server. 

When looking at a domain controller and who had access to it, you can focus on accounts with **Interactive Logins**
and filter out the accounts that only authenticated with the system. 

Network Shares
^^^^^^^^^^^^^^

This Network Shares menu item shows the remote network shares that were accessed. 
Explicit mounts for these shares as well as references to them in programs that were run and folders accessed determine these. 

.. figure:: /_static/img/chapter_3/3_11.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Network Shares Interface*

The rows in this table are grouped by remote host and rows include share name, users, and times. 

**What Should You Do**: You should review this data to look for shares that the user should not have needed access to. 
This could indicate that the account was compromised or the user is looking for sensitive data. 

Programs Run
^^^^^^^^^^^^

The Programs Run menu item will show the programs that were executed on the system. 
This is based on registry data and other system configurations. 

.. figure:: /_static/img/chapter_3/3_12.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Programs Run Interface*

There are a lot of programs that are run on the system and this section can be quite overwhelming. 
You want to be looking for malicious programs that were run by an authorized or unauthorized user.  
<<<<<<< HEAD
|cyTriage| will group these rows based on naming patterns that we have found for many programs, such as having a version number as a folder. 

Filtering options on the top you to focus on just the suspicious items, which are those running from temporary folders and folders that should contain only data files. 
Many of the items in this list will be for deleted files that no longer have content or come from programs that use a consistent naming convention. 
|cyTriage| allows you to filter out the items without content and will group items based on similar names. 
=======
Cyber Triage will group these rows based on naming patterns that we have found for many programs, such as having a version number as a folder. 

Filtering options on the top you to focus on just the suspicious items, which are those running from temporary folders and folders that should contain only data files. 
Many of the items in this list will be for deleted files that no longer have content or come from programs that use a consistent naming convention. 
Cyber Triage allows you to filter out the items without content and will group items based on similar names. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

**What Should You Do**: Review the items and identify the programs that are bad or suspicious based on their path and malware results.  
In a corporate environment, you may find it useful to add the events that are known and common to a Good List. 
For example, many auto update programs will run from the ``AppData`` folder and be shown here, but you can choose to add them to a Global Good List.

Web Artifacts
^^^^^^^^^^^^^

The Web Artifacts menu item shows web history, bookmarks, downloads, and cookies from Chrome, Firefox, Edge, and IE browsers. 
You can use this information to see what the user was viewing or what they downloaded. 
This is useful for phishing campaigns that cause the user to download executables or when you suspect an insider.

.. figure:: /_static/img/chapter_3/3_13.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Web Artifacts Interface*

**What Should You Do**: Review these items to look for suspicious downloads or search queries. 
You can filter based on type and date range. 

Startup Items
^^^^^^^^^^^^^

The Startup Items menu item shows the various files that are executed when the system starts.
It uses dozens of registry and file system locations to identify the startup files that may contain malware. 

.. figure:: /_static/img/chapter_3/3_14.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Startup Items Interface*

**What You Should Do**: Review the suspicious entries, which are often based on pat and if they are signed. 
Mark them as good or bad and consider adding them to the Good or Bad Lists. 

Triggered Tasks
^^^^^^^^^^^^^^^

The Triggered Tasks menu item shows the Windows Scheduled Tasks and WMI Actions that ran on a periodic basis. 

.. figure:: /_static/img/chapter_3/3_15.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Triggered Tasks Interface*

**What Should You Do**: Review the scheduled tasks and actions to identify ones that could be malicious programs that periodically run to check the system status or query a remote server. 
Look for suspicious paths, times, or names. 
You may find it useful to add the scheduled tasks that are known and common in your environment to a Global Good List. 

Processes
^^^^^^^^^

The Processes menu item shows the process tree for the computer when the collection was made.

.. figure:: /_static/img/chapter_3/3_16.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Processes Interface*

**What Should You Do**: Review the suspicious processes that were flagged based on parent process or name. 
Mark them as Good or Bad. 

Active Connections
^^^^^^^^^^^^^^^^^^

This Active Connections menu item shows the network connections that were open at the time the collection was made. 

.. figure:: /_static/img/chapter_3/3_17.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Active Connections Interface*

The rows are grouped by remote host and have columns for the process with the connection, remote and local ports, times, and direction. 

**What Should You Do**: You should review this data for connections to unexpected hosts and for processes with unexpected network

Listening Ports
^^^^^^^^^^^^^^^

The Listening Ports menu item shows the ports that were listening for new connections when the collection was made. 

.. figure:: /_static/img/chapter_3/3_18.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Listening Ports Interface*

The rows are grouped by port number and have columns for the protocol, process, user, and information about what is usually at that port number. 

**What Should You Do**: Review these to processes that you did not expect to be listening for a connection. 
These could be backdoor applications into your system. Consider adding ports that are normal in your environment to a Good List. 

DNS Cache
^^^^^^^^^

The DNS Cache menu items shows the contents of the DNS cache, which contains references to the hosts that the computer tried to resolve to an IP address. 
You will find addresses in here that the system previously connected to. 

.. figure:: /_static/img/chapter_3/3_19.jpg
   :figclass: align-center
   :class: no-scaled-link

   *DNS Cache Interface*

The rows are grouped by remote host domain and have columns for IP and country. 

**What Should You Do**: You should review the data here for suspicious items and connections to suspicious hosts or countries. 

System Configuration
^^^^^^^^^^^^^^^^^^^^

This area shows you various settings that were enumerated during the collection. 
These come from various registry keys and other configuration files. 

.. figure:: /_static/img/chapter_3/3_20.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Settings Interface*

**What Should You Do**: Review the data to detect if any security settings were disabled or determine what the audit settings were. 

Analysis Views
--------------

An alternative way of looking at the collected data is by date or file system location. 
<<<<<<< HEAD
|cyTriage| supports both of these views. 
=======
Cyber Triage supports both of these views. 
>>>>>>> ecdce2520bf3095322e3b198514739aeb4e4dd69

Timeline
^^^^^^^^

This area shows you the collected items organized by time. 
You can use this data to identify what happened before and after a specific event. 

.. figure:: /_static/img/chapter_3/3_21.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Timeline Interface*

You can get to this data by either selecting **Timeline** from the left side and picking a date range or right clicking on most entries in their respective table and choosing **View in Timeline**.

.. figure:: /_static/img/chapter_3/3_22.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Choose View Timeline*

At any point, if the timeline becomes overwhelming, you can reduce the amount of data shown by filtering by type:

.. figure:: /_static/img/chapter_3/3_23.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Filter by Type*

File Explorer
^^^^^^^^^^^^^

The Files menu item can show several things:

* If a full file system scan was performed, you can view all file metadata. Though, content for all files will not be available. 
* You can view only suspicious or bad files.
  
You can get to a file by either choosing the **Files** menu item and navigating the structure. 
Or, when you are reviewing an item associated with a file, such as a Startup item, you can right click and choose to **View File in Directory**. 

.. figure:: /_static/img/chapter_3/3_24.jpg
   :figclass: align-center
   :class: no-scaled-link

   *View File in Directory*

That will then bring you directly to the file: 

.. figure:: /_static/img/chapter_3/3_25.jpg
   :figclass: align-center
   :class: no-scaled-link

   *File Interface*

**What Should You Do**: Review the suspicious entries. 
The files flagged as malware will also be in the Bad Items menu item. 
You can also use this to see what other files are located in the same folder as malware and other **Bad Items**. 

Registry Entries
^^^^^^^^^^^^^^^^

The Registry Entries menu item shows the suspicious registry entries on the system. 

.. note:: 
   
   The menu does not currently display the full registry hive. Only the entries that were found to be suspicious based on size and name. 

**What Should You Do**: Review these and mark them as good or bad. 


