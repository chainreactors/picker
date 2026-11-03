---
title: Mutipath TCP: Use and Detection, (Mon, Nov 2nd)
url: https://isc.sans.edu/diary/rss/33482
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-02
fetch_date: 2026-11-03T08:51:42.766670
---

# Mutipath TCP: Use and Detection, (Mon, Nov 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33478)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Mutipath TCP: Use and Detection](/forums/diary/Mutipath%2BTCP%2BUse%2Band%2BDetection/33482/)

**Published**: 2026-11-02. **Last Updated**: 2026-11-02 14:52:05 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Mutipath%2BTCP%2BUse%2Band%2BDetection/33482/#comments)

Last week, an often-ignored TCP option, introduced in 2020, made the news due to a new vulnerability in Linux's implementation (RFC 8684,  CVE-2026-98432)

Instead of looking at the vulnerability, I am using this diary to talk a bit about multipath TCP (MPTCP) and how you may see it used in your network.

### What is MPTCP?

Traditionally, TCP is a connection-oriented protocol. Connections are established between a client and server, and host IP addresses are not expected to change for a specific connection. This restriction to a specific path does not always match modern system architecture. For example, mobile devices may switch from a local WIFI network to a cellular network at any time. Having to re-establish TCP connections may break applications. At the same time, servers often have a hard time "filling" high-bandwidth links using a single TCP connection due to limits on Window Size and the sequence number range [RFC 6182]. MPTCP is supposed to solve these problems by allowing connections to be split and handed over between different IP addresses.

The only widely used implementation I have observed is iOS/iPadOS. In this case, IPv4 connections to Apple (17.0.0.0/8) often utilize MPTCP [Apple]. MPTCP was initially used for Siri, and later for other services like Apple Music.

Two versions of MPTCP are currently defined and used: v0 and v1. At first,

### MPTCP Options

The MPTCP Option (0x1e, 30) is followed by a byte containing 4 bits indicating the subtype and 4 bits indicating the version (0 or 1).

`+----------------+--------------+----------------+----------------+
|   TCP Option   | Option Length|Subtype| Version|     Flags      |
+----------------+--------------+----------------+----------------+
|      30        | variable     |       | 0 or 1 |                |
+----------------+--------------+----------------+----------------+`

**MP\_CAPABLE (subtype 0)**: Indicates MPTCP support. Both sides must include it in the TCP handshake for MPTCP support to be enabled. Each MP\_CAPABLE option also carries an 8-byte key that will later be used to identify and authenticate the different sub-sessions.

**MP\_JOIN (subtype 1):** A second TCP connection may join an initial connection using the MP\_JOIN option. This connection will typically be initiated by the client, but may originate from a different IP address. The RFC does specifically allow the server to initiate the second (or additional) connection. The RFC states: "It is permissible for either host in a connection to initiate the creation of a new subflow, but it is expected that this will normally be the original connection initiator." Ports should be the same, but do not have to be. Of course, this also accounts for common firewall rules. The web server will likely listen only on port 443, and the client's firewall will reject inbound SYN packets.

**DSS (Data Sequence Signal, subtype 2):**Each TCP connection which is part of MPTCP maintains its own sequence numbers, and acts just like any other "normal" TCP connection. To stitch the content of multiple connections together, the DSS option is used. It maps the respective's TCP sequence numbers to the sequence numbers of the combined connection.

**ADD\_ADDR/REMOVE\_ADDR (subtypes 3, 4):** these options are somewhat similar to MP\_JOIN, but instead of actually setting up an additional connection, they advertise (or remove) additional addresses or ports that can be used.

### MPTCP Detection

The best way to detect MPTCP is to look for TCP Option 30. Here are a few ways to do so:

Wireshark/tshark: Wireshark has a "mptcp" display filter keyword. As so often, Wireshark does make it easy.

tcpdump: There is no great way to match TCP options in tcpdump. But MPTCP packets, particularly SYN packets, tend to have large TCP headers, so a quick match on TCP header length can help. For example: 'tcp[12]>0xd0'

Suricata: Use the "tcp.hdr" keyword to inspect TCP options. The tricky part is that the option length isn't always the same. But there should be at least one MP\_CAPABLE message that includes both the sender and receiver key, making this option 20 bytes long. The first three bytes are |1e 14 00| for version 0 or |1e 14 01| for version 1.

Snort: Snort does not have a keyword to inspect TCP options, and as far as I know, no way to filter for multipath TCP. The snort\_decoder "experimental TCP option" alert only triggers on specific option types reserved for experimental use.

Zeek: By default, zeek does not log options, but it does offer the tcp\_option and tcp\_options events that can easily be used to log MPTCP. For example:

`event tcp_option(c: connection, is_orig: bool, opt: count, optlen: count) {
      if ( opt == 30 ) {
            print(fmt("MPTCP between %s and %s", c$id$orig_h, c$id$resp_h));
      }
}`

[Apple] https://support.apple.com/en-us/101905
[RFC8694] https://www.rfc-editor.org/info/rfc8684
[CVE-2026-98432] https://www.openwall.com/lists/oss-security/2026/10/30/1

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [tcp multipath tcp mptcp](/tag.html?tag=tcp multipath tcp mptcp)

[0 comment(s)](/diary/Mutipath%2BTCP%2BUse%2Band%2BDetection/33482/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33478)

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
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)