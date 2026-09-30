---
title: louis-rs Security Audit
url: https://www.shielder.com/blog/2026/09/louis-rs-security-audit/
source: Blog on Shielder
date: 2026-09-29
fetch_date: 2026-09-30T07:42:53.168338
---

# louis-rs Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2026/09/louis-rs-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2026/09/louis-rs-security-audit/ "ITA")

# louis-rs Security Audit

## TL;DR

Shielder, together with [OSTIF](https://ostif.org/), performed a Security Audit of the [louis-rs](https://github.com/liblouis/louis-rs) component, a pure Rust re-implementation of the [liblouis](https://github.com/liblouis/liblouis) braille translation and back-translation library.

The audit resulted in three (3) findings of medium severity. All of them have been addressed by the louis-rs maintainers.

**Today, we are publishing the [full report](https://github.com/ShielderSec/public-reports/blob/main/2026/%5BOSTIF%5D%20louis-rs%20-%20Report%20v1.2.pdf) in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

## Introduction

In March 2026, Shielder was hired to perform a Security Audit of the [louis-rs](https://github.com/liblouis/louis-rs) component, a pure Rust re-implementation still in an alpha state of liblouis. The audit was facilitated by the [Open Source Technology Improvement Fund (OSTIF)](https://ostif.org/).

louis-rs is an open-source Braille translation library, its main functionality is converting text to Braille and Braille back to text.

Braille is a tactile writing system that represents letters, numbers, punctuation, and other symbols using patterns of raised dots that can be read by touch.

Braille translation tables, such as those used by liblouis and louis-rs, define the rules for converting between ordinary text and Braille, including language-specific conventions, contractions, and formatting.

The decision to rewrite liblouis in Rust was motivated by the fact that the vast majority of CVEs in liblouis, which is employed by all the major operating systems for translating Braille, are due to manual memory management. Therefore, Its maintainers opted for a memory-safe language that also provides a comfortable environment for development and maintenance.

louis-rs is built around the following core components:

* CLI: the `louis` binary, which provides commands to parse braille tables, translate text to/from braille, trace rule application, run YAML-based test suites, and query table metadata.
* `Parser`: the module that reads and expands liblouis braille table files.
* `Translator`: the translation pipeline that compiles parsed rules into lookup structures and executes them in stages to convert text to braille (forward-translation) or braille to text (back-translation).
* Braille tables: liblouis-format .ctb/.utb files that define the character mappings and contraction rules for a given language.

The source code is available at <https://github.com/liblouis/louis-rs>.

## Context and Scope

The audit mainly focused on:

* Assessing the risks of passing untrusted tables to the `Parser`.
* Assessing the risks of passing untrusted text to translate and backtranslate to the `Translator`.
* Assessing the resilience of regular expressions employed in the translation table from liblouis against ReDOS attacks.

Given the limited size of the codebase, the audit was mostly performed following a **Manual Source Code Review** approach coupled with SAST and LLM based analysis for a complete and thorough assessment of the code. We directed the review towards three classes of threats:

* Logical flaws in the translation and backtranslation operations.
* Errors while parsing the translation table.
* Unhandled exceptions leading to denial of service.

One of the goals of the audit was to develop a set of fuzzers to dynamically stress some of
the most complex parts of the library: table parsing and text translation.

For this purpose, we developed a custom fuzzer based on a modified version of `rust-fuzz`, configured to use the `libafl_libfuzzer` runtime instead of the default `libfuzzer` runtime. This configuration enables the fuzzer to leverage the built-in `grimoire mutator`, providing transparent and automated structure-aware fuzzing of the translation table syntax.

## Findings Summary and Recommendations

The louis-rs component is, overall, adequately robust and well designed from a security standpoint - but there is still some room for improvement.

The Shielder team identified **three (3) medium** findings.

The main theme is the possibility to cause denial of services in the library via malicious input.

| ID | Vulnerability | Severity | Status |
| --- | --- | --- | --- |
| 1 | Denial of Service via Uncontrolled Recursion in Table Inclusion | Medium | Closed |
| 2 | Denial of Service via Regex Catastrophic Backtracking on Custom Tables | Medium | Closed |
| 3 | Denial of Service via Panic on Double Negation in Match Rule Patterns | Medium | Closed |

### Details

All three findings fall within the family of denial of service vulnerabilities.

The first two findings both leverage mechanisms that cause the component to perform a huge amount of work in response to a small, malicious input. The third, instead, relies on a panic triggered by an unhandled edge case reachable again through a crafted input.

**Denial of Service via Uncontrolled Recursion in Table Inclusion** It is possible to cause a denial of service in louis-rs by causing an uncontrolled recursion via the abuse of the “include” directory, used by a translation table to reference and include an external table.

The library library does not verify if cycles arise during the inclusion process and does not implement a mechanism to stop the execution after a certain threshold of depth.

Therefore to cause a stack overflow it is sufficient to provide as input to the `Parser` a self referencing table.

It is possible to generate a malicious table to demonstrate the vulnerability simply as:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` echo 'include evil.utb' > evil.utb ``` |

To trigger the overflow:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` louis parse evil.utb ``` |

**Denial of Service via Regex Catastrophic Backtracking on Custom Tables** It is possible to cause a denial of service in louis-rs providing in input to the library a table containing malicious regular expressions capable of causing a catastrophic backtracking that exhausts memory.

The `Translator` does not verify how much backtracking it performs, being therefore susceptible to denial of service attacks based on regular expressions.

It is possible to generate a malicious table to demonstrate the vulnerability simply as:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` echo 'match (a+)+ b b 1' > redos.utb ``` |

To trigger the uncontrolled backtracking:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` louis translate redos.utb aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ``` |

**Denial of Service via Panic on Double Negation in Match Rule Patterns** It is possible to cause a denial of service in louis-rs providing in input to the library a table containing malicious regular expressions that make the program panic.

When a double negation produces a `NotString` or `NotCharacterClass` variant and `.negate()` is called on it a second time, the program panics.

It is possible to generate a malicious table to demonstrate the vulnerability simply as:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` echo 'match !!a b c 1' > crash.utb ``` |

To trigger the panic:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` louis translate crash.utb "any text" ``` |

All three were reported to louis-rs maintainers and fixed by following the attached recommendations....