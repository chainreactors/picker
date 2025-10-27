---
title: Can you please tell me what time it is&#x3f; Adventures with public NTP servers., (Wed, Dec 21st)
url: https://isc.sans.edu/diary/rss/29368
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-22
fetch_date: 2025-10-04T02:15:30.759405
---

# Can you please tell me what time it is&#x3f; Adventures with public NTP servers., (Wed, Dec 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29362)
* [next](/diary/29370)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Can you please tell me what time it is? Adventures with public NTP servers.](/forums/diary/Can%2Byou%2Bplease%2Btell%2Bme%2Bwhat%2Btime%2Bit%2Bis%2BAdventures%2Bwith%2Bpublic%2BNTP%2Bservers/29368/)

**Published**: 2022-12-21. **Last Updated**: 2022-12-21 18:51:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[6 comment(s)](/diary/Can%2Byou%2Bplease%2Btell%2Bme%2Bwhat%2Btime%2Bit%2Bis%2BAdventures%2Bwith%2Bpublic%2BNTP%2Bservers/29368/#comments)

Keeping accurate time has never been easier. In the early days of my computing experience, the accuracy of computer clocks was always questionable. Many of them kept worse time than a $5 wristwatch. Having a cheap quartz oscillator on a motherboard with widely varying temperatures just didn't work all that well.

Along came NTP, and now, almost all operating systems, even many IoT devices, come preconfigured with some reasonable NTP server. In addition, "pool.ntp.org" has made available many publicly available servers to choose from. Currently, "pool.ntp.org" claims to consist of about 4,000 servers provided by volunteers. But how good are they? That is a question that often comes up with volunteer projects like that. Pretty much anybody may join "the pool" and of course, there is no guarantee that the times are accurate. So I did a quick test and wrote a little python script to figure out how good they are.

Spoiler alert: They are actually pretty good.

I used various public NTP servers lists, and lists for pool.ntp.org to find as many servers as possible. Overall, I came up with 1,159 IP addresses for publicly advertised servers. Next, I used the Python NTP library to determine the offset of these servers to my own desktop. I realize that my desktop doesn't have a perfect clock, but it should be pretty good. I use two internal GPS-synchronized NTP servers. But overall, I wouldn't trust anything better than may be 10 ms.

Among the 1,158 datapoints, only 5 showed offsets well above one second.

```

+-----------------+------------+
| IP Address.     | lastoffset |
+-----------------+------------+
| 85.204.137.77   | 2147483647 | - looks like a consumer IP in Denmark
| 128.4.1.1       |    1175530 | - rackety.udel.edu. Probably the oddest one. A well known time server.
| 140.203.204.77  |       6999 | - Irish University
| 148.216.0.30    | 2147483647 | - Mexican Univeristy
| 199.249.223.123 |       1414 | - ntp.quintex.com
+-----------------+------------+
```

Note that 2147483647 is 2^31-1, so these servers were not in sync and returned an empty response. The others need a bit of additional investigation to eliminate a "fluke" or an issue with network connectivity.

Here is a quick frequency distribution:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202022-12-21%20at%201_19_56%20PM.png)

But overall, these public NTP servers are well suited for your average home or small business network. Don't run a 5G network with them as a time source. More sophisticated time servers usually do not just provide an accurate absolute time but also a frequency standard. For not too much money, you can either build your own with a relatively cheap GPS receiver and a small computer like a Raspberry Pi or buy a ready-made simple appliance from companies like Centerclick.com or timemachinescorp.com. These appliances typically use GPS as a source. Even if you use an external NTP server, try making one machine in your network the "time source" and sync your other machines to this one NTP server. This will help public time servers a bit.

NTP also has a nice "OS Fingerprinting" side effect: Many operating systems use specific NTP servers (like time.apple.com for Apple). In some cases, you may even be able to pick up on different IoT vendors based on the DNS lookup for the NTP service they are using. Use an internal DNS server to direct these requests to the IP address of your internal NTP server.

Lately, as a replacement for the old "ntpd" NTP server, some Linux operating systems started using "chrony". Chrony was created by Facebook and promised better accuracy. But resource requirements are similar to ntpd, and both use the same network protocol. There are also options to authenticate NTP requests and responses via a simple shared key, or, as with pretty much any protocol these days, there is an "NTP over TLS" protocol currently supported by Cloudflare's NTP servers.

For a list of NTP servers we are tracking, see https://isc.sans.edu/api/threatlist/ntpservers?json . The list is currently updated once a day.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[6 comment(s)](/diary/Can%2Byou%2Bplease%2Btell%2Bme%2Bwhat%2Btime%2Bit%2Bis%2BAdventures%2Bwith%2Bpublic%2BNTP%2Bservers/29368/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29362)
* [next](/diary/29370)

### Comments

I aim for a pair of machines to be the internal time references that use the same upstream references, so that my client networks have some redundancy if one of them goes down.
One could have one's own atomic clock as a reference, like my dad did with a homebrew unit he built in 1971, but that might just be overkill. (we haven't tried to hook up an NTP interface to it, yet)

#### Andy Konecny

#### Dec 22nd 2022 2 years ago

A few things to add, which makes the use of the pool a lot easier and gives an accurate time on your own systems:

1) Use at least 3 or up to 4 NTP servers as source, your local ntpd is so able to keep accurate time as it will be compared between all the servers.

3) To properly use them in your ntp.conf, please use 'pool' instead of 'server' (see https://community.ntppool.org/t/please-recommend-the-decade-old-pool-command-not-server-in-ntp-conf/2580), example (for details see the link and/or manpage):
tos minsane 2 maxclock 5
pool 0.pool.ntp.org iburst
pool 1.pool.ntp.org iburst
pool 2.pool.ntp.org iburst
pool 3.pool.ntp.org iburst

3) As mention in the article, for larger installation to have at least 3 systems to be the internal time source is very good suggestion. To further improve the quality you could setup NTP peer between them, and if possible also add a local GPS or DCFa clock to one or more of them. On your other internal systems configure this 3 servers (now with 'server' instead of 'pool').

4) The NTP Pool Project does monitor all the servers in the pool for accuracy. If a server does not match up expectation his IP address gets removed from the pool until the score is again above a cenprtain level. The owner even gets notification after a while. To check any NTP Pool server, go to https://www.pool.ntp.org/scores/<ip-address> (replace <ip-address> with the IP address of the server, works also for IPv6).
As I see it, it is kind of nice to have a 3rd party monitoring the quality of the NTP pool servers, but it is not something each user of the pool should do.

#### fab23

#### Dec 22nd 2022 2 years ago

What I do (and have been doing for a decade now) is configure my two DCs to connect to one of the following NTP servers

time-a.nist.gov
time-b.nist.gov
windowstime.com

Then all my internal clients connect to o...