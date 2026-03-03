# Connectors -- Training Plan Plugin

This plugin is self-contained and works without external connections.

## Optional Integrations

| System | Purpose | Notes |
|--------|---------|-------|
| File system | Read/write training plans, transcripts, checkpoints, learner profiles | Required for all operations |
| concept-builder format | Concept maps using shared node-type/relationship vocabulary | Format embedded in content-builder skill -- no plugin dependency |

## Currently Active

- **File system**: Training plans, session transcripts, checkpoint files, and learner profiles are saved to the current working directory as Markdown

## Concept Map Integration

The training-plan plugin can generate concept maps during TTT sessions (Phase 3.5). These maps use the same markdown nested-list format and node-type vocabulary as the concept-builder plugin, but the format is self-contained within this plugin's content-builder skill. There is no runtime dependency on concept-builder.

If concept-builder is also installed, concept maps generated during TTT sessions are structurally compatible with concept-builder's `/library` command, but this interoperability is a consequence of shared format, not a wired integration.
