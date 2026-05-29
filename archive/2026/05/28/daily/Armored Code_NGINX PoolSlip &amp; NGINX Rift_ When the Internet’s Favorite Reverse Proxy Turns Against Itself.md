---
title: NGINX PoolSlip &amp; NGINX Rift: When the Internet’s Favorite Reverse Proxy Turns Against Itself
url: https://armoredcode.com/blog/nginx-poolslip-nginx-rift-reverse-proxy-rce/
source: Armored Code
date: 2026-05-28
fetch_date: 2026-05-29T06:06:21.072535
---

# NGINX PoolSlip &amp; NGINX Rift: When the Internet’s Favorite Reverse Proxy Turns Against Itself

[Armored Code](/)

[Blog](/blog/)
[Newsletter](https://mailchi.mp/a61f93445c94/armored-code-newsletter)

# NGINX PoolSlip & NGINX Rift: When the Internet’s Favorite Reverse Proxy Turns Against Itself

May 2026

For nearly two decades, NGINX has been one of the silent pillars of the modern Internet.
Reverse proxies, Kubernetes ingress controllers, API gateways, WAFs, CDN edges — everywhere you look, NGINX is there.

That is precisely why the recent disclosure of **NGINX Rift** and the follow-up **NGINX PoolSlip** vulnerabilities should worry defenders far beyond the usual patch cycle.

What started as a critical heap overflow buried in the rewrite engine quickly evolved into something much larger: a reminder that memory-unsafe infrastructure software can become a single point of systemic Internet risk.

---

## The First Shock: NGINX Rift

Researchers disclosed **CVE-2026-42945**, nicknamed **NGINX Rift**, a critical heap buffer overflow affecting the `ngx_http_rewrite_module`.
The flaw reportedly existed in the codebase since **2008**.

Affected versions included:

* NGINX Open Source `0.6.27 → 1.30.0`
* NGINX Plus `R32 → R36`

The vulnerability is triggered through specific rewrite configurations involving:

* unnamed PCRE capture groups (`$1`, `$2`)
* rewrite replacement strings containing `?`
* chained rewrite/set directives

Under the right conditions, attackers could achieve:

* Worker process crashes
* Heap corruption
* Remote Code Execution (RCE)

without authentication.

---

## Why Rift Was Dangerous

The frightening part was not just the bug itself.

It was *where* the bug lived.

NGINX rewrite logic sits directly on the edge of infrastructure:

* load balancers
* ingress controllers
* reverse proxies
* API routing layers
* authentication gateways

In many environments, rewrite rules are treated as harmless operational plumbing.
In reality, they became an Internet-facing attack surface capable of memory corruption.

Even worse, exploitation was reportedly achievable through ordinary HTTP requests.

---

## Heap Corruption in the Rewrite Engine

The vulnerability allowed crafted requests to manipulate heap memory inside internal NGINX request structures.

In practical terms:

1. A malformed request reaches a vulnerable rewrite rule
2. Buffer calculations fail
3. Heap memory gets overwritten
4. Function pointers become attacker-controlled
5. NGINX executes corrupted cleanup callbacks

That turns a reverse proxy into a potential RCE primitive.

---

## Then Came PoolSlip

As administrators rushed to patch Rift, a second issue emerged:

**NGINX PoolSlip**

PoolSlip targets NGINX request memory pools (`ngx_pool_t`) and explores a different exploitation path in the memory allocator and cleanup chain.

The key concern is architectural:

> Fixing one memory corruption path did not eliminate the underlying unsafe design patterns.

PoolSlip reportedly enables:

* ASLR bypass techniques
* controlled heap corruption
* potential remote code execution

through alternative rewrite-driven execution flows.

---

## A Design Problem, Not Just a Bug

These vulnerabilities expose a broader truth:

Modern Internet infrastructure still relies heavily on memory-unsafe C code.

NGINX is fast because of:

* manual memory management
* custom allocators
* pooled request lifecycle handling

But these same decisions create long-lived attack surfaces that are extremely difficult to eliminate completely.

---

## The Rewrite Engine Is an Attack Surface

Configuration is code.

Rewrite rules are not harmless routing logic — they are part of the execution surface.

Risky patterns include:

```
rewrite ^/user/(.*)$ /profile.php?id=$1?;
set $target $1;
```

Regex capture groups and variable interpolation can turn configuration into a memory corruption trigger.

## Detection & Hardening

### Upgrade immediately

Apply vendor patches for your NGINX distribution or fork.

### Audit rewrite rules

Look for:

* $1, $2 capture usage
* chained rewrites
* ? in rewrite targets
* dynamic variable expansion

### Reduce complexity

Move routing logic out of NGINX when possible.

### Monitor crashes

Watch for:

* worker segfaults
* abnormal restarts
* request-triggered instability

## Off by one

NGINX became critical infrastructure because it is fast and flexible.

But flexibility built on unsafe memory handling comes at a cost.

Rift exposed how rewrite logic can become a corruption surface.
PoolSlip showed how quickly adjacent paths emerge.

The lesson is simple:

> The edge is not just traffic routing anymore. It is executable infrastructure.

© 2012 - 2026 Armored Code. All rights
reserved.