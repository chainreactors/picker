---
title: Wi-Fi Geolocation, Then and Now
url: http://windowsir.blogspot.com/2023/01/wi-fi-geolocation-then-and-now.html
source: Instapaper: Unread
date: 2023-01-17
fetch_date: 2025-10-04T04:05:00.908878
---

# Wi-Fi Geolocation, Then and Now

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Sunday, January 15, 2023

### Wi-Fi Geolocation, Then and Now

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1c9BTRghfQOhQHTyan4Iu4W5acAalSfSgc7OdBxZw97gTw13gZ6n0guu2b4zmy3-eQRw2NBWwD6cv5sDH5vS9BKbz_pVxa3r26_3vm2gaD76r11Abm1EnvQrcDLg_te8UhzBr-zUeRFsh0TyhkonzKoUboQyvxJ3YTaYWg9TUezFAvM8/s320/timex.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1c9BTRghfQOhQHTyan4Iu4W5acAalSfSgc7OdBxZw97gTw13gZ6n0guu2b4zmy3-eQRw2NBWwD6cv5sDH5vS9BKbz_pVxa3r26_3vm2gaD76r11Abm1EnvQrcDLg_te8UhzBr-zUeRFsh0TyhkonzKoUboQyvxJ3YTaYWg9TUezFAvM8/s2000/timex.jpg)

I've always been fascinated by the information maintained in the Windows Registry. But in order to understand this, to really get a view into this, you have to know a little bit about my background. The first computer I remember actually using was a Timex-Sinclair 1000, just like the one in the image shown to the right. You connected it to the TV, programs were created via the keyboard and usually copied from "recipes" in the manual or in a magazine, and the "programs" could be saved to or loaded from a tape in a tape recorder. Yes, you read that right...a tape recorder. I was programming BASIC programs on this system, and then on a [Mac IIe](https://en.wikipedia.org/wiki/Apple_IIe). After that, it was the [Epson QX-10](https://en.wikipedia.org/wiki/Epson_QX-10), and then for a very long time, in high school and then in college (I started college in August, 1985), the [TRS-80](https://en.wikipedia.org/wiki/TRS-80).

The point of all of this is that the configuration of these systems, particularly as we moved to systems running MS-DOS, was handled through configuration files, particularly autoexec.bat and a myriad \*.ini files. Even when I started using Windows 3.1 or Windows 3.11 for Workgroups, the same held true...configuration files. We started to see the beginnings of the Registry with Windows 95, and files such as system.dat.

Even from the very beginning of my experience with the Windows Registry, the amount and range of information stored in this data source has been absolutely incredible. In 2005, Cory Altheide and I [published the first paper outlining artifacts associated with USB devices](https://www.sciencedirect.com/science/article/abs/pii/S1742287605000320?via%3Dihub) being connected to Windows (Windows XP) systems. What we were looking at at the time was commonalities across systems when the same device was connected to multiple systems, say, to run programs from the thumb drive, or copy files from systems to then take back to a central computer system.

From there, this topic has continued to be explored and unraveled, even as Windows itself continued to evolve and recognize different types of devices (thumb drives, digital cameras, smart phones) based on the protocol used.

In 2009, I [wrote a blog post about another artifact](http://windowsir.blogspot.com/2009/09/where-was-waldo.html) stored within the Windows Registry; specifically, MAC addresses of wireless access points that a Windows system had connected to. By tracking this information and mapping the geo-location of those wireless access points based on data recorded in online databases, the idea was that an analyst could track the movements of that system, and hence, the owner.

Why was this interesting? I'd heard more than a few stories from analysts and investigators who talked about an (former) employee of a company who, usually after the fact, was found to have visited a competitor's offices prior to resigning and accepting employment with that competitor. In one instance, not only did the employee connect their work computer to the Wifi system at a competitor's location, but they also connected to a Starbuck's store Wifi system that morning, next to or close to the competitor's location. With the time stamps of the connections, analysts were then able to use other timeline information to illustrate applications opened and files accessed until the system was shut down again.

I [updated the tool I wrote in 2011](https://windowsir.blogspot.com/2011/11/tool-update-wifi-geolocation.html), and as you can see from the post and comments, there was still interest in this topic at the time. I remember working on the tool, and taking the lat/long coordinates returned by the online database to populate a Google Map URL. So, over the course of about 2 yrs, the interest...or at least, *my* interest...in moving this forward, or at least revisiting it, was still there.

I recently [ran across this tweet](https://twitter.com/akaclandestine/status/1614294824609251329) (I saw it on 15 Jan 2023), which led me to [this Github repository](https://github.com/GONZOsint/geowifi).

This is what I love, truly love to see...how something that was of interest at one point is once again on the forefront of someone's mind, to the point where they create a tool, and post it on Github. This truly shows that no matter how much work and effort is put into something at one point, there will always be growth, and different aspects of the early project (the platform, the Registry, the online databases, etc.) will be extended. This also shows that nothing ever really goes away...

Posted by
H. Carvey

at
[9:28 PM](http://windowsir.blogspot.com/2023/01/wi-fi-geolocation-then-and-now.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/7045202915592340012 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=7045202915592340012&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=7045202915592340012&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=7045202915592340012&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=7045202915592340012&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=7045202915592340012&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=7045202915592340012&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/9518042/7045202915592340012)

[Newer Post](http://windowsir.blogspot.com/2023/01/soft-skills-writing.html "Newer Post")

[Older Post](http://windowsir.blogspot.com/2022/12/persistence-and-lolbins.html "Older Post")
[Home](http://windowsir.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://windowsir.blogspot.com/feeds/7045202915592340012/comments/default)

## Pages

* [Home](http://windowsir.blogspot.com/)
* [Timelines](http://windowsir.blogspot.com/p/timelines.html)
* [Books](http://windowsir.blogspot.com/p/books.html)
* [Malware](http://windowsir.blogspot.com/p/malware.html)
* [FOSS Tools](http://windowsir.blogspot.com/p/foss-tools.html)

## Subscribe To WindowsIR

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_...