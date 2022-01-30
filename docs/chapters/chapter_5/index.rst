.. _ADT:

Advanced Topics
===============

Offline Malware Scanning
------------------------

You can still use the |cyTriage| Online File Reputation Service when you are on an air-gapped network.

After the collection has been fully imported, you can package up the file MD5 hashes into a text file. 
    
* Press the **Details** link on the Dashboard next to the Online File Reputation line. 
    .. figure:: /_static/img/chapter_5/5_1.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Status*

* Choose to **Export Hashes** and pick a folder. 
    .. figure:: /_static/img/chapter_5/5_2.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Offline Analysis*
    
* That will produce a JSON text file with the hashes and license information. 
  
* You can then copy that file to an Internet-connected computer and upload it to `<https://rep1.cybertriage.com>`_. |br| Copy and paste the text file into that page.
    .. figure:: /_static/img/chapter_5/5_3.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Reputation Service*  

* It will download another JSON file that you can then copy back into |cyTriage| and import using the same **Details** panel that you used to export the original set of hashes. 

Local NSRL
----------

|cyTriage| will use its Online File Reputation Service by default to assign a threat score to files. 
The service uses the NIST NSRL to identify files that ship with known applications (such as Microsoft Windows). 
If you are not using the online service, you can configure a local copy of the NIST NSRL.

The steps to do this include:

1. Download the `NSRL index <https://sourceforge.net/projects/autopsy/files/NSRL/>`_
2. Unzip the file
3. Open the |cyTriage| options panel, enable **Use Local NSRL**, and browse to where you unzipped the ``.idx`` file to.
    .. figure:: /_static/img/chapter_5/5_4.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Options (Use Local NSRL)*  

Bad Lists
---------

|cyTriage| allows you to configure items that should always be considered a high threat. 
These can be added in the **Options** area. To add an item, choose the **Add Entry**. 
You will have the option of adding the item at a global level so that it applies to all future hosts or at the Incident level so that it is applied only to future hosts in the same Incident. 

.. figure:: /_static/img/chapter_5/5_5.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Options (Bad List Tab)*  

You can bulk add Bad List items by pressing the **Import** button. 
It takes in a CSV file of file names, hashes, or other data types. 
Use the **Generate Sample File** button to generate a sample CSV file to determine what columns need to exist. 

Good Lists
----------

|cyTriage| allows you to configure items that should not be considered a high threat. 
This feature is in addition to using the NIST NSRL to ignore files that were shipped with known applications. 

Good List Basics
^^^^^^^^^^^^^^^^

Good Lists are applied as data is analyzed in the pipelines. 
They contribute to the overall score of the item and can overrule heuristics that may identify the item as suspicious. 
Many of the tables will hide items on the Good List from you, but you can choose to **Include Items on Good List**. 

.. figure:: /_static/img/chapter_5/5_6.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Startup Items (Good List)* 


Configuring Good List Items
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add an item to the Good List, right click on it and choose **Not a Threat**. 
You can then choose to add it to a global- or incident-level Good List or only for that session. 

.. figure:: /_static/img/chapter_5/5_7.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Add Item to Good List* 

You can remove Good List entries in two ways. 
One is to right click on an item that is on the Good List and choose **Remove from Good List**. 

.. figure:: /_static/img/chapter_5/5_8.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Remove Item from Good List* 

The other is to use the Good List section on the options panel.

.. figure:: /_static/img/chapter_5/5_9.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Options (Good List Tab)* 

The table displays all current Good List entries. 
If the host is **(Global)**, the entry will be applied to all data. 
Otherwise, it will only apply to the given host name (across all sessions for that host). 

One or more Good List entries can be removed from the table by highlighting them and selecting **Remove selected item(s)**. 

Network Proxy
-------------

If you need to go through a corporate proxy to access the Internet, then |cyTriage| will need to be configured to use it for malware scanning. 
You can configure it in **Options, Network Proxy**. 

You can choose between using the operating system settings for the proxy or to manually enter a proxy. 
Make sure you press the button to test the connection. Depending on your environment, you may be prompted to accept an SSL certificate that your proxy uses.

.. figure:: /_static/img/chapter_5/5_10.jpg
    :figclass: align-center
    :class: no-scaled-link

    *SSL Certificate Information* 

Changing Port Number
--------------------

|cyTriage| will open **TCP port 443** so that the collection tool can send data to it over the network. 
If you have another application that is using that port, then you can configure |cyTriage| to us a different 
one by going to the Options panel and choosing the Network Settings tab.

.. figure:: /_static/img/chapter_5/5_11.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Options (Network Settings)*

If you change the port number, you will need to explicitly specify this port number when you manually run the collection tool.  

Backups
-------

It's important to make sure your |cyTriage| data is backed up. |br|
Ensure the following paths are part of your regular backup process:

* AppData: Both the Standard and Team environments save data to the ``AppData\Local\cybertriage`` folder for the user that |cyTriage| is running as. This should be backed up. 
* PostgreSQL: If you have a Team deployment with PostgreSQL, then refer to its standard procedures for backing up the `PostgreSQL <https://www.postgresql.org/docs/13/backup.html>`_ databases. 
