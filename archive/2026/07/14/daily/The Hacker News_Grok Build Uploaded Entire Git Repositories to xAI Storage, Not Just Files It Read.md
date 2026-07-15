---
title: Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read
url: https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:50:00.391464
---

# Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read

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

# [Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html)

**Swati Khandelwal**Jul 14, 2026Artificial Intelligence / Data Privacy

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCYpkCY1h-DxV5yfxpkGspVFATaUS27q_vpRgQ2ebzGvc6YgSsYk81jDt3SkJQgxVCL8dWJqzDE3t6iUt4ceeTvA9LG8Z9cA65uBXC05Lkdv1xKLNBMH88dTa_6XCet3a0wf1VwfyxQsx_1AKc3lmHCxqiZHKTfvk9kJqvo0i15biGekBijFPNN16JHBM/s1700-e365/grok.jpg)

xAI's Grok Build coding CLI was uploading entire Git repositories, full commit history and all, to a Google Cloud Storage bucket run by xAI, not just the files a coding task needed.

A researcher publishing as [cereblab](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547), testing version `0.2.93`, captured one of those uploads, cloned the git bundle out of the intercepted request, and pulled back a file the agent had been told in plain terms not to open.

The upload rode a separate channel from the model itself, and the byte split is hard to argue with. On a 12 GB repo of files the model never read, model-turn traffic to `/v1/responses` came to about 192 KB while the storage channel to `/v1/storage` moved 5.10 GiB, a roughly 27,800x gap between what the model needed and what left the machine.

That storage upload ran as 73 chunks of about 75 MB, every one returning HTTP 200, and across the researcher's size sweep the volume tracked total repo size. The destination bucket, `grok-code-session-traces`, is named in the binary and in a staged `metadata.json` whose per-file paths point at `gs://grok-code-session-traces/`.

The unread file was `src/_probe/never_read_canary.txt`, planted with a unique marker. Cloning the captured bundle recovered it verbatim along with the repo's full commit history, and the same test replicated on a second, unrelated repo. What the captures establish is transmission, acceptance, and storage, not training.

The teardown does not claim xAI trained on the code, that staff read it, or that gitignored files are always swept in. Tracked files plus history is what the wire shows.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The secrets path is separate and simpler. When Grok reads a file, its contents go into the model turn, and a tracked `.env` went with them unredacted, canary `API_KEY` and `DB_PASSWORD` values and all. The same content also landed in a `session_state` archive bound for storage. The planted secrets were fake, so nothing real leaked in the test. The behavior is still the problem: a credential file the agent read during a task went out and was stored with no redaction.

The setting most developers would reach for did nothing here. With "Improve the model" turned off, Grok still uploaded the repository, and the server's own `/v1/settings` response kept returning `trace_upload_enabled: true`. That toggle governs whether your data trains the model. It does not govern whether your code leaves the machine. Those are two different controls, and only one of them was exposed to the user.

Every cloud coding agent has to send some source to a remote model to do its job, so the first channel is expected. Sending the entire tracked repository and its history is a wider boundary than sending the files a task needs.

A repo can hold proprietary code, internal URLs, customer data, and credentials that were removed from the working tree but still sit in commit history. In [cereblab's own cross-tool comparison](https://github.com/cereblab/grok-build-exfil-repro/blob/main/COMPARISON.md), Claude Code and Codex sent no repository bundle; Gemini sent none in an idle test, though its realistic-task run was quota-blocked before it finished.

Grok Build was the outlier. Those are still cloud tools that send the files they open, so "local only" is the wrong mental model for any of them. But wholesale collection of the workspace was specific to Grok Build.

## xAI's response

On July 13 the same `0.2.93` binary stopped making storage requests. cereblab retested six times and saw zero `/v1/storage` uploads, and the server now returned `disable_codebase_upload: true` and `trace_upload_enabled: false`.

The developer Peter Dedene [reported the same flag returned for his account](https://x.com/dedene/status/2076394152779301305), so the shutoff was not only cereblab's single-machine observation. The tested client stayed on `0.2.93` while its server settings changed, so this was a server-side switch, not a fix shipped in an update. xAI has not confirmed whether it reaches every account or is permanent.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

xAI has so far addressed the issue on X rather than through a security advisory or changelog note. The [@SpaceXAI account](https://x.com/SpaceXAI/status/2076692402442846289) said enterprise teams on zero data retention never have code or trace data stored, that API-key use respects ZDR, and that consumers who have not enabled it can run `/privacy` in the CLI to disable retention and delete previously synced data.

Elon Musk went further, [saying](https://x.com/elonmusk/status/2076739687658496209) all user data uploaded before now would be "completely and utterly deleted," with nothing left behind. ZDR covers enterprise teams and API use, so for individual subscribers the `/privacy` command is the control on offer.

For anyone who already ran the tool, the move is not to wait on xAI. Rotate any credential Grok could have sent: anything it read, anything in a tracked file, and anything in the git history the bundle carried, including a secret you committed and later deleted...