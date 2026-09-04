---
title: T-MAP
url: https://kitploit.com/en/tools/github/pwnhyo/t-map
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:36.514860
---

# T-MAP

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

T-MAP — Trajectory-aware evolutionary search framework for red-teaming LLM agents over MCP servers, generating adversarial prompts to map vulnerability landscapes across risk categories. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/pwnhyo/t-map

![](https://assets.kitploit.com/production/public/tools/53821/af7b780d42c9816dd5141b2bce67677051b9eba0327b55383340a88651ab3d83-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Penetration Testing](/en/categories/penetration-testing)[Machine Learning](/en/categories/machine-learning)[Red Teaming](/en/categories/red-teaming)[AI Security](/en/categories/ai-security)[Adversarial Attack](/en/categories/adversarial-attack)

![GitHub](/providers/github.png)pwnhyo/t-map

# T-MAP

Trajectory-aware evolutionary search framework for red-teaming LLM agents over MCP servers, generating adversarial prompts to map vulnerability landscapes across risk categories.

[View Repository](https://github.com/pwnhyo/t-map)

183165 months ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search

[![arXiv](https://img.shields.io/badge/arXiv-2603.22341-b31b1b.svg)](https://arxiv.org/abs/2603.22341)

![T-MAP Overview](https://assets.kitploit.com/production/public/readmes/53821/af7b780d42c9816dd5141b2bce67677051b9eba0327b55383340a88651ab3d83/57bf0074384562d35d60caf03e7c11d7a13470f296e9db7521048780143491c6-display-v1.webp)

**T-MAP** is a trajectory-aware evolutionary search framework for red-teaming LLM agents over MCP servers. It iteratively generates and mutates adversarial prompts guided by execution trajectories, mapping the agent's vulnerability landscape across diverse risk categories and attack styles.

---

## 🔧 Setup

root@kitploit:~

```
pip install -r requirements.txt
```

**Requirements:** Python 3.11+, API keys for attacker and target models, access to one or more MCP servers.

---

## 🚀 Quick Start

**Single server**

root@kitploit:~

```
python run_main.py \
  --server Slack \
  --attacker_model "deepseek-chat" \
  --attacker_model_api "https://api.deepseek.com" \
  --attacker_model_api_token "$DEEPSEEK_API_KEY" \
  --target_model "openai/gpt-5-mini" \
  --target_model_api "https://openrouter.ai/api/v1" \
  --target_model_api_token "$OPENROUTER_API_KEY" \
  --stdio_server_cmd npx \
  --stdio_server_args "-y slack-mcp-server@latest --transport stdio" \
  --stdio_server_envs "SLACK_MCP_XOXP_TOKEN=$SLACK_MCP_XOXP_TOKEN SLACK_MCP_ADD_MESSAGE_TOOL=true" \
  --iteration 100 \
  --mutation_n 3
```

**Multi-server**

root@kitploit:~

```
python run_main.py \
  --server "Slack,CodeExecutor" \
  --attacker_model "deepseek-chat" \
  --attacker_model_api "https://api.deepseek.com" \
  --attacker_model_api_token "$DEEPSEEK_API_KEY" \
  --target_model "openai/gpt-5-mini" \
  --target_model_api "https://openrouter.ai/api/v1" \
  --target_model_api_token "$OPENROUTER_API_KEY" \
  --stdio_server_cmd_1 npx \
  --stdio_server_args_1 "-y slack-mcp-server@latest --transport stdio" \
  --stdio_server_envs_1 "SLACK_MCP_XOXP_TOKEN=$SLACK_MCP_XOXP_TOKEN SLACK_MCP_ADD_MESSAGE_TOOL=true" \
  --stdio_server_cmd_2 docker \
  --stdio_server_args_2 "run -i --rm --workdir /app mcp-code-executor:latest" \
  --iteration 100 \
  --mutation_n 3
```

More examples in [`run_examples.sh`](https://github.com/pwnhyo/t-map/blob/main/run_examples.sh).

---

## ⚙️ Arguments

### Server Connection

| Argument | Description |
| --- | --- |
| `--server` | MCP server name(s), comma-separated for multi-server |
| `--server_config` | JSON config file for server definitions |
| `--stdio_server_cmd/args/envs` | Single-server stdio mode |
| `--stdio_server_cmd_1..8` / `_args_1..8` / `_envs_1..8` | Indexed multi-server stdio mode |
| `--remote_server_url`, `--remote_server_token` | Single remote MCP endpoint |

### Models

| Argument | Description |
| --- | --- |
| `--attacker_model/api/api_token` | Attacker LLM (generates and mutates prompts) |
| `--target_model/api/api_token` | Target LLM agent (executes prompts via MCP) |
| `--level_judge_model/api/api_token` | Judge LLM (defaults to attacker if omitted) |

### Experiment

| Argument | Default | Description |
| --- | --- | --- |
| `--iteration` | 100 | Number of mutation rounds |
| `--mutation_n` | 3 | Mutants sampled per round |
| `--max_workers` | 10 | Parallelism for generation and evaluation |
| `--query_timeout` | 300 | Per-query timeout (seconds) |
| `--checkpoint_interval` | 20 | Save checkpoint every N generations |
| `--output_dir` | `outputs` | Results and TCG snapshots |
| `--log_dir` | `logs` | Text logs |

---

## 📁 Project Layout

root@kitploit:~

```
.
├── core/
│   ├── base.py              # Experiment orchestration and evaluation
│   ├── config.py            # Risk categories and attack styles
│   ├── langchain_client.py  # LangChain-based MCP client
│   ├── llm.py               # LLM wrapper
│   └── utils.py             # CLI argument definitions
├── prompts/
│   └── tmap.py              # Seed, judge, mutate, and analysis prompts
├── run_main.py              # Entrypoint
├── run_examples.sh          # Example commands
└── requirements.txt
```

---

## 📄 Citation

root@kitploit:~

```
@article{lee2026tmapredteamingllmagents,
      title={T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search},
      author={Hyomin Lee and Sangwoo Park and Yumin Choi and Sohyun An and Seanie Lee and Sung Ju Hwang},
      year={2026},
      eprint={2603.22341},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2603.22341}
}
```

[Download Tool](https://github.com/pwnhyo/t-map)