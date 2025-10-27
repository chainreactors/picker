---
title: Phishing Page Branded with Your Corporate Website, (Tue, Feb 21st)
url: https://isc.sans.edu/diary/rss/29570
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-22
fetch_date: 2025-10-04T07:48:03.592528
---

# Phishing Page Branded with Your Corporate Website, (Tue, Feb 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29564)
* [next](/diary/29574)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Phishing Page Branded with Your Corporate Website](/forums/diary/Phishing%2BPage%2BBranded%2Bwith%2BYour%2BCorporate%2BWebsite/29570/)

**Published**: 2023-02-21. **Last Updated**: 2023-02-21 09:22:50 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[2 comment(s)](/diary/Phishing%2BPage%2BBranded%2Bwith%2BYour%2BCorporate%2BWebsite/29570/#comments)

Here is another perfect example that shows how attackers abuse free services...

Phishing campaigns are often combined with a layer of social engineering to make the victim more confident to click on a link or to open the attacked file. I spotted an interesting phishing email redirecting you to a classic login page.

The page asks you to provide your credentials to “unlock” access to a PDF document, but the attacker implemented a nice trick. The background of the fake login page is… a screenshot of your corporate website!

Here is an example with my own company:

![](https://isc.sans.edu/diaryimages/images/isc-20230221-1.png)

I changed the targeted email address, and here is an example with the sans.org website:

![](https://isc.sans.edu/diaryimages/images/isc-20230221-2.png)

I deobfuscated the JavaScript, and here is how they implemented this:

```

<script>
let emailzz = "[email protected]";

function jpgvbqitfwqpnhjgqktfqwpwoufrhtbrkktpjfizjuqjvxjjkperhumw(fscigkwyepzcytekcylktcjcpcurjwwebroblbnfyewnlqtqzgtwaa)
{
    return fscigkwyepzcytekcylktcjcpcurjwwebroblbnfyewnlqtqzgtwaa.split("").reverse().join("");
}
var dtisejcxzuvjbshjmgaewqkxryjqdxcqfykqczkhbwtdmytbtwgliiqerzem=document.write(atob(...)));
</script>
```

This function decodes a stream of Base64 data that has been reserved. Pretty simple obfuscation. To make the script more difficult to read, this technique has been implemented ten (yes, you read properly) times! I wrote a CyberCheck recipe to decode it:

```

Label('Loop0')
Regular_expression('User defined','[a-zA-Z0-9+=]{200,}',true,true,false,false,false,false,'List matches')
Reverse('Character')
From_Base64('A-Za-z0-9+/=',true)
Conditional_Jump('[a-zA-Z0-9+=]{200,}',false,'Loop0',8)
Regular_expression('User defined','[a-zA-Z0-9+=]{200,}',true,true,false,false,false,false,'List matches')
From_Base64('A-Za-z0-9+/=',true)
```

By the way, this is a good example to demonstrate how CyberChef recipes may contain conditional jumps and label to implement loops! Pretty handy in this case.

Now, here is the interesting piece of code found in the deobfuscated script:

```

<script>
const emailarr = emailzz.split("@");
let webzz = emailarr["1"];
const webzzarr = webzz.split(".");
let webnamezz = webzzarr["0"]
let googlezz = "https://www.google.com/s2/favicons?domain="+webzz;
let weblogozz = "https://logo.clearbit.com/"+webzz;
var bkimage = "url('https://image.thum.io/get/https://www."+webzz;"')"
</script>

...

<script>
document.body.style.backgroundImage = bkimage;
</script>
```

The variable 'emailzz' has been defined in the original HTML page (see above), and the domain is extracted. How the attacker gets the background?

It’s a free service provided by thum.io[[1](https://thumb.io/)], the free website screenshot generator:

```

hxxps://image[.]thum[.]io/get/https://www."+webzz;
```

The same domain name is also used to fetch interesting data:

* The company logo is fetched via hxxps://logo[.]clearbit[.]com/<domain>
* The favicon is fetched via hxxps://www[.]google[.]com/s2/favicons?domain=<domain>

These graphical elements help to build the fake page that looks familiar to potential victims!

[1] <https://thum.io/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Background](/tag.html?tag=Background) [Free Service](/tag.html?tag=Free Service) [Phishing](/tag.html?tag=Phishing)

[2 comment(s)](/diary/Phishing%2BPage%2BBranded%2Bwith%2BYour%2BCorporate%2BWebsite/29570/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29564)
* [next](/diary/29574)

### Comments

Some users at my work have seen this same kind of phishing attempt in the past month, but instead of using our domain/logo, the messages we received spoofed Google/Microsoft services.
I reached out to Clearbit after reading about their logo service, but only were only offered to have my own domain names/logos disallowed. I did my best to convince them their Logo API service, though "neat"/"cool" was being and would continue to be abused by malicious actors.
I did not get the impression they were interested in changing their services, so I've settled on adding them to our domain RBLs.

#### Joel

#### Feb 21st 2023 2 years ago

Great CyberChef recipe, but to cover everything, you need to add URL Decode as the last step of the recipe as at the end of the HTML, you can find some more javascript that requires to be decoded.

#### J0xA0

#### Feb 24th 2023 2 years ago

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