---
title: mcpsnoop v0.19.0
url: https://kitploit.com/en/posts/github-kerlenton-mcpsnoop-v0190
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:53.775965
---

# mcpsnoop v0.19.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9109/7eb33e7269ba3b548a394e06ff8227706b686533f7b12dac7a143e883b7f2c4f.gif)

New releaseAug 21, 2026

# mcpsnoop v0.19.0

Wireshark for MCP. A transparent proxy that shows every real tool call between your AI client and your MCP servers, live in your terminal.

Share

![mcpsnoop](https://assets.kitploit.com/production/public/readmes/9109/91d664ea266713affb29238906792777021b43fa6627b13f46382f48ad340a61.png)

**Wireshark for MCP.** A transparent proxy that shows every real tool call
between your AI client and your MCP servers, live in your terminal.

[![CI](https://github.com/kerlenton/mcpsnoop/actions/workflows/ci.yml/badge.svg)](https://github.com/kerlenton/mcpsnoop/actions/workflows/ci.yml)
[![Go Reference](https://pkg.go.dev/badge/github.com/kerlenton/mcpsnoop.svg)](https://pkg.go.dev/github.com/kerlenton/mcpsnoop)
[![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

![mcpsnoop demo](https://assets.kitploit.com/production/public/readmes/9109/30466d77be15250e4bab6639e48a4cd5b0d44cd96e48606b60c6bacb67c15c3d.gif)

## The problem

The official [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
connects as its own client, so it never sees what *your* client (Cursor, Claude
Code, Codex) actually sends your server. And anything that waits for a request
to arrive can't show the call the model never made, or made with the wrong
arguments. When a tool silently isn't called, capabilities don't line up, or a
call just hangs, you're left digging through logs and guessing.

**mcpsnoop sits in the real data path instead.** Wrap your server command with
it and watch every JSON-RPC frame live, as your real client and server talk.

## Quick start

See it right away, with nothing to set up.

root@kitploit:~

```
mcpsnoop demo
```

To use it for real, wrap your server in your client's MCP config.

root@kitploit:~

```
{
  "mcpServers": {
    "my-server": {
      "command": "mcpsnoop",
      "args": ["--", "node", "build/index.js"]
    }
  }
}
```

Everything after `--` is the command that normally launches your server. Swap in
whatever you already use, like `python server.py`, `npx -y @scope/server`, or a
compiled binary.

On Claude Desktop you don't have to make that edit by hand.

root@kitploit:~

```
mcpsnoop wrap my-server     # route my-server through mcpsnoop
mcpsnoop unwrap my-server   # put it back
```

`wrap` finds `claude_desktop_config.json`, copies it to
`claude_desktop_config.json.mcpsnoop.bak` the first time, and rewrites only that
one server's entry, so your formatting and every other server are left alone.
Inside the rewritten entry the keys come back in alphabetical order. `unwrap`
restores the file, and removes the backup once no server is wrapped any more.
Restart Claude Desktop after either, since MCP servers are launched once at
startup.

Then use your client as usual and open the UI.

root@kitploit:~

```
mcpsnoop
```

No flags, no socket paths, no startup order to remember. The shim and the UI find
each other on their own, and the UI backfills past sessions from disk.

For a streamable-HTTP server, run mcpsnoop as a reverse proxy.

root@kitploit:~

```
mcpsnoop http --target http://localhost:3000/mcp --listen :7000
```

The HTTP status of every response shows in the stream, so a response that carries
no JSON-RPC message of its own is still a visible frame rather than nothing: the
401 challenge, the 403 on a rejected Origin, the 202 that acknowledges a
notification, and the 502 when the target cannot be reached at all. A 401's
`WWW-Authenticate` header is kept verbatim and shown in the inspector, since it
names the auth scheme and the resource metadata to go to next. Filter by status
with `status:401` in the TUI, or by any failure with `status:err`. A 4xx or 5xx
counts as an error, so a default `mcpsnoop check` run fails on it.

No server of your own? [Try it for real](https://github.com/kerlenton/mcpsnoop/blob/HEAD/docs/TRY_IT.md) against a published
test server, driven by your own client. To inspect a session after it happened,
see [review past sessions from logs](https://github.com/kerlenton/mcpsnoop/blob/HEAD/docs/POST_MORTEM.md).

### Config file

If you reuse the same shim flags across a project, put them in a
`.mcpsnoop.toml` file in the current working directory.

root@kitploit:~

```
label = "filesystem"
trace-file = "trace.jsonl"
redact-secrets = true
redact-key = "token,authorization"
redact-value = "sk-[A-Za-z0-9]+"
redact-path = "$.params.arguments.password"
no-trace = false
```

Repeat `redact-key`, `redact-value`, and `redact-path` on their own lines to add
more than one of each.

Those are all the keys it supports.

The file is only looked up in the current working directory, not in parent
directories.

Explicit command-line flags override values from the config file.

## Commands

| Command | What it does |
| --- | --- |
| `mcpsnoop -- <server>` | wrap a stdio server as a transparent shim |
| `mcpsnoop` | open the live TUI |
| `mcpsnoop http --target <url>` | proxy a streamable-HTTP server |
| `mcpsnoop export` | render a session to json, html, text, har, or otlp |
| `mcpsnoop check` | fail CI on errors, invalid frames, warnings, routing mismatches, hung calls, or late results |
| `mcpsnoop baseline` | inspect, accept, or reset trusted tool definitions |
| `mcpsnoop diff` | compare tools and calls across two captured sessions |
| `mcpsnoop open` | open a saved session in the TUI |
| `mcpsnoop prune` | delete saved session logs older than a cutoff |
| `mcpsnoop wrap <server>` | route one of Claude Desktop's servers through mcpsnoop |
| `mcpsnoop unwrap <server>` | put that server's entry back the way it was |
| `mcpsnoop remote <user@host>` | print the SSH tunnel command |
| `mcpsnoop demo` | play a scripted session |

Run `mcpsnoop help` for the full list, or `mcpsnoop help <command>` for the flags of one.

## How it compares

|  | MCP Inspector | mcpsnoop |
| --- | --- | --- |
| Sees your real client and server traffic | no | yes |
| Flags hung calls and stream errors | no | yes |
| Flags stray output that corrupts the stream | no | yes |
| Flags malformed JSON-RPC frames | no | yes |
| Detects tool definition drift after approval | no | yes |
| Interactive terminal UI | no | yes |
| Zero-config, no flags or ordering | no | yes |
| Capability inspector | partial | yes |
| Replay a captured call | no | yes |
| Session export (json / html / text / otlp) | no | yes |
| Single binary, no runtime deps | no | yes |

## Install

### Go

root@kitploit:~

```
go install github.com/kerlenton/mcpsnoop/cmd/mcpsnoop@latest
```

### Homebrew

root@kitploit:~

```
brew install mcpsnoop
```

Prebuilt binaries for every platform are on the [Releases](https://github.com/kerlenton/mcpsnoop/releases) page.

### Shell completions

mcpsnoop ships completions for bash, zsh, fish, and PowerShell. Run
`mcpsnoop completion <shell> --help` for the setup steps, which cover enabling
completion and the install path for your OS.

## How it works

![mcpsnoop sits in the pipe between your AI client and your MCP servers, copying every JSON-RPC frame to a live terminal UI](https://raw.githubusercontent.com/kerlenton/mcpsnoop/HEAD/assets/architecture-light.svg)

mcpsnoop is two roles in one binary. `mcpsnoop -- <server>` is the transparent
shim your client spawns, forwarding bytes verbatim while shipping a copy of every
frame to the hub. `mcpsnoop` with no arguments is that hub and its live TUI. They
pair through a well-known socket and on-disk logs, so neither has to start first.

The hub loads the newest 100 saved sessions by default, kee...