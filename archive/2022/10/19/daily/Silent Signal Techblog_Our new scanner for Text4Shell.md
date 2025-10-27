---
title: Our new scanner for Text4Shell
url: https://blog.silentsignal.eu/2022/10/18/our-new-scanner-for-text4shell/
source: Silent Signal Techblog
date: 2022-10-19
fetch_date: 2025-10-03T20:18:45.502474
---

# Our new scanner for Text4Shell

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2025 © Silent Signal

![Our new scanner for Text4Shell](/wp-content/uploads/2022/10/screenshot-1.png)

# Our new scanner for Text4Shell

[dnet](/authors/dnet.html) 2022-10-18

Some say, [CVE-2022-42889](https://securitylab.github.com/advisories/GHSL-2022-018_Apache_Commons_Text/) is the new Log4Shell, for which we [developed our own tool to enumerate affected hosts](https://blog.silentsignal.eu/2021/12/12/our-new-tool-for-enumerating-hidden-log4shell-affected-hosts/) back in 2021. Others like Rapid7 [argue that it may not be as easy to exploit like Log4Shell](https://www.rapid7.com/blog/post/2022/10/17/cve-2022-42889-keep-calm-and-stop-saying-4shell/). Regardless of the severity and exploitability of this vulnerability, we quickly morphed a clone of our Log4Shell plugin into [an open source tool that can detect this vulnerability](https://github.com/silentsignal/burp-text4shell) reasonably well.

Unlike with Log4Shell, we found no trivial way to do nesting with variable expansion, so we have no hostname or username detection this time for the first release. Although these could be added easily through code execution, this requires OS-specific payloads, which just didn’t feel like a necessity for an MVP. Pull requests are welcome, though, so if you feel like adding this, we would be happy to merge a properly written patch.

Although the PoC presented in the original GitHub advisory contained RCE in itself, we chose the “dns” method mentioned by Rapid7 in their blog post. This way, we have a simple yet reliable detection method to use with Burp Collaborator that doesn’t depend on any OS-specific behavior.

Just as with Log4Shell, we created a Burp Extender plugin that registers itself as an Active scanner check and generates payloads. Synchronous interaction is logged using built-in scanner, while a background thread polls for Collaborator interactions once per minute to test for hosts and services doing asynchronous processing.

The plugin can be downloaded from [our GitHub repository](https://github.com/silentsignal/burp-text4shell) under a GPLv3 license, [pre-built JARs can be found on the Releases page](https://github.com/silentsignal/burp-text4shell/releases/), bug reports and pull requests are welcome.

[Twitter](https://twitter.com/intent/tweet?text=Our new scanner for Text4Shell&url=https://blog.silentsignal.eu/2022/10/18/our-new-scanner-for-text4shell/ "Share on Twitter")
[Facebook](https://facebook.com/sharer.php?u=https://blog.silentsignal.eu/2022/10/18/our-new-scanner-for-text4shell/ "Share on Facebook")

[# apache commons](/tags#apache+commons)
[# burp suite](/tags#burp+suite)
[# java](/tags#java)
[# kotlin](/tags#kotlin)
[# text4shell](/tags#text4shell)
[# tool](/tags#tool)
[# web](/tags#web)