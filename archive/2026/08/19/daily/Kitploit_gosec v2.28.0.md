---
title: gosec v2.28.0
url: https://kitploit.com/en/posts/github-securego-gosec-v2280
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:54:07.137999
---

# gosec v2.28.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F2947%2F5075759b5f9906cc21de89db2ef6f3366fe8f7d47b36ce3912da0882c5ae482b.png&w=3840&q=75)

New releaseAug 19, 2026

# gosec v2.28.0

Go security checker

Share

# gosec - Go Security Checker

Inspects source code for security problems by scanning the Go AST
and SSA code representation.

![](https://assets.kitploit.com/production/public/readmes/2947/83d294db3a312bcea542b6eb8261128e6f09b50a95271788fe301e164b1655b1.png)

## Quick links

* [GitHub Action](#github-action)
* [Local installation](#local-installation)
* [Quick start](#quick-start)
* [Common usage patterns](#common-usage-patterns)
* [Selecting rules](#selecting-rules)
* [Output formats](#output-formats)

## Features

* **Pattern-based rules** for detecting common security issues
  in Go code
* **SSA-based analyzers** for type conversions, slice bounds,
  and crypto issues
* **Taint analysis** for tracking data flow from user input to
  dangerous functions (SQL injection, command injection, path
  traversal, SSRF, XSS, log injection, SMTP injection, SSTI,
  unsafe deserialization, open redirect)

## License

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
You may obtain a copy of the License
[here](http://www.apache.org/licenses/LICENSE-2.0).

## Project status

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3218/badge)](https://bestpractices.coreinfrastructure.org/projects/3218)
[![Build Status](https://github.com/securego/gosec/workflows/CI/badge.svg)](https://github.com/securego/gosec/actions?query=workflows%3ACI)
[![Coverage Status](https://codecov.io/gh/securego/gosec/branch/master/graph/badge.svg)](https://codecov.io/gh/securego/gosec)
[![GoReport](https://goreportcard.com/badge/github.com/securego/gosec)](https://goreportcard.com/report/github.com/securego/gosec)
[![GoDoc](https://pkg.go.dev/badge/github.com/securego/gosec/v2)](https://pkg.go.dev/github.com/securego/gosec/v2)
[![Docs](https://readthedocs.org/projects/docs/badge/?version=latest)](https://securego.io/)
[![Downloads](https://img.shields.io/github/downloads/securego/gosec/total.svg)](https://github.com/securego/gosec/releases)
[![GHCR](https://img.shields.io/badge/ghcr.io-securego/gosec-blue)](https://github.com/orgs/securego/packages/container/package/gosec)
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://securego.slack.com)
[![go-recipes](https://raw.githubusercontent.com/nikolaydubina/go-recipes/main/badge.svg?raw=true)](https://github.com/nikolaydubina/go-recipes)

## Installation

### GitHub Action

You can run `gosec` as a GitHub action as follows:

Use the versioned tag with `@master` which is pinned to the
latest stable release. This will provide a stable behavior.

root@kitploit:~

```
name: Run Gosec
on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master
jobs:
  tests:
    runs-on: ubuntu-latest
    env:
      GO111MODULE: on
    steps:
      - name: Checkout Source
        uses: actions/checkout@v3
      - name: Run Gosec Security Scanner
        uses: securego/gosec@master
        with:
          args: ./...
```

#### Scanning Projects with Private Modules

If your project imports private Go modules, you need to
configure authentication so that `gosec` can fetch the
dependencies. Set the following environment variables in
your workflow:

* `GOPRIVATE`: A comma-separated list of module path prefixes
  that should be considered private
  (e.g., `github.com/your-org/*`).
* `GITHUB_AUTHENTICATION_TOKEN`: A GitHub token with read
  access to your private repositories.

root@kitploit:~

```
name: Run Gosec
on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master
jobs:
  tests:
    runs-on: ubuntu-latest
    env:
      GO111MODULE: on
      GOPRIVATE: github.com/your-org/*
      GITHUB_AUTHENTICATION_TOKEN: ${{ secrets.PRIVATE_REPO_TOKEN }}
    steps:
      - name: Checkout Source
        uses: actions/checkout@v3
      - name: Run Gosec Security Scanner
        uses: securego/gosec@v2
        with:
          args: ./...
```

### Integrating with code scanning

You can [integrate third-party code analysis tools](https://docs.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/integrating-with-code-scanning)
with GitHub code scanning by uploading data as SARIF files.

The workflow shows an example of running the `gosec` as a step
in a GitHub action workflow which outputs the `results.sarif`
file. The workflow then uploads the `results.sarif` file to
GitHub using the `upload-sarif` action.

root@kitploit:~

```
name: "Security Scan"

# Run workflow each time code is pushed to your repository and on a schedule.
# The scheduled workflow runs every at 00:00 on Sunday UTC time.
on:
  push:
  schedule:
  - cron: '0 0 * * 0'

jobs:
  tests:
    runs-on: ubuntu-latest
    env:
      GO111MODULE: on
    steps:
      - name: Checkout Source
        uses: actions/checkout@v3
      - name: Run Gosec Security Scanner
        uses: securego/gosec@v2
        with:
          # we let the report trigger content trigger a failure using the GitHub Security features.
          args: '-no-fail -fmt sarif -out results.sarif ./...'
      - name: Upload SARIF file
        uses: github/codeql-action/upload-sarif@v2
        with:
          # Path to SARIF file relative to the root of the repository
          sarif_file: results.sarif
```

### Go Analysis

The `goanalysis` package provides a
[`golang.org/x/tools/go/analysis.Analyzer`](https://pkg.go.dev/golang.org/x/tools/go/analysis)
for integration with tools that support the standard Go
analysis interface, such as Bazel's
[nogo](https://github.com/bazelbuild/rules_go/blob/master/go/nogo.rst)
framework:

root@kitploit:~

```
nogo(
    name = "nogo",
    deps = [
        "@com_github_securego_gosec_v2//goanalysis",
        # add more analyzers as needed
    ],
    visibility = ["//visibility:public"],
)
```

### Local Installation

gosec requires Go 1.25 or newer.

root@kitploit:~

```
go install github.com/securego/gosec/v2/cmd/gosec@latest
```

## Quick start

root@kitploit:~

```
# Scan all packages in current module
gosec ./...

# Write JSON report
gosec -fmt json -out results.json ./...

# Write SARIF report for code scanning
gosec -fmt sarif -out results.sarif ./...
```

### Exit codes

* `0`: scan finished without unsuppressed findings/errors
* `1`: at least one unsuppressed finding or processing error
* Use `-no-fail` to always return `0`

## Usage

Gosec can be configured to only run a subset of rules, to
exclude certain file paths, and produce reports in different
formats. By default all rules will be run against the supplied
input files. To recursively scan from the current directory you
can supply `./...` as the input argument.

### Available rules

gosec includes rules across these categories:

* `G1xx`: general secure coding issues (for example hardcoded
  credentials, unsafe usage, HTTP hardening, cookie security)
* `G2xx`: injection risks in query/template/command
  construction
* `G3xx`: file and path handling risks (permissions, traversal,
  temp files, archive extraction)
* `G4xx`: crypto and TLS weaknesses
* `G5xx`: blocklisted imports
* `G6xx`: Go-specific correctness/security checks (for example
  range aliasing and slice bounds)
* `G7xx`: taint analysis rules (SQL injection, command
  injection, path traversal, SSRF, XSS, log, SMTP injection,
  SSTI, unsafe deserialization, and open redirect)

...