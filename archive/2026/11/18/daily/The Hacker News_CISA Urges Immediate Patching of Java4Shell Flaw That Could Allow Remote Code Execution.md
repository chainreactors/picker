---
title: CISA Urges Immediate Patching of Java4Shell Flaw That Could Allow Remote Code Execution
url: https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html
source: The Hacker News
date: 2026-11-18
fetch_date: 2026-11-19T09:47:36.505354
---

# CISA Urges Immediate Patching of Java4Shell Flaw That Could Allow Remote Code Execution

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

# [CISA Urges Immediate Patching of Java4Shell Flaw That Could Allow Remote Code Execution](https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html)

**Ravie Lakshmanan**Nov 18, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivmrsz2fViEN49Su385gmuAShCPcxobsMF-FbR9t1sXw6aEbOMzFUT5YktViqASQUXP3bLT13HYMAE1wBQTN0ZRDGXWFJUy_EWOKhOjR7jSz-bhEK8jas_v9wWUYxevCAZt4PzOCaGNLLC96kDwFjtKBuXVW2O3K2BK9AO5nyZutFf_uCaZtvyaQ2qf8gK/s1700-nu-rw-lo-l85-e365/cisa-java.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has urged organizations to immediately patch a newly disclosed critical security flaw impacting Oracle Java.

The flaw, tracked as **[CVE-2026-114938](https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html)** (CVSS score: 8.1), refers to a case of out-of-bounds write that can lead to denial-of-service (DoS) or remote code execution under certain conditions.

"This critical memory-corruption vulnerability, known as '[Java4Shell](https://calif.io/java4shell),' affects the Base64 decoder of the x86-64 HotSpot Java Virtual Machine (JVM), which is part of the Java Development Kit (JDK)," CISA [said](https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching). "Specially crafted Base64 input could crash the JVM and allow for unauthenticated remote code execution."

Patches for the flaw have been released by [Oracle](https://www.oracle.com/security-alerts/cspunov2026.html) and [OpenJDK](https://openjdk.org/groups/vulnerability/advisories/2026-11-17). As of writing, there is no evidence the vulnerability has been exploited in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

As [reported](https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html) previously by The Hacker News, Java4Shell can enable attackers without an account to execute arbitrary code on Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins, and PingFederate, and with a login on Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit, and Spinnaker, under default settings.

Advisories for the flaw have been released by numerous security and software vendors, including [Aikido](https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938), [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2026-114938.html), [Blackpoint Cyber](https://blackpointcyber.com/blog/java4shell-cve-2026-114938-java-base64-decoder-flaw/), [Chainguard](https://www.chainguard.dev/unchained/java4shell-how-a-malformed-base64-string-breaks-the-jvm-on-avx-512), [Cisco Talos](https://blog.talosintelligence.com/java4shell/), [Cycode](https://cycode.com/blog/java4shell-cve-2026-114938/), [Datadog](https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/), [Dynatrace](https://www.dynatrace.com/news/security-alert/cve-2026-114938/), [Endor Labs](https://www.endorlabs.com/learn/java4shell-unauthenticated-rce-reported-in-openjdk-17-cve-2026-114938), [Field Effect](https://fieldeffect.com/blog/java4shell-exposure-concerns), [Hadrian](https://hadrian.io/vulnerability-alerts/oracle-critical-security-patch-update-java-17-rce-claims), [Horizon3.ai](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114938/), [Miggo](https://www.miggo.io/post/java4shell), [Orca Security](https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/), [Qualys](https://blog.qualys.com/vulnerabilities-threat-research/2026/11/17/how-to-find-mitigate-and-patch-the-critical-java4shell-flaw-cve-2026-114938-now), [Rapid7](https://www.rapid7.com/blog/post/etr-cve-2026-114938-reported-critical-pre-authentication-remote-code-execution-java-17/), [Red Hat](https://access.redhat.com/security/vulnerabilities/RHSB-2026-018), [SentinelOne](https://www.sentinelone.com/blog/java4shell-vulnerability-in-openjdk-enables-rce-on-avx-512-cpus/), [Sophos](https://www.sophos.com/en-us/blog/java4shell-could-allow-remote-code-execution), [Tanium](https://www.tanium.com/blog/java4shell-cve-2026-114938-find-every-java-runtime), [Tenable](https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability), [Upwind](https://www.upwind.io/blog/java4shell-what-we-know-now-and-what-comes-next), [VulnCheck](https://www.vulncheck.com/blog/java4shell), [watchTowr](https://watchtowr.com/intelligence/java4shell-cve-2026-114938-faq/), and [Wiz](https://www.wiz.io/blog/cve-2026-114938-rce-java4shell-openjdk).

In an update shared on November 18, 2026, the Keycloak team said an instance can be considered at risk if the following conditions apply -

* It runs an unpatched OpenJDK build from 17.0.6 onward, including unpatched OpenJDK 21 and 25 builds
* Its x86-64 host or virtual machine exposes the avx512vbmi CPU feature to Java
* The running JVM has Base64 intrinsics enabled and has not been limited to AVX2 with -XX:UseAVX=2

"The x86-64 Keycloak container images tagged 26.8.2-1 and 26.8.2-2 bundle an affected OpenJDK 21.0.13 build," the team [said](https://www.keycloak.org/2026/11/java4shell-vulnerability-cve-2026-114938). "These image tags alone do not establish whether your deployment is exploitable: check the CPU feature and effective JVM flags."

"A Keycloak ZIP or TAR.GZ distribution started directly on a host can also be affected; the conditions depend on its Java runtime and CPU, not on whether it runs in a container."

Keycloak is also recommending that users run the below command to check the CPU feature on a host or virtual machine -

```
grep -m1 '^flags' /proc/cpuinfo | grep -qw avx512vbmi && echo 'AVX-512 VBMI available'
```

If the output of the command returns nothing, it indicates that the CPU does not expose AVX-512 VBMI and is not known to be affected by the fl...