---
title: Detecting code copying at scale with Vendetect
url: https://blog.trailofbits.com/2025/07/21/detecting-code-copying-at-scale-with-vendetect/
source: The Trail of Bits Blog
date: 2025-07-22
fetch_date: 2025-10-06T23:27:43.717329
---

# Detecting code copying at scale with Vendetect

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Detecting code copying at scale with Vendetect

Evan Sultanik

July 21, 2025

[tool-release](/categories/tool-release/), [research-practice](/categories/research-practice/)

Page content

* [The vendoring problem nobody talks about](#the-vendoring-problem-nobody-talks-about)
* [How Vendetect works](#how-vendetect-works)
* [Version control awareness changes everything](#version-control-awareness-changes-everything)
* [Real-world detection in action](#real-world-detection-in-action)
* [Using Vendetect in practice](#using-vendetect-in-practice)
* [Beyond plagiarism detection](#beyond-plagiarism-detection)
* [Extending Vendetect](#extending-vendetect)
* [Try it yourself](#try-it-yourself)

Earlier this month, the maintainer of [Cheating-Daddy](https://cheatingdaddy.com/) [discovered](https://x.com/soham_btw/status/1940952786491027886) that a Y-Combinator-funded startup had copied their GPL-licensed codebase, stripped out the comments, and re-released it as “[Glass](https://pickle.com/glass)” under an incompatible license. This isn’t an isolated incident; we see code theft and improper vendoring constantly during security assessments. So we built a tool to catch it automatically.

[Vendetect](https://github.com/trailofbits/vendetect) is our new open-source tool for detecting copied and vendored code between repositories. It uses semantic fingerprinting to identify similar code even when variable names change or comments disappear. More importantly, unlike academic plagiarism detectors, it understands version control history, helping you trace vendored code back to its exact source commit.

## The vendoring problem nobody talks about

During our security assessments, we regularly encounter codebases with chunks of copy-pasted code from other projects. Sometimes it’s legitimate vendoring. Often it’s not. The problems run deeper than just license violations:

* **Security debt accumulates silently.** When developers vendor a function from OpenSSL or copy a smart contract utility from OpenZeppelin, they inherit any latent vulnerabilities in that code. But without tracking the source version, you can’t know if you’re affected when CVEs drop.
* **Attribution disappears.** We’ve seen proprietary codebases containing entire open-source libraries with copyright notices stripped. Whether malicious or accidental, this creates legal liability.
* **Updates never happen.** Vendored code becomes frozen in time. The original project fixes bugs and adds features, but the copied version bitrots.

## How Vendetect works

Vendetect implements the [Winnowing algorithm](https://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf), the same approach used by Stanford’s MOSS plagiarism detector, popular among computer science professors. But we’ve adapted it for real-world software engineering needs.

The algorithm works by creating semantic fingerprints of code that remain stable even when surface-level changes occur. Here’s the simplified process:

1. **Tokenize the code** using language-aware lexers (via [Pygments](https://pygments.org/))
2. **Generate *k*-grams** from the token stream
3. **Hash the *k*-grams** and select a subset using a sliding window
4. **Compare fingerprints** between files to find matches

This approach catches copied code even when someone:

* Renames all variables and functions
* Removes comments and documentation
* Reformats or restructures the code
* Changes from tabs to spaces (yes, really)

We built Vendetect’s architecture to be modular; the Winnowing implementation is just one detection back end. The tool can easily integrate other approaches like JPlag’s token-based matching or AST-based similarity detection. We use the Python [`copydetect`](https://pypi.org/project/copydetect/) package for the core Winnowing implementation, which gives us both speed and reliability.

## Version control awareness changes everything

Here’s where Vendetect differs from academic plagiarism detectors: it understands git history.

Say you’re auditing a codebase and find a suspicious crypto implementation. Vendetect doesn’t just tell you it matches some OpenSSL code—it identifies the exact commit from which it was copied. Now you can check if that version had the Heartbleed vulnerability, or any of the dozen memory corruption bugs fixed since then.

This feature has proven invaluable during assessments. We’ve found:

* Smart contracts with vendored OpenZeppelin code from versions with known bugs
* Cryptographic libraries copied from pre-disclosure commits containing weaknesses
* Authentication code lifted from tutorials with hardcoded backdoors

The tool automatically clones and analyzes repository history, comparing your target codebase against multiple versions to find the most likely source commit.

## Real-world detection in action

Running Vendetect on the Cheating-Daddy/Glass case took about 10 seconds on a laptop:

```
vendetect https://github.com/pickle-com/glass https://github.com/example/cheating-daddy
```

![Figure 1: Vendetect output comparing Glass (left) to Cheating-Daddy](/img/cheating-daddy.png)

Figure 1: Vendetect output comparing Glass (left) to Cheating-Daddy (right)

The results clearly showed extensive copying with high similarity scores across multiple files, despite Glass’s attempts to obscure the source through comment removal and reformatting.

In smart contract assessments, vendoring detection is even more critical. Ethereum developers routinely copy utility functions, math libraries, and security patterns from established projects. While often legitimate, this practice creates hidden dependencies.

## Using Vendetect in practice

Installation is straightforward:

```
pip install vendetect
```

Basic usage compares two repositories:

```
# Local repositories
vendetect /path/to/suspect/repo /path/to/source/repo
# Remote repositories
vendetect ./my-project https://github.com/openssl/openssl
# Output formats for automation
vendetect repo1 repo2 --format json > results.json
```

Figure 2: Basic Vendetect usage

The default rich output shows side-by-side code comparison with similarity percentages. The JSON output integrates easily into CI/CD pipelines for automated license compliance or security checks.

## Beyond plagiarism detection

We built Vendetect to solve real problems we encounter during security assessments, but its applications extend beyond catching code thieves:

* **Supply chain security**: Identify all vendored dependencies in a codebase, especially those not tracked by traditional dependency managers.
* **License compliance**: Automatically verify that vendored code maintains proper attribution and compatible licensing.
* **Security patch tracking**: When CVEs are announced, quickly check if your vendored code is affected by comparing against patched versions.
* **Code archaeology**: Trace the lineage of legacy code when documentation is missing or incorrect.

## Extending Vendetect

Vendetect’s modular architecture makes it easy to experiment with different detection algorithms. If you’ve implemented your own similarity detection method, whether based on AST analysis, machine learning embeddings, or novel algorithms, we want to hear from you. The tool provides a clean interface for adding new detection back ends:

```
class MyComparator(vendetect.comparison.Comparator[MyFingerprint]):
    def fingerprint(self, path: Path) -> MyFingerprint:
        # TODO: Fingerprint the file at `path`
        return my_fingerprint

    def compare(self, fp1: MyFingerprint, fp2: MyFingerprint) -> Comparison:
        # TODO: Compare two fingerprints and return the result
        return comparison
```

Figure 3: How to define a new custom comparator

We’re particularly interested in approaches that could improve detection in specific domains, such as smart contracts or embedded systems, where traditional...