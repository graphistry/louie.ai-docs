#!/bin/bash
set -ex

DOCS_FORMAT=${DOCS_FORMAT:-all}  # Default to building all formats if not specified

(
    cd infra \
    && docker compose build \
    && docker compose run --rm -e DOCS_FORMAT=$DOCS_FORMAT sphinx
)
