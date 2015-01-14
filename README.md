kc-data-project
===============

Python data scripts to validate and send data to service providers.

To use:


Install Python 2.7.9
--------------------
Go to https://www.python.org/downloads/

Click on the button that reads "Download Python 2.7.9"
This will download an installer.  Double-click the installer and accept all the default choices the wizard shows you as it installs.

Get the scripts
---------------
With a browser go to https://github.com/chriseisbrown/kc-data-project

See the button marked "Download ZIP".  Click on this and you will get a download file.  This will probably go to your Downloads file.  Expand the zip to any folder you like, I'd suggest a folder something like C:\scripts\

FOR WINDOWS ONLY - Run the install script
-----------------------------------------
Where you parked the downloaded zip file, you should see a folder called kc-data-project-master.
Open this and you should see a file called <b>windows_install.bat</b>.  Double-click on this and it will set up the necessary script libraries.

Run the scripts:
----------------
Where you parked the downloaded zip file, you should see a folder called kc-data-project-master.

<b>prepare_emails.bat</b>      double-click on this script to read data from the "Data collection.xls" spreadsheet in the input-data folder and just write a report of what data will be used to send e-mails out.  Run this first and check that the data about to be sent to the service providers is correct.

<b>send_emails.bat</b>      double-click on this script to send e-mails to the service providers, using the data from the "Data collection.xls" spreadsheet in the input-data folder.  Note that you don't have to run prepare-emails.bat first but it is a good idea just to check.

