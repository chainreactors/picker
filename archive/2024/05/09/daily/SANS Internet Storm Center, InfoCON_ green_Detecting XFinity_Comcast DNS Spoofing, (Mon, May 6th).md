---
title: Detecting XFinity/Comcast DNS Spoofing, (Mon, May 6th)
url: https://isc.sans.edu/diary/rss/30898
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-09
fetch_date: 2025-10-06T17:19:30.145510
---

# Detecting XFinity/Comcast DNS Spoofing, (Mon, May 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30894)
* [next](/diary/30904)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Detecting XFinity/Comcast DNS Spoofing](/forums/diary/Detecting%2BXFinityComcast%2BDNS%2BSpoofing/30898/)

**Published**: 2024-05-06. **Last Updated**: 2024-05-08 00:15:59 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Detecting%2BXFinityComcast%2BDNS%2BSpoofing/30898/#comments)

ISPs have a history of intercepting DNS. Often, DNS interception is done as part of a "value add" feature to block access to known malicious websites. Sometimes, users are directed to advertisements if they attempt to access a site that doesn't exist. There are two common techniques how DNS spoofing/interception is done:

1. The ISP provides a recommended DNS server. This DNS server will filter requests to known malicious sites.
2. The ISP intercepts all DNS requests, not just requests directed at the ISPs DNS server.

The first method is what I would consider a "recommended" or "best practice" method. The customer can use the ISP's DNS server, but traffic is left untouched if a customer selects a different recursive resolver. The problem with this approach is that malware sometimes alters the user's DNS settings.

Comcast, as part of its "Business Class" offer, provides a tool called "Security Edge". It is typically included for free as part of the service. Security Edge is supposed to interface with the customer's modem but can only do so for specific configurations. Part of the service is provided by DNS interception. Even if "Security Edge" is disabled in the customer's dashboard, DNS interception may still be active.

One issue with any filtering based on blocklists is false positives. In some cases, what constitutes a "malicious" hostname may not even be well defined. I could not find a definition on Comcast's website. But Bleeping Computer (www.bleepingcomputer.com) recently ended up on Comcast's "naughty list". I know all to well that it is easy for a website that covers security topics to end up on these lists. The Internet Storm Center website has been on lists like this before. Usually, sloppy signature-based checks will flag a site as malicious. An article may discuss a specific attack and quote strings triggering these signatures.

Comcast offers recursive resolvers to it's customers: 75.75.75.75, 75.75.76.76, 2001:558:feed:1 and 2001:558:feed:2. There are advantages to using your ISP's DNS servers. They are often faster as they are physically closer to your network, and you profit from responses cached by other users. My internal resolver is configured as a forwarding resolver, spreading queries among different well performing resolvers like Quad9, Cloudflare and Google.

So what happened to bleepingcomputer.com? When I wasn't able to resolve bleepingcomputer.com, I checked my DNS logs, and this entry stuck out:

> `broken trust chain resolving 'bleepingcomputer.com/A/IN': 8.8.8.8#53`

My resolver verifies DNSSEC. Suddenly, I could not verify DNSSEC, which is a good indication that either DNSSEC was misconfigured or someone was modifying DNS responses. Note that the response appeared to come from Google's name server (8.8.8.8).

My first step in debugging this problem was dnsviz.net, a website operated by Sandia National Laboratory. The site does a good job of visualizing DNSSEC and identifying configuration issues. Bleepingcomputer.com looked fine. Bleepingcomputer didn't use DNSSEC. So why the error? There was another error in my resolver's logs that shed some light on the issue:

> `no valid RRSIG resolving 'bleepingcomputer.com/DS/IN': 8.8.8.8#53`

DNSSEC has to establish somehow if a particular site supports DNSSEC or not. The parent zone should offer an "NSEC3" record to identify zones that are not signed or not signed. DS records, also offered by the parent zone, verify the keys you may receive for a zone. If DNS is intercepted, the requests for these records may fail, indicating that something odd is happening.

So, someone was "playing" with DNS. And it affected various DNS servers I tried, not just Comcast or Google. Using "dig" to query the name servers directly, and skipping DNSSEC, I received a response:

> `8.8.8.8.53 > 10.64.10.10.4376: 35148 2/0/1 www.bleepingcomputer.com. A 192.73.243.24, www.bleepingcomputer.com. A 192.73.243.36 (85)`

Usually, www.bleepingcomputer.com resolved to:

> % dig +short www.bleepingcomputer.com
> 104.20.185.56
> 172.67.2.229
> 104.20.184.56

It took a bit of convincing, but I was able to pull up the web page at the wrong IP address:

![screen shot of Comcast block page.](https://isc.sans.edu/diaryimages/images/Screenshot%202024-05-06%20at%208_18_59%E2%80%AFPM.png)

The problem with these warning pages is that you usually never see them. Even if you resolve the IP address, TLS will break the connection, and many sites employ strict transport security. As part of my Comcast business account, I can "brand" the page, but by default, it is hard to tell that this page was delivered by Comcast.

But how do we know if someone is interfering with DNS traffic? A simple check I am employing is to look for the DNS timing and compare the TTL values for different name servers.

(1) Check timing

Send the same query to multiple public recursive DNS servers. For example:

> `% dig www.bleepingcomputer.com @75.75.75.75`
>
> `; <<>> DiG 9.10.6 <<>> www.bleepingcomputer.com @75.75.75.75
> ;; global options: +cmd
> ;; Got answer:
> ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8432
> ;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1`
>
> `;; OPT PSEUDOSECTION:
> ; EDNS: version: 0, flags:; udp: 512
> ;; QUESTION SECTION:
> ;www.bleepingcomputer.com.    IN    A`
>
> `;; ANSWER SECTION:
> www.bleepingcomputer.com. 89    IN    A    104.20.185.56
> www.bleepingcomputer.com. 89    IN    A    104.20.184.56
> www.bleepingcomputer.com. 89    IN    A    172.67.2.229`
>
> `;; Query time: 59 msec
> ;; SERVER: 75.75.75.75#53(75.75.75.75)
> ;; WHEN: Tue May 07 20:00:05 EDT 2024
> ;; MSG SIZE  rcvd: 101`

Dig includes the "Query time" in its output. In this case, it was 59 msec. We expect a speedy time like this for Comcast's DNS server while connected to Comcast's network. But let's compare this to other servers:

8.8.8.8: 59 msec
1.1.1.1: 59 msec
9.9.9.9: 64 msec
11.11.11.11: 68 msec
113.113.113.113: 69 msec

The results are very consistent. In particular, the last one is interesting. This server is located in China.

(2) check TTLs

A recursive resolver will add a response it receives from an authoritative DNS server to its cache. The TTL for records bulled from the cache will decrease with the time the response sits in the resolver's cache. If all responses come from the same resolver, the TTL should decrement consistently. This test is a bit less telling. Often, several servers are used, and with anycast, it is not always easy to tell which server the response comes from. These servers do not always have a consistent cache.

### Final Words

DNS interception, even if well-meaning, does undermine some of the basic "internet trust issues". Even if it is used to block users from malicious sites, it needs to be properly declared to the user, and switches to turn it off will have to function. This could be a particular problem if queries to other DNS filtering services are intercepted. I have yet to test this for Comcast and, for example, OpenDNS.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter...