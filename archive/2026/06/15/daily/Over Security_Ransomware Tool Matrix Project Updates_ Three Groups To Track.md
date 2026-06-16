---
title: Ransomware Tool Matrix Project Updates: Three Groups To Track
url: https://blog.bushidotoken.net/2026/06/ransomware-tool-matrix-project-updates.html
source: Over Security
date: 2026-06-15
fetch_date: 2026-06-16T07:16:48.256207
---

# Ransomware Tool Matrix Project Updates: Three Groups To Track

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### Ransomware Tool Matrix Project Updates: Three Groups To Track

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[June 15, 2026](https://blog.bushidotoken.net/2026/06/ransomware-tool-matrix-project-updates.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTcsnDaxB_Q3pgDjrDIepU6TrBakrcGZKsPAWp04R05xc7JdO_kkOjMz96N2mePI7GmVHgSVunG-yMHoUcjJ-4BlLpMZ5X6fxESLz-bBGiV6l2TCd4_zbhVdftgLZWSDahLaBKIDp7XTssmg6lS9y3kyTtKJkAeS9Y73Gx4dqmdBOCXs0zc7bUTbQo03ja/w640-h358/IMG_4946.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTcsnDaxB_Q3pgDjrDIepU6TrBakrcGZKsPAWp04R05xc7JdO_kkOjMz96N2mePI7GmVHgSVunG-yMHoUcjJ-4BlLpMZ5X6fxESLz-bBGiV6l2TCd4_zbhVdftgLZWSDahLaBKIDp7XTssmg6lS9y3kyTtKJkAeS9Y73Gx4dqmdBOCXs0zc7bUTbQo03ja/s1376/IMG_4946.png)

Introduction

This blog is a focused update on the latest updates to the [Ransomware Tool Matrix (RTM)](https://github.com/BushidoUK/Ransomware-Tool-Matrix) and the [Ransomware Vulnerability Matrix (RVM)](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix) covering three groups that I have published profiles for to help defenders home in on the threats most relevant to them: TheGentlemen, DragonForce, and WarLock.

Rather than write another broad ecosystem summary, the goal of this post is to introduce these profiles, briefly explain why each group matters right now, and give readers direct links to them so defenders can pivot straight into hunting, detection engineering, and patch prioritisation.

For anyone new to the projects, please read the descriptions on GitHub or feel free to watch my talk explaining the project at [BSides London](https://www.youtube.com/watch?v=hyoOhAoaX1g).

Why these three groups?

Each of the three groups added in this update represents a different slice of the current ransomware ecosystem:

### TheGentlemen

TheGentlemen is a newer operation that has matured quickly, with a large and varied toolkit that reflects how cross-pollinated the affiliate ecosystem has become. The recent internal chat leak gave researchers a rare look into their tradecraft, and the profiles capture both the tooling and the exploited CVEs that have been observed across multiple intrusions. TheGentlemen’s RTM profile is [here](https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/GroupProfiles/TheGentlemen.md) and RVM profile is [here](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix/blob/main/GroupProfiles/TheGentlemen.md).

## DragonForce

DragonForce has continued to escalate throughout 2025 and into 2026, branching into MSP-focused attacks and standing up its own "cartel" model that other affiliates can plug into. Its exploitation of edge devices (Ivanti, Fortinet, SonicWall) and SimpleHelp RMM make it a high-priority threat for any organisation using such systems. DragonForce’s RTM profile is [here](https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/GroupProfiles/DragonForce.md) and RVM profile is [here](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix/blob/main/GroupProfiles/DragonForce.md).

## WarLock

WarLock jumped onto everyone's radar after the ToolShell SharePoint zero-day exploitation campaign, and has since been linked to a string of edge-application exploits including SmarterMail, SolarWinds Web Help Desk, and Gladinet CentreStack. It is a strong example of a likely China-based operator that lives on zero-day exploitation of internet-facing software. WarLock’s RTM profile is [here](https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/GroupProfiles/Warlock.md) and RVM profile is [here](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix/blob/main/GroupProfiles/WarLock.md).

Observations and Trends

A few themes are worth flagging across all three profiles:

* BYOVD is now standard, not novel. All three groups have been observed bringing vulnerable drivers to disable or blind EDR. TheGentlemen with ThrottleStop driver, DragonForce with the TrueSight and Hangzhou Shunwang drivers, and WarLock with Antiy, NsecSoft, Rising, and VMTools drivers. If your detection stack is not yet hunting on or blocking suspicious driver loads and known-bad driver hashes, that is a high-priority gap to close.
* Network edge devices and other internet-facing systems remain the front door to victim networks for these groups. Fortinet, Ivanti, SonicWall, SimpleHelp, Microsoft SharePoint, SmarterMail, SolarWinds Web Help Desk, and Gladinet CentreStack all appear across these three profiles. Patch prioritisation that focuses on internet-exposed appliances and admin tooling continues to give defenders a valuable return on effort.
* Legitimate tooling continues to blur the line. Velociraptor, Cloudflared, VSCode Tunnels, AnyDesk, MeshCentral, FreeRDP, PuTTY, OpenSSH, and a long list of legitimate cloud services are all being repurposed for ransomware operations. Defender should use these lists to begin baselining what should exist in their environment and start alerting on the rest.

Conclusion

My recommendation for defenders remains the same as in previous updates: take the tools and CVEs from the RTM and RVM profiles and start threat hunting for their presence, writing detection rules to alert on certain behaviours, and blocking what is not expected or permitted in your environment. These three new profiles should make that easier to scope by group when you need to brief leadership, prioritise a hunt, or map your exposure to a specific campaign.

Here's a few sites that can help with turning the threat intel in these new profiles into detections:

- <https://rulehound.com/rules>

- <https://detection.fyi>

- <https://www.snapattack.com/community>

As always, feedback and pull requests are very welcome on both repos. Thanks to everyone who has contributed reports, corrections, and ideas. These projects only stay useful because the community keeps feeding them one way or another.

[DragonForce](https://blog.bushidotoken.net/search/label/DragonForce)
[Fortinet](https://blog.bushidotoken.net/search/label/Fortinet)
[Ivanti](https://blog.bushidotoken.net/search/label/Ivanti)
[ransomware](https://blog.bushidotoken.net/search/label/ransomware)
[Ransomware Tool Matrix](https://blog.bushidotoken.net/search/label/Ransomware%20Tool%20Matrix)
[SharePoint](https://blog.bushidotoken.net/search/label/SharePoint)
[SimpleHelp](https://blog.bushidotoken.net/search/label/SimpleHelp)
[SonicWall](https://blog.bushidotoken.net/search/label/SonicWall)
[TheGentlemen](https://blog.bushidotoken.net/search/label/TheGentlemen)
[WarLock](https://blog.bushidotoken.net/search/label/WarLock)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### [Ransomware Tool Matrix Project Updates: May 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

-
[May 05, 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_BpTZksj9aZ67Y0MoiVTbyhuF2ZNK6mjoCeIlkF5MIjc7DlouoqPLYd-7XXsHgxT6Vytvvo-gY5b8JO3Ujab_8XLnSo1LbYrBUW78GrP2U8wx3ZT-B2ZwMGLO2aVCovVuIX3qZWYIN3X-GCw470E7tr2aiI0CPIgi9bkXbvDldhDL1hNZEc48rVTPyvxY/s320/OIG2.jpg)](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

Introduction This blog is a summary and analysis of recent additions to the Ransomware Tool Matrix (RTM) as well as the Ransomware Vulnerability Matrix (RVM) .  Feedback from the infosec community about these projects has been overwhelmingly positive and many researchers have contacted me to tell me how helpful they have found these to be.  It makes me happy to hear how doing something in my spare time can help stop ransomware attacks and cybercriminals from exploiting our society’s systems. And it is for that reason, I shall continue to m...