---
title: Fingerprintx - Standalone Utility For Service Discovery On Open Ports!
url: https://buaq.net/go-156337.html
source: unSafe.sh - 不安全
date: 2023-04-01
fetch_date: 2025-10-04T11:19:31.623161
---

# Fingerprintx - Standalone Utility For Service Discovery On Open Ports!

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9b97b0daabb01714755d90279ab3e2b8.jpg)

Fingerprintx - Standalone Utility For Service Discovery On Open Ports!

fingerprintx is a utility similar to httpx that also supports fingerprinting services like
*2023-3-31 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-156337.htm)
阅读量:32
收藏*

---

`fingerprintx` is a utility similar to [httpx](https://github.com/projectdiscovery/httpx "httpx") that also supports [fingerprinting](https://www.kitploit.com/search/label/Fingerprinting "fingerprinting") services like as RDP, SSH, MySQL, PostgreSQL, Kafka, etc. `fingerprintx` can be used alongside port scanners like [Naabu](https://github.com/projectdiscovery/naabu "Naabu") to [fingerprint](https://www.kitploit.com/search/label/Fingerprint "fingerprint") a set of ports identified during a port scan. For example, an engineer may wish to scan an IP range and then rapidly fingerprint the service running on all the discovered ports.

* Fast fingerprinting of exposed services
* Application layer service discovery
* Plays nicely with other [command line](https://www.kitploit.com/search/label/Command%20Line "command line") tools
* Automatic metadata collection from identified services

[ ](https://user-images.githubusercontent.com/69640071/193334167-8405dd50-f9bf-4386-b7b8-83255af41a8b.mov)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi_oZY--g6jUlxxsW0idLZTr0Pz5lrH8yDV6qIRkkDqo3trQHSVWo2YzEuKOvv8u6OBcx2_MRLwyYKypQH8mpigy4348bHijXPNATi-bxCrEvRGgSMXJoGCZoJzPUnsHuZYiot-QMwaEpGHTY32XuS10PMZ_BjxeajQpPKzYKv--y6xW12b0CGQ0oDzaw=w640-h522)](https://blogger.googleusercontent.com/img/a/AVvXsEi_oZY--g6jUlxxsW0idLZTr0Pz5lrH8yDV6qIRkkDqo3trQHSVWo2YzEuKOvv8u6OBcx2_MRLwyYKypQH8mpigy4348bHijXPNATi-bxCrEvRGgSMXJoGCZoJzPUnsHuZYiot-QMwaEpGHTY32XuS10PMZ_BjxeajQpPKzYKv--y6xW12b0CGQ0oDzaw)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgQYxwPjlJFqA7YpK51rfkEokLyRFWUIKR7hnzjMDKXK3BOdzqQ06WniAkiH73B6s5lM9RhnUczkiuqEcblZsGfRBeOp33Y6yDlWVcQbF90yCHJgOigTnSVz70chxInI7gEuHO1hWiVZGfa-chaPlJ5GC_qQ9hoRvT9Taea_Ky5iepcJz3pYbp83YQQ9w=w640-h236)](https://blogger.googleusercontent.com/img/a/AVvXsEgQYxwPjlJFqA7YpK51rfkEokLyRFWUIKR7hnzjMDKXK3BOdzqQ06WniAkiH73B6s5lM9RhnUczkiuqEcblZsGfRBeOp33Y6yDlWVcQbF90yCHJgOigTnSVz70chxInI7gEuHO1hWiVZGfa-chaPlJ5GC_qQ9hoRvT9Taea_Ky5iepcJz3pYbp83YQQ9w)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhaIh2C3COaq1fA7tOVw5BYwU6JzwnWVDD1TWkMAmaWs1HFIOtf_UVxP9vhRMlSe_dLsvd-pjNwB7kcgyqXoInsxEaXvkEY0Fp_6Vebbu4r35IQqNsNYJ38SL2B2mSm75DdBxeACD6fVplrqs9ucqMA3WN3DlMlfDFNo2S0wK9cP4a6o2swvZaFaDwrsw=w640-h466)](https://blogger.googleusercontent.com/img/a/AVvXsEhaIh2C3COaq1fA7tOVw5BYwU6JzwnWVDD1TWkMAmaWs1HFIOtf_UVxP9vhRMlSe_dLsvd-pjNwB7kcgyqXoInsxEaXvkEY0Fp_6Vebbu4r35IQqNsNYJ38SL2B2mSm75DdBxeACD6fVplrqs9ucqMA3WN3DlMlfDFNo2S0wK9cP4a6o2swvZaFaDwrsw)

## Supported Protocols:

| SERVICE | TRANSPORT | SERVICE | TRANSPORT |
| --- | --- | --- | --- |
| HTTP | TCP | REDIS | TCP |
| SSH | TCP | MQTT3 | TCP |
| MODBUS | TCP | VNC | TCP |
| TELNET | TCP | MQTT5 | TCP |
| FTP | TCP | RSYNC | TCP |
| SMB | TCP | RPC | TCP |
| DNS | TCP | OracleDB | TCP |
| SMTP | TCP | RTSP | TCP |
| PostgreSQL | TCP | MQTT5 | TCP (TLS) |
| RDP | TCP | HTTPS | TCP (TLS) |
| POP3 | TCP | SMTPS | TCP (TLS) |
| KAFKA | TCP | MQTT3 | TCP (TLS) |
| MySQL | TCP | RDP | TCP (TLS) |
| MSSQL | TCP | POP3S | TCP (TLS) |
| LDAP | TCP | LDAPS | TCP (TLS) |
| IMAP | TCP | IMAPS | TCP (TLS) |
| SNMP | UDP | Kafka | TCP (TLS) |
| OPENVPN | UDP | NETBIOS-NS | UDP |
| IPSEC | UDP | DHCP | UDP |
| STUN | UDP | NTP | UDP |
| DNS | UDP |  |  |

From Github

From source (go version > 1.18)

```
$ git clone [email protected]:praetorian-inc/fingerprintx.git
```

Docker

```
$ git clone [email protected]:praetorian-inc/fingerprintx.git
$ cd fingerprintx

# build
docker build -t fingerprintx .

# and run it
docker run --rm fingerprintx -h
docker run --rm fingerprintx -t praetorian.com:80 --json
```

The `-h` option will display all of the supported flags for `fingerprintx`.

```
Usage:
  fingerprintx [flags]
TARGET SPECIFICATION:
	Requires a host and port number or ip and port number. The port is assumed to be open.
	HOST:PORT or IP:PORT
EXAMPLES:
	fingerprintx -t praetorian.com:80
	fingerprintx -l input-file.txt
	fingerprintx --json -t praetorian.com:80,127.0.0.1:8000

Flags:
      --csv               output format in csv
  -f, --fast              fast mode
  -h, --help              help for fingerprintx
      --json              output format in json
  -l, --list string       input file containing targets
  -o, --output string     output file
  -t, --targets strings   target or comma separated target list
  -w, --timeout int       timeout (milliseconds) (default 500)
  -U, --udp               run UDP plugins
  -v, --verbose           verbose mode
```

The `fast` mode will only attempt to fingerprint the default service associated with that port for each target. For example, if `praetorian.com:8443` is the input, only the `https` plugin would be run. If `https` is not running on `praetorian.com:8443`, there will be NO output. Why do this? It's a quick way to fingerprint most of the services in a large list of hosts (think the [80/20 rule](https://en.wikipedia.org/wiki/Pareto_principle "80/20 rule")).

With one target:

```
$ fingerprintx -t 127.0.0.1:8000
http://127.0.0.1:8000
```

By default, the output is in the form: `SERVICE://HOST:PORT`. To get more detailed service output specify JSON with the `--json` flag:

```
$ fingerprintx -t 127.0.0.1:8000 --json
{"ip":"127.0.0.1","port":8000,"service":"http","transport":"tcp","metadata":{"responseHeaders":{"Content-Length":["1154"],"Content-Type":["text/html; charset=utf-8"],"Date":["Mon, 19 Sep 2022 18:23:18 GMT"],"Server":["SimpleHTTP/0.6 Python/3.10.6"]},"status":"200 OK","statusCode":200,"version":"SimpleHTTP/0.6 Python/3.10.6"}}
```

Pipe in output from another program (like [naabu](https://github.com/projectdiscovery/naabu "naabu")):

```
$ naabu 127.0.0.1 -silent 2>/dev/null | fingerprintx
http://127.0.0.1:8000
ftp://127.0.0.1:21
```

Run with an input file:

```
$ cat input.txt | fingerprintx
http://praetorian.com:80
telnet://telehack.com:23

# or if you prefer
$ fingerprintx -l input.txt
http://praetorian.com:80
telnet://telehack.com:23
```

With more metadata output:

Why Not Nmap?

[Nmap](https://nmap.org/ "Nmap") is the standard for network scanning. Why use `fingerprintx` instead of nmap? The main two reasons are:

* `fingerprintx` works smarter, not harder: the first plugin run against a server with port 8080 open is the http plugin. The default service approach cuts down scanning time in the best case. Most of the time the services running on port 80, 443, 22 are http, https, and ssh -- so that's what `fingerprintx` checks first.
* `fingerprintx` supports json output with the `--json` flag. Nmap supports numerous output options (normal, xml, grep), but they are often hard to parse and script appropriately. `fingerprintx` supports json output which eases integration with other tools in processing pipelines.

* Why do you have a `third_party` folder that imports the Go [cryptography](https://www.kitploit.com/search/label/Cryptography "cryptography") libraries?
  + Good question! The `ssh` fingerprinting module identifies the various cryptographic options supported by the server when collecting metadata during the handshake process. This makes use of a few unexported functions, which is why the Go cryptography libraries are included here with an [export.go file](https://github.com/praetorian-inc/fingerprintx/blob/main/third_party/cryptolib/ssh/export.go "export.go file").
* Fingerpr...