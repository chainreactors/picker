---
title: Setting up your bug bounty scripts with Python and Bash
url: https://infosecwriteups.com/setting-up-your-bug-bounty-scripts-with-python-and-bash-327baa414c99?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-31
fetch_date: 2025-10-04T02:47:58.254572
---

# Setting up your bug bounty scripts with Python and Bash

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F327baa414c99&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsetting-up-your-bug-bounty-scripts-with-python-and-bash-327baa414c99&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsetting-up-your-bug-bounty-scripts-with-python-and-bash-327baa414c99&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-327baa414c99---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-327baa414c99---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The subdomain monitoring bot — Setting up your bug bounty scripts with Python and Bash

[![Shriyans Sudhi](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*cf0G9f64xhKZtfrA)](https://shriyanssudhi.medium.com/?source=post_page---byline--327baa414c99---------------------------------------)

[Shriyans Sudhi](https://shriyanssudhi.medium.com/?source=post_page---byline--327baa414c99---------------------------------------)

8 min read

·

Dec 30, 2022

--

Listen

Share

Hi there,

Automation is very interesting things, and if done in a right manner, it is more interesting. But writing automation scripts is the most important thing for that. So, in this article, we’ll be discussing about writing automation scripts in Python and Bash for your VPS server (or maybe raspberry pi). If you’ve not read my previous article, [Monitoring your targets for bug bounties](/monitoring-your-targets-for-bug-bounties-36f6be3e69c9), which is the main article for our series, I highly recommend you reading that first.

Press enter or click to view image in full size

![]()

Photo by [Sai Kiran Anagani](https://unsplash.com/%40anagani_saikiran?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral); Automation script

First of all let’s decide what will be our automation system could be for. The following are the possibilities:-

* New subdomain monitoring
* Log poisoning
* Nuclei
* Waybackurls with gf
* Etc.

So, in this article, we will start by the very basic bot, for new subdomain monitoring

## The algorithm

The algorithm can be designed in various methods. In bash, in python, mixed, so we will go for running python and shell commands with help of bash scripts

> Open the existing file “domains.txt” containing targets provided by the user
>
> Sort a few targets form that as the file could contain thousands of domains, and we don’t want that much load on our network/machine
>
> Run a tool, maybe amass, on them and output it to a file “new-subdomains.txt”
>
> Compare it with the old file, called “subdomains.txt” and filter out new ones.
>
> Send them to a user defined channel, maybe slack or email (slack is highly recommended as you will have an organized data). Also, write the new subdomain to the “subdomains.txt” file so that you can easily get a list when you want to hunt on that target

## Setting up things

Creating directories to organize all the data is important. So we need to set up directories so that things won’t get messed up. The structure of the directory could be:-

```
.
├── domains.txt
├── init.py
├── last.txt
├── main.sh
├── max.txt
├── runner.py
├── sorter.py
└── targets
    ├── abc.com
    │   ├── new-subdomains.txt
    │   └── subdomains.txt
    └── xyz.com
        ├── new-subdomains.txt
        └── subdomains.txt
```

So here, `domains.txt` is well known, `init.py` is the script that will initialize new targets, `runner.py` is the main script, `sorter.py` will take out desired number of domains from `domains.txt` and output it to `max.txt.` And the last, `last.txt` is the file containing the last scanned domains so that the script can continue from that.

## sorter.py

First of all, let’s see the code for `sorter.py`

```
import os

# Edit the line below to specify the number of domains to be scanned in a run
max_scans = 11

last_scanned_url = open("last.txt", 'r').read().replace("\n", '')

length = 0

with open("domains.txt", "r") as urls_file:
    for url in urls_file:
        url = url.replace('\n', '')
        if url == last_scanned_url:
            for i in range(max_scans):
                next_url = urls_file.readline().replace('\n', '')
                print(next_url)
                length += 1
                open('last.txt', 'w').write(next_url)

if length < max_scans:
    with open("domains.txt", 'r') as urls_file:
        for url in urls_file:
            url = url.replace('\n', '')
            if length < max_scans:
                print(url)
                length += 1
                open('last.txt', 'w').write(url)
```

And now, let’s see this in action

Video to sorter.py

I hope that you’ve understood, but if not let’s understand.

This code first of all opens a file called `last.txt` , and gets the last scanned domain. After that it opens the file `domains.txt` and check where is the last scanned domain. Once it is found, it prints the domain and write it to `last.txt` so that it can continue from there next time it is run. Also, if it reaches the last line of file, it jumps to the first and then start reading again. It is run with command `python3 sorter.py > max.txt` so that it can write the output to the file. Now, a simple question

> This can be done straight from the main script, so why it is here?
>
> Ans. Yes, you can do that. But things gets messy when you have multiple bots. To avoid messing up in things, do them in a neat manner

## Creating the main script — runner.py

`runner.py` — It is the most important script for us, as this will be responsible for doing all the tasks. But before setting it up, we need to set up our slack channel, so let’s do that first.

### Setting up slack channel

Assuming that you already have a slack account and a workspace, follow the steps below:-

* ***Open the slack workspace (https://app.slack.com/client/<something>/<otherthing>) and click add channel***

Press enter or click to view image in full size

![]()

Click on add channels button

* ***Give it a good name and click create and skip adding some people (if you wish to add some people, feel free to go ahead)***

![]()

Giving the channel a name

* ***Now, head over to*** [***https://api.slack.com/***](https://api.slack.com/) ***and click create an app***

Press enter or click to view image in full size

![]()

Creating a new app

* ***After that, a new box should pop up, on that click*** `From Scratch` ***> Give it a name > Assign it a channel and click creat...