---
title: My howto script
url: https://gynvael.coldwind.pl/?id=771
source: gynvael.coldwind//vx.log (en)
date: 2023-08-08
fetch_date: 2025-10-04T12:00:48.208386
---

# My howto script

# [![gynvael.coldwin//vx.log](/img/logo.gif)](/?blog=1)

![](/images/something_suspicious.png)

[Available for Consulting and Projects](https://hexarcana.ch/?utm=gyn-blog)
[hackArcana (edu+CTF)](https://hackarcana.com/?utm=gyn-blog-w)

![](/img/gynvael-close.jpg)

* [Return to dashboard ⇪](/)

### *Sections*

* **lang**: [![PL](/images/lang_pl.png)](?blog=1&lang=pl) | [![EN](/images/lang_en.png)](?blog=1&lang=en)
* **RSS**: [![RSS PL](/images/lang_pl.png)](/rss_pl.php) | [![RSS EN](/images/lang_en.png)](/rss_en.php)
* [About me](?id=50)
* [Tools](?id=182)
* [→ YT YouTube (EN)](https://youtube.com/c/GynvaelEN)
* [→ D Discord](/discord)* [→ M Mastodon](https://infosec.exchange/%40gynvael)* [→ T Twitter](https://twitter.com/gynvael)* [→ GH GitHub](https://github.com/gynvael)

        [![](/img/hA-logo.png)](https://hackarcana.com)

        [My edu+CTF site](https://hackarcana.com)

        [![](/img/hexarcana160_2.png)](https://hexarcana.ch)

        [My consulting company](https://hexarcana.ch)

        [![](/img/po_issue_5_rbanner.png)](https://pagedout.institute/)

        [Paged Out! zine](https://pagedout.institute/)

        [![](/img/ds_logo_160.jpg)](https://dragonsector.pl/)

        [Dragon Sector CTF Team](https://dragonsector.pl/)

### *Links / Blogs*

* **Security/Hacking:**
  + [j00ru's blog](https://j00ru.vexillium.org/)
  + [lcamtuf's thing](https://lcamtuf.substack.com/)
  + [pi3's blog](http://blog.pi3.com.pl/)
  + [tavis ormandy's site](https://lock.cmpxchg8b.com/)
  + [pawel golen's blog](http://wampir.mroczna-zaloga.org/)
  + [zaufana trzecia strona](http://zaufanatrzeciastrona.pl/)
  + [niebezpiecznik](https://niebezpiecznik.pl/)
  + [sekurak](https://sekurak.pl/)
* **Reverse Eng./Low-Level:**
  + [security news](https://www.secnews.pl/)
  + [rev3rsed](http://rev3rsed.blogspot.com/)
* **Programming/Code:**
  + [adam sawicki](http://asawicki.info/)

### *Posts*

* [Paged Out! prints are here, and so is #7 CFP deadline,](?id=805)
* [CONFidence 2025 is next week,](?id=804)
* [No, CTRL+D in Linux terminal doesn't send EOF signal,](?id=801)
* [New edu platform and 'Sanitization and Validation and Escaping, Oh My!' article,](?id=800)
* [On hackers, hackers, and hilarious misunderstandings,](?id=799)
* [Paged Out! #5 is out,](?id=797)
* [CVEs of SSH talk this Thursday,](?id=796)
* [Debug Log: Internet doesn't work (it was the PSU),](?id=793)
* [FAQ: The tragedy of low-level exploitation,](?id=791)
* [Solving Hx8 Teaser 2 highlight videos!,](?id=789)
* [→ see all posts on main page](/)

// copyright © Gynvael Coldwind
// design & art by Xa
// logo font (birdman regular) by utopiafonts / Dale Harris

/\* the author and owner of this blog hereby allows anyone to test the security of this blog (on HTTP level only, the server is not mine, so let's leave it alone ;>), and try to break in (including successful breaks) without any consequences of any kind (DoS attacks are an exception here) ... I'll add that I planted in some places funny photos of some kittens, there are 7 of them right now, so have fun looking for them ;> let me know if You find them all, I'll add some congratz message or sth ;> \*/

**Vulns found in blog:**
\* XSS *(pers, user-inter)* by ged\_
\* XSS *(non-pers)* by Anno & Tracerout
\* XSS *(pers)* by Anno & Tracerout
\* Blind SQLI by Sławomir Błażek
\* XSS *(pers) by* Sławomir Błażek

2023-08-07:

## [My howto script](?id=771)

ai

Since I started my coding livestreams again there is one common question, which I wanted to address in this blogpost: what is this weird howto command I'm using?

`$ howto convert a set of jpegs into a pdf, assume 90 dpi A4 page
convert -quality 100 -density 90x90 -page A4 *.jpg output.pdf
$ howto block any access to tcp port 1234 using iptables
sudo iptables -A INPUT -p tcp --dport 1234 -j DROP
$ howto zoom in my webcam
v4l2-ctl --set-ctrl=zoom_absolute=300
$ howto encrypt a file using openssl with aes in authenticated mode
openssl enc -aes-256-gcm -salt -in inputfile -out outputfile`

And yes, that is just ChatGPT over [API](https://platform.openai.com/docs/api-reference). It's actually a super simple Python script based on their examples. See for yourself:

`` #!/usr/bin/env python
import openai
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
# !!!You need an API key!!!
# https://platform.openai.com/account/api-keys
with open(f"{dir_path}/api_key.txt") as f:
openai.api_key = f.read().strip()
arg = ' '.join(sys.argv[1:])
r = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
#model="gpt-4",
messages=[
{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
{"role": "user", "content": f"Answer with only the actual command without any intro or explanation. What is the ubuntu command line command to {arg}"}
]
)
text = r["choices"][0]["message"]["content"]
if text.startswith('`') and text.endswith('`'):
text = text[1:-1]
print(text) ``

Note that you both need to install the openai Python package (pip install openai) and an [API key](https://platform.openai.com/docs/api-reference). The API is paid, but the cost is ridiculously low for using such a simple script – using it daily from the beginning of the year I haven't yet exceeded the [$1 mark needed to unlock the gpt-4 model](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4) ;f. My usage for July is apparently even below 1 cent.

Now, if there is actually a better version of such a script out there – and I'm sure that's the case – feel free to let me know in the comments below.

**By the way...**
If want to improve your binary file and protocol skills, check out the workshop I'll be running between April and June → [Mastering Binary Files and Protocols: The Complete Journey](https://hackarcana.com/workshop-session/2025-Q1-Q1-mastering-binary/buy?utm=gyn-blog-inad)

## Comments:

2023-08-09 21:12:55 = [AdamPelc](http://)

{

Seems like there is GitHub repo with similar tool: https://github.com/JohannLai/gptcli

}

2023-09-19 21:45:23 = [J\_](http://)

{

TIL python openai module has a CLI:

}

2023-09-19 21:51:40 = [J\_](http://)

{

According to https://tiktokenizer.vercel.app/ you could save some tokens by writing the prompt in a single chat message.

}

## Add a comment:

|  |  |
| --- | --- |
| Nick: |  |
| URL (optional): |  |
| Math captcha: 9 ∗ 3 ＋ 9 = |  |
|  | |