---
title: Ruby Ships Fixes for 7 Flaws, Including Critical Ruby2Shell, Said to Hit Default Rails Apps Pre-Auth
url: https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:13.573931
---

# Ruby Ships Fixes for 7 Flaws, Including Critical Ruby2Shell, Said to Hit Default Rails Apps Pre-Auth

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Ruby Ships Fixes for 7 Flaws, Including Critical Ruby2Shell, Said to Hit Default Rails Apps Pre-Auth](https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html)

**Swati Khandelwal**Nov 19, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7rmcgZ7yffFsn_7SX4iQcfMhw1dgsxPFXXh6TUunbQ9VaxZh8O5-AFT2V3q0PE7Wx0rW9nLKuB73eluixYuM9N38Dvq_Gjs1nNOXVk3e71jjfhHoP7W97eeuc5AivI3CQNxIrwSaPR9IGV0f2NZ7900Ihtkdgiw1ZivTvgVrXWH2CrX2X5MZGjos6-bs/s1700-nu-rw-lo-l85-e365/ruby.jpg)

Ruby contains seven memory-safety flaws in its regular expression engine and its string case-conversion code. For five of them, its maintainers say, proof-of-concept exploits, or PoCs, have shown that crafted input can run code on the machine.

"We are aware of PoCs that prove some of them can be used to trigger remote code execution," the maintainers said.

The project released fixed versions yesterday: Ruby 4.0.10, 3.4.13 and 3.3.14. Whether an application is at risk depends on whether an attacker can get crafted patterns or strings into the affected code, and the advisories report no attacks so far.

The other two flaws are weaker. The maintainers say one has proof-of-concept code that corrupts memory under an attacker's control but has not been shown to run code, and the other can only read memory it should not or crash the program.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The project set the seven out in a [security announcement](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/) and a separate advisory for each. The advisories rate three flaws critical, three high, and one moderate, and say which carry the remote-code-execution PoCs. In order of severity:

* **Critical.** `GHSA-34m4-m9fh-gqp5`, now tracked as `CVE-2026-132825`, a one-byte heap overflow when Ruby changes the case of a string in certain single-byte encodings, such as `ISO-8859-1` or `Windows-1252`. It has a remote-code-execution PoC. New [research from Veria Labs](https://verialabs.com/ruby2shell/), published on November 19 under the name **Ruby2Shell**, says the flaw is reachable over the network, without authentication, in the default configuration of Rails and classic-style Sinatra applications. An [analysis by Moritz Sanft](https://durendal.sh/blog/ruby-case-mapping-bugs), published the same day, traces the path through Rack, the request-handling layer under Rails: during its normal processing of a crafted form submission, Rack changes the case of one request field, so a newly generated Rails application reaches the flaw before any of its own code runs. Veria Labs says it will publish its proof of concept about a week after disclosure, once users have had time to upgrade. ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-34m4-m9fh-gqp5))
* **Critical.** `GHSA-7x2q-68qv-6p8x`, a double free when Ruby compiles a crafted regular expression that uses a character-class intersection (`&&`). It has a remote-code-execution PoC. ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-7x2q-68qv-6p8x))
* **Critical.** `GHSA-3p8q-wmhx-vm2w`, a heap overflow when the size of a compiled regular expression overflows during compilation. It has a remote-code-execution PoC. ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-3p8q-wmhx-vm2w))
* **High.** `GHSA-87fm-7w84-j2px`, a heap overflow when a case change produces a result larger than 4 GiB. It has a remote-code-execution PoC, though the size needed puts it out of reach for most requests. ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-87fm-7w84-j2px))
* **High.** `GHSA-7whj-cfh7-xgm4`, a heap overflow when Ruby turns a crafted compiled regular expression back into text with `Regexp#to_s`. It has a remote-code-execution PoC. ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-7whj-cfh7-xgm4))
* **High.** `GHSA-wpqw-5qxg-m68r`, an out-of-bounds read during case-insensitive matching. Its PoC shows attacker-controlled memory corruption, and the maintainers say remote code execution is possible but not shown. ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-wpqw-5qxg-m68r))
* **Moderate.** `GHSA-pvgc-g7gj-pv6h`, an out-of-bounds read when Ruby matches a case-insensitive backreference against a crafted subject string. The advisory says it "may disclose memory contents or crash the process." ([GitHub advisory](https://github.com/ruby/ruby/security/advisories/GHSA-pvgc-g7gj-pv6h))

The project credits Stephan Lipp of Ada Logics and Anthropic with four of the findings, and baba\_\_yaga, aphantom, Hiroya Fujinami and Hiroshi SHIBATA with the other three.

### Which Applications Are Exposed

The flaws are in Ruby's own code, so every application on an affected version carries them. Whether an attacker can reach one depends on how the application handles external input.

The regex flaws need an application that builds a regular expression from input an attacker controls and then compiles or runs it. Matching untrusted text against a pattern the developers wrote themselves does not pose the same risk, except in one case below.

The two case-conversion flaws do not involve regular expressions at all. They fire when the application changes the case of a crafted string, so code that runs case conversion over imported or outside text is worth checking. For the critical one, the Veria Labs research and Sanft's analysis report that the application's own code does not have to run the conversion in a default Rails setup, because Rack does it while processing a crafted request.

The one case is the moderate read flaw, which fires when the application matches a crafted subject string against a fixed pattern that uses a case-insensitive backreference. The announcement and advisories do not include the proof-of-concept code.

The fixes ...