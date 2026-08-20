---
title: firefox-devtools-mcp v0.10.0
url: https://kitploit.com/en/posts/github-mozilla-firefox-devtools-mcp-v0100
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:14.657621
---

# firefox-devtools-mcp v0.10.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F8655%2Ff3cb67f359fcc5b9d9675ac3f73c311e49097d4c89536927bd264cdc76c78dd0.png&w=3840&q=75)

New releaseAug 19, 2026

# firefox-devtools-mcp v0.10.0

Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

Share

# Firefox DevTools MCP

[![npm version](https://badge.fury.io/js/@mozilla/firefox-devtools-mcp.svg)](https://www.npmjs.com/package/mozilla/firefox-devtools-mcp)
[![CI](https://github.com/mozilla/firefox-devtools-mcp/workflows/CI/badge.svg)](https://github.com/mozilla/firefox-devtools-mcp/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mozilla/firefox-devtools-mcp/branch/main/graph/badge.svg)](https://codecov.io/gh/mozilla/firefox-devtools-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE-MIT) [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE-APACHE)

[![Glama](https://assets.kitploit.com/production/public/readmes/8655/a78a7d97ae218a4638aa3f14a824feef8d0e205b36490113ed8fa15dac83148a.png)](https://glama.ai/mcp/servers/%40mozilla/firefox-devtools-mcp)

Model Context Protocol server for automating Firefox via WebDriver BiDi (through Selenium WebDriver). Works with Claude Code, Claude Desktop, Cursor, Cline and other MCP clients.

Repository: <https://github.com/mozilla/firefox-devtools-mcp>

> **Note**: This MCP server requires a local Firefox browser installation and cannot run on cloud hosting services like glama.ai. Use `npx @mozilla/firefox-devtools-mcp@latest` to run locally, or use Docker with the provided Dockerfile.

## Security

Browser MCP servers carry inherent risks. A few key practices:

* **Use a dedicated Firefox profile.** Never run the server against your regular profile — the agent has access to whatever the browser can reach, including cookies and saved sessions.
* **Be cautious about which sites you visit.** Pages can return content designed to manipulate the agent (prompt injection). Stick to sites you control or trust.
* **Enable only the tool modules you need.** Higher presets such as `--tool-preset developer` (script, debugging) and `--tool-preset mozilla` (privileged context) significantly expand what the agent can do.

See [SECURITY.md](https://github.com/mozilla/firefox-devtools-mcp/blob/HEAD/SECURITY.md) for a full breakdown of risks and how to report vulnerabilities.

## Requirements

* Node.js ≥ 20.19.0
* Firefox 100+ installed (auto‑detected, or pass `--firefox-path`)

## Install and use with Claude Code (npx)

Recommended: use npx so you always run the latest published version from npm.

Option A — Claude Code CLI

root@kitploit:~

```
claude mcp add firefox-devtools npx @mozilla/firefox-devtools-mcp@latest
```

Pass options either as args or env vars. Examples:

root@kitploit:~

```
# Headless + viewport via args
claude mcp add firefox-devtools npx @mozilla/firefox-devtools-mcp@latest -- --headless --viewport 1280x720

# Or via environment variables
claude mcp add firefox-devtools npx @mozilla/firefox-devtools-mcp@latest \
  --env START_URL=https://example.com \
  --env FIREFOX_HEADLESS=true
```

Option B — Edit Claude Code settings JSON

Add to your Claude Code config file:

* macOS: `~/Library/Application Support/Claude/Code/mcp_settings.json`
* Linux: `~/.config/claude/code/mcp_settings.json`
* Windows: `%APPDATA%\Claude\Code\mcp_settings.json`

root@kitploit:~

```
{
  "mcpServers": {
    "firefox-devtools": {
      "command": "npx",
      "args": ["-y", "@mozilla/firefox-devtools-mcp@latest", "--headless", "--viewport", "1280x720"],
      "env": {
        "START_URL": "about:blank"
      }
    }
  }
}
```

Option C — Helper script (local dev build)

root@kitploit:~

```
npm run setup
# Choose Claude Code; the script saves JSON to the right path
```

## Try it with MCP Inspector

root@kitploit:~

```
npx @modelcontextprotocol/inspector npx @mozilla/firefox-devtools-mcp@latest --start-url https://example.com --headless
```

Then call tools like:

* `list_pages`, `select_page`, `navigate_page`
* `take_snapshot` then `click_by_uid` / `fill_by_uid`
* `list_network_requests` (always‑on capture), `get_network_request`
* `list_downloads` (always‑on capture), `set_download_behavior`
* `screenshot_page`, `list_console_messages`

## CLI options

You can pass flags or environment variables (names on the right):

* `--firefox-path` — absolute path to Firefox binary
* `--headless` — run without UI (`FIREFOX_HEADLESS=true`)
* `--viewport 1280x720` — initial window size
* `--profile-path` — use a specific Firefox profile
* `--firefox-arg` — extra Firefox arguments (repeatable)
* `--start-url` — open this URL on start (`START_URL`)
* `--accept-insecure-certs` — ignore TLS errors (`ACCEPT_INSECURE_CERTS=true`)
* `--connect-existing` — attach to an already-running Firefox instead of launching a new one (`CONNECT_EXISTING=true`)
* `--marionette-port` — Marionette port for connect-existing mode, default 2828 (`MARIONETTE_PORT`)
* `--pref name=value` — set Firefox preference at startup via `moz:firefoxOptions` (repeatable)
* `--tool-preset` — select which tool modules to enable: `slim`, `basic` (default), `developer`, `mozilla`, or `all`. See [Tool modules and presets](#tool-modules-and-presets). (`TOOL_PRESET`)
* `--tools` — explicit list of tool modules to enable, overriding `--tool-preset` entirely (e.g. `--tools pages network script`). See [Tool modules and presets](#tool-modules-and-presets).
* `--enable-script` — *deprecated, use `--tool-preset developer` or `--tools ... script debugging`.* Selects the `developer` tool preset. (`ENABLE_SCRIPT=true`)
* `--enable-privileged-context` — *deprecated, use `--tool-preset mozilla` or `--tools ... privileged prefs`.* Selects the `mozilla` tool preset. Requires `MOZ_REMOTE_ALLOW_SYSTEM_ACCESS=1` (`ENABLE_PRIVILEGED_CONTEXT=true`)
* `--android-device` — enable Firefox for Android mode; value is the ADB device serial (e.g. `emulator-5554`). Run `adb devices` to list connected devices. Omit the value or use `auto` to select the single connected device automatically.
* `--android-package` — Android app package name, default `org.mozilla.firefox`. Other packages: `org.mozilla.firefox_beta` for Firefox Beta, `org.mozilla.fenix` for Firefox Nightly, `org.mozilla.fenix.debug` for Firefox Nightly Debug, `org.mozilla.geckoview_example` for geckoview (`ANDROID_PACKAGE`)
* `--log-file` — write MCP server logs to a file instead of stderr. Useful for debugging sessions with MCP clients that hide server output. Set `DEBUG=*` to also include verbose debug logs. Example: `--log-file /tmp/firefox-mcp.log`

### Tool modules and presets

Tools are grouped into modules. You choose which modules to expose either with a named preset
(`--tool-preset`) or with an explicit list (`--tools`). When both are given, `--tools` wins and
the preset is ignored.

Modules: `pages`, `snapshot`, `input`, `network`, `console`, `screenshot`, `utilities`,
`management`, `webextension`, `profiler`, `screencast`, `script`, `debugging`, `prefs`,
`privileged`.

Presets (each is a superset of the previous):

* `slim` — `pages`, `snapshot`, `input`, `network`, `console`
* `basic` (default) — `slim` plus `screenshot`, `utilities`, `management`, `webextension`, `profiler`, `screencast`
* `developer` — `basic` plus `script`, `debugging`
* `mozilla` — `developer` plus `prefs`, `privileged`
* `all` — every module

root@kitploit:~

```
# Use the developer preset (adds script and debugging tools)
npx @mozilla/firefox-devtools-mcp --...