import re

def scan_for_secrets(code_snippet: str) -> list:
    """
    Scans a given string of code for exposed secrets or hardcoded credentials.
    Returns a list of detected vulnerabilities.
    """
    vulnerabilities = []
    
    # Regex patterns for common secrets
    patterns = {
        "AWS Access Key": r"AKIA[0-9A-Z]{16}",
        "Generic API Key": r"(?i)(api_key|apikey|secret)(?:[\s=:>]*)(['\"][a-zA-Z0-9\-]{16,}['\"])",
        "Hardcoded Password": r"(?i)(password|passwd)(?:[\s=:>]*)(['\"][^'\"]{6,}['\"])"
    }

    for vulnerability_type, pattern in patterns.items():
        matches = re.finditer(pattern, code_snippet)
        for match in matches:
            vulnerabilities.append({
                "type": vulnerability_type,
                "matched_text": match.group(0),
                "severity": "HIGH",
                "recommendation": f"Remove the hardcoded {vulnerability_type} and use environment variables instead."
            })
            
    return vulnerabilities