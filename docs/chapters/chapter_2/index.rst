.. _CDRH:

Collecting Data From Remote Host
================================

The first step to investigating the remote host is to collect data from it. 
This section outlines how to collect data and add it to Cyber Triage for analysis. 

Incidents and Hosts
-------------------

Cyber Triage uses the following data management terminology:

* An Incident represents an investigation and can contain data from one or more hosts.
* A Host represents a computer that is being investigated. There are a variety of ways to get data from hosts into the application. 
  
The basic workflow for adding a host is: 
    
1. Create a new incident or open an existing one.
2. Choose the collection method to get data into Cyber Triage. Details are given below. 
3. Choose the kinds of data you want to collect.
4. Choose your malware scanner settings.


Creating an Incident
--------------------

Every host needs to be part of an incident. An incident will have its own good and bad lists and its own database. 
You can create an incident from the opening Cyber Triage screen:

.. figure:: /_static/img/chapter_2/2_1.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Cyber Triage screen*

1. Press **New Incident** and add:
   
   * Incident Name: Must be unique and not have special characters
   * Description: Optional

.. figure:: /_static/img/chapter_2/2_2.jpg
   :figclass: align-center
   :class: no-scaled-link

   *New Incident Form*

2. That will then bring you to the Incident Dashboard:

.. figure:: /_static/img/chapter_2/2_3.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Incident Dashboard*

From here, you can add data from hosts and open existing hosts. 

Collection Methods
------------------

To add data from a host, press **Add New Host** and you'll be presented with this screen, which gives you five options:

.. figure:: /_static/img/chapter_2/2_4.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Adding New Host*

The five collection methods to get data into Cyber Triage are: 

1. **Live Automatic**: Cyber Triage will push the collection tool to a remote host over the network using PsExec. Collected data is sent directly back to Cyber Triage. See `Section 2.3.1 <#live-automatic>`_ for details. This is not available in the Lite version. 
2. **Live File**: The collection tool is manually run from a network or USB drive on the remote host. Data is saved to the USB drive, network share, or S3 bucket and then manually imported into Cyber Triage. This is useful when the host has been unplugged from the network or for consultants who have clients perform the acquisition. See `Section 2.3.2 <#live-file>`_ for details. 
3. **Live Manual**: The collection tool is manually run from a network or USB drive on the remote host (like Live File), but the data is sent over the network instead of being saved to the USB drive. See `Section 2.3.4 <#live-manual>`_ for details. 
4. **Disk Image**: Dead analysis is performed on a disk image that was previously acquired in either raw or E01 format. See `Section 2.3.5 <#disk-image-based-dead>`_ for details. 
5. **Memory Image**: Dead analysis is performed on a memory image that was previously acquired (using your own tools – Cyber Triage does not do memory acquisition). See `Section 2.3.6 <#memory-image-based-dead>`_ for details. 

The following sections provide more details of each method.

Live Automatic
^^^^^^^^^^^^^^

With **Live Automatic**, Cyber Triage will push the collection tool to a live system and it will send its results back to Cyber Triage over the network. 
This feature is not available in the Lite version.
To do this, the following configuration must exist on the remote system:

*  Running Windows XP or later
*  File and network sharing enabled
*  Domain account with administrator privileges

   + If you have a local administrator account on the remote system, see the instructions in `Section 6.1 </chapters/chapter_6#allow-remote-connections-with-local-accounts>`_ for configuring it.

To perform the collection, select the **Live Automatic** icon. You will be presented with a panel to enter:

* Hostname of computer to collect from
* User name, domain, and password for an account on the remote system that has administrator privileges
  
If you did not configure **PSExec** as described in `Section 2.3 </chapters/chapter_1#standard-installation-steps>`_, then you will be prompted to do so. 

.. figure:: /_static/img/chapter_2/2_5.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Live Collection - Automatic*

After pressing *Continue*, you will be prompted to choose what data types to collect and what malware scanner settings to use. 
Refer to `Section 2.5 <#collection-settings>`_ for details on those panels. 

If this is your first time running the program, you may also be prompted by Windows or a security program to allow Cyber Triage to open a network port. 
You will need to allow this to happen so that the collection tool can send data to Cyber Triage on TCP port 443. 

See `Section 6.1 </chapters/chapter_6#allow-remote-connections-with-local-accounts>`_ if the administrator account on the remote system is a local account and you are having problems.

After the collection has started, you will be able to see the results. Proceed to :ref:`Section 3 <ASD>` for an overview of the analysis techniques.    

Queuing Up Collections
++++++++++++++++++++++

If you have a Team deployment of Cyber Triage, you can submit multiple host names to collect from. 
This allows you to enter a set of hosts, have basic data collected from them, and then you can prioritize what you review. 
To do this, use the *Add Multiple* button when entering host details. 

