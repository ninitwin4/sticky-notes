# Manual Testing Checklist — Sticky Notes

## Setup
- [ ] Two accounts exist (testuser01 and testuser02), each with notes.

## Two-user isolation
- [ ] Log in as testuser01 → list shows only testuser01's notes.
- [ ] Log out, log in as testuser02 → list shows only testuser02's notes.
- [ ] testuser01's notes are never visible to testuser02, and vice versa.

## Cross-user 404
- [ ] As testuser01, note the URL of one of its notes (e.g. /note/1/).
- [ ] Log in as testuser02 and visit that same URL → page returns 404.

## Logged-out redirect
- [ ] Log out completely.
- [ ] Visit / (list) → redirected to the login page.
- [ ] Visit /note/new/ (create) → redirected to the login page.

## CRUD as owner
- [ ] Create a note → it saves and shows in your list.
- [ ] Edit it → change persists; "Updated" timestamp moves.
- [ ] Delete it → confirmation page → removed from list.
