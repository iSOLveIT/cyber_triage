.. _HSTRY:

History
=======

The following were added in 3.0.2 (Nov 30, 2021):

* New Features:
   + Collect WofCompressedData files using native APIs.
   + Added creation time and file sizes to various UIs. 

* Bug Fixes: 
   + Fix ransomware note bug that could flag the wrong file (with the same name)

The following were added in 3.0.1 (Nov 10, 2021):

* New Features: 
   + Flag Ransomware notes based on known names and heuristics
   + Flag commands that disable volume shadow and Windows backup
   + Added ability to filter OS Accounts based on their actions on the system
   + Detect and mark WOF compressed files (content is still not collected)
   + Added ability to collect only hashes instead of file content to the UI
  
* Bug Fixes:
   + Fixed issues with collection from IPv6 hosts
   + Fixed Google Object upload bug 
   + Fixed bug about not being able to open Yara rule
   + Fixed issue when deleting multiple hosts. 
   + Various other minor bug fixes

The following were added in 3.0.0 (Sept 13, 2021):

* New Feature:
   + The backend database was replaced with SQLite and PostgreSQL and the same schema as used by Autopsy. This results in better stability.
   + Added ability to delete incidents.
   + Added ability to **soft delete** hosts. They are not shown in the UI, but the actual data is still retained. This will be improved. 
   + All collected data must now be part of an Incident.
   + Collection tool JSON schema changed and is not compatible with v2.
   + Renamed **Session** to **Host**. 
   + Added host name to the top of each panel (user request)
   + Users are reported as being local or domain

* Team Changes: 
   + More extensive REST APIs exist because clients now connect to the REST API instead of directly to the database
   + Clients must use a **Server Key** to connect to the REST API. 
  
* Bug Fixes:
   + Fixed issue where a process would be collected twice
   + No longer create an **inferred user** from a failed login for an account that didn't exist

The following were added in 2.14.5 (June 4, 2021):

* Fixes:
   + Fixed parsing error with WMI Databases 
   + Updated URL to download evaluation data

The following were added in 2.14.4 (Apr 15, 2021):

* New Feature:
   + Collect Exchange files from wwwroot for WebShell detection
   + Distribute NSA-based Yara rules to detect web shells related to recent Exchange compromises
   + Added keyboard short cuts for scoring items. 
   + Added ``--skip_file_contents`` and ``--skip_source_file_contents`` command line arguments to collect only MD5s and not file content.
  
* Fixes:
   + Do not flag **inferred accounts** when there are no local logins. Inferred accounts come from event logs. 
   + Support PsExec 2.3 and above 
   + Fixed bug that prevents Server from stopping when it was run as a Windows server

The following were added in 2.14.3 (Mar 1, 2021):

* New Feature:
   + Temporary S3 Session Tokens can be used.

* Fixes: 
   + Better deal with corrupt compressed JSONs
   + Better UI feedback while encrypted JSONs are being checked
   + Fixed bug that incorrectly reported local login as remote
   + Fixed bugs with parsing some startup items
   + Fixed bug with WMI Action heuristics
   + Fixed Bug showing WMI DB in timeline
   + Collection tool will use different output folder if run from SysWow (via EDR)

The following were added in 2.14.2 (Jan 25, 2021):

* New Features
   + DLLs of running processes are collected
   + Files can be rescanned by new Yara rules and bad lists after initial collection
   + Updated Volatility for Windows 10 19041 Profile
  
* Fixes
   + Improved event log parsing performance
   + Fixed bug that prevented S3 uploads on large JSON files
   + Allow new version of PsExec (2.3) to be used.
   + Fix UI refresh issues over RDP
   + Fixed memory issue with large encrypted JSONs

The following were added in 2.14.1 (Oct 28, 2020):

* New Features:
   + S3 Test button uses configured proxy
   + Collection tool can use proxy for S3 using configuration file
   + Added CSV and JSONL incident-level reporting

* Bug Fixes:
   + Changed JMX to not listen for remote connections and require TLS.
   + Fixed bug with Team options panel 
   + Fixed HTML incident-level reporting

The following were added to 2.14.0 (Oct 7, 2020):

* New Features:
   + Collection Tool output can now be encrypted using AES
   + Collection Tool output is now compressed when saved to local file
   + Collection Tool output can be uploaded to S3 bucket
   + Yara rules are applied to memory images using Volatility
   + The Event Log Id is displayed in the UI
   + Session files are no longer deleted after they are imported
   + When evaluating, a session can be automatically created with evaluation data. 

* Bug Fixes:
   + Faster processing of systems with a large number of user accounts and logins. 
   + Fixed UI rendering issues from font scaling
   + Partial files are collected when read errors occur (most often occurs with event logs that use NTFS compression)

