# Sticky Notes Application — Design Diagrams

These Mermaid diagrams can be rendered in Markdown viewers that support Mermaid.

## 1. Use-case diagram
```mermaid
flowchart LR
    User([User])
    subgraph App[Sticky Notes Application]
      List((View all notes))
      Detail((View note details))
      Create((Create note))
      Edit((Update note))
      Delete((Delete note))
    end
    User --> List
    User --> Detail
    User --> Create
    User --> Edit
    User --> Delete
```

## 2. Create-note sequence diagram
```mermaid
sequenceDiagram
    actor User
    participant Browser as Template / Browser
    participant View as Django View
    participant Form as NoteForm
    participant Model as Note Model
    participant DB as SQLite Database
    User->>Browser: Open new-note page
    Browser->>View: GET /notes/new/
    View-->>Browser: Render empty form
    User->>Browser: Submit title, content, author
    Browser->>View: POST form data
    View->>Form: Validate submitted data
    Form-->>View: Valid form
    View->>Model: Save note
    Model->>DB: INSERT note
    DB-->>Model: Saved record
    View-->>Browser: Redirect to note list
    Browser-->>User: Show saved note
```

## 3. Model/class diagram
```mermaid
classDiagram
    class Note {
      +int id
      +str title
      +str content
      +str author
      +datetime created_at
      +datetime updated_at
      +str __str__()
    }
```

## 4. Request flow
```mermaid
flowchart TD
    A[User action] --> B[Django URL router]
    B --> C[View function]
    C --> D[Validate NoteForm]
    D -->|Valid| E[Note model / SQLite]
    D -->|Invalid| F[Re-render form with errors]
    E --> G[Redirect or render template]
    F --> G
    G --> H[HTML response to user]
```

## Component responsibilities
- **Model (`posts/models.py`)**: defines the note fields and database representation.
- **View (`posts/views.py`)**: receives requests, processes forms and chooses responses.
- **Template (`posts/templates/`)**: renders the pages and note information as HTML.
- **URL configuration**: maps browser paths to the correct view.
- **Form (`posts/forms.py`)**: validates user-entered data before it is saved.
