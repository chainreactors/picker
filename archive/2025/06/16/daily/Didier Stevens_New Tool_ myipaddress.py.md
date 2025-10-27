---
title: New Tool: myipaddress.py
url: https://blog.didierstevens.com/2025/06/15/new-tool-myipaddress-py/
source: Didier Stevens
date: 2025-06-16
fetch_date: 2025-10-06T22:53:20.435965
---

# New Tool: myipaddress.py

# [Didier Stevens](https://blog.didierstevens.com/)

## Sunday 15 June 2025

### New Tool: myipaddress.py

Filed under: [Announcement](https://blog.didierstevens.com/category/announcement/),[My Software](https://blog.didierstevens.com/category/my-software/),[Networking](https://blog.didierstevens.com/category/networking/) — Didier Stevens @ 0:00

This is a new tool that I use for IPv4 operations, like generating a list of CIDRs based on ASNs, checking if IPv4 addresses are members of CIDRs, …

Here is the man page:

```
Usage: myipaddress.py [options] command ...
IP address tool

Arguments:
@file: process each file listed in the text file specified
wildcards are supported

Source code put in the public domain by Didier Stevens, no Copyright
Use at your own risk
https://DidierStevens.com

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -m, --man             Print manual
  -u, --uniques         Remove duplicates
  -s, --sort            Sort
  -q, --quiet           Quiet
  -o OUTPUT, --output=OUTPUT
                        Output to file (# supported)
  -v, --invert          Invert selection
  -e, --extra           Include extra info

Manual:

4 commands are available: cidr2ip, asn2cidr, ipincidr and aso2cidr.

Command cidr2ip is used to generate IPv4 addresses for the given
CIDRs.

Example: myipaddress.py cidr2ip 192.168.0.0/24 10.10.10.0/30

Option -u (--unique) will remove all duplicates from the generated
list.

Option -s (--sort) will sort the list.

Command asn2cidr is used to generate a list of IPv4 CIDRs for the
given ASNs (autonomous system numbers).

Example: myipaddress.py asn2cidr 100 1234

Output:
100: 12.30.153.0/24 74.123.89.0/24 102.210.158.0/24 192.118.48.0/24
198.180.4.0/22 199.36.118.0/24 199.48.212.0/22 216.225.27.0/24
1234: 132.171.0.0/16 137.96.0.0/16 193.110.32.0/21

Option -q (--quiet) will produce a simple list of CIDRs, nothing more.

Example: myipaddress.py -q asn2cidr 1234

Output:
132.171.0.0/16
137.96.0.0/16
193.110.32.0/21

Option -u (--unique) will remove all duplicates from the generated
list.

This command requires CSV file GeoLite2-ASN-Blocks-IPv4.csv to be
present in the same folder as script myipaddress.py.
See below for more info.

Command ipincidr is used to generate a list of IPv4 addresses for the
text files.

The text files either contain a list of IPv4 addresses or a list of
IPv4 CIDRs (it can actually be a mix of both in the same file).
Then the command will produce a list for the given IPv4 addresses that
are contained in the given CIDRs.
If a line of the text file contains a / character, it is interpreted
as a CIDR, otherwise it is interpreted as a IPv4 address.
CIDRs can also be followed by an ASO with the tab character as
separator.

Example: myipaddress.py ipincidr cidrs.txt ipv4s.txt

Option -v (--inverse) will invert the logic: all given IPv4 addresses
that are NOT contained in the GIVEN CIDRs are listed.

Command aso2cidr is used to generate a list of IPv4 CIDRs for the
given ASOs substrings (autonomous system organisations).

Example: myipaddress.py aso2cidr sans-institute

Output:
SANS-INSTITUTE: 66.35.60.0/24 104.193.44.0/24

Example: myipaddress.py aso2cidr sans-institute amadeus

Output:
SANS-INSTITUTE: 66.35.60.0/24 104.193.44.0/24
Amadeus Data Processing GmbH: 82.150.224.0/21 82.150.248.0/23
168.153.3.0/24 168.153.4.0/22 168.153.8.0/23 168.153.32.0/22
168.153.40.0/22 168.153.64.0/22 168.153.96.0/24 168.153.106.0/24
168.153.109.0/24 168.153.110.0/23 168.153.144.0/22 168.153.160.0/22
171.17.128.0/18 171.17.255.0/24 185.165.8.0/23 193.23.186.0/24
193.24.37.0/24 195.27.162.0/23 213.70.140.0/24
Amadeus Soluciones Tecnologicas S.A.: 94.142.200.0/21
Amadeus is an international computer reservations system. A subsidary
is in Bangalore and t: 168.153.1.0/24
Amadeus India Pvt.Ltd.: 202.0.109.0/24
Amadeus India: 203.89.132.0/24

Option -q (--quiet) will produce a simple list of CIDRs, nothing more.

Example: myipaddress.py -q aso2cidr sans-institute

Output:
66.35.60.0/24
104.193.44.0/24

Option -e (--extra) will add the ASO (with tab character as
separator).

Example: myipaddress.py -q -e aso2cidr sans-institute

Output:
66.35.60.0/24   SANS-INSTITUTE
104.193.44.0/24 SANS-INSTITUTE

Option -u (--unique) will remove all duplicates from the generated
list.

This command requires CSV file GeoLite2-ASN-Blocks-IPv4.csv to be
present in the same folder as script myipaddress.py.
See below for more info.

File GeoLite2-ASN-Blocks-IPv4.csv can be obtained for free by creating
an account on maxmind.com and then download database known as:
GeoLite ASN: CSV Format
It's a ZIP file that contains file GeoLite2-ASN-Blocks-IPv4.csv.
```

[myipaddress\_V0\_0\_1.zip](https://didierstevens.com/files/software/myipaddress_V0_0_1.zip) ([http](http://didierstevens.com/files/software/myipaddress_V0_0_1.zip))
MD5: 839550C3E5C6A07C088D27EFD51BE2F7
SHA256: F4DCF325E578F797B3D15316E797EB359E1DA13255E9644841593A1C1C5A9F54

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2025/06/15/new-tool-myipaddress-py/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2025/06/15/new-tool-myipaddress-py/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2025/06/15/new-tool-myipaddress-py/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2025/06/15/new-tool-myipaddress-py/feed/) [TrackBack URI](https://blog.didierstevens.com/2025/06/15/new-tool-myipaddress-py/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/pr...