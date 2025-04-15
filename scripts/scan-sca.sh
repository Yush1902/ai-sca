#!/bin/bash
set -e

if ! command -v snyk &> /dev/null; then
    echo "Snyk CLI not found!"
    exit 1
fi

if [[ -z "$SNYK_TOKEN" ]]; then
    echo "SNYK_TOKEN not set."
    exit 1
fi

echo "Running Snyk scan..."
snyk test --all-projects --json > snyk_results.json
echo "Snyk scan complete. Results saved to snyk_results.json"
