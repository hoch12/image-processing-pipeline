# Project Issue Tracking

**Project:** Parallel Image Processing Pipeline  
**Document Date:** 2025-12-03   
**Author:** Dominik Hoch

This document maintains a record of known bugs, architectural limitations, and planned enhancements (feature requests).

## 🐛 Known Bugs & Limitations

These issues have been identified during testing and code review.

| ID          | Severity | Description | Status    |
|:------------| :--- | :--- |:----------|
| **BUG-001** | **High** | **Filename Collisions:** The pipeline saves files using only the filename stem. If input folders contain duplicate filenames in different subdirectories (e.g., `A/img.jpg` and `B/img.jpg`), the output file is overwritten by the last thread, causing data loss. | **To Do** |
| **BUG-002** | **Medium** | **Lack of Input Validation:** The application crashes or behaves unexpectedly if invalid arguments are provided (e.g., negative integers for `--workers`). | **To Do** |
| **BUG-003** | **Low** | **Silent Failure on Invalid Path:** If the provided `--input` path does not exist, the program runs successfully with 0 files instead of raising an error or warning the user. | **To Do** |

---

## 💡 Feature Requests (Backlog)

Ideas for future improvements and user experience enhancements.

| ID | Type | Description | Priority |
| :--- | :--- | :--- | :--- |
| **FEAT-001** | **UX** | **CLI Progress Bar:** Implement a visual progress bar (e.g., using `tqdm`) to indicate the percentage of completion during parallel processing. | Low |
| **FEAT-002** | **Feature** | **Format Conversion:** Add a `--format` argument to allow converting images (e.g., JPEG to PNG, PNG to WebP) during the processing step. | Medium |