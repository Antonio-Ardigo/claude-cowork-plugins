# Connectors -- Project Planning Plugin

This plugin can work standalone using conversational input. For enhanced workflows, the following integrations are available via MCP:

## Optional Integrations

| System | Purpose | MCP Server |
|--------|---------|-----------|
| **Primavera P6** | Import/export CPM schedules, resource loading | Not yet configured |
| **Microsoft Project** | Import/export schedules (.mpp) | Not yet configured |
| **CostOS / Cleopatra** | Cost estimation database, parametric models | Not yet configured |
| **Aveva E3D / PDMS** | 3D model data, MTO extraction | Not yet configured |
| **SharePoint / DMS** | Document management, gate package storage | Not yet configured |
| **Excel** | Workbook generation (openpyxl) | Local Python execution |

## Currently Active

- **Excel generation**: The plugin generates .xlsx workbooks at each toll gate using Python (openpyxl). This requires Python 3.12+ with openpyxl installed.

## Setting Up Connectors

To connect an external system, configure the MCP server in `.mcp.json` at the plugin root or project level. See Claude Code documentation for MCP server configuration.
