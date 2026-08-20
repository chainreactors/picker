---
title: clawpatrol v0.5.9
url: https://kitploit.com/en/posts/github-denoland-clawpatrol-v059
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:15.224798
---

# clawpatrol v0.5.9

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F8440%2F673b69e3f3ecc5c95d14876450044d1424813a54e8eb469125e7d5fba33b35cc.png&w=3840&q=75)

New releaseAug 19, 2026

# clawpatrol v0.5.9

Wire-level proxy firewall for AI agents that intercepts and gates SQL, Kubernetes, and HTTP traffic using HCL rules, with per-process tunnel isolation and human-in-the-loop approval.

Share

# clawpatrol

The security firewall for agents.

Claw Patrol sits between your agents and prod, parses their traffic
at the wire, and gates each action against rules you write in HCL.
For example, you can block destructive SQL, or pause `kubectl delete pod`
until a human approves it before the request reaches Kubernetes.

For the full overview see [clawpatrol.dev](https://clawpatrol.dev).

## Install

root@kitploit:~

```
curl -fsSL https://clawpatrol.dev/install.sh | sh
```

From source: `make` (requires Go and Node.js).

## A rule

A real rule from our own production config:

root@kitploit:~

```
rule "k8s-no-secrets" {
  endpoint  = k8s-prod
  condition = "k8s.resource == 'secrets'"
  verdict   = "deny"
  reason    = "Secret values must not leave the cluster via the agent"
}
```

Conditions are CEL expressions over wire-level facts the gateway
extracts per protocol: SQL verbs and table names for Postgres /
ClickHouse, resource / verb / namespace for Kubernetes, method /
path / headers / body for HTTP. The full set of facts lives in the
[config reference](https://clawpatrol.dev/docs/config-reference).

## Run

Three deployment shapes; pick whichever fits.

root@kitploit:~

```
clawpatrol gateway config.hcl   # run the proxy itself
clawpatrol join <gateway-url>   # join a gateway
clawpatrol run claude           # wrap one agent's process tree
```

`clawpatrol run` opens a per-process tunnel on Linux (via netns) or
macOS (via NetworkExtension); only the wrapped command's traffic
goes through the gateway. `clawpatrol join` brings up a WireGuard
tunnel that routes the whole host. `clawpatrol gateway` is the
proxy: a single binary that loads your HCL config and accepts
clients tunneling in via WireGuard or Tailscale.

## Configure

[clawpatrol.dev/docs/getting-started](https://clawpatrol.dev/docs/getting-started)
walks through a first config end-to-end.
[clawpatrol.dev/docs/config-reference](https://clawpatrol.dev/docs/config-reference)
is the auto-generated field reference. See
[`gateway.example.hcl`](https://github.com/denoland/clawpatrol/blob/HEAD/examples/gateway.example.hcl) for an
annotated starting template.

## License

MIT. See [LICENSE.md](https://github.com/denoland/clawpatrol/blob/HEAD/LICENSE.md).

[Read more](/en/tools/github/denoland/clawpatrol?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[Container Security](/en/categories/container-security)[Web Proxies & Interception](/en/categories/web-proxies-interception)[IDS/IPS Evasion](/en/categories/ids-ips-evasion)[API Security Testing](/en/categories/api-security-testing)[Network Security](/en/categories/network-security)[Cloud Security](/en/categories/cloud-security)[Misconfiguration](/en/categories/misconfiguration)[API Security](/en/categories/api-security)

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

clawpatrol v0.5.9 — Wire-level proxy firewall for AI agents that intercepts and gates SQL, Kubernetes, and HTTP traffic using HCL rules, with per-process tunnel isolation and human-in-the-loop approval. | Kitploit