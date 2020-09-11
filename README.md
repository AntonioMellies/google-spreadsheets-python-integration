# GOOGLE SHEETS PYTHON INTEGRATION

Basic example of integration of google spreadsheets

## Prerequisites

- Python
- pip
- virtualenv (optional)

## Running

### Clone the project
```
git clone https://github.com/AntonioMellies/googlesheets-python-integration.git
```

### Install dependencies
```
pip install -r requirements.txt
```

### Create credentials in to Google API
- Create new project
- Add library - Google Drive
- Add library - Google Spreadsheet
- Create service credential 
- Download of the credential (json file)


### Share spreedsheet
- Share the spreadsheet with the email contained in the credentials file (client_email)

### Create .env file
- Create in folder project .env file
- Add 'CREDENTIALS_FILE' variable (path of the credentials file) 
- Add 'URL_SPREADSHEET' variable (url of the spreadsheet shared)

### Run local
```python
python main.py
```

## Author
* **Antonio Frederico Mellies Neto**