---
title: Sandfly 2.5.0 – Higher Performance, SSH Key Certificates and More Linux Forensics
url: https://sandflysecurity.com/blog/sandfly-2-5-0-higher-performance-ssh-key-certificates-and-more-linux-forensics
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:28:00.468787
---

# Sandfly 2.5.0 – Higher Performance, SSH Key Certificates and More Linux Forensics

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.5.0 – Higher Performance, SSH Key Certificates and More Linux Forensics

17 February 2020

Product Update

Sandfly 2.5.0 has been released and features a 5-10X boost in investigation speed, lower CPU impacts during investigations and support for SSH key certificates. Of course, we’ve added more agentless Linux intrusion detection and threat hunting methods on top of this.

## Higher Performance Investigations and Less Bandwidth

This update features big upgrades to scanning performance. Host investigations are anywhere from 5-10X faster. We also have enabled data compression to reduce network overhead by up to 90% in many cases. Sandfly can operate efficiently even in high latency and low bandwidth monitoring applications without tying up critical system resources.

The overall result is that Sandfly can spot check for security problems agentlessly on Linux systems often in under 15 seconds and then vanish without a trace. Our system was designed to be lightweight and low impact, and now it’s even better.

## SSH Key Certificates Support

We have added in support for SSH key certificates. SSH certificates are a great way for organizations to do SSH key management vs. using private keys alone. There are a variety of advantages to using SSH certificates and we recommend that customers investigate this approach. These articles below describe how to use SSH certificates for authentication:

[Scalable and Secure Access with SSH](https://engineering.fb.com/security/scalable-and-secure-access-with-ssh/)

[How to Harden SSH with Identities and Credentials](https://ef.gy/hardening-ssh)

If you want to add a credential in Sandfly to use SSH certificates, you simply put in your private key as usual, and the certificate to go along with it in the box below. Once that’s done, the certificate authentication will handle the rest.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Private Key and Certificate Credentials](https://www.datocms-assets.com/56687/1635216294-ssh-host-credentials-1.png?auto=format&dpr=2&q=60&w=920 "SSH Private Key and Certificate Credentials")

**Note that if you use certificates that expire you will need to update the credentials on an on-going basis for Sandfly to authenticate and work.** It is easy to rotate keys with Sandfly using the [Sandfly REST API Credentials Endpoint to automate the credential renewal process](https://docs.sandflysecurity.com/v2.5.0/reference#credentials-1). Please contact us if you need help using this new feature.

## Enhanced Linux Network Connection Forensics

We have enhanced forensics reporting for Linux network connections. We now break out each connection by protocol type such as TCP, UDP, ICMP, TCPv6, UDPv6, ICMPv6, and raw sockets. You can now search for local or remote addresses on a connection or local or remote network ports. You can also search for listening connections, established connections or any connection that is operating which is to say it is listening or established. Here are some ideas on how to use these new features:

1. Search for hosts that are connected to a specific IP address or IP address range. Networks often lack visibility to see what hosts are talking to who internally. In fact, many networks have a hard time seeing even if a host is talking to a specific IP outside the network. If you are investigating a compromise you can now quickly look for connections without needing to rely on spotty or missing network monitoring in your organization. Just go ask the hosts and they will tell you with an agentless query.
2. You can search for network processes listening on or communicating with another system on a specific network port. For instance, if you are chasing down a malicious Command and Control (C2) malware that listens on TCP port 1763, you can quickly query your hosts and find any process that is doing that in seconds.
3. Like the above, you can also see if a host is communicating on a network port you are investigating. You can quickly find network connections to any network port across your hosts. Again, if you know outbound traffic connected to port 1763 is malicious, you can quickly look on all your endpoints for that information without needing to rely on network monitoring to be in place.

You can quickly write custom Sandfly threat modules to look for either suspicious IPs or suspicious ports as in the examples below. In this example we are looking for any program operating on TCP ports 4444, 31337 or 1337:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Custom Sandfly to look for suspicious TCP ports in use.](https://www.datocms-assets.com/56687/1635216306-process-local-tcp-port-operating.png?auto=format&dpr=2&q=60&w=920 "Custom Sandfly to look for suspicious TCP ports in use.")

In the next example we are looking for a remote connection to an address in the 10.1.1.\* range on the TCP protocol. This is very useful when tracking down a known suspicious IP address to see if any hosts are connected to it actively:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Remote IP Address on TCP Port Search](https://www.datocms-assets.com/56687/1635216315-process-remote-tcp-ip-address.png?auto=format&dpr=2&q=60&w=920 "Remote IP Address on TCP Port Search")

Here is what the output would look like if we found a network connection that matches our search REGEX above for an IP address:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Process With Remote TCP Connection](https://www.datocms-assets.com/56687/1635216323-process-remote-ip-address-active.png?auto=format&dpr=2&q=60&w=920 "Process With Remote TCP Connection")

We have added search templates to make searching for any kind of connection easier:

* Search for TCP, UDP, ICMP and raw sockets with connections on IPv4 or IPv6 addresses of your choice.
* Search for local IP addresses on an interface listening or operating with a connection.
* Search for a remote IP address on any port or interface that is connected to the host.
* Wildcard searches for IP addresses if you are working with a range of addresses you need to hunt for on your network.

All of the above parameters are searchable combined or by themselves using the Sandfly custom JSON format shown above. Like all custom Sandfly checks, you can turn your hunting parameters into security signatures that are run automatically 24 hours a day. This can be used to help spot if any customized threats suddenly show up on your network that are of interest to your security team.

## Enhanced Linux Anti-Forensics Detection

In addition to all of the above, we have enhanced our anti-forensics detection. We now cover more hiding methods in the following areas:

* Enhanced login and logout anti-forensics detection.
* Enhanced system-wide anti-forensics detection.

## Enhanced Linux Backdoor and Nmap Port Scanning Detection

We have added in new methods to find more kinds of backdoors from *telnet* to *Python* scripts. We added methods to flag the *nmap* port scanner, and *nmap* processes masquerading under a different name. While *nmap* can be a legitimate tool for port scanning, if you don’t know why it’s running on a host you control it is a good idea to find out who is doing it and why. If *nmap* is running on a host but someone has renamed it like below, then it’s a **really** good idea to find out who is doing it and why.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![nmap Process Masquerading Attack](https://www.datocms-assets.com/56687/1635216332-nmap-process-masquerading.png?auto=format&dpr=2&q=60&w=920 "nmap Process Masquerading Attack")

## How to Upgrade Sandfly

Sandfly is easy to upgrade. Please ...