# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the runtime entrypoint for the game loop.
- Core runtime state and types live in `data/runtime/` and `data/types/`.
- Gameplay logic sits in `logic/`, while rendering/UI is in `view/`.
- State flow and screen routing live in `state/`, with helpers in `collaborator/`.
- Constants and definitions are split across `constants/` and `defs/`.
- Assets are under `assets/` (e.g., `assets/characters/<name>/` and `assets/stages/<stage>/`).
- Configuration is in `config/` and `config.json`.
- Documentation sources are in `source/` with built docs under `build/`.

## Build, Test, and Development Commands
- `./init.sh` creates `venv/`, installs `requirements.txt`, and runs the game.
- `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt` sets up the environment manually.
- `python3 main.py` runs the game loop directly.
- `make html` builds Sphinx docs from `source/` into `build/`.

## Coding Style & Naming Conventions
- Use 4-space indentation and keep the existing type-hint style.
- Prefer `snake_case` for functions/variables and `PascalCase` for classes.
- Constants are uppercase and live in `constants/` (e.g., `SCREEN_WIDTH`).
- New modules should follow the existing `snake_case.py` pattern.
- Asset naming follows motion/state labels like `STAND.gif`, `JUMP.gif`.

## Testing Guidelines
- No automated test framework is configured; testing is manual via `python3 main.py`.
- If you add tests, document the runner and conventions here for consistency.

## Commit & Pull Request Guidelines
- Commit history uses short, descriptive summaries (often in Japanese); keep messages brief and action-oriented.
- PRs should include: change summary, how to run locally, and screenshots/GIFs for visual changes.
- Link any related issues or design notes when available.

## Architecture Notes
- See `ARCHITECTURE.md` for the intended separation of specs vs runtime state and dependency direction.
- Keep rendering concerns in `view/` and avoid coupling gameplay logic directly to assets.
