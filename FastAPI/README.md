# Hello world example for FastAPI with the command pattern
This guide demonstrates how to set up a basic FastAPI app using **pip** as the package manager.

## Local development

1. **Set Up Virtual Environment**
```bash
python -m venv .venv
```
2. **Activate Virtual Environment**
```bash
.\.venv\Scripts\activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the Application**
```bash
python app.py
```
5. **Open the OpenAPI site**\
Navigate to the following url in the browser.
```bash
http://localhost:8000/docs
```

## Deployment to Azure App Service

1. **Install Azure vscode extension**
2. **Zip the needed files including the requirements.txt**
3. **Deploy the zip to Azure Web App**
4. **Set the following as the startup command in Settings and Configuration**
```bash
gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app:app
```