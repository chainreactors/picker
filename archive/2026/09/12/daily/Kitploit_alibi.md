---
title: alibi
url: https://kitploit.com/en/tools/github/owasp-noir/alibi
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:28.917433
---

# alibi

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/owasp-noir/alibi

![](https://assets.kitploit.com/production/public/tools/54803/e64a464537bd3cd0885e61980b7fd1c2d63b0e0da662d2ded43792c9e35b7a21-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Reconnaissance](/en/categories/reconnaissance)[Static Analysis](/en/categories/static-analysis)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Code Analysis](/en/categories/code-analysis)[Configuration Auditing](/en/categories/configuration-auditing)[Information Gathering](/en/categories/information-gathering)[Web Security](/en/categories/web-security)[DevSecOps](/en/categories/devsecops)[API Security](/en/categories/api-security)

![GitHub](/providers/github.png)owasp-noir/alibi

# alibi

10362 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Cross-check the views of your attack surface and find the endpoints that cannot corroborate each other.

[View Repository](https://github.com/owasp-noir/alibi)

Share

# alibi

Cross-check the views of your attack surface and find the endpoints that cannot
corroborate each other.

An endpoint should be able to account for itself. It is in the code, so a
contract should describe it. It is in the contract, so something should
implement it. It takes real traffic, so it had better exist somewhere. When one
view knows about an endpoint and the others do not, that gap is the finding.

alibi runs [OWASP noir](https://github.com/owasp-noir/noir), reads its JSON, and
compares the views against each other.

## Why this is a separate tool

Noir already reads five independent views of the same surface:

| View | Read from |
| --- | --- |

|  |  |
| --- | --- |
| **code** | 200-plus analyzers across 33 languages |
| **doc** | OpenAPI, RAML, WSDL, GraphQL SDL, AsyncAPI, gRPC, Smithy, TypeSpec, OData, OpenRPC |
| **traffic** | HAR, mitmproxy, Burp, Caido, ZAP, Postman, Insomnia, Bruno, `.http` |
| **gateway** | nginx, Apache, Envoy, Kong, Traefik, APISIX, Caddy, Istio, Kubernetes Ingress and Gateway API |
| **infra** | Terraform, CloudFormation, CDK, Serverless, Vercel, Netlify, Wrangler, Azure Functions, Kamal |

What it does not do is compare them. That is the whole job here, and it needs no
change to noir — alibi runs it once per view and joins the results.

The per-view part matters. Noir deduplicates by `(method, url)` across every
analyzer, so a Flask route and an OpenAPI path spelled identically collapse into
one endpoint carrying one technology. That is right for a discovery tool — it is
one endpoint — but it erases the corroboration this tool is built to measure,
and it erases it in the worst possible direction: the better two views agree,
the more of them vanish. Casdoor scans as 372 code endpoints and 9 documented
ones; scan its `swagger/` directory alone and the specification has 235.

`--only-techs` restricts the detector pool, so one scan per view keeps each one
whole. Which technology speaks for which view is `views.yml`; which
technologies exist is whatever `noir list techs` reports.

alibi parses no API formats of its own. Its only input is noir's JSON.

## Install

Requires [noir](https://github.com/owasp-noir/noir) **1.0.0 or newer** on
`PATH` -- that is the release where `noir list techs` became a subcommand, and
that catalog is what assigns every technology to a view. Development tracks the
current noir release. An older binary is refused by name rather than left to
fail on its first catalog read.

root@kitploit:~

```
$ uv tool install noir-alibi     # or: pipx install noir-alibi
$ alibi scan ./my-service
```

## Use

root@kitploit:~

```
$ alibi scan                                      # the working directory
$ alibi scan ./service ./contracts ./prod.har     # or wherever the views live
```

Every path is a source, scanned once per view. Point it at whatever you have —
a source tree, a spec directory, a single capture file — and the views you are
missing switch their rules off rather than flooding the report.

root@kitploit:~

```
alibi  ·  1 source  ·  377 endpoints

  code 372   doc 235

  230 corroborated -- vouched for by more than one view

  19 endpoints nearly matched another view -- these may be matching failures, not real gaps

SHADOW  Shadow API -- Implemented, but no contract describes it
  134 findings  ·  4 critical, 57 high, 62 medium, 11 low

  critical POST    /api/upload-groups        router.go:87
           upload paths carry more consequence than reads
  critical POST    /api/upload-permissions   router.go:208
  ...
  ... and 122 more (SHADOW in full: -f json)

TWO SURFACES?
  The doc view is 97% under /api, and 37 of these findings are outside it.
  If that is a separate surface the contract never covered, narrow the scan:
    alibi scan <paths> --ignore '^/(?!api(/|$))'
  If it is the same surface left undocumented, they are the findings that matter most.
```

Groups stop at twelve — the ordering is worst-first, so the tail is the least
informative part, and `-f json` has all of it.

### In CI

root@kitploit:~

```
- run: alibi scan . ./contracts -f sarif > alibi.sarif
- uses: github/codeql-action/upload-sarif@v3
  with: { sarif_file: alibi.sarif }
```

### Seeing what each view held

The report says the views disagree; `--endpoints` says what each of them
contained.

root@kitploit:~

```
$ alibi scan ./repo -f json --endpoints
```

Every view gets a list: the key, which views vouched for it, the technologies
behind it, the files, and the spelling before normalization — which is where
the difference always is when two rows should have matched and did not. It is
three to four times the rest of the payload, so it is a flag rather than the
default.

Or gate directly: `alibi scan . ./contracts --fail-on high` exits non-zero when
a finding reaches that severity. A scan noir could not read in full reports
`executionSuccessful: false`, so a degraded run does not pass as a clean one.

## How endpoints are matched

Noir keeps each framework's own route syntax rather than inventing a common one,
so the same endpoint arrives spelled several ways:

root@kitploit:~

```
python_flask   /api/users/<int:user_id>
aiohttp        /users/{id}
java_spring    /api/catalog/{id}
oas3           /v1/pets/{petId}
rails          /posts/:id
nginx          /admin/.*
```

The rule that makes these comparable: **a path parameter's name is not part of
its identity.** `{petId}` and `<int:user_id>` describe the same slot; only its
position and whether it spans a `/` matter. Names are kept as evidence and
reported, but never reach the key.

Findings say how the match was made:

| Grade | Meaning |
| --- | --- |
| `G1` | the spellings already agreed |
| `G2` | they agree once parameter syntax is normalized |
| `G0` | only one view has it — nothing was matched |

## What keeps it honest

A tool like this dies by reporting hundreds of findings on its first run, or by
reporting progress nobody made. Six things push back:

**Rules do not fire without both views.** Scan a codebase with no contr...