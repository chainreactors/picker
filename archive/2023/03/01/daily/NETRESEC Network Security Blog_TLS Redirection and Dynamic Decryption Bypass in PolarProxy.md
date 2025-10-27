---
title: TLS Redirection and Dynamic Decryption Bypass in PolarProxy
url: https://www.netresec.com/?page=Blog&month=2023-02&post=TLS-Redirection-and-Dynamic-Decryption-Bypass-in-PolarProxy
source: NETRESEC Network Security Blog
date: 2023-03-01
fetch_date: 2025-10-04T08:22:31.194082
---

# TLS Redirection and Dynamic Decryption Bypass in PolarProxy

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

Tuesday, 28 February 2023 13:42:00 (UTC/GMT)

## [TLS Redirection and Dynamic Decryption Bypass in PolarProxy](/?page=Blog&month=2023-02&post=TLS-Redirection-and-Dynamic-Decryption-Bypass-in-PolarProxy)

PolarProxy is constantly being updated with new features, enhanced performance and bug fixes, but these updates are not always communicated other than as a short mention in the ChangeLog. I would therefore like to highlight a few recent additions to PolarProxy in this blog post.

**Custom TLS Redirection**

One new feature in [PolarProxy](https://www.netresec.com/?page=PolarProxy) is the --redirect argument, which can be used to redirect TLS traffic destined for a specific domain name to a different domain. This feature can be used to redirect TLS-encrypted malware traffic going to a known C2 domain to a local HTTPS sandbox instead, for example [INetSim](https://www.inetsim.org/).

PolarProxy --redirect malware-c2.com:inetsim.local --leafcert noclone

This --redirect argument will cause PolarProxy to terminate outgoing TLS traffic to malware-c2.com and redirect the decrypted traffic into a new TLS session going to inetsim.local instead. The “--leafcert noclone” argument forces PolarProxy to generate a fake X.509 certificate for “malware-c2.com” rather than sending a clone of the certificate received from the INetSim server to the malware implant.

> Note: You also need to specify a proxy mode, such as -p for transparent proxy or --socks for SOCKS proxy, to make the command above work.

![PolarProxy TLS redirect](https://www.netresec.com/images/PolarProxy_TLS-redirect_ASCII_518x174.png)

The --redirect argument can also be used to perform [domain fronting](https://en.wikipedia.org/wiki/Domain_fronting), which is a clever method for hiding the true destination of HTTPS based communication, in order to circumvent censorship or for other reasons conceal who you’re communicating with. The following command can be used to set up a local socks proxy that redirects traffic destined for YouTube to google.com instead:

PolarProxy --socks 1080 --redirect youtube.com,www.youtube.com,youtu.be:google.com

A browser configured to use PolarProxy as a SOCKS proxy will send HTTPS requests for youtube.com to PolarProxy, which then decrypts the TLS layer and re-encrypts the HTTP communication in a new TLS session directed at google.com instead. Someone who monitors the outgoing traffic from PolarProxy will assume that this is normal Google traffic, since the
[SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) as well as certificate will be for google.com. On the server side however, after having decrypted the TLS layer, Google will kindly forward the client’s original HTTP request for youtube.com to an endpoint that serves the content for YouTube.

**Dynamic TLS Decryption Bypass**

PolarProxy is designed to block TLS connections that it can’t decrypt, except for when the server’s domain name is explicitly marked for decryption bypass with the “--bypass” command line argument. However, as of recently PolarProxy also supports dynamic TLS decryption bypass using a form of fail-open mode. When this fail-open mode is enabled, PolarProxy attempts to intercept and decrypt proxied TLS traffic, but allows connections to bypass decryption if the same client-server pair has previously rejected PolarProxy’s certificate. This method is convenient when monitoring network traffic from applications that enforce certificate pinning or for some other reason can’t be configured to
[trust PolarProxy’s root CA](https://www.netresec.com/?page=PolarProxy#PolarProxyTrustCA) – provided that it’s acceptable to let traffic that can’t be decrypted to pass through untouched rather than blocking it, of course.

The following command line option configures PolarProxy to allow new TLS connections to bypass decryption for one hour (3600 seconds) after previously having failed to decrypt traffic between the same client and server.

--bypassonfail 1:3600

A simple way to verify this fail-open feature is to do a simple test with curl. It doesn’t matter if the client you’re testing on is Windows, Linux or macOS, since PolarProxy as well as curl is available for all three platforms.

PolarProxy --bypassonfail 1:3600 --socks 1080

curl --socks4 localhost -I https://example.com
curl: (60) SSL certificate problem: unable to get local issuer certificate

curl --socks4 localhost -I https://example.com
HTTP/2 200
content-encoding: gzip
accept-ranges: bytes
age: 593298
cache-control: max-age=604800
content-type: text/html; charset=UTF-8
date: Mon, 27 Feb 2023 14:29:46 GMT
etag: "3147526947"
expires: Mon, 06 Mar 2023 14:29:46 GMT
last-modified: Thu, 17 Oct 2019 07:18:26 GMT
server: ECS (nyb/1DCD)
x-cache: HIT
content-length: 648

Web browsers that don’t trust PolarProxy’s root CA will display a certificate warning the first time they visit a website that PolarProxy tries to decrypt traffic for.

![Firefox certificate warning](https://www.netresec.com/images/Firefox-certificate-warning_example-com_509x218.png)

But once the dynamic bypass has kicked in the user will no longer see a certificate warning when visiting the same website again, since traffic between that client and server is now end-to-end encrypted.

**Handling of non-TLS traffic and Better Logging**

Other new features in PolarProxy is the “--nontls” argument, which can be used to specify how to handle connections that doesn’t use TLS. The default action is to block non-TLS connections, but they can also be allowed to pass through (if the target host is known) or to forward the connection to a specific host and port. There is even a “--nontls encrypt” argument, which can be used to encrypt traffic that isn’t already TLS-encrypted before forwarding it to a specific host. This feature can be used as an alternative to stunnel to wrap traffic from applications that lack TLS support inside a TLS tunnel.

PolarProxy now also produces less output to stdout, unless -v is used, and error messages have been improved to be more specific and easier to understand.

Posted by Erik Hjelmvik on Tuesday, 28 February 2023 13:42:00 (UTC/GMT)

Tags:
#[PolarProxy](/?page=Blog&tag=PolarProxy)​
#[TLS](/?page=Blog&tag=TLS)​
#[redirect](/?page=Blog&tag=redirect)​
#[bypass](/?page=Blog&tag=bypass)​
#[fail-open](/?page=Blog&tag=fail-open)​
#[SNI](/?page=Blog&tag=SNI)​
#[ASCII-art](/?page=Blog&tag=ASCII-art)​

Short URL:
<https://netresec.com/?b=23275c9>

### Recent Posts

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

» [PureRAT = ResolverRAT = PureHVNC](/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC)

» [PureLogs Forensics](/?page=Blog&month=2025-07&post=PureLogs-Forensics)

» [CapLoader 2.0.1 Released](/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released)

» [Detecting PureLogs traffic with CapLoader](/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader)

» [CapLoader 2.0 Released](/?page=Blog&month=2025-06&post=CapLoader-2-0-Released)

» [Comparison of tools that extract files from PCAP](/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP)

### Blog Archive

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [20...