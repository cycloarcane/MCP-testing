# MCP-testing: OpenWebUI + mcpo Integration

This repo is for experimenting with running MCP tools (premade and custom) via `mcpo` and integrating them cleanly with OpenWebUI.

---

## ✨ Current Goal

Set up and successfully call **one premade MCP tool** (`mcp-server-time`) using `mcpo`'s config-based proxy and OpenWebUI.

---

## 🔧 Run the Proxy

Use this command to launch `mcpo` with your tool config:

```bash
uvx mcpo --port 8000 --api-key dev123 --config ./config.json
```

This will serve your tools on `http://127.0.0.1:8000`, with each tool mounted under its key (e.g. `/time`).

---

## 📊 Config File Example (single tool)

**`config.json`**:

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=America/New_York"]
    }
  }
}
```

---

## 🌐 OpenWebUI Setup

### Correct Endpoint:

> **Base URL:**
>
> ```
> http://127.0.0.1:8000/time
> ```
>
> **OpenAPI URL:**
>
> ```
> /openapi.json
> ```

> **❌ Don't do this:**
>
> * `http://127.0.0.1:8000` as base URL (this fails)
> * `/time/openapi.json` as OpenAPI URL (this fails)

---

## 🏁 Tool Call Checklist

1. mcpo launched successfully with config
2. Tool appears under available tools in OpenWebUI
3. Chat tool toggle is enabled (right sidebar or on bottom left of chat input)
4. Chat model supports function calling (e.g. GPT-4, Mistral-7B-func, Qwen3)
5. Tool is invoked using correct path: `/time/get_current_time`

---

## 🔄 Troubleshooting

* **401 Unauthorized:** Ensure you use `Authorization: Bearer dev123` header or input the key into OpenWebUI's API key field.
* **404 Not Found:** Double check tool mount path. Tool functions are under `/tool-name/function-name` in config mode.
* **Tool doesn't respond:** Wrong Base URL in OpenWebUI (likely still pointing at root).

---

## 📓 Development Roadmap

* [x] Single premade tool using config
* [ ] Multiple premade tools using config
* [ ] Single custom tool using config
* [ ] Mix of custom and premade tools using config

---

Happy hacking ✨
