---
title: resterm v1.5.6
url: https://kitploit.com/en/posts/github-unkn0wn-root-resterm-v156
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:26.280129
---

# resterm v1.5.6

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9255/1e06e2fdfb1f34f2291ec50ff379f7d82bdf3cdd839b9a84d21c8ef27042f58e.png)

New releaseSep 5, 2026

# resterm v1.5.6

Terminal API client for HTTP, GraphQL and gRPC. Plain .http files you can diff and version, with workflows, mocks, profiling, tracing, OpenAPI import, SSH tunnels, Kubernetes port-forwards, WebSocket, SSE and a CLI runner.

Share

# ![Resterm](https://assets.kitploit.com/production/public/readmes/9255/fbbb3a11ae3be73099da760872eb38c475c9d1b4912908cc6e94ee5f40173c7b.png) Resterm

*A terminal-native API client and workbench for REST, GraphQL, gRPC, WebSocket and SSE.*

![Screenshot of Resterm TUI base](https://assets.kitploit.com/production/public/readmes/9255/165e5afbbfbae610d2faedd80e3aee887977daa533f2989d904f4390b32f0848/bedc9e3f4bbab0389d6fca7eb6e47e000d8df954d1d8c07dde02ad39f7c93864-display-v1.webp)

Resterm is an *API-as-code* workbench - or, in more familiar terms, an API client - built around plain `.http` and `.rest` files that you can diff, review and version. It combines interactive request editing with declarative workflows, assertions, mock servers, tracing, profiling and headless automation. Everything stays on your machine. No accounts, no cloud sync, no telemetry.

If you are looking for a Postman-style client centered on GUI collections, Resterm is probably *not* for you, but give it a try anyway!

> [!NOTE]
> Resterm is now v1! See the [v1.0.0 release notes](https://github.com/unkn0wn-root/resterm/releases/tag/v1.0.0) for new features and breaking changes.

Quick links: [Screenshots](#screenshot-tour), [Quick Start](#quick-start), [Request files](#request-files), [Installation](#installation), [Documentation](#documentation).

## Screenshot tour

See the UI in action (click to expand)

**Workflows**

![Screenshot of Resterm with Workflow](https://assets.kitploit.com/production/public/readmes/9255/1b1c75ae16ecab6c514ab21193dd4fb409a6e3c5d09022d0dc88cc559be69991.png)

**Trace and Timeline**

![Screenshot of Resterm with timeline](https://assets.kitploit.com/production/public/readmes/9255/3c14a406f55fdc5efdf6080f791e661e391882435a4e0b423060da6437416e54.png)

**Profiler**

![Screenshot of Resterm profiler](https://assets.kitploit.com/production/public/readmes/9255/6d6638969702fe3c5e40670861f7e53cb4d9f1b8f7ad89d8b34a3479da196e53.png)

**Explain**

![Screenshot of Resterm Explain Tab](https://assets.kitploit.com/production/public/readmes/9255/6cddc040db5f7c648eda66979494802f8d3da10b8c27bdc8939663ea3b87287c.png)

**RestermScript**

![Screenshot of Resterm with RestermScript](https://assets.kitploit.com/production/public/readmes/9255/fd8c0678c1e02347d875afacd1308fffe8e2c21f622074d98933d6eae3af6bb3.png)

**Light Theme**

![Screenshot of Resterm in Lighttheme](https://assets.kitploit.com/production/public/readmes/9255/1bb7a710c1d246214941eeec2eb2f36039b013039c0d5495055c2d1bf48f3a7f.png)

**OAuth browser demo (old UI design)**

![Resterm OAuth flow](https://raw.githubusercontent.com/unkn0wn-root/resterm/HEAD/_media/oauth.gif)

## Why Resterm

* **HTTP, GraphQL, gRPC, WebSocket and SSE** out of the box.
* **Automation lives in the request files:** conditions (`@when`, `@if`/`@elif`/`@else`, `@for-each`), multi-step workflows (`@workflow` / `@step`), captures, variables and assertions (`@capture`, `@var`, `@assert`).
* **RestermScript**, a small expression language built for Resterm, with JavaScript hooks when you want them.
* **Vim-style controls** with contextual bottom bar hints, searchable offline help, `K` help under the cursor, `/` search and commands like `:w`, `:q`, `:help` and `:docs`.
* **Built-in auth and tunneling:** OAuth 2.0 (client credentials, password, auth code with PKCE), auth backed by your existing CLIs, SSH tunnels and Kubernetes port-forwards. No extra tools needed.
* **CLI runner:** `resterm run` for scripted runs and CI, with JSON and JUnit output.
* **Mock servers** declared next to the requests they mimic, with matching rules, sequences, call verification and hot reload.
* **Timeline tracing, profiling and compare runs** across environments.
* **Streaming transcripts** and an interactive console for WebSocket and SSE.
* **No AI integration**, ever.

## Quick Start

1. Install Resterm (see [Installation](#installation) for scripts, Windows and manual installs).

   root@kitploit:~

   ```
   brew install resterm
   ```
2. Bootstrap a workspace.

   root@kitploit:~

   ```
   mkdir my-api && cd my-api
   resterm init
   ```

   `resterm init` gives you a small project that works without an internet connection. The generated `requests.http` includes local mock scenarios and a few requests that build on each other. They cover assertions, bearer auth, JSON matching, `json-rules`, and `@for-each`.
3. Start it and send your first request.

   root@kitploit:~

   ```
   resterm
   ```

   Press `Ctrl+Enter` in the editor to send the highlighted request.

No files yet? Just run `resterm`, type a URL and press `Ctrl+Enter`. A pasted curl command works too.

## Request files

Resterm request files use standard HTTP syntax plus `# @` directives for configuration and automation:

root@kitploit:~

```
# @setting base-url https://api.example.com/v1/

### Create users
// Send this request once for each name in the list.
# @for-each ["david", "tom"] as name
# @when env.mode == "development"
# @assert response.statusCode == 201
POST users
Content-Type: application/json

{"name":"{{= name }}"}
```

Settings before the first request apply to the whole file, `###` separates requests, and directives can repeat, limit or validate a request. More examples here: [`_examples/`](https://github.com/unkn0wn-root/resterm/blob/main/_examples).

## CLI

`resterm run` executes `.http` / `.rest` files without opening the TUI, which is what CI runs.

root@kitploit:~

```
resterm run --request CreateUser requests.http
```

The generated project talks to a local mock server. Start it in another terminal first:

root@kitploit:~

```
resterm mock requests.http
```

In the TUI, press `g Shift+M` instead to start the same mock server from the workspace.

The [CLI documentation](https://github.com/unkn0wn-root/resterm/blob/main/docs/cli.md) covers selectors, output formats and more examples.

## Keyboard cheat sheet

* Pane focus and layout
  + `Tab` / `Shift+Tab`: move between sidebar, editor and response.
  + `g+r`, `g+i`, `g+p`: jump to requests, editor or response.
  + `g+h` / `g+l`: resize horizontally. Changes sidebar width when the sidebar is focused, the editor/response split otherwise.
  + `g+j` / `g+k`: resize editor/response height when stacked, collapse or expand branches in the navigator.
  + `g+v` / `g+s`: toggle the response pane between inline and stacked layout.
  + `g+1`, `g+2`, `g+3`: minimize or restore sidebar, editor, response.
  + `g+z` / `g+Z`: zoom the focused pane, clear zoom.
* Environments and globals
  + `Ctrl+E`: switch environments.
  + `Ctrl+G`: inspect captured globals.
* Help and commands
  + `?`: open the searchable offline help index.
  + `K` (editor normal mode): open help for the directive, template or keyword under the cursor.
  + `:help <topic>` / `:man <topic>`: open an embedded topic; `:docs <topic>` opens the version-matched full manual.
  + `Ctrl+O`: open the file/workspace popup. Type to filter, scroll with `Up` / `Down`, and use `Tab` to descend into directories.
  + `:`: open the command line. Use `Up` / `Down` to select suggestions, `Tab` to complete one, or `Enter` to accept and run a selection. Path arguments such as `:mock start --source` and `:edit` browse the filesystem in the same popup.
* Respons...