---
title: How to Inspect TLS Encrypted Traffic
url: https://www.netresec.com/?page=Blog&month=2024-08&post=How-to-Inspect-TLS-Encrypted-Traffic
source: NETRESEC Network Security Blog
date: 2024-08-08
fetch_date: 2025-10-06T18:08:00.165044
---

# How to Inspect TLS Encrypted Traffic

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

Wednesday, 07 August 2024 11:40:00 (UTC/GMT)

## [How to Inspect TLS Encrypted Traffic](/?page=Blog&month=2024-08&post=How-to-Inspect-TLS-Encrypted-Traffic)

Do you want to analyze decrypted TLS traffic in Wireshark or let an [IDS](https://en.wikipedia.org/wiki/Intrusion_detection_system), like Suricata, Snort or Zeek, inspect the application layer data of potentially malicious TLS encrypted traffic? There are many different TLS inspection solutions to choose from, but not all of them might be suitable for the specific challenge you’re facing. In this blog post I describe three different methods for decrypting TLS and explain when to use one or the other.

|  |  |  |  |
| --- | --- | --- | --- |
|  | RSA Private Key | TLS Key Log | TLS Inspection Proxy |
| Works for all ciphers | No (DHE cipher suites not supported) | **Yes** | **Yes** |
| TLS 1.3 supported | No | **Yes** | **Yes** |
| Zero client configuration required | **Yes** | No (pre-master secrets must be logged or extracted from TLS libraries) | No (root CA certificate must be installed) |
| Decrypts traffic from any application | No (most applications use modern ciphers with [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy), which RSA doesn’t provide) | No (each method for TLS key extraction typically only supports a specific set of applications or TLS libraries) | No (apps that use certificate pinning or a custom certificate trust store cannot be intercepted without patching the app) |
| L7 traffic in PCAP files can be analyzed without decrypting TLS | No | No | **Yes** |
| Allows decrypted traffic to be mirrored to a network interface | No | No | **Yes** |

**RSA Private Key**

TLS decryption with a private RSA key was for a long time the preferred method for inspecting SSL and TLS traffic. This approach allowed anyone with access to the server’s private RSA key to decrypt the traffic and inspect the application layer (L7) communication.

The primary drawback with RSA private key decryption is that a stolen or leaked private RSA key can be used by an attacker to decrypt all previously captured traffic from that server, if RSA key exchange is being used. Modern TLS stacks have therefore deprecated such ciphers in favor of ones that support [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy), which typically perform an ephemeral [Diffie–Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) (DHE) key exchange instead of reusing the same private RSA key over and over. This means that the RSA private key decryption method cannot be used if the client and server are using a key exchange algorithm that supports forward secrecy.

RSA private key decryption can only be performed when all these conditions are met:

* The protocol version is SSL 3.0, TLS 1.0, TLS 1.1 or TLS 1.2 (RSA was removed in TLS 1.3)
* The server has selected a cipher suite that use RSA key exchange, such as
  TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384,
  TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256,
  TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256,
  TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256,
  TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA or
  TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA
* The private key matches the server certificate (traffic cannot be decrypted with a client certificate or an intermediate or root certificate)
* The session has not been resumed (the handshake must include a Client Key Exchange message)

This Wireshark display filter can be used to check if the server has selected an RSA cipher:

tls.handshake.type == 2 and tls.handshake.ciphersuite in {10,47,53,60,61,156,157}

You can check for a client key exchange message with:

tls.handshake.type == 16

A private RSA key can be loaded into Wireshark by clicking Edit, Preferences and RSA Keys. Another alternative is to use the command line tool tshark’s -ouat:rsa\_keys switch like this:

tshark -r tls.pcap -ouat:rsa\_keys:'"/path/rsa.key",""'

**TLS Key Log**

Wireshark can decrypt the TLS layer in captured network traffic if the [pre-master secrets](https://wiki.wireshark.org/TLS#using-the-pre-master-secret) used to establish the encrypted connection are provided. These secrets, or encryption key material, can be loaded into Wireshark from an [SSLKEYLOGFILE](https://datatracker.ietf.org/doc/draft-ietf-tls-keylogfile/) by clicking Edit, Preferences, Protocols, TLS, and setting the (Pre)-Master-Secret log filename to the path of your SSLKEYLOGFILE.

![Wireshark SSLKEYLOGFILE](https://media.netresec.com/images/Wireshark_SSLKEYLOGFILE_520x407.png)

Another alternative is to encode the key material as metadata in a [pcap-ng](https://pcapng.com/) file with editcap like this:

editcap --inject-secrets tls,SSLKEYLOG.txt tls.pcap tls-and-keys.pcapng

The primary drawback with the TLS key log decryption method is that only Wireshark and tshark can be used to analyze the decrypted TLS traffic.
You also need to get hold of the keys or pre-master secrets in order to perform the decryption.
Some applications, such as Firefox, Chrome and [curl](https://everything.curl.dev/usingcurl/tls/sslkeylogfile.html), can be configured to export a key log.
Another alternative is to install an agent that extracts key material from specific TLS libraries.

The limitation of only being able to extract keys from a specific set of applications or TLS libraries makes the TLS key log method unsuitable for analyzing TLS encrypted C2 traffic from malware, which often use custom TLS libraries.
It is also difficult to send decrypted TLS traffic to an IDS or a network security monitoring tool using a TLS key log.
If you, on the other hand, want to analyze network traffic from your own Firefox or Chrome browser in Wireshark, then the TLS key log approach is probably the best solution.

**TLS Inspection Proxy**

A TLS inspection proxy acts as a [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) that intercepts and decrypts TLS traffic for inspection, it then re-encrypts the traffic and forwards it to the intended destination.

![TLS inspection proxy](https://media.netresec.com/images/TLS-inspection-proxy_1040x390.webp)

A major advantage of using a TLS inspection proxy is that decrypted TLS traffic can be analyzed from applications even if they use modern ciphers with forward secrecy and don’t support logging of TLS keys. The drawback, however, is that clients have to trust the root CA certificate that the proxy is using.

TLS inspection proxies often differ in how they make the decrypted traffic available to external tools, if at all. In fact, many TLS inspection proxies and [Next-Generation Firewalls](https://en.wikipedia.org/wiki/Next-generation_firewall) (NGFW) only make the decrypted payload available to the internal application or appliance. Such an approach prevents analysis of the decrypted traffic with an external tool, like Wireshark, Snort, Suricata, Zeek or NetworkMiner.

Another approach, used by proxies like [mitmproxy](https://github.com/mitmproxy/mitmproxy), is to save a TLS key log for all proxied traffic. That approach allows captured TLS traffic to or from the proxy to be decrypted and inspected with Wireshark, but the application layer traffic cannot be inspected with other tools that don’t support TLS decryption using a key log.

The third and most integration friendly approach is to save the decrypted traffic in clear text form, so that other applications can inspect the unencrypted traffic without having to decrypt TLS. Some TLS proxies, like [PolarProxy](https://www.netresec.com/?page=PolarProxy) and [SSLsplit](https://github.com/droe/sslsplit), can even save the decrypted t...