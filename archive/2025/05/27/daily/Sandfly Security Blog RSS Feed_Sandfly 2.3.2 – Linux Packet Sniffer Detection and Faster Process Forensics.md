---
title: Sandfly 2.3.2 – Linux Packet Sniffer Detection and Faster Process Forensics
url: https://sandflysecurity.com/blog/sandfly-2-3-2-linux-packet-sniffer-detection-and-faster-process-forensics
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:28:02.948613
---

# Sandfly 2.3.2 – Linux Packet Sniffer Detection and Faster Process Forensics

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.3.2 – Linux Packet Sniffer Detection and Faster Process Forensics

11 November 2019

Product Update

Sandfly 2.3.2 has been released. It includes new capabilities to detect a variety of Linux network packet sniffers, plus has internal optimizations that have improved process forensic performance up to 600%.

## Linux Network Packet Sniffer Detection

Packet sniffers on Linux can be legitimate, but also can be very bad news depending on who is using them. A packet sniffer operated maliciously can result in credential theft, or reveal internal network operations that allow an attacker to spread further.

Earlier versions of Sandfly included sniffer detection methods, but this version improves on them dramatically by targeting several critical areas discussed below. We are able to detect many kinds of sniffing activity on Linux now in some way or another.

## Linux Network Packet Sniffer Operating

We now look directly at processes for signs they are using packet capture resources of the host. We will discuss this more below, but these methods allow us to find sniffers even when they are trying to hide.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Packet Sniffer Hiding Under Benign Name](https://www.datocms-assets.com/56687/1635216293-process-masquerading-sniffer-1.png?auto=format&dpr=2&q=60&w=920 "Packet Sniffer Hiding Under Benign Name")

## Network Packet Sniffer Library Detection Expanded

This version of Sandfly includes a wider set of libraries to flag a system process as likely sniffing traffic.

## Common Network Packet Sniffer Process Running

We are now flagging any process with a known name that indicates it is a sniffer. This will catch simple usage of tools like *tcpdump* and other common sniffer names. These can be legitimate for development and network debugging purposes, but depending on what system you see them it could warrant a closer look into who or what started them.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux tcpdump Process Running](https://www.datocms-assets.com/56687/1635216305-process-tcpdump-running.png?auto=format&dpr=2&q=60&w=920 "Linux tcpdump Process Running")

## Network Packet Sniffer Process with Hidden Name

Any process with a hidden name and has any indications of being a sniffer will be flagged. Processes with hidden filenames are suspicious enough, but one sniffing traffic is a serious problem.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Network Sniffer with Hidden Name](https://www.datocms-assets.com/56687/1635216316-process-sniffer-hidden-name.png?auto=format&dpr=2&q=60&w=920 "Network Sniffer with Hidden Name")

## Network Packet Sniffer Process Masquerading

We have built out the list of ways to spot packet sniffers that are masquerading under different names. We had this already with *tcpdump*, but now include other common sniffer programs found on Linux.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![ngrep Sniffer Masquerading as Another Linux Process](https://www.datocms-assets.com/56687/1635216323-process-ngrep-sniffer-masquerading.png?auto=format&dpr=2&q=60&w=920 "ngrep Sniffer Masquerading as Another Linux Process")

## Incident Response Checks for Network Sniffer of Any Kind

New sandfly checks will flag any process using packet capture sockets or libraries. These checks are for incident response as it can flag legitimate programs that are watching for certain network traffic (such as *dhclient*). However, it can be tuned to ignore these alerts with the custom sandfly feature and is extremely reliable at finding network sniffers that are unknown. See below for how to do this.

## Create Your Own Network Packet Sniffer Detection

Select *sandfly process running sniffer* operating from the Incident Response tab and run it against your hosts knowing you will see false alarms.

Going through the list of alerts will show obvious legitimate system daemons quickly and you can add them to the ignore list as needed. For instance, *dhclient* will almost certainly show up along with some *systemd* services. These are all perfectly normal processes that will be watching network traffic to operate.

Next, clone this check and give it a unique name. In the example below we called it *sandfly\_process\_running\_sniffer\_operating\_tuned*.

Go under the *name\_ignore* key under the process section. This is an array of REGEX patterns of process names we should not alarm on if seen. Here you can add an exact match REGEX (such as *^dhclient$*). Or you can use a wildcard if you see false alarms from certain categories of system processes and you want to ignore variants (such as *^systemd.\**).

You can add as many patterns as you need, just be sure you keep them between brackets [] and use a comma between the entries. You can check your REGEX using an [online REGEX testing tool](http://www.regex101.com/).

Finally, be sure you change the *type* key from *“incident”* to *“process.”* This will let Sandfly know this is a process checking sandfly and should be run in the normal automated schedule (incident response sandflies can only be run manually).

Click the *Add* button. Your new check will now be active during random scheduled scans hunting for unknown sniffers that are running.

Below is a screenshot that shows you what to modify to add your own sniffer detection rule. Follow the arrows.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Custom Sandfly Linux Packet Sniffer Detection](https://www.datocms-assets.com/56687/1635216331-sandfly-custom-packet-sniffer-detection.png?auto=format&dpr=2&q=60&w=920 "Custom Sandfly Linux Packet Sniffer Detection")

If you need help setting this up as a general use sniffer detector, please contact us and we are happy to assist. This is a great check to run in your automatic rotation and can find unknown or malicious packet sniffers quickly.

## File Descriptor Socket Decoders

As part of the sniffer detection, we have added the ability to decode Linux file descriptor sockets a process has open. These values can be used in generic search just like any other sandfly search parameter. You can search for socket types that include *packet*, *unix*, *netfilter*, *tcp*, *udp*, *icmp*, *raw*, *tcpv6*, *udpv6*, *icmpv6* and *rawv6* types.

For example, running *sandfly process network* port operating shows all system processes with network sockets operating and you can view all open file descriptors and what they are in the listing. Below is a dump of a system Apache server which gives you an idea of some of the data. We show files open and provide a file type also if we can determine what it is. We will also display system named pipes and other devices.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Apache Open File Descriptors on Linux](https://www.datocms-assets.com/56687/1635216340-process-apache-open-file-descriptors.png?auto=format&dpr=2&q=60&w=920 "Apache Open File Descriptors on Linux")

All of these keys can be turned into REGEX searchable signatures depending on what you are looking to do. You can look under the *Incident Response* tab to clone sandflies that look for particular file descriptors such as TCP ports, raw ports, etc. You can combine it with other keys to get very specific. Again, customers can contact us for assistance and we will help them get a quick solution.

## Processes Masquerading as Kernel Threads

We have expanded the number and types of process masquerading attacks we can find that are trying to look like Linux kernel threads. We have had this ability for some time, but now we have even more methods with different techniques to make it much harder fo...