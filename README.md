**<u>SecureVault:</u>**

A secure file storage and auditing system built with Python.  
SecureVault encrypts uploaded files, stores metadata securely, and maintains tamper-evident audit logs for forensic analysis.

**<u>Features:</u>**

- AES-based file encryption
- Secure authentication with bcrypt password hashing
- Role-Based Access Control (Admin, Analyst, Viewer)
- MySQL database storage for file metadata
- Tamper-evident forensic audit logs
- Web dashboard built with Flask
- Encrypted file upload and storage
- SHA-256 file integrity verification

**<u>System Architecture:</u>**

User → Flask Web Server → Encryption Engine → MySQL Database  
↓  
Audit Logger → Hash Chain Logs

**<u>Technologies Used:</u>**

- Python
- Flask
- MySQL
- Cryptography (AES encryption)
- bcrypt (password hashing)
- Git & GitHub

**<u>Project Structure:</u>**

```text
SecureVault/
│
├── app.py
├── auth.py
├── encryption.py
├── database.py
├── audit.py
│
├── templates/
│   └── index.html
│
├── uploads/
├── logs/
│   └── audit_log.json
│
└── README.md
```
