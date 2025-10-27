---
title: UDPX - Fast A nd Lightweight, UDPX Is A Single-Packet UDP Scanner Written In Go That Supports The Discovery Of Over 45 Services With The Ability To Add Custom Ones
url: https://buaq.net/go-159663.html
source: unSafe.sh - 不安全
date: 2023-04-21
fetch_date: 2025-10-04T11:32:32.850547
---

# UDPX - Fast A nd Lightweight, UDPX Is A Single-Packet UDP Scanner Written In Go That Supports The Discovery Of Over 45 Services With The Ability To Add Custom Ones

* [unSafe.sh - õĖŹÕ«ēÕģ©](https://unsafe.sh)
* [µłæńÜäµöČĶŚÅ](/user/collects)
* [õ╗ŖµŚźńāŁµ”£](/?hot=true)
* [Õģ¼õ╝ŚÕÅĘµ¢ćń½Ā](/?gzh=true)
* [Õ»╝Ķł¬](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [ń╝¢ńĀü/Ķ¦ŻńĀü](/encode)
* [µ¢ćõ╗Čõ╝ĀĶŠō](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
ķ╗æÕż£µ©ĪÕ╝Å

![](https://8aqnet.cdn.bcebos.com/46ffbec9494e7d938588ce329e2def4c.jpg)

UDPX - Fast A nd Lightweight, UDPX Is A Single-Packet UDP Scanner Written In Go That Supports The Discovery Of Over 45 Services With The Ability To Add Custom Ones

Fast and lightweight, UDPX is a single-packet UDP scanner written in Go that supports the
*2023-4-20 20:30:0
Author: [www.kitploit.com(µ¤źń£ŗÕÄ¤µ¢ć)](/jump-159663.htm)
ķśģĶ»╗ķćÅ:35
µöČĶŚÅ*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjN_W7QkXkjYzEc2luEbs-zRF447vJ3SK0hUFdiQblcVXJlG8q7JWVYsBEG_w7uhpHStkMtSh00b6sd3RnuqtctWgEeWLU0vDWwboa2L5-XqRi8y_g8ivSsQSis-Q257zvK_6O3_Wd8B25z4vlsg2EaVj9paRg2M0bt0PW2WlcgkHglcLIvxFVX3H9KPw=w640-h138)](https://blogger.googleusercontent.com/img/a/AVvXsEjN_W7QkXkjYzEc2luEbs-zRF447vJ3SK0hUFdiQblcVXJlG8q7JWVYsBEG_w7uhpHStkMtSh00b6sd3RnuqtctWgEeWLU0vDWwboa2L5-XqRi8y_g8ivSsQSis-Q257zvK_6O3_Wd8B25z4vlsg2EaVj9paRg2M0bt0PW2WlcgkHglcLIvxFVX3H9KPw)

Fast and lightweight, UDPX is a single-packet UDP scanner written in Go that supports the [discovery](https://www.kitploit.com/search/label/Discovery "discovery") of over 45 services with the ability to add custom ones. It is [easy to use](https://www.kitploit.com/search/label/Easy%20To%20Use "easy to use") and portable, and can be run on Linux, Mac OS, and Windows. Unlike internet-wide [scanners](https://www.kitploit.com/search/label/Scanners "scanners") like zgrab2 and zmap, UDPX is designed for portability and ease of use.

* It is fast. It can scan whole /16 network in ~20 seconds for a single service.
* You don't need to instal libpcap or any other dependencies.
* Can run on Linux, Mac Os, Windows. Or your Nethunter if you built it for Arm.
* Customizable. You can add your probes and test for even more protocols.
* Stores results in JSONL format.
* Scans also domain names.

## How it works

Scanning UDP ports is very different than scanning TCP - you may, or may not get any result back from probing an UDP port as UDP is a connectionless protocol. UDPX implements a single-packet based approach. A protocol-specific packet is sent to the defined service (port) and waits for a response. The limit is set to 500 ms by default and can be changed by `-w` flag. If the service sends a packet back within this time, it is certain that it is indeed listening on that port and is reported as open.

A typical technique is to send 0 byte UDP packets to each port on the target machine. If we receive an "ICMP Port Unreachable" message, then the port is closed. If an UDP response is received to the probe (unusual), the port is open. If we get no response at all, the state is open or filtered, meaning that the port is either open or packet filters are blocking the communication. This method is not implemented as there is no added value (UDPX tests only for specific protocols).

## Usage

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjEm1llmMZX4-ztohOZp-2Ra_4BjNpJq8lGHLh1LijGVrzHY6JuE7AH3dmPMkp4MCp6hYZDGyg0qJYDeaNOqSYbkl-XRQhGZ7ew-CSh8b57RnF-McxnEPgTg9VdKKsvsvYO5lasyrs2lyCsAe1aDKb9PBUZVEZVp8ulSmJre-oXla0kvjcVZc8w_DEyXw=w640-h242)](https://blogger.googleusercontent.com/img/a/AVvXsEjEm1llmMZX4-ztohOZp-2Ra_4BjNpJq8lGHLh1LijGVrzHY6JuE7AH3dmPMkp4MCp6hYZDGyg0qJYDeaNOqSYbkl-XRQhGZ7ew-CSh8b57RnF-McxnEPgTg9VdKKsvsvYO5lasyrs2lyCsAe1aDKb9PBUZVEZVp8ulSmJre-oXla0kvjcVZc8w_DEyXw)

> **Concurrency:** By default, concurrency is set to 32 connections only (so you don't crash anything). If you have a lot of hosts to scan, you can set it to 128 or 256 connections. Based on your hardware, connection stability, and ulimit (on \*nix), you can run 512 or more concurrent connections, but this is not recommended.

To scan a single IP:

To scan a CIDR with maximum of 128 connections and timeout of 1000 ms:

```
udpx -t 1.2.3.4/24 -c 128 -w 1000
```

To scan targets from file with maximum of 128 connections for only specific service:

```
udpx -tf targets.txt -c 128 -s ipmi
```

Target can be:

* IP address
* CIDR
* Domain

IPv6 is supported.

If you want to store the results, use flag `-o [filename]`. Output is in JSONL format, as can be seen bellow:

```
{"address":"45.33.32.156","hostname":"scanme.nmap.org","port":123,"service":"ntp","response_data":"JAME6QAAAEoAAA56LU9vp+d2ZPwOYIyDxU8jS3GxUvM="}
```

## Options

```
        __  ______  ____ _  __
       / / / / __ \/ __ \ |/ /
      / / / / / / / /_/ /   /
     / /_/ / /_/ / ____/   |
     \____/_____/_/   /_/|_|
         v1.0.2-beta, by @nullt3r

Usage of ./udpx-linux-amd64:
  -c int
    	Maximum number of concurrent connections (default 32)
  -nr
    	Do not randomize addresses
  -o string
    	Output file to write results
  -s string
    	Scan only for a specific service, one of: ard, bacnet, bacnet_rpm, chargen, citrix, coap, db, db, digi1, digi2, digi3, dns, ipmi, ldap, mdns, memcache, mssql, nat_port_mapping, natpmp, netbios, netis, ntp, ntp_monlist, openvpn, pca_nq, pca_st, pcanywhere, portmap, qotd, rdp, ripv, sentinel, sip, snmp1, snmp2, snmp3, ssdp, tftp, ubiquiti, ubiquiti_discovery_v1, ubiquiti_discovery_v2, upnp, valve, wdbrpc, wsd, wsd_malformed, xdmcp, kerberos, ike
  -sp
    	Show received packets (only first 32 bytes)
  -t string
       	IP/CIDR to scan
  -tf string
    	File containing IPs/CIDRs to scan
  -w int
    	Maximum time to wait for a response (socket timeout) in ms (default 500)
```

## Building

You can grab prebuilt binaries in the release section. If you want to build UDPX from source, follow these steps:

From git:

```
git clone https://github.com/nullt3r/udpx
cd udpx
go build ./cmd/udpx
```

You can find the binary in the current directory.

Or via go:

After that, you can find the binary in `$HOME/go/bin/udpx`. If you want, move binary to `/usr/local/bin/` so you can call it directly.

## Supported services

The UDPX supports more then 45 services. The most interesting are:

* ipmi
* snmp
* ike
* tftp
* openvpn
* kerberos
* ldap

The complete list of supported services:

* ard
* bacnet
* bacnet\_rpm
* chargen
* citrix
* coap
* db
* db
* digi1
* digi2
* digi3
* dns
* ipmi
* ldap
* mdns
* memcache
* mssql
* nat\_port\_mapping
* natpmp
* netbios
* netis
* ntp
* ntp\_monlist
* openvpn
* pca\_nq
* pca\_st
* pcanywhere
* portmap
* qotd
* rdp
* ripv
* sentinel
* sip
* snmp1
* snmp2
* snmp3
* ssdp
* tftp
* ubiquiti
* ubiquiti\_discovery\_v1
* ubiquiti\_discovery\_v2
* upnp
* valve
* wdbrpc
* wsd
* wsd\_malformed
* xdmcp
* kerberos
* ike

## How to add your own probe?

Please send a feature request with protocol name and port and I will make it happen. Or add it on your own, the file `pkg/probes/probes.go` contains all available payloads. Specify the protocol name, port and packet data (hex-encoded).

```
{
        Name: "ike",
        Payloads: []string{"5b5e64c03e99b51100000000000000000110020000000000000001500000013400000001000000010000012801010008030000240101"},
        Port: []int{500, 4500},
},
```

## Credits

* [Nmap](https://nmap.org/ "Nmap")
* [UDP Hunter](https://github.com/NotSoSecure/udp-hunter "UDP Hunter")
* [ZGrab2](https://github.com/zmap/zgrab2 "ZGrab2")
* [ZMap](https://github.com/zmap/zmap "ZMap")

## Disclaimer

I am not responsible for any damages. You are responsible for your own actions. Scanning or attacking targets without prior mutual consent can be illegal.

## License

UDPX is [distributed](https://www.kitploit.com/search/label/Distributed "distributed") under [MIT License](https://raw.githubusercontent.com/nullt3r/udpx/main/LICENSE "MIT License").

UDPX - Fast A nd Lightweight, UDPX Is A Single-Packet UDP Scanner Written In Go That Supports The Discovery Of O...