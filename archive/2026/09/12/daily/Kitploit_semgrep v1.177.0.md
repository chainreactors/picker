---
title: semgrep v1.177.0
url: https://kitploit.com/en/posts/github-semgrep-semgrep-v11770
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:32.025380
---

# semgrep v1.177.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13771/753c289d978f141e41356454c8ffd44811dc19a02a1c223d0b6240a9c4f84ac4.jpg)

New releaseSep 12, 2026

# semgrep v1.177.0

Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.

Share

[![Semgrep logo](https://raw.githubusercontent.com/semgrep/semgrep/develop/images/semgrep-logo-light.svg)](https://semgrep.dev)

## Code scanning at ludicrous speed.

[![Homebrew](https://img.shields.io/homebrew/v/semgrep?style=flat-square)](https://formulae.brew.sh/formula/semgrep)
[![PyPI](https://img.shields.io/pypi/v/semgrep?style=flat-square&color=blue)](https://pypi.org/project/semgrep/)
[![Documentation](https://img.shields.io/badge/docs-semgrep.dev-purple?style=flat-square)](https://semgrep.dev/docs/)
[![Join Semgrep community Slack](https://img.shields.io/badge/slack-3.5k%20members-green?style=flat-square)](https://go.semgrep.dev/slack)
[![Issues welcome!](https://img.shields.io/badge/issues-welcome-green?style=flat-square)](https://github.com/semgrep/semgrep/issues/new/choose)
[![Star Semgrep on GitHub](https://img.shields.io/github/stars/semgrep/semgrep?label=GitHub%20Stars&style=flat-square)](https://github.com/semgrep/semgrep#readme)
[![Docker Pulls](https://img.shields.io/docker/pulls/semgrep/semgrep.svg?style=flat-square)](https://hub.docker.com/r/semgrep/semgrep)
[![Docker Pulls (Old)](https://img.shields.io/docker/pulls/semgrep/semgrep.svg?style=flat-square)](https://hub.docker.com/r/semgrep/semgrep)
[![Follow @semgrep on Twitter](https://img.shields.io/twitter/follow/semgrep?label=Follow%20semgrep&style=social&color=blue)](https://twitter.com/intent/follow?screen_name=semgrep)

Semgrep is a fast, open-source, static analysis tool that searches code, finds bugs, and enforces secure guardrails and coding standards. Semgrep [supports 30+ languages](#language-support) and can run in an IDE, as a pre-commit check, and as part of CI/CD workflows.

Semgrep is semantic grep for code. While running `grep "2"` would only match the exact string *2*, Semgrep would [match `x = 1; y = x + 1` when searching for *2*](https://semgrep.dev/playground/s/5rKgj). Semgrep rules look like the code you already write; no abstract syntax trees, regex wrestling, or painful DSLs.

Note that in security contexts, Semgrep Community Edition will miss many true positives as it can only analyze code within the boundaries of a single function or file. If you want to use Semgrep for security purposes (**SAST**, **SCA**, or **secrets scanning**), the Semgrep AppSec Platform is strongly recommended since it adds the following critical capabilities:

1. Improved core analysis capabilities (cross-file, cross-function, data-flow reachability) that greatly reduce false positives by 25% and increase detected true positives by 250%
2. Contextual post-processing of findings with Semgrep Assistant (AI) to further reduce noise by [~20%](https://a.storyblok.com/f/151984/x/2d12dc0223/whitepaper_-ai-powered-appsec-engineer-automate.pdf?cv=1728584410408). In addition, Assistant enriches findings with tailored, step-by-step remediation guidance that humans find actionable >80% of the time.
3. Customizable policies and seamless integration into developer workflows, giving security teams granular control over where, when, and how different findings are presented to developers (IDE, PR comment, etc.)

The Semgrep AppSec Platform works out-of-the-box with 20000+ proprietary rules across SAST, SCA, and secrets. Pro rules are written and maintained by the Semgrep security research team and are highly accurate, meaning AppSec teams can feel confident bringing findings directly to developers without slowing them down.

Semgrep analyzes code locally on your computer or in your build environment: **by default, code is never uploaded**. [Get started →.](#getting-started-)

[![Semgrep CLI image](https://assets.kitploit.com/production/public/readmes/13771/753c289d978f141e41356454c8ffd44811dc19a02a1c223d0b6240a9c4f84ac4.jpg)](#option-1-getting-started-from-the-cli)

### Language support

**Semgrep Code** supports 30+ languages, including:

Apex · Bash · C · C++ · C# · Clojure · Dart · Dockerfile · Elixir · HTML · Go · Java · JavaScript · JSX · JSON · Julia · Jsonnet · Kotlin · Lisp · Lua · OCaml · PHP · Python · R · Ruby · Rust · Scala · Scheme · Solidity · Swift · Terraform · TypeScript · TSX · YAML · XML · Generic (ERB, Jinja, etc.)

**Semgrep Supply Chain** supports 12 languages across 15 package managers, including:

C# (NuGet) · Dart (Pub) · Go (Go modules, `go mod`) · Java (Gradle, Maven) · Javascript/Typescript (npm, Yarn, Yarn 2, Yarn 3, pnpm) · Kotlin (Gradle, Maven) · PHP (Composer) · Python (pip, pip-tool, Pipenv, Poetry) · Ruby (RubyGems) · Rust (Cargo) · Scala (Maven) · Swift (SwiftPM)

For more information, see [Supported languages](https://semgrep.dev/docs/supported-languages/).

### Getting started 🚀

1. [From the Semgrep AppSec Platform](#option-1-getting-started-from-the-semgrep-appsec-platform-recommended)
2. [From the CLI](#option-2-getting-started-from-the-cli)

For new users, we recommend starting with the [Semgrep AppSec Platform](#option-1-getting-started-from-the-semgrep-appsec-platform-recommended) because it provides a visual interface, a demo project, result triaging and exploration workflows, and makes setup in CI/CD fast. Scans are still local and code isn't uploaded. Alternatively, you can also start with the CLI and navigate the terminal output to run one-off searches.

### Option 1: Getting started from the Semgrep Appsec Platform (Recommended)

[![Semgrep platform image](https://assets.kitploit.com/production/public/readmes/13771/764e8fb3153f751e81cd2ba4b47a4a2ac4d2b6d8696fbfe7c4a39153b5c6434a.jpg)](https://go.semgrep.dev/login-ghrmgo)

1. Register on [semgrep.dev](https://go.semgrep.dev/login-ghrmgo)
2. Explore the demo findings to learn how Semgrep works
3. Scan your project by navigating to `Projects > Scan New Project > Run scan in CI`
4. Select your version control system and follow the onboarding steps to add your project. After this setup, Semgrep will scan your project after every pull request.
5. [Optional] If you want to run Semgrep locally, follow the steps in the CLI section.

### Notes:

If there are any issues, [please ask for help in the Semgrep Slack](https://go.semgrep.dev/slack).

### Option 2: Getting started from the CLI

1. Install Semgrep CLI

   root@kitploit:~

   ```
   # For macOS
   $ brew install semgrep

   # For Ubuntu/WSL/Linux/macOS
   $ python3 -m pip install semgrep

   # To try Semgrep without installation run via Docker
   $ docker run -it -v "${PWD}:/src" semgrep/semgrep semgrep login
   $ docker run -e SEMGREP_APP_TOKEN=<TOKEN> --rm -v "${PWD}:/src" semgrep/semgrep semgrep ci
   ```
2. Run `semgrep login` to create your account and login to Semgrep. This step is optional, but logging into Semgrep gets you access to:

   * [Semgrep Supply Chain](https://semgrep.dev/products/semgrep-supply-chain?utm_medium=readme&utm_source=github&utm_content=ssc-product): A dependency scanner that detects reachable vulnerabilities in third party libraries
   * [Semgrep Code's Pro rules](https://semgrep.dev/products/semgrep-code?utm_medium=readme&utm_source=github&utm_content=code-pro-rules): 600+ high confidence rules written by Semgrep's security research team
   * [Semgrep Code's Pro engine](https://semgrep.dev/products/pro-engine?utm_medium=readme&utm_source=github&utm_content=pro-engine): An advanced code analysis engine, designed to detect complex vulnerabilities, and reduce false positives
3. Go to your app's...