.. figure:: /_static/img/chapter_2/2_6.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Live Collection - Automatic*

You can then enter a list of host names. 

.. figure:: /_static/img/chapter_2/2_7.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Add Multiple Host Names*

Cyber Triage will then validate the credentials with those host names and then queue them up. 
You can see progress from either the Incident Dashboard (which is where Cyber Triage will redirect you to) 
or by choosing the **Pending Sessions** button from the main panel.

.. figure:: /_static/img/chapter_2/2_8.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Pending Sessions*

Live File
^^^^^^^^^

This approach saves the collected data from the live host to a file (typically on a USB drive). That file is then manually imported into Cyber Triage. 
The first thing you'll need to do is get access to the Cyber Triage Collection Tool. Follow the instructions in `Section 2.4 <#extracting-the-collection-tool-for-live-collections>`_ to do this. 
To perform a collection, the following are performed on the remote computer:

1. Insert the USB device into the target computer or make the collection tool available on a network share. 
2. Decide if you want to use the graphical interface or command line interface. The graphical interface will ultimately call the command line interface tool with arguments based on your UI selections. 
   
3. To use the graphical interface:
    a. Double click on the CyberTriageGUI.exe program.
    b. Confirm that the data is going to the correct location (path, S3 bucket, etc.)
    c. Add an optional password if you want to encrypt the output. NOTE there is no recovery mechanism if you forget it. 
    d. Choose the data types you want to collect. See `Section 2.5.1 <#data-collection-types>`_ for details. 
    e. Choose Start.

4. To use the command line interface: 
    a. Open a window that shows the **CyberTriageCLI.exe** executable. Right-click the ``CyberTriageCLI.exe`` file and select **Run as Administrator**. This will start collection of the host.
    b. Alternatively, you can launch a command prompt with admin privileges and run the **CyberTriageCLI.exe** program with no arguments. |br| If you want to customize what data types are collected, then there are arguments you can give. Run with “—help” to get the list. 

5. When the collection tool has finished its collection, there will be a directory called ``CyberTriage_<timestamp>`` on the USB device, network share, or S3 bucket. 

The next step is to import the collected data into Cyber Triage. 

.. note::

    It is important to have *AutoRun* disabled on the computer running Cyber Triage so that it does not get infected by malware that spreads by USB devices. 

The following are performed on the computer running Cyber Triage:

1. From the **Incident Dashboard**, choose **Add New Hos** and then choose the **Live File** box. 
2. Enter a host name for the remote host. 
3. In the file selector, navigate to the folder that was created for the collection on the USB drive or downloaded S3 bucket. |br| Choose the JSON file in that folder. This will import the data into Cyber Triage. 

.. figure:: /_static/img/chapter_2/2_9.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Live Collection - File*

You will need to choose the malware settings to use. Refer to `Section 2.5.2 <#file-reputation-malware-scanning-settings>`_.

After collection has started, proceed to :ref:`Section 3 <ASD>` for an overview of the analysis techniques. 

Importing from S3
^^^^^^^^^^^^^^^^^

Some users use S3 buckets as a way to get data from remote sites. To do this:

* Extract the Collection Tool with **S3** configured (see `Section 2.4 <#extracting-the-collection-tool-for-live-collections>`_).
* On the target system, launch ``CyberTriageGUI.exe`` and choose **S3 Cloud Bucket** as the destination (it should be the default if you configured the **S3** destination)
* Pick an optional encryption password.
  
After the collection has locally saved the data, it will then perform an upload to **S3**.

To get data into Cyber Triage from **S3**, you currently (as of 3.0.0) need to manually download it to a local file 
and then add it using **Live File** (see `Section 2.3.2 <#live-file>`_). 
A future version will allow you to directly review the contents of **S3 buckets**. 

Live Manual
^^^^^^^^^^^

**Live Manual** is for cases when you cannot automatically push the collection tool to the remote system. 
In this approach, you run the collection tool from the remote system and it sends the results over the network to Cyber Triage. 

As with **Live Collection - Automated**, the collection tool will need to be able to communicate with the Cyber Triage system over **TCP port 443**. 

If you haven't already done so, extract the collection tool to a USB drive using the steps outlined in `Section 2.4 <#extracting-the-collection-tool-for-live-collections>`_. 

To perform the collection, you will need to interact with both Cyber Triage and the remote system. 

In Cyber Triage:

1. Choose the **Live Manu** box from the **Add New Host** area. 
2. You will be prompted to enter information about the host being collected from:
   
.. figure:: /_static/img/chapter_2/2_10.jpg
    :figclass: align-center
    :class: no-scaled-link

    *Live Collection - Manual*

3. If this is the first time that you are running Cyber Triage, you maybe prompted by Windows Firewall or another security application to allow Cyber Triage to accept connections. You will need to do this to allow data to be imported into Cyber Triage.
4. Cyber Triage will tell you what settings to use on the remote system.

