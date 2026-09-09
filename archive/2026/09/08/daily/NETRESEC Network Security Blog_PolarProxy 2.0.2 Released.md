---
title: PolarProxy 2.0.2 Released
url: https://www.netresec.com/?page=Blog&month=2026-09&post=PolarProxy-2-0-2-Released
source: NETRESEC Network Security Blog
date: 2026-09-08
fetch_date: 2026-09-09T06:56:50.559363
---

# PolarProxy 2.0.2 Released

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

Tuesday, 08 September 2026 12:35:00 (UTC/GMT)

## [PolarProxy 2.0.2 Released](/?page=Blog&month=2026-09&post=PolarProxy-2-0-2-Released)

![PolarProxy 2.0.2](https://media.netresec.com/images/PolarProxy_2-0-2_2000x2000.webp)

A few more handy features have been added to [PolarProxy](https://www.netresec.com/?page=PolarProxy), our TLS inspection proxy. PolarProxy can now tunnel outgoing connections through SOCKS proxies and supports environment variables as an alternative to command-line arguments. PolarProxy also ships with a software bill of materials (SBOM), providing greater transparency into its dependencies.

**SOCKS Proxy Client**

PolarProxy has been able to accept incoming connections over SOCKS [since version 0.9](https://netresec.com/?b=221953b). With this release, PolarProxy can also send outgoing connections through another SOCKS proxy server. Both SOCKS4 and SOCKS5 are supported. This feature enables many use cases, including inspecting your own HTTPS requests before sending them through the Tor network.

The following command starts a SOCKS proxy on TCP port 1080 and forwards all traffic to a Tor SOCKS5 proxy listening on TCP port 9050. A copy of the traffic transmitted through the tunnel, including decrypted TLS traffic, is made available through a PCAP-over-IP service on TCP port 57012.

PolarProxy --socks 1080 --connect socks5:127.0.0.1:9050 --nontls allow --pcapoverip 57012 --writeall

Note
PolarProxy normally serves only decrypted TLS traffic over PCAP-over-IP. The --writeall option extends the PCAP output to include all proxied traffic.

PolarProxy’s SOCKS client can also be used as a protocol converter. For example, incoming HTTP proxy and HAProxy connections can be converted into SOCKS proxy requests with the following command:

PolarProxy --httpconnect 8080 --haproxy 7654 --nontls allow --connect socks5:localhost:1080

Pro-Tip
Use PolarProxy’s --bypass switch if you want to use PolarProxy only as a protocol converter, without decrypting and re-encrypting TLS traffic.

**Simplified and Flexible Deployments**

PolarProxy 2.0.2 enables users to supply configuration settings through environment variables as an alternative to command-line arguments. PolarProxy environment variables use uppercase names with the PP\_ prefix. For example, the PP\_SOCKS environment variable corresponds to the --socks command-line option.

Pro-Tip
Use PolarProxy’s --helpenv switch to print a list of supported environment variables.

Environment variables provide a clean separation between an application and its configuration. This is particularly useful when running PolarProxy with systemd, Docker, Podman, Kubernetes, Helm or other orchestration tools. They can simplify deployments and make ongoing configuration changes more flexible.

PolarProxy 2.0.2 also ships with a docker-compose.yml (musl builds only) or a systemd unit file (non-musl Linux builds), depending on which target the downloaded release is built for. These files simplify deployment. A docker container can, for example, be deployed by running:

curl https://www.netresec.com/?download=PolarProxy\_linux-musl-x64 | tar -xzf -
# Modify polarproxy.env
docker compose up -d

A systemd service can be deployed with:

curl https://www.netresec.com/?download=PolarProxy | tar -xzf -
# Modify polarproxy.env
./install-polarproxy-service.sh

**More Timeouts**

PolarProxy 2.0.2 adds a new type of timeout that allows connections to be closed when the client or server has been idle for a specified period. Closing unused “dead” connections helps maintain a clean state and prevents zombie connections from lingering in PolarProxy or in clients connected through PolarProxy.

PolarProxy can now close connections based on timeouts at the following communication stages:

* TCP handshake: --timeout <seconds>
* TLS handshake: --tlstimeout <seconds>
* Idle client connection: --idletimeoutclient <seconds>
* Idle server connection: --idletimeoutserver <seconds>

The default timeout for TCP and TLS handshakes is 30 seconds, while the idle timeout is disabled by default.

**SBOM: Software Bill of Materials**

PolarProxy 2.0.2 includes a software bill of materials (SBOM), providing an overview of the components, libraries, and dependencies included in PolarProxy.

The SBOM supports software transparency and helps users assess their software supply chain. The file shipped with PolarProxy uses the SPDX format and is named polarproxy.spdx.json.

PolarProxy's SBOM can be integrated into your security and compliance workflows using standard vulnerability scanning tools. For more info about SBOMs, refer to NIST's [Software Supply Chain Security Guidance](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-supply-chain-security-guidance-20).

**Downloading and Installing PolarProxy**

For more information on how to download and deploy PolarProxy in your environment, see the [official PolarProxy product page](https://www.netresec.com/?page=PolarProxy).

Posted by Erik Hjelmvik on Tuesday, 08 September 2026 12:35:00 (UTC/GMT)

Tags:
#[PolarProxy](/?page=Blog&tag=PolarProxy)​
#[SOCKS](/?page=Blog&tag=SOCKS)​
#[Tor](/?page=Blog&tag=Tor)​

Short URL:
<https://netresec.com/?b=2692ad6>

### Recent Posts

» [PolarProxy 2.0.2 Released](/?page=Blog&month=2026-09&post=PolarProxy-2-0-2-Released)

» [OT Networks Still Need Monitoring](/?page=Blog&month=2026-08&post=OT-Networks-Still-Need-Monitoring)

» [CNCMachineRMS C2 Protocol](/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol)

» [PureLogs, PureRAT and misleading zgRAT](/?page=Blog&month=2026-07&post=PureLogs-PureRAT-and-misleading-zgRAT)

» [Ping32 RMM and ValleyRAT](/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT)

» [Maximizing IOC Impact](/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact)

» [PolarProxy 2.0.1 Released](/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released)

» [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

### Blog Archive

» [2026 Blog Posts](?page=Blog&year=2026)

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)