---
title: Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files
url: https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:38.777962
---

# Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files](https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html)

**Swati Khandelwal**Sep 17, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJbYvRH1MRTGK43JYSWe2X3djxWAuNa3_r94FvOPBjt9sWrkRiEQi7D0DPksj3NH9vDPjm7MGSGY9UEc7JqePjd4aA-c4zuMzLZXH0Y5NWKWGnzNgbFe0tYlEFSFLrJFWVRuRKs_PQN8IKkdzYYNn8T7YWuUkZC4_2skq3deXYAw7i0aqWdx6G0FQwVzs/s1700-nu-rw-lo-l85-e365/docker-macos.jpg)

Malicious code running inside a **Docker Sandboxes** virtual machine on macOS could escape the project directory shared into it and read or change files anywhere else on the host, Docker warns in a [security announcement](https://docs.docker.com/security/security-announcements/#docker-sandboxes-0420-security-update-cve-2026-77179-and-cve-2026-79994) on September 15.

The escape runs with the rights of the host account that runs the virtual machine. The flaw, [CVE-2026-77179](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/77xxx/CVE-2026-77179.json), is rated Critical, affects versions 0.28.0 up to but not including 0.42.0 on macOS, and was fixed in [0.42.0](https://github.com/docker/sbx-releases/releases/tag/v0.42.0) on September 7.

Docker Sandboxes runs each AI coding agent in its own small virtual machine with the project directory shared in. The code that could escape is whatever runs inside that machine, such as a coding agent that has been turned against its user, or anything malicious the agent installs and runs.

Docker has not reported any exploitation. CISA's added assessment on the CVE record lists exploitation as none, and the flaw is not in CISA's Known Exploited Vulnerabilities catalog as of the catalog version released on September 16.

The flaw needs malicious code inside the sandbox, and protecting the host from what an agent runs is what the sandbox is for. The agent installs packages and runs commands with sudo inside the virtual machine, and Docker's [isolation documentation](https://docs.docker.com/ai/sandboxes/security/isolation/) says the hypervisor boundary "is the isolation control, not in-VM privilege separation."

The escape goes through the virtio-fs host server, the host side of the file sharing between the Mac and the virtual machine, which followed symlinks when it reopened a removed file from a stored path, Docker said.

A guest, meaning whatever runs inside the virtual machine, could replace a parent directory with a symlink and then read or change files as the VMM user, the host account under which the virtual machine monitor runs, Docker said, "potentially leading to code execution on the host."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Docker's documentation has said [since March](https://github.com/docker/docs/commit/cdde205ba837f5c3deff203900d35153882631f0) that symlinks pointing outside the workspace, Docker's term for the shared project directory, are not followed.

The same release fixes a second flaw, [CVE-2026-79994](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/79xxx/CVE-2026-79994.json), rated High by Docker with a CVSS score of 8.7, in the relay that allows a sandbox to connect to Unix domain sockets within its authorized workspace.

The relay checked that a socket path was inside the workspace, then reconnected using the path name. A guest that replaced a directory along that path with a symlink between the check and the connection could make the host connect to any AF\_UNIX socket outside the workspace, Docker said, "exposing data or host-side capabilities provided by that socket."

That flaw affects versions 0.37.0 through 0.41.9, but not 0.42.0. Docker lists the first flaw as macOS-only but states no platform for it, whereas Docker Sandboxes runs on macOS, Windows, and Linux hosts. CISA's assessment on its record also lists exploitation as none, and it is not in the KEV catalog either.

### Affected Versions and What to Install

| CVE | Component | Affected versions | Platform | Docker rating |
| --- | --- | --- | --- | --- |
| CVE-2026-77179 | virtio-fs host server | 0.28.0 up to but not including 0.42.0 | macOS | Critical, CVSS 9.4 |
| CVE-2026-79994 | Guest-to-host Unix socket relay | 0.37.0 up to but not including 0.42.0 | None stated | High, CVSS 8.7 |

1. Update to 0.42.0 or later. As of September 17, the most recent release is 0.43.0, published on September 15.
2. If you cannot update yet, use [clone mode](https://docs.docker.com/ai/sandboxes/usage/#clone-mode) and avoid adding read-write host mounts. That is Docker's advice for both flaws.

By default, sbx run shares the current directory into the sandbox with read and write access. Clone mode works only when the project is a Git repository, and it is set when the sandbox is created, so an existing sandbox has to be removed and created again with --clone.

Clone mode protects the repository from changes, not from reading. The repository is mounted read-only at /run/sandbox/source, and untracked files such as .env stay readable inside the sandbox, Docker's documentation says.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

Docker published the CVE records and the advisory on September 15, eight days after 0.42.0 shipped.

The [0.42.0 release notes](https://github.com/docker/sbx-releases/releases/tag/v0.42.0) on GitHub and on Docker's documentation site do not name either CVE as of September 17. Among routine fixes, they list one for "a sandboxed process could get the daemon to open a host D-Bus transport and execute an arbitrary command on the host." Docker has not connected that fix to either CVE.

The record for CVE-2026-79994 [initially listed](https://github.com/CVEProject/cvelistV5/commit/f0a7e57b413b6619561661c8a48d08599b7a01a5) 0.41.0 as the first fixed version and linked to a 0.41.0 release ...