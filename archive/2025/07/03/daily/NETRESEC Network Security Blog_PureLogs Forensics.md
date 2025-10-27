---
title: PureLogs Forensics
url: https://www.netresec.com/?page=Blog&month=2025-07&post=PureLogs-Forensics
source: NETRESEC Network Security Blog
date: 2025-07-03
fetch_date: 2025-10-06T23:56:38.106646
---

# PureLogs Forensics

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Wednesday, 02 July 2025 11:52:00 (UTC/GMT)

## [PureLogs Forensics](/?page=Blog&month=2025-07&post=PureLogs-Forensics)

I analyzed some [PureLogs Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.purelogs) malware infections this morning and found some interesting behavior and artifacts that I want to share.

PureLogs infections sometimes start with a dropper/downloader ([PureCrypter](https://malpedia.caad.fkie.fraunhofer.de/details/win.purecrypter)) that retrieves a .pdf file from a legitimate website. The dropper I will demo here downloaded this file:

> hxxps://www.vastkupan[.]com/wp-admin/js/Daupinslenj.pdf

This file isn’t really a PDF though, but more on that later. Here’s a [CapLoader](https://www.netresec.com/?page=CapLoader) screenshot with some interesting flows from the infection:

![Flows from PureLogs infection in CapLoader](https://media.netresec.com/images/CapLoader-PureLogs-Flows-1937x378.webp)

The PCAP in the screenshot above comes from a [sandbox execution on any.run](https://app.any.run/tasks/dfe55a5f-e412-4737-91b7-14fdce81f534) of a file called BSN100357-HHGBM100002525.exe.

Here’s a breakdown of what happens behind the scenes in this execution:

1. Dropper connects to www.vastkupan[.]com (DNS and TLS flows).
2. A fake PDF (Daupinslenj.pdf) is downloaded over HTTPS.
3. The fake PDF is decrypted to a DLL (PureLogs), which is stored in memory.
4. InstallUtil.exe is started.
5. The PureLogs DLL is injected into the running InstallUtil process.
6. PureLogs connects to C2 server at 91.92.120.101:65535

The same dropper has also been [run on JoeSandbox](https://www.joesandbox.com/analysis/1718460/0/html), with almost identical behavior. The vastkupan.com website belongs to a legitimate company (Västkupan Fastigheter).

**The PDF that Wasn’t**

This is what the downloaded “PDF” looks like:

![Hex view of Daupinslenj.pdf](https://media.netresec.com/images/Daupinslenj-pdf-xxd_1170x383.webp)

So, what’s up with all that “171171” data? Let’s XOR with “711” and see what we get.

![Hex view of decrypted Daupinslenj.pdf](https://media.netresec.com/images/Daupinslenj-decoded-xxd_1170x383.webp)

The downloaded PDF turns out to be a .NET DLL file with MD5 38d29f5ac47583f39a2ff5dc1c366f7d. This is the file that was injected into the otherwise legitimate InstallUtil process. Some PureLogs droppers use RegAsm.exe instead of InstallUtil though (see [JoeSandbox](https://www.joesandbox.com/analysis/1689536/0/html) and [any.run](https://app.any.run/tasks/abe65316-704a-45ab-8840-c2d60966fdf0)).

**IOC List**

Droppers (MD5):

* 711d9cbf1b1c77de45c4f1b1a82347e6
* 6ff95e302e8374e4e1023fbec625f44b
* e6d7bbc53b718217b2de1b43a9193786
* a9bc0fad0b1a1d6931321bb5286bf6b7
* 09bb5446ad9055b9a1cb449db99a7302

Dropper TLS handshake signatures:

* JA3: 3b5074b1b5d032e5620f69f9f700ff0e
* JA4: t12d210700\_76e208dd3e22\_2dae41c691ec

Payload URLs:

* hxxps://www.vastkupan[.]com/wp-admin/js/Cicdwkknms.pdf
* hxxps://www.vastkupan[.]com/wp-admin/js/Daupinslenj.pdf
* hxxps://www.new.eventawardsrussia[.]com/wp-includes/Ypeyqku.pdf

Payloads (MD5):

* ab250bb831a9715a47610f89d0998f86 (Cicdwkknms.pdf)
* cec53e8df6c115eb7494c9ad7d2963d4 (Daupinslenj.pdf)
* eedc8bb54465bd6720f28b41f7a2acf6 (Ypeyqku.pdf)

Decrypted payloads:

* MD5: 38d29f5ac47583f39a2ff5dc1c366f7d
* SHA1: fc8b0ee149027c4c02f7d44cc06cade3222bb6b6
* SHA256: 8d7729ca0b25a677287076b4461304a21813e6f15053e190975512e58754988f

PureLogs C2:

* 91.92.120.101:62520 (old)
* 91.92.120.101:65535 (new)

**Update 2025-07-16**

Additional PureLogs payloads have been found on vastkupan.com.

Payload URLs:

* hxxps://www.vastkupan[.]com/wp-admin/js/Cxqyoub.dat
* hxxps://www.vastkupan[.]com/wp-admin/js/Qlwxqgsag.dat

Cxqyoub.dat is decrypted by XOR-ing with "414".

![Hex view of Cxqyoub.dat](https://media.netresec.com/images/Cxqyoub-dat_1025x310.webp)

Qlwxqgsag.dat is a DLL with reversed content.

![Hex view of Qlwxqgsag.dat](https://media.netresec.com/images/Qlwxqgsag-dat_1055x310.webp)

Payloads (MD5):

* 22a304ea9c006e2ccb2f6110c4d3f53f (Cxqyoub.dat)
* d5b6607ee4718506eb4970c02cf286cd (XOR decrypted DLL from Cxqyoub.dat)
* 062d2a5906fac4c2ef07c6b43141e19c (Qlwxqgsag.dat)
* 40624de03bc3c53331b6e903d9e3860f (DLL from reversed Qlwxqgsag.dat)

C2 server:

* 91.92.120.102:62050

See [JoeSandbox](https://www.joesandbox.com/analysis/1735925/0/html) and [any.run](https://app.any.run/tasks/652f1021-12fb-4ab9-81fb-83bcff5e170a) for sandbox executions of the dropper aa06d06ddb6d3801c70cc1991f393112 (retrieves Cxqyoub.dat),
and [JoeSandbox](https://www.joesandbox.com/analysis/1738261/0/html) and [any.run](https://app.any.run/tasks/c1300bb8-d66d-40a3-987f-781d01d39a66) for c45a95dc7ebc8c78217cd996a8f6dda7 (gets Qlwxqgsag.dat).

**Update 2025-07-21**

Yet another PureLogs payload found on vastkupan.com.

* Dropped by: 031a9c2f44881f4db1c6f6d88a540206
* URL of encrypted DLL: hxxp://www.vastkupan[.]com/wp-admin/js/Kplbc.pdf
* Encrypted DLL MD5: 6ed3c9b70ca02d1c558d1ef9a8aaab77
* C2: 65.108.24.103:62050

Sandbox executions are available on [JoeSandbox](https://www.joesandbox.com/analysis/1740959/0/html) and [any.run](https://app.any.run/tasks/451bf60e-aa0f-4d59-bdfb-35e0637b152a).

**Update 2025-07-30**

Additional encrypted PureLogs DLLs found on vastkupan.com

* Dropped by: 67861615d765d0c59d65e8d4454e5ffc
* URL of encrypted DLL: hxxps://www.vastkupan[.]com/wp-admin/js/Qytqk.pdf
* Encrypted DLL MD5: 668a42bdfd253e0d54716cd115479b9f
* C2: 91.92.120.102:62050 (same as Cxqyoub.dat and (Qlwxqgsag.dat)

* Dropped by: 031a9c2f44881f4db1c6f6d88a540206
* URL of encrypted DLL: hxxps://www.vastkupan[.]com:443/wp-admin/js/Kplbc.pdf
* Encrypted DLL MD5: 6ed3c9b70ca02d1c558d1ef9a8aaab77
* C2: 65.108.24.103:62050

* Dropped by: 07ff4006101f117aa4f198c984a45137
* URL of encrypted DLL: hxxps://www.vastkupan[.]com/wp-admin/js/Pnnvrpjewlq.vdf
* Encrypted DLL MD5: 98cf831688941cc8bccfe1e8a33c9c16

* Dropped by: a1fd8053b49442028d66e3adea550d19
* URL of encrypted DLL: hxxps://www.vastkupan[.]com/wp-admin/js/Niose.wav
* Encrypted DLL MD5: 067086aff11080357b92931e96ecebae

* Dropped by: 3cf704e64cbba6560663ec45ce2dabc2
* URL of encrypted DLL: hxxps://www.vastkupan[.]com:443/wp-admin/js/Frfkft.vdf
* Encrypted DLL MD5: c9bac721c9b6f2900fd3d8ed922bc759
* C2: 91.92.120.101:7705

* Dropped by: 486d6c9cbdb638f9d574c58459676ed9
* URL of encrypted DLL: hxxps://www.vastkupan[.]com/wp-admin/js/Skrcygatz.dat
* Encrypted DLL MD5: a3cf5108315a06d564c97c8367994fd1
* C2: 216.250.252.231:2080

**Update 2025-07-31**

Turns out the whole /wp-admin/js/ directory on Västkupan's website allows directory listing.
Among the files in that directory is "New PO 102456688.exe", which drops PureLogs.

![Open directory listing on vastkupan.com](https://media.netresec.com/images/vastkupan-open-dir_1479x767.webp)

* Filename: New PO 102456688.exe
* MD5: b2647b263c14226c62fe743dbff5c70a
* C2: 147.124.219.201:65535

See executions on [Tria.ge](https://tria.ge/250730-za8khswpx4) and [any.run](https://app.any.run/tasks/67a3c69f-a20b-47e1-8358-450a3e7724b2) for details.

Posted by Erik Hjelmvik on Wednesday, 02 July 2025 11:52:00 (UTC/GMT)

Tags:
#[PureLogs](/?page=Blog&tag=PureLogs)​
#[PureCoder](/?page=Blog&tag=PureCoder)​
#[3b5074b1b5d032e5620f69f9f700ff0e](/?page=Blog&tag=3b5074b1b5d032e5620f69f9f700ff0e)​
#[JoeSandbox](/?page=Blog&tag=JoeSandbox)​

Short URL:
<https://netresec.com/?b=257eead>

### Recent Posts

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

» [PureRAT = Resolv...