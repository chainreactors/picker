---
title: envsec v1.0.0-rc.2
url: https://kitploit.com/en/posts/github-davidnussio-envsec-v100-rc2
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:37.377720
---

# envsec v1.0.0-rc.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12811/f887c4b9ba3d12c73dbebb379d9c2313665f8c12b66b02da52ed34c3d1d9e01b.gif)

New releaseSep 3, 2026

# envsec v1.0.0-rc.2

Secure CLI tool for managing environment secrets using native OS credential stores (macOS Keychain, Linux Secret Service, Windows Credential Manager)

Share

# envsec

Secure environment secrets management using native OS credential stores.

## Demo

![Image](https://assets.kitploit.com/production/public/readmes/12811/f887c4b9ba3d12c73dbebb379d9c2313665f8c12b66b02da52ed34c3d1d9e01b.gif)

## Features

* Store secrets in your OS native credential store (not plain text files)
* Cross-platform: macOS, Linux, Windows
* Organize secrets by context (e.g. `myapp.dev`, `stripe-api.prod`, `work.staging`)
* Track secret metadata (key names, timestamps) via SQLite
* Search contexts and secrets with glob patterns
* Run commands with secret interpolation
* Save and rerun commands with `cmd` (search, list, run, delete)
* Export secrets to `.env` files (with generation tracking via `audit`)
* Export secrets as shell environment variables (`eval $(envsec env)`)
* Load secrets from `.env` files (with conflict detection)
* Share secrets encrypted with GPG for team members
* Interactive terminal UI (`envsec tui`) for managing secrets without memorizing commands

## Packages

This is a monorepo containing the following packages:

| Package | Description | npm |
| --- | --- | --- |
| [`envsec`](https://github.com/davidnussio/envsec/blob/main/packages/cli) | CLI tool for managing secrets | [![npm](https://img.shields.io/npm/v/envsec)](https://www.npmjs.com/package/envsec) |
| [`@envsec/sdk`](https://github.com/davidnussio/envsec/blob/main/packages/sdk) | Node.js / Bun SDK for loading secrets programmatically | [![npm](https://img.shields.io/npm/v/@envsec/sdk)](https://www.npmjs.com/package/%40envsec/sdk) |
| [`@envsec/core`](https://github.com/davidnussio/envsec/blob/main/packages/core) | Core engine — OS credential store adapters + metadata DB | [![npm](https://img.shields.io/npm/v/@envsec/core)](https://www.npmjs.com/package/%40envsec/core) |
| [`@envsec/tui`](https://github.com/davidnussio/envsec/blob/main/packages/tui) | Interactive terminal UI for secrets management | [![npm](https://img.shields.io/npm/v/@envsec/tui)](https://www.npmjs.com/package/%40envsec/tui) |

## SDK Quick Start

For programmatic access to secrets from Node.js or Bun, use `@envsec/sdk`:

root@kitploit:~

```
npm install @envsec/sdk
```

root@kitploit:~

```
import { loadSecrets } from "@envsec/sdk";

// Load and inject into process.env
await loadSecrets({ context: "myapp.dev", inject: true });

// Or use the client for full control
import { EnvsecClient } from "@envsec/sdk";
const client = await EnvsecClient.create({ context: "myapp.dev" });
const apiKey = await client.get("api.key");
await client.close();
```

See the full [SDK documentation](https://github.com/davidnussio/envsec/blob/main/packages/sdk/README.md) for all APIs, multi-context support, and options.

## Requirements

* Node.js >= 22

### macOS

No extra dependencies. Uses the built-in Keychain via the `security` CLI tool.

### Linux

Requires `libsecret-tools` (provides the `secret-tool` command), which talks to GNOME Keyring, KDE Wallet, or any Secret Service API provider via D-Bus.

root@kitploit:~

```
# Debian / Ubuntu
sudo apt install libsecret-tools

# Fedora
sudo dnf install libsecret

# Arch
sudo pacman -S libsecret
```

A running D-Bus session and a keyring daemon (e.g. `gnome-keyring-daemon`) must be active. Most desktop environments handle this automatically.

### Windows

No extra dependencies. Uses the built-in Windows Credential Manager via `cmdkey` and PowerShell.

## Installation

### Homebrew (macOS / Linux)

root@kitploit:~

```
brew tap davidnussio/homebrew-tap
brew install envsec
```

### npm

root@kitploit:~

```
npm install -g envsec
```

### npx (no install)

root@kitploit:~

```
npx envsec
```

### mise

root@kitploit:~

```
mise use -g npm:envsec
```

## Usage

Most commands require a context specified with `--context` (or `-c`).
A context is a free-form label for grouping secrets — e.g. `myapp.dev`, `stripe-api.prod`, `work.staging`.

### Global options

These options are available on all commands:

* `--context`, `-c` — Context name (e.g. `myapp.dev`, `stripe-api.prod`). Also reads `ENVSEC_CONTEXT` env var
* `--debug`, `-d` — Enable debug logging
* `--json` — Output in JSON format for scripting
* `--db` — Path to SQLite database file (default: `~/.envsec/store.sqlite`). Also reads `ENVSEC_DB` env var

### Custom database path

By default, metadata is stored at `~/.envsec/store.sqlite`. You can override this with `--db` or the `ENVSEC_DB` environment variable:

root@kitploit:~

```
# Use a project-local database
envsec --db ./local-store.sqlite -c myapp.dev list

# Or via environment variable
export ENVSEC_DB=/shared/team/envsec.sqlite
envsec -c myapp.dev list
```

The `--db` flag takes precedence over `ENVSEC_DB`. Use cases include per-project databases, team-shared databases on network drives, and CI/CD with ephemeral storage.

### Add a secret

Store a secret in the OS credential store.

* `<key>` — Secret key name (e.g. `api.key`, `db.password`)
* `--value`, `-v` — Value to store (omit for interactive masked prompt)
* `--expires`, `-e` — Expiry duration (e.g. `30m`, `2h`, `7d`, `4w`, `3mo`, `1y`)

root@kitploit:~

```
# Store a value inline
envsec -c myapp.dev add api.key --value "sk-abc123"

# Or use the short alias
envsec -c myapp.dev add api.key -v "sk-abc123"

# Omit --value for an interactive masked prompt
envsec -c myapp.dev add api.key

# Set an expiry duration with --expires (-e)
envsec -c myapp.dev add api.key -v "sk-abc123" --expires 30d

# Supported duration units: m (minutes), h (hours), d (days), w (weeks), mo (months), y (years)
# Combinable: 1y6mo, 2w3d, 1d12h
envsec -c myapp.dev add api.key -v "sk-abc123" -e 6mo
```

### Get a secret

Retrieve a secret value from the OS credential store.

* `<key>` — Secret key name to retrieve
* `--quiet`, `-q` — Print only the raw value (no warnings or extra output)
* `--json` — Output in JSON format (includes context, key, value, expires\_at)

root@kitploit:~

```
envsec -c myapp.dev get api.key

# Print only the raw value (no warnings or extra output)
envsec -c myapp.dev get api.key --quiet
envsec -c myapp.dev get api.key -q
```

### Delete a secret

Remove a secret from the OS credential store.

* `<key>` — Secret key name to delete (optional if `--all` is used)
* `--yes`, `-y` — Skip confirmation prompt
* `--all` — Delete all secrets in the context

root@kitploit:~

```
envsec -c myapp.dev delete api.key

# or use the alias
envsec -c myapp.dev del api.key
```

### Rename a secret

Rename a secret key within the same context. The value and expiry metadata are preserved.

* `<old-key>` — Current secret key name
* `<new-key>` — New secret key name
* `--force`, `-f` — Overwrite target if it already exists

root@kitploit:~

```
# Rename a key
envsec -c myapp.dev rename old.key new.key

# Overwrite target if it already exists
envsec -c myapp.dev rename old.key existing.key --force
```

### List all secrets in a context

List all secret keys and metadata in a context.

* `--json` — Output in JSON format

root@kitploit:~

```
envsec -c myapp.dev list
```

### List all contexts

List all available contexts with secret counts.

* `--json` — Output in JSON format

root@kitploit:~

```
# Without --context, lists all available contexts with secret counts
envsec list
```

### Search secrets

Search secrets or contexts using glob patterns.

* `<p...