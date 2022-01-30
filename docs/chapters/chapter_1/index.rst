.. _SI:

Standard Installation
=====================

This section outlines how to install the Standard (desktop) version of |cyTriage|. 
If you have the Team (client server) version, then refer to :ref:`Section 7 <CTEAM>`. 

Hardware Requirements
---------------------

The Standard version of |cyTriage| requires: 

* 64-bit version of Windows 7 or newer
* 12GB+ of RAM
* 4+ cores
* 100GB+ of free hard drive space. 
  
We recommend using SSD storage for best performance. 

Refer to :ref:`Section 7 <CTEAM>` for Team version requirements. 

Software Requirements
---------------------

* `Cyber Triage <https://www.cybertriage.com/download-eval/>`_ MSI installer.
* :download:`PSExec 2.2 <https://download.sysinternals.com/files/PSTools.zip>` (or newer) if you want to push the collection tool to remote hosts over the network.

Standard Installation Steps
---------------------------

These installation steps are for the **Standard and Lite versions** of |cyTriage|.
If you are using the **Team version (client server)**, first go to :ref:`Section 7 <CTEAM>` for an overview of that process. |br|

|cyTriage| is installed on your analysis system, not on the system being investigated. 

1. Run the MSI installer and choose the default settings. 
2. Launch |cyTriage| from the Start menu or the Desktop icon. 
3. You will be notified that a license file was not found on your system and you will have a choice to either use the evaluation version or to enter your license key, named something like ``cybertriage-license.l4j``.

.. figure:: /_static/img/chapter_1/license_404.jpg
   :figclass: align-center
   :class: no-scaled-link

   *License file not found*

Configuring PsExec for Remote Collection
----------------------------------------

If you are going to be pushing the collection tool to remote hosts, you will also need to configure **PSExec**. 
Extract the contents of the ``PSTools.zip`` file to a folder on your computer. 

1. Open the **Options** panel from the opening |cyTriage| window. 
2. Navigate to the **General** tab.
3. Find the **PsExec Settings** area, choose the *Browse* button, and navigate to the folder that you extracted the contents into.  Confirm that you read the *PSTools End User License Agreement*. 

.. figure:: /_static/img/chapter_1/options.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Configuring* **PSExec** *tool*

Network Requirements
--------------------

Inbound Network Ports
^^^^^^^^^^^^^^^^^^^^^

|cyTriage| will require several network ports as outlined in the table below. A description of each will follow. 

.. table::
   :align: center
   :width: 100%
   :class: align-center
   :widths: auto
      
   +----------------------------------------------------------------------------------------------------------------------------+
   | .. centered:: Target Endpoints for Live Automatic Collection                                                               |
   +=========================+====================================+=============================================================+
   | **Protocol**            | **Port(s)**                        | **Usage (Inbound from)**                                    |
   +-------------------------+------------------------------------+-------------------------------------------------------------+
   | TCP                     | 445\ [#at]_                        | File Sharing / PsExec (Server)                              |
   +-------------------------+------------------------------------+-------------------------------------------------------------+

.. table::
   :align: center
   :width: 100%
   :class: align-center
   :widths: auto
      
   +----------------------------------------------------------------------------------------------------------------------------+
   | .. centered:: |cyTriage| Server                                                                                            |
   +=========================+====================================+=============================================================+
   | **Protocol**            | **Port(s)**                        | **Usage (Inbound from)**                                    |
   +-------------------------+------------------------------------+-------------------------------------------------------------+
   | TCP                     | 443\ [#at]_                        | Collection Tool (Target / Client)                           |
   +-------------------------+------------------------------------+-------------------------------------------------------------+
   | TCP                     | 9443\ [#at]_                       | Rest API (Client)                                           |
   +-------------------------+------------------------------------+-------------------------------------------------------------+
   | TCP                     | 61616\ [#at]_                      | ActiveMQ (Client)                                           |
   +-------------------------+------------------------------------+-------------------------------------------------------------+

.. table::
   :align: center
   :width: 100%
   :class: align-center
   :widths: auto
      
   +----------------------------------------------------------------------------------------------------------------------------+
   | .. centered:: PostgreSQL                                                                                                   |
   +=========================+====================================+=============================================================+
   | **Protocol**            | **Port(s)**                        | **Usage (Inbound from)**                                    |
   +-------------------------+------------------------------------+-------------------------------------------------------------+
   | TCP                     | 5432\ [#at]_                       | Postgres (Server)                                           |
   +-------------------------+------------------------------------+-------------------------------------------------------------+


-----

.. [#at] The description of each network port:

    + **TCP 443:** Used to receive connections from the collection tool and Team clients with collected data. You can change this if you have a conflict. 
    + **TCP 445 (SMB):** File sharing is required for PsExec to work on any target system where “Live Automatic” collection is used. 
    + **TCP 5432:** PostgreSQL uses this port by default and the Team server must be able to connect to it. 
    + **TCP 9443:** REST API used with Team clients and SOAR/SIEM integrations. 
    + **TCP 61616:** ActiveMQ uses this to communicate with the clients.

.. note:: Ports are customizable and any port modifications must be reflected in firewall rules.
    
Outgoing Remote Hosts
^^^^^^^^^^^^^^^^^^^^^

Cyber Triage will reach out to some hosts to test network settings or upload file hashes and content. 
If you have a proxy, you may need to add exceptions for these hosts: 

* https://data.reversinglabs.com
* https://www2.cybertriage.com
* https://rep1.cybertriage.com

