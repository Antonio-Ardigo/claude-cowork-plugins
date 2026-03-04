# Cost Engineer Plugin

Full cost engineering suite for EPC and construction projects. Covers estimation, benchmarking, earned value management, change orders, and lifecycle costing — with the ability to analyze cost data from Excel files.

## Skills

| Skill | What It Covers |
|-------|---------------|
| **Cost Estimation Methods** | Parametric (Lang/Hand/Chilton), capacity-scaled, bottom-up, unit-rate, and three-point estimation with factor tables and worked examples |
| **Cost Benchmarking & Normalization** | AACE/IPA benchmarking methodology, escalation indices (CEPCI, ENR, Nelson-Farrar), location factors by country, currency normalization |
| **Earned Value Management** | Full EVM metrics (CPI, SPI, EAC, TCPI), WBS-level drill-down, multiple EAC methods, S-curves, trend analysis with early warning indicators |
| **Change Order Management** | Direct/indirect cost impact analysis, markup structure, pricing format template, cumulative impact assessment, reasonableness checks |
| **Lifecycle Cost Analysis** | CAPEX + OPEX, NPV, IRR, payback, EAC (equivalent annual cost), sensitivity analysis, OPEX benchmarks by facility type |

## Commands

| Command | Purpose |
|---------|---------|
| `/analyze-estimate` | Read an Excel cost estimate and check for gaps, outliers, and consistency against AACE standards |
| `/cost-benchmark` | Normalize a project's costs and compare against industry benchmarks (IPA quartiles) |
| `/change-order` | Evaluate a proposed change order — calculate direct costs, indirects, markups, and total value |
| `/evm-report` | Generate an EVM report from actuals data — CPI, SPI, EAC forecasts, WBS analysis, trend assessment |

## Usage

Ask questions about cost engineering topics and the relevant skill will load automatically. Use the slash commands for structured analysis workflows.

### Example Prompts

- "How do I estimate the cost of a 200 MW CCGT plant using parametric methods?"
- "What are typical location factors for the Middle East vs. Australia?"
- "Explain the difference between CPI-based and composite EAC methods"
- `/analyze-estimate` — then provide your Excel file
- `/cost-benchmark` — then provide project type, capacity, cost, and location
- `/change-order` — then describe the proposed change
- `/evm-report` — then provide BAC, PV, EV, AC data
