# Known Limitations

Version: 1.0

Status: Living Documentation

---

# Purpose

This document records the current known limitations of AI Studio.

A limitation is not necessarily a bug. It may be an intentional design decision, a feature that has not yet been implemented, or a temporary restriction.

---

# Current Limitations

## Local-Only Operation

The application is designed for local execution.

Cloud deployment is outside the current project scope.

---

## Filesystem Storage

Projects are stored on the local filesystem.

Database-backed persistence is not currently implemented.

---

## AI Model Availability

AI Studio depends on a compatible locally running AI model.

If no supported model is available, AI-assisted features cannot operate.

---

## Hardware Requirements

Large language models may require significant:

- RAM
- CPU resources
- GPU resources

Performance depends on the user's hardware.

---

## Browser Support

Development and testing focus on modern Chromium-based browsers.

Behavior on unsupported browsers is not guaranteed.

---

## Offline Model Management

Downloading and updating AI models is handled by external software.

AI Studio does not currently manage model installation.

---

## Project Compatibility

Backward compatibility for project data is maintained where practical but is not guaranteed across major architectural changes.

---

## Concurrent Editing

Simultaneous editing of the same project from multiple browser sessions is not currently supported.

---

# Future Improvements

Potential future enhancements include:

- Improved AI abstraction
- Better project migration tools
- Additional validation
- Improved recovery from interrupted operations
- Enhanced performance optimization

---

# Reporting Limitations

When documenting a newly discovered limitation, include:

- Description
- Impact
- Workaround (if available)
- Related milestone
- Current status

---

# Maintenance

Remove limitations from this document once they have been resolved and documented in the corresponding milestone and changelog.

---

End of Known Limitations.