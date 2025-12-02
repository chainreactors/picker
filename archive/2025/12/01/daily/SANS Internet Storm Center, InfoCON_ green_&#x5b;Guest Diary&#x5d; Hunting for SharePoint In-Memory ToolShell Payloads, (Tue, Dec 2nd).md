---
title: &#x5b;Guest Diary&#x5d; Hunting for SharePoint In-Memory ToolShell Payloads, (Tue, Dec 2nd)
url: https://isc.sans.edu/diary/rss/32524
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-01
fetch_date: 2025-12-02T03:19:04.056585
---

# &#x5b;Guest Diary&#x5d; Hunting for SharePoint In-Memory ToolShell Payloads, (Tue, Dec 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32518)

# [[Guest Diary] Hunting for SharePoint In-Memory ToolShell Payloads](/forums/diary/Guest%2BDiary%2BHunting%2Bfor%2BSharePoint%2BInMemory%2BToolShell%2BPayloads/32524/)

**Published**: 2025-12-02. **Last Updated**: 2025-12-01 23:27:08 UTC
**by** [James Woodworth, SANS.edu BACS Student](/handler_list.html#james-woodworth,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BHunting%2Bfor%2BSharePoint%2BInMemory%2BToolShell%2BPayloads/32524/#comments)

[This is a Guest Diary by James Woodworth, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].

In July 2025, many of us were introduced to the Microsoft SharePoint exploit chain known as ToolShell. ToolShell exploits the deserialization and authentication bypass vulnerabilities, CVE-2025-53770 [2] and CVE-2025-53771 [3], in on-premises SharePoint Server 2016, 2019, and Subscription editions. When the exploit chain was initially introduced, threat actors used payloads that attempted to upload web shells to a SharePoint server’s file system. The problem for threat actors was that the uploaded web shells were easily detectable by most Endpoint Detection and Response (EDR) solutions. So the threat actors upped the game and reworked their payloads to execute in-memory. This new technique made it more difficult for defenders to detect the execution of these new payloads [4].

Many articles have been written on the technical details of the ToolShell vulnerabilities, so I won’t go into an in-depth analysis here. If you want an in-depth analysis, check out the Securelist article, *ToolShell: a story of five vulnerabilities in Microsoft SharePoint* [5]. What I will present to you in this post is a process using Zeek Network Security Monitor, DaemonLogger, and Wireshark to hunt for in-memory ToolShell exploit payloads and how to decode them for further analysis.

## Review Zeek Logs

The first step in the hunt is to review the HTTP requests to our SharePoint server. We will do this by reviewing our Zeek http logs and looking for POST requests that contain the following indicators of a malicious request:

* **URLs:**
  + `/_layouts/15/ToolPane.aspx/<random>?DisplayMode=Edit&<random>=/ToolPane.aspx`
  + `/_layouts/16/ToolPane.aspx/<random>?DisplayMode=Edit&<random>=/ToolPane.aspx`
* **Referer headers:**
  + `/_layouts/SignOut.aspx`
  + `/_layouts/./SignOut.aspx`
* **Request Body:**
  + Length greater than 0

Zeek log files are rotated and compressed daily. To review the compressed log files over multiple days we use a combination of two tools, `zcat` and `zcutter.py` [6]. From the `/opt/zeek/logs` directory we run the following commands to search all Zeek http logs for August 2025.

```

zcat 2025-08**/http*.log.gz | ~/bin/zcutter.py -d ts id.orig_h id.resp_p host method uri user_agent request_body_len | grep ToolPane | grep -v "\"request_body_len\": 0}"
```

Reviewing the returned http logs entries, we see many matching the indicators of a malicious request. We will focus on the highlighted entries from August 24, 2025.

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure1.PNG)
Figure 1: Zeek http.log file matching indicators of a malicious request.**

## Prepare PCAP Files

