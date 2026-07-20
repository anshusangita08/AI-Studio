---
Status: Active
Generated From: Source Code
Last Reviewed: 2026-07-20
---

# AI Studio Architecture

## High Level Architecture

- **Entry point**: `run.bat` → `launcher.py`.
- **Server start**: `uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)` starts a FastAPI app.
- **FastAPI lifespan**: On startup, the async context manager `lifespan` logs *Starting AI Studio*, calls `bootstrap.initialize()`, and on shutdown logs *Stopping AI Studio*.
- **Bootstrap initialization**:
  - Creates workspace directories (`app.core.workspace.WorkspaceManager`).
  - Loads configuration from `config/default.json` via `app.core.config.Config.load()`.
  - Validates environment requirements (`app.hardware.requirements.validate_environment`).
- **UI startup**: FastAPI mounts static files under `/static` and includes routers for projects and story routes. The UI templates are served by the FastAPI app.
- **Shutdown flow**: Not implemented beyond the lifespan context manager's final log statement. No explicit cleanup actions.

## Folder Structure
- **.`app`** – Core application package.
  - *Responsibility*: Hosts the FastAPI app instance, bootstrap logic, service definitions, hardware checks, UI routing, and shared utilities. It is the central runtime component that orchestrates request handling and background tasks.
  - *Owner*: Application.
  - *Depends on*: `config`, `services`, `core`, `ui` modules.
  - *Used by*: All runtime paths – API handlers, background workers, and any module that requires application state.
- **.`config`** – Configuration package.
  - *Responsibility*: Provides access to default configuration data and exposes a loader for environment‑specific overrides. It supplies configuration objects used during bootstrap.
  - *Owner*: Configuration.
  - *Depends on*: None.
  - *Used by*: `app.core.config.Config`, bootstrap initialization.
- **.`docs`** – Documentation package.
  - *Responsibility*: Stores architectural diagrams, guides, and milestone notes. It is read‑only from the application perspective.
  - *Owner*: Documentation.
  - *Depends on*: None.
  - *Used by*: Developers, CI documentation generators.
- **.`tests`** – Test suite package.
  - *Responsibility*: Contains unit and integration tests exercising application logic. It imports the public API of `app`, `services`, and `core` for validation.
  - *Owner*: Tests.
  - *Depends on*: `app`, `services`, `core` modules.
  - *Used by*: Test runners such as pytest.
- **.`run.bat` / `launcher.py`** – Entry‑point scripts.
  - *Responsibility*: Bootstrap the Uvicorn server and expose command‑line entry points for developers and CI pipelines.
  - *Owner*: Infrastructure.
  - *Depends on*: `app.app` module.
  - *Used by*: End users, automated deployment scripts.
- **`.git`, `.clinerules`, `.continue`** – Repository tooling files.
  - *Responsibility*: Store Git metadata and CLI helper definitions. They are external to the application runtime.
  - *Owner*: Infrastructure.
  - *Depends on*: None.
  - *Used by*: Developers, version control system.
- **`bootstrap.py`** – Application bootstrapper.
  - *Responsibility*: Exposes a `main()` entry point that orchestrates application start‑up and shutdown. It wires together configuration, services, and the FastAPI app.
  - *Owner*: Application.
  - *Depends on*: `launcher` module.
  - *Used by*: CI scripts, local development commands.
- **`LICENSE`, `README.md`, etc.** – Project metadata files.
  - *Responsibility*: Provide legal and informational context for the project. They are static assets.
  - *Owner*: Documentation.
  - *Depends on*: None.
  - *Used by*: Developers, users, documentation generators.

## Dependency Injection

- **Container**: `app.core.container.Container` is a simple registry that stores service instances keyed by name.
- **Registration**: Services are registered via `container.register(name, instance)`. Duplicate names raise a `ValueError`.
- **Service resolution**: `container.resolve(name)` retrieves the stored instance; an unknown name raises a `KeyError`.
- **Singleton behavior**: The container holds one instance per service name; it does not create new instances on each resolve, thus enforcing singleton semantics for registered services.
- **Lifecycle**: Services are added during bootstrap (`bootstrap.initialize()`) and can be cleared with `container.clear()` (not used in the current flow). No automatic disposal or scoped lifetimes are implemented.

## Service Registry

- **Registry**: `app.services.service_registry.ServiceRegistry` keeps a mapping of service names to instantiated objects.
- **Startup order**: Services are registered during the bootstrap phase via `services.register(name, instance)`. The current code registers services in whatever order the bootstrap logic executes; there is no explicit ordering mechanism beyond that.
- **Shutdown order**: No shutdown sequence is defined. The registry simply holds references until the process exits or `clear()` is called (not used in the current flow).
- **Service lookup**: `services.get(name)` returns the instance, while `get_optional(name)` returns `None` if missing.
- **Error handling**: `get(name)` raises a standard `KeyError` if the service name is unknown; other methods silently ignore missing keys (`unregister`, `clear`).

