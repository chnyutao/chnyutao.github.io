#!/bin/bash

SRC_DIR="$(dirname $0)"
DEST_DIR="$SRC_DIR/../public/typst"

find "$SRC_DIR" -type f -name "*.typ" | while read -r source; do
    filename="${source#$SRC_DIR/}"
    target="$DEST_DIR/${filename%.typ}.pdf"
    mkdir -p "$(dirname "$target")"
    typst compile "$source" "$target"
done
