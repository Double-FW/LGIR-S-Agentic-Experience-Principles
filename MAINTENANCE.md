# Maintain the repository

The editable canonical records for generated pages are in data/. The specification, Understanding pages and eight case pages are derived views. Other documentation is independently authored guidance. Keep both representations aligned and preserve source/criterion identity.

From the repository root, a maintainer can run:

```bash
python scripts/render_documents.py
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

These commands use Python's standard library. They perform no live agent actions or external publication. The checker validates the record constraints documented in VALIDATION.md; it is not a complete JSON Schema engine or an implementation of the LGIR+S criteria.

Review sources after relevant standards/protocol changes, corrected evidence or a material question. Confirm public availability before adding a Double-FW dependency. Preserve exact inspected revisions and qualification; a changed link alone does not establish a changed meaning or updated legal verification.

Use versioned editorial releases and record material changes. Do not reuse a retired criterion ID for another meaning. Any future pilot report must name the actual scope, evidence, reviewer and limitations. Keep operational evidence in approved controlled systems.

A weekly Hugging Face export workflow is provided; see [setup](huggingface/SETUP.md). It exports committed documentation without changing adopted requirements or reviewing external sources. Configuration and a successful publication run must be verified separately. No agent monitoring service or product evaluation is provided.
