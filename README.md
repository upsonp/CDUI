# Running the application
## Requirements
1. Python 3.11+  

## Pre-setup
1. Open a file explorer and navigate to a location to install the application
2. In the addressbar enter `cmd`
   
## Clone and Setup
1. Clone the repo to a local directory: ```git clone https://github.com/upsonp/CDUI```  
1. Change Directory into the new cloned directory: ```cd CDUI```  
1. Create a new Virtual Enviornment: ```python -m venv env```  
1. Activate the new Virtual Enviornment: ```env\Scripts\activate```  
1. Update libraries based on the projects requierments: ```python -m pip install -r requierments.txt```  

You can test if the install worked correctly by starting the application with ```python manage.py cdui``` if the install worked the application will open, but it's not ready yet to connect to a database. Close the application and setup the enviornment.

## Setup the Enviornment
1. ```copy .env_sample .env```
1. ```notepad .env```
2. Fill out the ORACLE_DB_xxx connection details
3. The application should be ready now to start and connect and query the database. Make sure you have VPN turned on or are on the DFO Network.
4. Start the application with `python manage.py cdui`
5. click the 'Chief Scientists' button.

If all went well you should now see a list of Chief Scientists
