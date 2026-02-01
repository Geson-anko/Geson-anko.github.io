FROM hugomods/hugo:exts

RUN apk add --no-cache \
    bash \
    tmux \
    nodejs \
    npm \
    just \
    python3 \
    py3-pip \
    lazygit

RUN npm install -g @anthropic-ai/claude-code

WORKDIR /src
EXPOSE 1313