.. figure:: /_static/img/chapter_2/2_11.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Live Collection - Manual*

Next, perform the following on the remote system.

1. Insert the USB device with the collection tool, or ensure that the collection tool is available via a network share. See `Section 2.4 <#extracting-the-collection-tool-for-live-collections>`_ for details. 
2. Decide you are going to use the graphical interface or command line interface. 
3. To use the graphical interface: 
    a. Open the USB drive in file explorer.
    b. Double click on the ``CyberTriageGUI.exe`` program.
    c. Choose **Remote Server** as the Destination and enter the hostname of the computer running Cyber Triage.
    d. Press Start after configuring the other collection options

    .. figure:: /_static/img/chapter_2/2_12.jpg
        :figclass: align-center
        :class: no-scaled-link

        *Collection Tool*

4. To use the command line interface:
    a. Open a command prompt with Administrator privileges and change directory to the collection tool folder. 
    b. Type the command that was given by Cyber Triage. Something like: 
        .. code-block:: powershell

           CyberTriageCLI.exe --server host1

    c. You should see the collection tool start to produce output: 
        .. figure:: /_static/img/chapter_2/2_13.jpg
            :figclass: align-center
            :class: no-scaled-link

            *Command Output*

After collection has started, proceed to :ref:`Section 3 <ASD>` for an overview of the analysis techniques. 

Disk Image-based Dead 
^^^^^^^^^^^^^^^^^^^^^

Disk image-based analysis is useful if a full disk image has already been performed of the system. 
To collect data from a disk image:

1. Choose the **Disk Image** button from the **Add New Host** area.
2. Browse to your raw or E01 file.
3. Choose a name for the host. 
   
After collection has started, proceed to :ref:`Section 3 <ASD>` for an overview of the analysis techniques. 

Memory Image-based Dead 
^^^^^^^^^^^^^^^^^^^^^^^

Memory image-based analysis allows you to review volatile data from a system and bypass advanced rootkits and malware. 
Cyber Triage uses the open source Volatility 2 program to parse the memory images. 
You need to acquire the memory with your own software. 
Cyber Triage will not make an image of memory. 

To import a memory image:

1. Choose the **Memory Image** button from the **Add New Host** area.
2. Browse to your memory image file
3. Choose the Volatility profile, if you know it. Cyber Triage will use Volatility's auto detection features, but sometimes they are not correct and manually picking will provide better results. 
4. Choose a name for the host. 
   
After collection has started, proceed to :ref:`Section 3 <ASD>` for an overview of the analysis techniques. 

.. note::
    
    A session created from a memory image will not have all of the data and fields that you'd see from the Cyber Triage Collection Tool. 
    The interface will identify places that have incomplete data. 

Extracting the Collection Tool for Live Collections
---------------------------------------------------

If you are going to use either **Live Manual** or **Live File** methods to create a session, you will need to first extract the collection tools from the Cyber Triage UI. 

To extract, choose the **Collection Tools** feature from the opening Cyber Triage window. |br|
Choose a folder and it will make a **CyberTriageCollectionTool** folder with the command line and graphic interface programs. |br|
This folder will typically go on either a USB drive, a network share, or emailed to someone.

.. figure:: /_static/img/chapter_2/2_14.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Extract Collection Tool*

Configuring S3 Bucket Uploads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the collection tool is going to automatically upload data to an S3 bucket (on AWS or some other provider), 
then you will need to configure those settings before you extract it. 

The settings will be saved to a configuration file. 
The intended use case is that the Cyber Triage user will configure the S3 details and pass off the extracted folder to an end user. 

You will need to pick:

* Provider: Amazon AWS or another S3-equivalent
* Region: If using AWS, you'll need to pick the region your bucket is in.
* Service URL: If using a non-AWS provider, you'll need to specify the Service URL. It should have the region in the URL. 
  + For example: S3.us-east-2.wasabisys.com
* Bucket: The name of the bucket to save the results to. The bucket will be created if it does not already exist. There are limits on bucket names, so please be mindful of them. For example, no spaces or capital letters. 
* Access Key ID and Key: You will need to get an access key from the provider. These will be saved **unencrypted** in the configuration file. 
* Session Token: An optional field if you are using temporary credentials. You can generate this via the `AWS Command Line Tool <https://docs.aws.amazon.com/cli/latest/reference/sts/get-session-token.html>`_:

.. figure:: /_static/img/chapter_2/2_15.jpg
   :figclass: align-center
   :class: no-scaled-link

   *S3 Configuration*

After these settings are entered, you need to press **Test Connection** to verify they are correct. 

.. note::

    Version 2.14.0 does not currently support proxies with S3. So, the test may fail if your network has a proxy. 

S3 Access Control
^^^^^^^^^^^^^^^^^

