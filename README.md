# multiagent

A multi-agent system framework.

## Installation

```bash
pip install -r requirements.txt
```

## Development

```bash
pip install -r requirements-dev.txt
```

## Testing

```bash
pytest
```

## CI/CD

This repository includes two GitHub Actions workflows:

- **Build Pipeline** (`build.yml`): Runs on pushes to the main branch to verify the repository can be built and run
- **PR Pipeline** (`pr.yml`): Runs on pull requests to ensure PRs don't break the build

Both pipelines:
- Test against multiple Python versions (3.9, 3.10, 3.11, 3.12)
- Install dependencies
- Run linting (if configured)
- Run tests (if present)
- Build the package (if configured)