# Project Service Refactor

The application uses a module‑level `ProjectService` instance (`project_service = ProjectService()`) for production compatibility.  Tests instantiate isolated `ProjectService` instances with configurable project roots (typically `tmp_path / "projects"`), ensuring all filesystem operations occur inside temporary directories.  This preserves production behavior while eliminating filesystem side effects during automated testing.
## Recommended Local Model
Development and testing are currently performed using `openai/gpt-oss-20b` through LM Studio. Other OpenAI‑compatible models may work, but GPT‑OSS‑20B is the reference model used during ongoing development and testing.

> Note: Qwen3 was previously used during early development.

