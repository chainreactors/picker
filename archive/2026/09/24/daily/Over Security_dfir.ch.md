---
title: dfir.ch
url: https://dfir.ch/posts/__tweet/
source: Over Security
date: 2026-09-24
fetch_date: 2026-09-25T06:53:17.208503
---

# dfir.ch

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

#

**Table of Contents**

During a recent incident response engagement, we responded to a single-host infection handed over to us by the SOC. The user downloaded a malicious “Remote Desktop Connection Manager”, a legitimate tool developed by Microsoft, but attackers were now misusing the brand.

After the infection, the attackers had full access to the infected device. The RAT was ChainScript, as Nicely depicted here. [1]

As soon as we took over this case, we began hunting inside the network for traces of lateral movement and/or similar techniques (TTPs, IOCs). Additionally, we found 3 additional infected computers with the same malware, with infections occurring in a short time span.

It turns out the devices belonged to employees on the same team, and one employee pasted the malicious link in a Teams Chat, encouraging the rest of the team to install the software from the same malicious site. So the sentence could not be truer: Trust, but verify.

[1] <https://blackpointcyber.com/blog/chainscript-tracing-a-nodejs-rat-across-the-blockchain/>

√Ç¬© 2026 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).