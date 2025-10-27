---
title: The Russian APT Tool Matrix
url: https://blog.bushidotoken.net/2024/09/the-russian-apt-tool-matrix.html
source: Over Security - Cybersecurity news aggregator
date: 2024-09-23
fetch_date: 2025-10-06T18:24:56.811998
---

# The Russian APT Tool Matrix

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### The Russian APT Tool Matrix

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[September 22, 2024](https://blog.bushidotoken.net/2024/09/the-russian-apt-tool-matrix.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj5LVZE8VqBmLY4biNqQRwXB0N7xT-9RSjpqavj2_78D11pwiyS0iL_e4EtDADS3tg_02yc0QGU5vfG-pm9blLmfe7sbvAzSIBYKUpiCfg51DPqIey9joDktv9VqXO6dAgrlsM6s6u3icm6UIEWJP0keJkIsmbgiQTYhiWpT2vOtL7o1ev1RtggzZR9A99/w400-h400/OIG4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj5LVZE8VqBmLY4biNqQRwXB0N7xT-9RSjpqavj2_78D11pwiyS0iL_e4EtDADS3tg_02yc0QGU5vfG-pm9blLmfe7sbvAzSIBYKUpiCfg51DPqIey9joDktv9VqXO6dAgrlsM6s6u3icm6UIEWJP0keJkIsmbgiQTYhiWpT2vOtL7o1ev1RtggzZR9A99/s1024/OIG4.jpg)

### Introduction

Based on feedback I have received from fellow CTI
researchers, incident responders, and managed detection and response teams
around my [Ransomware
Tool Matrix](https://blog.bushidotoken.net/2024/08/the-ransomware-tool-matrix.html) project, I decided to make another Tool Matrix focused on one hostile
state in particular: Russia.

Again, as defenders, we should exploit the fact the tools
used by these Russian APT groups are often reused and through proactive defensive
work, we can frustrate and even eliminate the ability of certain adversaries to
launch intrusions.

Using the Russian APT Tool Matrix comes with its own
challenges. While it is undoubtedly useful to have a list of tools commonly
used by Russian APTs to hunt, detect, and block, there are some risks, as noted
in the repository.

The new repository also contains multiple types of Russian threat
groups, this includes adversaries part of the GRU, SVR, and FSB. The alias of
each Russian threat group has been chosen by what the author of this repo
believes it is most well-known as.

* Russian GRU: Main Intelligence Directorate (Russian
  Military)
* Russian SVR: Foreign Intelligence Service of the Russian
  Federation
* Russian FSB: Federal Security Service of the Russian
  Federation

Also, if you’re short on time, you can now listen to this blog as a podcast via [YouTube](https://www.youtube.com/watch?v=SU3LMzgym9M), which I generated using Google’s NotebookLM.

### Key Findings

Following the collection, extraction, and labelling of all
the tools identified as being used by [Russian
threat groups](https://github.com/BushidoUK/Russian-APT-Tool-Matrix/tree/main/GroupProfiles), some interesting findings were uncovered. These are as
follows:

The adversary that used the most scanners was EMBER BEAR, which
is affiliated with the GRU. Other GRU threat groups, such as FANCY BEAR and
Sandworm, were found often relying on a wide variety offensive security tools
(OSTs) to support their intrusions.

Another interesting finding was that Russian threat groups
using lots of different tools and platforms for exfiltration was Turla and COZY
BEAR. Overall, the Russian threat group with the highest total number different
tools used was COZY BEAR, which is affiliated with the SVR.

From extracting all the [various
tools](https://github.com/BushidoUK/Russian-APT-Tool-Matrix/blob/main/Tools/AllToolsRU.csv) from several years’ worth of threat reports, some general
observations about how Russian threat groups used public-available resources to
support their campaigns. The thing that stood out most was a large reliance on OSTs
across multiple Russian threat groups. Up to 27 different OSTs were recorded. The
tools mutually used by the highest number of Russian threat groups are as
follows:

* **Mimikatz** is used by COZY BEAR, FANCY BEAR, BERSERK BEAR,
  Gamaredon, and Turla.
* **Impacket** is used by COZY BEAR, FANCY BEAR, EMBER BEAR,
  Sandworm, and BERSERK BEAR.
* **PsExec** is used by COZY
  BEAR, EMBER BEAR, BERSERK BEAR, Gamaredon, and Turla.
* **Metasploit** is used by FANCY BEAR, EMBER BEAR, Sandworm, and Turla.
* **ReGeorg** is used by COZY BEAR, FANCY BEAR, EMBER BEAR, and Sandworm.

If a combination of the above tools are observed during an
intrusion, then that intrusion could have been conducted by a Russian state-sponsored
threat group. However, using the Ransomware Tool Matrix, we know that four out
of the top five tools used by Russian threat groups are also very commonly used
by ransomware groups.

The network tunnelling utility [ReGeorg](https://github.com/sensepost/reGeorg) is potentially notable for
its use by multiple Russian threat groups. ReGeorg is not a well-known tool and
it is often used in conjunction with a web shell to turn a compromised server
into a proxy. From my collection and extraction of tools from threat reports related
to the Ransomware Tool Matrix, I can confirm ReGeorg is used by virtually none
of the large ransomware gangs. Therefore, if this specific tool is found during
an intrusion, alongside the other top five tools mentioned above, there is
arguably an increased chance it was conducted by a Russian threat group.

### Russian APT Tool Matrix Project

You can find The Russian APT Tool Matrix in my GitHub
repository below:

[APT28](https://blog.bushidotoken.net/search/label/APT28)
[APT29](https://blog.bushidotoken.net/search/label/APT29)
[APT44](https://blog.bushidotoken.net/search/label/APT44)
[CozyBear](https://blog.bushidotoken.net/search/label/CozyBear)
[FancyBear](https://blog.bushidotoken.net/search/label/FancyBear)
[Russia](https://blog.bushidotoken.net/search/label/Russia)
[Russian FSB](https://blog.bushidotoken.net/search/label/Russian%20FSB)
[Russian GRU](https://blog.bushidotoken.net/search/label/Russian%20GRU)
[Russian SVR](https://blog.bushidotoken.net/search/label/Russian%20SVR)
[Sandworm](https://blog.bushidotoken.net/search/label/Sandworm)
[Tool Matrix](https://blog.bushidotoken.net/search/label/Tool%20Matrix)
[Turla](https://blog.bushidotoken.net/search/label/Turla)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### [Raspberry Robin: A global USB malware campaign providing access to ransomware operators](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html)

-
[May 02, 2023](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd_7gSbs89Orm2BQ22KJ76nRHlAoIyaj6Rph2DA0sQ2IaBIrPTmDZdn_9uHremHSL1vxAG9t1m-fg_Yqgova-eqexDrglh-rIRmXxXrvvmb0_h6dSJlqBsTRSCIhvTEweAprIcS8JYsBWdRni5xwMAG5SysOEnDAvzJwdRHZJVh0Jp2obgs43Ui4w7Yg/s16000/RRobin_April2023.png)](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html)

Logo credit: RedCanary Ever since it first appeared in late 2021, the Raspberry Robin malware campaign has been propagating globally. A number of threat intelligence reports by vendors such as RedCanary (who named it) and Microsoft (who track it as DEV-0856/Storm-0856) have covered the malware campaign in great detail.  In fact, the list of blogs I do recommend to read to catch up on this threat are as follows: https://redcanary.com/blog/raspberry-robin https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity https://blog.sekoia.io/raspberry-robins-botnet-second-life/ https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/ https://research.checkpoint.com/2023/raspberry-robin-anti-evasion-how-to-exploit-analysis/ https://securityintelligence.com/posts/raspberry-robin-worm-dridex-malware/ https://blogs.cisco.com/security/raspberry-robin-highly-evasive-worm-sprea...

[Read more](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html "Raspberry Robin: A global USB malware campaign providing access to ransomware operators")

### [BlackBasta Leaks: Lessons from the Ascension Health attack](https://blog.bushidotoken.net/2025/02/blackbasta-leaks-lessons-from-a...