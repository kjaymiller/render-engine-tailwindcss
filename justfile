_default:
  just --list

test:
  uv run pytest tests/ -v

test-coverage:
  uv run pytest tests/ -v --cov=render_engine_tailwindcss --cov-report=term-out

check:
  just test

release version:
  gh release create {{version}} --generate-notes

prelease version:
  gh release create {{version}} -p --generate-notes
