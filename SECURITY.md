# Security Policy

## Supported Versions

The following versions of NIDS are currently supported with security updates:

| Version | Supported          |
| ------- | :----------------: |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

## Reporting a Vulnerability

If you discover a security vulnerability in NIDS, please report it responsibly:

### DO NOT:
- Create a public GitHub issue for the vulnerability
- Share vulnerability details publicly
- Exploit the vulnerability for any purpose

### DO:
1. **Email the maintainers privately** with:
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (if you have one)

2. **Include details such as**:
   - Affected version(s)
   - Your contact information
   - Timeline expectations (reasonable disclosure timeline)

3. **Wait for acknowledgment** from the maintainers
   - We will respond within 48 hours
   - We will keep you updated on the fix progress

### Responsible Disclosure Timeline

- **Day 0**: Vulnerability reported
- **Day 1**: Initial response and acknowledgment
- **Day 7**: Expected initial assessment
- **Day 30**: Target patch release date
- **Day 90**: Public disclosure (if patch is not yet released)

## Security Best Practices

When using NIDS, please follow these security best practices:

### 1. Data Protection
- Ensure training data is kept secure and private
- Use encryption for sensitive network data
- Follow data protection regulations (GDPR, CCPA, etc.)

### 2. Model Security
- Store trained models securely
- Restrict access to `models/` directory
- Use access controls and authentication if deploying as a service

### 3. Dependency Management
- Keep dependencies updated regularly
- Review security advisories for dependencies
- Use `pip audit` to check for known vulnerabilities:
  ```bash
  pip install pip-audit
  pip-audit
  ```

### 4. Deployment Security
- Never expose the Streamlit interface to the public internet without authentication
- Use HTTPS when deploying
- Implement proper network security controls
- Run with minimal required privileges

### 5. Code Security
- Validate all inputs
- Avoid using untrusted data in model inference
- Keep the application logs secure
- Monitor for suspicious activities

## Dependency Security

This project uses the following key dependencies:
- **Streamlit**: Web interface framework
- **scikit-learn**: ML algorithms
- **Pandas**: Data processing
- **NumPy**: Numerical computing
- **Joblib**: Model serialization
- **Scapy**: Network packet handling (optional)

All dependencies are pinned to secure versions in `requirements.txt`. Update dependencies regularly:

```bash
# Check for updates
pip list --outdated

# Update all packages
pip install --upgrade -r requirements.txt
```

## Vulnerability Disclosure

Resolved vulnerabilities will be documented in:
- The `CHANGELOG.md` file
- Release notes
- Security advisory announcements (if applicable)

## Security Headers and Configuration

### For Streamlit Deployment
Add these security best practices:

```bash
# Run with restricted permissions
streamlit run app.py --logger.level=info

# Use environment variables for sensitive data
export MODEL_PATH=./models/best_model.joblib
export DATA_PATH=./data/
```

### For Production Deployment
- Use a reverse proxy (nginx, Apache)
- Enable HTTPS/TLS
- Implement rate limiting
- Add authentication/authorization
- Monitor and log access
- Use Web Application Firewall (WAF)

## Questions or Concerns

For security-related questions (not vulnerabilities), please:
1. Check the documentation
2. Open a private security advisory (GitHub feature)
3. Contact the maintainers through the responsible disclosure process

---

Thank you for helping keep NIDS secure! 🛡️
