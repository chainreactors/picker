---
title: Blocking Malicious sites with a TLS Firewall
url: https://www.netresec.com/?page=Blog&month=2025-01&post=Blocking-Malicious-sites-with-a-TLS-Firewall
source: NETRESEC Network Security Blog
date: 2025-01-28
fetch_date: 2025-10-06T20:10:51.572687
---

# Blocking Malicious sites with a TLS Firewall

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Monday, 27 January 2025 10:45:00 (UTC/GMT)

## [Blocking Malicious sites with a TLS Firewall](/?page=Blog&month=2025-01&post=Blocking-Malicious-sites-with-a-TLS-Firewall)

Over 90 percent of all web traffic is encrypted nowadays, which is great of course. However, as HTTP and DNS traffic gets encrypted, defenders have a more difficult time blocking malicious network traffic. One solution to this problem is to use a TLS firewall, which effectively blocks encrypted connections to known bad websites.

**DNS Firewalls and Sinkholes**

DNS firewalls and DNS sinkholes, like [pihole](https://pi-hole.net/) and [RPZ firewalls](https://www.isc.org/rpz/), are simple yet effective solutions that can prevent users from connecting to malicious websites. They work by acting as recursive name servers that deny clients from resolving known-bad domain names. However, more and more DNS traffic is becoming encrypted with [DNS-over-TLS](https://en.wikipedia.org/wiki/DNS_over_TLS) (DoT) and [DNS-over-HTTPS](https://en.wikipedia.org/wiki/DNS_over_HTTPS) (DoH), where clients send DNS queries inside an end-to-end encrypted connection directly to a DNS provider. This prevents many DNS based security solutions, like DNS firewalls, from inspecting the queried hostnames.

One way around this problem is to block the actual connections to known-bad domains instead of preventing clients from resolving them. For outgoing TLS connections, such as HTTPS, this can be done with a TLS Firewall.

**TLS Firewalls**

A TLS firewall inspects client TLS handshakes and extracts the requested server name from the
[Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication) (SNI) extension. This hostname is generally sent unencrypted in HTTPS traffic (even if you use TLS 1.3), which allows the hostname to be inspected without having to break the TLS encryption. The TLS firewall then checks if the hostname is a known bad or malicious website, in which case the connection is either closed or the user gets redirected to a warning page.

**Blocklists**

There are several blocklists with malicious domain names, including commercial services as well as freely available lists from [ThretFox](https://threatfox.abuse.ch/export/#rpz), [CERT Polska](https://cert.pl/en/warning-list/) and others. These blocklists are often created for DNS firewalls and sinkholes, but they can also be leveraged by TLS firewalls to identify and block traffic to malicious websites.

**PolarProxy**

[PolarProxy](https://www.netresec.com/?page=PolarProxy) can be used as a [TLS firewall](https://tlsfirewall.com) simply by loading a [ruleset](https://github.com/Netresec/PolarProxy/blob/main/rulesets/ruleset-block-malicious.json) that blocks connections to malicious domains.

![PolarProxy block/inspect/bypass ASCII](https://media.netresec.com/images/PolarProxy_block-inspect-bypass-ascii_520x380.png)

PolarProxy has the capability to decrypt and inspect what’s inside the TLS encryption, but this feature is not needed when acting as a TLS firewall. The hostname the client wants to connect to is generally provided in the SNI without encryption, so PolarProxy doesn’t have to use the “inspect” action when acting as a TLS firewall. When running in “firewall mode” PolarProxy performs the “block” action for connections to known malicious domains and the “bypass” action for all other TLS traffic. Because of this there is no need for configuring clients to trust PolarProxy’s root certificate in TLS firewall deployments, unless you add a custom rule that decrypts and inspects certain traffic. In fact, if PolarProxy is deployed as a transparent forward proxy in this TLS firewall mode, then zero client configuration is required. This means that managed as well as unmanaged devices, including [BYOD](https://en.wikipedia.org/wiki/Bring_your_own_device), embedded devices, appliances etc., will be protected!

**Transparent TLS Firewall (Linux)**

![Network ASCII drawing](https://media.netresec.com/images/Internet-firewall-clients_22x20.svg)

If your network has a Linux based firewall that uses iptables, then you’ll be able to run [PolarProxy](https://www.netresec.com/?page=PolarProxy) as a transparent TLS firewall directly on your Linux firewall with this command:

./PolarProxy -p 10443,80,443 --ruleset https://raw.githubusercontent.com/Netresec/PolarProxy/main/rulesets/ruleset-block-malicious.json

You then need to configure the iptables firewall to redirect HTTPS traffic from your network to PolarProxy (see "Routing Option #1" in the [PolarProxy documentation](https://www.netresec.com/?page=PolarProxy) for more details).

* sudo iptables -I INPUT -i eth1 -p tcp --dport 10443 -m state --state NEW -j ACCEPT
* sudo iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 443 -j REDIRECT --to 10443

Congratulations, your firewall now blocks outgoing HTTPS connections from local clients to known malicious websites!

PolarProxy can also be run in a container using [Docker](https://netresec.com/?b=20Accbd) or [Podman](https://netresec.com/?b=20A16ef).

**HTTPS Proxy TLS Firewall (Windows)**

It’s even possible to run [PolarProxy](https://www.netresec.com/?page=PolarProxy) directly on a Windows PC and configure the local proxy settings to send outgoing traffic through PolarProxy. Use the following command to start [PolarProxy](https://www.netresec.com/?page=PolarProxy) as a [HTTP CONNECT](https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_method) proxy server on port 8080 with a TLS firewall ruleset:

PolarProxy.exe --httpconnect 127.0.0.1:8080 --ruleset https://raw.githubusercontent.com/Netresec/PolarProxy/main/rulesets/ruleset-block-malicious.json

Then configure the Windows PC to use a proxy server on 127.0.0.1 on port 8080.

![Windows proxy server exceptions](https://media.netresec.com/images/Windows-proxy-server-exceptions_520x555.webp)

Add the following exceptions to the Windows proxy settings to ensure that PolarProxy can download the ruleset and blocklists:

> raw.githubusercontent.com;\*.abuse.ch;hole.cert.pl;zonefiles.io;github.com

Click “Save”.

One side effect of running PolarProxy as an HTTP connect proxy (with --httpconnect) is that this mode only allows TLS encrypted traffic to pass through the proxy. This means that plaintext HTTP traffic that Windows forwards to PolarProxy on port 8080 will be blocked. You’ll see error messages like “Request method "GET" is not supported by HTTP CONNECT proxy” in PolarProxy’s output if it is started with the “-v” argument.

A workaround for this side effect is to run inetcpl.cpl (Window’s old school Internet Properties), select “Connections” tab and click the “LAN settings” button.

![Windows inetcpl.cpl connections](https://media.netresec.com/images/Windows-inetcpl-connections_409x535.png)

Then click the “Advanced” button in the Proxy server section of the LAN Settings window to configure which protocols that should run through the proxy.

![Windows LAN settings](https://media.netresec.com/images/Windows-LAN-settings_380x339.png)

Uncheck “Use the same proxy server for all protocols” and remove the proxy settings for everything except “Secure”, which is HTTPS traffic and clock “OK”.

![Windows proxy settings: only https](https://media.netresec.com/images/Windows-proxy-settings_only_https_395x433.png)

The Windows PC should now only forward HTTPS traffic to PolarProxy’s TLS firewall.

**Pro Tip**

Enter the following value as “Proxy IP address” directly in the modern “Edit proxy server” settings in Windows 10/11 to only proxy HTTPS traffic without using the legacy inetcpl.cpl settings:

http://https=127.0.0.1

Finall...