FROM hugomods/hugo:exts

RUN apk add --no-cache \
    git-lfs \
    github-cli \
    bash \
    tmux \
    nodejs \
    npm \
    ripgrep \
    just \
    python3 \
    py3-pip \
    lazygit

RUN npm install -g @anthropic-ai/claude-code

WORKDIR /src
EXPOSE 1313
