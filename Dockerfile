FROM hugomods/hugo:exts

RUN apk add --no-cache \
    tmux \
    nodejs \
    npm \
    just

RUN npm install -g @anthropic-ai/claude-code

WORKDIR /src
EXPOSE 1313
