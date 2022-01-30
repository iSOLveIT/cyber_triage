.. _GRT:

Generating Reports
==================

Once your analysis is complete, you can generate a report to share with others. 
There are three types of reports supported by |cyTriage|: HTML, JSON, and CSV. 
All of these can be created from the Dashboard. 

.. figure:: /_static/img/chapter_4/4_1.jpg
   :figclass: align-center
   :class: no-scaled-link

   *Types of Reports*

HTML Report
-----------

HTML Reports are useful to share with other groups who want a human readable report. 
It contains the list of Bad and Suspicious items that were found on the system.

The report provides both a summary and a detailed view. 
The summary view provides basic information about each item and is organized into two tables: Bad and Suspicious. 
Selecting any item brings you to the detailed view that contains information such as MD5 hashes and time stamps. 

Any comments that you added during the investigation will be shown in the report. 

You can generate a PDF report based on the HTML report by using the **Print** feature in your web browser. 

JSON Report
-----------

The JSON report is useful for importing the results into another system, such as a SIEM. 
It is a JSON array with each element being a data item that was collected by |cyTriage|. 
For example, the first entry could be for a Startup Item or a Program Run entry. 

CSV Report
----------

The CSV report contains timeline data. 
It has one row for each event and this report can then be imported into other timeline tools, such as Excel. 
