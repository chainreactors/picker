---
title: Microsoft's Coreutils for Windows, (Thu, Jun 4th)
url: https://isc.sans.edu/diary/rss/33048
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-04
fetch_date: 2026-06-05T06:14:14.837920
---

# Microsoft's Coreutils for Windows, (Thu, Jun 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33044)

Click HERE to learn more about classes Didier is teaching for SANS

# [Microsoft's Coreutils for Windows](/forums/diary/Microsofts%2BCoreutils%2Bfor%2BWindows/33048/)

**Published**: 2026-06-04. **Last Updated**: 2026-06-04 06:10:44 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Microsofts%2BCoreutils%2Bfor%2BWindows/33048/#comments)

I've been using the GnuWin32 CoreUtils for Windows for many years now (it gives you many \*nix core commands on Windows).

Microsoft has just [released](https://github.com/microsoft/coreutils) their coreutils version for Windows.

You can install them with a winget command (winget install Microsoft.Coreutils) or with the [installer released on GitHub](https://github.com/microsoft/coreutils/releases).

It takes just a few clicks:

![](https://isc.sans.edu/diaryimages/images/20260604-074226.png)

![](https://isc.sans.edu/diaryimages/images/20260604-074240.png)

![](https://isc.sans.edu/diaryimages/images/20260604-074312.png)

It installs a single executable compiled with Rust (coreutils.exe) in the program files folder:

![](https://isc.sans.edu/diaryimages/images/20260604-074636.png)

And each individual command is a hard link to this executable:

![](https://isc.sans.edu/diaryimages/images/20260604-074703.png)

Here is the full list of commands:

```

arch.cmd
b2sum.cmd
base32.cmd
base64.cmd
basename.cmd
basenc.cmd
cat.cmd
cksum.cmd
comm.cmd
cp.cmd
csplit.cmd
cut.cmd
date.cmd
df.cmd
dirname.cmd
du.cmd
echo.cmd
env.cmd
expr.cmd
factor.cmd
false.cmd
find.cmd
fmt.cmd
fold.cmd
grep.cmd
head.cmd
hostname.cmd
join.cmd
link.cmd
ln.cmd
ls.cmd
md5sum.cmd
mkdir.cmd
mktemp.cmd
mv.cmd
nl.cmd
nproc.cmd
numfmt.cmd
od.cmd
pathchk.cmd
pr.cmd
printenv.cmd
printf.cmd
ptx.cmd
pwd.cmd
readlink.cmd
realpath.cmd
rm.cmd
rmdir.cmd
seq.cmd
sha1sum.cmd
sha224sum.cmd
sha256sum.cmd
sha384sum.cmd
sha512sum.cmd
shuf.cmd
sleep.cmd
sort.cmd
split.cmd
stat.cmd
sum.cmd
tac.cmd
tail.cmd
tee.cmd
test.cmd
touch.cmd
tr.cmd
true.cmd
truncate.cmd
tsort.cmd
unexpand.cmd
uniq.cmd
unlink.cmd
uptime.cmd
wc.cmd
xargs.cmd
yes.cmd
```

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/Microsofts%2BCoreutils%2Bfor%2BWindows/33048/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33044)

### Comments

I ran winget and it installed the programs under program files\coreutils\bin but did not put that in the path. I didn't see the setup windows you show, either
PS C:\WINDOWS\system32> winget install Microsoft.Coreutils
The `msstore` source requires that you view the following agreements before using.
Terms of Transaction: https://aka.ms/microsoft-store-terms-of-transaction
The source requires the current machine's 2-letter geographic region to be sent to the backend service to function properly (ex. "US").

Do you agree to all the source agreements terms?
[Y] Yes [N] No: y
Found Coreutils for Windows [Microsoft.Coreutils] Version 2026.5.29
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.
Downloading https://github.com/microsoft/coreutils/releases/download/v2026.5.29/coreutils-2026.5.29-x64.exe
██████████████████████████████ 4.86 MB / 4.86 MB
Successfully verified installer hash
Starting package install...
Successfully installed

#### afbach

#### Jun 4th 2026 13 hours ago

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)