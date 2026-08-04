# centralgit

## Cursor Cloud specific instructions

This repo is a single self-contained static web app: `devops-8-week-plan.html` (an interactive 8-Week DevOps learning planner). There is no backend, no package manager, no build step, and no dependencies to install. All state is stored in the browser via `localStorage` (key `devops-plan-de-1h-v2`).

### Running the app (dev)

Serve the file over a static HTTP server (avoids `file://` quirks) from the repo root:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080/devops-8-week-plan.html`.

### Lint / test / build

There is no lint, automated test, or build tooling in this repo. "Testing" is manual: open the page, toggle task checkboxes, and confirm progress persists across a reload (via `localStorage`). Schedule rule: Mon–Sat = full 1-hour lessons; Sunday = rest (no micro/15-min mode).
