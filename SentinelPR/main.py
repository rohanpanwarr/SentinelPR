from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from scanner import scan_for_secrets

app = FastAPI(title="DevSecOps PR Scanner")

# 1. Yeh class FastAPI ko batayegi ki hume kis tarah ka data chahiye
class WebhookPayload(BaseModel):
    title: str = "Test PR"
    body: str = "Fixing bugs. My api_key=AKIAIOSFODNN7EXAMPLE and password=mysecretpassword"

@app.get("/")
def read_root():
    return {"status": "Scanner is online. Send POST requests to /webhook."}

@app.post("/webhook")
async def github_webhook(payload: WebhookPayload):
    """
    Endpoint to receive GitHub pull request payloads.
    """
    # Ab FastAPI khud hi data ko parse aur validate kar lega
    pr_title = payload.title
    pr_body = payload.body

    # Run the security scan on the PR content
    scan_results = scan_for_secrets(pr_body)

    # Determine the status based on findings
    if scan_results:
        status = "FAILED"
        message = f"Security scan failed for '{pr_title}'. Vulnerabilities found."
    else:
        status = "PASSED"
        message = f"Security scan passed for '{pr_title}'. No secrets detected."

    # Return the automated security report
    return {
        "status": status,
        "message": message,
        "vulnerabilities": scan_results
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)