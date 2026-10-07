---
title: Reversing Engineering a Captive Portal
url: https://binary.ninja/2026/10/06/reverse-engineering-airbnb-captive-portal.html
source: Binary Ninja
date: 2026-10-06
fetch_date: 2026-10-07T07:55:07.744484
---

# Reversing Engineering a Captive Portal

[Skip to main content](#main-content)

[![Binary Ninja](/images/binary-ninja-wordmark-light-2tone.svg)](/)

Features

[Features Overview](/features/)
[Enterprise](/enterprise/)

[Sidekick](https://sidekick.binary.ninja)
[Portal](https://portal.binary.ninja/dashboard)
[Training](/training/)

Support

[Support Overview](/support/)
[Extended Support](/support/extended.html)
[Documentation](/support/#documentation)
[License/Installer Recovery](/recover/)
[Renew Current License](/renew/)
[Slack Signup](https://slack.binary.ninja/)
[FAQ](/faq/)
[Sponsorship Information](/sponsorship/)
[Contact Us](/support/)

[Blog](/blog/)
[Gear](https://shop.binary.ninja)

[Try For Free](/free)
[Purchase](/purchase)

Not a bird, a plane, it's [Binary Ninja 6.0](/2026/09/03/binary-ninja-6.0-krypton.html)! A
super-powered release with more improvements than ever. Massive performance gains, binary similarity, TMS320C6x, MCP, and much more.

[Binary Ninja Blog](/blog/)

# Reversing Engineering a Captive Portal

By [Xusheng Li](https://github.com/xusheng6)
 2026-10-06

I recently stayed at an vacation rental with a strange Wi-Fi setup. After I selected the network (SSID) and entered the WPA2 password, I was presented with a captive portal asking for a bunch of information instead of being given Internet access:

![A reconstructed StayFi captive portal with property-specific content replaced by placeholders](/blog/images/stayfi-express/captive-portal-mockup.jpg)

*A reconstruction of the portal with the property name, Wi-Fi name, property managerâs name, welcome message, and location-specific background replaced.*

This immediately caught my eye. Captive portals are common at hotels or on open networks, but I had not expected one at this vacation rental after entering the Wi-Fi password. So I decided to find out what was going on.

## Starting with the Network

The captive portal pointed to `guest.stayfi.com`, and a quick Google search led me to the [StayFi](https://stayfi.com/) home page which describes the product as âWiFi & Guest Marketing Built For Vacation Rentals.â This looked interesting, though it was not immediately clear how it worked.

I asked an AI agent to map out the network topology, and it ran a few quick commands:

```
route -n get default
scutil --dns
arp -an
```

I initially assumed the captive portal was implemented by the gateway, but these commands quickly showed that the gateway and DNS server were two different hosts:

```
default gateway:  192.168.x.1
DNS server:       192.168.x.y

ARP entry for gateway:  78:45:58:xx:xx:xx
ARP entry for DNS:      88:a2:9e:yy:yy:yy
```

The DNS serverâs MAC prefix, `88:a2:9e`, pointed to Raspberry Pi hardware. Conveniently, the [StayFi Express](https://stayfi.com/stayfi-express/) webpage includes a photo of the device, and it is unmistakably a Raspberry Pi. The [setup guide](https://hubspot.stayfi.com/knowledge/stayfi-express-use-your-existing-wifi-to-collect-guest-emails) also lists configuring custom DNS as part of installation.

This also explains how the StayFi device can trigger the captive portal. As the DNS server, it can direct queries such as `captive.apple.com` to itself. Its local HTTP server then redirects the browser to the remote StayFi portal shown earlier. If you submit the requested information, StayFi authorizes your device for Internet access.

At this point, several possible bypasses came to mind. We could try a different DNS server, such as `1.1.1.1` or `8.8.8.8`, or perhaps connect through our own VPN. For the latter, we might need to know the VPNâs IP in advance. I manually changed the DNS server and the bypass worked on this network, but I still wanted to see exactly how StayFi works.

## Imaging the Device

I decided to dig deeper. The operating system lives on an easily removable SD card (thanks, Raspberry Pi!), so I dumped a full disk image of it:

```
sudo dd if=/dev/rdisk8 \
  of=stayfi-express.img \
  bs=8m conv=noerror,sync
```

The resulting image was about 30 GB, most of which was empty space. The layout uses an A/B update scheme: two root slots allow a new system image to be installed while retaining a known-good one for rollback. A persistent data partition provides an overlay for configuration, databases, logs, and credentials.

After unpacking everything, the root filesystem contained mostly recognizable Linux packages. The custom part was thankfully small: three stripped AArch64 ELF binaries all built with Go 1.22.5.

| Component | Size | Job |
| --- | --- | --- |
| `dnsserver` | 7.6 MB | Resolves DNS, associates requests with client MAC addresses, applies access policy, and logs queries |
| `httpserver` | 7.2 MB | Redirects unauthenticated HTTP clients to the cloud portal and proxies selected traffic |
| `stayfi-agent` | 7.7 MB | Handles configuration, telemetry, remote commands, and device state |

This is one reason appliance reversing can be fun: a multi-gigabyte filesystem often reduces to a few megabytes of code that actually answers your question. The remaining data is just Linux doing Linux things.

## Reverse Engineering the Go Programs

Go binaries are large, but they are often generous to reverse engineers. Even in stripped executables, metadata such as `.gopclntab` can preserve package paths and function names. I asked my AI agent to recover those names and analyze the binaries with the help of [Binary Ninjaâs MCP server](https://docs.binary.ninja/guide/mcp.html). The overall design became clear quickly.

The HTTP service uses Goâs standard `net/http` stack and `net/http/httputil.ReverseProxy`. The DNS service uses the well-known [`miekg/dns`](https://github.com/miekg/dns) package. Both use SQLite for local state. Using existing protocol libraries meant I could focus my analysis on the policy wrapped around them.

In simplified Go-like pseudocode, the HTTP flow looked roughly like this:

```
clientMAC := macForIP(request.RemoteAddr)

if isAuthorized(clientMAC) {
    proxyRequest(request)
    return
}

if matchesSmartConnect(request.UserAgent) {
    go authorizeWithCloud(clientMAC)
    proxyRequest(request)
    return
}

redirectToCaptivePortal(clientMAC)
```

For each client request, the appliance maps the source IP address back to a MAC address using its ARP table, with `arping` as a fallback. The MAC address becomes the local identity. SQLite records whether that identity is authorized, blocked, or eligible for a bypass rule.

DNS and HTTP then cooperate as DNS applies the clientâs policy and records the query. When an unauthenticated browser makes a plain HTTP request, the HTTP service sends a redirect resembling:

```
https://guest.stayfi.com/sbc/captive_portal?sbc_mac=<appliance>&client_mac=<guest>
```

Notice that this is no longer on the local deviceâthe request goes to a remote server.

According to StayFiâs [privacy policy](https://stayfi.com/privacy-policy/) (last updated July 31, 2025), StayFi may disclose personal information such as email addresses, device identifiers, phone numbers, and usage information to the property manager. It may also share information with advertising partners.

I even tried entering a syntactically valid but fake-looking email address. The webpage had no issue with it, but the server rejected it. StayFiâs [setup documentation](https://hubspot.stayfi.com/knowledge/setting-up-your-stayfi-account) says its optional valid-email check uses ZeroBounce, which is consistent with the rejection I observed. That check validates an email address; it does not establish the identity of the person entering it.

## A Serious Privacy Concern

A closer look at the DNS server showed that it logs requests to `dnsserver.log`. A [Datadog](https://www.datadoghq.com/) agent tails this file, with a configuration to forward the DNS logs to that third-party service.

The log recovered from my device covered about three and a half hours. It contained 11,801 DNS-request records representing 639 unique domain names. Packet captures showed...