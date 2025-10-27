---
title: Linux LOLBins Applications Available in Windows, (Sat, Dec 3rd)
url: https://isc.sans.edu/diary/rss/29296
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-04
fetch_date: 2025-10-04T00:29:27.035068
---

# Linux LOLBins Applications Available in Windows, (Sat, Dec 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29294)
* [next](/diary/29298)

# [Linux LOLBins Applications Available in Windows](/forums/diary/Linux%2BLOLBins%2BApplications%2BAvailable%2Bin%2BWindows/29296/)

**Published**: 2022-12-03. **Last Updated**: 2022-12-03 20:09:25 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Linux%2BLOLBins%2BApplications%2BAvailable%2Bin%2BWindows/29296/#comments)

Some useful Linux applications that are now part of default installation in Windows 10, Windows Server 2019/2022 (LOLBins - Living Off the Land Binaries).

**cURL**

The first one is curl which can be very useful for scripting to download or upload files and/or use with a username/password (curl --help) and save the output either to a new filename or the same:

C:\Users\guy\Downloads>curl https://handlers.sans.edu/gbruneau/scripts/Example.csv -o Example.csv
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  230k  100  230k    0     0  1443k      0 --:--:-- --:--:-- --:--:-- 1461k

**tar**

The next application is tar (tar --help) is used to store, extract and manipulate archive files. Let’s take the previous file Example.csv, archive and compress it and then review the result. Using the same options as Linux will use gzip compression and create the file Example.tgz:

-c Create  -r Add/Replace  -t List  -u Update  -x Extract
-f <filename>  Location of archive
-v Verbose
-z, -j, -J, --lzma  Compress archive with gzip/bzip2/xz/lzma

C:\Users\guy\Downloads>tar zcvf example.tgz Example.csv
C:\Users\guy\Downloads>dir Example.\*
 Volume in drive C is Starbase
 Volume Serial Number is EEB2-C010

 Directory of C:\Users\guy\Downloads

12/03/2022  01:39 PM           236,526 Example.csv
12/03/2022  01:46 PM            38,247 example.tgz

To extract the file(s), using the following command:

C:\Users\guy\Downloads>tar xvf example.tgz
x Example.csv

To view the content of the archive:

c:\Users\guy\Downloads>tar ztvf Example.tgz
-rw-rw-rw-  0 0      0      236526 Dec 03 13:39 Example.csv

**PktMON**

This tool is a Windows original which I think is worth mentionning again. I wrote a diary in May 2020 [[1](https://isc.sans.edu/diary/Windows%2B10%2BBuiltin%2BPacket%2BSniffer%2BPktMon/26186)] on how to use PktMON to capture packets using this tool in Windows 10. The resulting packet capture can be converted into a pcapng format to be read later with Wireshark.

**OpenSSH**

The last one that is always useful is ssh/scp/sftp which is using the OpenSSH. The location of the OpenSSH binaries is: C:\Windows\System32\OpenSSH

ssh
scp
sftp
ssh-add.exe
ssh-agent.exe
ssh-keygen.exe
ssh-keyscan.exe

First lest create some public/private keys using the default user home directory:

C:\Users\guy>ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\guy/.ssh/id\_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\guy/.ssh/id\_rsa.
Your public key has been saved in C:\Users\guy/.ssh/id\_rsa.pub.
[...]
C:\Users\guy>cd .ssh

C:\Users\guy\.ssh>dir
 Volume in drive C is Starbase
 Volume Serial Number is EEB2-C010

 Directory of C:\Users\guy\.ssh

12/03/2022  02:10 PM    <DIR>          .
12/03/2022  02:10 PM    <DIR>          ..
12/03/2022  02:10 PM             2,655 id\_rsa
12/03/2022  02:10 PM               567 id\_rsa.pub
11/10/2022  01:49 PM               545 known\_hosts

Now ssh/scp/sftp is ready to use with a public key to a remote server. By default OpenSSH doesn't run the SSH listener service but it can be configured using the information posted [here](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_server_configuration) in a Microsoft article.

[1] https://isc.sans.edu/diary/Windows+10+Builtin+Packet+Sniffer+PktMon/26186
[2] https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh\_overview
[3] https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh\_server\_configuration
-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [curl](/tag.html?tag=curl) [LOLBins](/tag.html?tag=LOLBins) [PktMon](/tag.html?tag=PktMon) [scp](/tag.html?tag=scp) [sftp](/tag.html?tag=sftp) [ssh](/tag.html?tag=ssh) [tar](/tag.html?tag=tar)

[0 comment(s)](/diary/Linux%2BLOLBins%2BApplications%2BAvailable%2Bin%2BWindows/29296/#comments)

* [previous](/diary/29294)
* [next](/diary/29298)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)