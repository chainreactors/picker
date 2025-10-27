---
title: GitHub Actions is Someone Else's Computer
url: https://jbp.io/2025/05/02/github-actions-is-someone-elses-computer.html
source: jbp.io
date: 2025-05-03
fetch_date: 2025-10-06T22:26:47.529986
---

# GitHub Actions is Someone Else's Computer

[jbp.io](/)
[Archive](/archive)

02 May 2025

# GitHub Actions is Someone Else's Computer

Your project should treat GitHub Actions like Someone Else’s Computer.

What do I mean by that? Well, I view GHA runners as public, unsecured
shell boxes that I can run scripts on. They can check out and build
public code, but at no point should they be given any kind of privileges
or secrets.

Why is that? Well, I view the engineering discipline that went into
GHA as similar to PHP4-era web security in the early 2000s –
“unsafe at any speed”. They are functionally similar in a way – uncontrolled
string interpolation, no type system, no tainting, no meaningful software
testing. A stringly-typed carambolage.

**Treating GHA like this is freeing.**

There’s no supply chain risk – you’re stealing a read only `GITHUB_TOKEN`
to a public open source repository? We had a tool for this, it was called
“git clone https://github.com/shaddap/yaface”.

Your creaky CI scripts need Python 2 linked against OpenSSL 0.9.8xxzz?
Wonderful! Beautiful work.

**Treating GHA like this is restrictive.**

An action can *never* have commit privileges, or any other privilege more
than any GH user. External services wanting to alter something (like, post
on a PR) need to be a GitHub App, they cannot use `GITHUB_TOKEN`.

Packages (Rust crates, PyPI packages, ..) cannot be published automatically
from a GitHub Action. GHA in this model cannot keep secrets, and nor should
it ever be given OIDC `id-token: write` permissions. So neither publishing
directly nor as a “trusted publisher” can work.

**But… but… my workflows! My PR labeller!**

If you can’t swing this, [zizmor](https://github.com/woodruffw/zizmor) is good.
GitHub should fund remedial tooling like this.

### Related Posts

* 27 Jun 2024 » [CVE-2024-5535: `SSL\_select\_next\_proto` buffer overread](/2024/06/27/cve-2024-5535-openssl-memory-safety.html)
* 30 Oct 2023 » [Replacing a C library: a testing strategy](/2023/10/30/replacing-a-c-library.html)
* 14 Jun 2020 » [Third-party audit of rustls](/2020/06/14/rustls-audit.html)

Joseph Birr-Pixton

Mail: jbp@jbp.io

GitHub: [github.com/ctz](https://github.com/ctz/)

Bluesky: [bsky.app/profile/jbp.io](https://bsky.app/profile/jbp.io/)