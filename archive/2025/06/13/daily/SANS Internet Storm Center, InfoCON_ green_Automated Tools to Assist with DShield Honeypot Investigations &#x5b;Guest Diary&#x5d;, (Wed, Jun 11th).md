---
title: Automated Tools to Assist with DShield Honeypot Investigations &#x5b;Guest Diary&#x5d;, (Wed, Jun 11th)
url: https://isc.sans.edu/diary/rss/32038
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-13
fetch_date: 2025-10-06T22:55:20.218494
---

# Automated Tools to Assist with DShield Honeypot Investigations &#x5b;Guest Diary&#x5d;, (Wed, Jun 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32036)
* [next](/diary/32044)

# [Automated Tools to Assist with DShield Honeypot Investigations [Guest Diary]](/forums/diary/Automated%2BTools%2Bto%2BAssist%2Bwith%2BDShield%2BHoneypot%2BInvestigations%2BGuest%2BDiary/32038/)

**Published**: 2025-06-11. **Last Updated**: 2025-06-14 19:38:52 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Automated%2BTools%2Bto%2BAssist%2Bwith%2BDShield%2BHoneypot%2BInvestigations%2BGuest%2BDiary/32038/#comments)

[This is a Guest Diary by William Constantino, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

In the beginning of my Internet Storm Center (ISC) internship, I wasted too much time trying to build my SIEM from an old computer I had lying around, or a new Raspberry Pi I purchased. I keep running into roadblocks and errors. Also, I was distracted while trying to finish up another course, and I had every intention of looking at my log files every day, but it wasn’t happening. I did the easy thing of saying “I’ll look at it tomorrow. The JSON logs and Sqlite3 were the other problems with reading the logs without a SIEM, it produced massive amounts of data to parse through. To me it was like trying to find a needle in a haystack. To resolve this problem, I built two automated python tools to assist with those tasks and analyze the data.

The first tool helped me process and organize the data I was looking at and helped point me in the right direction of interesting things to investigate further. This tool gave me the following capabilities:

1. It loads, reads, and parses JSON files by extracting the source IP addresses, request methods, accessed URLs, timestamps, user agents, response codes, credentials, and hashes.
2. Tracks IP activity by recording the different request methods used (GET, POST, etc.), and it stores the timestamps of requests for timeline analysis.
3. Counts URL accesses for identifying the most frequently visited endpoints, logs the user agent strings to detect patterns in client access, and captures the response codes to track server errors or unusual behavior.
4. Detects suspicious activity by flagging suspicious file requests (.php, .exe, .zip, etc.), extracts credential attempts (20 of the most used usernames and passwords), and identifies hashed values (MD5, SHA1, CRC32, NTLM, etc.)
5. Generates a generic security report by reporting the top 10 most active IPs, bottom 10 least active IPs, and the total amount of Unique IPs. It gives a summary of total requests, detected hashes, and credential attempts.
6. Lastly it measures how long the script takes to process the log file. It displays the results in minutes and seconds (I added this last because I just wanted to know how long it was taking to read and parse through the data).
7. The sample output from this tool is from 2025-05-31, and it was a massive log file at over 3.5GB for one day (why I added the timer). I will break down the output in sections for Tool 1 below:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic1.png)

Figure 1: Top 10 most Active IP addresses, Bottom 10 Least Active IPs, and General Summary.

Continued Output Tool 1:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic2.png)
Figure 2: The Request Methods Used and Top Accessed URLs.

Continued Output Tool 1:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic3.png)
Figure 3: Suspicious File Requests and Top User-Agent Strings.

Continued Output Tool 1:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic4.png)
Figure 4: Top attempted usernames and attempted passwords.

Continued Output Tool 1:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic5.png)
Figure 5: Hashes Detected and the Time it took to read the log file.

Once I had this output to look at, I determine what IP address that is the most interesting. However, I usually start with the one with the largest number of requests to see what is going on. I will look at all 10-20 (Top and Bottom 10) individually and see what they were doing and then determine which IP address to highlight for my analysis. Sometimes, if I’m looking at the same exploit, I’ll research all the other IPs to see if there is a novel attack or a different type of attack. To assist with a further investigation, I developed a second tool to help me with this. It is basically, the same as the first tool, but it focuses on further detailed analysis of specific IP(s).

The second python tool performs a detailed analysis on a specific IP address or addresses that you want further analysis on from a given a JSON log file. This tool does the following things:

1. Provides a prompt to input one (1) or multiple IP addresses.
2. It extracts the “sip” (source IP) field from each log entry and identifies requests.
3. The script gathers the HTTP request methods used by the target IP (GET, POST, HEAD, etc.). It also records the timestamps of the request timeframe.
4. Analyzes the User-Agent Strings which can provide insight into whether the requests originated from a legitimate browser, automated bot, or a hacking tool.
5. Examines response codes to show whether the target IP successfully accessed certain resources.
6. Detects suspicious file requests (.php, .exe, .zip, .bat, .sh, .py)
7. Credential attempts using default usernames and passwords (currently only the top twenty of each).

Below is my output for the second tool (also for 2025-05-31). It is basically, the same as the first tool, but it focuses on further detailed analysis of specific IPs.

Output Tool 2:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic6.png)
Figure 6: Prompt to enter one (1) IP or multiple IP addresses separated by a comma.

Continued output Tool 2:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic7.png)
Figure 7: I inputted IP address (141.98.80.134). In this case, it was the #1 active IP.

Continued output of Tool 2:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic8.png)
Figure 8: Analysis for IP (141.98.80.134) with a massive number of requests.

According to the top accessed URLs in this investigation of this IP are known for CVE-2021-20016. I’ve actually seen this type of attack lately.

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic9.png)
Figure 9: Internet Storm Center Report for an exploit for Sonicwall [[1](https://isc.sans.edu/diary/31906)].

Continued output of Tool 2:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic10.png)
Figure 10: User-Agent Strings and Attempted Passwords.

This script will notify if it did not find any data for the specific fields looked at. The first tool does not do this, but usually there are all types of data and no field is empty during the investigation.

Continued output of Tool 2:

![](https://isc.sans.edu/diaryimages/images/William_Constantino_pic11.png)
Figure 11: The Log Analysis is Complete.

It took almost 13 minutes to complete. This was a massive file compared to other days, so analysis will be much faster with less data.
Using this tool to analyze the data in a short amount of time, the analyst will be able to inquire more information about the IP from websites like [Virustotal](https://www.virustotal.com/gui/home/upload), [IPQualityScore](https://www.ipqualityscore.com/ip-reputation-check), [APIVoid](https://www.apivoid.com/tools/ip-reputation-check/), and etc. That information might give additional data points to see if further investigation is warranted or not.

In Conclusion, my script(s) or python tool(s) can assist help detect potential attackers that are targeting their DShield Honeypot. The t...