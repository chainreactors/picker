---
title: Offensively Groovy
url: https://trustedsec.com/blog/offensively-groovy
source: TrustedSec
date: 2024-10-23
fetch_date: 2025-10-06T18:55:28.396768
---

# Offensively Groovy

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
* [Offensively Groovy](https://trustedsec.com/blog/offensively-groovy)

October 22, 2024

# Offensively Groovy

Written by
Brandon McGrath

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OffensivelyGroovy_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1729014948&s=2e7bf1ef1bdc119bb2a2202cb5033d78)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#94abe7e1f6fef1f7e0a9d7fcf1f7ffb1a6a4fbe1e0b1a6a4e0fcfde7b1a6a4f5e6e0fdf7f8f1b1a6a4f2e6fbf9b1a6a4c0e6e1e7e0f1f0c7f1f7b1a6a5b2f5f9e4aff6fbf0eda9dbf2f2f1fae7fde2f1f8edb1a6a4d3e6fbfbe2edb1a7d5b1a6a4fce0e0e4e7b1a7d5b1a6d2b1a6d2e0e6e1e7e0f1f0e7f1f7baf7fbf9b1a6d2f6f8fbf3b1a6d2fbf2f2f1fae7fde2f1f8edb9f3e6fbfbe2ed "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foffensively-groovy "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Offensively%20Groovy%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Foffensively-groovy "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foffensively-groovy&mini=true "Share on LinkedIn")

On a recent red team engagement, I was able to compromise the Jenkins admin user via retrieving the necessary components and decrypting credentials.xml. From here, I wanted to investigate Groovy, as it’s something I’ve never really used—this blog covers a bunch of post-exploitation tasks in Groovy.

## 1.1      Install

In my case, Jenkins was operating on Windows, which led me down some interesting rabbit holes that we will see soon. But, at first glance, it was running as the machine account. After installing Jenkins, it became apparent as to why this was.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OffensivelyGroovy_McGrath/Fig1_McGrath.png?w=320&q=90&auto=format&fit=max&dm=1729015095&s=9d45d91f63010f837500792a05812e42)

The install process is straightforward and documented at [jenkins.io](http://jenkins.io).

## 1.2      Post-Exploitation

Groovy has a lot of room to work with and is designed for all sorts of automation. Let’s take a look through some examples of host enumeration.

### 1.2.1     Username and Hostname

This information is easily obtained by the ***java.net.InetAdress***class and the system property ***user.name***.

```
import java.net.InetAddress

def hostname = InetAddress.localHost.hostName
println "Host: $hostname"

def username = System.getProperty("user.name")
println "User: $username"
```

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OffensivelyGroovy_McGrath/Fig2_McGrath.png?w=320&q=90&auto=format&fit=max&dm=1729015096&s=d473c62b96a3a83f918c2ba876d56eaa)

### 1.2.2     Directories

Listing directories is just as simple. Using the File class, we can simply loop over each object and check if it’s a file or a directory.

```
def directoryPath = "c:\\"
def directory = new File(directoryPath)

if (directory.exists() && directory.isDirectory()) {
    directory.eachFile { file ->
        println "${file.name.padRight(50)} ${file.isDirectory() ? 'Directory' : 'File'} ${file.length()} bytes"
    }
} else {
    println "The specified directory does not exist or is not accessible."
}
```

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OffensivelyGroovy_McGrath/Fig3_McGrath.png?w=320&q=90&auto=format&fit=max&dm=1729266664&s=98ae916518ce2888283e319598fe419a)

### 1.2.3     Read Files

Another simple one is reading files—using the same File class as before, we can get the text and print it to the screen.

```
def content = new File("c:\\readme.txt").getText("UTF-8")
println content
```

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OffensivelyGroovy_McGrath/Fig4_McGrath.png?w=320&q=90&auto=format&fit=max&dm=1729267350&s=311642ce483c675129b1f6c95d83dc13)

### 1.2.4     Miscellaneous and Etcetera

The possibilities are endless. During this session, I was able to implement the following functions to further the operation:

* Exfiltrating/Uploading data over HTTP
* Enumerating Jenkins versions, properties, nodes, executors, etc.
* Listing stored credentials
* Starting and stopping processes
* Operating system commands

## 1.3      Java Native Access (JNA)

This is where it gets fun. So, up until now, I just wanted to cover some things you may want to do when landing on Jenkins to further figure out where you are. Let’s now investigate utilizing the WinAPI. In this example, we are going to implement ***EnumProcesses*** to create a ***...