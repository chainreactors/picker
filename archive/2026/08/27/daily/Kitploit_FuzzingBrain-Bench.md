---
title: FuzzingBrain-Bench
url: https://kitploit.com/en/tools/github/fuzzingbrain/fuzzingbrain-bench
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:39.774655
---

# FuzzingBrain-Bench

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/fuzzingbrain/fuzzingbrain-bench

![](https://assets.kitploit.com/production/public/tools/53253/e5761331c1984c7d06618d2048ca1c092ff35fc306c2624334bd5129f018d25e-display-v1.webp)

[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Fuzzing](/en/categories/fuzzing)[Learning & Education](/en/categories/education)[AI Security](/en/categories/ai-security)[Labs & Practice](/en/categories/labs-practice)

![GitHub](/providers/github.png)fuzzingbrain/fuzzingbrain-bench

# FuzzingBrain-Bench

A sealed benchmark for LLM-driven bug discovery: 77 challenges across 43 open-source projects (C/C++/Java). Each challenge is an answer-free Docker image with in-image grading — no patch, Poc or answer key ships.

[View Repository](https://github.com/fuzzingbrain/fuzzingbrain-bench)

43367 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# FuzzingBrain Bench

**A benchmark for LLM-driven vulnerability reproduction on 77 real zero-day
bugs across 43 open-source projects (C / C++ / Java).**

Each challenge gives the agent only the **fuzz harness** (the target) and the
project source at the vulnerable revision — no patch, no fix commit, no target
line. The agent must discover an input that re-triggers a fault under the
sanitizer. Every grade is **deterministic** (no LLM-as-judge) and happens
**in-image and offline**: the candidate runs through the official
sanitizer-instrumented harness baked into the challenge container, and the run
is scored by the distinct crashes the agent triggered. Nothing leaves the
machine and no service has to be up.

| Challenges | Projects | Languages | Grader |
| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
| **77** end-to-end | **43** | C · C++ · Java | deterministic — in-image, offline |

Nothing in the images or this repository reveals what a bug is — challenges are
named by neutral alias (`<project>-NN`, e.g. `avro-03`), and the answer key
(PoC, expected fault, fixed build) is in neither: it stays with the maintainer.
**Browse all 77:** [`tools/sealed/CHALLENGES.md`](https://github.com/fuzzingbrain/fuzzingbrain-bench/blob/HEAD/tools/sealed/CHALLENGES.md).

---

## Quick start

### 1. Setup

root@kitploit:~

```
git clone https://github.com/fuzzingbrain/FuzzingBrain-Bench
cd FuzzingBrain-Bench

python3 -m venv .venv && source .venv/bin/activate   # recommended (and required on
                                                     # Debian/Ubuntu, PEP 668)
pip install -e .                              # needs Python ≥ 3.10 and Docker

# put your model key(s) in ./.env — auto-loaded on every run, no need to export
cat > .env <<'EOF'
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
DEEPSEEK_API_KEY=sk-...
EOF

fb-bench list                                 # the 77 challenges (by alias)
fb-bench models                               # supported models + which keys are loaded
```

(`./.env` is read automatically; a plain `export ANTHROPIC_API_KEY=...` also works.)

> Re-`source .venv/bin/activate` in each new shell. Or skip the venv with
> `pip install --break-system-packages -e .` (not recommended).

`fb-bench run` pulls the public challenge image, drives the agent loop on the
host (calling your model API), and grades every candidate **inside that image** —
no network, nothing to reach. Only Docker + your model key are required, and a
run scores the **distinct crashes** the agent found — a crash's identity is its
sanitizer fault type plus its top stack frames, so the same fault hit twenty
times counts once.

> The default `--arm api` needs nothing beyond the above. The `--arm codex` and
> `--arm claudecode` backends need extra **vendor CLIs — optional**, installed
> separately (never part of `pip install -e .`); see [§4](#4-agent-modes--same-run-pick-the-backend-with---arm).

### 2. Run one challenge with a model

root@kitploit:~

```
# Claude family  (haiku is cheapest/fastest; swap in opus/sonnet for harder runs)
fb-bench run avro-03 --model claude-haiku-4-5

# GPT family
fb-bench run avro-03 --model gpt-5.5

# Gemini family
fb-bench run avro-03 --model gemini-3.1-pro-preview

# DeepSeek family  (OpenAI-compatible endpoint; needs DEEPSEEK_API_KEY)
fb-bench run avro-03 --model deepseek-v4-flash
```

Models: `claude-haiku-4-5` · `claude-sonnet-4-6` · `claude-opus-4-8` ·
`gpt-5.5` · `gpt-5.4` · `gpt-5` · `gemini-3.1-pro-preview` · `gemini-2.5-flash` ·
`deepseek-v4-pro` · `deepseek-v4-flash`
(any catalog id works via `--model`; see `fb-bench models`).

### 3. Run many — same command, one or many

`fb-bench run` takes one bug or many, one model or many. A single run is just a
matrix of size one, so there is no separate "sweep" command:

root@kitploit:~

```
# recommended full run: one model over the whole corpus, named output, PoCs
# preserved (the default) for later inspection. The agent keeps hunting past its
# first crash unless you pass --stop-on-crash
fb-bench run all --model claude-haiku-4-5 --output run1 --max-turns 100

# the curated cross-model roster, all challenges, 4 cells in parallel
fb-bench run all --model default-lineup --output sweep1 --jobs 4

# a couple of bugs, 3 samples each
fb-bench run avro-03,jq-01 --model gpt-5.5 --samples 3 --output probe

# just re-print the leaderboard from an existing run
fb-bench run all --model claude-haiku-4-5 --output run1 --report-only
```

`<bugs>` is one alias, a comma list, or `all`; `--model` is one id, a comma list,
`default-lineup`, or `all`. Results land in `output/<name>/<bug>/<model>/seed-N/`
(`score.json`, `episode.jsonl`, `transcript.jsonl`, `cost.json`, distilled
`traj.md`); a leaderboard is printed at the end. `--output` takes a bare name
(nested under `output/`) or a path (used as-is). **Every run gets its own
folder**: omit `--output` and it lands in `output/run_<timestamp>`; name a folder
that already exists and a fresh run forks `<name>_<timestamp>` rather than
resuming into it — so two runs never share results (`--report-only` is the one
reader, opening a folder in place).

### 4. Agent modes — same `run`, pick the backend with `--arm`

The three agent backends share **one entry**. `--arm` selects which one drives
the challenge; everything else (`<bugs>`, `--jobs`, `--samples`, `--output`,
the per-run folder, the leaderboard) is identical across arms.

root@kitploit:~

```
fb-bench run avro-03 --model gpt-5.5            # --arm api (default): provider model
fb-bench run avro-03 --arm codex               # OpenAI codex CLI (default gpt-5.5)
fb-bench run avro-03 --arm claudecode --model sonnet --auth sub   # Claude Code CLI
fb-bench run all     --arm codex --jobs 4      # whole corpus, batched
```

* **`--arm codex`** drives OpenAI's `codex exec` over the bench MCP server.
  `--model` sets the codex model (default `gpt-5.5`), pinned via its config.toml.
* **`--arm claudecode`** drives the Claude Code CLI. `--model` picks the claude
  model (`sonnet`/`...