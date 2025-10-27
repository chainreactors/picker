---
title: Set Up an Android Hacking Lab for $0
url: https://www.trustedsec.com/blog/set-up-an-android-hacking-lab-for-0/
source: Instapaper: Unread
date: 2022-10-15
fetch_date: 2025-10-03T20:00:33.175753
---

# Set Up an Android Hacking Lab for $0

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Set Up an Android Hacking Lab for $0](https://trustedsec.com/blog/set-up-an-android-hacking-lab-for-0)

October 13, 2022

# Set Up an Android Hacking Lab for $0

Written by
Kurt Muhl

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AndroidHackingLab_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695576853&s=60725f953b4ba982373bbeb472269057)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#112e6264737b7472652c527974727a3423217e64653423216579786234232170636578727d7434232177637e7c3423214563646265747542747234232037707c612a737e75682c4274653423214461342321707f342321507f75637e78753423215970727a787f763423215d7073342321777e63342321342325213422503423217965656162342250342357342357656364626574756274723f727e7c342357737d7e763423576274653c64613c707f3c707f75637e78753c7970727a787f763c7d70733c777e633c21 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fset-up-an-android-hacking-lab-for-0 "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Set%20Up%20an%20Android%20Hacking%20Lab%20for%20%240%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fset-up-an-android-hacking-lab-for-0 "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fset-up-an-android-hacking-lab-for-0&mini=true "Share on LinkedIn")

With the ever-increasing demand for mobile technology, it seems like there is an app to do just about anything you can think of, right on your cell phone. From banking to mobile gaming and even controlling the RGB lights installed in your home office, everything is interconnected now. With the rise of this functionality also comes the responsibility of ensuring that these apps are safe to use. When it comes to learning about mobile security, setting up a lab is a great first step. The intent of this writeup is to provide the building blocks to getting a lab set up and starting the process of learning how to assess a mobile application.

**Prerequisites:**

* Python3 - <https://www.python.org/downloads/>
* Android Studio - <https://developer.android.com/studio>
* Android Platform-Tools - <https://developer.android.com/studio/releases/platform-tools>
* ADB Drivers (for Windows users) - <https://developer.oculus.com/downloads/package/oculus-go-adb-drivers/>
* DVBA - <https://github.com/rewanthtammana/Damn-Vulnerable-Bank/raw/master/dvba.apk>
* Frida-server 15.2.2- <https://github.com/frida/frida/releases>
* ***Frida** client* – `pip3 install frida==15.2.2`
* ***Frida-tools** –* `pip3 install frida-tools`
* ***Objection** –* `pip3 install objection`

## 1    Emulator Setup

An Android emulator is the core of this setup. Since Android is an open-source technology, it costs nothing to set up. Within Android Studio, it is possible to set up multiple devices with a variety of operating systems that can be used for testing purposes.

To get started, launch Android Studio and select ***New Project***.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Muhl_1.png)

Choose ***No Activity*** and click ***next***—this is just to get a project started to run an emulator,and any code generated will not actually be used. On the next page, give the project a name and click ***Finish***.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Muhl_2.png)

Figure 2 - Phone and Tablet Template with No Activity

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Muhl_3.png)

Figure 3 - New Project Details

Once the project is created, in the top center of Android Studio, there should be a dropdown menu that says ***No Devices***. Within this menu, open the Device Manager and select ***Create device***.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Muhl_4.png)

Figure 4 - Device Manager

The options used for this device are:

* Category – Phone
* Pixel 5

Click ***Next***

* System Image ‘S’ (this may need to be downloaded)

Click ***Next***

* Choose a name for the virtual device
* Make sure that the startup orientation is “Portrait”

Click ***Finish***

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Muhl_5.png)

Figure 5 - Android Virtual Device (AVD) Configuration

Back in Device Manager, a new device with the name ***Pixel 5 API 31*** should be there. Click ***Play*** to start the emulator. The emulator will start as a window at the bottom of the Device Manager. Click and drag the ***Emulator*** header to have the device in its own window.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Muhl_6.png)

Figure 6 - New Interactive AVD

One nice benefi...