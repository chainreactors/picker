---
title: We hardened zizmor's GitHub Actions static analyzer
url: https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/
source: The Trail of Bits Blog
date: 2026-05-22
fetch_date: 2026-05-23T05:39:08.872537
---

# We hardened zizmor's GitHub Actions static analyzer

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We hardened zizmor's GitHub Actions static analyzer

[Alexis Challande](/authors/alexis-challande/)

May 22, 2026

[ecosystem-security](/categories/ecosystem-security/), [open-source](/categories/open-source/), [supply-chain](/categories/supply-chain/), [engineering-practice](/categories/engineering-practice/)

Page content

* [Building the test corpus](#building-the-test-corpus)
* [How anchors are used in the wild](#how-anchors-are-used-in-the-wild)
* [Four anchor handling bugs found and fixed](#four-anchor-handling-bugs-found-and-fixed)
* [What else the corpus surfaced](#what-else-the-corpus-surfaced)
* [Securing CI where it matters most](#securing-ci-where-it-matters-most)

In March 2026, attackers exploited a `pull_request_target` misconfiguration in
the [`aquasecurity/trivy-action`](https://github.com/aquasecurity/trivy-action) GitHub Action to exfiltrate organization and
repository secrets, then used those credentials to backdoor [LiteLLM](https://github.com/BerriAI/litellm) on PyPI (see
[Trivy’s post-mortem](https://github.com/aquasecurity/trivy/discussions/10462) for the full timeline). [`zizmor`](https://github.com/zizmorcore/zizmor) is a static analyzer
that GitHub Actions users run to catch exactly these misconfigurations before they ship.
When GitHub Actions [added support for YAML anchors](https://github.blog/changelog/2025-09-18-actions-yaml-anchors-and-non-public-workflow-templates/) in September 2025, a small but
high-value slice of the ecosystem started writing workflows that `zizmor` could only
analyze on a best-effort basis.

Over the past three months, Trail of Bits collaborated with the `zizmor` maintainers
to bring `zizmor`’s anchor support up to full coverage. First, we fixed parsing bugs
that caused crashes, produced wrong-location findings, and silently mishandled aliased values.
Second, we surfaced deserialization edge cases that broke zizmor on otherwise valid workflows.
Finally, we helped align `zizmor`’s expression evaluator with GitHub’s own
[Known Answer Tests](https://github.com/actions/languageservices). We validated all of this against a new corpus of 41,253 workflows
from 6,612 high-value open-source repositories. The result: 20 filed issues, 15 merged pull
requests.

## Building the test corpus

To understand how anchors are used in CI today and to stress-test `zizmor`
against the full variety of YAML it encounters in the wild, we built a corpus
of real workflows. We used [BigQuery’s GitHub dataset](https://cloud.google.com/blog/topics/public-datasets/github-on-bigquery-analyze-all-the-open-source-code) to identify the 10,000
most-starred repositories created between 2022 and 2025, filtered to the 6,612
that use GitHub Actions, and downloaded every workflow file. That gave us
41,253 YAML files.

![Pipeline diagram showing repository selection from BigQuery, filtering for GitHub Actions usage, and workflow download feeding into the zizmor scan stage](/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/pipeline_hu_50937b9976f313d5.webp)

Figure 1: Building a testing corpus

When we ran `zizmor` against the corpus, it crashed on 45 of the 41,253
workflows. That’s a low rate, but each crash means a bug in `zizmor`.

## How anchors are used in the wild

`zizmor`’s anchor support was deliberately limited, and for good reason.
YAML anchors make workflows non-local: an alias defined in one place changes
behavior elsewhere in the file. This complicated `zizmor`’s parsing model, and
adoption was rare enough that the `zizmor` maintainers reasonably [discouraged](https://blog.yossarian.net/2025/09/22/dear-github-no-yaml-anchors)
anchor use. In our corpus, only 43 of the 41,253 workflows use YAML anchors (roughly 0.1%), but those 43 include some of the most foundational projects in open source:

* [Bitcoin Core](https://github.com/bitcoin/bitcoin)
* [PHP](https://github.com/php/php-src)
* [OpenSSL](https://github.com/openssl/openssl)

However, anchors are a supported feature, and their use will likely grow over time.

We found two common patterns. The first is **reusing steps across jobs**, as
Bitcoin Core’s CI does:

```
jobs:
  runners:
    steps:
      - &ANNOTATION_PR_NUMBER
        name: Annotate with pull request number
        run: |
          if [ "${{ github.event_name }}" = "pull_request" ]; then
            echo "::notice ..."
          fi

  test-each-commit:
    steps:
      - *ANNOTATION_PR_NUMBER
      - uses: actions/checkout@v6
```

Figure 2: Reuse step definition

The second pattern is **pinning action versions once**. For instance,
[Home Assistant’s CI](https://github.com/home-assistant/core) defines the action reference (with its
SHA hash) using an anchor, then reuses it wherever the same action appears:

```
jobs:
  lint:
    steps:
      - uses: &actions-setup-python actions/setup-python@a309ff8b42...
      # later in the same workflow:
      - uses: *actions-setup-python
```

Figure 3: Reuse action definition

## Four anchor handling bugs found and fixed

When we started, four anchor patterns from these workflows broke `zizmor`.

**Aliases in sequences were incorrectly flattened.** When a YAML alias appeared
inside a sequence (like a list of steps), `zizmor`’s internal path representation
spread the alias contents rather than treating it as a single element. This
caused `zizmor` to crash or produce findings pointing at the wrong location
in the file. (Fixed in [#1557](https://github.com/zizmorcore/zizmor/pull/1557))

**Anchor prefixes leaked into values.**

```
foo: [&name v, *x]
```

Figure 4: Anchor prefix leak

In YAML flow sequences, anchor prefixes like `&name` weren’t stripped from
resolved values. Given the snippet in [Figure 4](#figure-4), looking up the first element of
`foo` would return `&name v` instead of `v`, causing any step that consumed the
node value to fail. (Fixed in [#1562](https://github.com/zizmorcore/zizmor/pull/1562))

**Duplicate anchors caused a crash.** The YAML spec allows redefining an anchor
name (the last definition wins). `zizmor`’s YAML layer assumed anchor names were
unique and panicked on duplicates. (Fixed in [#1575](https://github.com/zizmorcore/zizmor/pull/1575))

**The `template-injection` audit crashed on aliased `run` values.** When a
YAML alias was used as a scalar `run:` value, the audit didn’t expect the
indirection and failed. (Fixed in [#1732](https://github.com/zizmorcore/zizmor/pull/1732))

To prevent future regressions, we also added integration tests covering anchor
patterns found in real workflows ([#1682](https://github.com/zizmorcore/zizmor/pull/1682)) and updated the anchor documentation
([#1788](https://github.com/zizmorcore/zizmor/pull/1788)).

## What else the corpus surfaced

Running `zizmor` against the full test corpus also surfaced bugs that had nothing to
do with anchors.

**Deserialization edge cases.** GitHub Actions accepts YAML constructs that
`zizmor`’s workflow model didn’t anticipate: `if: 0` (an integer where a string
is expected), `timeout-minutes: 0.5` (a float where an integer is expected),
`secrets: inherit` (a string where a mapping is expected). Each one caused
`zizmor` to reject the entire workflow. We reported these as individual issues
([#1670](https://github.com/zizmorcore/zizmor/issues/1670), [#1672](https://github.com/zizmorcore/zizmor/issues/1672), [#1674](https://github.com/zizmorcore/zizmor/issues/1674)), and the maintainers fixed them quickly.

**Expression evaluator bugs.** `zizmor` evaluates GitHub Actions expressions to
determine whether user-controlled data flows into dangerous sinks. We validated
the evaluator against GitHub’s own [Known Answer Tests](https://github.com/actions/languageservices) and helped the
maintainers align `zizmor`’s behavior with the official test suite ([#1694](https://github.com/zizmorcore/zizmor/issues/1694)).

**Upstream issues.** We al...