---
title: Memory Forensics R&D Illustrated: Recovering Raw Sockets on Windows 10+
url: https://volatility-labs.blogspot.com/2023/08/memory-forensics-r-d-illustrated-recovering-raw-sockets0-on-windows-10.html
source: Volatility Labs
date: 2023-08-15
fetch_date: 2025-10-04T12:03:54.909768
---

# Memory Forensics R&D Illustrated: Recovering Raw Sockets on Windows 10+

# [[Archive of Volatility Labs]](https://volatility-labs.blogspot.com/)

**This site is an archive of the Volatility Labs blog. The blog has moved to <https://volatilityfoundation.org/volatility-blog/>**

## Monday, August 14, 2023

### Memory Forensics R&D Illustrated: Recovering Raw Sockets on Windows 10+

*As mentioned in a *[recent blog post](https://volatility-labs.blogspot.com/2023/06/malware-and-memory-forensics-training-headed-to-amsterdam-in-october-2023.html)*, our team is once again offering in-person training, and we have substantially updated our course for this occasion. Our next offering will be in**[Amsterdam in Octobe*r 2023*](https://volatility-labs.blogspot.com/2023/06/malware-and-memory-forensics-training-headed-to-amsterdam-in-october-2023.html)**. To showcase our team’s new research, we are publishing a series of blog posts to offer a sneak peek at the types of analysis incorporated into the updated *[Malware & Memory Forensics training course](https://www.memoryanalysis.net/memory-forensics-training)*.*

---

In this blog post, we present our recent research effort to modernize Volatility’s ability to detect the usage of raw sockets by malicious applications, which led to the creation of a new Volatility 3 plugin. Before we begin the technical breakdown, we would like to take this moment to officially welcome the newest member of the Volatility core development team, *[Gus Moreira](https://www.linkedin.com/in/gustavocmoreira/)*, who was a key contributor to this research effort. Gus began working with Volatility when he submitted to and won the *[2020 Volatility plugin contest](https://volatility-labs.blogspot.com/2020/11/the-2020-volatility-plugin-contest-results.html)* and he has since contributed many new plugins, APIs, and bug fixes to Volatility 3. We are very happy to have Gus’s help with moving Volatility 3 forward, and there will be several future blog posts detailing other research efforts in which he was deeply involved.

## Raw Sockets Background

*[Raw sockets](https://attack.mitre.org/techniques/T1040/)* allow privileged applications to both read (sniff) incoming network traffic and construct packets from scratch before being sent, including creating the protocol headers. A wide variety of malicious applications have abused these features in order to steal sensitive information as it traverses the network, forge network streams, bypass network intrusion monitors, and implement custom command-and-control protocols.

The following excerpt from *[The Art of Memory Forensics](https://www.amazon.com/Art-Memory-Forensics-Detecting-Malware/dp/1118825098)* shows how applications can use the *[SIO\_RCVALL](https://learn.microsoft.com/en-us/windows/win32/winsock/sio-rcvall)*IOCTL to receive all packets that traverse the system:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhu3kiPv-gBQtXs-gcKVcbvddZ9fuCWujxvAtVaVCAQoF7k6kfNID83LZgsw0jvMpzvw0cTHyMQ__kyRCMPJkliyo1GeuCFdku2CH3TNjBKhejhgm3E-0BgQjmVL2rv1Vj8X4SzSyTB4C8ExWxkABCK47NMWKERaiBM6PGprCgyri2ctp4fmZY3Y8vk-so/w400-h304/image001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhu3kiPv-gBQtXs-gcKVcbvddZ9fuCWujxvAtVaVCAQoF7k6kfNID83LZgsw0jvMpzvw0cTHyMQ__kyRCMPJkliyo1GeuCFdku2CH3TNjBKhejhgm3E-0BgQjmVL2rv1Vj8X4SzSyTB4C8ExWxkABCK47NMWKERaiBM6PGprCgyri2ctp4fmZY3Y8vk-so/s1358/image001.png)

Once the code described above is executed, the calling application can then receive all packets that traverse the system. To send raw packets, applications only need to create a socket (as shown in step 1 above). *[This sample project](https://github.com/microsoft/Windows-classic-samples/blob/main/Samples/Win7Samples/netds/winsock/ping/Ping.cpp)* from Microsoft illustrates how to send and receive raw ICMP packets in an application.

## Detecting Raw Sockets Before Windows 10

Given the danger posed by raw sockets, it is important that DFIR methodologies can be used to detect their use.  Before Windows 10, it was possible to detect raw sockets using memory forensics by looking for process handles open to the “\Device\RawIp\0” device, as well as looking for sockets with a local port of “0” and protocol of “0” (HOPOPT/RAW).

The following shows how Volatility is used to find handles to the “rawip” device in a memory sample infected with the Ursnif malware:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1uXZLeJtTDS9JrfrbNnZRkZn0wdRxYS7Ke1Fr4Zki0xsXREmxukvwQkvLY9L6QDZg_UYLOXHVZN9iIBQgutyZbD5EnbxVV2pD10L2UuB3L4_z05xMCq0-tJAs3pwx2QcrZhQ5nWopih97g2Ju-HUaXOnvZ3hbHH_5pAgElh2iHw57KYT7Sei7x7Et_Fw/s320/image002.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1uXZLeJtTDS9JrfrbNnZRkZn0wdRxYS7Ke1Fr4Zki0xsXREmxukvwQkvLY9L6QDZg_UYLOXHVZN9iIBQgutyZbD5EnbxVV2pD10L2UuB3L4_z05xMCq0-tJAs3pwx2QcrZhQ5nWopih97g2Ju-HUaXOnvZ3hbHH_5pAgElh2iHw57KYT7Sei7x7Et_Fw/s569/image002.jpg)

As seen, two processes were found to have this handle open: PID 4, which is the kernel, and PID 1824.

Running the *sockets* plugin and searching for raw sockets also leads us to PID 1824:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCuLuF6ALdQCwbuZuBmvug2_Lc0RbH5We7n0jDP53qEl-K9xTs8xW5uYeKatvzlJ0svLpCkQSMC0HhKg391A7TnkNLxg51XKM91cK-Epel2AzIgEqTGFbVEkgDO_m2yDkv_S4eDJRxij1gMyV5Jg_URGXanVhRlCI1nXFO7SW5M8EEe5pEoq4zJAOJjTg/s320/image003.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCuLuF6ALdQCwbuZuBmvug2_Lc0RbH5We7n0jDP53qEl-K9xTs8xW5uYeKatvzlJ0svLpCkQSMC0HhKg391A7TnkNLxg51XKM91cK-Epel2AzIgEqTGFbVEkgDO_m2yDkv_S4eDJRxij1gMyV5Jg_URGXanVhRlCI1nXFO7SW5M8EEe5pEoq4zJAOJjTg/s665/image003.jpg)

In a real investigation, we could then begin to inspect this oddly named process:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKCbUDIF4aWZ7InCYVRZkiWAsSKMHmbtrufS4HRnmVYdynw-3LFvwUfrpKv79232pZxuYNMpZMxKNCpHK9y8z7hHpVu4kFfzKwCZEh8JDU3gzqTGRkLMH3_3S5EvPPkCwAuQuprxoKAB8yQ2IT3F9_7qf0ePG-ZED4WdVBOL8sELPTnyPSoh7yKKhYwsk/s320/image004.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKCbUDIF4aWZ7InCYVRZkiWAsSKMHmbtrufS4HRnmVYdynw-3LFvwUfrpKv79232pZxuYNMpZMxKNCpHK9y8z7hHpVu4kFfzKwCZEh8JDU3gzqTGRkLMH3_3S5EvPPkCwAuQuprxoKAB8yQ2IT3F9_7qf0ePG-ZED4WdVBOL8sELPTnyPSoh7yKKhYwsk/s649/image004.jpg)

## Detecting Raw Sockets in Windows 10+

Due to significant changes made by Microsoft to the Windows network stack, the above methods for detecting raw sockets are no longer viable on modern versions of Windows. This led us to begin a new research project to determine how raw sockets could again be detected.

To avoid relying on indirect artifacts, such as opened handles, our main goal was to determine which data structure within the network stack was now being used to track raw sockets, since the regular socket structure seemingly did not. Analysis of the network stack requires careful and time-consuming reverse engineering, as the debug symbols for network stack driver, *tcpip.sys*, only provide symbol names and no types. Furthermore, Microsoft now makes significant updates to *tcpip.sys* between versions, so it is not always the case that previous knowledge applies directly to the latest release.

Given our team’s experience in analyzing the Windows 10+ network stack, we were pretty confident that raw sockets would now be created using their own endpoint structure, similar to how the operating system is handling TCP sockets, UDP sockets, and connections. This led us to search for related functions in IDA Pro, which brought us to *RawCreateEndpoint*. Analysis of this function showed that it did create a new pool allocation for raw sockets, and that the socket references its owning process. Unfortunately, we did not see where raw sockets still track their create time as other socket types still do.

The following screenshot shows the main part of this function:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2AIhVDof0fIz8ou53KZj_GHStqQxDARuZQ9r8iNp5u-bAJ8y64AaO4YP1bIhiT87g-kEJ5OlLPF8jqNZyAOrMVOR-gq4eH__dY4GPupt3Klh5_vEoWRm6iie...