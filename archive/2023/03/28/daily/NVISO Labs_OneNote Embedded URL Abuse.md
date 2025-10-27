---
title: OneNote Embedded URL Abuse
url: https://blog.nviso.eu/2023/03/27/onenote-embedded-url-abuse/
source: NVISO Labs
date: 2023-03-28
fetch_date: 2025-10-04T10:50:53.325599
---

# OneNote Embedded URL Abuse

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# OneNote Embedded URL Abuse

[Nicholas Dhaeyer](https://blog.nviso.eu/author/nicholas-dhaeyer/ "Posts by Nicholas Dhaeyer")

[SOC](https://blog.nviso.eu/category/soc/), [Threat Hunting](https://blog.nviso.eu/category/threat-hunting/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [Qbot](https://blog.nviso.eu/category/malware/qbot/), [OneNote](https://blog.nviso.eu/category/maldoc/onenote/), [Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [Maldoc](https://blog.nviso.eu/category/maldoc/), [phishing](https://blog.nviso.eu/category/phishing/), [Malware](https://blog.nviso.eu/category/malware/)

March 27, 2023January 17, 2025
5 Minutes

In my [previous blogpost](https://blog.nviso.eu/2023/02/27/onenote-embedded-file-abuse/) I described how OneNote is being abused in order to deliver a malicious URL. In response to this attack, [helpnetsecurity recently reported](https://www.helpnetsecurity.com/2023/03/10/protection-malicious-onenote-documents/) that Microsoft is planning to release a fix for the issue in April this year. Currently, it’s still unknown what this fix will look like, but from helpnetsecurity’s post, it seems like Microsoft’s fix will focus on the OneNote embedded file feature.
During my testing, I discovered that there is another way to abuse OneNote to deliver malware: **Using URLs**. The idea is similar to how Threat Actors are already abusing URLs in HTML pages or PDFs. Where the user is presented with a fake warning or image to click on which would open the URL in their browser and loads a phishing page.

The focus of this blogpost will be on URLs withing a OneNote file that is delivered via an attachment. Not a URL that leads to OneNote online.

There are 3 ways to deliver URLs via a OneNote file.

1. Just plainly paste your URL in the OneNote file (Clickable URL)
2. Make some text (like “Open”) clickable with a malicious URL (Clickable text)
3. Embed URLs in pictures (Clickable picture)

Now it is important to note that these 3 ways rely on social engineering and tricking the user to click your URL or picture, either via instructions or deceiving the user. We have seen this technique being used through OneDrive and SharePoint online already

So, let’s create some examples and see what this attack could look like.

# URLs in OneNote

## Clickable URLs

The most straightforward way is to just put a URL in a OneNote file. In an actual phishing email, the OneNote file will probably not just contain the URL alone. To make things more believable, Threat Actors could potentially write a small story or an “encrypted” message in the OneNote file (an example of this can be observed below). The idea would then be to convince the user into clicking the URL in order to “decrypt” the message. Once clicked on the URL, the user would then either have to download something or provide credentials to “log in”.

If you would like to read the message in the OneNote file, you would have to click the URL. Which could then lead to the download of a malicious file or a credential harvest page.
An example of such an “encrypted” message could be:

![](https://blog.nviso.eu/wp-content/uploads/2023/03/Pasted-image-20230319142512.png)

An example of a fake encrypted message where a user has to click a URL to decrypt it

## Clickable text

Similar to clickable URLs, you can hide a URL behind normal text. Once you hover over the URL, you will see where it points towards. If the address points to wards a malicious domain that uses typo squatting (e.g. `g00gle[.]com` instead of `google[.]com`) then Threat Actors could fool the human eye.

![](https://blog.nviso.eu/wp-content/uploads/2023/03/Pasted-image-20230312180721-1024x344.png)

The text “open” hiding a malicious URL

The issue here lies in the fact that once you click the “open” text, you will immediately be redirected to the website. There is no pop up asking if you really want to visit the website.
Taking this technique into account, it is also possible to use our “encrypted message” example from before and make the user think they will visit a legitimate page but embed a different URL:

![](https://blog.nviso.eu/wp-content/uploads/2023/03/Pasted-image-20230319142958-1.png)

The visible URL “<https://microsoft.com&#8221>; is hiding a malicious URL

## Clickable Pictures

To create an embedded URL in a picture, right-click your picture, and Click “Link…”

![](https://blog.nviso.eu/wp-content/uploads/2023/03/Pasted-image-20230312160449-1024x413.png)

Here you can put a URL to your malicious file or phishing page. Yes, you could spin this story so that you would have to authenticate and login, to your browser with a fake login website.
Do note that to open a URL that is embedded within a picture, you will need to hold the `CTRL` key and click the image. The phishing document will have to instruct the user to hold `CTRL` and click the picture; however, I do not see this as an obstacle for threat actors.

![](https://blog.nviso.eu/wp-content/uploads/2023/03/Pasted-image-20230312160637-1024x404.png)

A picture with the button “open” that has an embedded malicious URL

# Detection Capabilities

## On OneNote Interaction

Opening the URL, will launch the default browser. This can be translated to OneNote spawning a child process, which is the browser. A full process flow could look something like this:

![](https://blog.nviso.eu/wp-content/uploads/2023/03/Pasted-image-20230322203614.png)

Process execution of explorer.exe > Outlook.exe > OneNote.exe > firefox.exe

Do note that, as typically done so by Outlook, once you click the file, it saves a copy in a temporary cache folder (depending on your version of outlook, this can be a slightly different place than is shown above here, but generally, you will have the name `INetCache` and `Content.Outlook` in the folder path.)

A quick hunting rule for this behaviour can be to look for the process tree that was observed before. This process tree can be adjusted to the needs of your environment, depending on what browser is being used (e.g. if you are running brave.exe, you should include this in the “FileName” section of the query)

```
DeviceProcessEvents
| where InitiatingProcessFileName contains "onenote.exe"
| where FileName has_any ("firefox.exe","msedge.exe","chrome.exe")
```

Now if you’d like a more “catch all” approach, the last line can be replaced with a query that lo...