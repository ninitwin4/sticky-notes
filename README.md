# 📝 Sticky Notes

> *A Django web application for creating and managing personal sticky notes, with per-user authentication so every note stays private to its owner.*


## 🌟 Highlights

- Full CRUD: create, read, update, and delete notes
- Per-user authentication — each user sees only their own notes
- Clean Model-View-Template (MVT) architecture with function-based views
- Tested with Django's built-in test framework
- Responsive styling for a simple, usable interface


## ℹ️ Overview

Sticky Notes is a Django application that lets a logged-in user capture quick notes — a title (optional) and a body — and manage them through a clean web interface. Notes are owned by individual users: when you log in, you see only your own notes, and attempting to reach another user's note by URL returns a 404. The project was built as part of the USF AI Engineering Bootcamp to demonstrate the MVT architecture, CRUD functionality, user authentication, and automated testing.

The data layer is a single `Note` model linked to Django's built-in `User` via a foreign key. Views are function-based for clarity, URLs are namespaced within the app, and templates extend a shared base layout.


### ✍️ Author

Built by Ni Ni — [github.com/ninitwin4](https://github.com/ninitwin4)


## 🚀 Usage

Once the server is running, sign up or log in, then create and manage your notes from the home page.

```
Sign up  →  Log in  →  Create a note  →  View / edit / delete your notes
```

Each user's notes are private to their account.


## ⬇️ Installation

Requires Python 3.10+ and Django.

```bash
# Clone the repository
git clone https://github.com/ninitwin4/sticky-notes.git
cd sticky-notes

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

To run the test suite:

```bash
python manage.py test
```


## 🔐 Authentication

Sticky Notes uses Django's built-in authentication to keep each user's notes private.

- **Sign up / log in** — users create an account and log in to access their notes.
- **Per-user ownership** — every note is tied to the user who created it via a foreign key.
- **Filtered views** — the notes list shows only the logged-in user's notes.
- **Access control** — requesting another user's note by URL returns a 404, and logged-out users are redirected to the login page.


## 💭 Future Enhancements

- Tags or categories for organizing notes
- Search and filtering across a user's notes
- Color-coded notes for a more authentic sticky-note feel
- Migration to a server-based database (e.g. MariaDB) for production
