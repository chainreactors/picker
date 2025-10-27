---
title: OneNote Embedded file abuse
url: https://blog.nviso.eu/2023/02/27/onenote-embedded-file-abuse/
source: NVISO Labs
date: 2023-02-28
fetch_date: 2025-10-04T08:14:34.482520
---

# OneNote Embedded file abuse

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

# OneNote Embedded file abuse

[Nicholas Dhaeyer](https://blog.nviso.eu/author/nicholas-dhaeyer/ "Posts by Nicholas Dhaeyer")

[Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [OneNote](https://blog.nviso.eu/category/maldoc/onenote/), [Maldoc](https://blog.nviso.eu/category/maldoc/), [Malware](https://blog.nviso.eu/category/malware/), [phishing](https://blog.nviso.eu/category/phishing/), [Reverse Engineering](https://blog.nviso.eu/category/reverse-engineering/), [Threat Hunting](https://blog.nviso.eu/category/threat-hunting/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Qbot](https://blog.nviso.eu/category/malware/qbot/)

February 27, 2023January 17, 2025
8 Minutes

# OneNote in the media

In recent weeks OneNote has gotten a lot of media attention as threat actors are abusing the embedded files feature in OneNote in their phishing campaigns.
I first observed this OneNote abuse in the media via Didier’s [post](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/). This was later also mentioned in Xavier’s [ISC diary](https://isc.sans.edu/diary/A%2BFirst%2BMalicious%2BOneNote%2BDocument/29470) and on the [podcast](https://isc.sans.edu/podcastdetail.html?id=8336). Later, in the beginning of February, [the hacker news](https://thehackernews.com/2023/02/post-macro-world-sees-rise-in-microsoft.html) covered this as well.

# Attack technique

The OneNote feature that is being abused during these phishing campaigns is hiding embedded files behind pictures which entices the user to click the picture. If the picture is clicked, it will execute the file hidden beneath. These files could be executables, JavaScript files, HTML files, PowerShell, …. Basically any type of file that can execute malware when executed. Recently we have also observed the usage of `.chm` files which have an `index.html` file embedded that would run inline JavaScript.
On a Windows system this roughly translates to either one of the following processes executing the script/file: `'powershell.exe', 'pwsh.exe', 'wscript.exe', 'cscript.exe', 'mshta.exe', 'cmd.exe', 'hh.exe'`.

![](https://blog.nviso.eu/wp-content/uploads/2023/02/Pasted-image-20230217220449-1024x455.png)

An image of a malicious embedded OneNote file

![](https://blog.nviso.eu/wp-content/uploads/2023/02/Pasted-image-20230217223551-1024x404.png)

An image of a malicious embedded OneNote file

# Anatomy of a OneNote file

Didier did amazing work in his [blogpost](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/) where he described how a OneNote file looks like. What is interesting to us, is that OneNote files work with [GUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) to indicate the start of the embedded file section. The GUID that represents the start of an embedded file in OneNote is: `{BDE316E7-2665-4511-A4C4-8D4D0B7A9EAC}` Using the following [tool](https://toolslick.com/conversion/data/guid) we can convert the GUID to a HEX string: `e716e3bd65261145a4c48d4d0b7a9eac`.
If a HEX editor is used, you can search for this string and find the exact location of the embedded file.
OneNote will then reserve 20 bytes. The first 8 bytes are used to indicate the length of the file, the following 4 bytes are unused and have to be zero, and the last 8 bytes being reserved and also zero. This results in the following HEX string `E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00` before the embedded file data beings.
When taking a look at the OneNote file through a HEX editor it becomes quickly clear that OneNote does not attempt to encrypt or compress anything. That is if you are looking at a `.one` file not a `.onepkg`. A `.onepkg` file acts similar as a ZIP file that contains the exported files from a OneNote Notebook. It is possible to open these files using 7zip.
The OneNote file (`.one`) will display the contents of the embedded file as followed:

![](https://blog.nviso.eu/wp-content/uploads/2023/02/Pasted-image-20230217213523.png)

A OneNote file in a HEX editor, that shows a plaintext embedded file

This means that we can easily check for known false positives while analyzing these files, which brings me to the next point, creating a detection rule.

# YARA Rule

It would not be easy to create a detection rule that catches all malicious embedded files as usually scripts do not have a “magic byte” unlike executables which have the famous “MZ” header. While it would be easy to create a YARA rule that looks as the previously observed hex string + the MZ file header, this would only flag embedded executables. If this is your goal then it is a great rule, however I would like something more flexible that I can use on an email gateway to flag all potential malicious incoming OneNote files.
So I took a different approach. I observed that it is common for pictures (e.g.: screenshots) to be embedded in a OneNote file. I did not observe many cases that had other files embedded. This led me to create a YARA rule that would look at a OneNote file, ignore the file sections that indicate that an image is present but would raise an alert when any other file was observed. So instead of looking for Malicious files, I will ignore known legitimate files. This simple trick allowed me to create a high confident detection rule while not overloading analysts with too many false positives.
Of course every environment is different and if it is common for PDF files to be embedded in OneNote files in your environment, you should exclude those PDF files as well. Therefore, it is important to establish a baseline during a testing period.
Below is an example of this technique. The `00`‘s after the `??` can be replaced with `??` as well. Although these bytes should always be empty, this rule will not detect the files if the bytes were altered.

```
rule OneNote_EmbeddedFiles_NoPictures
{
    meta:
        author = "Nicholas Dhaeyer - @DhaeyerWolf"
        date_created = "2023-02-14 - &lt;3"
        date_last_modified = "2023-02-17"
        description = "OneNote files that contain embedded files that are not pictures."
        reference = "https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/"

    strings:
        $Embedd...