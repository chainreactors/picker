---
title: Our audit of Homebrew
url: https://blog.trailofbits.com/2024/07/30/our-audit-of-homebrew/
source: Trail of Bits Blog
date: 2024-07-31
fetch_date: 2025-10-06T17:43:35.158477
---

# Our audit of Homebrew

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Our audit of Homebrew

[William Woodruff](https://infosec.exchange/%40yossarian)

July 30, 2024

[research-practice](/categories/research-practice/)

This is a joint post with the Homebrew maintainers; [read their announcement here](https://brew.sh/2024/07/30/homebrew-security-audit/)!

Last summer, we performed an audit of [Homebrew](https://brew.sh/). Our audit’s scope included [Homebrew/brew](https://github.com/Homebrew/brew) itself (home of the brew CLI), and three adjacent repositories responsible for various security-relevant aspects of Homebrew’s operation:

* [Homebrew/actions](https://github.com/Homebrew/actions): a repository of custom GitHub Actions used throughout Homebrew’s CI/CD;
* [Homebrew/formulae.brew.sh](https://github.com/Homebrew/formulae.brew.sh): the codebase responsible for Homebrew’s JSON index of installable packages;
* [Homebrew/homebrew-test-bot](https://github.com/Homebrew/homebrew-test-bot): Homebrew’s core CI/CD orchestration and lifecycle management routines.

We found issues within Homebrew that, while not critical, could allow an attacker to load executable code at unexpected points and undermine the integrity guarantees intended by Homebrew’s use of sandboxing. Similarly, we found issues in Homebrew’s CI/CD that could allow an attacker to surreptitiously modify binary (“[bottle](https://docs.brew.sh/Bottles)”) builds of formulae and potentially pivot from triggering CI/CD workflows to controlling the execution of CI/CD workflows and exfiltrating their secrets.

This audit was sponsored by the [Open Tech Fund](https://www.opentech.fund/) as part of their larger mission to secure critical pieces of internet infrastructure. You can read the full report in [our publications repository](https://github.com/trailofbits/publications#technology-product-reviews).

### Homebrew

Homebrew is the self-described “missing package manager for macOS (or Linux).” It serves as the *de facto* standard package manager for software developers on macOS, and [serves hundreds of millions of package installs](https://formulae.brew.sh/analytics/install/365d/) annually. These installations include “keystone” packages such as [Golang](https://formulae.brew.sh/formula/go#default), [Node.js](https://formulae.brew.sh/formula/node#default), and [OpenSSL](https://formulae.brew.sh/formula/openssl%403#default), making Homebrew’s security (and the integrity of its builds) critical to the security of downstream software ecosystems as a whole. Homebrew’s core (not to be confused with [homebrew-core](https://github.com/Homebrew/homebrew-core)) is a Ruby monolith responsible for providing the [`brew` CLI](https://docs.brew.sh/Manpage) to users along with an [importable Ruby API](https://rubydoc.brew.sh/).

Since its inception in 2009, Homebrew has undergone several architectural shifts aimed at improving the reliability and usability of packages delivered to users: binary builds (bottles) were implemented, made into the default installation mechanism (replacing local source builds), and subsequently built solely on CI/CD to limit the risk of a compromised developer machine. Despite this increasingly static approach, Homebrew’s core codebase is fundamentally dynamic and, in many places, reflects Homebrew’s historical need for dynamic loading of [DSL-specified formulae](https://docs.brew.sh/Formula-Cookbook) via user-controlled Ruby code.

### Scope

Homebrew is both a user-installable package manager (the `brew` CLI) and a packaging ecosystem, with an extensive and bespoke CI/CD configuration for reviewing, building, and distributing bottles to end users. Our audit focused on aspects of both of these, and aimed to answer questions like (but not limited to) the following:

* Can a local actor induce unexpected execution of a formula’s DSL, e.g. without an explicit invocation of `brew install`?
* Can a local actor induce unexpected evaluation of a tap’s formulae, e.g. from just `brew tap` with no subsequent user actions?
* Can a local actor induce namespace confusions or conflicts within brew, resulting in `brew install foo` installing an unexpected formula?
* Can a locally installed formula surreptitiously subvert or bypass Homebrew’s build isolation mechanisms?
* Can an unprivileged or low-privilege CI/CD actor (such as a third-party contributor) pivot to a higher privilege in Homebrew’s CI/CD?
* Can an unprivileged or low-privilege CI/CD actor surreptitiously taint or compromise a bottle build?
* Can an unprivileged or low-privilege CI/CD actor establish persistence in Homebrew’s CI/CD?

### Highlighted findings

#### brew

During our review of the `brew` CLI’s codebase, we uncovered a number of findings that, while not critical, could potentially undermine Homebrew’s per-formula integrity and isolation properties. We also uncovered findings that could allow loading of formulae (i.e., executable code) from surprising sources, such as remote URLs.

Some findings of interest include:

* TOB-BREW-2, wherein a formula can influence the construction of its sandbox through string injection, resulting in a sandbox escape.
* TOB-BREW-5, wherein Homebrew used a collision-prone hash function (MD5) for a synthetic namespace (`FormulaNamespace`) could allow an attacker to induce runtime confusion between formulae.
* TOB-BREW-8, wherein a formula can surreptitiously include networked resources in its build without explicitly listing them via `resource` stanzas.
* TOB-BREW-11, wherein a formula can potentially use a socket pivot to escape its build sandbox on macOS.
* TOB-BREW-12, wherein a formula could opportunistically perform a privilege escalation through a user’s previously activated `sudo` token.
* TOB-BREW-13, wherein `brew install` can be induced to install formulae from non-local URLs for any protocol supported by the version of `curl` being used, such as SFTP or SCP.

Our overall evaluation of [Homebrew/brew](https://github.com/Homebrew/brew) is reflected in our report: while extensively tested, Homebrew’s large API and CLI surface and informal local behavioral contract offer a large variety of avenues for unsandboxed, local code execution to an opportunistic attacker. These avenues do not necessarily violate Homebrew’s core security assumptions (which assume trustworthy formulae), but may be subverted either by malicious formulae or through unexpected sources of formula loading (such as insufficiently sanitized inputs).

#### Homebrew’s CI/CD

Our review of Homebrew’s CI/CD workflows and actions uncovered findings that, while not critical, could undermine the integrity of Homebrew’s CI/CD runs and allow a less-privileged user to pivot to a position of higher privilege or even obtain persistence on Homebrew’s self-hosted GitHub Actions runners.

Some findings of interest include:

* TOB-BREW-18, wherein multiple CI/CD workflows use the `pull_request_target` trigger to allow third-party pull requests to run code in the context of Homebrew’s upstream repository, potentially enabling either credential disclosure or tampering with Homebrew’s bottle builds.
* TOB-BREW-23, wherein multiple CI/CD workflows inadvertently allow shell injection via unsanitized `workflow_dispatch` inputs, potentially enabling vertical movement by a less-privileged user (i.e., one who can dispatch workflows but not modify them).

Beyond CI/CD-specific findings, many brew findings are also salient in the CI/CD setting:

* TOB-BREW-6, which describes a lack of sandboxing/isolation during archive extraction, could be used by a less-privileged CI actor to pivot into a higher-privileged context by inducing extraction of a formula or other executable code that gets auto-loaded and executed during the CI’s lifecycle.
* TOB-BREW-13, described above, could be used by a less-privileged CI actor to pivot into a higher-privileged context, by inducing arbitrary cod...