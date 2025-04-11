def extract_vulnerable_packages(data):
    summary = []
    for project in data.get('projects', []):
        for vuln in project.get('vulnerabilities', []):
            pkg = vuln.get('packageName')
            ver = vuln.get('version')
            fix = vuln.get('fix', {}).get('versions', [])
            summary.append(f"Package: {pkg}, Version: {ver}, Fix versions: {fix}")
    return "\n".join(summary)
