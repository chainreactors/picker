---
title: Statusline for Claude Code, agy, Codex, Grok
url: https://www.hahwul.com/notes/agent-cli/statusline/
source: HAHWUL
date: 2026-09-24
fetch_date: 2026-09-25T06:52:08.241561
---

# Statusline for Claude Code, agy, Codex, Grok

[Skip to content](#main-content)

[HAHWUL](https://www.hahwul.com/)

[Posts](/posts/)
[Notes](/notes/)
[Projects](/projects/)
[About](/about/)

⌘K

# Statusline for Claude Code, agy, Codex, Grok

SEPTEMBER 25, 2026

Claude Code, Antigravity CLI(agy), Codex, Grok의 statusline 설정

## Claude Code

`~/.claude/settings.json`

```
{
  "statusLine": {
    "type": "command",
    "command": "bash ~/.claude/statusline-command.sh"
  }
}
```

`~/.claude/statusline-command.sh`

```
#!/usr/bin/env bash
# Claude Code status line — model, effort, session limits, context

input=$(cat)

model_name=$(echo "$input" | jq -r '.model.display_name // empty')
effort_level=$(echo "$input" | jq -r '.effort.level // empty')
used_pct=$(echo "$input" | jq -r '.context_window.used_percentage // empty')
five_pct=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')
five_resets_at=$(echo "$input" | jq -r '.rate_limits.five_hour.resets_at // empty | if type == "number" then floor else . end')
daily_pct=$(echo "$input" | jq -r '.rate_limits.daily.used_percentage // empty')
weekly_pct=$(echo "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty')
weekly_resets_at=$(echo "$input" | jq -r '.rate_limits.seven_day.resets_at // empty | if type == "number" then floor else . end')

parts=""

# Model display name (with optional effort level)
if [ -n "$model_name" ]; then
    if [ -n "$effort_level" ]; then
        parts="${model_name} (${effort_level})"
    else
        parts="${model_name}"
    fi
fi

# 5-hour rate limit (with optional reset time as local HH:MM)
if [ -n "$five_pct" ]; then
    [ -n "$parts" ] && parts="${parts}  "
    five_label="5h:$(printf "%.0f" "$five_pct")%"
    if [ -n "$five_resets_at" ]; then
        five_time=$(date -r "$five_resets_at" "+%H:%M" 2>/dev/null)
        [ -n "$five_time" ] && five_label="${five_label}(~${five_time})"
    fi
    parts="${parts}${five_label}"
fi

# Daily rate limit
if [ -n "$daily_pct" ]; then
    [ -n "$parts" ] && parts="${parts}  "
    parts="${parts}daily:$(printf "%.0f" "$daily_pct")%"
fi

# Weekly rate limit (with optional reset time as day-of-week + HH:MM)
if [ -n "$weekly_pct" ]; then
    [ -n "$parts" ] && parts="${parts}  "
    weekly_label="weekly:$(printf "%.0f" "$weekly_pct")%"
    if [ -n "$weekly_resets_at" ]; then
        weekly_time=$(date -r "$weekly_resets_at" "+%a %H:%M" 2>/dev/null)
        [ -n "$weekly_time" ] && weekly_label="${weekly_label}(~${weekly_time})"
    fi
    parts="${parts}${weekly_label}"
fi

# Context window usage
if [ -n "$used_pct" ]; then
    [ -n "$parts" ] && parts="${parts}  "
    parts="${parts}ctx:$(printf "%.0f" "$used_pct")%"
fi

printf "%s\n" "$parts"
```

![](images/claude.webp)

## Antigravity CLI (agy)

`~/.gemini/antigravity-cli/settings.json`

```
{
  "statusLine": {
    "type": "command",
    "command": "/Users/hahwul/.gemini/antigravity-cli/statusline-command.sh",
    "enabled": true
  }
}
```

`~/.gemini/antigravity-cli/statusline-command.sh`

```
#!/usr/bin/env bash
# Antigravity CLI (agy) status line — model, effort, session quota (5h / weekly), context

input=$(cat)
[ -z "$input" ] && exit 0

eval $(echo "$input" | jq -r '
  .model.display_name as $md |
  .model.effort as $me |
  .context_window.used_percentage as $ctx |
  (if ($md // "" | ascii_downcase | contains("claude")) then "3p" else "gemini" end) as $p |
  .quota[$p + "-5h"] as $q5 |
  .quota[$p + "-weekly"] as $qw |

  [
    "model_name=" + (($md // "") | @sh),
    "effort_level=" + (($me // "") | @sh),
    "used_pct=" + (($ctx // "") | @sh),
    "five_rem_frac=" + (($q5.remaining_fraction // "") | @sh),
    "five_reset_sec=" + (($q5.reset_in_seconds // "") | @sh),
    "weekly_rem_frac=" + (($qw.remaining_fraction // "") | @sh),
    "weekly_reset_sec=" + (($qw.reset_in_seconds // "") | @sh)
  ] | join("\n")
')

now=$(date +%s)
parts=""

# Model display name (with optional effort level if not already in name)
if [ -n "$model_name" ]; then
    if [ -n "$effort_level" ] && ! echo "$model_name" | grep -qi "(${effort_level})"; then
        parts="${model_name} (${effort_level})"
    else
        parts="${model_name}"
    fi
fi

# 5-hour quota (used/reached percentage + reset local time)
if [ -n "$five_rem_frac" ]; then
    five_pct=$(awk -v f="$five_rem_frac" 'BEGIN {printf "%.0f", (1 - f) * 100}')
    [ -n "$parts" ] && parts="${parts}  "
    five_label="5h:${five_pct}%"
    if [ -n "$five_reset_sec" ] && [ "$five_reset_sec" != "null" ]; then
        five_epoch=$(( now + ${five_reset_sec%.*} ))
        five_time=$(date -r "$five_epoch" "+%H:%M" 2>/dev/null)
        [ -n "$five_time" ] && five_label="${five_label}(~${five_time})"
    fi
    parts="${parts}${five_label}"
fi

# Weekly quota (used/reached percentage + reset local day/time)
if [ -n "$weekly_rem_frac" ]; then
    weekly_pct=$(awk -v f="$weekly_rem_frac" 'BEGIN {printf "%.0f", (1 - f) * 100}')
    [ -n "$parts" ] && parts="${parts}  "
    weekly_label="weekly:${weekly_pct}%"
    if [ -n "$weekly_reset_sec" ] && [ "$weekly_reset_sec" != "null" ]; then
        weekly_epoch=$(( now + ${weekly_reset_sec%.*} ))
        weekly_time=$(date -r "$weekly_epoch" "+%a %H:%M" 2>/dev/null)
        [ -n "$weekly_time" ] && weekly_label="${weekly_label}(~${weekly_time})"
    fi
    parts="${parts}${weekly_label}"
fi

# Context window usage
if [ -n "$used_pct" ]; then
    ctx_pct=$(awk -v c="$used_pct" 'BEGIN {printf "%.0f", c}')
    [ -n "$parts" ] && parts="${parts}  "
    parts="${parts}ctx:${ctx_pct}%"
fi

printf "%s\n" "$parts"
```

![](images/agy.webp)

## Codex

`~/.codex/config.toml`

```
[tui]
status_line = ["model-with-reasoning", "five-hour-limit", "weekly-limit", "context-used"]
```

![](images/codex.webp)

## Grok

`~/.grok/config.toml`

```
[ui.status_line]
type = "command"
command = "~/.grok/statusline-command.sh"
```

`~/.grok/statusline-command.sh`

```
#!/usr/bin/env bash
# Grok status line — model, effort, cost, context

input=$(cat)

model_name=$(echo "$input" | jq -r '.model.display_name // empty')
effort_level=$(echo "$input" | jq -r '.effort.level // empty')
cost_usd=$(echo "$input" | jq -r '.cost.total_cost_usd // empty')
used_pct=$(echo "$input" | jq -r '.context_window.used_percentage // empty')

parts=""

# Model display name (with optional effort level)
if [ -n "$model_name" ]; then
    if [ -n "$effort_level" ]; then
        parts="${model_name} (${effort_level})"
    else
        parts="${model_name}"
    fi
fi

# Session cost (Grok has no rate-limit data)
if [ -n "$cost_usd" ]; then
    [ -n "$parts" ] && parts="${parts}  "
    parts="${parts}cost:\$$(printf "%.2f" "$cost_usd")"
fi

# Context window usage
if [ -n "$used_pct" ]; then
    [ -n "$parts" ] && parts="${parts}  "
    parts="${parts}ctx:$(printf "%.0f" "$used_pct")%"
fi

printf "%s\n" "$parts"
```

![](images/grok.webp)

[TAGS](/tags/)
[USES](/about/uses/)
[CONTACT](/contact/)
[SPONSOR](/sponsor/)
[FEEDS](/feeds/)
[PRIVACY](/privacy/)

Developed and Designed by Me
2026 HAHWUL.

Esc

All
Posts
Notes
Projects
Archive
Pages

All
EN
KO

Type to search posts, notes, projects and the archive.