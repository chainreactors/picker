---
title: Introducing mrva, a terminal-first approach to CodeQL multi-repo variant analysis
url: https://blog.trailofbits.com/2025/12/11/introducing-mrva-a-terminal-first-approach-to-codeql-multi-repo-variant-analysis/
source: The Trail of Bits Blog
date: 2025-12-11
fetch_date: 2025-12-12T03:20:59.634096
---

# Introducing mrva, a terminal-first approach to CodeQL multi-repo variant analysis

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Introducing mrva, a terminal-first approach to CodeQL multi-repo variant analysis

[Matt Schwager](/authors/matt-schwager/)

December 11, 2025

[codeql](/categories/codeql/), [tool-release](/categories/tool-release/), [static-analysis](/categories/static-analysis/)

Page content

* [Installing and running mrva](#installing-and-running-mrva)
* [Comparing mrva with GitHub tooling](#comparing-mrva-with-github-tooling)
* [Interesting implementation details](#interesting-implementation-details)
  + [CodeQL database API](#codeql-database-api)
  + [Analyze flags](#analyze-flags)
  + [CodeQL query kinds](#codeql-query-kinds)
* [Running at scale, locally](#running-at-scale-locally)

In 2023 GitHub introduced CodeQL [multi-repository variant analysis](https://github.blog/security/vulnerability-research/multi-repository-variant-analysis-a-powerful-new-way-to-perform-security-research-across-github/) (MRVA). This functionality lets you run queries across thousands of projects using pre-built databases and drastically reduces the time needed to find security bugs at scale. There’s just one problem: it’s largely built on [VS Code](https://github.com/github/vscode-codeql) and I’m a Vim user and a terminal junkie. That’s why I built [`mrva`](https://github.com/trailofbits/mrva), a composable, terminal-first alternative that runs entirely on your machine and outputs results wherever `stdout` leads you.

In this post I will cover installing and using `mrva`, compare its feature set to GitHub’s MRVA functionality, and discuss a few interesting implementation details I discovered while working on it. Here is a quick example of what you’ll see at the end of your `mrva` journey:

![Figure 1: Pretty-printing CodeQL SARIF results](/2025/12/11/introducing-mrva-a-terminal-first-approach-to-codeql-multi-repo-variant-analysis/introducing-mrva-image_hu_fd3f685a1b3d7931.webp)

Figure 1: Pretty-printing CodeQL SARIF results

## Installing and running mrva

First, install `mrva` from [PyPI](https://pypi.org/project/mrva/):

`$ python -m pip install mrva`

*Or, use your favorite Python package installer like `pipx` or `uv`.*

Running `mrva` can be broken down into roughly three steps:

1. Download pre-built CodeQL databases from the GitHub API (`mrva download`).
2. Analyze the databases with CodeQL queries or packs (`mrva analyze`).
3. Output the results to the terminal (`mrva pprint`).

Let’s run the tool with Trail of Bits’ [public CodeQL queries](https://github.com/trailofbits/codeql-queries). Start by downloading the top 1,000 Go project databases:

```
$ mkdir databases
$ mrva download --token YOUR_GH_PAT --language go databases/ top --limit 1000
2025-09-04 13:25:10,614 INFO mrva.main Starting command download
2025-09-04 13:25:14,798 INFO httpx HTTP Request: GET https://api.github.com/search/repositories?q=language%3Ago&sort=stars&order=desc&per_page=100 "HTTP/1.1 200 OK"
...
```

You can also use the `$GITHUB_TOKEN` environment variable to more securely specify your personal access token. Additionally, there are other strategies for downloading CodeQL databases, such as by GitHub organization (`download org`) or a single repository (`download repo`). From here, let’s clone the queries and run the multi-repo variant analysis:

```
$ git clone https://github.com/trailofbits/codeql-queries.git
$ mrva analyze databases/ codeql-queries/go/src/crypto/ -- --rerun --threads=0
2025-09-04 14:03:03,765 INFO mrva.main Starting command analyze
2025-09-04 14:03:03,766 INFO mrva.commands.analyze Analyzing mrva directory created at 1757007357
2025-09-04 14:03:03,766 INFO mrva.commands.analyze Found 916 analyzable repositories, discarded 84
2025-09-04 14:03:03,766 INFO mrva.commands.analyze Running CodeQL analysis on mrva-go-ollama-ollama
...
```

This analysis may take quite some time depending on your database corpus size, query count, query complexity, and machine hardware. You can filter the databases being analyzed by passing the `--select` or `--ignore` flag to `analyze`. Any flags passed after `--` will be sent directly to the CodeQL binary. Note that, instead of having `mrva` parallelize multiple CodeQL analyses, we instead recommend passing `--threads=0` and letting CodeQL handle parallelization. This helps avoid CPU thrashing between the parent and child processes. Once the analysis is done, you can print the results:

```
$ mrva pprint databases/
2025-09-05 10:01:34,630 INFO mrva.main Starting command pprint
2025-09-05 10:01:34,631 INFO mrva.commands.pprint pprinting mrva directory created at 1757007357
2025-09-05 10:01:34,631 INFO mrva.commands.pprint Found 916 analyzable repositories, discarded 84
tob/go/msg-not-hashed-sig-verify: Message must be hashed before signing/verifying operation

  builtin/credential/aws/pkcs7/verify.go (ln: 156:156 col: 12:31)
  https://github.com/hashicorp/vault/blob/main/builtin/credential/aws/pkcs7/verify.go#L156-L156

  155 if maxHashLen := dsaKey.Q.BitLen() / 8; maxHashLen < len(signed) {
  156    signed = signed[:maxHashLen]
  157 }

  builtin/credential/aws/pkcs7/verify.go (ln: 158:158 col: 25:31)
  https://github.com/hashicorp/vault/blob/main/builtin/credential/aws/pkcs7/verify.go#L158-L158

  157 }
  158 if !dsa.Verify(dsaKey, signed, dsaSig.R, dsaSig.S) {
  159    return errors.New("x509: DSA verification failure")
...
```

This finding is a false positive because the message is indeed being truncated, but updating [the query’s](https://github.com/trailofbits/codeql-queries/blob/main/go/src/crypto/MsgNotHashedBeforeSigVerfication/MsgNotHashedBeforeSigVerfication.ql) list of [barriers](https://codeql.github.com/codeql-standard-libraries/go/semmle/go/security/IncorrectIntegerConversionLib.qll/predicate.IncorrectIntegerConversionLib%24ConversionWithoutBoundsCheckConfig%24isBarrier.2.html) is beyond the scope of this post. Like previous commands, `pprint` also takes a number of flags that can affect its output. Run it with `--help` to see what is available.

A quick side note: `pprint` is also capable of pretty-printing SARIF results from non-`mrva` CodeQL analyses. That is, it solves one of my first and biggest gripes with CodeQL: why can’t I get the output of [`database analyze`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze) in a human readable form? It’s especially useful if you run `analyze` with the `--sarif-add-file-contents` flag. Outputting CSV and SARIF is great for machines, but often I just want to see the results then and there in the terminal. `mrva` solves this problem.

## Comparing mrva with GitHub tooling

`mrva` takes a lot of inspiration from GitHub’s CodeQL VS Code extension. GitHub also provides an unofficial CLI extension [by the same name](https://github.com/GitHubSecurityLab/gh-mrva). However, as we’ll see, this extension replicates many of the same cloud-first workflows as the VS Code extension rather than running everything locally. Here is a summary of these three implementations:

|  | `mrva` | `gh-mrva` | `vscode-codeql` |
| --- | --- | --- | --- |
| Requires a GitHub controller repository | ❌ | ✅ | ✅ |
| Runs on GitHub Actions | ❌ | ✅ | ✅ |
| Supports self-hosted runners | ❌ | ✅ | ✅ |
| Runs on your local machine | ✅ | ❌ | ❌ |
| Easily modify CodeQL analysis parameters | ✅ | ❌ | ❌ |
| View findings locally | ✅ | ❌ | ✅ |
| AST viewer | ✅ | ❌ | ✅ |
| Use GitHub search to create target lists | ✅ | ❌ | ✅ |
| Custom target lists | ✅ | ✅ | ✅ |
| Export/download results | ✅ (SARIF) | ✅ (SARIF) | ✅ (Gist or Markdown) |

As you can see, the primary benefits of `mrva` are the ability to run analyses and view findings locally. This gives the user more control over analysis options and ownership of their findings data. Everything is just a file on disk—where you take it from there is up to you.

## Interesting implementation details

After working ...