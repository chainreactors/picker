---
title: “The” IP Address
url: https://textslashplain.com/2026/09/24/the-ip-address/
source: text/plain
date: 2026-09-24
fetch_date: 2026-09-25T06:52:08.663200
---

# “The” IP Address

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# “The” IP Address

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-09-242026-09-24](https://textslashplain.com/2026/09/24/the-ip-address/)Posted in[tech](https://textslashplain.com/category/tech/)Tags:[dns](https://textslashplain.com/tag/dns/), [networking](https://textslashplain.com/tag/networking/)

As elaborated in [a prior post](https://textslashplain.com/2023/09/11/the-challenge-of-ip-reputation/), sites and services often try to use an IP address as an input into **protection** (e.g. blocking a spammer) or **customization** (providing local weather info) algorithms.

Commonly, software would like to know “*What is this device’s IP address?*” Unfortunately, this is not a trivial question to answer, because it makes several incorrect assumptions:

1. That the client device only has *one* IP address
2. That network packets received by a service from the client device will have that IP address as the `remote_addr`.

Both of these assumptions are incorrect, in several ways.

# Not One Address

Devices may have multiple network adapters, each with their own address. Those adapters may be “physical” (e.g. a network card) or “virtual” (e.g. a VPN adapter). Each network adapter may itself have multiple addresses, which is almost universally true for modern devices that support both IPv4 and IPv6.

# Client Perspective != Remote Perspective

It is commonly the case that client requests are sent from networks that change the source address as the traffic flows (e.g. “Network Address Translation”). For example, many home users connect to the Internet from behind a WiFi router linked to their Internet Service Provider over a fiberoptic connection. In such cases, the web server will commonly see the IP address of the router, not the “private” address of the user’s PC.

Similarly, users may use VPNs, [Tor](https://torproject.org), proxies, [iCloud Private Relay](https://support.apple.com/en-us/102602), [Oblivious HTTP](https://www.rfc-editor.org/info/rfc9458/), or other networking features that result in the server having a different perspective of the client’s network address.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-8.png?resize=741%2C567&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-8.png?ssl=1)

In cases where a scenario requires a client to understand the “Internet’s perspective” of the client’s IP address, technologies like [STUN](https://en.wikipedia.org/wiki/STUN) may be used.

## IPv6 Background

The vast majority of relevant internet traffic reaches its destination by way of Internet Protocol addresses. These numeric addresses exist in one of two **families:** IPv4 addresses are 32-bits in length and can reference around 3.7 billion routable endpoints, while IPv6 addresses are 128 bits long and can reference approximately 42 undecillion endpoints.

To accommodate the public internet which uses both IPv4 and IPv6 addresses, most clients and servers support both IPv4 and IPv6 simultaneously (“**Dual Stack**”), such that a given client device will have multiple addresses, at least one from each family. Web servers that offer support for both families will register both addresses in DNS. An [A query](https://dns.google/query?name=example.com&rr_type=A&ecs=) for the fully-qualified domain name will return the IPv4 address, while an [AAAA query](https://dns.google/query?name=example.com&rr_type=AAAA&ecs=) will return the IPv6 address.

For example, sending both `A` and `AAAA` queries to DNS for `example.com` returns `104.18.27.120` and `2606:4700::6812:1a78` respectively.

Address family choice applies to the *connection*: when connecting to an IPv4 server address, the client uses its IPv4 client address, and when an IPv6 server is connected, the connection originates from a client’s IPv6 address.

There is usually no direct relationship between a client’s IPv4 and IPv6 addresses.

A given client may be configured to support both address families or only one. It may be designed to prefer a given family, or “[race](https://en.wikipedia.org/wiki/Happy_Eyeballs)” parallel connections to both families to prefer whichever works more quickly. On Windows, the decision about whether IPv6 or IPv4 is used varies based on:

1. Device Configuration (RFC 6724, prefix table, adapters)
2. DNS results (RFC 3596, A, AAAA records)
3. Happy Eyeballs (RFC 8305, which is timing and blocked connection fallback)
4. Network QOS fallback (latency, packet loss, etc)

For example, when navigating a browser to `Bing.com`, a Microsoft service that supports both IPv4 and IPv6:

* The browser DNS query returns records for both AAAA (IPv6) and A (IPv4) queries
* Windows TCP/IP “prefers” IPv6 and that’s what Windows will try first
* The TCP/IP stack starts IPv6 connection attempt
* The TCP/IP stack waits ~300 ms, and will then try establishing an IPv4 connection
* Whichever connection succeeds first wins, the other is abandoned

[Today](https://www.google.com/intl/en/ipv6/statistics.html), approximately half of Internet traffic occurs over IPv6:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-6.png?resize=658%2C316&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-6.png?ssl=1)

##### Understanding Address Family Preference

The command netsh interface ipv6 show prefixpolicies [displays the **IPv6 Prefix Policy Table**](https://kb.firedaemon.com/support/solutions/articles/4000160803-prioritising-ipv4-over-ipv6-on-windows-10-and-11), which determines the order in which a computer selects IP addresses when multiple options are available (e.g., deciding whether to prefer IPv6 over IPv4). The table is a set of rules to rank destination and source addresses.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-9.png?resize=750%2C293&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-9.png?ssl=1)

**By default**, Windows prefers IPv6 (::/0 at precedence 40) over IPv4-mapped (::ffff:0:0/96 at precedence 35).

* **Precedence:** The “weight” or priority. A higher number means a higher priority. For example, `::1/128` (Loopback) has a precedence of 50.
* **Label:** A value used to match source addresses with destination addresses. If a source and destination have the same label, they are preferred for each other.
* **Prefix:** The specific IP range the rule applies to.
  + `::1/128`: The local machine (Loopback).
  + `::/0`: Default IPv6 unicast.
  + `::ffff:0:0/96`: This represents **IPv4** addresses mapped into IPv6.

To change the priority of IPv4 so that it is preferred over IPv6, [adjust the precedence](https://oneuptime.com/blog/post/2026-03-20-configure-ipv6-prefix-policy-windows/view) of the **IPv4-mapped IPv6 prefix** (`::ffff:0:0/96`).

## Preventing Tracking

When looking at your IPv6 address in Windows, you might find something surprising: there are several described as `Temporary IPv6 Address`, and [they change](https://superuser.com/questions/703915/why-does-my-windows-have-hundreds-of-temporary-ipv6-addresses).

The **Temporary IPv6 Address** feature in Windows (technically known as **Privacy Extensions for SLAAC**) is a security mechanism designed to prevent third parties from tracking your device’s activity across the internet as you move between networks or over long periods of time.

**1. The Problem: The “EUI-64” Privacy Leak**

In the early days of IPv6, addresses were typically generated using **Stateless Address Autoconfiguration (SLAAC)**. To ensure every device on a network had a unique address, SLAAC often used the device’s **MAC address** to fill in the second half (the Interface Identifier) of the 128-bit IPv6 address.

This method, called **EUI-64**, created two major privacy risks:

* **Device Fingerprinting:** Since your MAC address is gl...