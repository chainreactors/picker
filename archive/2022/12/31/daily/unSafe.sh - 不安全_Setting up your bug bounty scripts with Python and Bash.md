---
title: Setting up your bug bounty scripts with Python and Bash
url: https://buaq.net/go-143463.html
source: unSafe.sh - 不安全
date: 2022-12-31
fetch_date: 2025-10-04T02:47:06.046539
---

# Setting up your bug bounty scripts with Python and Bash

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Setting up your bug bounty scripts with Python and Bash

Hi there,Automation is very interesting things, and if done in a right manner, it is more interestin
*2022-12-30 17:5:44
Author: [infosecwriteups.com(查看原文)](/jump-143463.htm)
阅读量:32
收藏*

---

Hi there,

Automation is very interesting things, and if done in a right manner, it is more interesting. But writing automation scripts is the most important thing for that. So, in this article, we’ll be discussing about writing automation scripts in Python and Bash for your VPS server (or maybe raspberry pi). If you’ve not read my previous article, [Monitoring your targets for bug bounties](https://infosecwriteups.com/monitoring-your-targets-for-bug-bounties-36f6be3e69c9), which is the main article for our series, I highly recommend you reading that first.

Photo by [Sai Kiran Anagani](https://unsplash.com/%40anagani_saikiran?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral); Automation script

First of all let’s decide what will be our automation system could be for. The following are the possibilities:-

* New subdomain monitoring
* Log poisoning
* Nuclei
* Waybackurls with gf
* Etc.

So, in this article, we will start by the very basic bot, for new subdomain monitoring

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

Creating directories to organize all the data is important. So we need to set up directories so that things won’t get messed up. The structure of the directory could be:-

```
.
```

So here, `domains.txt` is well known, `init.py` is the script that will initialize new targets, `runner.py` is the main script, `sorter.py` will take out desired number of domains from `domains.txt` and output it to `max.txt.` And the last, `last.txt` is the file containing the last scanned domains so that the script can continue from that.

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

`runner.py` — It is the most important script for us, as this will be responsible for doing all the tasks. But before setting it up, we need to set up our slack channel, so let’s do that first.

## Setting up slack channel

Assuming that you already have a slack account and a workspace, follow the steps below:-

* ***Open the slack workspace (https://app.slack.com/client/<something>/<otherthing>) and click add channel***

Click on add channels button

* ***Give it a good name and click create and skip adding some people (if you wish to add some people, feel free to go ahead)***

Giving the channel a name

* ***Now, head over to*** [***https://api.slack.com/***](https://api.slack.com/) ***and click create an app***

Creating a new app

* ***After that, a new box should pop up, on that click*** `From Scratch` ***> Give it a name > Assign it a channel and click create app***

Select scratch here

* ***Once created, go to*** `Incoming Webhooks` ***and switch it on***

Incoming webhook

Switch incoming webhooks on

* ***After it is switched on, you’ll see something like this on the same page below***

Slack webhook API

* ***Click on*** `Add New Webhook to Workspace` ***and it will redirect you to a page where you can select the slack channel to which it can send messages. Now, just select a channel, and click allow***

Allow the bot to send messages to slack channel with help of incoming webhook

* ***Once done, you will see a*** `curl` ***command at the place of*** `Sample curl request to post to a channel` ***. Just copy it, paste to a terminal, and you will see a message in your slack channel***

Get the cURL command for sending a slack message

Execute the command

And check your slack channel for the message

Now, we are done setting up our slack channel. The message could be changed by changing the value of `"text"` in JSON post data.

## runner.py — The main script

This script will be responsible for running different tools, comparing the output, and then send message to slack.

So first of all, we will create a function, that will send the message to slack

```
import requests

def send_msg_to_slack(message):
    # Get your webhook URL `Incoming Webhooks` page. It will be like
    # https://hooks.slack.com/services/T04RRRRRRRR/B04RRRRRRRR/B55JREDACTEDREDACTEDAAAA
    # The link above is just a random link
    webhook_url = "<paste_your_webhook_URL_here>"
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
```

Now, we need to run a tool for subdomains enumeration (here I will demonstrate with amass) with the help of python and then, compare the old file and new file. (**IMPORTANT**: The command should be run in the directory of the target only, and the script in `.` (according to directory structure above))

And before that, we will use the `system()` function of `os` module to execute the command. This can be done with `subprocess` module also.

```
from os import system

def run_amass():
    with open("max.txt", 'r') as file:
        for target in file:
            target = target.replace("\n", '')
            system(f"cd targets/{target}/ && amass enum -d {target} -o new-subdomains.txt")

# read the old subdomain list and save it in old_subdomains
            old_subdomains = []
            with open...