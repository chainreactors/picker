---
title: New GitDoor and GraphDoor Backdoors Turn GitHub and SharePoint Into Covert C2 Channels
url: https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html
source: The Hacker News
date: 2026-11-17
fetch_date: 2026-11-18T09:22:48.880625
---

# New GitDoor and GraphDoor Backdoors Turn GitHub and SharePoint Into Covert C2 Channels

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [New GitDoor and GraphDoor Backdoors Turn GitHub and SharePoint Into Covert C2 Channels](https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html)

**Ravie Lakshmanan**Nov 17, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhGYnRRqAfAZ2q0dS56dC5lC86Kx69VT0moHy1Pxt67C0ic8RbLOL9LR68b4atQmvb7O6Gq3Btm1axv2aCRaNkhagPKbFHvThWlye3QPpK1xnEj4kovoJn8dsbTlCmAjXOIb8EHV3RJuhNQdVNKRxc4uwiuIfws_a63koiBaCQvs5jwbnTFG8EUwuA0RiA/s1700-nu-rw-lo-l85-e365/git-share.jpg)

Government sectors in Asia and Africa have been targeted by an active cyber intrusion campaign that delivers to previously undocumented backdoors that leverage legitimate services like Microsoft SharePoint and GitHub for command‑and‑control (C2).

The activity has been codenamed **Operation ShadowCloud** by Kaspersky. The Russian cybersecurity company said it identified the campaign in early 2026.

"The threat actor behind it is abusing the legitimate MeshAgent utility to drop two brand-new backdoors," Kaspersky researchers Saurabh Sharma and Noushin Shabab said in a [two-part](https://securelist.com/operation-shadowcloud-gitdoor/122004/) [analysis](https://securelist.com/operation-shadowcloud-graphdoor/122005/). "These implants hide their command‑and‑control (C2) traffic behind cloud services Microsoft SharePoint, GitHub, and Ably, allowing the implants to blend in with normal traffic, effectively evading network-based detections."

The modular backdoors, dubbed GraphDoor and GitDoor for their choice of the cloud platform used for C2, enable the download of additional plugins on demand and the execution of shellcode directly in memory to extend their functionality. Traffic between infected systems and the C2 servers is proxied by deploying a modified Erfrp client and Ably messaging service-based plugins.

The starting point of the attack has been traced back to a MeshCentral Agent, a legitimate remote access tool that's used for remote desktop control, command‑line access, and file management. The attack is said to have targeted an unspecified Taiwanese organization.

The exact method by which the utility is installed on the host remains unknown. However, signs point to the "reuse of a prior infection already present on the network," Kaspersky added.

The MeshCentral Agent is configured to contact a hard-coded C2 server ("wss://27.102.66[.]162:443/agent.ashx") and then fetch three payloads staged on the endpoint -

* A legitimate binary used for DLL sideloading (start.exe, pythonw.exe, and zoomit.exe)
* A rogue loader DLL used to unpack and execute the next-stage malware (jli.dll, SbieDll.dll, python39.dll, WINMM.dll, and libcef.dll)
* An encrypted file containing the core payload

At least two different DLL loaders have been identified to date, each employing its own method to decode and launch the encrypted backdoor payload by injecting it into the current process's memory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"Loader (Type 1) employs a hybrid scheme: first running the data through an RC4 stream cipher and then applying an XOR mask, while Loader (Type 2) simplifies the process by using a straight XOR operation alone," Kaspersky noted.

The end goal is to deploy backdoors like GitDoor and GraphDoor, which employ a number of encryption and obfuscation techniques like control flow flattening and nested helper functions to complicate analysis efforts and make it harder to trace genuine execution flow.

GitDoor, as the name implies, uses GitHub for C2. It relies on two distinct repositories for receiving command payloads ("/repos/LatonyCharnleyaW/Havo") and uploading the results of the execution ("/repos/LatonyCharnleyaW/Trix"). While the Havo repository is public, the Trix repository is private.

The creation date of these repositories suggests that preparations for the campaign have been underway since at least the end of 2024. GitDoor supports 26 commands that allow the backdoor to -

* Perform file management
* Log keystrokes
* Launch a proxy, including using Ably
* Load shellcode to Base64-encoded Common Object File Format (COFF) binaries and terminate the backdoor

The custom shellcode feature is used to download and run different modules that facilitate the following functions -

* Conduct process injection using methods like Asynchronous Procedure Call (APC) injection
* Enumerate and manage Windows services
* List files and directories, wipe file contents, and recursively delete a directory
* Conduct network-related activity by displaying active TCP connections and modify firewall rules
* Manage processes, including dumping the memory of the process with a specified process ID into a file and terminating specific processes
* Execute commands using "cmd.exe"
* Enumerate, create, and run scheduled tasks
* Enumeration Windows Registry keys and values recursively and set a value in the Registry
* Extract user information, along with local groups and its members
* Add of a new Windows user account or add a user to a global or a local group
* Record keystrokes to a file ("%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat")
* Dump cookies from Google Chrome and Microsoft Edge directly from the process memory using CookieKatz
* Use Mimikatz to dump credentials from Windows LSASS
* Capture screenshots of the entire screen or a specific window identified by its process ID
* Extract WhatsApp's database decryption key
* Initiate NTLM authentication to an attacker-controlled destination
* Calculate system idle time and display the last time a user was active on the host using mouse movement and keyboard input

GraphDoor, on the other hand, opens a [named pipe](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipes), creates a directory named "Intel\_Log" inside the system's Application Data folder, and gathers system information to send back to the attacker.

To establish communications with the C2 s...