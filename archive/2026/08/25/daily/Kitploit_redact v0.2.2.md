---
title: redact v0.2.2
url: https://kitploit.com/en/posts/gitlab-phpboyscoutgo-redact-v022
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:15.779275
---

# redact v0.2.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/49608/c243ece7e4d7774b78eab3ed5b6d7ba715a1a8fad279995a0d1455779e716238.png)

New releaseAug 25, 2026

# redact v0.2.2

Zero-dependency Go library stripping credential-like patterns (API keys, JWTs, Authorization headers, URL userinfo) before they reach logs/telemetry.

Share

# redact

**Strip credential-like content from free-form strings before they reach logs, telemetry, or any third-party surface**

[![Go Reference](https://pkg.go.dev/badge/gitlab.com/phpboyscout/go/redact.svg)](https://pkg.go.dev/gitlab.com/phpboyscout/go/redact)
[![Pipeline](https://gitlab.com/phpboyscout/go/redact/badges/main/pipeline.svg)](https://gitlab.com/phpboyscout/go/redact/-/pipelines)
[![Coverage](https://gitlab.com/phpboyscout/go/redact/badges/main/coverage.svg)](https://gitlab.com/phpboyscout/go/redact/-/graphs/main/charts)
[![phpboyscout Go toolkit](https://img.shields.io/badge/phpboyscout-Go%20toolkit-554488?logo=gitlab&logoColor=white)](https://go.phpboyscout.uk)

*Part of the [phpboyscout Go toolkit](https://go.phpboyscout.uk) — small, framework-free Go modules extracted from [go-tool-base](https://gitlab.com/phpboyscout/go-tool-base). Docs: [redact.go.phpboyscout.uk](https://redact.go.phpboyscout.uk)*

---

`gitlab.com/phpboyscout/go/redact` redacts credential-like content from free-form
strings **at the boundary** between trusted and untrusted observability surfaces —
telemetry vendors, log aggregators, metric stores. Error messages, command
arguments, and HTTP header values routinely carry secrets by accident (a URL with
embedded userinfo, an `--api-key=sk-…` flag in `os.Args`, an `Authorization`
header quoted in an export error). Route those through `redact.String` on the way
out and they never leave the process in the clear.

## Design

* **Zero dependencies.** Pure standard library (`regexp`, `strings`) — nothing but
  the module enters your graph. A `depfootprint_test.go` guard enforces it.
* **Boundary redaction.** Sanitise where data leaves the host, not everywhere.
* **Conservative by default.** The opaque-token fallback requires ≥41 chars so it
  never false-positives on UUIDs, MD5, or SHA-1.

## Install

root@kitploit:~

```
go get gitlab.com/phpboyscout/go/redact
```

## Usage

root@kitploit:~

```
import "gitlab.com/phpboyscout/go/redact"

safe := redact.String("failed calling https://user:[email protected]?api_key=sk-abc123…")
// → credentials in the URL userinfo, the api_key query param, and the sk- token are masked

msg := redact.Error(err) // redact.String applied to err.Error() (nil-safe)

if redact.IsSensitiveHeaderKey("Authorization") { /* … redact this header's value … */ }
```

`redact.String` strips URL userinfo for any scheme (`https://`, `postgres://`,
`redis://`, …), credential `name=value` assignments, JSON credential fields such
as `"access_token"` and `"client_secret"`, `Authorization`-header tokens, JWTs,
well-known provider prefixes (`sk-`, `ghp_`, `glpat-`, `AIza`, `AKIA`, Slack),
and long opaque tokens. `SensitiveHeaderKeys` / `IsSensitiveHeaderKey` identify
headers whose values should be redacted.

## Limitations

Pattern catalogues never reach 100% recall, and this one is deliberately
conservative:

* **No configuration.** You cannot add, disable or reorder a pattern — the
  package exports four symbols and nothing to tune. Compose around it instead.
* **`String` does not mask arbitrary header values.** It knows `Authorization:`
  and nothing else; `X-API-Key: …` passes through. That is what the header
  symbols are for.
* **Bespoke and short secrets slip through.** The catch-all fallback needs 41
  characters, and each provider prefix has a hard minimum length.
* **Patterns are ASCII-only**, and redaction is one-way — nothing to reverse and
  no record of what was replaced.

[What redact does not do](https://redact.go.phpboyscout.uk/explanation/limitations/)
states the full boundary.

## Documentation

Full guides, reference and threat model:
**[redact.go.phpboyscout.uk](https://redact.go.phpboyscout.uk)**.
Generated API docs and runnable examples:
**[pkg.go.dev](https://pkg.go.dev/gitlab.com/phpboyscout/go/redact)**.

## License

See [LICENSE](https://gitlab.com/phpboyscout/go/redact/-/blob/main/LICENSE).

[Read more](/en/tools/gitlab/phpboyscout/go/redact?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[Privacy](/en/categories/privacy)[Secret Detection](/en/categories/secret-detection)[Log Analysis](/en/categories/log-analysis)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories