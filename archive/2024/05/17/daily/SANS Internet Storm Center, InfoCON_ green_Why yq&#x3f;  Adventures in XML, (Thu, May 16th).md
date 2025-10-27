---
title: Why yq&#x3f;  Adventures in XML, (Thu, May 16th)
url: https://isc.sans.edu/diary/rss/30930
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-17
fetch_date: 2025-10-06T17:17:24.965441
---

# Why yq&#x3f;  Adventures in XML, (Thu, May 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30926)
* [next](/diary/30934)

# [Why yq? Adventures in XML](/forums/diary/Why%2Byq%2BAdventures%2Bin%2BXML/30930/)

**Published**: 2024-05-16. **Last Updated**: 2024-05-16 12:04:52 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[0 comment(s)](/diary/Why%2Byq%2BAdventures%2Bin%2BXML/30930/#comments)

I was recently asked to <ahem> "recover" a RADIUS key from a Microsoft NPS server.  No problem I think, just export the config and it's all there in clear text right?

... yes, sort of ...

The XML file that gets output is of course perfect XML, but that doesn't mean it's easy to read for a human, it's as scrambled as my weekend eggs.  I got my answer, but then of course started to look for a way to get the answer in an easier way, something I could document and hand off to my client.  In other words, I started on the quest for a "jq" like tool for XML.  Often security work involves taking input in one text format and converting it to something that's human readable, or more easily parsed by the next tool in the pipeline.  (see below)

XMLLint is a pretty standard one that's in Linux, you can get it by installing libxml2.  Kali has it installed by default - usage is very straightforward:

```

xmllint < file.xml
```

or

```

cat file.xml | xmllint
```

There are a bunch of output options, but because it's not-so windows friendly I didn't dig to far - run man xmllint or browse here: [https://gnome.pages.gitlab.gnome.org/libxml2/xmllint.html](http://https://gnome.pages.gitlab.gnome.org/libxml2/xmllint.html)  if you need more than the basics on this.

However, finding something like this for Windows turned into an adventure, there's a port of xmllint for Windows but it's in that 10-year age range that makes me a bit leary to install it.  With a bit of googling I found yq.

This is a standalone install on most Linux distro's (sudo apt-get install yq or whatever), and has a few standard install methods for windows:

* you can just download the binary and put it in your path
* choco install yq
* winget install --id MikeFarah.yq

yq is written to mimic jq like you'd expect from the name, but will take json, yaml, xml, csv and tsv files.  It's not as feature-heavy as jq, but it's got enough, and let's face it, most of us use these for pretty print output, so that we can grep against that anyway.
I especially liked it for today's problem because I can adjust the indent, since the NPS XML export has a fairly deep heirarchy I went with an indent of 1:

```

type nps-export.xml | yq --input-format xml --output-format xml --indent 1 > pretty.xml
```

A quick peek at the file found me my answwer in the pretty (and grep-able) format that I wanted.  A typical RADIUS Client section looks lke:

```

 <Clients name="Clients">
  <Children>
   <DEVICE name="DEVICENAME">
    <Properties>
     <Client_ _Template_Guid="_Template_Guid" xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="string">{00000000-0000-0000-0000-000000000000}</Client_>
     <IP_Address xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="string">IP.Address.Goes.Here</IP_Address>
     <NAS_Manufacturer xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="int">0</NAS_Manufacturer>
     <Opaque_Data xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="string"></Opaque_Data>
     <Radius_Client_Enabled xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="boolean">1</Radius_Client_Enabled>
     <Require_Signature xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="boolean">0</Require_Signature>
     <Shared_Secret xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="string">SuperSecretSharedKeyGoesHere</Shared_Secret>
     <Template_Guid xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="string">{1A1917B8-D2C0-43B3-8144-FAE167CE9316}</Template_Guid>
    </Properties>
```

Or I could dump all the shared secrets with the associated IP Addresses with:

```

type pretty.xml | findstr "IP_Address Shared_Secret"
```

or

```

cat pretty.xml | grep 'IP_address\|Shared_Secret'
```

After all that, I think I've found my go-to for text file conversions - in particular xml or yaml, especially in Windows ..

Full details on these two tools discussed:
<https://github.com/mikefarah/yq>
<https://linux.die.net/man/1/xmllint>

If you've got a different text formatter (or un-formatter), or if you've used xmllint or yq in an interesting way, please let us know about it in our comment form!

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [yq](/tag.html?tag=yq) [xmllint](/tag.html?tag=xmllint) [xml](/tag.html?tag=xml) [yaml](/tag.html?tag=yaml) [jq](/tag.html?tag=jq)

[0 comment(s)](/diary/Why%2Byq%2BAdventures%2Bin%2BXML/30930/#comments)

* [previous](/diary/30926)
* [next](/diary/30934)

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