## Follow these steps to start the project
### Create a python virtual environment
    1. python3 -m venv my_venv_name -> Creating virtual environment
    2. .\my_venv_name\bin\activate -> Activating virtual environment
### Command for installing required packages.
    pip install -r requirements.txt
### Execute this commadn to start the project:
    python manage.py runserver



### Folowing are the 3 endpoints to fetch data
    1. http://127.0.0.1:8000/api/transaction?transId={transactionid}  --->GET API /transaction/{transaction_id}
    2. http://127.0.0.1:8000/api/transactionSummaryBySKU?daysago={last_n_days} --->GET API /transaction-summary-bySKU/{last_n_days}
    3. http://127.0.0.1:8000/api/transactionSummaryByCategory?daysago={last_n_days} --->GET API /transaction-summary-bycategory/{last_n_days}

    NOTE - all the values transactionid,last_n_days are int values.