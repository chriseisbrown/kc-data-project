kc-data-project
===============

Python data scripts to validate and send data to service providers.

To use:

FOR WINDOWS USERS
-----------------

Install Python 2.7.9
--------------------
Go to https://www.python.org/downloads/

Click on the button that reads "Download Python 2.7.9"
This will download an installer.  Double-click the installer and accept all the default choices the wizard shows you as it installs.

Get the scripts
---------------
With a browser go to https://github.com/chriseisbrown/kc-data-project

See the button marked "Download ZIP".  Click on this and you will get a download zip file.  This will probably go to your Downloads file.  Expand the zip file into any folder you like, I'd suggest a folder something like C:\scripts\

Run the install script
-----------------------------------------
In the folder that you expanded the downloaded zip file into, you should see a folder called kc-data-project-master.
Open this and you should see a file called <b>windows_install.bat</b>.  Double-click on this and it will set up the necessary script libraries.

Run the scripts:
----------------
In the folder that you expanded the downloaded zip file into, you should see a folder called kc-data-project-master.  This contains two scripts that you will run when you want to do the process of contacting service providers.  Get your "Data collection.xls" spreadsheet ready and then copy it into the <i>input-data</i> folder.  It will be used for input to the mail out process.

<b>prepare_emails.bat</b>      double-click on this script to read data from the "Data collection.xls" spreadsheet in the input-data folder and just write a report of what data will be used to send e-mails out.  Run this first.  It will write an Excel file called data_report with a timestamp of today's date and time in its name (e.g.; data_report_2015-01-14-1115.xls).  Open this file in Excel (or just double-click it).  Check that the data about to be sent to the service providers is correct.  As the prepare_emails script runs it will write its progress out to a file called prepare_emails_log.log.   Open the log file by double-clicking it to see if everything ran ok, no nasty error messages or warnings.

<b>send_emails.bat</b>      double-click on this script when you are ready to send e-mails to the service providers, using the data from the "Data collection.xls" spreadsheet in the input-data folder.  Note that you don't have to run prepare_emails.bat first but it is a good idea to do so just to check all wil be ok.  The script will write its progress out to a file called send_emails_log.log.  Open the log file by double-clicking it to see if everything ran ok, no nasty error messages or warnings.  It should list all the e-mails that it sent to the service providers.


FOR MAC USERS
-------------
Install Python 2.7.9
--------------------
Mac OS X comes with the correct version of Python so there should be nothing to do here.

Get the scripts
---------------
With a browser go to https://github.com/chriseisbrown/kc-data-project

See the button marked "Download ZIP".  Click on this and you will get a download zip file.  This will probably go to your Downloads file.  Expand the zip file into any folder you like, I'd suggest a folder something like <your user-name>/scripts/

Run the install script
-----------------------------------------
In the folder that you expanded the downloaded zip file into, you should see a folder called kc-data-project-master.
Open this and you should see a file called <b>windows_install.command</b>.  Double-click on this and it will set up the necessary script libraries.

Run the scripts:
----------------
Folow the instructions for Windows users above but use <b>prepare_emails.command</b> and <b>send_emails.command</b> to run the scripts.



