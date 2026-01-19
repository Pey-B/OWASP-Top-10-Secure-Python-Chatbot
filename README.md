# OWASP Top 10 Secure Python Chatbot

## 📌 Project Overview

This project demonstrates the design, implementation, and security hardening of a **Python-based chatbot API** built in **Visual Studio Code**. The chatbot operates using a defined knowledge base and was intentionally secured against multiple **OWASP Top 10 Web Application Security Risks**.

The goal of this lab was to simulate a real-world API-backed chatbot service, then apply industry-standard security controls such as authentication, authorization, and input validation to prevent common attacks.

This repository is intended to showcase:
- Secure Python backend development
- API security best practices
- Practical OWASP Top 10 mitigation techniques
- Clear, auditable evidence of security controls in action

---

## 🧠 Key Features

- Python-based chatbot API
- Knowledge base–driven responses
- RESTful API with Swagger documentation
- JWT authentication
- Role-Based Access Control (RBAC)
- Input validation and injection protection
- Demonstrated protection against OWASP Top 10 risks

---

## 🛠️ Technology Stack

- **Language:** Python
- **Framework:** FastAPI
- **IDE:** Visual Studio Code
- **Authentication:** JSON Web Tokens (JWT)
- **Authorization:** Role-Based Access Control (RBAC)
- **API Documentation:** Swagger / OpenAPI
- **Security Focus:** OWASP Top 10

---

## 🚀 Application Functionality

The chatbot API accepts user queries and responds using a predefined knowledge base. Access to chatbot endpoints is restricted based on authentication and authorization controls.

### Example Flow:
1. User authenticates and receives a JWT
2. JWT is required for protected endpoints
3. RBAC enforces role-level permissions
4. Input validation prevents malicious payloads
5. Chatbot responds only to authorized, sanitized requests

---

## 🔐 Security Controls Implemented (OWASP Top 10)

This project directly addresses several OWASP Top 10 vulnerabilities:

### ✅ Broken Access Control
- Implemented **RBAC** to restrict access by role
- Unauthorized users are denied access to protected endpoints

### ✅ Identification & Authentication Failures
- Secure **JWT-based authentication**
- Token validation enforced on protected routes

### ✅ Injection
- Input validation and sanitization
- Injection attempts are rejected and logged

### ✅ Security Misconfiguration
- Explicit security middleware
- Protected API routes by default
- Swagger UI reflects authentication requirements

---

## 📸 Evidence & Screenshots

### Project Structure
![Project Structure](screenshots/01_project_structure.png)

### Server Running Successfully
![Server Running](screenshots/02_server_running.png)

### Swagger API
![Swagger Overview](screenshots/03_swagger_overview.png)

### JWT Token Issued
![JWT Token](screenshots/04_jwt_token.png)

### RBAC Enforcement – Access Denied
![RBAC Denied](screenshots/05_rbac_denied.png)
![RBAC Denied](screenshots/06_rbac_denied.png)

### Injection Attempt Blocked
![Injection Attempt](screenshots/07_injection_attempt.png)

### Knowledge Base Functionality
![Knowledge Base](screenshots/08_knowledge_base.png)


---



