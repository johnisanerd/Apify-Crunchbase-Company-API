# 🏢 Crunchbase Company API: Firmographics & Funding to Structured JSON

> The most efficient, reliable, and developer-friendly way to use the Crunchbase Company API.

**Actor page:** [apify.com/johnvc/crunchbase-company-api](https://apify.com/johnvc/crunchbase-company-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/crunchbase-company-api/input-schema](https://apify.com/johnvc/crunchbase-company-api/input-schema?fpr=9n7kx3)

Send one or many public Crunchbase organization URLs and get back one clean JSON row per company: name, industries, total funding, investors, employee count, HQ location, rank, and IPO status. It is built API-first and MCP-ready, so you can call it from Python or drive it as a tool from an AI agent.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Crunchbase-Company-API.git
   cd Apify-Crunchbase-Company-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python crunchbase-company-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python crunchbase-company-api-example.py
```

## Why Use This Crunchbase Company API?

**A URL in, structured data out.** You never touch collection infrastructure. Pass a public organization URL and get flat, predictable firmographic and funding fields you can load straight into a sheet, a database, or a CRM.

**Batch friendly.** Send up to 1000 company URLs in one run. They are collected in parallel and returned one row each, so enriching a target list is one call.

**Pay per company.** Billing is per company returned, with no per-run setup fee, so you only pay for what is delivered.

**Reliable and predictable.** Every company comes back with the same field shape, and a URL that cannot be collected returns a clear error row instead of failing the whole run.

**MCP-ready.** Call it as a tool from Claude, Cursor, and other AI agents (see the install sections below).

## Features

### Core Capabilities
- Collect one or many public Crunchbase organization pages by URL
- Name, industries, employee-count band, HQ location, and description
- Funding summary (total funding, number of rounds, investor count) and investor names
- Acquisitions, IPO status, Crunchbase rank, growth score, and web-traffic signal

### Data Quality
- One consistent JSON row per company, every time
- A plain-language `summary` field on every row for quick scanning and AI use
- Clear per-URL error rows so a single bad link never sinks the batch

## Usage Examples

### Basic Example
```json
{
  "companyUrls": ["https://www.crunchbase.com/organization/apple"]
}
```

### Batch Example (collected in parallel)
```json
{
  "companyUrls": [
    "https://www.crunchbase.com/organization/apple",
    "https://www.crunchbase.com/organization/anthropic"
  ]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `companyUrls` | `list[str]` | YES | - | One or more public Crunchbase `/organization/` page URLs. Up to 1000 per run; non-`/organization/` URLs are skipped. |

## Output Format

Each company is returned as one JSON row:

```json
{
  "result_type": "company",
  "name": "OpenAI",
  "legalName": "OpenAI OpCo, LLC",
  "cbRank": 10,
  "description": "OpenAI is an AI research and deployment company.",
  "website": "https://www.openai.com",
  "hqLocation": "San Francisco, California, United States",
  "country": "United States",
  "employeeCount": "1001-5000",
  "industries": ["Artificial Intelligence", "Machine Learning"],
  "numFundingRounds": 11,
  "numInvestors": 104,
  "numAcquisitions": 22,
  "operatingStatus": "active",
  "companyType": "for_profit",
  "ipoStatus": "private",
  "contactEmail": "support@openai.com",
  "companyUrl": "https://www.crunchbase.com/organization/openai",
  "summary": "OpenAI, Artificial Intelligence, 1001-5000 employees, San Francisco, California, United States"
}
```

The `investors`, `contactEmail`, and `totalFunding` fields are returned when Crunchbase lists them.

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Crunchbase Company API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Crunchbase Company API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Crunchbase Company API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/crunchbase-company-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api`, using OAuth when prompted.
5. Ask Claude to run the Crunchbase Company API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Crunchbase Company API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/crunchbase-company-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

## Use it in n8n (no code)

Prefer a no-code path? There is a ready-made n8n template that runs this actor for you: paste Crunchbase organization URLs, get funding totals, rounds, investors, and firmographics as rows in Google Sheets. No Crunchbase API key required.

- Template: [Collect Crunchbase funding data into Google Sheets with Apify](https://n8n.io/workflows/17353-collect-crunchbase-funding-data-into-google-sheets-using-apify/)
- It uses the official Apify node, so it works on n8n Cloud and self-hosted.
- Self-hosting n8n? There is also a dedicated community node: [n8n-nodes-crunchbase-company-api](https://www.npmjs.com/package/n8n-nodes-crunchbase-company-api)

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Crunchbase Company API to power your venture capital research, company enrichment, and CRM workflows with reliable, structured results.*

Last Updated: 2026.08.19
