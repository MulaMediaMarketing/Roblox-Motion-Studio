# Security Baseline

Kinetic Studio processes untrusted user files and generated motion data.

## Rules

- Treat uploaded videos, GLTF files, JSON, and imported assets as untrusted.
- Validate MIME type, extension, size, and parseability.
- Never execute uploaded content.
- Keep processing isolated from application secrets.
- Do not expose filesystem paths in API responses.
- Apply request and upload limits.
- Sanitize filenames and project identifiers.
- Keep temporary processing files isolated and disposable.
- Validate animation documents before export.
- Never trust client-side timing, joint names, or event payloads.
- Use server-side validation for backend operations.
- Log security-relevant failures without logging sensitive payloads.

## Future production controls

- authentication and authorization
- rate limiting
- job isolation
- resource quotas
- antivirus/content scanning where appropriate
- signed export artifacts
- dependency vulnerability scanning
- secret scanning
