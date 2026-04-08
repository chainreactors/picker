---
title: A Little Bit Pivoting: What Web Shells are Attackers Looking for&#x3f;, (Tue, Apr 7th)
url: https://isc.sans.edu/diary/rss/32874
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-07
fetch_date: 2026-04-08T04:39:02.112568
---

# A Little Bit Pivoting: What Web Shells are Attackers Looking for&#x3f;, (Tue, Apr 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32870)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [A Little Bit Pivoting: What Web Shells are Attackers Looking for?](/forums/diary/A%2BLittle%2BBit%2BPivoting%2BWhat%2BWeb%2BShells%2Bare%2BAttackers%2BLooking%2Bfor/32874/)

**Published**: 2026-04-07. **Last Updated**: 2026-04-07 18:28:16 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/A%2BLittle%2BBit%2BPivoting%2BWhat%2BWeb%2BShells%2Bare%2BAttackers%2BLooking%2Bfor/32874/#comments)

Webshells remain a popular method for attackers to maintain persistence on a compromised web server. Many "arbitrary file write" and "remote code execution" vulnerabilities are used to drop small files on systems for later execution of additional payloads. The names of these files keep changing and are often chosen to "fit in" with other files. Webshells themselves are also often used by parasitic attacks to compromise a server. Sadly (?), attackers are not always selecting good passwords either. In some cases, webshells come with pre-set backdoor credentials, which may be overlooked by a less sophisticated attacker.

I noticed first requests for a particular URL: /turkshell.php . This URL is linked to a well-known webshell. On this particular day, only four IPs were scanned for it:

20.48.232.178, 20.215.65.23, 51.12.84.116, 51.103.130.249

It is a little bit odd, but all four appear to be assigned to Microsoft. There may be an attacker targeting systems inside Microsoft's cloud environment. Or all four are used by the same (compromised?) organization.

Next, I queried our database to see which other URLs these IP addresses probed, and ended up with 287(!) hits. Here are the top 10:

| URL | Count |
| --- | --- |
| /wp-content/ | 45 |
| /ms-edit.php | 44 |
| /fe5.php | 43 |
| /wp-content/admin.php | 39 |
| /av.php | 36 |
| /wp-content/plugins/hellopress/wp\_filemanager.php | 27 |
| /wp-content/themes/index.php | 23 |
| /k.php | 23 |
| /goods.php | 23 |
| /222.php | 23 |

One common theme was the use of the prefix "wp-", likely to better fit in on WordPress sites. The scans also included "non-webshell" URLs like "/wp-content/plugins/hellopress/wp\_filemanager.php," which may be useful for fingerprinting the site or may be vulnerable to being used as or deployed as webshells.

What should you do to protect yourself from webshells?

1. Don't have any remote code execution or file upload vulnerabilities (yes... easy to say)
2. Restrict permissions to not allow file uploads to your document root (sadly, in particular CMSs like WordPress sometimes have to be able to do so)
3. Monitor the file system for changes

What does not work (or not work very well): Scanning for specific filenames. The 287 files these four IPs looked for make a rather incomplete list. I will add it below, but please don't consider it complete. I am not even sure it is worth the effort to scan for these specific filenames. You may also get some false positives. Not every item on this list is a webshell, and some sites may use identical filenames for regular content.

