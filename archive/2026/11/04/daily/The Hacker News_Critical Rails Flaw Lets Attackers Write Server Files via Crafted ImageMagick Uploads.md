---
title: Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Uploads
url: https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:12.792360
---

# Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Uploads

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Uploads](https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html)

**Swati Khandelwal**Nov 04, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaJWnScdkMx0R5_Zt00NtYVNjNavBR7IMrLzJM_tZGMTpZtAvV7uNWt6BQbBrlUzH-aBoj_ZmMEOG__aTA8VmfTeiHUR9gfqNe2eYf9fSM-sYQkmCOg10qZ3ZaKyM_RS1QUQhm8s5NMw-xnYaWMDgDakmFyp9tbJgQ4hOZTf0cxe9E6x7uWt3JeN6bS3k/s1700-nu-rw-lo-l85-e365/ruby-rails.jpg)

A critical flaw in **Ruby on Rails** could allow an unauthenticated attacker to write arbitrary files on an app's server by uploading a crafted file if the app processes uploads using **ImageMagick**. The Rails project disclosed the flaw in [an advisory](https://github.com/rails/rails/security/advisories/GHSA-f3w6-w445-fwh9) and fixed it in versions 8.1.4.1 and 8.0.5.2.

The flaw is in Active Storage, the part of Rails that handles file uploads. Some apps store uploaded files using Active Storage's Disk service, which stores them on the server's disk. In those apps, an attacker could also read any file the app can read.

Those files typically include the app's secret\_key\_base and its credentials for other systems, according to Rails. Reading them may in turn allow remote code execution or lateral movement into those systems.

Rails rates the flaw 9.8 out of 10 on the CVSS scale. It is tracked as GHSA-f3w6-w445-fwh9 and does not yet have a CVE identifier.

ImageMagick selects a format handler, which it calls a coder, based on the file's content. Some coders act on other files named inside the image, not on the image itself. Active Storage imposes no limits on which coders an upload can use, so the server's own ImageMagick policy was the only limit.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The ImageMagick analyzer in Active Storage runs when a file is attached. Attaching the upload is enough to reach the flaw. The app does not have to make a variant (a transformed copy of the image) or a preview, or call analyze.

An uploaded SVG file reached ImageMagick's MSL coder through that analyzer, according to [the commit that fixed the flaw](https://github.com/rails/rails/commit/468aa9a93fc98f5476b6821770f4ccfcb7f7d328). MSL is a scripting coder that reads and writes files named by its script.

Rails said one attack chain was reported to it, but it does "not assume it is the only one that exists." The advisory does not say whether the flaw has been exploited.

The flaw was reported through HackerOne by RyotaK, a researcher at GMO Flatt Security.

### Which Rails Apps Are Affected

An app is affected only if all three of these are true:

* It uses ImageMagick for Active Storage image processing. That is the setting `config.active_storage.variant_processor = :mini_magick`, the default for apps on `load_defaults 6.1` or earlier.
* Its ImageMagick security policy does not already block the coders involved. Rails says the policies that Debian and Ubuntu ship do not.
* It accepts file uploads from untrusted users.

To check the first condition, look at `config.active_storage.variant_processor`. If it is not set, the default depends on `load_defaults`: `:mini_magick` before 7.0, and `:vips` from 7.0 on. The same setting decides which library analyzes uploads, not only which one makes variants.

Every Active Storage version before 8.0.5.2 is affected, as are 8.1 versions before 8.1.4.1. Release series older than 8.0 are no longer supported, and Rails will not release fixed versions for them.

In July, Rails fixed [a different critical Active Storage flaw](https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html), CVE-2026-66066, which affected apps that use libvips instead of ImageMagick. Apps using ImageMagick were not exposed to that flaw's attack path, but they can be exposed to this one.

The same releases fix a second Active Storage flaw, [GHSA-v924-7rp8-4mxh](https://github.com/rails/rails/security/advisories/GHSA-v924-7rp8-4mxh), which Rails rates high with a CVSS score of 8.8. Active Storage passed uploads to ImageMagick and FFmpeg under temporary file names that kept the uploaded file's extension.

Those tools can pick a decoder from the extension when a file's content does not show its format. So an attacker who chose an upload's filename and declared its content type could choose the decoder that processes it.

### What to Do

Rails strongly recommends upgrading as soon as possible. The two releases fix [21 security issues](https://www.openwall.com/lists/oss-security/2026/11/04/2) in total.

The fixed versions ship an ImageMagick security policy. MiniMagick is the Ruby gem Active Storage uses to call ImageMagick. In its default setup, every ImageMagick command it runs applies the policy, not only commands from Active Storage.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The policy blocks the MSL coder; coders that read or delete files other than the image; coders that fetch remote or local references or display them on a screen; every coder backed by Ghostscript, along with the gs delegate; and @filename indirection.

* Upgrade to Rails 8.1.4.1 or 8.0.5.2. Apps on `:mini_magick` also need mini\_magick 5.1 or later, or they raise an error at boot. Rails 8.0 gets security fixes only until November 7, 2026, under its [maintenance policy](https://rubyonrails.org/maintenance).
* Confirm that the app loads the new policy, as the [Active Storage guide](https://guides.rubyonrails.org/active_storage_overview.html) describes, by running `bin/rails runner 'puts MiniMagick.identify { |i| i.list "policy" }'`.
* Check whether the shipped policy reaches the app at all. It does not reach an app that replaces `MiniMagick.cli_env` after boot, clears the environment with `MiniMagick.cli_prefix`, or installs its own `MiniMagick::Shell`. Such an app must put the rules in I...