---
title: preflight v0.22.0
url: https://kitploit.com/en/posts/github-preflightsh-preflight-v0220
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:54:46.948840
---

# preflight v0.22.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/10544/49f8f3bf619108faefecbf37b4481f68645a048498dc4c64d1d047f94a1ecc34.png)

New releaseSep 8, 2026

# preflight v0.22.0

Go-based CLI tool that scans codebases for launch readiness, detecting missing configuration, security hygiene issues, secret leaks, and integration gaps before production deployment.

Share

# Preflight.sh

[![Agent skill on skills.sh](https://skills.sh/b/preflightsh/preflight)](https://skills.sh/preflightsh/preflight)

[Preflight.sh](https://preflight.sh/) is a command-line tool that scans your codebase for launch readiness. Identifies missing configuration, integration issues, security concerns, SEO metadata gaps, and other common mistakes before you deploy to production.

Don't embarrass yourself in production. Just run the command.

## Installation

### Homebrew (macOS/Linux)

root@kitploit:~

```
brew install preflightsh/preflight/preflight
```

### npm

root@kitploit:~

```
npm install -g @preflightsh/preflight
```

### Go

root@kitploit:~

```
go install github.com/preflightsh/preflight@latest
```

### Docker

root@kitploit:~

```
docker pull ghcr.io/preflightsh/preflight
```

### Shell Script

root@kitploit:~

```
curl -sSL https://preflight.sh/install.sh | sh
```

### Manual Download

Download the latest release from [GitHub Releases](https://github.com/preflightsh/preflight/releases).

## Quick Start

root@kitploit:~

```
# Initialize in your project directory
cd your-project
preflight init

# Run all checks
preflight scan

# Scan a specific directory
preflight scan /path/to/project

# Run with verbose output (shows which files matched each check)
preflight scan --verbose
preflight scan -v  # short form

# Run in CI mode with JSON output
preflight scan --ci --format json

# Run only specific checks, or skip some, for fast iteration
# (one-off; unlike `preflight ignore` it doesn't change preflight.yml)
preflight scan --only seo_meta,og_twitter
preflight scan --skip vulnerability,secrets

# Silence a check
preflight ignore sitemap

# Unsilence a check
preflight unignore sitemap

# List all check IDs
preflight checks
```

## Agent Skill

This repo includes a skills.sh-compatible agent skill at [`skills/preflight/SKILL.md`](https://github.com/preflightsh/preflight/blob/main/skills/preflight/SKILL.md). It gives coding agents a repeatable Preflight workflow: inspect `preflight.yml`, run CI-safe scans, triage findings, avoid unsafe ignores, rerun validation, and report residual launch risk.

List the skill from this repository:

root@kitploit:~

```
# With Bun
bunx --yes skills add preflightsh/preflight --list

# Or with npm
npx --yes skills add preflightsh/preflight --list
```

Install only the Preflight skill:

root@kitploit:~

```
# With Bun
bunx --yes skills add preflightsh/preflight --skill preflight

# Or with npm
npx --yes skills add preflightsh/preflight --skill preflight
```

## Dashboard & AI Suggestions

Preflight is fully usable from the command line with no account. The optional dashboard at [app.preflight.sh](https://app.preflight.sh) adds a hosted history of your scans and AI-generated fix suggestions for each finding. Your code never leaves your machine: scanning runs locally, and only a redacted summary of results (check IDs, statuses, and messages, never secret values or file contents) is sent when you publish.

Create a free account, then connect the CLI:

root@kitploit:~

```
preflight auth login    # opens your browser to authorize this CLI
preflight auth status   # show who you're logged in as
preflight auth logout   # remove stored credentials
```

Publish a scan to your dashboard with `--publish`. It prints a link to view the run. Publishing is best-effort: if you're offline or not logged in, the scan still runs and exits normally.

root@kitploit:~

```
preflight scan --publish
```

On the dashboard you get each run's pass/warn/fail breakdown, the full list of findings, and a per-project history so you can see what changed between deploys.

You can also read that history from the terminal with `preflight history`:

root@kitploit:~

```
preflight history                       # recent runs across your projects
preflight history --here                # only the current project's runs
preflight history <run-id>              # one run's full check results
preflight history --here --format json  # machine-readable, for agents
```

Requires `preflight auth login`. `--here` matches runs to the current repository by its git remote, the same key used when publishing.

Open any failed or warning check on a published run to generate a step-by-step fix tailored to your detected stack, with copy-ready commands and code.

* **Free** includes 5 published runs per month.
* **Bring your own key:** add an OpenAI or Anthropic API key in your dashboard settings and publishing stays free and unlimited (you pay your provider directly).
* **Managed ($5/mo):** we cover the AI costs and runs are unlimited, no API key required.

## What It Checks

| Check | Description |
| --- | --- |
| **ENV Parity** | Compares `.env` and `.env.example` for missing variables |
| **Health Endpoint** | Verifies site is reachable; auto-detects `/health`, `/healthz`, `/api/health` or falls back to root |
| **Vulnerability Scan** | Checks for dependency vulnerabilities (bundle audit, npm audit, etc.) |
| **SEO Metadata** | Checks for title, description, and Open Graph tags |
| **OG & Twitter Cards** | Validates og:image, twitter:card and social sharing metadata |
| **Canonical URL** | Verifies canonical link tag is present |
| **Viewport** | Checks for proper viewport meta tag for mobile |
| **Lang Attribute** | Validates html lang attribute for accessibility |
| **Structured Data** | Checks for JSON-LD Schema.org markup |
| **Security Headers** | Validates HSTS, CSP, X-Content-Type-Options on both prod and staging |
| **SSL Certificate** | Checks SSL validity and warns before expiration |
| **WWW Redirect** | Verifies www/non-www redirect to canonical URL |
| **Email Auth** | Checks SPF/DMARC DNS records for email deliverability (opt-in) |
| **Secret Scanning** | Finds leaked API keys and credentials in code |
| **Debug Statements** | Detects console.log, var\_dump, debugger left in code |
| **Error Pages** | Checks for custom 404/500 error pages |
| **Image Optimization** | Finds large images (>500KB) that hurt load times |
| **Legal Pages** | Checks for privacy policy and terms of service pages |
| **Cookie Consent** | Detects cookie consent solution (GDPR/CCPA compliance) |
| **Favicon & Icons** | Checks for favicon, apple-touch-icon (.png, .webp, .svg), and web manifest |
| **robots.txt** | Verifies robots.txt exists and has content |
| **sitemap.xml** | Checks for sitemap presence or generator |
| **llms.txt** | Checks for LLM crawler guidance file |
| **ads.txt** | Validates ads.txt for ad-supported sites (opt-in) |
| **humans.txt** | Checks for humans.txt to credit the team (opt-in) |
| **IndexNow** | Verifies IndexNow key file for faster search indexing (opt-in) |
| **LICENSE** | Checks for license file (opt-in, for open source projects) |

## Supported Services (72)

Preflight auto-detects and validates configuration for these services:

**Payments**

* Stripe, PayPal, Braintree, Paddle, LemonSqueezy

**Error Tracking & Monitoring**

* Sentry, Bugsnag, Rollbar, Honeybadger, Datadog, New Relic, LogRocket

**Email & Newsletters**

* Postmark, SendGrid, Mailgun, AWS SES, Resend, Mailchimp, Kit, Beehiiv, AWeber, ActiveCampaign, Campaign Monitor, Drip, Klaviyo, Buttondown

**Analytics**

* Plausible, Fathom, Umami, Fullres Analytics, Datafa.st Anal...