---
title: Its about time: OS Fingerprinting using NTP, (Tue, Jan 3rd)
url: https://isc.sans.edu/diary/rss/29394
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-04
fetch_date: 2025-10-04T03:01:48.406508
---

# Its about time: OS Fingerprinting using NTP, (Tue, Jan 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29390)
* [next](/diary/29400)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Its about time: OS Fingerprinting using NTP](/forums/diary/Its%2Babout%2Btime%2BOS%2BFingerprinting%2Busing%2BNTP/29394/)

**Published**: 2023-01-03. **Last Updated**: 2023-01-03 17:30:07 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Its%2Babout%2Btime%2BOS%2BFingerprinting%2Busing%2BNTP/29394/#comments)

Most current operating systems, including many small systems like IoT devices, use some form of NTP to sync time. NTP is lightweight and reasonably accurate in most use cases to synchronize time across the internet with millisecond accuracy [1]. Some protocols, like PTP, are more accurate but are designed for local networks and may require special hardware on the host [2]. Smaller systems with less stringent accuracy requirements sometimes use SNTP, a variant of NTP.

One of the most obvious and best-documented ways to identify an operating system based on NTP is the hostname of the NTP server. For examples:

* time.apple.com for Apple
* time.windows.com for Microsoft

Others use subdomains of pool.ntp.org. Pool.ntp.org offers free time servers provided by the community. They are currently claiming around 4,000 participating servers. In the past, vendors have, in a few cases, abused this system and caused a DoS against some public NTP servers. To better control traffic, vendors are offered subdomains, and you may see them used. For example:

* android.pool.ntp.org - Android
* amazon.pool.ntp.org - Amazon devices (Kindle, Echo)
* askozia.pool.ntp.org
* centos.pool.ntp.org
* debian.pool.ntp.org
* dragonfly.pool.ntp.org
* freebsd.pool.ntp.org
* irobot.pool.ntp.org
* opnsense.pool.ntp.org
* rhel.pool.ntp.org
* smartos.pool.ntp.org

And many more.

But the opportunities for fingerprinting continue beyond DNS. Different operating systems, or versions of operating systems, use different NTP implementations. There are, for example:

* timed - used by Apple
* chrony - used by newer Linux versions
* ntpd - old "default" and probably most used ntp servers
* Windows Time Service w32time - Windows

I collected the first NTP packet emitted by different operating systems after reboot. I picked the first one as it has yet to be informed by any responses from the timeserver. All systems were reasonably in sync before the reboot. tcpdump does a decent job analyzing NTP if the verbose options are selected, and below you will see the tcpdump output. Hosts participating in pool.ntp.org could also use that to fingerprint clients. Shodan once proposed joining pool.ntp.org to find more IPv6 hosts, as scanning for them is not feasible [3].

Here is a quick summary table outlining some of the differences:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Windows 10 | Linux Chrony | Linux ntpd | iOS | macOS |
| Source Port | 123 | > 1024 | 123 | > 1024 | 123 |
| NTP Version | 3 | 4 | 4 | 3 | 4 |
| Leap Indicator | 192 | 0 | 192 | 0 | 0 |
| Poll Interval | 17 | 6 | 6 | 0 | 0 |
| Root Dispersion | 1 | 0 | 0 | 0 | 0 |
| Reference TS | current time | 0 | 0 | 0 | 0 |
| Transmit TS | current time | random | random? | current time | random? |

I marked some of the "random" transmit timestamps with a question mark as I only found this documented for chrony. But overall, this needs more work to determine how consistent these observations are. I was surprised that iOS and macOS used different NTP versions. Usually, these two operating systems are very similar to each other. I did not include the non-NTP-related fingerprints, like the TTL.

Please let me know if you are observing different values or have a fingerprint for different operating systems. Note that some of these values will change for later NTP requests.

Here is the "raw" data:

### Windows 10

