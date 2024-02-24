# Image source code: https://github.com/axonasif/workspace-images/tree/tmp
# Also see: https://github.com/gitpod-io/workspace-images/issues/1071
FROM axonasif/workspace-python@sha256:f5ba627a31505ea6cf100abe8e552d7ff9e0abd6ba46745b6d6dab349c001430

RUN pyenv install 3.10 \
    && pyenv global 3.10