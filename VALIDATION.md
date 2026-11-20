# Validation and review boundary

Version 0.1.0 · 20 November 2026

Result: the repository integrity checker and all thirteen regression tests passed. These results concern documentation/data integrity, not agentic effectiveness or product conformance.

## What the local checks cover

- Five named principles and preservation of the exact owner-supplied Agentic Robustness definition.
- Twenty-five distinct candidate criterion IDs and their required context fields.
- Eight fictional case records, with five-principle applications and explicit Not evaluated status.
- Valid source, example and technique references and recorded public/pinned Double-FW source relationships.
- Agreement between canonical records and generated specification, Understanding, technique and case views.
- Relative Markdown destinations and fragments outside fenced literal examples.
- Four synthetic operation examples, basic record fields/enums and selected invariants for unknown outcomes, completion evidence, no-effect claims and recovery limits.

The regression suite checks a valid package and deliberately introduces a missing Satisfactory principle, empty principle list, changed owner definition, dangling source, false product result, false WCAG-tier claim, fictional case presented as real, stale generated page, broken link, unsafe retry in the conservative example profile, false undo and missing completion evidence.

## What these checks do not cover

They do not implement or evaluate an agent, verify real provider events, authenticate approval, validate the complete JSON Schema language, perform a live audit of every external URL, establish WCAG conformance, determine legal applicability or prove that LGIR+S improves experience. Passing synthetic-record checks is not production recovery evidence.

External primary reference pages and seven public Double-FW documents were inspected for this edition. The latter are recorded at exact commits. This is selected-source review, not an exhaustive audit of all linked content. Protocol versions are pinned examples rather than claims about the latest versions.

No participant study, benchmark or live deployment was performed. All 25 product evaluation statuses remain Not evaluated. All eight cases are fictional. Normative-style candidate requirements, provisional local priorities and informative techniques remain draft material for review and pilot.

## Run the checks

```bash
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

After changing canonical content, first run `python scripts/render_documents.py`. These commands use Python's standard library and perform no network publication or live tool actions.
