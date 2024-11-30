# Hello world example for NiceGUI with the command pattern
This guide demonstrates how to set up a basic NiceGUI app using either **Poetry** or **pip** as the package manager.

---

## Option 1: Using Poetry

### Steps

1. **Install Poetry**
```bash
pip install poetry
```
2. **Configure Poetry**\
Set up the virtual environment to be inside the project directory
```bash
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "."
```
3. **Create and Activate Virtual Environment**  
```bash
poetry shell
```
4. **Install Dependencies**  
```bash
poetry install
```
5. **Run the Application**  
```bash
python src/app.py
```

---

## Option 2: Using pip

### Steps

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
python src/app.py
```