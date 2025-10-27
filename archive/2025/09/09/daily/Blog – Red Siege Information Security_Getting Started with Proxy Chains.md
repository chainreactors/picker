---
title: Getting Started with Proxy Chains
url: https://redsiege.com/blog/2025/09/getting-started-with-proxy-chains/
source: Blog – Red Siege Information Security
date: 2025-09-09
fetch_date: 2025-10-02T19:50:35.571825
---

# Getting Started with Proxy Chains

Register Now For On-Demand Training!

[Learn More](https://training.redsiege.com)

[![](https://redsiege.com/wp-content/uploads/2022/01/redsiege-logo-300x73.png)](https://redsiege.com)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

![](https://redsiege.com/wp-content/themes/red-siege-theme/img/icon-phone.svg) +1 234-249-1337

# Getting Started with Proxy Chains

By Red Siege | September 8, 2025

![](https://redsiege.com/wp-content/uploads/2025/08/GETTING-STARTED-PROXY.jpg)

**by Justin Palk**

Oftentimes on an assumed breach test, we need or want to run tools on our local Kali VM and proxy them into the client’s network over a SOCKS5 proxy (if you’re on Windows, take a look at Proxifier). Some tools are proxy aware, so we can just point them at the proxy port and let them go. Others… Aren’t. Which is where [ProxyChains](https://github.com/rofl0r/proxychains-ng) comes in.

ProxyChains is a tool that hooks into networking libraries in order to redirect traffic through one proxy or a chain of proxies. It supports SOCKS4/5 or HTTP proxies for TCP connections, no UDP or ICMP.

A quick primer on proxies:

Putting it simply, a proxy is an application that accepts network traffic and redirects it to another destination. The three most common types you’ll encounter are HTTP, SOCKS4 and SOCKS5.

* HTTP(S) proxies relay primarily web traffic between clients and servers.
* SOCKS4 proxies can relay TCP traffic, but not UDP, and have no authentication or encryption
* SOCKS5 proxies can relay TCP and UDP, and support authentication, but are not encrypted

Proxies have their own protocols, or, in the case of HTTP proxies, specific methods, that let them know where they are supposed to send traffic. Some tools are built to be proxy-aware, that is, they have functionality built-in that can speak the relevant proxy protocol and connect directly to a proxy specified by command-line options. Others aren’t proxy-aware, so something else needs to handle the proxy communications for them, which is where ProxyChains comes in.

ProxyChains is controlled through configuration files, the default being `/etc/proxychains4.conf`. The configuration file has a lot of options you can configure, including how it handles DNS, which local IP addresses or networks and ports to exclude, timeouts, and how proxied IP addresses are generated.

For basic usage, we can ignore most of that and jump straight to the end, where we define our proxies or proxy chains. I typically use only a single proxy, either a SOCKS5 proxy running through a beacon, or an SSH SOCKS5 proxy running through the dropbox we have in a client’s network. In either case, this takes only one line specifying the proxy type, host IP, and port in the [ProxyList] block at the end of the configuration file, as shown below.

![](https://redsiege.com/wp-content/uploads/2025/08/proxychains1-300x105.png)

Configuring ProxyChains to use a Single SOCKS5 Proxy

The type of proxy can be either socks5, socks4, or http, and if your socks5 proxy requires authentication, you just need to add the username and password to the end of the line, like this:
`socks5 127.0.0.1 9000 justin SecretPassword`

The simplest way to run ProxyChains is simply prepending proxychains to whatever command you’re trying to run. Here’s an example of me running Impacket’s getTGT.py to request a Kerberos ticket over my SOCKS5 proxy.

![](https://redsiege.com/wp-content/uploads/2025/08/proxychains2-300x140.png)

Requesting a Kerberos Ticket using getTGT.py Over a Proxy

Notice the [proxychains] lines throughout. ProxyChains is very chatty, and by default will report every connection it makes. If you’re running a tool like Pre2k, which makes a lot of connections, this makes it difficult to identify useful information and get clean screenshots, as shown below.

![](https://redsiege.com/wp-content/uploads/2025/08/proxychains3-300x263.png)

ProxyChains is Very Chatty

You can stop this by using the `-q` (quiet) flag. The screenshot below shows me running the same command as before, but with the `-q` flag on.

![](https://redsiege.com/wp-content/uploads/2025/08/proxychains4-300x178.png)

Running ProxyChains with the Quiet Flag

If you’ve got multiple proxies with different destinations, such as one running on a beacon, and one running on a dropbox, you can create multiple configuration files pointing to different proxy ports, and name them appropriately, so you can select them on the command line using the `-f` flag. For example, I’ve got `proxychains.beacon.conf`, `proxychains.dropbox.conf`, and `proxychains.burp.conf`, and I can route things (quietly) using the appropriate proxy like this:

`proxychains -q -f /etc/proxychains.burp.conf curl -Ikv https://redsiege.com`

If you’re attempting to reach a port on 127.0.0.1 on your target host, say, if you want to reach 445/tcp on your foothold host, but it blocks incoming SMB connections on its real IP address, you need to make sure that ProxyChains is not configured to block those connections. Check your localnet directives in your configuration file and make sure that 127.0.0.0/255.0.0.0 is commented out. The localnet directives tell ProxyChains to not proxy traffic bound for those networks. The proper configuration to proxy to localhost on the remote host is shown below.

![](https://redsiege.com/wp-content/uploads/2025/08/proxychains5-300x62.png)

This Config Permits Proxying to the Remote Machine’s Loopback Address

---

#### About Justin Palk, Senior Security Consultant:

![](https://redsiege.com/wp-content/uploads/2023/03/JUSTIN-RED-SIEGE_2.jpg)

Justin Palk has more than 16 years of experience in IT and information security, and has worked in the academic, federal civilian government and health research sectors. He has held a variety of roles including system administrator, developer, auditor, assessment team lead and web application penetration tester. He regularly competes in CTFs in the U.S. and Europe.

**Certifications:**
GCIH, GWAPT, GPEN, GMOB, GDSA

Related Stories

[View More](/blog/)

## Threat Detection Made Simple: Splunk Attack Range Basics

By Red Siege | September 22, 2025

by Ian Briley Let’s be honest, when starting a new skill or interest, one of the largest hurdles is setting up an environment//playground//attack range for your learning activities. Sometimes it […]

Learn More

[Threat Detection Made Simple: Splunk Attack Range Basics](https://redsiege.com/blog/2025/09/threat-detection-made-simple-splunk-attack-range-basics/)

## Kerberoasting, Microsoft, and a Senator

By Tim Medin | September 11, 2025

Kerberoasting, Microsoft, and a Senator When I came up with Kerberoasting in 2014, I never thought it would live for more than a year or two. I (erroneously) thought that […]

Learn More

[Kerberoasting, Microsoft, and a Senator](https://redsiege.com/blog/2025/09/kerberoasting-microsoft-and-a-senator/)

## Stupid Simple: Windows Data Exfiltration

By Red Siege | September 8, 2025

by Ian Briley To get around a DLP (Data Loss Prevention) implementation, you don’t need a fancy C2 setup to exfil your treasures. In fact, it’s incredibly easy using native […]

Learn More

[Stupid Simple: Windows Data Exfiltration](https://redsiege.com/blog/2025/09/stupid-simple-windows-data-exfiltration/)

## Find Out What’s Next

Stay in the loop with our upcoming events.

Please enable JavaScript in your browser to complete this form.

Email \*

Email

JOIN OUR EMAIL LIST

Stay Connected

* [![](https://redsiege.com/wp-co...