---
title: wrongsecrets-binaries v0.3.0
url: https://kitploit.com/en/posts/github-owasp-wrongsecrets-binaries-v030
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:37.961340
---

# wrongsecrets-binaries v0.3.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/39595/2a3aa4856964fa38c05e947736458a74f0dfe1dd52953fa75f928ef11aadec0d.png)

New releaseSep 3, 2026

# wrongsecrets-binaries v0.3.0

Source code for the Binaries of OWASP WrongSecrets

Share

# wrongsecrets-binaries

[![Pre-commit](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/pre-commit.yml)
[![Compile C](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_c.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_c.yml)
[![Compile CPlus](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_cplus.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_cplus.yml)
[![Compile GoLang](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_golang.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_golang.yml)
[![Compile Rust](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_rust.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_rust.yml)
[![dotnet package](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_dotnet.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_dotnet.yml)
[![Compile Swift](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_swift.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_swift.yml)
[![Compile Java](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_java.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/compile_java.yml)
[![Security Scanning](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/security-scanning.yml/badge.svg)](https://github.com/OWASP/wrongsecrets-binaries/actions/workflows/security-scanning.yml)

This is a supportive repository for [OWASP WrongSecrets](https://github.com/OWASP/wrongsecrets).
Here we create our binaries which are included in the official project.
Want to add a challenge related to secrets hiding in binary? Open a ticket at [WrongSecrets issues](https://github.com/OWASP/wrongsecrets/issues).
Want to fix something you found in one of the binaries: open a ticket or a PR here.

## CTF Support

This repository now supports generating **CTF (Capture The Flag) versions** of all binaries with randomized secrets. CTF versions use the format `this is the secret in <language> : <random_hex>` instead of static secrets, making them suitable for CTF competitions.

* **Automatic Generation**: Both `quickbuild.sh` and GitHub Actions generate CTF versions alongside regular binaries
* **All Languages**: Supports C, C++, Go, Rust, .NET, and Swift
* **Easy Testing**: Use `./test_ctf_generation.sh` to verify functionality

See [docs/CTF\_GENERATION.md](https://github.com/owasp/wrongsecrets-binaries/blob/main/docs/CTF_GENERATION.md) for detailed usage instructions.

## Development

This repository uses [pre-commit lite](https://pre-commit.com/) with **automated code formatting** to maintain code quality with minimal friction. The lightweight configuration automatically fixes formatting issues for Rust and Go code. See [docs/PRE\_COMMIT.md](https://github.com/owasp/wrongsecrets-binaries/blob/main/docs/PRE_COMMIT.md) for setup instructions.

## Security Scanning

This repository includes comprehensive security scanning using GitHub's free tools:

### CodeQL Analysis

* **Languages Covered**: C, C++, Go, C#/.NET, Swift
* **Triggers**: Push to main/master, pull requests, manual dispatch, weekly schedule
* **Integration**: Results automatically uploaded to GitHub Security tab

### Semgrep Analysis

* **Languages Covered**: All languages (C, C++, Go, Rust, C#/.NET, Java, Swift)
* **Rulesets**:
  + OWASP Top 10 security issues
  + CWE Top 25 vulnerabilities
  + Secrets detection
  + General security audit rules
* **Integration**: SARIF results uploaded to GitHub Security tab

### Viewing Security Results

Security scan results are available in the repository's **Security** tab under **Code scanning alerts**. The scans run automatically on code changes and weekly on Sundays at 3 AM UTC.

## Special thanks

### Contributors:

Leaders:

* [Ben de Haan @bendehaan](https://github.com/bendehaan)
* [Jeroen Willemsen @commjoen](https://github.com/commjoen)

(Top) contributors:

* [Puneeth Y @puneeth072003](https://github.com/puneeth072003)
* [Rodolfo Cabral Neves @roddas](https://github.com/roddas)
* [Diamond Rivero @diamant3](https://github.com/diamant3)
* [Joss Sparkes @remakingeden](https://github.com/remakingeden)
* [Arpit Jain](https://https://github.com/arpitjain099)

### Sponsorships:

We would like to thank the following parties for helping us out:

[![gitguardian_logo.png](https://assets.kitploit.com/production/public/readmes/39595/60c5377dbed6d97c9de54e020e8d48204b4a2d26e6d524b3fd9bc48e4ba95f9c.jpg)](https://blog.gitguardian.com/gitguardian-is-proud-sponsor-of-owasp/)

[GitGuardian](https://blog.gitguardian.com/gitguardian-is-proud-sponsor-of-owasp/) for their sponsorship which allows us to pay the bills for our cloud-accounts.

[![jetbrains_logo.png](https://assets.kitploit.com/production/public/readmes/39595/19234cdcf99acad12bea498764fa1a4220ab90ddddfcfa64c1f2d3c32fc72f7d.png)](https://www.jetbrains.com/)

[Jetbrains](https://www.jetbrains.com/) for licensing an instance of Intellij IDEA Ultimate edition to the project leads. We could not have been this fast with the development without it!

[![docker_logo.png](https://assets.kitploit.com/production/public/readmes/39595/f87d09d77c5206d9a6826242fa7b6f1f1861c2939771bdbd29002935d7e69dd2.png)](https://www.docker.com)

[Docker](https://www.docker.com) for granting us their Docker Open Source Sponsored program.

[![1password_logo.png](https://assets.kitploit.com/production/public/readmes/39595/8945ae3f629bcdfd68265c54159763c6f719afb356c3cc748d5e7a6ec3a114c9.png)](https://github.com/1Password/1password-teams-open-source/pull/552)

[1Password](https://github.com/1Password/1password-teams-open-source/pull/552) for granting us an open source license to 1Password for the secret detection testbed.

## Copyrights

Copyright (c) 2020-2026 Jeroen Willemsen and WrongSecret contributors.

[Read more](/en/tools/github/owasp/wrongsecrets-binaries?expand=1)

## Categories

[Static Analysis](/en/categories/static-analysis)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Code Analysis](/en/categories/code-analysis)[CTF](/en/categories/ctf)[Secret Detection](/en/categories/secret-detection)[Binary Analysis](/en/categories/binary-analysis)[Supply Chain Security](/en/categories/supply-chain-security)[Learning & Education](/en/categories/education)[Labs & Practice](/en/categories/labs-practice)

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