`20:40:15.871314 IP (tos 0x0, ttl 128, id 2668, offset 0, flags [none], proto UDP (17), length 76)
    client.123 > server.123: [udp sum ok] NTPv3, Client, length 48
    Leap indicator: clock unsynchronized (192), Stratum 0 (unspecified), poll 17 (131072s), precision -23
    Root Delay: 0.000000, Root dispersion: 1.000000, Reference-ID: (unspec)
      Reference Timestamp:  3881680738.241951499 (2023-01-02T20:38:58Z)
      Originator Timestamp: 0.000000000
      Receive Timestamp:    0.000000000
      Transmit Timestamp:   3881680815.491954199 (2023-01-02T20:40:15Z)
        Originator - Receive Timestamp:  0.000000000
        Originator - Transmit Timestamp: 3881680815.491954199 (2023-01-02T20:40:15Z)`

### Linux (Chrony, Ubuntu 22.04)

`20:29:37.705016 IP (tos 0x0, ttl 64, id 24799, offset 0, flags [DF], proto UDP (17), length 76)
    client.49127 > server.123: [udp sum ok] NTPv4, Client, length 48
    Leap indicator:  (0), Stratum 0 (unspecified), poll 6 (64s), precision 32
    Root Delay: 0.000000, Root dispersion: 0.000000, Reference-ID: (unspec)
      Reference Timestamp:  0.000000000
      Originator Timestamp: 0.000000000
      Receive Timestamp:    0.000000000
      Transmit Timestamp:   3504697137.365672118 (2011-01-22T14:58:57Z)
        Originator - Receive Timestamp:  0.000000000
        Originator - Transmit Timestamp: 3504697137.365672118 (2011-01-22T14:58:57Z)`

### Linux (ntpd, CentOS 7)

`20:20:41.734648 IP (tos 0xc0, ttl 64, id 33643, offset 0, flags [DF], proto UDP (17), length 76)
    client.123 > server.123: [udp sum ok] NTPv4, Client, length 48
    Leap indicator: clock unsynchronized (192), Stratum 0 (unspecified), poll 6 (64s), precision 32
    Root Delay: 0.000000, Root dispersion: 0.000000, Reference-ID: (unspec)
      Reference Timestamp:  0.000000000
      Originator Timestamp: 0.000000000
      Receive Timestamp:    0.000000000
      Transmit Timestamp:   338734125.654620735 (1910-09-26T12:48:45Z)
        Originator - Receive Timestamp:  0.000000000
        Originator - Transmit Timestamp: 338734125.654620735 (1910-09-26T12:48:45Z)`

### iOS

20:15:34.372666 IP (tos 0x0, ttl 64, id 30369, offset 0, flags [none], proto UDP (17), length 76)
    10.5.1.61.54652 > 10.5.3.31.123: [udp sum ok] NTPv3, Client, length 48
    Leap indicator:  (0), Stratum 0 (unspecified), poll 0 (1s), precision 0
    Root Delay: 0.000000, Root dispersion: 0.000000, Reference-ID: (unspec)
      Reference Timestamp:  0.000000000
      Originator Timestamp: 0.000000000
      Receive Timestamp:    0.000000000
      Transmit Timestamp:   3881697332.315805911 (2023-01-03T01:15:32Z)
        Originator - Receive Timestamp:  0.000000000
        Originator - Transmit Timestamp: 3881697332.315805911 (2023-01-03T01:15:32Z)

### macOS

`20:11:17.373265 IP (tos 0x0, ttl 64, id 30032, offset 0, flags [none], proto UDP (17), length 76)
    10.5.1.108.123 > 10.5.3.31.123: [udp sum ok] NTPv4, Client, length 48
    Leap indicator:  (0), Stratum 0 (unspecified), poll 0 (1s), precision 0
    Root Delay: 0.000000, Root dispersion: 0.000000, Reference-ID: (unspec)
      Reference Timestamp:  0.000000000
      Originator Timestamp: 0.000000000
      Receive Timestamp:    0.000000000
      Transmit Timestamp:   2861060949.483695313 (1990-08-31T03:09:09Z)
        Originator - Receive Timestamp:  0.000000000
        Originator - Transmit Timestamp: 2861060949.483695313 (1990-08-31T03:09:09Z)`

[1] https://ntp.org
[2] https://www.nist.gov/system/files/documents/el/isd/ieee/tutorial-basic.pdf
[3] https://isc.sans.edu/diary/Targeted+IPv6+Scans+Using+pool.ntp.org+./20681

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.e...