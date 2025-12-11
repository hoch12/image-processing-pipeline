# Project Issue Tracking

**Project:** Parallel Image Processing Pipeline  
**Document Date:** 2025-12-03   
**Author:** Dominik Hoch

This document maintains a record of known bugs, architectural limitations, and planned enhancements (feature requests).

## 🐛 Known Bugs & Limitations

These issues have been identified during testing and code review.

| ID          | Severity | Description | Status    |
|:------------| :--- | :--- |:----------|
| **BUG-001** | **High** | **Filename Collisions:** The pipeline saves files using only the filename stem. If input folders contain duplicate filenames in different subdirectories (e.g., `A/img.jpg` and `B/img.jpg`), the output file is overwritten by the last thread, causing data loss. | **TO DO** |
| **BUG-002** | **Medium** | **Lack of Input Validation:** The application crashes or behaves unexpectedly if invalid arguments are provided (e.g., negative integers for `--workers`). | **FIXED** |
| **BUG-003** | **Low** | **Silent Failure on Invalid Path:** If the provided `--input` path does not exist, the program runs successfully with 0 files instead of raising an error or warning the user. | **FIXED** |
| **BUG-004** | **Medium** | **Case-Sensitive Extension Filtering: On macOS and Linux, the glob pattern matching is case-sensitive. The loader currently searches for *.jpg or *.png, causing it to ignore files with uppercase extensions like Image.JPG or Photo.PNG. | **TO DO** |

---

## 💡 Feature Requests (Backlog)

Ideas for future improvements and user experience enhancements.

| ID | Type | Description                                                                                                                                     | Priority | Status    |
| :--- | :--- |:------------------------------------------------------------------------------------------------------------------------------------------------| :--- |:----------|
| **FEAT-001** | **UX** | **CLI Progress Bar:** Implement a visual progress bar (e.g., using `TQDM`) to indicate the percentage of completion during parallel processing. | Low | **DONE**  |
| **FEAT-002** | **Feature** | **Format Conversion:** Add a `--format` argument to allow converting images (e.g., JPEG to PNG, PNG to WebP) during the processing step.        | Medium | **TO DO** |