## Application Lifecycle
+
+The application lifecycle is managed by FastAPI's lifespan context manager defined in `app/app.py`.
+
+### Startup sequence
+1. The FastAPI app starts and enters the `lifespan` async context manager.
+2. A log message *Starting AI Studio* is emitted via `app.core.logging.logger`.
+3. `bootstrap.initialize()` is called.  This function currently **does not exist** in the codebase; the call is present but will raise an AttributeError at runtime if executed.  Therefore, no actual bootstrap actions occur.
+
+### Service initialization
+There are no services registered or initialized during startup – the service registry and container are defined elsewhere but never populated in the current flow.
+
+### Router registration
+The FastAPI app mounts static files under `/static` and includes two routers:
+- `app.ui.routes_projects.router` (mounted at the root via `include_router`).
+- `app.ui.routes_story.router` (also mounted at the root).
+These routes provide project and story related endpoints.
+
+### FastAPI lifespan
+The `lifespan` context manager is responsible for logging on startup and shutdown.  It yields control to allow the application to run, then logs *Stopping AI Studio* upon exit.
+
+### Shutdown behavior
+Only a log statement *Stopping AI Studio* is executed; no explicit cleanup or service disposal occurs.
+
+Any functionality that would normally be performed during bootstrap (workspace creation, config loading, environment validation) is **not implemented** in the current codebase.

## Project Lifecycle

Project lifecycle management is currently limited.

The application can load and persist project-related content through the existing services and routes, but it does not yet implement a dedicated lifecycle manager responsible for project creation, opening, closing, event propagation, or state transitions.

These responsibilities are expected to evolve in future milestones.

If future development adds such functionality (e.g., a `ProjectManager` service or REST endpoints), this section should be updated accordingly.

## Story Pipeline

### User Request
The user interacts with the story editor UI which sends HTTP requests to endpoints under `/projects/{slug}/story*`. The actions include viewing, generating, and saving story, expanded story, and scenes.

### Route
FastAPI routes defined in `app/ui/routes_story.py`:
- `GET /projects/{slug}/story` – Render the story page with current content.
- `POST /projects/{slug}/story/generate` – Generate mock story based on expanded story; returns JSON if AJAX or renders template.
- `POST /projects/{slug}/story` – Save story content (form field `content`).
- `POST /projects/{slug}/expanded-story` – Save expanded story content.
- `POST /projects/{slug}/scenes` – Save scenes content.
- `POST /projects/{slug}/scenes/generate` – Generate mock scenes from expanded story; returns JSON or renders template.

### Service
All operations delegate to an instance of `StoryService` (from `app/services/story_service.py`). The service handles file path resolution, reading, writing, and generating placeholder content.

### Persistence
The `StoryService` persists data as plain Markdown files under the project workspace:
- `story.md` – main story.
- `expanded_story.md` – expanded version used for generation.
- `scenes.md` – scenes derived from the expanded story.
Directories are created on write if missing.

### Response
For GET requests, a Jinja2 template `projects/story.html` is rendered with context containing project data and current story/expanded_story/scenes content. For POST generate routes, JSON payloads (`{"expanded_story": ...}` or `{"scenes": ...}`) are returned for AJAX calls; otherwise the same template is rendered with updated context. Successful save POSTs redirect to `/projects/{slug}/story` using a 303 status.

### Error Handling
- If the project slug does not exist, `_get_project_or_404` raises `HTTPException(404)`.
- File I/O failures in `StoryService.save_*` methods return `False`; routes translate this to `HTTPException(500)` with an appropriate detail message.
- JSON generation endpoints check the `Content-Type` header for AJAX; if not matched they fall back to template rendering.
No other error handling is present.

## Scene Pipeline

The current scene pipeline is implemented as part of `StoryService` rather than as a dedicated subsystem.

### Generation

Scenes are generated from the expanded story using placeholder/mock generation logic.

### Persistence

Generated scenes are stored as Markdown within the project workspace (`scenes.md`).

### Retrieval

Scene content is loaded from disk whenever the Story page is opened.

### API

Scene generation and persistence are exposed through the story routes in `app/ui/routes_story.py`.

### Current Limitations

- No dedicated SceneService.
- No scene validation.
- No incremental regeneration.
- No dependency graph between scenes.

## LM Studio Integration

LM Studio integration exists through `app.core.lm_studio_client`.

The client provides communication with a locally running LM Studio server using the OpenAI-compatible API.

Current responsibilities include:

- connection management
- health checks
- text generation
- timeout handling
- error propagation

Current story generation still relies primarily on mock generation. Full LM Studio integration is planned for a later milestone.

## HTMX/UI Interaction

The web interface is implemented using FastAPI, Jinja2 templates and client-side JavaScript.

Request flow:

1. User interacts with the Story page.
2. Browser submits GET or POST requests.
3. FastAPI routes invoke the appropriate service.
4. Updated data is returned either as HTML or JSON.
5. The browser updates the visible UI.

Current implementation uses server-rendered templates with lightweight client-side interactions. There is no complex frontend state management.

## Testing Architecture

Testing is performed using pytest.

Current test coverage includes:

- service layer
- project management
- story routes
- persistence logic

Tests use isolated temporary workspaces where appropriate.

External services such as LM Studio are mocked where required.

The current test suite focuses primarily on unit testing with a limited number of integration tests.

