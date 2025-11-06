#!/bin/bash
# Simple script to watch for file changes and rebuild docs
# Usage: ./watch-and-build.sh

echo "Watching for changes in source/..."
echo "Press Ctrl+C to stop"
echo ""
echo "View docs at: http://localhost:8000"
echo ""

# Initial build
make html

# Watch for changes (macOS uses fswatch if available, otherwise falls back to simple loop)
if command -v fswatch &> /dev/null; then
    fswatch -o source/ | while read change; do
        echo "Changes detected, rebuilding..."
        make html
        echo "Build complete! Refresh your browser."
    done
else
    echo "Note: Install fswatch for better file watching: brew install fswatch"
    echo "Falling back to periodic rebuild (every 3 seconds when you save)"
    echo ""

    LAST_MTIME=$(find source -type f -name "*.md" -o -name "*.rst" | xargs stat -f "%m" | sort -nr | head -1)

    while true; do
        sleep 3
        CURRENT_MTIME=$(find source -type f -name "*.md" -o -name "*.rst" | xargs stat -f "%m" | sort -nr | head -1)

        if [ "$CURRENT_MTIME" != "$LAST_MTIME" ]; then
            echo "Changes detected, rebuilding..."
            make html
            echo "Build complete! Refresh your browser."
            LAST_MTIME=$CURRENT_MTIME
        fi
    done
fi
