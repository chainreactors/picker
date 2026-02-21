---
title: Turn Dependabot Off
url: https://words.filippo.io/dependabot/
source: Filippo Valsorda
date: 2026-02-20
fetch_date: 2026-02-21T04:00:25.868761
---

# Turn Dependabot Off

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

20 Feb 2026

# Turn Dependabot Off

Dependabot is a noise machine. It makes you feel like you’re doing work, but you’re actually discouraging more useful work. This is *especially* true for security alerts in the Go ecosystem.

I recommend turning it off and replacing it with a pair of scheduled GitHub Actions, one running govulncheck, and the other running your test suite against the latest version of your dependencies.

## A little case study

On Tuesday, I [published a security fix](https://github.com/FiloSottile/edwards25519/security/advisories/GHSA-fw7p-63qq-7hpr) for [filippo.io/edwards25519](https://filippo.io/edwards25519). The `(*Point).MultiScalarMult` method would produce invalid results if the receiver was not the identity point.

A lot of the Go ecosystem depends on filippo.io/edwards25519, mostly through [github.com/go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) (228k dependents only on GitHub). [Essentially no one uses `(*Point).MultiScalarMult`.](https://github.com/search?q=%22filippo.io%2Fedwards25519%22+%2F%5C.MultiScalarMult%2F+language%3AGo+-path%3A*_test.go&type=code)

Yesterday, Dependabot opened [thousands of PRs](https://github.com/search?q=%22d1c650a+extra%3A+initialize+receiver+in+MultiScalarMult%22&type=pullrequests) against unaffected repositories to update filippo.io/edwards25519. These PRs were accompanied by a security alert with [a nonsensical, made up CVSS v4 score](https://github.com/advisories/GHSA-fw7p-63qq-7hpr) and by a worrying [73% compatibility score](https://github.com/C2SP/wycheproof/pull/220), allegedly based on the breakage the update is causing in the ecosystem. Note that the diff between v1.1.0 and v1.1.1 is [one line in the method no one uses](https://github.com/FiloSottile/edwards25519/compare/v1.1.0...v1.1.1#diff-0d9d6ab39182b0d5344623ba5d70c2db0e05607b28b9f77067a7120d1ccdeb49).

![the Dependabot alert](https://assets.buttondown.email/images/e10daca1-9504-4b3e-bbf5-71b3262b55a1.png?w=960&fit=max)

We even got [one of these alerts](https://github.com/C2SP/wycheproof/pull/220) for the Wycheproof repository, which *does not import the affected filippo.io/edwards25519 package at all*. Instead, it only imports the unaffected filippo.io/edwards25519/field package.

```
$ go mod why -m filippo.io/edwards25519
# filippo.io/edwards25519
github.com/c2sp/wycheproof/tools/twistcheck
filippo.io/edwards25519/field
```

We have turned Dependabot off.

## Use a serious vulnerability scanner instead

But isn’t this toil unavoidable, to prevent attackers from exploiting old vulnerabilities in your dependencies? Absolutely not!

Computers are perfectly capable of doing the work of filtering out these irrelevant alerts for you. The [Go Vulnerability Database](https://go.dev/doc/security/vuln/) has rich version, package, *and symbol* metadata for all Go vulnerabilities.

Here’s [the entry for the filippo.io/edwards25519 vulnerability](https://pkg.go.dev/vuln/GO-2026-4503), also available in [standard OSV format](https://vuln.go.dev/ID/GO-2026-4503.json).

```
modules:
    - module: filippo.io/edwards25519
      versions:
        - fixed: 1.1.1
      vulnerable_at: 1.1.0
      packages:
        - package: filippo.io/edwards25519
          symbols:
            - Point.MultiScalarMult
summary: Invalid result or undefined behavior in filippo.io/edwards25519
description: |-
    Previously, if MultiScalarMult was invoked on an
    initialized point who was not the identity point, MultiScalarMult
    produced an incorrect result. If called on an
    uninitialized point, MultiScalarMult exhibited undefined behavior.
cves:
    - CVE-2026-26958
credits:
    - shaharcohen1
    - WeebDataHoarder
references:
    - advisory: https://github.com/FiloSottile/edwards25519/security/advisories/GHSA-fw7p-63qq-7hpr
    - fix: https://github.com/FiloSottile/edwards25519/commit/d1c650afb95fad0742b98d95f2eb2cf031393abb
source:
    id: go-security-team
    created: 2026-02-17T14:45:04.271552-05:00
review_status: REVIEWED
```

Any decent vulnerability scanner will *at the very least* filter based on the package, which requires a simple `go list -deps ./...`. This already silences a lot of noise, because it’s common and good practice for modules to separate functionality relevant to different dependents into different sub-packages.[1](#fn:pkgdeps) For example, it would have avoided the false alert against the Wycheproof repository.

If you use a third-party vulnerability scanner, you should demand at least package-level filtering.

*Good* vulnerability scanners will go further, though, and filter based on the reachability of the vulnerable *symbol* using static analysis. That’s what [govulncheck](https://go.dev/doc/tutorial/govulncheck) does!

```
$ go mod why -m filippo.io/edwards25519
# filippo.io/edwards25519
filippo.io/sunlight/internal/ctlog
github.com/google/certificate-transparency-go/trillian/ctfe
github.com/go-sql-driver/mysql
filippo.io/edwards25519

$ govulncheck ./...
=== Symbol Results ===

No vulnerabilities found.

Your code is affected by 0 vulnerabilities.
This scan also found 1 vulnerability in packages you import and 2
vulnerabilities in modules you require, but your code doesn't appear to call
these vulnerabilities.
Use '-show verbose' for more details.
```

govulncheck noticed that my project indirectly depends on filippo.io/edwards25519 through github.com/go-sql-driver/mysql, which does not make the vulnerable symbol reachable, so it chose not to notify me.

If you want, you can tell it to show the package- and module-level matches.

```
$ govulncheck -show verbose,color ./...
Fetching vulnerabilities from the database...

Checking the code against the vulnerabilities...

The package pattern matched the following 16 root packages:
  filippo.io/sunlight
  filippo.io/sunlight/internal/stdlog
  [...]
Govulncheck scanned the following 54 modules and the go1.26.0 standard library:
  filippo.io/sunlight
  crawshaw.io/sqlite@v0.3.3-0.20220618202545-d1964889ea3c
  filippo.io/bigmod@v0.0.3
  filippo.io/edwards25519@v1.1.0
  filippo.io/keygen@v0.0.0-20240718133620-7f162efbbd87
  filippo.io/torchwood@v0.8.0
  [...]

=== Symbol Results ===

No vulnerabilities found.

=== Package Results ===

Vulnerability #1: GO-2026-4503
    Invalid result or undefined behavior in filippo.io/edwards25519
  More info: https://pkg.go.dev/vuln/GO-2026-4503
  Module: filippo.io/edwards25519
    Found in: filippo.io/edwards25519@v1.1.0
    Fixed in: filippo.io/edwards25519@v1.1.1

=== Module Results ===

Vulnerability #1: GO-2025-4135
    Malformed constraint may cause denial of service in
    golang.org/x/crypto/ssh/agent
  More info: https://pkg.go.dev/vuln/GO-2025-4135
  Module: golang.org/x/crypto
    Found in: golang.org/x/crypto@v0.44.0
    Fixed in: golang.org/x/crypto@v0.45.0

Vulnerability #2: GO-2025-4134
    Unbounded memory consumption in golang.org/x/crypto/ssh
  More info: https://pkg.go.dev/vuln/GO-2025-4134
  Module: golang.org/x/crypto
    Found in: golang.org/x/crypto@v0.44.0
    Fixed in: golang.org/x/crypto@v0.45.0

Your code is affected by 0 vulnerabilities.
This scan also found 1 vulnerability in packages you import and 2
vulnerabilities in modules you require, but your code doesn't appear to call
these vulnerabilities.
```

It’s easy to integrate govulncheck into your processes or scanners, either using the `govulncheck -json` CLI or the [golang.org/x/vuln/scan](https://pkg.go.dev/golang.org/x/vuln/scan) Go API.

### Replace Dependabot with a govulncheck GitHub Action

You can replace Dependabot security alerts with this GitHub Action.

```
name: govulncheck
on:
  push:
  pull_request:
  schedule: # daily at 10:22 UTC
    - cron: '22 10 * * *'
  workflow_dispatch:
permissions:
  contents: read
jobs:
  govulncheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
        with:
 ...