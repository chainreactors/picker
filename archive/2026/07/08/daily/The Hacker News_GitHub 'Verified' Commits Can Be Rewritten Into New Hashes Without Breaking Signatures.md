---
title: GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures
url: https://thehackernews.com/2026/07/github-verified-commits-can-be.html
source: The Hacker News
date: 2026-07-08
fetch_date: 2026-07-09T06:03:34.025282
---

# GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures](https://thehackernews.com/2026/07/github-verified-commits-can-be.html)

**Swati Khandelwal**Jul 08, 2026DevSecOps / Open Source Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifE8OSGx2cVUZ1jiVnMC-LHyladj2cJ1FWw2-t0wDJEK4Icxrhk_bFReZr8jCiNkmpamFxdBGLpgruMJh1g7c687TCf4R76GG8xJEzB9kzPLTXo18DUZkT9_T5LHeikWsoEDeBm-gapabqgRUl2sAyhaPeYOWIs7Re0-jr2CMoKVn5AzlXdU1W6oWIy6mv/s1700-e365/git-hash.jpg)

New research shows that a signed Git commit's hash is not the one-of-a-kind name that much of the software world assumes it to be. Given any signed commit, someone without the signing key can mint a second commit with the same files, author, and date, and a valid signature, GitHub still stamps "Verified."

Everything a reviewer would check matches. The commit's hash does not. That matters because so many systems treat a verified commit hash as a permanent, unique name for its contents.

Here is the concrete failure: block a bad commit by its hash, and an attacker can re-push the same content under a fresh, still-"Verified" hash your blocklist has never seen. Deduplication, provenance logs, and reproducible-build records that key on the hash inherit the same soft spot.

A compromised or hostile mirror can hand cloners validly signed commits whose hashes differ from those on the canonical forge.

What this is not is a way to slip different code past a signature check. The files are identical in every copy, so a hash you pinned still fetches exactly the content you expected, or fails.

There is no CVE and no vendor advisory, and nothing to change in your own repo: the flaw is in how a forge decides what "Verified" means, and the fix belongs on the forge's side.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The work comes from [Jacob Ginesin](https://arxiv.org/abs/2607.02820), a PhD student at Carnegie Mellon University and a cryptographic auditor at Cure53. His five-page paper, posted to arXiv on July 2, comes with a [public tool](https://github.com/JakeGinesin/git-chain-malleator) that runs all three attacks, plus two demo repositories where the malleated commits still show "Verified" on GitHub.

Because every commit names its parent by hash, malleating one commit forces new hashes on the commits above it. The tool rewrites that chain to keep it consistent. A signed descendant, though, loses its own badge the moment its parent pointer changes. Ginesin calls the effect "**hash chain malleability**."

The cause is signature malleability. A commit's hash is computed over everything inside it, including the raw bytes of the signature in its header. Many signatures can be rewritten into a different but still-valid form, and changing those bytes changes the hash without touching a line of code.

The three routes cover every GPG scheme GitHub verifies, plus S/MIME:

* **ECDSA keys:** flip the signature with a classic piece of elliptic-curve algebra (turn the value s into n - s). Both forms are valid. This passes a local git verify-commit and earns a GitHub badge.
* **RSA and EdDSA keys:** add an extra, ignored field to the signature's "unhashed" section, the part the signature deliberately does not cover. The signature still checks out, but the commit's bytes, and its hash, change. Local and GitHub both accept it.
* **S/MIME (X.509) keys:** rewrite a length field in the signature's DER structure into a longer, non-standard form. A strict local check (via gpgsm) rejects it, but GitHub still marks it "Verified," both of which the tool reproduces.

The three routes share one enabler: GitHub does not normalize a signature before checking it. No strict encoding on S/MIME, no stripping of those OpenPGP fields, and non-canonical ECDSA values accepted as-is.

GitHub then files a "Verified" record against each commit hash and does not re-check it, so a commit stays "Verified" even after its signing key is revoked. Push an original and its twin to two branches, and GitHub's compare view treats them as divergent histories, one commit ahead and one behind, despite identical files.

To be clear: this is not a hash collision. It does not break SHA-1 or SHA-256, and has nothing to do with Git's move to SHA-256. Nobody is forcing two different commits to share one hash; it is the reverse, one commit that can be written many valid ways, each with its own hash.

The core move is old. Bitcoin fought the exact same [ECDSA symmetry](https://en.bitcoin.it/wiki/Transaction_malleability) years ago, when anyone could flip the s value in a transaction signature and change the transaction's ID without the owner's key. The fix was to accept only the "low-S" form, and later to move signatures out of the ID with SegWit.

The paper's fixes rhyme with that: canonicalize the encoding before you trust the hash. A known lesson, not exotic new cryptography.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

The paper also connects this to the recent GitHub Actions tag hijacks, the 2025 [tj-actions/changed-files](https://thehackernews.com/2025/03/github-action-compromise-puts-cicd.html) and 2026 [trivy-action](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html) attacks (it cites the latter). After those, the advice was simple: pin to a full commit hash, not a movable tag. That advice still holds.

Pinning stopped those attacks, and this research does not change that. Its point is narrower. In the Trivy case, the malicious commits stood out because they could not be validly signed. This is a caution against leaning too hard on that tell: a valid signa...