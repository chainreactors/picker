---
title: Catching malicious package releases using a transparency log
url: https://blog.trailofbits.com/2025/12/12/catching-malicious-package-releases-using-a-transparency-log/
source: The Trail of Bits Blog
date: 2025-12-12
fetch_date: 2025-12-13T03:14:27.671329
---

# Catching malicious package releases using a transparency log

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Catching malicious package releases using a transparency log

[Facundo Tuesca](/authors/facundo-tuesca/)

December 12, 2025

[engineering-practice](/categories/engineering-practice/), [supply-chain](/categories/supply-chain/), [ecosystem-security](/categories/ecosystem-security/), [open-source](/categories/open-source/)

Page content

* [Why transparency logs matter](#why-transparency-logs-matter)
* [Monitoring a transparency log](#monitoring-a-transparency-log)
* [What’s next](#whats-next)

We’re getting Sigstore’s [rekor-monitor](https://github.com/sigstore/rekor-monitor) ready for production use, making it easier for developers to detect tampering and unauthorized uses of their identities in the [Rekor](https://docs.sigstore.dev/logging/overview/) transparency log. This work, funded by the [OpenSSF](https://openssf.org/), includes support for the new [Rekor v2 log](https://blog.sigstore.dev/rekor-v2-ga/), certificate validation, and integration with The Update Framework (TUF).

For package maintainers that publish attestations signed using Sigstore (as supported by [PyPI](https://docs.pypi.org/attestations/producing-attestations/) and [npm](https://docs.npmjs.com/generating-provenance-statements)), monitoring the Rekor log can help them quickly become aware of a compromise of their release process by notifying them of new signing events related to the package they maintain.

Transparency logs like Rekor provide a critical security function: they create append-only, tamper-evident records that are easy to monitor. But having entries in a log doesn’t mean that they’re trustworthy by default. A compromised identity could be used to sign metadata, with the malicious entry recorded in the log. By improving rekor-monitor, we’re making it easy for everyone to actively monitor for unexpected log entries.

## Why transparency logs matter

Imagine you’re adding a dependency to your Go project. You run `go get`, the dependency is downloaded, and its digest is calculated and added to your `go.sum` file to ensure that future downloads have the same digest, trusting that first download as the source of truth. But what if the download was compromised?

What you need is a way of verifying that the digest corresponds to the exact dependency you want to download. A central database that contains all artifacts and their digests seems useful: the `go get` command could query the database for the artifact, and see if the digests match. However, a normal database can be tampered with by internal or external malicious actors, meaning the problem of trust is still not solved: instead of trusting the first download of the artifact, now the user needs to trust the database.

This is where transparency logs come in: logs where entries can only be added (append-only), any changes to existing entries can be trivially detected (tamper-evident), and new entries can be easily monitored. This is how [Go’s checksum database works: it stores](https://go.dev/ref/mod#checksum-database) the digests of all Go modules as entries in a transparency log, which is used as the source of truth for artifact digests. Users don’t need to trust the log, since it is continuously checked and monitored by independent parties.

In practice, this means that an attacker cannot modify an existing entry without the change being detectable by external parties (usually called “witnesses” in this context). Furthermore, if an attacker releases a malicious version of a Go module, the corresponding entry that is added to the log cannot be hidden, deleted or modified. This means module maintainers can continuously monitor the log for new entries containing their module name, and get immediate alerts if an unexpected version is added.

While a compromised release process usually leaves traces (such as GitHub releases, git tags, or CI/CD logs), these can be hidden or obfuscated. In addition, becoming aware of the compromise requires someone noticing these traces, which might take a long time. By proactively monitoring a transparency log, maintainers can very quickly be notified of compromises of their signing identity.

Transparency logs, such as [Rekor](https://docs.sigstore.dev/logging/overview/) and [Go’s checksum database](https://go.dev/ref/mod#checksum-database), are based on Merkle trees, a data structure that makes it easy to cryptographically verify that has not been tampered with. For a good visual introduction of how this works at the data structure level, see [Transparent Logs for Skeptical Clients](https://research.swtch.com/tlog).

## Monitoring a transparency log

Having an entry in a transparency log does not make it trustworthy by default. As we just discussed, an attacker might release a new (malicious) Go package and have its associated checksum added to the log. The log’s strength is not preventing unexpected/malicious data from being added, but rather being able to monitor the log for unexpected entries. If new entries are not monitored, the security benefits of using a log are greatly reduced.

This is why making it easy for users to monitor the log is important: people can immediately be alerted when something unexpected is added to the log and take immediate action. That’s why, thanks to funding by the [OpenSSF](https://openssf.org/), we’ve been working on getting Sigstore’s [rekor-monitor](https://github.com/sigstore/rekor-monitor) ready for production use.

The Sigstore ecosystem uses [Rekor](https://docs.sigstore.dev/logging/overview/) to log entries related to, for example, the [attestations for Python packages](https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/). Once an attestation is signed, a new entry is added to Rekor that contains information about the signing event: the CI/CD workflow that initiated it, the associated repository identity, and more. By having this information in Rekor, users can [query the log](https://search.sigstore.dev/?logIndex=243090039) and have certain guarantees that it has not been tampered with.

[rekor-monitor](https://github.com/sigstore/rekor-monitor) allows users to monitor the log to ensure that existing entries have not been tampered with, and to monitor new entries for unexpected uses of their identity. For example, the maintainer of a Python package that uploads packages from their GitHub repository (via [Trusted Publishing](https://docs.pypi.org/trusted-publishers/)) can monitor the log for any new entries that use the repository’s identity. In case of compromise, the maintainer would get a notification that their identity was used to upload a package to PyPI, allowing them to react quickly to the compromise instead of relying on waiting for someone to notice the compromise.

As part of our work in rekor-monitor, we’ve added support for the new [Rekor v2 log](https://blog.sigstore.dev/rekor-v2-ga/), implemented certificate validation against trusted Certificate Authorities (CAs) to allow users to better filter log entries, added support for fetching the log’s public keys using [TUF](https://theupdateframework.io/), solved outstanding issues to make the system more reliable, and made the associated GitHub reusable workflow ready for use. This last item allows anyone to monitor the log via the [provided reusable workflow](https://github.com/sigstore/rekor-monitor?tab=readme-ov-file#github-workflow-setup), lowering the barrier of entry so that anyone with a GitHub repository can run their own monitor.

## What’s next

A next step would be a hosted service that allows users to subscribe for alerts when a new entry containing relevant information (such as their identity) is added. This could work similarly to [GopherWatch](https://www.gopherwatch.org/), where users can subscribe to notifications for when a new version of a Go module is uploaded.

A hosted service wi...