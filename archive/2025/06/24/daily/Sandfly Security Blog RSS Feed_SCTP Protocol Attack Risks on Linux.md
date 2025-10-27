---
title: SCTP Protocol Attack Risks on Linux
url: https://sandflysecurity.com/blog/sctp-protocol-attack-risks-on-linux
source: Sandfly Security Blog RSS Feed
date: 2025-06-24
fetch_date: 2025-10-06T22:53:38.172980
---

# SCTP Protocol Attack Risks on Linux

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# SCTP Protocol Attack Risks on Linux

23 June 2025

Malware

The SCTP protocol on Linux provides reliable communications largely for the telecommunications sector. While it has legitimate uses, it also can be a stealthy way to access Linux and avoid detection. In this article we're going to demonstrate a simple SCTP backdoor and how it can be missed by security teams. Then, we'll show you how to look for this kind of activity.

### SCTP Enabled by Default

As discussed, SCTP is a protocol mainly used for telcos. It provides reliable transport like TCP, but is not TCP. As a result, many teams may not be monitoring for this kind of traffic and, even worse, packet filters can be mis-configured meaning it can sometimes bypass firewalls.

Further, SCTP is enabled on **heaps** of Linux systems by default but it's rarely used. This is a recipe for mischief. The big thing to understand is that if you are not telco, seeing SCTP traffic on your network may be a sign of trouble. If you are a telco, malicious SCTP traffic can easily blend in and likewise needs monitoring.

### SCTP Backdoor Example

For this article, we have a simple SCTP backdoor using the *socat* command line program. The attack is carried over SCTP and again may often go unnoticed by security teams not specifically monitoring for traffic using this protocol. For our attack we simply run the *id* command and then disconnect. In actual use the *socat* command (or other backdoors) would connect the attacker to a full-blown system shell.

SCTP backdoors are well-known and easily found online. The simple one we'll use is the *socat* command:

*socat SCTP-Listen:1177, fork EXEC:/usr/bin/id*

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SCTP backdoor on Linux.](https://www.datocms-assets.com/56687/1750706871-socat-exec-usr-bin-id-raw.png?auto=format&dpr=2&q=60&w=920 "SCTP backdoor on Linux.")

Here we see the response if you connect to the backdoor remotely with SCTP. It simply shows the output of the *id* command and disconnects. In this case, it is running as the *root* user.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SCTP backdoor response on Linux.](https://www.datocms-assets.com/56687/1750706892-socat-sctp-bin-id-output-raw.png?auto=format&dpr=2&q=60&w=920 "SCTP backdoor response on Linux.")

### Missing SCTP Sockets with Common Commands

If you run Linux commands like *netstat* or *ss* with common flags, you won't see this kind of port. Below we see the the command *ss -ltun* to list all listening TCP and UDP ports. Notice that our SCTP backdoor is not there. You need to be explicit sometimes when using these commands to make sure all listening sockets are shown.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SCTP sockets will not show unless you look for them.](https://www.datocms-assets.com/56687/1750706913-sctp-ss-ltun-no-sctp-port-shown-listening-raw.png?auto=format&dpr=2&q=60&w=920 "SCTP sockets will not show unless you look for them.")

You can use *ss* with the -l option to list all listening sockets, but this will give you a lot of data to parse. A shortcut is *ss -lStu* which specifically includes SCTP along with TCP/UDP ports that are listening like this:

*ss -lStu*

If you want to see what process owns each socket, use the -p option like this:

*ss -lStup*

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Finding SCTP listening sockets on Linux.](https://www.datocms-assets.com/56687/1750706929-sctp-ss-lstu.png?auto=format&dpr=2&q=60&w=920 "Finding SCTP listening sockets on Linux.")

### Checking if SCTP is Enabled

Since many Linux systems ship with SCTP enabled, you may want to know how to check if your systems have it turned on. First, you can check loaded kernel modules using this command:

*lsmod | grep sctp*

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Using lsmod to see loaded SCTP protocol kernel modules.](https://www.datocms-assets.com/56687/1750706947-sctp-enabled-lsmod.png?auto=format&dpr=2&q=60&w=920 "Using lsmod to see loaded SCTP protocol kernel modules.")

Next is to check */proc/net/protocols* and see if it is listed with this command:

*cat /proc/net/protocols*

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![The /proc/net/protocols file shows all protocols enabled in the Linux kernel.](https://www.datocms-assets.com/56687/1750706980-sctp-proc-net-protocols.png?auto=format&dpr=2&q=60&w=920 "The /proc/net/protocols file shows all protocols enabled in the Linux kernel.")

Finally, you can check */proc/net/sctp/eps* and see what sockets are using the protocol. It will need some interpretation, but basically if you see something here but not in system tools, then something may be hiding.

*cat /proc/net/sctp/eps*

This is what our sample backdoor looked like, you can see the reference to port 1177 along with the *inode* which can be used to find out what process is using the socket:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![/proc/net/sctp/eps shows all open SCTP sessions on a Linux host.](https://www.datocms-assets.com/56687/1750706993-sctp-proc-net-sctp-eps-raw.png?auto=format&dpr=2&q=60&w=920 "/proc/net/sctp/eps shows all open SCTP sessions on a Linux host.")

### Disabling SCTP

If you want to disable SCTP on your systems, you'll need to blacklist the module and reboot. Make sure your gold image builds for Virtual Machines (VMs) also have it disabled. There are instructions online on how to do this. Many cloud images have SCTP enabled by default so this issue is very common. If you don't need SCTP, it is a good idea to disable it in your builds.

### Find Suspicious SCTP Processes Automatically

By default [Sandfly Security](https://www.linkedin.com/company/sandfly/) searches for SCTP processes on Linux as they are very unusual to find outside of specific industry use cases (again, telcos). We'll alert you immediately if we see any running. This type of alert would likely be malicious for most networks.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly agentlessly hunts for suspicious SCTP processes on Linux.](https://www.datocms-assets.com/56687/1750707009-socat-alert.png?auto=format&dpr=2&q=60&w=920 "Sandfly agentlessly hunts for suspicious SCTP processes on Linux.")

Again, if you're not a telco you probably shouldn't see this. Sandfly will also flag any SCTP processes that have unusual features like deleted binaries, unusual operating directories, and more. This can help cover those users that do need to run SCTP and need to keep an eye on things.

### Watch SCTP for Abuse

SCTP is an interesting protocol that needs monitoring. It's as reliable as TCP, but the lack of awareness and default availability makes it a prime target for attackers looking to operate under the radar on Linux. Keep an eye on this protocol on your network and your endpoints. It makes a fine backdoor and is ripe for abuse.

If you are concerned about how SCTP may be abused on your Linux hosts, check out [Sandfly Security](https://sandflysecurity.com/get-sandfly) to get a free license for our agentless Linux security platform. Sandfly can find SCTP abuse and thousands of other threats against Linux without the risk and performance impact of endpoint agents.

---

Post Tags:

[Malware](/blog/tag/malware)[Linux Security](/blog/tag/linux-security)[Linux Forensics](/blog/tag/linux-forensics)[Rootkits](/blog/tag/rootkits)

Share this post:

[← Return to Blog](/blog)

---

#### Contact Us

---

+64 3 3792313[4 Ash Street Christchurch, New Zealand 8011](https://goo.gl/maps/9cFto1o6GNa9RK6S9)

#### Connect With Us

---

#### Product Navigation

---

* [Threat ...