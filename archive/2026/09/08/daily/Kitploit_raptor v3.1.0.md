---
title: raptor v3.1.0
url: https://kitploit.com/en/posts/github-gadievron-raptor-v310
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:55:23.744097
---

# raptor v3.1.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9945/01af21fe357b02be600095405e38ff7f010979a17b1f697900cad13d3888ed45.png)

New releaseSep 8, 2026

# raptor v3.1.0

Autonomous security research framework integrating static analysis, binary analysis, fuzzing, LLM-powered vulnerability validation, exploit generation, and patch writing for offensive and defensive operations.

Share

root@kitploit:~

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║             ██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗             ║
║             ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗            ║
║             ██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝            ║
║             ██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗            ║
║             ██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║            ║
║             ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝            ║
║                                                                           ║
║             Autonomous Offensive/Defensive Research Framework             ║
║             Based on Claude Code (v3.1.0)                                 ║
║                                                                           ║
║             Gadi Evron, Daniel Cuthbert, Thomas Dullien (Halvar Flake)    ║
║             Michael Bargury, John Cartwright                              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠿⠿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣤⣴⣶⣶⣶⣤⣿⡿⠁⠀⠀⠀
⣀⠤⠴⠒⠒⠛⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⡟⠻⢿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢿⣿⠟⠀⠸⣊⡽⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⡁⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣧⠀ Get them bugs.....⠀⠀⠀⠀⠀
```

[![](https://github.com/gadievron/raptor/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/gadievron/raptor/actions/workflows/github-code-scanning/codeql)

**Authors:** Gadi Evron, Daniel Cuthbert, Thomas Dullien (Halvar Flake), Michael Bargury, John Cartwright
([@gadievron](https://github.com/gadievron), [@danielcuthbert](https://github.com/danielcuthbert), [@thomasdullien](https://github.com/thomasdullien), [@mbrg](https://github.com/mbrg), [@grokjc](https://github.com/grokjc))

**Licence:** MIT, see LICENSE. Note that CodeQL has its own licence and does not permit commercial use.

**Repository:** <https://github.com/gadievron/raptor>

---

## What is RAPTOR?

RAPTOR is an autonomous security research framework built on top of Claude Code (but not tied to it -- you can plug in your own analysis layer too). It chains together static analysis, binary analysis, LLM-powered vulnerability validation, exploit generation, and patch writing into a single workflow you can run against a codebase or binary.

It is not polished software. It was built in free time, held together with enthusiasm and duct tape, and it works well enough that we can't stop using it. If you want to make it better, open a PR.

RAPTOR stands for Recursive Autonomous Penetration Testing and Observation Robot. We really wanted to call it RAPTOR.

### How it's built

RAPTOR is mostly AI-generated code. The humans set direction, review
output, and make design decisions; the AI writes the implementation.
Mechanical verification (tests, static analysis, corpus calibration) keeps
the quality bar where it needs to be regardless of who — or what — wrote
the code.

---

## Prerequisites

* **Claude Code** with an active subscription (Max, Pro, Team, or Enterprise) or an Anthropic API key. This is the orchestration layer -- RAPTOR runs inside a Claude Code session.
* **Python 3.10+** and **Node.js 18+**.
* **Semgrep** (`pip install semgrep`) for static analysis. CodeQL is optional but recommended.

For the analysis dispatch layer (the LLM that analyses individual findings), Claude Code itself handles everything by default -- no extra API keys needed. If you want multi-model analysis (e.g. Claude + GPT + Gemini), you will need API keys for each provider. See [Using a different LLM](#using-a-different-llm) below.

## Quick Start

### Option 1: Install manually

root@kitploit:~

```
# Clone the repo
git clone https://github.com/gadievron/raptor.git
cd raptor

# Install Python dependencies
pip install -r requirements.txt

# Install Claude Code (if you don't already have it)
npm install -g @anthropic-ai/claude-code

# Install Semgrep (required for scanning)
pip install semgrep

# Add the launcher to your PATH -- put this in your shell profile to make it
# permanent. Append rather than prepend, so system directories stay ahead of
# the repo. (Alternatively, symlink bin/raptor into a directory already on PATH.)
export PATH="$PATH:$PWD/bin"

# Launch RAPTOR
raptor
```

The `raptor` launcher is the recommended way to start a session, and it works from any directory -- it resolves the RAPTOR installation, remembers the directory you launched from (so commands like `/scan` default to it), runs the pre-flight trust and project checks, loads the coverage-tracking plugin, and sanitises the environment before handing off to Claude Code. It also takes an optional target path and flags like `--project`, `--continue`, and `--model` -- see `raptor --help`.

Running plain `claude` from inside the repo directory also works -- Claude Code picks up RAPTOR's configuration from the checkout -- but you skip everything the launcher does above: no pre-flight checks, no coverage tracking, and commands that default to "the directory you ran this from" can't see it.

**Important:** RAPTOR loads its configuration from the repo directory. If you run `claude` from any other directory, you get plain Claude Code, not RAPTOR. The `raptor` launcher avoids this failure mode entirely.

### Option 2: Run in a container (recommended)

Using containers is a common security practice to restrict agents from accessing areas of your filesystem you don't want them to, as well as limiting the blast radius of any malicious code that may execute (e.g via supply-chain attack). The image is large (around 6 GB). It starts from the Microsoft Python 3.12 devcontainer and adds static analysis, fuzzing, and browser automation tooling.

You can pull down a pre-built image:

root@kitploit:~

```
docker pull danielcuthbert/raptor:latest
```

or build it locally using the included `Dockerfile`:

root@kitploit:~

```
docker build -f .devcontainer/Dockerfile -t raptor:latest .
```

The image expects the RAPTOR framework (this repo) to be mounted into `/workspaces/raptor` on startup. You can optionally mount a target folder for local analysis.

To start the container:

root@kitploit:~

```
docker run -it \
  -v "$(pwd):/workspaces/raptor" \
  raptor:latest
```

To mount a target folder as well:

root@kitploit:~

```
docker run -it \
  -v "$(pwd):/workspaces/raptor" \
  -v "/path/to/target-folder:/workspaces/target" \
  raptor:latest
```

Add `--privileged` if you need the `rr` deterministic debugger.

VS Code devcontainers are also supported. To mount a target folder, add it to the `mounts` section of `.devcontainer/devcontainer.json`:

root@kitploit:~

```
"mounts": [
  // ...existing entries...
  "source=/path/to/target-folder,target=/workspaces/target,type=bind,consistency=cached"
]
```

Then open the repo in VS Code — it will prompt you to reopen in the container:

root@kitploit:~

```
cd /path/to/raptor
code .
```

Either way, once you're inside the container, run `raptor` to get started.

---

## What to expect on a ...