---
title: Network Forensics With Wireshark
url: https://blog.cyber5w.com/Network_forensics_with_wireshark.html
source: Instapaper: Unread
date: 2024-09-11
fetch_date: 2025-10-06T18:30:51.654761
---

# Network Forensics With Wireshark

[![CYBER 5W](/images/logo.png)](/)

## Menu

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

Search

Search for Blog

![Network Forensics With Wireshark](/images/network_forensics_with_wireshark/cover.png)

3 min read
Sep 8, 2024

## Network Forensics With Wireshark

[![Cyber 5W's Picture](https://avatars.githubusercontent.com/u/80437140?s=328&v=32)](/about/)

[Cyber 5W](/about/)
in

[SOC](/tag/SOC)

# What Is Network Forensics?

Network forensics is a specialized field within cybersecurity focused on the monitoring, capturing, and analysis of network traffic to uncover and investigate security incidents or breaches.

By examining data packets, network logs, and communication patterns, network forensics aims to reconstruct events leading up to an incident, and understand their methods.
This process is crucial for not only resolving current security issues but also for strengthening defenses against future attacks.

With cyber threats becoming increasingly sophisticated, network forensics plays a vital role in safeguarding digital infrastructures and ensuring overall network security.

To identify attacks, investigators must have a good understanding of how different parts of a network communicate, such as websites, emails, general network communications, and file transfers.

Serious cyberattacks, like ransomware or attacks on supply chains, usually start with someone getting into the target system without permission. After that, they move around inside the network, this happens through multiple network devices like routers, firewalls, and switches.

# What Is Wireshark?

Wireshark is a powerful tool for examining network traffic, commonly used in digital investigations. By installing Wireshark on a portable drive, Investigators can perform real-time forensic analysis, which helps in responding to incidents and focusing on important tasks first.

This tool enables investigators to quickly understand the current situation, stop the attack, and collect evidence and information to avoid similar incidents in the future.

Wireshark is a free and open-source network protocol and traffic analyzer that enables users to capture and troubleshoot network traffic.

Essentially, Wireshark allows you to capture traffic on a network and presents the captured traffic as individual packets for detailed analysis. It captures packets on a network, displaying various packet fields and headers based on the type of packet selected.

When capturing traffic, you do so through an interface, which Wireshark calls a network interface card (NIC). This could be a wired or a wireless connection. The amount of data you capture depends on your interface.

For example, if you’re using a wireless adapter that doesn’t support monitor mode (which allows you to capture traffic from other devices on a wireless network), you won’t be able to capture that traffic. So, the type of device you use affects your ability to capture different types of network traffic.

# Practical Show

Let’s work on an example exercise. We need to examine harmful network traffic, and the pcap file we use will have data that’s either sent over HTTPS or HTTP but protected by a TLS certificate. Our job is to decrypt this data and figure out what kind of harmful software was used to attack a computer on the network.

![error](/images/network_forensics_with_wireshark/wireshark_case.png)

As a digital forensics’ investigator, you may need to examine a pcap file to find out if a device was infected and what happened. In these situations, you can use the helpful filtering tool in Wireshark. For example, you can filter for successful TLS handshakes by using tls.handshake.type == 1. This example shows the use of TLS protocol version 1.2.

![error](/images/network_forensics_with_wireshark/handshake.png)

You can tell that this traffic is encrypted because it has an SSL certificate. By following the TCP stream.

To follow a TCP request in Wireshark:

* Right-click the packet, then select “Follow” > “TCP Stream” from the context menu.
* A new window will open showing the entire conversation between the client and server for that TCP connection.

![error](/images/network_forensics_with_wireshark/follow_tcp.png)

You’ll notice that all the data remains encrypted.

![error](/images/network_forensics_with_wireshark/tcp_stream.png)

It gives you the real SSL keys needed to decrypt HTTPS or SSL encrypted data. Now that we have these keys, how do we use them to unlock the data?

To do this, click on Edit, then choose Preferences. Look for Protocols and find TLS. You’ll find a spot for the Pre-Master Secret log file name. Go to where you saved the file, pick the Wireshark tutorial keys log file, and press Open

![error](/images/network_forensics_with_wireshark/tls_key.png)

When we use a filter to look at the TLS handshake by typing “tls.handshake.type == 1” and press enter, we can then follow the TCP stream to see the communication. By examining the TLS stream, we can see the actual POST requests being made, which lets us analyze the data that is being sent

![error](/images/network_forensics_with_wireshark/tls_follow.png)

Now, our goal is to determine which system was affected and what type of malware led to the infection.

We’ll use a filter in Wireshark. First, we’ll set the filter to http.request, and then we’ll use logical operators.

We’ll set the filter to http.request or tls.handshake.type equal to 1 (which is the filter we used previously), and then we’ll exclude the SSDP protocol.

So, our full filter will look like this: (http.request or tls.handshake.type == 1) and !(ssdp). Once we’ve set this up correctly, we’ll press enter to show all the HTTP requests or secure communications, but we won’t show any SSDP messages.

![error](/images/network_forensics_with_wireshark/http_request.png)

We have a GET request, and by clicking on it, we see that it’s requesting or downloading a specific resource called invest20.ell

![error](/images/network_forensics_with_wireshark/invest_dll.png)

By right-clicking on the packet and selecting Follow HTTP Stream, we can observe what happened. We see that the source IP on the network made a GET request to a specific server for the DLL. The server responded with an OK, indicating that the file was found, and then provided the octet stream containing the DLL.

![error](/images/network_forensics_with_wireshark/get_.png)

The application data contained within that packet appears to be the actual DLL. We can confirm this because we see the DOS stub, which includes the message “This program cannot be run in DOS mode.” This indicates that the content of the packet is indeed the DLL file.

![error](/images/network_forensics_with_wireshark/mz.png)

As a malware analyst or threat hunter, you would need to download or save the content of this DLL file to analyze it with a tool like VirusTotal.
you can save the DLL as a file because it’s no longer encrypted. Follow these steps:

1- Find the correct data packet in Wireshark.

2- Click on that packet and choose the Export Objects to save it as an HTTP file

![error](/images/network_forensics_with_wireshark/save_option.png)

We are looking for the file named invest\_20.dll. To save this file, choose to export it and save it on your desktop as invest20.dll. This will allow you to save the downloaded file for further analysis.

![error](/images/network_forensics_with_wireshark/save_dll.png)

Once the file is saved, you can use a service like VirusTotal to identify the type of malware. Simply upload the malware file to VirusTotal for analysis.

![error](/images/network_forensics_with_wireshark/virustotal.png)

You’ll see that this is flagged as malware, with the original DLL being crowddrive.dll. You can learn more details about it here, i...