The extracted collection tool will have S3 credentials in a configuration file. We recommend:

* You create a bucket that the collection user will upload to
* You create access keys that have only write (not read) permissions for the target bucket
* Consider using temporary credentials that works for your situation
  
With this design, if the S3 credentials are compromised, the data already uploaded cannot be accessed.

Collection Settings
-------------------

Regardless of the method used to get data from the target system into Cyber Triage, 
you will need to decide at some point about what data types to collect and how to detect malware. 

Data Collection Types
^^^^^^^^^^^^^^^^^^^^^

The **Add New Host** wizard will show you a dialog such as this:

.. figure:: /_static/img/chapter_2/2_16.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Scan Type*

This is where you pick what types of data will be collected. 
The Collection tool has a similar interface and set of options. 

Cyber Triage groups the types based on the concepts in the Divide and Conquer DFIR Process:

**Users**

* **Accounts**: Collects information about all users on the system and who is actively logged in.
* **Logins**: Collects user login information from event logs and the registry.
* **Network Shares**: Collects information about mounted network shares.
* **Programs Run**: Collects information about what programs were executed by users and collects the corresponding executable file. 
* **Web Artifacts**: Collects Firefox, Chrome, IE and Edge databases and analyzes them for downloads, cookies, and history. Also collects files from Downloads folder. 

**Malware**

* **Startup Items**: Collects the programs that are run each time the computer is started or a user logs in. 
* **Scheduled Tasks**: Collects Schedule Task information and the associated executable files. 
* **Processes**: Collects information about running processes. Includes executable files being used by processes. 
* **Network**: Collects information about active network connections and open ports
* **Network Caches**: Collects DNS cache, ARP cache, and routing tables.
  
**System Configuration**

* **System Configuration**: Collects information about the system, such as audit and security settings.
  
**Full File System Scan**: Scans each file on the system and collects the file content if they are suspicious. 
This is the most time intensive step of the collection process. 

The default is **Full Scan**, which includes all of the types listed above. 
You can also skip the most time intensive process and choose **Skip File Scan**. 

If time is very limited and you what you are looking for, you can choose **Custom** and select only certain types. 

File Reputation / Malware Scanning Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will also be prompted to choose how the files will be analyzed for malware. 

.. figure:: /_static/img/chapter_2/2_17.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Scan Type - File Reputation*

Cyber Triage uses its Online File Reputation Service to analyze files for malware. 
This service uses ReversingLabs, the NIST NSRL, and other sources to assign a score to each file. 

You need to configure what data is uploaded. See `Section 3.6.1 </chapters/chapter_3#executable-analysis>`_ for details on how these results are used. 

* **Upload MD5 hashes**: This will send only the MD5 hash of your files to the service. If the service knows that the file content is associated with malware, then it will identify it as such. Note that any minor change to malware will change its MD5 and it will not be flagged as malware using this technique.
* **Upload file content**: This will send the full file to the service if the SHA1 value was not found. It will be scanned and a result will be returned. The raw content will not be visible to other users, only the analysis results. 
* **Mark unknown file as suspicious**: If the file was not known to the service and you do not want to upload file content, you can choose to have those files marked as suspicious so that you can be aware of them and decide that they are worth additional analysis or ignored.

If you use Cyber Triage on a computer not connected to the Internet, then you have two options:

* You can export hash values and manually submit them to the online file reputation service using a website (see `Section 5.1 </chapters/chapter_5#offline-malware-scanning>`_)
* You can use a local copy of the NIST NSRL to ignore known files (see `Section 5.1 </chapters/chapter_5#offline-malware-scanning>`_)

Collection Tool Arguments
-------------------------

The Collection Tool is a command line program with various optional arguments that allow you (or other applications) to control what it will collect. 
To see the options, you can choose supply the ``—help`` option.  
If you supply no arguments, the Collection Tool will collect from the live running system using default settings.

.. code-block:: powershell

   CyberTriageCLI --help
   usage:

   CyberTriageCLI -i image_name -o output_file <options>

        --encrypt_outfile password password : Encrypt the output file with the given password (password specified twice)
        --s3_upload_config s3_config_file : Upload output file to S3 storage
        --server host : Stream data back to the given Cyber Triage server hostname/IP
        --port port : Port number to connect to the Cyber Triage server
        --sessionid sessionID : Session ID
        --serverkey serverkey : Get from CyberTriage server config panel
        --incident : Use with --serverkey to set the incident for the session
        --fast : Skips full file by file scan. Faster but less comprehensive triage
        --dtypes : Comma list of data types
        --tempdir : Path where temp files are written to
        --skip_file_contents : Report only MD5 hashes and not content for files of interest.
        --skip_source_file_contents : Report only MD5 hashes and not content for source files (registry hives, prefetch, etc..) 
