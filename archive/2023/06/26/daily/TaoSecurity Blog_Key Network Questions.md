---
title: Key Network Questions
url: https://taosecurity.blogspot.com/2023/06/key-network-questions.html
source: TaoSecurity Blog
date: 2023-06-26
fetch_date: 2025-10-04T11:47:53.967791
---

# Key Network Questions

[Skip to main content](#main)

### Search This Blog

# [TaoSecurity Blog](https://taosecurity.blogspot.com/)

Richard Bejtlich's blog on digital security, strategic thought, and military history.

### Key Network Questions

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[June 25, 2023](https://taosecurity.blogspot.com/2023/06/key-network-questions.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJfUey3be9pEMCVYML3MlBe_hqBQf975kYJkoW93oo_eOJTjoAecqJjqBPQ4U5w2PZLpdHKHNiCI7kkK3HCxXx8gDofwJsNI-6apqT7qiXle0SQOzD1XWg0FHZWGb9nsgp89l5jsarqhRP2yiZ4RC-FP35sZGKhjfEdlJqvtOxha7y2LRDuEBY/w400-h363/sguil_login.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJfUey3be9pEMCVYML3MlBe_hqBQf975kYJkoW93oo_eOJTjoAecqJjqBPQ4U5w2PZLpdHKHNiCI7kkK3HCxXx8gDofwJsNI-6apqT7qiXle0SQOzD1XWg0FHZWGb9nsgp89l5jsarqhRP2yiZ4RC-FP35sZGKhjfEdlJqvtOxha7y2LRDuEBY/s475/sguil_login.png)

I wrote this on 7 December 2018 but never published it until today. The following are the "key network questions" which "would answer many key questions about [a] network, without having to access a third party log repository. This data is derived from mining Zeek log data as it is created, rather than storing and querying Zeek logs in a third party repository."

This is how I was thinking about Zeek data in the second half of 2018.

1. What networking technologies are in use, over user-specified intervals?

1. Enumerate non-IP protocols (IPv6, unusual Ethertypes)

2. Enumerate IPv4 and IPv6 protocols (TCP, UDP, ICMP, etc.)

3. What is the local IP network topology/addressing scheme?

2. What systems are providing core services to the network, over user-specified intervals?

1. DHCP

2. DNS

3. NTP

4. Domain Controller

5. File sharing

6. Default gateway (via DHCP inspection, other?)

7. Web and cloud services

3. What tunnel mechanisms are in use, over user-specified intervals?

1. IPSec or other VPNs

2. SOCKS proxy

3. Web proxy (port 3128)

4. Other proxy

4. What access services are in use, over user-specified intervals?

1. SSH

2. Telnet

3. RDP

4. VNC

5. SMB

6. Other

5. What file transfer services are in use, over user-specified intervals?

1. SCP or other SSH-enabled file transfers

2. FTP

3. SMB

4. NFS

6. Encryption measurement, over user-specified intervals

1. What encryption methods are in use?

2. What percentage of network traffic over a user-specified interval is encrypted, and by which method?

7. Bandwidth measurement, over user-specified intervals

1. Aggregate

2. By IP address

3. By service

8. Conversation tracking, over user-specified intervals

1. Top N connection pairs

2. Bottom N connection pairs

9. Detection counts, over user-specified intervals

1. Provide a counter of messages from Zeek weird.log

2. Provide a counter of messages from other Zeek detection logs

10. For each IP address (or possibly IP-MAC address pairing), over user-specified intervals, build a profile with the following:

1. First seen, last seen

2. Observed names via DNS, SMB, other

3. Core services accessed and provided

4. Tunnel mechanisms used and provided

5. Access services used and provided

6. File transfer services used and provided

7. Encryption methods

8. Bandwidth measurements

9. Top N and bottom N conversation tracking

10. Detection counts

[nsm](https://taosecurity.blogspot.com/search/label/nsm)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4088979/2237548773167512604)

### Popular posts from this blog

### [Zeek in Action Videos](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

[July 29, 2021](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcWFyS3aGQrT6UiiiBbLkOiUs5W_Y9cYMLeH2Z7KkzzqINSWjFIEG8inSUNbYNGTjF7dcEUOOOkK7DzHQXcNMY3Nhl1PIFsdZZeJOH7bzRzpQMUdez5M7_g3t_xyygra49FBKK/w640-h360/capture_001_29072021_143006.jpg)](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

This is a quick note to point blog readers to my Zeek in Action YouTube video series for the Zeek network security monitoring project .  Each video addresses a topic that I think might be of interest to people trying to understand their network using Zeek and adjacent tools and approaches, like Suricata, Wireshark, and so on.  I am especially pleased with Video 6 on monitoring wireless networks . It took me several weeks to research material for this video. I had to buy new hardware and experiment with a Linux distro that I had not used before -- Parrot .  Please like and subscribe, and let me know if there is a topic you think might make a good video.

[Read more](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "Zeek in Action Videos")

### [MITRE ATT&CK Tactics Are Not Tactics](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

[October 23, 2020](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh8UtkHOxII5KLGuTgeVk3iVj3KMfkoFLyDb11MrasYGQ9J2Q5NPBgNUX4-Dk5YKF_26s2quTQ_ve4bEh4yIF1H97CJeNqoGqlpAATJPzThQ_IGALsANV3MZLlF_zogZNHM-LI/s320/on+tactics.jpg)](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

Just what are "tactics"? Introduction MITRE ATT&CK  is a great resource, but something about it has bothered me since I first heard about it several years ago. It's a minor point, but I wanted to document it in case it confuses anyone else. The MITRE ATT&CK Design and Philosophy document from March 2020 says the following: At a high-level, ATT&CK is a behavioral model that consists of the following core components: • Tactics, denoting short-term, tactical adversary goals during an attack; • Techniques, describing the means by which adversaries achieve tactical goals; • Sub-techniques, describing more specific means by which adversaries achieve tactical goals at a lower level than techniques; and • Documented adversary usage of techniques, their procedures, and other metadata. My concern is with MITRE's definition of "tactics" as "short-term, tactical adversary goals during an attack," which is oddly recursive. The key word in the tacti...

[Read more](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "MITRE ATT&CK Tactics Are Not Tactics")

### [New Book! The Best of TaoSecurity Blog, Volume 4](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html)

[April 13, 2021](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe6YF9WJiKp0uULA6gH7y4zgy_L4W5xkOUmCV3fENBessbRL3bdnf6xy2y-uWNS1ScWWzyQ5qBL56XVyeknUtWhFk29Ol6pGst3H78RCAT2c53h7VCq4bU00BGhRhXRygZs8kZ/w400-h640/The+Best+of+TaoSecurity+Blog%252C+Volume+4.jpg)](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html)

I've completed the TaoSecurity Blog book series . The new book is  The Best of TaoSecurity Blog, Volume 4: Beyond the Blog with Articles, Testimony, and Scholarship .  It's available now for Kindle , and I'm working on the print edition.  I'm running a 50% off promo on Volumes 1-3 on Kindle through midnight 20 April. Take advantage before the prices go back up. I described the new title thus: Go beyond TaoSecurity Blog with this new volume from author Richard Bejtlich. In the first three volumes of the series, Mr. Bejtlich selected and republished the very best entries from 18 years of writing and over 18 million blog views, along with commentaries and additional material.  In this title, Mr. Bejtlich collects material that has not been published elsewhere, including articles that are no longer available or are stored in assorted digital or physical archives. Volume 4 ...