---
title: Applocker bypass on Lenovo machines – The curious case of MFGSTAT.zip
url: https://oddvar.moe/2025/07/03/applocker-bypass-on-lenovo-machines-the-curious-case-of-mfgstat-zip/
source: Oddvar Moe's Blog
date: 2025-07-04
fetch_date: 2025-10-06T23:55:54.379944
---

# Applocker bypass on Lenovo machines – The curious case of MFGSTAT.zip

[Skip to content](#content)

Menu

* [Home](/)
* [About](https://oddvar.moe/about/)
* [Presentations](https://oddvar.moe/presentations/)
* [Articles](https://oddvar.moe/articles/)
* [AppLocker Case study](https://oddvar.moe)
  + [AppLocker – Case study – Part 1](https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/)
  + [AppLocker – Case study – Part 2](https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/)
  + [AppLocker – Hardening – Part 1](https://oddvar.moe/2017/12/13/harden-windows-with-applocker-based-on-case-study-part-1/)
  + [AppLocker – Hardening – Part 2](https://oddvar.moe/2017/12/21/harden-windows-with-applocker-based-on-case-study-part-2/)
  + [AppLocker for admins – Does it work?](https://oddvar.moe/2018/07/27/applocker-for-admins-does-it-work/)
  + [Bypassing AppLocker as an admin](https://oddvar.moe/2019/02/01/bypassing-applocker-as-an-admin/)
  + [AppLocker – Making sure that local rules are removed](https://oddvar.moe/2018/09/28/applocker-making-sure-that-local-rules-are-removed/)
  + [Real whitelisting attempt using AppLocker](https://oddvar.moe/2018/05/14/real-whitelisting-attempt-using-applocker/)
  + [Ultimate AppLocker Bypass List](https://github.com/api0cradle/UltimateAppLockerByPassList)
* [Previous Blogs](https://oddvar.moe)
  + [MSItpros – Waybackmachine](https://web.archive.org/web/20201101151155/http%3A//msitpros.com/)
  + [moe.am – Waybackmachine](https://web.archive.org/web/20120625102124/http%3A//www.moe.am/)

[Oddvar Moe's Blog](https://oddvar.moe/)

Notes from My adventures with Windows security

# Applocker bypass on Lenovo machines – The curious case of MFGSTAT.zip

Posted on [3 Jul 20253 Jul 2025](https://oddvar.moe/2025/07/03/applocker-bypass-on-lenovo-machines-the-curious-case-of-mfgstat-zip/) by [Oddvar Moe [MVP]](https://oddvar.moe/author/oddvarhmoe/)

This blogpost is about a minor discovery I made regarding a writeable file inside the Windows folder that is present on Lenovo machines. Initially when I found it I thought it was only a handful of Lenovo machines, but it seems as if this affects all variants. Since this can be abused as an AppLocker bypass I thought I would write about it here instead of the [TrustedSec blog](https://trustedsec.com/blog/?author_filter=oddvar-moe.117907), since my personal blog is mostly about AppLocker.

## ISSUE

When I ran my [accesschk script](https://gist.github.com/api0cradle/95cd51fa1aa735d9331186f934df4df9) I found that the file was writeable for any authenticated user.

![](https://oddvar.moe/wp-content/uploads/2025/07/image-1.png?w=1024)

I then looked at the ACL’s in Explorer just to verify.

![](https://oddvar.moe/wp-content/uploads/2025/07/image.png?w=746)

This confirms that a standard authenticated user can write to and execute this file. If you have deployed [AppLocker default rules](https://oddvar.moe/2017/12/13/harden-windows-with-applocker-based-on-case-study-part-1/) in your environment it will allow execution from the anything under the **C:\Windows** folder and than the **mfgstat.zip** becomes and issue because a standard user can then exploit this. To exploit this as a bypass the user has to add the contents of a binary file into an alternate datastream and then execute it. I have not been able to overwrite the zip file directly (might be possible). You can find various methods of doing alternate data stream adding and execution [here](https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f). In this example I choose to execute autoruns.exe from Sysinternals. First I placed the autoruns.exe file inside **c:\temp** and then I used the following command to add it as an alternate data stream to the **mfgstat.zip** file:

```
type c:\temp\autoruns.exe > c:\windows\mfgstat.zip:this
```

After successfully adding it, I executed it using the **Appvlp.exe** ([Details on lolbas](https://lolbas-project.github.io/lolbas/OtherMSBinaries/Appvlp/)) file using the following command

```
"C:\Program Files (x86)\Microsoft Office\root\Client\appvlp.exe" c:\Windows\mfgstat.zip:this
```

To make this more enjoyable I have created a quick video that shows it.

## Story

I originally made this discovery on a Lenovo machine I had back in 2019. I actually tweeted about it at the time: <https://x.com/Oddvarmoe/status/1126473466235035650>. Back then I thought this was just on my specific brand of Lenovo X1 Extreme, but once I rechecked this on my new Lenovo in 2025 I was surprised that I had the same issue there (<https://x.com/Oddvarmoe/status/1882026713397522873>). This time however I decided to send an email to the Lenovo PSIRT about it and see if they would fix it. They responded promptly, but they decided to not put out a fix, instead a guidance on how to remove it. From a corporate perspective I guess most companies perform their own deployment of operating systems and not rely on the operating system already present on the machine that comes default from Lenovo. Deploying the operating system based on the company standard image would remove this file since this is specific to the default Lenovo operating system image shipped with the machines.

## FIX

Lenovo provided a guidance for fixing this issue here: <https://support.lenovo.com/us/en/product_security/HT517812>. The guidance is simply to delete the C:\Windows\MFGSTAT.zip file using one of the three explained methods. If you are in a corporate environment you could also leverage Group Policy Preferences/SCCM or other tools to remove the file.

## Conclusion

My conclusion is that everyone should be checking their filesystems when you are deploying or have deployed AppLocker. It is really quick to miss out on small things like this. If you are more interested in AppLocker I did a webinar a while back that would be worth checking out. Hope you found this post useful.

Part 1:

Part 2:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://oddvar.moe/2025/07/03/applocker-bypass-on-lenovo-machines-the-curious-case-of-mfgstat-zip/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://oddvar.moe/2025/07/03/applocker-bypass-on-lenovo-machines-the-curious-case-of-mfgstat-zip/?share=facebook)

Like Loading...

### *Related*

Tagged [ADS](https://oddvar.moe/tag/ads/), [AppLocker](https://oddvar.moe/tag/applocker/), [bypass](https://oddvar.moe/tag/bypass/), [research](https://oddvar.moe/tag/research/), [security](https://oddvar.moe/tag/security/), [technology](https://oddvar.moe/tag/technology/), [windows](https://oddvar.moe/tag/windows/)

## Post navigation

[Previous Post A small discovery about AppLocker](https://oddvar.moe/2019/05/29/a-small-discovery-about-applocker/)

## 11 thoughts on “Applocker bypass on Lenovo machines – The curious case of MFGSTAT.zip”

1. Pingback: [Writable File in Lenovo’s Windows Directory Enables a Stealthy AppLocker Bypass](https://cybersecuritynews.com/writable-file-in-lenovos-windows-directory/)
2. Pingback: [Writable File in Lenovo’s Windows Directory Enables a Stealthy AppLocker Bypass – GNN](https://gnn.vircom.in/2025/07/05/writable-file-in-lenovos-windows-directory-enables-a-stealthy-applocker-bypass/)
3. Pingback: [Critical Writable File in Lenovo’s Windows Directory Lets Attackers Bypass AppLocker](https://cyberpress.org/critical-writable-file-in-lenovos-windows-directory-lets-attackers-bypass-applocker/)
4. Pingback: [Writable File in Lenovo’s Windows Directory Enables a Stealthy AppLocker Bypass – serisec](https://serisec.com/index.php/2025/07/06/writable-file-in-lenovos-windows-directory-enables-a-stealthy-applocker-bypass/)
5. Pingback: [Lenovo sfătuiește utilizatorii să șteargă un fișier Windows pentru a preveni bifurcarea AppLocker – Cyber Insider](https://cyberinsider.ro/lenovo-sfatuieste-utilizatorii-sa-stearga-un-fisier-windows-pentru-a-preveni-bifurcarea-applocker/)
6. Pingback: [This Week in Security: Anthropic, Coinbase, and Oops Hunting – The Latest...