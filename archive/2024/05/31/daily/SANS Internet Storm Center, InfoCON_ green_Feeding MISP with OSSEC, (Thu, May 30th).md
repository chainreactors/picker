---
title: Feeding MISP with OSSEC, (Thu, May 30th)
url: https://isc.sans.edu/diary/rss/30968
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-31
fetch_date: 2025-10-06T16:52:20.234529
---

# Feeding MISP with OSSEC, (Thu, May 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30962)
* [next](/diary/30972)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Feeding MISP with OSSEC](/forums/diary/Feeding%2BMISP%2Bwith%2BOSSEC/30968/)

**Published**: 2024-05-30. **Last Updated**: 2024-05-30 06:56:44 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Feeding%2BMISP%2Bwith%2BOSSEC/30968/#comments)

I'm a big fan of OSSEC[[1](https://ossec.net)] for years. OSSEC ("Open Source Security Event Correlator") is a comprehensive, open-source host-based intrusion detection system (HIDS). It is designed to monitor and analyze system logs, detect suspicious activities, and provide real-time alerts for security incidents. OSSEC can perform log analysis, file integrity monitoring, rootkit detection, and active response to mitigate threats. It supports various platforms including Linux, Windows, and macOS, and can be integrated with various security tools and SIEM solutions. I already wrote some diaries about it in the past[[2](https://isc.sans.edu/search.html?q=ossec&token=&Search=Search)]. I'm running my instance on all my servers, I made some contributions to the project.

One of the features I like most is "Active-Response". It allows us to automatically take predefined actions in response to detected security events or threats. When a specific rule is triggered, OSSEC can execute scripts or commands to mitigate the threat, such as blocking an IP address, disabling a user account, or restarting a service. This feature enhances the system's security by providing real-time, automated reactions to potential intrusions or malicious activities, reducing the window of opportunity for attackers to exploit vulnerabilities.

Being a big fan of MISP[3], making them talk together to improve our detection capabilities is a great improvement. Most of my OSSEC agents are installed on many servers facing the Internet and get scanned/visited/flooded by thousands of malicious requests. The default Active-Response enabled in OSSEC is to temporarily block offending addresses to slow down attackers (for example, brute-force attacks). These addresses are also interesting for multiple reasons:

1. If one host is attacked, the same IP address could be blocked on all servers

2. The IP address could be shared with peers (it's an interesting IOC - Indicator of Compromise))

3. We can track if the same IP address is coming back regularly

I wrote an Active-Response script that, if conditions are met, will submit offending IP addresses to a MISP instance. How does it work?

First, you need to configure a new Active-Response config:

```

<active-response>
  <disabled>no</disabled>
  <command>ossec2misp</command>
  <location>server</location>
  <rules_id>100213,100201,31509</rules_id>
</active-response>
```

The most important parameter is the list of rules that will trigger the active response. By example, my rule 31509 detects Wordpress login brute-force attacks:

```

<!-- WordPress wp-login.php brute force -->
  <rule id="31509" level="3">
    <if_sid>31108</if_sid>
    <url>wp-login.php|/administrator</url>
    <regex>] "POST \S+wp-login.php| "POST /administrator</regex>
    <description>CMS (WordPress or Joomla) login attempt.</description>
</rule>
```

When the alert triggers, the OSSEC server will execute the command called "ossec2misp":

```

<command>
  <name>ossec2misp</name>
  <executable>ossec2misp.py</executable>
  <expect>srcip</expect>
  <timeout_allowed>no</timeout_allowed>
</command>
```

The command will call my Python script located in your Active-Response scripts repository (usually $OSSEC\_HOME/active-response/bin/). The script can be configured, most options are self-explaining:

```

misp_url          = "https://misp.domain.tld"
misp_key          = "<redacted>"
misp_verifycert   = True
misp_info         = "OSSEC ActiveResponse"      # Event title
misp_last         = "30d"                       # Max period to search for IP address
misp_new_event    = False                       # Force the creation of a new event for every report
misp_distribution = 0                           # The distribution setting used for the newly created event, if relevant. [0-3]
misp_analysis     = 1                           # The analysis level of the newly created event, if applicable. [0-2]
misp_threat       = 3                           # The threat level ID of the newly created event, if applicable. [1-4]
misp_tags         = [ "source:OSSEC" ]          # Tags for the newly created event, if applicable
misp_publish      = True                        # Automatically puslish the event
syslog_server     = "192.168.1.1"               # If defined, enable syslog logging
redis_server      = "redis"                     # Redis server hostname/ip
redis_port        = 6379                        # Redis server port
redis_db          = 0                           # Redis server db
```

The Redis server is used to prevent the MISP server from being flooded by API requests. Once an IP has been detected, it is stored in Redis for 1h.

When an offending IP address is already present in MISP, the script will add a "sighting" to it. The purpose of "sighting" is to provide feedback on the usage and relevance of the IP address within the platform. This helps in verifying the prevalence and impact of the IOC, enhances collaborative threat intelligence by validating data, and assists in prioritizing IP addresses based on their sightings frequency and relevance.

Here is an example of an OSSEC event:

![](https://isc.sans.edu/diaryimages/images/isc-20240530-1.png)

My script is available in my Github repo[[4](https://github.com/xme/ossec/blob/main/ossec2misp.py)]. Comments, improvements or ideas are welcome!

[1] [https://ossec.net/](https://ossec.net)
[2] <https://isc.sans.edu/search.html?q=ossec&token=&Search=Search>
[3] <https://www.misp-project.org>
[4] <https://github.com/xme/ossec/blob/main/ossec2misp.py>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Feeder](/tag.html?tag=Feeder) [IOC](/tag.html?tag=IOC) [MISP](/tag.html?tag=MISP) [OSSEC](/tag.html?tag=OSSEC) [Python](/tag.html?tag=Python) [Threat](/tag.html?tag=Threat) [Intelligence](/tag.html?tag=Intelligence)

[0 comment(s)](/diary/Feeding%2BMISP%2Bwith%2BOSSEC/30968/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/30962)
* [next](/diary/30972)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sen...