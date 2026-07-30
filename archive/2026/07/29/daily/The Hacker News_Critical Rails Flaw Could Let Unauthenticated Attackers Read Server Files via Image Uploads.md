---
title: Critical Rails Flaw Could Let Unauthenticated Attackers Read Server Files via Image Uploads
url: https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:42.325868
---

# Critical Rails Flaw Could Let Unauthenticated Attackers Read Server Files via Image Uploads

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

# [Critical Rails Flaw Could Let Unauthenticated Attackers Read Server Files via Image Uploads](https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html)

**Swati Khandelwal**Jul 29, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjswJ2Clfk448ySFwyQiVVviqzKzT4B9iwnvVio4_dzvA1TXPnNuDJUI8MozBddPvdWmL2JH3jVvzTxg8A2Z6X9qNPYtxjuVx7RKQkMW8vNVBIEs0sgcrLfywQVufYMEKpxa0vgo2k24bNa_EJaudCFTsvlqQKqbT3jsuzRJdI26GR4pRJrkNKAFx_xiKk/s1700-e365/rubyrails.jpg)

Ruby on Rails has released fixes for a critical Active Storage vulnerability that could let unauthenticated attackers read arbitrary files from application servers through crafted image uploads.

Tracked as **CVE-2026-66066** (CVSS score: 9.5), the flaw can expose the Rails process environment and secrets such as `secret_key_base`, the Rails master key, database passwords, cloud storage credentials, and API tokens. Those secrets may enable remote code execution (RCE) or lateral movement into connected systems.

Affected applications use libvips for Active Storage image processing and accept image uploads from untrusted users. Rails selects Vips under `load_defaults 7.0`, and later defaults retain it.

Ethiack and GMO Flatt Security list the affected ranges as Rails 7.0.0 through 7.2.3.1, Rails 8.0.0 through 8.0.5, and Rails 8.1.0 through 8.1.3. Rails 6.0.0 through 6.1.7.10 releases are affected only when Active Storage is configured to use Vips, which was not the default processor in Rails 6.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The Rails Security Team told The Hacker News that the researchers' affected range is accurate. It said the public advisory covers Rails releases under security support, meaning Rails 7.2, 8.0, and 8.1, while Rails 6.x is also affected when Vips is enabled, which was not the default at the time. Applications using MiniMagick are not exposed through this specific attack path. Rails 7.1 and earlier are end of life and will receive no backport, so affected applications must upgrade to Rails 7.2.3.2 or later.

Operators should upgrade to Rails 7.2.3.2, 8.0.5.1, or 8.1.3.1 and rotate every secret readable by the application process. Patched installations require libvips 8.13 or later and, when ruby-vips is installed, ruby-vips 2.2.1 or later.

Neither research team had published a proof-of-concept (PoC) as of 17:30 UTC on July 29, 2026. A third-party [GitHub repository](https://github.com/Zer0SumGam3/CVE-2026-66066-POC) published after that check claims to reproduce the full arbitrary-file-read-to-RCE chain in a loopback-only Docker lab using Rails 8.1.3, with Rails 8.1.3.1 as the patched control. The code uses a crafted MATLAB/HDF5 upload to read the Rails process environment, recover `SECRET_KEY_BASE`, sign an embedded Marshal payload, and trigger an out-of-band `curl` callback. The Hacker News has not independently validated the PoC.

The flaw sits at the trust boundary between Active Storage and libvips. The [Rails security advisory](https://github.com/rails/rails/security/advisories/GHSA-xr9x-r78c-5hrm) says libvips supports loaders, savers, and other operations, some backed by third-party libraries and marked "unfuzzed" or "untrusted" because they are unsafe for hostile input. Active Storage did not block them, allowing a crafted upload to invoke one and disclose files readable by the Rails worker.

A vulnerable application does not need to expose a dedicated resize or thumbnail operation. "Generating variants is not a separate requirement," Rails said. The [public patch](https://github.com/rails/rails/commit/349e7a5d5b4b715af1e416db824f3c078a7d59e5) also shows that both the Vips analyzer and transformer passed untrusted attachments to the unsafe operations.

A successful request gives the attacker an arbitrary file-read primitive. Code execution or lateral movement would depend on what the attacker extracts and what those credentials can reach. Rails tells operators to rotate `secret_key_base`, the master key and decrypted credentials, database credentials, Active Storage service keys, and third-party tokens.

The patch calls `Vips.block_untrusted(true)` when Active Storage starts. Applications that cannot immediately update Rails can set `VIPS_BLOCK_UNTRUSTED` when running libvips 8.13 or later, or call `Vips.block_untrusted(true)` with ruby-vips 2.2.1 or later. Rails says earlier libvips versions cannot block these operations, so applications must upgrade libvips or remove it from the application.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

Rails credited André Baptista, Bruno Mendes, and Rafael Castilho of [Ethiack](https://ethiack.com/info-hub/research/kindarails2shell-rails-rce-cve-2026-66066), and RyotaK of [GMO Flatt Security](https://blog.flatt.tech/entry/kindarails2shell_rails), with independently reporting the issue. The researchers have not disclosed the malicious format, file-read construction, or RCE chain. Rails said further technical details will be released no later than August 28, 2026.

The Rails Security Team told The Hacker News that it is not aware of exploitation or attempted exploitation before or after disclosure. It also said Rails has no telemetry or reasonable estimate for how many applications use Active Storage with Vips and accept untrusted image uploads. The Hacker News has also contacted Ethiack about the attack chain and will update this story with any response.

A review by The Hacker News at 17:30 UTC on July 29 found that `CVE-2026-66066` was not listed in version 2026.07.27 of CISA's [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulne...