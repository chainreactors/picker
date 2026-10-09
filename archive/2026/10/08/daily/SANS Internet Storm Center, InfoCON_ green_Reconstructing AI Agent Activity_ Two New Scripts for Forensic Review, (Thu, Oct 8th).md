---
title: Reconstructing AI Agent Activity: Two New Scripts for Forensic Review, (Thu, Oct 8th)
url: https://isc.sans.edu/diary/rss/33410
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-08
fetch_date: 2026-10-09T08:12:10.751326
---

# Reconstructing AI Agent Activity: Two New Scripts for Forensic Review, (Thu, Oct 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jim Clausing](/handler_list.html#jim-clausing "Jim Clausing")

Threat Level: [green](/infocon.html)

* [previous](/diary/33406)

Click [HERE](https://www.sans.org/profiles/jim-clausing) to learn more about classes Jim is teaching for SANS

# [Reconstructing AI Agent Activity: Two New Scripts for Forensic Review](/forums/diary/Reconstructing%2BAI%2BAgent%2BActivity%2BTwo%2BNew%2BScripts%2Bfor%2BForensic%2BReview/33410/)

**Published**: 2026-10-08. **Last Updated**: 2026-10-08 16:52:53 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/Reconstructing%2BAI%2BAgent%2BActivity%2BTwo%2BNew%2BScripts%2Bfor%2BForensic%2BReview/33410/#comments)

We just did a major update to FOR577 and added a lot of new material on day 5 about investigating AI usage in incident response. In the new material we dicsuss 8 of the most popular AI coding assistants and agents including Claude Code, Codex, Gemini CLI, Cursor, Copilot, Warp, Windsurf, and Qwen Code. I've been using Claude Code and a little bit of Codex, but I also have recently been playing with OpenCode and am setting up Hermes. I decided to figure out where the chat history was in OpenCode and where any Hermes evidence might be located.

I’ve added two new Python scripts to my GitHub repository for examining the records left behind by these two tools: `opencode-chat-replay.py`[[1](https://github.com/clausing/scripts/blob/master/opencode-chat-replay.py)] and `hermes_forensic_extract.py`[[2](https://github.com/clausing/scripts/blob/master/hermes_forensic_extract.py)]. I absolutely had OpenCode write the opencode script and Hermes wrote the hermes script (which explains some of the differences between them).

Both focus on **reconstruction**, but they approach it differently. The opencode script turns stored session data into readable chat transcripts or structured exports. The Hermes script extracts a broader collection of evidence, including conversation records, model usage, API request dumps, and application logs.

These are forensic review tools, not tools for running or replaying an agent’s actions (the title of the opencode script not withstanding, opencode named it). The goal is to make recorded activity accessible for investigation: what the user asked, what the assistant returned, what tool activity was captured, and what surrounding context remains available.

Both scripts require Python 3.10 or later and use only the Python standard library. Both tools allow use of `--start` and `--end` (in YYYY-mm-dd [HH[:MM[:SS]]] format) to narrow the time range of the extraction, and `-f/--file` to point to a specific sqlite db (which is probably insufficient for the hermes script, so may be removed in the future), or `-d/--dir` to point to the home directory (though the `--hermes-home` switch probably does this better for the hermes script) where the evidence can be found, e.g. from a mounted image or a tarball collected from a system under investigation.

## opencode Chat Replay: From SQLite to a Readable Conversation

`opencode-chat-replay.py` reconstructs session transcripts from opencode’s SQLite database, located by default at:

~/.local/share/opencode/opencode.db

The script supports both the separate `message` and `part` tables and the newer consolidated `session_message` storage. When consolidated storage is populated for a session, it uses that instead of the separate message and part records.

That distinction matters because the transcript is more than a list of text messages. Stored turns can contain text, assistant reasoning, tool calls, completion information, errors, and token or cost accounting.

## Start with the session inventory

Running the script without a selector lists sessions. You can also request that explicitly:

python opencode-chat-replay.py --list

The listing includes session IDs, slugs, message and part counts, creation times in UTC, and titles.

From there, select the most recently created session, a specific session ID, or a slug:

# Most recently created session

./opencode-chat-replay.py --latest

# Exact session ID or unique ID prefix

./opencode-chat-replay.py --session ses\_f074ee11

# Slug selection

./opencode-chat-replay.py --slug swift-star

Ambiguous session ID prefixes abort rather than silently selecting a session. Slug selection first looks for an exact match, then uses a case-insensitive substring match.

## Readable reports or structured exports

Markdown is the default output format for this script (again, a choice made by the tool, I will probably change it to json later). Each transcript starts with session metadata, including the session ID, slug, working directory, version, timestamps, cost, tokens, and turn count.

The conversation follows in numbered role sections. Reasoning and tool calls appear in collapsible `<details>` blocks, keeping the main transcript readable while retaining access to the supporting material.

For a compact review copy:

python opencode-chat-replay.py --latest --no-reasoning --no-tools --out report.md

For structured analysis:

python opencode-chat-replay.py --slug swift-star --format json --out chat.json

JSON output contains a session object and an array of turns. One of the design goals for this script was to be able to reproduce the output of `opencode export <session>` on an investigative system where opencode was not installed. JSONL output places one turn on each line, with session metadata embedded in each record:

python opencode-chat-replay.py --all --format jsonl --out-dir ./exports/transcripts

That exports every session to a separate file named using the session date and slug.

Tool input and output rendering is capped at 2,000 characters by default. Truncation is explicitly annotated rather than silently dropping the remainder. To remove the cap:

python opencode-chat-replay.py \ --latest \ --max-tool-output 0 \ --out full-transcript.md

The `--include-children` option also attaches child-session metadata when examining sessions that have associated sub-sessions.

## Working with the exported data

The structured formats make targeted review straightforward. For example, extract user prompts from a JSON transcript:

jq -r ' .turns[] | select(.role == "user") | .parts[] | select(.type == "text") | .text ' chat.json

Or identify turns with recorded errors in JSONL:

jq -c ' select(.turn.error != null) | {id: .turn.id, role: .turn.role, error: .turn.error} ' chat.jsonl

## Source handling

Before querying SQLite, both scripts copy the sqlite database and any present `-wal` and `-shm` sidecars into a temporary directory (this works around a potential issue in opening the db read-only, that still might result in a write to the database due to partially staged results when we don't want to potentially tamper with the evidece). It opens that snapshot with SQLite’s read-only URI mode and removes the temporary directory on exit.

It does not write to or delete files in the original opencode data location. A custom database path also allows examination of a copied database:

python opencode-chat-replay.py --db /mnt/evidence/opencode.db --list

Original epoch-millisecond timestamps remain in JSON and JSONL output; Markdown renders timestamps in ISO-8601 UTC.

The script never opens `auth.json`. That does not make the resulting transcript nonsensitive: recorded tool inputs and outputs may still contain secrets.

## Hermes Forensic Extractor: Conversations Plus Supporting Artifacts

`hermes_forensic_extract.py` takes a broader extraction approach.

Its documented sources include:

* `~/.hermes/state.db` for sessions, messages, and model usage.
* `~/.hermes/sessions/request_dump_*.json` for full LLM API request and response payloads.
* `~/.hermes/logs/*.log` for agent, error, gateway, and GUI activity.

The output is newline-delimited JSON, with one JSON object per line.

Each record identifies ...