Now that we have identified potential http requests to analyze further, our next step in the hunt will be to prepare our PCAP files for packet analysis. For this scenario we are using DaemonLogger to capture packets [7]. Each day DaemonLogger creates two PCAP files.

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure2.PNG)
Figure 2: DaemonLogger PCAP files from October 31, 2025.**

We will need to merge the two PCAP files to ensure we are analyzing all packets that were captured for the day in question. To do this we will use the tool mergecap from Wireshark [8]. The following command will merge the two PCAP files that we identified in Figure 2 above into a new file named `2025-08-24.pcap`.

```

./mergecap ~/pcaps/daemonlogger.pcap.* -w ~/pcaps/2025-08-24.pcap
```

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure3.PNG)
Figure 3: Mergecap command and resulting merged PCAP file.**

## Packet Analysis with Wireshark

We will now analyze the newly created PCAP file using Wireshark. With the following filter we can limit the packets displayed to only those packets containing POST requests to the URL `/_layouts/15/ToolPane.aspx`.

**Filter: \_ws.col.info matches "POST /\_layouts/15/ToolPane.aspx"**

![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure4.PNG)
Figure 4: Wireshark displaying packets containing POST requests to the URL /\_layouts/15/ToolPane.aspx.

Analyzing the packet with the timestamp 2025-08-24T04:22:33, we see an HTTP POST request to the URL `/_layouts/15/toolpane.aspx/lx?DisplayMode=Edit&lx=/ToolPane.aspx` and a Referer header of `/_layouts/./SignOut.aspx`. The analysis also shows a URL encoded payload being sent via the `MSOtlPn_DWP` parameter. The parameter contains a property named CompressedDataTable that in turn contains a malicious payload that attempts to exploit the SharePoint deserialization vulnerability.

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure5.PNG)
Figure 5: Wireshark HTTP Stream showing malicious POST request**

## Deserialization Vulnerability Payload Analysis

Our hunt is almost complete. Now it is time to decode the malicious deserialization payload to see what it contains. With the Wireshark HTTP Stream window still open, copy the `CompressedDataTable` property and save to a file named `property-encoded.txt`. This will include everything between `CompressedDataTable%3D%22` and `%22+DataTable-CaseSensitive`. The property usually starts with the characters `H4sI`.

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure6.PNG)
Figure 6: Wireshark HTTP Stream highlighting the beginning of the CompressedDataTable property.**

With the CompressedDataTable property copied to a file we can decode the property using the commands below and output the results to the file `property-decoded.txt`.

```

cat property-encoded.txt | python3 -c "import sys, urllib.parse as ul; print(ul.unquote_plus(sys.stdin.read().strip()))" | base64 -d | zcat > property-decoded.txt
```

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure7.PNG)
Figure 7: Decoded view of the CompressedDataTable property with the encoded malicious payload.**

One more copy and decode and we will have our malicious in-memory payload. Open the `property-decoded.txt` file created in the step above. Copy the `MethodParameter` string to a new file named `method-encoded.txt`. The beginning of the string is highlighted in Figure 7 above. We will then run the following commands to decode the method.

```

cat method-encoded.txt | base64 -d > method-decoded.txt
```

Once our payload is decoded, we see that it contains a known malicious .NET Dynamiclink Library (DLL) binary named `osvmhdfl.dll`. If this in-memory payload was executed successfully on a vulnerable SharePoint server, it could extract machine keys and other system information and return the information in the HTTP response [9].

**![](https://isc.sans.edu/diaryimages/images/2025-12-02_figure8.PNG)
Figure 8: Partially decoded method containing a malicious payload.**

## Additional Payloads Discovered

Using this process, I have discovered security scanner payloads and payloads containing encoded PowerShell commands.

## Nuclei Scanner Template CVE-2025-53770

The Project Discovery Nuclei Scanner, when using the http template CVE-2025-53770, sends the payload in Figure 9. This payload contains the .NET Dynamic-link Library (DLL) binary named `jlaneafi.dll`. If the SharePoint server is vulnerable, an additional HTTP response he...