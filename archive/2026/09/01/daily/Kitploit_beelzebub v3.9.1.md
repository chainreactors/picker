---
title: beelzebub v3.9.1
url: https://kitploit.com/en/posts/github-beelzebub-labs-beelzebub-v391
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:08.965044
---

# beelzebub v3.9.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9670/38080b103591f912d2aacf0feaf330531560f6bafc2fe8f4fbbdd42c3e60ea29.gif)

New releaseSep 1, 2026

# beelzebub v3.9.1

A secure low code deception runtime framework, leveraging AI for System Virtualization.

Share

# Beelzebub

[![CI](https://github.com/beelzebub-labs/beelzebub/actions/workflows/main.yml/badge.svg)](https://github.com/beelzebub-labs/beelzebub/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/beelzebub-labs/beelzebub/v3)](https://goreportcard.com/report/github.com/beelzebub-labs/beelzebub/v3)
[![codecov](https://codecov.io/gh/beelzebub-labs/beelzebub/graph/badge.svg?token=8XTK7D4WHE)](https://codecov.io/gh/beelzebub-labs/beelzebub)
[![Go Reference](https://pkg.go.dev/badge/github.com/beelzebub-labs/beelzebub/v3.svg)](https://pkg.go.dev/github.com/beelzebub-labs/beelzebub/v3)
[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/beelzebub-labs/beelzebub)](https://archestra.ai/mcp-catalog/beelzebub-labs__beelzebub)
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge.svg)](https://github.com/avelino/awesome-go)

**Deception Runtime Framework**

Beelzebub is an open-source deception runtime that deploys adaptive, LLM-powered decoy services across SSH, HTTP, TCP, TELNET, and MCP protocols. It goes beyond passive honeypots by actively engaging attackers in realistic interactions, collecting high-fidelity threat intelligence, and detecting prompt injection attacks against AI agents.

![github beelzebub - inception program](https://assets.kitploit.com/production/public/readmes/9670/8401fdc02c7675bd6c11555a308c25a09fc2bfe2b6eae16450a6b27242a10168.jpg)

## Table of Contents

* [Beelzebub](#beelzebub)
  + [Table of Contents](#table-of-contents)
  + [Key Features](#key-features)
  + [LLM Deception Demo](#llm-deception-demo)
  + [Quick Start](#quick-start)
    - [Installer](#installer)
    - [Local (Go)](#local-go)
    - [Docker](#docker)
    - [Using Helm (Kubernetes)](#using-helm-kubernetes)
  + [CLI Reference](#cli-reference)
    - [`beelzebub run`](#beelzebub-run)
    - [`beelzebub validate`](#beelzebub-validate)
    - [`beelzebub plugin`](#beelzebub-plugin)
    - [`beelzebub version`](#beelzebub-version)
  + [Plugin System](#plugin-system)
    - [Interfaces](#interfaces)
    - [Writing a Plugin](#writing-a-plugin)
    - [Installing External Plugins](#installing-external-plugins)
  + [Observability](#observability)
    - [Prometheus Metrics](#prometheus-metrics)
    - [RabbitMQ Integration](#rabbitmq-integration)
  + [Testing](#testing)
  + [Code Quality](#code-quality)
  + [License](#license)
  + [Contributing](#contributing)
  + [Configuration Reference](#configuration-reference)
    - [Core Configuration](#core-configuration)
    - [Service Configuration](#service-configuration)
  + [Deception Services](#deception-services)
    - [MCP Deception Service](#mcp-deception-service)
      * [How It Works](#how-it-works)
    - [HTTP Deception Service](#http-deception-service)
    - [SSH Deception Service](#ssh-deception-service)
    - [TELNET Deception Service](#telnet-deception-service)
    - [TCP Deception Service](#tcp-deception-service)
  + [Supported By](#supported-by)

## Key Features

* **Adaptive deception engine**: LLM integration (OpenAI, Ollama) generates contextually accurate responses in real time, keeping attackers engaged long enough to collect actionable TTPs
* **Low-code service definition**: YAML-based configuration with regex command matching — no custom code required to deploy a new decoy service
* **Multi-protocol coverage**: SSH, HTTP, TCP, TELNET, MCP from infrastructure targets to AI agent attack surfaces
* **Extensible plugin system**: Implement the `CommandPlugin` or `HTTPPlugin` interface and register via `init()` no core changes required
* **Full observability stack**: Prometheus metrics, RabbitMQ event streaming
* **Production-ready runtime**: Docker, Kubernetes (Helm), graceful shutdown, per-service memory limits

## LLM Deception Demo

![demo-beelzebub](https://assets.kitploit.com/production/public/readmes/9670/38080b103591f912d2aacf0feaf330531560f6bafc2fe8f4fbbdd42c3e60ea29.gif)

## Quick Start

### Installer

root@kitploit:~

```
./install.sh     # asks local or Docker, checks prerequisites, and starts it
```

Non-interactive: `./install.sh --local` or `./install.sh --docker`. Use
`./install.sh --local --no-run` to install and build without starting the local
runtime. On non-root hosts, local installation does not auto-start when the
default configuration includes privileged ports.

### Local (Go)

root@kitploit:~

```
make start     # installs any declared plugins, compiles them in, and runs
```

### Docker

root@kitploit:~

```
make docker    # builds an image with declared plugins baked in, then runs it
```

### Using Helm (Kubernetes)

root@kitploit:~

```
helm install beelzebub ./beelzebub-chart
# Upgrade:
helm upgrade beelzebub ./beelzebub-chart
```

## CLI Reference

Beelzebub ships with a structured CLI. Run `beelzebub --help` to see all available commands.

### `beelzebub run`

Start all configured deception services.

root@kitploit:~

```
beelzebub run [flags]

Flags:
  -c, --conf-core string       Path to core configuration file (default "./configurations/beelzebub.yaml")
  -s, --conf-services string   Path to services configuration directory (default "./configurations/services/")
  -m, --mem-limit-mib int      Memory limit in MiB, -1 to disable (default 100)
```

### `beelzebub validate`

Parse and validate all configuration files without starting any services. Useful in CI pipelines. See [Configuration Validation](https://github.com/beelzebub-labs/beelzebub/blob/HEAD/docs/configuration-validation.md) for the validation architecture and rule reference.

root@kitploit:~

```
beelzebub validate --conf-core ./configurations/beelzebub.yaml --conf-services ./configurations/services/
```

### `beelzebub plugin`

Install, list, and remove plugins fetched from GitHub. See [Plugin System](#plugin-system).

root@kitploit:~

```
beelzebub plugin install github.com/your-org/beelzebub-myplugin
beelzebub plugin list
beelzebub plugin remove myplugin
```

### `beelzebub version`

Print version, commit SHA, build date, and Go runtime information.

root@kitploit:~

```
beelzebub version
```

## Plugin System

Beelzebub exposes a stable public SDK at `pkg/plugin` for extending the deception runtime without modifying core code.

### Interfaces

root@kitploit:~

```
// CommandPlugin generates text responses for SSH, TCP, TELNET, and HTTP services.
type CommandPlugin interface {
    Metadata() Metadata
    Execute(ctx context.Context, req CommandRequest) (string, error)
}

// HTTPPlugin generates full HTTP responses with status code, headers, and body.
type HTTPPlugin interface {
    Metadata() Metadata
    HandleHTTP(r *http.Request) HTTPResponse
}
```

### Writing a Plugin

root@kitploit:~

```
package myplugin

import (
    "context"
    "github.com/beelzebub-labs/beelzebub/v3/pkg/plugin"
)

type MyPlugin struct{}

func (p *MyPlugin) Metadata() plugin.Metadata {
    return plugin.Metadata{
        Name:        "MyPlugin",
        Description: "Custom deception response generator",
        Version:     "1.0.0",
        Author:      "your-name",
    }
}

func (p *MyPlugin) Execute(_ context.Context, req plugin.CommandRequest) (string, error) {
    return "simulated response to: " + req.Command, nil
}

func init() {
    plugin.Register(&MyPlugin{})
}
```

### Installing External Plugins

root@kitploit:~

```
# Declare plugins in configurations/plugins.yaml, or:
beelze...