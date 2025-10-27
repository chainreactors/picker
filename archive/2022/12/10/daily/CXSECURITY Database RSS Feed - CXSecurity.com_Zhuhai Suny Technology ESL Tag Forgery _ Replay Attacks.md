---
title: Zhuhai Suny Technology ESL Tag Forgery / Replay Attacks
url: https://cxsecurity.com/issue/WLB-2022120020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-10
fetch_date: 2025-10-04T01:05:18.496920
---

# Zhuhai Suny Technology ESL Tag Forgery / Replay Attacks

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Zhuhai Suny Technology ESL Tag Forgery / Replay Attacks** **2022.12.09**  Credit:  **[Steffen Robertz](https://cxsecurity.com/author/Steffen%2BRobertz/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45914](https://cxsecurity.com/cveshow/CVE-2022-45914/ "Click to see CVE-2022-45914")**  CWE: **N/A** | |

SEC Consult Vulnerability Lab Security Advisory < 20221201-0 >
=======================================================================
title: Replay attacks & Displaying arbitrary contents
product: Zhuhai Suny Technology ESL Tag / ETAG-TECH protocol
(electronic shelf labels)
vulnerable version: All
fixed version: -
CVE number: CVE-2022-45914
impact: critical
homepage: http://www.zhsuny.com/
found: 2022-05-27
by: Steffen Robertz (Office Vienna)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Zhuhai Suny Technology Co., Ltd, founded in 2016 and located in Zhuhai
Guangdong, is the manufacturer of electronic shelf labels and Alibaba
Super Key Account Gold Supplier specializing in ESL with over 10 years’
experiences focusing on helping customers reduce cost and boost sales.
Since its founding, Suny has attached great importance to exploring
both international and domestic markets, thus becoming China’s top 1
manufacturer of electronic shelf labels. Its products have been widely
applied in supermarkets, retail stores, pharmacies, warehouses,
exhibitions, etc. We has currently provided services to customers from
more than 180 countries, and total sales in 2020 have exceeded
15 million US dollars."
Source: http://www.zhsuny.com/profile/
Business recommendation:
------------------------
The vendor did not respond to our communication attempts, there is no patch
available. In case you are using the product, contact the vendor and urge
them to fix the security vulnerabilities.
SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.
The research has also been presented at various security conferences such as
hardwear.io, named "Self-labeling electronic shelf labels".
Vulnerability overview/description:
-----------------------------------
1) Replay Attack
The displayed information on the price tag can be updated via a 433 MHz
custom protocol (called ETAG-TECH). An attacker can record transmitted
RF samples and replay them later to cause the same action. Thus, it is
possible to restore an older price on the tag without the need for any
information about the protocol or tag.
2) Forging ETAG-TECH protocol messages to display arbitrary content (CVE-2022-45914)
The ETAG-TECH protocol was reverse engineered. It was noted, that no
authentication is existent. Hence, one can display arbitrary content
on the electronic tag by simply transmitting messages according to the
protocol.
Proof of concept:
-----------------
1) Replay Attack
The tag and base station communicate at 433.264 MHz. Thus, the following
HackRF command can be used to record a transmission:
hackrf\_transfer -r /tmp/old\_price -f 433264000 -s 4000000 -a 1 -x 43 -l 16 -g 20
The following command was used in order to replay the signal:
hackrf\_transfer -t /tmp/old\_price -f 433264000 -s 4000000 -a 1 -x 43 -l 16 -g 20
A video of the attack has been published here: https://youtu.be/hj\_ao25HU1E
2) Forging ETAG-TECH protocol messages to display arbitrary content (CVE-2022-45914)
The base station will transmit a compressed image to the tag. Thus,
any content can be displayed.
Following steps will have to happen:
I) Send wake-up frames to the tag.
II) Compress the picture that should be displayed.
III) Wrap the compressed picture into the picture data structure.
IV) Split the data structure into the image frames.
V) Listen for the tag's response.
I) The Wake-up Frame:
The CRC is calculated over the whole frame, starting with the frame length
field. The frame counter is counting down to zero. Every unique frame
(=unique frame counter) is sent five times. The frame is transmitted at
175 kBaud.
| Preamble | Sync Header | Frame Length | Tag ID | Fixed Value | Frame Counter | Fixed Value | CRC16 |
|------------------|-------------|--------------|--------|-------------|---------------|-------------|-------|
| AAAAAAAAAAAAAAAA | D391D391 | 08 | 065302 | 0000 | 0398 | 0A | CRC |
II) The Compression Algorithm:
Runlength encoding is used as compression algorithm. The image is read in
rows. An "a" stands for either a 1 or 0, depending on if it's a run of
ones or zeros that is being encoded. A "c" stands for the length of the
run.
There are four different cases:
Case 1: Less than 8 consecutive bits
0b1aaaaaaa
Case 2: Less than 32 consecutive bits
0b0acccccc
Case 3: Less than 256 consecutive bits
0b1a000000 0bcccccccc
Case 4: Less than 2^16 consecutive bits
0b0a000000 0bcccccccc 0bcccccccc
III) The picture data structure
The compression header indicates the color channel:
FC00000000 = black
FC80000000 = red
| LED | Batch Code | Fixed Value | LED Time | Compression header | Display Height | Display Width | Compressed Image Data |
|---------|------------|-------------|----------|--------------------|----------------|---------------|-------------------------|
| 0700 | BF75 | 00ED | 000A | FC00000000 | 007F | 0127 | <Compressed Image Data> |
IV) The Image Frames
Image frames can only hold 54 Bytes of data. Thus the previously generated
image data structure is split into chunks of 54 bytes or less.
The CRC is calculated over the whole frame, starting with the frame length
field. The frame counter indicates frame 1 out of 9. The frame is transmitted
at 100 kBaud.
| Preamble | Sync Header | Frame Length | Tag ID | Frame Counter | Fixed Value | Payload | CRC16 |
|------------------|-------------|--------------|--------|---------------|-------------|------------------------|-------|
| AAAAAAAAAAAAAAAA | D391D391 | 08 |...