---
title: Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely
url: https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
source: The Hacker News
date: 2026-10-07
fetch_date: 2026-10-08T08:08:36.216857
---

# Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely](https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html)

**Swati Khandelwal**Oct 07, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyMSiFF8XNm1OpF4uWou7e4nt4fqsuPc0IXyUXhHky9w8ydKkauWm_j0yxdpMsRFlDx-5PHhtAxYNg3Z-rYqvexgILhokXO8tARRTtDHn2P83GOlUhiD6jN7rtkf3Ul1-Hp7O4VyvwV6EGNUgjmcC-B_o_P-xQy9eD7RaTnO_RoDpDwgjTePDvkjC9xso/s1700-nu-rw-lo-l85-e365/lm.jpg)

A critical vulnerability in **LMCache**, open-source software that speeds up large language model (LLM) servers such as vLLM, lets an attacker run code on the cache server without logging in, and no fixed version is available.

The flaw is in LMCache's [multiprocess mode](https://docs.lmcache.ai/mp/index.html), where the cache runs as a standalone server that LLM workers reach over the ZeroMQ messaging library. A single network message to that server can run commands as the user the LMCache process runs as.

The server can be reached from another machine only when an operator sets it to listen on a routable address, rather than the localhost it uses by default.

[JFrog disclosed the flaw](https://research.jfrog.com/vulnerabilities/lmcache-is-vulnerable-to-unauthenticated-remote-code-execution-via-pickle-deserialization-on-the-multiprocess-zmq-transport-cve-2026-105192-jfsa-2026-001694382/) on October 7 and assigned it a severity score of 9.8 out of 10, in the critical range, the rating it gives a server bound to a routable address.

The vulnerability, tracked as [CVE-2026-105192](https://www.cve.org/CVERecord?id=CVE-2026-105192), affects LMCache from version 0.3.9, released in October 2025, through 0.5.5, the latest stable release, and is also present in the 0.5.6 release candidates and the development branch. No fixed version exists.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Whether a server is exposed comes down to one setting. By default, the multiprocess server listens only on the local machine, so another host cannot reach it. It becomes reachable when an operator starts it with a routable address, much like multi-node deployments share a cache across machines.

LMCache's own [example Kubernetes deployment](https://github.com/LMCache/LMCache/blob/v0.5.5/examples/multi_process/lmcache-daemonset.yaml) starts the server that way, listening on every network interface. A copy of LMCache running inside a single vLLM process does not open the port at all.

The ZeroMQ socket the multiprocess server opens for worker processes to register and share cached data has no authentication. One type of message is [unpacked with pickle](https://github.com/LMCache/LMCache/blob/v0.5.5/lmcache/v1/platform/base/ipc_wrapper.py), a Python format that can carry code and run it as the data is decoded. The server unpacks it while still reading the message's arguments, before any check of the message's type, so a crafted message can run the sender's code.

The code runs with the privileges of the LMCache process. On the project's official container images, that process runs as root, according to JFrog. The flaw was found by Yuval Moravchick of JFrog's security research team.

There is no patched release. Until one ships, JFrog advises operators not to assign the multiprocess server a routable address and to keep its port on the local machine or on a trusted cluster network. A firewall that limits who can reach the port lowers the risk but does not remove it, because any host that can still open a connection can run code.

LMCache has [not published a security advisory](https://github.com/LMCache/LMCache/security/advisories) for the flaw. JFrog's advisory does not provide operators with a way to determine whether a server has already been attacked.

### Other Reports and a Related vLLM Fix

Separately, a GitHub user opened six additional LMCache security reports on October 6, the day before CVE-2026-105192 was made public. They allege [unauthenticated access to cached data](https://github.com/LMCache/LMCache/issues/5507) belonging to different tenants, as well as to [several network services](https://github.com/LMCache/LMCache/issues/5508) that execute commands without a login.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The reports come from one account, rest on proof-of-concept claims, and have no CVE, no confirmation from the maintainers, and no fix. One points to a default LMCache that has since changed: an admin HTTP server that listened on every network interface in 0.5.5 listens only on the local host in the 0.5.6 release candidates.

A related flaw in vLLM is already fixed. Before version 0.30.0, released September 22, a single request carrying a malformed cache\_salt value could crash the engine on deployments that use the LMCache multiprocess connector, a denial-of-service bug tracked as [CVE-2026-105756](https://github.com/vllm-project/vllm/security/advisories/GHSA-2823-qmq8-rwvj). It is rated 6.5 and does not allow code execution.

The core mistake, handing data from an unauthenticated network socket to pickle, is the same one researchers found across other AI inference frameworks in November 2025, in a group of flaws they called [ShadowMQ](https://thehackernews.com/2025/11/researchers-find-serious-ai-bugs.html). Whether LMCache's code shares a common source with those projects has not been established.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Shar...