from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import NoteForm
from .models import Note


@login_required
def note_list(request):
    """Display the logged-in user's notes, newest first."""
    notes = request.user.notes.all().order_by("-updated_at")
    return render(request, "notes/note_list.html", {"notes": notes})


@login_required
def note_detail(request, pk):
    """Display one of the user's notes, or 404."""
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(
        request, "notes/note_detail.html", {"note": note}
    )


@login_required
def note_create(request):
    """Show a blank form then save a new note on POST."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """Edit an existing note via a pre-filled form."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """Show a confirmation page before deleting a note."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})


def signup(request):
    """Register a new user, then log them in."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the new user in right after they register
            login(request, user)
            return redirect("note_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
