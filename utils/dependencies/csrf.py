from fastapi import Request, HTTPException, status, Form
import secrets


def generate_csrf_token(request: Request):
    csrf_token = request.session.get("csrf_token")
    if not csrf_token:
        csrf_token = secrets.token_urlsafe(16)
        request.session["csrf_token"] = csrf_token
    return csrf_token


def verify_csrf_token(request: Request, csrf_token: str = Form(...)):
    session_csrf_token = request.session.get("csrf_token")
    if not session_csrf_token or session_csrf_token != csrf_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid CSRF token")
    return True
