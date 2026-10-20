# Sticky Notes Application — Part 2

A Django sticky-notes application with create, read, update and delete (CRUD)
features, form validation, responsive styling, and automated unit tests.

## Requirements
- Python 3.10 or newer
- pip

## Setup (Windows PowerShell, VS Code terminal)
1. Open this folder in VS Code.
2. Create a virtual environment:
   ```powershell
   py -m venv venv
   ```
3. Activate it:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use `venv\Scripts\activate.bat` in Command Prompt.
4. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Create and apply database migrations:
   ```powershell
   python manage.py makemigrations posts
   python manage.py migrate
   ```
6. Run the automated tests:
   ```powershell
   python manage.py test posts
   ```
7. Start the website:
   ```powershell
   python manage.py runserver
   ```
8. Open http://127.0.0.1:8000/ in your browser.

The `venv` directory is intentionally not included in this submission. Django
will create the SQLite database after `migrate`.

## Features
- View all sticky notes and open an individual note.
- Create a note with title, content and author.
- Edit and delete notes (deletion requires a confirmation page).
- Input validation and useful empty-state messages.
- Django tests for model fields, list/detail views, create/update/delete flows,
  invalid form submissions and missing notes.
- Responsive CSS stored in `posts/static/posts/style.css`.

## Design diagrams
See `docs/design_diagrams.md` for the use-case, flow and model diagrams.

## GitHub submission
1. Create a **public** repository on GitHub, e.g. `django-sticky-notes`.
2. From this folder run:
   ```powershell
   git init
   git add .
   git commit -m "Complete Django sticky notes application with tests"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/django-sticky-notes.git
   git push -u origin main
   ```
3. Replace the placeholder in `sticky_github.txt` with your actual public repository URL.
4. Do not upload the virtual environment or `db.sqlite3`.
