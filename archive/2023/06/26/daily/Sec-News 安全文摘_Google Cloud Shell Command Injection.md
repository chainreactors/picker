---
title: Google Cloud Shell Command Injection
url: https://govuln.com/news/url/8njp
source: Sec-News 安全文摘
date: 2023-06-26
fetch_date: 2025-10-04T11:44:13.267809
---

# Google Cloud Shell Command Injection

[bugra.ninja](/)

# Google Cloud Shell - Command Injection

2022-08-10

![Google Cloud Shell - Command Injection](/images/shell.png)

Hi, I’m [bugra](https://twitter.com/bugraeskici), and here is a write-up about my Google Bug Bounty report.

On January 28, 2022, I was chatting in the [TR Bug Hunters](https://twitter.com/trbughunters) telegram group. One of the group members, [Numan TÃ¼rle](https://twitter.com/numanturle), told us that we should give Google Cloud Shell a try to find some juicy stuff.
I was in burn-out but investigating Cloud Shell caught my attention. So, let’s start.

#### What is Google Cloud Shell? (explanation from <https://cloud.google.com/shell>) [#](#what-is-google-cloud-shell-explanation-from-httpscloudgooglecomshell)

`Cloud Shell is an online development and operations environment accessible anywhere with your browser. You can manage your resources with its online terminal preloaded with utilities such as the gcloud command-line tool, kubectl, and more. You can also develop, build, debug, and deploy your cloud-based apps using the online Cloud Shell Editor.`

#### Investigating Google Cloud Shell [#](#investigating-google-cloud-shell)

Firstly, I always check my target’s [web archive page](http://web.archive.org/cdx/search/cdx?url=*.shell.cloud.google.com/*&output=text&fl=original&collapse=urlkey) to find some interesting URLs.
There were not a lot of URLs, but I could find some parameters to dig.
One of them was the `project` parameter. This parameter’s value changes our project in the Cloud Shell.
Simply, if we visit `https://shell.cloud.google.com/?project=test`, our project name changes to `test` in the Cloud Shell terminal.
I tried many things in this parameter but couldn’t find anything. While playing with this parameter, I noticed there is another parameter called `show`, which changes the Cloud Shell terminal.
In default, Cloud Shell works with `show=ide,terminal`. And that terminal looks like this :

![](/images/cloudshelltheme2.png)

I changed that parameter to `show=ide`, and I got this terminal :

![](/images/cloudshelltheme1.png)
While in this terminal, I tried the same things I tested in the first terminal.
I typed `asd'` to the project parameter and saw something very exciting in the terminal.

![](/images/cloudshell1.png)
![](/images/cloudshell2.png)
Do you see what I see? The terminal ran a Python script that included the value of the `project` parameter without any encoding. And I got this error :

```
 File "<stdin>", line 9
  if 'asd'':
       ^
SyntaxError: EOL while scanning string literal
```

The apostrophe character in my value caused that error in the Python code. I quickly changed my value to `asd':#` to fix that syntax error. However, I got another error :

![](/images/cloudshell3.png)
![](/images/cloudshell4.png)

```
 File "<stdin>", line 10
  config.set('core', 'project', 'asd':#')
                    ^
SyntaxError: invalid syntax
```

So, my value also reflects to another line of the code. I know the first location is `if 'value':` and the other one is `config.set('core', 'project', 'value')`. The first one ends with `':` and the other one ends with `')`.
If we check [multi-line syntax](https://www.w3schools.com/python/gloss_python_multi_line_strings.asp) in Python, we can create multi-line texts with three apostrophes.

![](/images/pythonmultiline.png)

There is one apostrophe in the first code part and one apostrophe in the last code part. So, I just added two apostrophes to the print function and made the built-in code dummy.
I changed my project value to `asd':print(''` and the Python code ran without any syntax errors!
I fixed the syntax of the Python code, and then I can execute any Python code after the `if` statement. Right? Yep!

I changed my project value to `asd':import os;os.system("cat /etc/passwd");print(''` and got this :

![](/images/cloudshell5.png)
![](/images/cloudshell6.png)

Bingo, got the command injection in the Cloud Shell! I was also able to get a remote shell without any trouble. Here is a video demonstrating the attack.

#### Timeline [#](#timeline)

Jan 28, 2022, 06:40 PM: Sent the report to Google VRP.
Jan 28, 2022, 07:00 PM: Got the `Nice Catch!` message. Report accepted as P1.
Feb 15, 2022, 08:55 PM: $$$$ :)
Jun 1, 2022, 02:42 PM: Fixed. (probably fixed before, but I noticed on Jun 1)

Kudos to the Google VRP team for triaging the report within 20 minutes. That’s insane! Also, thanks to Numan TÃ¼rle for inspiring me to research the Cloud Shell.
Lastly, thank you very much for reading my write-up. I hope you liked it. You can contact me on Twitter [@bugraeskici](https://twitter.com/bugraeskici).

[Bugra Eskici](https://twitter.com/bugraeskici) | Theme created by
[panr](https://twitter.com/panr)