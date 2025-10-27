---
title: Multiple Vulnerabilities in Proxmox VE & Proxmox Mail Gateway
url: https://starlabs.sg/blog/2022/12-multiple-vulnerabilites-in-proxmox-ve--proxmox-mail-gateway/
source: Blogs on STAR Labs
date: 2022-12-03
fetch_date: 2025-10-04T00:23:07.408516
---

# Multiple Vulnerabilities in Proxmox VE & Proxmox Mail Gateway

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Multiple Vulnerabilities in Proxmox VE & Proxmox Mail Gateway

December 2, 2022 · 13 min · Li JianTao (@cursered)

Table of Contents

* [Background](#background)
* [Locating the source code](#locating-the-source-code)
* [Setting up debug environment](#setting-up-debug-environment)
  + [In IDEA](#in-idea)
  + [On the PVE server](#on-the-pve-server)
* [Bug 0x01: Post-auth XSS in API inspector](#bug-0x01-post-auth-xss-in-api-inspector)
  + [Further Analysis](#further-analysis)
  + [Impacts, attack conditions & constraints](#impacts-attack-conditions--constraints)
  + [Patch](#patch)
* [Bug 0x02: CRLF injection in response headers](#bug-0x02-crlf-injection-in-response-headers)
  + [Impacts, attack conditions & constraints](#impacts-attack-conditions--constraints-1)
  + [Patch](#patch-1)
* [Bug 0x03: Post-auth SSRF + LFI + Privilege Escalation](#bug-0x03-post-auth-ssrf--lfi--privilege-escalation)
  + [SSRF](#ssrf)
  + [Arbitrary file read](#arbitrary-file-read)
  + [Privilege escalation in PMG via unsecured backup file](#privilege-escalation-in-pmg-via-unsecured-backup-file)
    - [Proof-of-concept](#proof-of-concept)
  + [Patch](#patch-2)
* [Timeline](#timeline)

## Background[#](#background)

Proxmox Virtual Environment (Proxmox VE or PVE) is an open-source type-1 hypervisor. It includes a web-based management interface programmed in Perl. Another Proxmox product written in Perl, Proxmox Mail Gateway (PMG), comes with a similar web management interface. They share some of the codebases.

In this article, I will introduce how to debug PVE’s web service step-by-step and analyse three bugs I have found in PVE and PMG.

**[UPDATE] This is a quick and minor update to this blog post. MITRE email back to us on 9th December 2022 assigned CVE-2022-35507 & CVE-2022-35508 for the remaining 2 bugs**

Greatly appreciate MITRE for getting back to us.

## Locating the source code[#](#locating-the-source-code)

PVE is a Debian-based Linux distribution. The ISO installer is available at [their website](https://www.proxmox.com/en/downloads). Do note that if you would like to reproduce any of the bugs in this article, please use “Proxmox VE 7.2 ISO Installer” updated on 04 May 2022, which does not include the patches unless you run `apt update` manually.

In a default installation, the web service should listen on port 8006.

![](/blog/2022/images/01.png)

With a few commands, it is not difficult to figure out that the scripts of the web service are located in `/usr/share/perl5/`:

```
ss -natlp | grep 8006           # Which process is listening on port 8006
which pveproxy                  # Where is the executable
head `which pveproxy`           # Is it an ELF, a shell script or something else?
find /usr -name "SafeSyslog*"   # Where is the "SafeSyslog" module used by pveproxy?
```

![](/blog/2022/images/02.png)

## Setting up debug environment[#](#setting-up-debug-environment)

I choose IntelliJ IDEA and its Perl plugin for debugging. Here are the steps to set it up:

### In IDEA[#](#in-idea)

1. Pack `/usr/share/perl5/` on the PVE server and open it as Project in IDEA
2. Go to *Settings > Plugins* and install *Perl* plugin
3. Go to *Settings > Languages & Frameworks > Perl5*,
   * Select a *Perl5 Interpreter* (both *Local* and *Docker* would work), then
   * Set *Target version* to v5.32, the same `perl --version` as PVE uses
4. In Project window (Alt+1), right click on `perl5` directory, *Mark Directory as > Perl5 Library Root*.

At this stage, you should have correct syntax highlighting and dependency resolving in IDEA.

![](/blog/2022/images/03.png)

5. Go to *Run > Edit Configurations*, add a new “Perl Remote Debugging” entry and save:
   * Name: PVE remote
   * Remote project root: `/usr/share/perl5`
   * Connection mode: `IDE connects to the perl process`
   * Server host: your PVE server IP
   * Server port: 12345

![](/blog/2022/images/04.png)

### On the PVE server[#](#on-the-pve-server)

Run these commands to install the required debug tools:

```
apt install gcc make
cpan Devel::Camelcadedb
```

All set. To start a debug session, click **`Run > Debug 'PVE remote'`** in IDEA and run `PERL5_DEBUG_HOST=<your PVE server IP> PERL5_DEBUG_PORT=12345 PERL5_DEBUG_ROLE=server perl -T -d:Camelcadedb /usr/bin/pveproxy start -debug` on the server. If everything goes well, the debugger should break at line 330 of `SSL.pm` by default, as shown in the image below.

![](/blog/2022/images/05.png)

## Bug 0x01: Post-auth XSS in API inspector[#](#bug-0x01-post-auth-xss-in-api-inspector)

By logging in to the web interface, it can be observed that a lot of requests are sent to endpoints under the path `/api2/json/`. Usually, `json` after `/api` indicates the format the response data is in, and the server might support various formats for different purposes. For example, `xml` might be implemented for RPC calls, `jsonp` for cross-origin `<script>` tags, or `html` for setting `innerHTML`. In PVE, if we change `json` to `html`, the server will return an “API Inspector” page containing the json result:

![](/blog/2022/images/06.png)

Further testing shows that the server does not properly escape user’s input. If we visit a non-existent API endpoint, the request path will be reflected in the `href` attribute of an `<a>` tag. As such, an attacker can inject HTML tags to achieve reflected cross-site scripting.

![](/blog/2022/images/07.png)

### Further Analysis[#](#further-analysis)

The function `handle_request` at `perl5/PVE/APIServer/AnyEvent.pm` line 1100 is our entry point. If the request path starts with `/api2`, it will pass the request on to function `handle_api2_request`.

![](/blog/2022/images/08.png)

Stepping into `handle_api2_request`, we can see at line 865 the variables `$rel_uri` and `$format` are extracted from the rest of the request path by a regex. Then function `PVE::APIServer::Formatter::get_formatter` is called to get a “formatter” for generating the response.
![](/blog/2022/images/09.png)

Later on, the `$formatter` is called at line 946. When generating the “breadcrumb” HTML of the navigation bar, the request path is directly concatenated to the `href` attribute of the `<a>` tag.

![](/blog/2022/images/10.png)

![](/blog/2022/images/11.png)

### Impacts, attack conditions & constraints[#](#impacts-attack-conditions--constraints)

Since the authentication cookie `PVEAuthCookie` is set with the `Session` attribute, successful exploitation requires the victim to be logged in to the web interface in the same browser session before he visits the malicious link.

An attacker can access every functionality in the web interface by executing malicious JavaScript code. One of the features is to execute shell commands. Here is a video demonstrating a possible attack scenario. In the video, the victim logged in to PVE web UI, and then visited a link. A reverse shell of the PVE host was spawned on the attacker’s machine.

### Patch[#](#patch)

This vulnerability is [patched](https://git.proxmox.com/?p=pve-http-server.git;a=commitdiff;h=00661f1223b7c0afffa64e1d91f5e018b985f762) by encoding user inputs to HTML entities in `pve-http-server` version `4.1-2`.

## Bug 0x02: CRLF injection in response headers[#](#bug-0x02-crlf-injection-in-response-headers)

While handling HTTP requests, if there is any error, the PVE server will write the error message in the status line of the response.

![](/blog/2022/images/12.png)

The corresponding code is located ...