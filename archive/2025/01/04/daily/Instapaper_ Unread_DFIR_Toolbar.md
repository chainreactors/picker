---
title: DFIR_Toolbar
url: https://malwaremaloney.blogspot.com/2025/01/dfirtoolbar.html
source: Instapaper: Unread
date: 2025-01-04
fetch_date: 2025-10-06T20:13:05.186126
---

# DFIR_Toolbar

[![MALoney (It's in the name)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFONMYzjaTaf0PMebgsLM2EgUZ1tLRqAAASIGtbHMoC0Lg8n676906qdGcFww5mXGQRtu3Cg4j3a8uB5oYQMljPSjjopnUdxLDQFxeSdleqk_TvvwAk1rBaBd-UfxK-W5caERP14HExgw/s1600/9-30-2016+6-41-54+AM.png)](https://malwaremaloney.blogspot.com/)

## Pages

* [Home](https://malwaremaloney.blogspot.com/)
* [All Things Symantec](https://malwaremaloney.blogspot.com/p/all-things-symantec.html)
* [All Things OneDrive](https://malwaremaloney.blogspot.com/p/all-things-onedrive.html)
* [Tools](https://malwaremaloney.blogspot.com/p/tools.html)

## Thursday, January 2, 2025

### DFIR\_Toolbar

For this post I thought I'd do something fun. I've been toying around with an idea for a toolbar. The idea came from a [BlueHat IL](https://www.youtube.com/watch?v=Da_9SV9FA34) talk Ulf Frisk gave in 2019. I found it interesting how Ulf could queue up commands for his demo. Ulf was nice enough to give me a copy. The original toolbar was a .hta file. I suited his needs for the talk but I wanted something more configurable and extendable.

I decided to make a toolbar in python that can be pretty much anything you want it to be. The menus are created with a configuration file and commands can be added through plugins. The two plugings included at this time are to launch a browser and copy what ever text you choose. It acts as a true toolbar, taking space at the top of the screen and not allowing applications to go over the top of it or behind.

Here is a list of websites that is included in the default config:
<https://br0k3nlab.com/LoFP/>
<https://www.loldrivers.io/>
<https://gtfobins.github.io/>
<https://lolbas-project.github.io/>
<https://lots-project.com/>
<https://filesec.io/>
<https://malapi.io/>
<https://hijacklibs.net/>
<https://wadcoms.github.io/>
<https://www.loobins.io/>
<https://lolapps-project.github.io/>
<https://www.bootloaders.io/>
<https://cloud.google.com/blog/topics/threat-intelligence/bring-your-own-land-novel-red-teaming-technique/>
<https://lothardware.com.tr/>
<https://wtfbins.wtf/>
<https://lofl-project.github.io/>
<https://persistence-info.github.io/>
<https://github.com/WithSecureLabs/lolcerts>
<https://boostsecurityio.github.io/lotp/>
<https://lolbins-ctidriven.vercel.app/>
<https://lolesxi-project.github.io/LOLESXi/>
<https://lolrmm.io/>
<https://lolad-project.github.io/>
<https://beercow.github.io/LOLCloud-Project.github.io/index.html>
<https://attack.mitre.org/>
<https://d3fend.mitre.org/>
<https://github.com/rabobank-cdc/DeTTECT>
<https://atlas.mitre.org/matrices/ATLAS>
<https://unprotect.it/>
<https://github.com/MBCProject/mbc-markdown>
<https://github.com/palantir/alerting-detection-strategy-framework>
<https://mitre-attack.github.io/attack-navigator/>
<https://center-for-threat-informed-defense.github.io/attack-flow/ui/>
<https://www.vergiliusproject.com/>
<http://terminus.rewolf.pl/terminus/>
<https://any.run/>
<https://analyze.intezer.com/>
<https://iris-h.services/pages/dashboard#/pages/dashboard>
<https://tria.ge/>
<https://www.hybrid-analysis.com/>
<https://www.joesandbox.com/>
<https://app.threat.zone/scan>
<https://valkyrie.comodo.com/>
<https://www.filescan.io/scan>
<https://intelligence.gatewatcher.com/>
<https://labs.inquest.net/dfi>
<https://manalyzer.org/>
<https://threatpoint.checkpoint.com/ThreatPortal/emulation>
<https://www.virustotal.com/gui/home/upload>
<https://yomi.yoroi.company/upload>
<https://virus.exchange/>
<https://virusshare.com/>
<https://www.virussign.com/malware-scan/>
<https://malpedia.caad.fkie.fraunhofer.de/library>
<https://app.malcore.io/>
<https://hash.cymru.com/>
<https://crxaminer.tech/>
<https://lookyloo.circl.lu/capture>
<https://dfir.blog/unfurl/>
<https://urlquery.net/>
<https://urlscan.io/>
<https://sigconverter.io/>
<https://uncoder.io/>
<https://yarahq.github.io/>
<https://yaratoolkit.securitybreak.io/>
<https://start.me/p/7kj9X5/03-incident-response>
<https://start.me/p/ekq7Al/digital-forensics>
<https://start.me/p/BnmK5m/digital-forensics-incdident-respons>
<https://start.me/p/xbwgd0/sans-dfir-2022>
<https://start.me/p/AD57Rr/dfir-jedi>
<https://start.me/p/DPYPMz/the-ultimate-osint-collection>
<https://start.me/p/wMrA5z/cyber-threat-intelligence>
<https://start.me/p/jj0B26/dfir>
<https://start.me/p/OmxDbb/digital-forensics>
<https://start.me/p/q6mw4Q/forensics>
<https://start.me/p/wMmkPz/cyber-security>
<https://msportals.io/>
<https://cmd.ms>
<https://attackrulemap.netlify.app/>
<https://vulnerability.circl.lu>
<https://strontic.github.io/xcyclopedia/intro>
<https://www.kqlsearch.com/>
<https://gchq.github.io/CyberChef/>
<https://explainshell.com/>
<https://dogbolt.org/>
<https://dfiq.org/>
<https://iocparser.com/>
<https://wigle.net/>

For the copy menu, I have included Andrew Rathbun's [DFIRRegex](https://github.com/AndrewRathbun/DFIRRegex)

Menus that you use the most can also be configured to tear away so they are always available. I would really love your thoughts and ideas to make this into something useful for all. Here is a quick demo of what the toolbar can currently do.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaPb3X2F-n2i2E7Lyhw4sQCLbMV8yBmqHo770jOY0eZNfm5s4CPnFpu6y7v-zNFCQnKCpSd8lXIsxLn7d7Tene2ApNVyNEsp6moxZR1kQYGc5wx1Pu44M_weR46M0vHdP3EU3bMNO4sNXJCj9N29TmDCqjWm543_7GUaglSqyQd-EfHemQZnOAjeVOhsE/s1600/34D6JIiHEE.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaPb3X2F-n2i2E7Lyhw4sQCLbMV8yBmqHo770jOY0eZNfm5s4CPnFpu6y7v-zNFCQnKCpSd8lXIsxLn7d7Tene2ApNVyNEsp6moxZR1kQYGc5wx1Pu44M_weR46M0vHdP3EU3bMNO4sNXJCj9N29TmDCqjWm543_7GUaglSqyQd-EfHemQZnOAjeVOhsE/s1600/34D6JIiHEE.gif)

DFIR\_Toolbar can be found [here](https://github.com/Beercow/DFIR_Toolbar).

Posted by

[Brian Maloney](https://www.blogger.com/profile/09611238856421094240 "author profile")

at
[7:12 PM](https://malwaremaloney.blogspot.com/2025/01/dfirtoolbar.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1633622407275871326&postID=4114485628303103038&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=1633622407275871326&postID=4114485628303103038&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=1633622407275871326&postID=4114485628303103038&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=1633622407275871326&postID=4114485628303103038&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=1633622407275871326&postID=4114485628303103038&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=1633622407275871326&postID=4114485628303103038&target=pinterest "Share to Pinterest")

#### No comments:

#### Post a Comment

[Newer Post](https://malwaremaloney.blogspot.com/2025/01/onedrive-evolution-update.html "Newer Post")

[Older Post](https://malwaremaloney.blogspot.com/2025/01/happy-new-year.html "Older Post")
[Home](https://malwaremaloney.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://malwaremaloney.blogspot.com/feeds/4114485628303103038/comments/default)

## Linkedin

[![View Brian Maloney's profile on LinkedIn](https://static.licdn.com/scds/common/u/img/webpromo/btn_liprofile_blue_80x15.png)](https://www.linkedin.com/pub/brian-maloney/4b/275/123)

## Twitter

[Follow @bmmaloney97](https://twitter.com/bmmaloney97)

## Github

[Follow @Beercow](https://github.com/Beercow)

## Blog Archive

* ▼
  [2025](https://malwaremaloney.blogspot.com/2025/)
  (13)
  + ►
    [September](https://malwaremaloney.blogspot.com/2025/09/)
    (1)
  + ►
    [June](https://malwaremaloney.blogspot.com/2025/06/)
    (1)
  + ►
    [May](https://malwaremaloney.blogspot.com/2025/05/)
    (2)
  + ►
    [February](https://malwaremaloney.blogspot.com/2025/02/)
    (2)
  + ▼
    [January](https://malwaremaloney.blogspot.com/2025/01/)
    (7)
    - [OneDrive Offline Mode (Recallish vibes)](https://ma...