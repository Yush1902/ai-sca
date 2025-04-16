#!/bin/bash
set -e

if ! command -v snyk &> /dev/null; then
    echo "Snyk CLI not found. Please install it with 'npm install -g snyk'"
    exit 1
fi

if [[ -z "9e77ee4e-a024-45d9-9e14-ad561566c104" ]]; then
    echo "SNYK_TOKEN not set. Export it with 'export SNYK_TOKEN=your-token'"
    exit 1
fi

echo "Authenticating with Snyk..."
snyk auth "9e77ee4e-a024-45d9-9e14-ad561566c104"

echo "Running Snyk scan..."
snyk code test > snyk_results.json || {
    echo "Snyk scan failed. Check snyk_results.json or run with --debug for more details."
    exit 1
}

echo "Snyk scan complete. Results saved to snyk_results.json"