> /.mopj.php
> /.tmb/8.php
> /.tmb/a5.php
> /.tmb/nano.php
> /.well-known/
> /.well-known/7.php
> /.well-known/8.php
> /.well-known/a5.php
> /.well-known/f35.php
> /.well-known/simple.php
> /.yuf.php
> //a1.php
> //aa.php
> //about.php
> //admin.php
> //admina.php
> //adminfuns.php
> //av.php
> //cacheee.php
> //cgi-bin/index.php
> //edit.php
> //f6.php
> //fetch.php
> //inputs.php
> //wp-content/admin.php
> //wp-content/uploads/2021/02/index.php
> //wp-includes/css/dist/
> //wp-includes/css/index.php
> //wp-includes/js/jquery/
> //wp-includes/l10n/
> //wp-mter.php
> //xwpg.php
> /1.php
> /10.php
> /100.php
> /111.php
> /1111.php
> /1111.php?p=
> /13.php
> /133927/8.php
> /19.php
> /2.php
> /2026w.php
> /222.php
> /2e754/a5.php
> /3.php
> /4.php
> /403.php
> /404.php
> /5.php
> /6.php
> /66.php
> /7.php
> /8.php
> /9.php
> /a1.php
> /a2.php
> /a5.php
> /aa.php
> /aaa.php
> /aaa.php?p=
> /abc.php
> /abcd.php
> /about.php
> /about2.php
> /acp.php
> /admin.php
> /admin.php.
> /admin/controller/extension/extension/ultra.php
> /adminfuns.php
> /administrator/7.php
> /alfa.php
> /alfashell.php
> /aligk.php
> /alpha.php
> /an.php
> /as.php
> /ass.php
> /autoload\_classmap.php
> /av.php
> /aw.php
> /axx.php
> /bal.php
> /bb.php
> /BDKR28WP.php
> /bengi.php
> /bgymj.php
> /bless.php
> /bless4.php
> /bogles.php
> /bs1.php
> /bthil.php
> /bypltspd.php
> /byrgo.php
> /cabs.php
> /cache.php
> /cacheee.php
> /cgi-bin/
> /cgi-bin/7.php
> /cgi-bin/8.php
> /cgi-bin/a5.php
> /cgi-bin/index.php
> /chosen.php
> /class-t.api.php
> /class.php
> /class19.php
> /class20.php
> /classwithtostring.php
> /classwithtostring.php?p=
> /cli/7.php
> /config.php
> /configPCJ/f35.php
> /content.php
> /control.php
> /css/autoload\_classmap.php
> /defaults.php
> /dev.php
> /edit.php
> /eee.php
> /esp.php
> /ew.php
> /f35\_S.php
> /f35.php
> /f6.php
> /fe5.php
> /fetch.php
> /fff.php
> /fi.php
> /file.php
> /file18.php
> /file21.php
> /file31.php
> /file48.php
> /file61.php
> /fine.php
> /flower.php
> /ftde.php
> /function/function.php
> /fvvff.php
> /fx.php
> /g.php
> /gecko-new.php
> /gelay.php
> /gettest.php
> /ghhjh.php
> /god4m.php
> /goods.php
> /gptsh.php
> /gssdd.php
> /hplfuns.php
> /images/simple.php
> /in.php
> /includes/7.php
> /index.php
> /index/8.php
> /index/function.php
> /inege.php
> /info.php
> /inputs.php
> /ioxi-o.php
> /item.php
> /jp.php
> /k.php
> /kbfr.php
> /kj.php
> /lock360.php
> /makeasmtp.php
> /makeasmtp.php?p=
> /mari.php
> /moon.php
> /motu.php
> /ms-edit.php
> /nano.php
> /new.php
> /NewFile.php
> /no1.php
> /no18.php
> /o.php
> /ok.php
> /ol.php
> /pcp/simple.php
> /plss3.php
> /plugins.php
> /plugins/7.php
> /prv8.php
> /qqa.php
> /randkeyword.PhP7
> /read.php
> /rip.php
> /s.php
> /sbhu.php
> /seo.php
> /sf.php
> /simple.php
> /style.php
> /swallowable.php
> /system.php
> /tea.php
> /test1.php
> /themes.php
> /tinyfilemanager.php
> /tinyfilemanager.php?p=
> /tmp.php
> /turkshell.php
> /txets.php
> /update/f35.php
> /uploads/
> /uuu.php
> /vee.php
> /w2025.php
> /we.php
> /well-known/nano.php
> /wen.php
> /wi.php
> /wk/index.php
> /wordpress/8.php
> /wp-act.php
> /wp-admin/8.php
> /wp-admin/a.php
> /wp-admin/alfa.php
> /wp-admin/css/bolt.php
> /wp-admin/css/colors
> /wp-admin/css/colors/ectoplasm/
> /wp-admin/images/
> /wp-admin/js/
> /wp-admin/js/fi.php
> /wp-admin/js/widgets/
> /wp-admin/nano.php
> /wp-admin/network/index.php
> /wp-admin/user/index.php
> /wp-blog.php
> /wp-conf.php
> /wp-content/
> /wp-content/8.php
> /wp-content/a5.php
> /wp-content/admin.php
> /wp-content/plugins/core-plugin/include.php
> /wp-content/plugins/hellopress/wp\_filemanager.php
> /wp-content/plugins/index.php
> /wp-content/plugins/pwnd/as.php
> /wp-content/plugins/WordPressCore/
> /wp-content/themes/
> /wp-content/themes/admin.php
> /wp-content/themes/hideo/network.php
> /wp-content/themes/index.php
> /wp-content/uploads/
> /wp-content/uploads/2021/02/index.php
> /wp-content/uploads/index.php
> /wp-good.php
> /wp-includes/
> /wp-includes/8.php
> /wp-includes/a5.php
> /wp-includes/css/dist/
> /wp-includes/css/index.php?p=
> /wp-includes/html-api/
> /wp-includes/ID3/
> /wp-includes/images/
> /wp-includes/IXR/test1.php
> /wp-includes/js/crop/cropper.php
> /wp-includes/js/jquery/
> /wp-includes/l10n/
> /wp-includes/nano.php
> /wp-includes/PHPMailer/
> /wp-includes/Requests/src/Response/about.php
> /wp-includes/SimplePie/
> /wp-includes/Text/Diff/Engine/about.php
> /wp-kd4xalrg7m.php
> /wp-login.php
> /wp-michan.php
> /wp-mter.php
> /wp-the.php
> /wp-trackback.php
> /wp-update.php
> /wp.php
> /wp1.php
> /wpx.php
> /ws.php
> /x1da....