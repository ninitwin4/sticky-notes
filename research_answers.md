# 1. How HTTP applications preserve state across request-response cycles

HTTP is "stateless" like a cinema usher with no memory - it cannot naturally remember who you are between interactions. To fix this, we use a system mirroring a movie theater's entry process.

When you log in, the server verifies your credentials. Once confirmed, it issues you a "ticket", known as a session cookie. This is a small piece of data your browser stores. Just as showing your ticket at the gate allows you to leave for popcorn and return without re-buying entry, your browser automatically presents this cookie with every subsequent request.

Crucially, the ticket holds only a number — a session ID — not your actual identity. The server maintains a private "ledger" (a session) that links your specific ticket number to your user identity and data, which stays safely server-side. When you present your cookie, the server checks its ledger, recognizes you, and grants access to your profile or cart without requiring a password again.

This setup creates the illusion of a continuous conversation. If you log out, the server "voids" your ticket in its ledger, ensuring that the cookie in your browser is no longer valid, effectively ending your session.


# 2. Procedures for performing Django database migrations to a server-based relational database like MariaDB.

Think of Django migrations as updating the blueprints for our cinema. The workflow itself is identical to working with SQLite — what changes is the destination.

First, you prepare the connection. Install a MariaDB driver (`mysqlclient`), then update the `DATABASES` setting in `settings.py` to use the `django.db.backends.mysql` engine, pointing it at your production credentials (host, port, database name, user, password). Make sure that database and user already exist on the MariaDB server before migrating. Then the familiar two-step runs:

- **Model Definition:** You define your building requirements (e.g., "add a snack bar") in your code.
- **Migration Files:** Run `python manage.py makemigrations`. This genrates the "Change Order" - a document detailing the exact structural modifications needed.
- **Execution:** Run `python manage.py migrate`. This is your construction crew applying those changes to the MariaDB database.
This process relies on a special tracking table that records which change orders are already completed, ensuring the crew doesn't rebuild existing rooms. Always back up the database before migrating in production, and treat migration files as immutable historical records — never edit them manually. Consistency between your code's blueprints and the database's structure is vital for stability.