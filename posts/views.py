from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import NoteForm
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, "posts/note_list.html", {"notes": notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "posts/note_detail.html", {"note": note})

def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, "Your sticky note was created.")
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm()
    return render(request, "posts/note_form.html", {"form": form, "heading": "Create a sticky note"})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Your sticky note was updated.")
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, "posts/note_form.html", {"form": form, "heading": "Edit sticky note", "note": note})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        messages.success(request, "Your sticky note was deleted.")
        return redirect("note_list")
    return render(request, "posts/note_confirm_delete.html", {"note": note})
