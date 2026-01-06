---
title: Risks of OOB Access via IP KVM Devices, (Mon, Jan 5th)
url: https://isc.sans.edu/diary/rss/32598
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-05
fetch_date: 2026-01-06T03:28:08.425059
---

# Risks of OOB Access via IP KVM Devices, (Mon, Jan 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32594)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Risks of OOB Access via IP KVM Devices](/forums/diary/Risks%2Bof%2BOOB%2BAccess%2Bvia%2BIP%2BKVM%2BDevices/32598/)

**Published**: 2026-01-05. **Last Updated**: 2026-01-05 17:33:50 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Risks%2Bof%2BOOB%2BAccess%2Bvia%2BIP%2BKVM%2BDevices/32598/#comments)

Recently, a new "breed" of IP-based KVM devices has been released. In the past, IP-based KVM devices required dedicated "server-grade" hardware using IPMI. They often cost several $100 per server, and are only available for specific systems that support the respective add-on cards. These cards are usually used to provide "Lights Out" access to servers, allowing a complete reboot and interaction with the pre-boot environment via simple web-based tools. In some cases, these IPMI tools can also be used via various enterprise/data center management tools.

The first "non-datacenter grade" device that provided similar capabilities to arbitrary systems was the "PIKVM"[1]. This device was based on a Raspberry Pi and combined various add-on cards (HDMI capture and USB device ports) to turn the Raspberry Pi into a remote access device. But even the PIKVM wasn't cheap. The hardware cost added up to around $100-$200. Fully assembled devices are available for around $300. While within reach for some hobbiists, it was still too expensive for many.

More recently, A chinese company, Sipeed, started offering a "NanoKVM" [2]. This device offers comparable capabilities for as low as $30 for a bare bones version ($60 for a more full-featured assembled version). The NanoKVM uses a very minimal RISC CPU and runs a stripped-down Linux variant providing just enough features to act as a servicable KVM. Consumer-oriented device manufacturers like GL-INET and others have released similar devices competing directly with the "NanoKVM", often offering some additional capabilities.

But turning these devices into a ubiquitous commodity has not come without problems.

Some have accused Sipeed of installing deliberate backdoors in their devices and delaying addressing security vulnerabilities. Ultimately, you should never deploy a device from a vendor you do not trust. I am not able to answer for you, but you need to figure out if this is a risk you are willing to take. A device like an IP KVM will always have direct access to your system, and it will be able to intercept keystrokes and video output. Many of the alleged vulnerabilities, like insecure firmware updates, are sadly very common in consumer devices. The NanoKVM will download firmware updates from Sipeed's servers in China. It will report some system status with these requests, which again is not that unusual. Sipeed offers other products (for example, camera systems) built around the same RISC board, explaining things like microphones and such that are located on the board. For more details, see the reports released by [Tom's Hardware in December](https://www.tomshardware.com/tech-industry/cyber-security/researcher-finds-undocumented-microphone-and-major-security-flaws-in-sipeed-nanokvm) [3].

Here are some tips to consider when installing one of these devices:

### 1. Do not expose the device to the Internet

Just like any administrative interface, do not expose the KVM to the internet. In particular, for KVMs, there is often a need to access them remotely. After all, you could reboot the system without KVM if you are at the same location as the system. Luckily, these KVMs often support Tailscale out of the box, or can support it with simple additional installs. Tailscale provides a simple VPN and NAT bypass solution to access systems even if your IP is dynamic. Any other VPN solution will work as well, but this usually requires you to operate some kind of "bastion host" at a cloud provider if you do not want to rely on the VPN offered by your firewall/router.

### 2. Set up strong authentication

PiKVM at least offers MFA via one-time passwords. I have not seen much else, but this is a reasonably good solution for this purpose. Just don't forget to enable it. NanoKVM considers MFA a "TODO Item". I don't think it has been implemented yet.

### 3. Configure TLS

Even running over a VPN, you should still use TLS to connect to your KVM to avoid MitM issues. This requires a valid certificate, either issued by an internal or public CA. I was able to install "certbot" without too much trouble on a PiKVM. If you are unable to automatically renew certificates, use an internal CA, which can issue certificates with a longer lifetime. But avoid self-signed certificates that are not recognized as valid by your browser.

NanoKVM specifically points out in its manual that the system is not quite able to support the full bitrate over TLS, and you may see some dropped frames. This is annoying but usually not a deal breaker for simple remote access during emergencies. It may be an issue if you use the KVM for more routine work, for example, if you attempt to use a laptop located in the US from an office in North Korea to work your remote job.

### 4. Logging

I wrote in the past about securing out-of-band access. One thing I see often missing, even with devices like console servers, is a decent logging or alerting solution to track use of the OOB access. At least log to a central syslog server. In some cases, I implemented little scripts that alert me of each login via SMS and e-mail.

### 5. Console Access Security

Once you are using a KVM to access your system, it is important to implement authentication on the system connected to the KVM. You should have the standard login and auto-logout/screen lock features enabled, just as you would on a system sitting in an office.

### 6. Test

OOB systems are usually used infrequently. It is important to verify that the system is working and configure alerts in case they are not. Sadly, it all too often happens that systems like this are "Dead" for a long time, something that is only noticed during the emergency when they are used. Some simple monitoring scripts should check that the system is operating correctly.

[1] https://pikvm.org
[2] https://sipeed.com
[3] https://www.tomshardware.com/tech-industry/cyber-security/researcher-finds-undocumented-microphone-and-major-security-flaws-in-sipeed-nanokvm

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [oob access](/tag.html?tag=oob access) [remote work](/tag.html?tag=remote work) [kvm](/tag.html?tag=kvm) [NanoKVM](/tag.html?tag=NanoKVM) [PiKVM](/tag.html?tag=PiKVM)

[0 comment(s)](/diary/Risks%2Bof%2BOOB%2BAccess%2Bvia%2BIP%2BKVM%2BDevices/32598/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32594)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  +...