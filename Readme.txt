1. About: The code reads an excel file and creates a list of objects each with the following attributes:
          a. Category: Basic Functionality of the service (Big Data and Analytics, Compute, etc.)
          b. Service: Type of Service (Big Data as a Query, etc.)
          c. Title: Name of the cloud service (Amazon Athena, Amazon Cognito, etc.)
          d. Ranking: Base value is 1, for same services with 2 or more products ranking is done correspondingly. 

2. Requirements and dependencies:  Python version 3.0
                                 - openpyxl version 2.6.2

3. Running the files:
               a. Download all the files along with data (class.xlsx) into working directory.
               b. Change data filepath in AWSmaps.py file.
               c. Run from CMD: python AWSmaps.py