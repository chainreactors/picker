---
title: PolarProxy 2.0 Released
url: https://www.netresec.com/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released
source: NETRESEC Network Security Blog
date: 2026-05-18
fetch_date: 2026-05-19T06:04:40.510074
---

# PolarProxy 2.0 Released

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

Monday, 18 May 2026 07:01:00 (UTC/GMT)

## [PolarProxy 2.0 Released](/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released)

![PolarProxy 2.0](https://media.netresec.com/images/PolarProxy_2-0_2000x2000.webp)

A new major release of [PolarProxy](https://www.netresec.com/?page=PolarProxy) is out with a self-contained single-file binary, expanded platform support (musl/ARM), and improved container and service plumbing.

PolarProxy is a transparent TLS/SSL inspection proxy built for incident responders, malware analysts and security researchers. It decrypts and re‑encrypts TLS traffic and writes decrypted sessions to PCAP for analysis in Wireshark or an IDS.

**What's new**

* Packaged as a self-contained, single-file binary for easier installation and management.
* Improved HTTP proxy server: support for unencrypted HTTP traffic with --nontls allow
* Upgraded runtime: migrated from .NET 8 to .NET 10.
* More supported platforms: Linux musl (Alpine) builds for ARM and ARM64 architectures added.
* Simplified container deployment: Dockerfile and docker-compose.yml included with all musl/Alpine releases.
* Service installer for Linux: systemd unit (polarproxy.service) and install script included in non-musl Linux releases.
* New runtime flags:
  + --tlstimeout <seconds> — sets a TLS handshake/authentication timeout.
  + --cutoff <bytes> — limits PCAP output to the specified number of bytes per flow.

**Why this release matters**

* Self-contained single binary simplifies deployment and maintenance. This is a breaking change, at least for container/pod deployments, so make sure to validate your deployment before rolling out the new 2.0 release to production.
* The .NET 10 upgrade brings improved runtime performance and security updates.
* Better container support with musl/Alpine build for ARM and ARM64 in addition to existing x64 builds, and simplified container deployments with included config files.
* The new timeout for TLS handshakes improves error handling of connections to broken TLS middleboxes and extremely slow web servers.
* The flow cutoff CLI option enables users to prevent large downloads from filling up disk volumes. This setting also limits the per-flow size of decrypted traffic that is made available through [PCAP-over-IP](https://netresec.com/?b=228fddf).

**Quick start for Linux (regular user)**

1. Download the appropriate tar archive for your platform (see [download links](https://www.netresec.com/?page=PolarProxy)).
2. Create directory:

   mkdir ~/PolarProxy
3. Change directory:

   cd ~/PolarProxy/
4. Extract the archive:

   tar -xzf ~/Downloads/PolarProxy\_2.0.0\_linux-x64.tar.gz
5. Create log directory:

   sudo mkdir -p /var/log/polarproxy
6. Change log dir owner:

   sudo chown "$USER" /var/log/polarproxy
7. Start PolarProxy:

   ./PolarProxy -p 10443,80,443 --socks 1080 --httpconnect 8080 --nontls allow --certhttp 10080 -x /var/log/polarproxy/polarproxy.cer -f /var/log/polarproxy/proxyflows.log --pcapoverip 0.0.0.0:57012 -o /var/log/polarproxy/ -v

**Quick start for Linux with systemd**

1. Download the appropriate tar archive for your platform (see [download links](https://www.netresec.com/?page=PolarProxy)).
2. Create and change into a new temp directory:

   cd $(mktemp -d)
3. Extract the archive:

   tar -xzf ~/Downloads/PolarProxy\_2.0.0\_linux-x64.tar.gz
4. Run install script:

   sudo ./install-polarproxy-service.sh
5. Show service status:

   systemctl status polarproxy.service
6. Show logs:

   sudo journalctl -t polarproxy

The install script creates a system user “polarproxy”, a systemd service called “polarproxy.service”, and then starts that service. You are, of course, free to modify the installation script and polarproxy.service file if you want a different configuration.

**Quick start for Alpine Docker**

1. Download the appropriate Linux musl archive for your platform (see [download links](https://www.netresec.com/?page=PolarProxy)).
2. Create and change into a new temp directory:

   cd $(mktemp -d)
3. Extract:

   tar -xzf ~/Downloads/PolarProxy\_2.0.0\_linux-musl-x64.tar.gz
4. Deploy to docker:

   sudo docker compose up -d --build
5. Show container status:

   sudo docker ps --filter "name=polarproxy"
6. Show logs:

   sudo docker logs polarproxy

The docker-compose.yml will create a container named “polarproxy” with a non-root user called “polarproxy” without a password.

**Listening services in quick start examples**

All three quick start deployments above expose the following TCP ports:

* 10443 — Transparent TLS proxy
* 1080 — SOCKS server
* 8080 — HTTP Proxy server
* 10080 — Web server hosting the root CA certificate
* 57012 — [PCAP-over-IP](https://netresec.com/?b=228fddf) server providing decrypted traffic

A port forwarding (DNAT) firewall rule must be configured, which redirects TCP 443 traffic to the transparent TLS proxy, in order to run PolarProxy as a transparent TLS proxy that intercepts outgoing TLS traffic.
See the Routing Option alternatives on the [official PolarProxy page](https://www.netresec.com/?page=PolarProxy) for more details.

Decrypted traffic from all proxy services is accessible through the [PCAP-over-IP](https://netresec.com/?b=228fddf) service on TCP port 57012. They are also written to PCAP files in /var/log/polarproxy/.

**Test your deployment**

Download PolarProxy’s root CA certificate:

curl -L -o /tmp/polarproxy.cer http://localhost:10080

Convert to PEM format:

openssl x509 -inform DER -in /tmp/polarproxy.cer -out /tmp/pp.crt

Monitor decrypted traffic via [PCAP-over-IP](https://netresec.com/?b=228fddf) in one terminal/shell:

nc 127.0.0.1 57012 | tcpdump -Anr -

Test transparent proxy in another terminal/shell:

curl --cacert /tmp/pp.crt --connect-to www.netresec.com:443:127.0.0.1:10443 https://www.netresec.com/

Test SOCKS proxy:

curl --cacert /tmp/pp.crt --socks5 127.0.0.1 https://www.netresec.com/

Test HTTP proxy:

curl --cacert /tmp/pp.crt --proxy 127.0.0.1:8080 https://www.netresec.com/

**Downloads and docs**

See the [PolarProxy product page](https://www.netresec.com/?page=PolarProxy) for downloads, full command-line options, sample configurations etc.

![TLS added and removed here](https://www.netresec.com/images/PolarProxy-flow-chart_TLS-added-and-removed_680x234.png)

Feel free to [share feedback or report bugs](https://www.netresec.com/?page=AboutNetresec) about PolarProxy.

Posted by Erik Hjelmvik on Monday, 18 May 2026 07:01:00 (UTC/GMT)

Tags:
#[PolarProxy](/?page=Blog&tag=PolarProxy)​
#[systemd](/?page=Blog&tag=systemd)​
#[cutoff](/?page=Blog&tag=cutoff)​

Short URL:
<https://netresec.com/?b=2658a26>

### Recent Posts

» [PolarProxy 2.0 Released](/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released)

» [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

» [FlowCarp Identifies Protocols](/?page=Blog&month=2026-05&post=FlowCarp-Identifies-Protocols)

» [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

» [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

» [Decoding malware C2 with CyberChef](/?page=Blog&month=2026-01&post=Decoding-malware-C2-with-CyberChef)

» [Latrodectus BackConnect](/?page=Blog&month=2025-12&post=Latrodectus-BackConnect)

» [NetworkMiner 3.1 Released](/?page=Blog&month=2025-12&post=NetworkMiner-3-1-Released)

### Blog Archive

» [2026 Blog Posts](?page=Blog&year=2026)

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [...