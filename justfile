# Hugo blog development commands

# Install dependencies and setup pre-commit
setup:
    pip install pre-commit
    pre-commit install
    git submodule update --init --recursive

# Start development server
up:
    docker compose up -d

# Stop containers
down:
    docker compose down

# Production build
build:
    docker compose run --rm hugo --minify

# Create new post (usage: just new blog/my-post)
new path:
    docker compose run --rm hugo new content/{{path}}/index.md

# Open shell in container
shell:
    docker compose exec hugo sh

# Start tmux session in container
tmux:
    docker compose exec hugo tmux

# Run Claude Code in container
claude:
    docker compose exec hugo claude

# Format files with Prettier
format:
    npx prettier --write "content/**/*.md" "config/**/*.toml" "**/*.yaml" "**/*.json"

# Run pre-commit on all files
lint:
    pre-commit run --all-files
