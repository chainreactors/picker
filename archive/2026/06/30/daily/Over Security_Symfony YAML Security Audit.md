---
title: Symfony YAML Security Audit
url: https://www.shielder.com/blog/2026/06/symfony-yaml-security-audit/
source: Over Security
date: 2026-06-30
fetch_date: 2026-07-01T06:24:23.055300
---

# Symfony YAML Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2026/06/symfony-yaml-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2026/06/symfony-yaml-security-audit/ "ITA")

# Symfony YAML Security Audit

## TL;DR

Shielder, together with [OSTIF](https://ostif.org/) and the [Sovereign Tech Agency](https://www.sovereign.tech/), performed a Security Audit of the [Symfony YAML](https://github.com/symfony/yaml) component, a PHP library to parse and dump YAML files.

The audit resulted in five (5) findings ranging from low to informational severity, including three (3) CVEs. All of them have been addressed by the Symfony maintainers.

**Today, we are publishing the [full report](https://github.com/ShielderSec/public-reports/blob/main/2026/%5BOSTIF%5D%20Symfony%20YAML%20-%20Report%20v1.2.pdf) in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

## Introduction

In December 2025, Shielder was hired to perform a Security Audit of the [Symfony YAML](https://github.com/symfony/yaml) component, a PHP library to load and dump YAML files. The audit was facilitated by the [Open Source Technology Improvement Fund (OSTIF)](https://ostif.org/).

YAML - *YAML Ain’t Markup Language* - is a human-friendly data serialization language for all programming languages. It is a hugely popular format for configuration files, striking a balance between human readability and advanced features. That same set of “advanced features” is exactly what makes YAML parsers an interesting target: the more a format can do, the more an attacker can ask it to do on your behalf.

The Symfony YAML component is shipped by default together with [Symfony](https://symfony.com/), an industry-leading PHP framework for building web applications, but it can also be pulled in as a standalone Composer package. It provides:

* A `Parser` to load YAML into PHP.
* A `Dumper` to serialize PHP structures into YAML.
* A `LintCommand` CLI to validate the syntax of YAML files.

The source code is available at <https://github.com/symfony/yaml>.

## Context and Scope

When you ship a YAML parser inside a framework that powers a large chunk of the PHP web, the most interesting question is not “is the happy path correct?” but rather “what happens when someone feeds it input it was never meant to see?”. Developers reach for `Yaml::parse()` to read config files they control, but the same call frequently ends up at the other end of an HTTP request, parsing data that an attacker fully controls.

With that in mind, the audit focused on:

* Assessing the risks of passing untrusted YAML content to the `Parser`.
* Assessing the lack of proper security considerations in the documentation and in the provided examples.

Given the limited size of the codebase, the audit was mostly performed following a **Manual Source Code Review** approach. We directed the review towards three classes of threats:

* Code deserialization gadgets triggered during YAML parsing.
* Leaks of sensitive information into the parsed PHP output.
* Resource starvation or program hangs occurring during parsing.

We also set up a fuzzing campaign using the experimental [PHP-Fuzzer](https://github.com/nikic/PHP-Fuzzer). Honesty time: between some rough edges of the tool and the harnesses we wrote, this particular campaign did not surface anything interesting. Not every avenue pays off, and that’s fine - it’s part of the job.

Finally, to measure how closely Symfony YAML follows the YAML spec, we wrote a script to run the component against the [YAML Test Suite](https://github.com/yaml/yaml-test-suite): feed each test’s `in.yaml` to the parser, serialize the result with `json_encode`, and diff it against the expected `in.json`. This is where parser *differentials* start to show up - more on that below.

## Findings Summary and Recommendations

The Symfony YAML component is, overall, adequately robust and well designed from a security standpoint - but there is still some room for improvement.

The Shielder team identified **three (3) low** and **two (2) informational** findings. The main themes were unmitigated resource starvation when parsing complex data, and a lack of security-focused documentation around the parser’s more dangerous features.

| ID | Vulnerability | Severity | Status |
| --- | --- | --- | --- |
| 1 | [Denial of Service (DoS) via Infinite Recursion of Nested YAML Blocks](https://github.com/symfony/symfony/security/advisories/GHSA-c2p3-7m5p-cv8x) (CVE-2026-45133) | Low | Closed |
| 2 | [Denial of Service (DoS) via Unbounded Alias Resolution](https://github.com/symfony/symfony/security/advisories/GHSA-4qpc-3hr4-r2p4) (CVE-2026-45304) | Low | Closed |
| 3 | [Regular Expression Denial of Service (ReDoS) in `Parser::cleanup`](https://github.com/symfony/symfony/security/advisories/GHSA-9frc-8383-795m) (CVE-2026-45305) | Low | Closed |
| 4 | Lack of Security Warning for Object Deserialization | Informational | Closed |
| 5 | Lack of Security Warning for Constant Resolution | Informational | Closed |

### Three flavors of Denial of Service

The first three findings are all variations on the same theme: handing the parser a small, innocent-looking string that asks it to do an enormous amount of work.

**Infinite Recursion of Nested YAML Blocks (CVE-2026-45133).** The `doParse()` and `parseBlock()` methods in `Parser.php` are mutually recursive: every time `doParse()` meets an indented line, it calls `parseBlock()`, which spins up a new parser and calls `doParse()` on the indented content. Since nothing capped the maximum depth, a deeply nested document keeps pushing frames until PHP gives up with a Fatal Error. A few kilobytes of indentation is enough to take down the process.

**Unbounded Alias Resolution - a.k.a. “Billion Laughs” (CVE-2026-45304).** YAML supports anchors (`&foo`) and aliases (`*foo`) so you can reuse a node instead of repeating it. Without a cap on how many times those references can expand, you get the classic [Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack) amplification:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"] b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a] c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b] d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c] # ... keep going and watch the memory graph go vertical ``` |

A tiny document expands into a structure with billions of nodes, exhausting memory. A fun wrinkle we noted in the report: thanks to PHP’s lazy allocation, the process often doesn’t die on `parse()` - it dies later, on `json_encode()`, when something finally walks the structure to materialize it. So the crash can surface far away from the line that actually parsed the attacker’s input.

**ReDoS in `Parser::cleanup` (CVE-2026-45305).** Before parsing, `Parser::cleanup()` strips spaces, headers, and comments. One of the regexes used to remove YAML headers is:

```
#^\%YAML[: ][\d\.]+.*\n#u
```

The `[\d\.]+` and `.*` subpatterns can match the same input, and with greedy quantifiers that’s a recipe for *catastrophic backtracking*: a crafted header makes the regex engine explore an exponential number of paths, stalling the process. The fix is the textbook one - remove the overlap or switch to possessive quantifiers.

All three were reported to `security@symfony.com`, moved to GitHub advisories, assigned CVEs, and fixed by adding the appropriate limits.

### The dangerous features nobody warned you about

The two informational findings aren’t bugs in the...