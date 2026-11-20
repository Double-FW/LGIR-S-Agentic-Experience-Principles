# Illustrative operation records

These four records demonstrate local separation of execution state, external effect, cancellation and recovery. They contain no real transaction, actual authority or product evidence. The evidence identifiers are explicitly synthetic. They are not MCP/OpenAPI messages or a production implementation.

| Record | What it demonstrates |
| --- | --- |
| [Timeout, outcome unknown](timeout-unknown.json) | New work can stop while an earlier provider effect remains unknown |
| [Reconciled completion](reconciled-completion.json) | Later confirmation can establish that an earlier effect committed; it does not rewrite history as cancelled |
| [Failure before an effect](failed-before-effect.json) | No effect is a distinct claim needing appropriate evidence |
| [Irreversible send](irreversible-send.json) | A delivered effect may need correction without any complete undo |

The first two describe snapshots of the same fictional operation. They are not an executed transition trace. A timestamped event log, provider-specific transaction model, authorisation and actual reconciliation would be needed in a real service.

The [example schema](../../schemas/operation-record.schema.json) defines this local record shape. Its conservative example profile blocks retries while the outcome is unknown; another design could use properly verified provider idempotency, with its actual guarantees and scope evaluated. The profile is not a universal protocol requirement.

The repository checker covers required fields, basic types/enums and selected cross-field invariants. It is not a complete JSON Schema engine and cannot establish that a claimed real event occurred. Do not upload actual operational records to this public example folder.
