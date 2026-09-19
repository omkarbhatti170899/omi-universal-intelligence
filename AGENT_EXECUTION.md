# Omi Agent Execution v10

Omi now has a bounded agent-execution stage after planning.

Flow:
request → planner → bounded execution plan → approved provider/tool stage → verification.

The agent does not receive arbitrary shell access, credentials, or unrestricted network access.
Each privileged capability remains behind the existing security and provider/research adapters.
This stage records execution intent and prepares the next action rather than pretending an
external action succeeded when it has not.
