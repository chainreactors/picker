---
title: deadair v0.6.0
url: https://kitploit.com/en/posts/github-big-comfy-deadair-v060
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:04.686261
---

# deadair v0.6.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/791/9430ecf0da8731840cb393f12919086e64014ef49bac08d869efa0c03c937ea2.png)

New releaseAug 21, 2026

# deadair v0.6.0

Finds the detection rules in your SIEM that are running blind

Share

![deadair - SIEM detection coverage health](https://raw.githubusercontent.com/big-comfy/deadair/HEAD/docs/assets/banner-light.svg)

[![CI](https://github.com/alephnull-sh/deadair/actions/workflows/ci.yml/badge.svg)](https://github.com/alephnull-sh/deadair/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/alephnull-sh/deadair)](https://github.com/alephnull-sh/deadair/releases)
![Go 1.26](https://img.shields.io/badge/go-1.26-00ADD8)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

**Open-source SIEM detection health.**
Find enabled detections that are blind because their telemetry is missing, stale, late, or
schema-incompatible.

Runs locally · Read-only · No agent · No telemetry upload

[Read the technical write-up](https://alephnull-sh.github.io/deadair/) ·
[Featured in Detection Engineering Weekly](https://www.detectionengineering.net/i/208193682/detection-engineering-gem)

![deadair scan of a disposable Elastic lab showing dead and impaired detections](https://assets.kitploit.com/production/public/readmes/791/fc36f93c2d5fcaceffd370452b89b908a930eb10e810c0187fb3bba59cb156dd.png)

Real scan of a disposable Elastic lab with deliberately missing, stale, late, and unused telemetry. Reproduce it with `make record-scan-lab`.

## Why deadair

A rule can be enabled, scheduled, and error-free while the data it needs is gone. deadair reads the
live rule inventory, resolves each rule's inputs using the backend's native semantics, and checks the
concrete sources behind them.

It catches:

* rules whose index, alias, or data-stream selectors resolve to nothing;
* rules whose matching sources are all stale or empty;
* rules running with missing fields or an ingest-lag blind window;
* healthy telemetry that no enabled detection reads.

deadair currently works with Elastic Security and OpenSearch Security Analytics.

## Quick start

Download a binary for macOS, Linux, or Windows from
[GitHub Releases](https://github.com/alephnull-sh/deadair/releases), or install with Go:

root@kitploit:~

```
go install github.com/alephnull-sh/deadair/cmd/deadair@latest
```

Connect a read-only SIEM credential:

root@kitploit:~

```
deadair setup elastic   # print the least-privilege setup
deadair check           # verify the credential can scan
deadair scan            # assess live rules and telemetry
```

Exit codes are stable: `0` is healthy, `1` means findings, and `2` means the scan failed.

## How it works

| Stage | What deadair does |
| --- | --- |
| Inventory | reads enabled detections and the inputs they declare |
| Resolve | asks Elastic or OpenSearch to resolve index patterns, aliases, data streams, selectors, and remote inputs |
| Measure | checks document count, freshest event, storage, field mappings, schema history, and ingest lag |
| Report | emits terminal, JSON, HTML, fleet rollups, and Prometheus metrics with the evidence behind each verdict |

deadair proves whether a detection's observable telemetry prerequisites are present and healthy. It
does not prove that the rule logic is correct or that a simulated attack will produce an alert. Pair
it with static rule validation and end-to-end detection testing for those layers.

## Findings

| Finding | Meaning | First check |
| --- | --- | --- |
| no matching source | none of the rule's inputs resolve to a visible index or data stream | pattern changes, missing integrations, and credential scope |
| all sources stale or empty | every resolved source is unusable right now | source cadence and the ingest path |
| missing fields | declared fields are absent from every matched source mapping | parser, package, and mapping changes |
| lag blind window | measured ingest lag exceeds the rule's lookback margin | rule interval, lookback, timestamp override, and pipeline delay |
| source degradation | a source is stale, empty, low-volume, or schema-drifted | source history and expected maintenance |
| unused telemetry | data is being stored but no enabled local detection resolves to it | disabled rules and intentional collection |

Every verdict is limited to what the configured credential can see. JSON reports include the
configured expressions, resolved sources, resolution method, assessment status, backend metadata,
and capability evidence. See the [usage guide](https://github.com/big-comfy/deadair/blob/HEAD/docs/usage.md) for worked examples and triage.

## Connect a SIEM

Elastic:

root@kitploit:~

```
export DEADAIR_ES_URL=https://es.example.internal:9200
export DEADAIR_KIBANA_URL=https://kibana.example.internal:5601
export DEADAIR_API_KEY=<read-only-api-key>

deadair check
deadair scan --json-out report.json --html-out report.html
```

OpenSearch:

root@kitploit:~

```
export DEADAIR_BACKEND=opensearch
export DEADAIR_OPENSEARCH_URL=https://opensearch.example.internal:9200
export DEADAIR_OPENSEARCH_USERNAME=deadair
export DEADAIR_OPENSEARCH_PASSWORD=<password>

deadair check
deadair scan
```

Use the documented least-privilege roles for
[Elastic](https://github.com/big-comfy/deadair/blob/HEAD/docs/credentials/elastic.md) or [OpenSearch](https://github.com/big-comfy/deadair/blob/HEAD/docs/credentials/opensearch.md). The trusted
integration suite also proves that write attempts made with those credentials are rejected.

## CI, fleets, and monitoring

root@kitploit:~

```
# Gate a candidate rule against live source availability.
deadair scan --rule new-rule.json

# Fail only on new regressions between reports.
deadair diff yesterday.json today.json

# Scan multiple SIEM instances from one process.
deadair scan --fleet fleet.json

# Export cached scan results as Prometheus metrics.
deadair serve --interval 5m
```

`scan --rule` isolates the candidate rule from unrelated backlog. `diff` works with deterministically
redacted reports. Fleet configuration references secrets through environment variables rather than
storing secret values.

![deadair candidate-rule gate followed by a report diff](https://assets.kitploit.com/production/public/readmes/791/34031bf87a1515497998e3165ebb5a234f01dd4e63a01b1b7d1bca5bd1f644f3.gif)

A candidate-rule gate and report diff against a throwaway Elastic stack.

See [CI gate behavior](https://github.com/big-comfy/deadair/blob/HEAD/docs/usage.md#gate-detection-changes),
[fleet and MSSP deployment](https://github.com/big-comfy/deadair/blob/HEAD/docs/mssp.md), and the [Prometheus examples](https://github.com/big-comfy/deadair/blob/HEAD/contrib/) for production
patterns.

## Tested backends

The integration workflow currently tests these exact versions:

| Backend | Exact live-CI versions |
| --- | --- |
| Elastic Security | 8.19.19, 9.4.4 |
| OpenSearch Security Analytics | 2.19.6, 3.7.0 |

Other versions may work but are not covered by the current CI matrix.

## Security model

* All backend access is read-only; trusted integration tests prove the documented credentials cannot write.
* Reports, HTML, state files, and fleet output are written `0600` on POSIX systems.
* Credentials can come from environment variables or files, avoiding secrets in process arguments.
* `--redact` replaces tenant, rule, source, pattern, and field names with stable digests.
* The exporter binds to loopback by default.
* deadair has no phone-home behavior or usage telemetry.

Treat reports as sensitive SOC artifacts: they identify blind detections, source names, schema gaps,...