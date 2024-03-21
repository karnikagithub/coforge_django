##############################################  INVENTORY MANAGEMANT  ######################################################

###### This application handles the CRUD operations of Inventory Management based on Location, Category, Item Masters #####

################################################# SET UP ####################################################################

1. cd INVENTORY_MANAGEMENT 
2. cd inventenv (virtual env)
3. inventenv\Scripts\activate.bat
4. (inventenv) inventory_management\py manage.py runserver

################################################ URLS ########################################################################

########### To do CRUD operations for LOCATION MASTER ###########
>>> url     :   http://127.0.0.1:8000/inventory/locations/

########### To do CRUD operations for CATEGORY MASTER ###########
>>> url     :   http://127.0.0.1:8000/inventory/categories/

########### To do CRUD operations for ITEM MASTER ###########
>>  url     :   http://127.0.0.1:8000/inventory/itemmasters/
>>> url     :   http://127.0.0.1:8000/inventory/itemmasters/1/download_file/ ( TO download the item file based upon the item ID)

########### To do CRUD operations for INVENTORY STOCK MASTER ###########
>>> url     :   http://127.0.0.1:8000/inventory/inventorymasters/

################################################ TEST #########################################################################

>>>>> Fixtures and test cases for API calls
>>> To CREATE fixtures.json of data from database : py manage.py dumpdata inventory_app.Model_Name > Model_Name_Fixture.json
>>> To LOAD fixtures.json                         : py manage.py loaddata Model_Name_Fixture.json
>>> cmd     :  py manage.py test inventory_app.tests (To run the tests)

################################################ SOCAIL_AUTH ##################################################################

>>>>> social_auth configurations are found in settings.py 

#################################################### END #######################################################################