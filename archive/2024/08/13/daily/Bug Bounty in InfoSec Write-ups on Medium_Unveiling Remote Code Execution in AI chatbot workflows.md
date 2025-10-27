---
title: Unveiling Remote Code Execution in AI chatbot workflows
url: https://infosecwriteups.com/unveiling-remote-code-execution-in-ai-chatbot-workflows-3c7f633f63c3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-13
fetch_date: 2025-10-06T18:04:32.073434
---

# Unveiling Remote Code Execution in AI chatbot workflows

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3c7f633f63c3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funveiling-remote-code-execution-in-ai-chatbot-workflows-3c7f633f63c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funveiling-remote-code-execution-in-ai-chatbot-workflows-3c7f633f63c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3c7f633f63c3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3c7f633f63c3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unveiling Remote Code Execution in AI chatbot workflows 💵

[![Anurag__Verma](https://miro.medium.com/v2/resize:fill:64:64/1*ztIXKD8m9nIjY6Am8Tk5HQ@2x.jpeg)](https://varmaanu001.medium.com/?source=post_page---byline--3c7f633f63c3---------------------------------------)

[Anurag\_\_Verma](https://varmaanu001.medium.com/?source=post_page---byline--3c7f633f63c3---------------------------------------)

5 min read

·

Aug 5, 2024

--

1

Listen

Share

Hi Readers 👋, this article goes through a remote code execution finding worth $$$$ that I found on one of the popular chatbot platforms so let's get started.

**Introduction:**

In recent years, AI chatbots have become increasingly popular across various industries, providing efficient customer service, enhancing user engagement, and streamlining business operations. These intelligent systems, driven by complex algorithms and natural language processing capabilities, are designed to interact with users seamlessly. However, like any software, they are not immune to security vulnerabilities.

One of the most critical types of security vulnerabilities is ***Remote Code Execution (RCE)***, which allows attackers to execute arbitrary code on a target system. RCE vulnerabilities pose significant risks, as they can lead to unauthorized access, data breaches, and complete control over affected systems.

During a recent security assessment, I discovered a Remote Code Execution vulnerability in a widely-used AI chatbot platform. This vulnerability was found within the chatbot’s custom workflow response code, a feature that allows developers to extend the bot’s functionality by creating tailored workflows. While these workflows are powerful tools for enhancing chatbot interactions, they can also introduce security risks if not properly secured.

In this article, I will share the journey of uncovering this vulnerability, delve into the technical details, and discuss its potential implications.

**Background:**

The target was a proper business management platform with **multiple team management features**, **email management**, **chatbots** etc.

**Reference**: <https://nodejs.org/api/globals.html>

while going through multiple features specific to the chatbot for automation, one of the features that caught my attention is the “Start from scratch” option as shown below.

Press enter or click to view image in full size

![]()

Now this option “**Start from scratch**” is composed of multiple options for customizing the automation for the chatbot for example: workflows, webhooks and custom code snippets as you can see in the below image.

After looking at the other options, I started exploring the “**run a code snippet**” option.

Press enter or click to view image in full size

![]()

**Technical Details:**

This feature contains customizable code for getting a custom response from the chatbot with sample functions like responseJson with botMessage parameter with a default value like “Hello World”

default snippet looks like this:

```
const responseJson = {
botMessage: "Hello world",
responseExpected: false
}
```

as the chatbot was built using Node 18.x framework I tried to get/check responses for the global variables like **\_\_dirname**,**\_\_filename** and tried to execute functions like **eval(7\*7)** in place of “**Hello World**”.

This is how the response code looks while using global variables along with chatbot responses.

**\_\_dirname**

```
const responseJson = {
botMessage: __dirname,
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

you can observe I am getting “**/var/task**” as output in the chatbot it means the global variable **\_\_dirname** executed internally and we are getting successful output.

let go for more leads,

**\_\_filename**

```
const responseJson = {
botMessage: __filename,
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

It also executed successfully returning the output “**/var/task/Template.js**”

**eval(7\*7)**

```
const responseJson = {
botMessage: eval(7*7),
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

These are some positive leads but aren’t much promising or sensitive for getting reported as RCE (remote code execution).

At this point, I started looking at Nodejs official documentation and found some more global variables/objects to check for more data leaks.

you can find the official documentation here: [***https://nodejs.org/api/globals.html#process***](https://nodejs.org/api/globals.html#process)

such as **process.env** , **process.argv** **process.execPath**,**process.memoryUsage(),process.getuid(),process.cpuUsage()** etc

let's see response for these global objects:

**process.env**

```
const responseJson = {
botMessage: process.env,
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

This is crucial to check the environment variable as these sometimes stores AWS\_SECRET and AWS\_KEY and you may get a good reward at this point.

**process.platform**

```
const responseJson = {
botMessage: process.platform,
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

**process.execPath**

```
const responseJson = {
botMessage: process.execPath,
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

process.memoryUsage()

```
const responseJson = {
botMessage: process.memoryUsage(),
responseExpected: false
}
```

Press enter or click to view image in full size

![]()

**Getting full RCE:**

Till this point, we have some good leads like we are getting responses for almost every node global object and access to environment variables.

But still, I was looking for full RCE and tried to build some payloads for it after multiple tries, debugging and discussing with co-researchers I was able to create a full **RCE payload** which looked like this:

```
const ...