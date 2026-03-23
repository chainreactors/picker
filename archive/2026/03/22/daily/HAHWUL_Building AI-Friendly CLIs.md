---
title: Building AI-Friendly CLIs
url: https://www.hahwul.com/posts/2026/building-ai-friendly-clis/
source: HAHWUL
date: 2026-03-22
fetch_date: 2026-03-23T04:23:22.595943
---

# Building AI-Friendly CLIs

[Skip to content](#main-content)

[![HAHWUL](/images/logo.webp)](https://www.hahwul.com/)

[Posts](/posts/)
[Notes](/notes/)
[Projects](/projects/)
[About](/about/)

# Building AI-Friendly CLIs

MARCH 22, 2026

EN

[KO](/ko/posts/2026/building-ai-friendly-clis/ "Building AI-Friendly CLIs")

JSON-First Design with Schema Commands

These days, AI agents are writing code, calling tools, and even handling deployments. With that shift, the CLI is getting attention again. GUIs and web dashboards are great for humans, but from an AI agent's perspective, CLIs are a much easier interface to work with.

The thing is, most existing CLIs were designed for humans. Pretty table outputs, color codes, shorthand flags. All nice for human eyes, but painful for agents to parse. Output formats subtly change between versions, and figuring out the exact usage often means reading separate documentation.

This week, I did a major overhaul of our team's internal CLI at work, rebuilding it around JSON I/O and schema commands. The agent's task success rate jumped noticeably. Based on that experience, I want to share some thoughts on how to build AI-friendly CLIs.

## Why JSON-First Input / Output Matters for AI Agents

### Human vs AI CLI Usage Patterns

When humans use a CLI, they check `--help`, read man pages, eyeball error messages, and iterate through trial and error. Even if the output changes a bit, they adapt by reading the context. AI agents, on the other hand, take the output as a raw string and process it literally. They have to parse table-formatted output with regex, and the moment column order shifts or line breaks change, things break immediately.

```
# This is convenient for humans, but...
$ kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
my-app-7d4b8c6f5-x2k9z  1/1     Running   0          3d

# This is what agents need
$ kubectl get pods -o json
{
  "items": [{
    "metadata": {"name": "my-app-7d4b8c6f5-x2k9z"},
    "status": {"phase": "Running", "containerStatuses": [{"ready": true}]}
  }]
}
```

### The Pain of Unstructured Text Output

Unstructured text output causes more problems for agents than expected. Here are some patterns I actually ran into:

* Inconsistent parsing: sometimes the output has headers, sometimes it doesn't
* Locale dependency: date/number formats change based on system locale
* Color code pollution: ANSI escape codes sneak in and break string comparisons
* Progress bar collisions: stderr and stdout get mixed up, garbling the output
* Silent truncation: long values get clipped to `...` with no way to detect it

When you start handling these edge cases one by one, your agent code ends up buried in CLI parsing logic instead of actual work.

### Advantages of JSON

JSON I/O solves most of these.

* Type safety: numbers are numbers, strings are strings. You can distinguish `"3"` from `3`
* Schema-based validation: define and validate input/output shapes upfront with JSON Schema
* Easy chaining: instantly parseable by `jq`, pipelines, and any programming language
* Consistency: identical output regardless of locale or terminal settings
* Structured errors: return errors as JSON so agents can identify error types and respond appropriately

```
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Pod 'my-app' not found in namespace 'default'",
    "suggestions": ["Check namespace with --namespace flag"]
  }
}
```

### Real-World Test Results from Our Project

Here's a quick summary of what changed after adding a `--json` flag to the CLI and having agents perform the same tasks:

| Metric | Text Output | JSON Output |
| --- | --- | --- |
| Task success rate | Around 60% | Around 90% |
| Average retries | 2.3 times | 0.4 times |
| Parsing-related errors | 41% of all errors | Nearly 0% |

These numbers are from specific tasks I tested, so your mileage may vary. Still, just switching to JSON making this much difference was surprising.

## The Schema Command – Letting AI Learn and Adapt at Runtime

JSON I/O alone is a huge improvement, but there's a way to take it one step further: the schema command.

### Inspiration from Google Workspace CLI (gws)

This idea was inspired by [Google Workspace CLI (gws)](https://github.com/googleworkspace/cli). gws has a structure that lets you query schema information per resource at runtime. Looking at that, I thought: "Why not let the agent ask the CLI directly instead of reading documentation?"

### How the Schema Subcommand Works

The concept is simple. Add a `schema` subcommand to your CLI — specify a resource and action, and it returns the JSON Schema for that command's input and output.

```
$ mytool schema user.create
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "description": "Create a new user",
  "input": {
    "type": "object",
    "required": ["email", "role"],
    "properties": {
      "email": {"type": "string", "format": "email"},
      "role": {"type": "string", "enum": ["admin", "member", "viewer"]},
      "name": {"type": "string", "maxLength": 100}
    }
  },
  "output": {
    "type": "object",
    "properties": {
      "id": {"type": "string", "format": "uuid"},
      "email": {"type": "string"},
      "role": {"type": "string"},
      "created_at": {"type": "string", "format": "date-time"}
    }
  }
}
```

Even better if you can also query the list of available resources:

```
$ mytool schema --list
["user.create", "user.delete", "user.get", "user.list", "project.create", ...]
```

### Benefits for Agents

* No external docs needed: agents can query the CLI directly and construct accurate inputs
* Auto-adapts to API changes: when the CLI updates, the schema updates with it, so agents always work against the latest spec
* Pairs with dry-run: build input from the schema, validate with `--dry-run`, then execute
* Self-describing: the CLI can describe itself without needing a separate AGENTS.md or tool description

### Our Implementation Overview

In our project, we implemented it with the following structure:

1. Define input/output schemas on each command handler (based on Pydantic models)
2. The `schema` subcommand serializes these into JSON Schema and returns them
3. A `--list` option allows browsing the full resource/action tree
4. Include an `examples` field in schema responses so agents have something to reference

The implementation itself wasn't particularly difficult. Since we were already defining input/output models with Pydantic, most of it was solved just by calling `.model_json_schema()`.

### Example Agent Workflow Using Schema

Here's what the actual flow looks like when an agent uses the schema:

```
1. Agent: mytool schema --list
   → Check available commands

2. Agent: mytool schema user.create
   → Check input schema (required fields: email, role)

3. Agent: mytool user create --json '{"email":"new@example.com","role":"member"}' --dry-run
   → Validate before execution

4. Agent: mytool user create --json '{"email":"new@example.com","role":"member"}'
   → Execute, receive JSON response

5. Agent: Use the id field from the response for the next task
```

Throughout this entire flow, the agent never references documentation once. The CLI itself serves as the documentation.

## Practical Design Patterns

Some patterns worth considering when applying JSON I/O and Schema.

### Input Design Choices

Roughly three input approaches, pick based on the situation:

| Approach | Example | Best For |
| --- | --- | --- |
| stdin JSON | `echo '{"key":"val"}' | mytool create` | Large payloads, pipeline chaining |
| argument JSON | `mytool create --json '{"key":"val"}'` | Single command execution, keeping it in shell history |
| Mixed | `mytool create --name foo --json '{"extra":"opts"}'` | Frequently used options as flags, the rest as JSON |

Personally, I'd recommend argument JSON as the default with stdin support as well. From an agent's perspective, a self-contained single command is the easiest to work with.

### Output Design Bes...