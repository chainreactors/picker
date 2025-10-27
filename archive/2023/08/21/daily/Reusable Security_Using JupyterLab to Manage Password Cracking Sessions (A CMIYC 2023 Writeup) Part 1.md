---
title: Using JupyterLab to Manage Password Cracking Sessions (A CMIYC 2023 Writeup) Part 1
url: https://reusablesec.blogspot.com/2023/08/using-jupyterlab-to-manage-password.html
source: Reusable Security
date: 2023-08-21
fetch_date: 2025-10-04T11:59:29.095625
---

# Using JupyterLab to Manage Password Cracking Sessions (A CMIYC 2023 Writeup) Part 1

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### Using JupyterLab to Manage Password Cracking Sessions (A CMIYC 2023 Writeup) Part 1

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://www.blogger.com/profile/16111343330590419341 "author profile")

-
[August 19, 2023](https://reusablesec.blogspot.com/2023/08/using-jupyterlab-to-manage-password.html "permanent link")

[![MidJourney Imagining a Bunch of Data Scientists Cracking Passwords](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihtL654wNiDQbEEkozTnOuR8F86CffSe0MnNbnBL02R3LF4JgoMcKig1wXTQ5euhqy5YNmkAjvR05bHrOnPMi67sCRFKMGjfbCqb0cpjak17wheTMD1VD_2eCdFsZuzsKwkgzdauchtoWj73VRKGg2AVnnADbKXO2krNG0BA4ifX0rJJAzM5eGM_NRgok/w640-h366/group_of_computer_security_experts_graphs_and_charts.png "MidJourney Imagining a Bunch of Data Scientists Cracking Passwords")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihtL654wNiDQbEEkozTnOuR8F86CffSe0MnNbnBL02R3LF4JgoMcKig1wXTQ5euhqy5YNmkAjvR05bHrOnPMi67sCRFKMGjfbCqb0cpjak17wheTMD1VD_2eCdFsZuzsKwkgzdauchtoWj73VRKGg2AVnnADbKXO2krNG0BA4ifX0rJJAzM5eGM_NRgok/s1456/group_of_computer_security_experts_graphs_and_charts.png)

> **“We become what we behold. We shape our tools, and thereafter our tools shape us.”**
>
> **-- Marshall McLuhan**

This year I didn't compete in the Defcon Crack Me If You Can password cracking competition. It was my wife's first Defcon, so there was way too much stuff going on to sit around our hotel room slouched over a computer. But now that a week has passed and I'm back home, I figure the CMIYC Street Team Challenge would be a great use-case to talk about data science tools!

**Big Disclaimer:** I've read spoilers from other teams and have participated in the post-contest Discord server. I'm totally cheating here. The focus is on how you can use JupyterLab to perform analysis while cracking passwords. Not my problem solving skills (or lack there-of).

### Initial Exploration of the Challenge Files:

The CMIYC challenge file for street teams is available [here](https://contest-2023.korelogic.com/downloads.html). It's a pgp encrypted file so the first thing to do is decrypt them with the password KoreLogic provided.

* gpg -o cmiyc\_street\_01\_2023.yaml -d cmiyc-2023\_01\_street.yaml.pgp

Looking at the file in a text editor, you can quickly see that at first glance it appears to be a yaml file.

[![Picture of the start of the yaml file for the contest](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiduWn1xFuh8h3bHcxn0acCmoWPdnVKntIW51nNqb4wO1UhCIGATdPwY3UOibcqeOzfDGeCiTWO41fH-ITJogG9gc3TIbNG3Bv3FWVSQRuOyuQtBXDPt7mvzTrVVQcVvq8I_gWLTARkCzqdmTartWCBpMq-UqYr2RjzleSVa0XvJJFlXZwPhcZb14FtglY/w400-h271/cmiyc2023_yaml.png "I really don't like yaml files due to indentation mattering. But I do like Python... I can't explain it.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiduWn1xFuh8h3bHcxn0acCmoWPdnVKntIW51nNqb4wO1UhCIGATdPwY3UOibcqeOzfDGeCiTWO41fH-ITJogG9gc3TIbNG3Bv3FWVSQRuOyuQtBXDPt7mvzTrVVQcVvq8I_gWLTARkCzqdmTartWCBpMq-UqYr2RjzleSVa0XvJJFlXZwPhcZb14FtglY/s1084/cmiyc2023_yaml.png)

Of course, you shouldn't trust anything that the contest organizers throw your way! Next up is to validate the yaml format and see if there is anything obviously wrong with it. A quick way to do that is using yamllint. To install and run yamllint:

* pip install yamllint
* yamllint cmiyc\_2023\_01\_street.yaml

And the results are .... ok there's a lot of long lines....

[![Lots of line too long errors](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQsAqDXv4TjJqr36YB3ihor0UTMDPKbEdUHQyvSsaoBMPW_j2R-pL7kexobmjxkMZTHTzu3q4zkSFc2TKENRI2Sx0HjoXjxjSytSdZ5VZcKPUajzqyAKgwJr8cvBCn4K2fG_SXHBxmCajCDAi9Tv2h8Ld2aEbojmCh_BkD0L9nxMZ0glLIvtsiMNpH9-8/w400-h116/cmiyc2023_yaml_error.png "To be fair, most of my code has lines too long. Heck, this alt-text is way too long!")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQsAqDXv4TjJqr36YB3ihor0UTMDPKbEdUHQyvSsaoBMPW_j2R-pL7kexobmjxkMZTHTzu3q4zkSFc2TKENRI2Sx0HjoXjxjSytSdZ5VZcKPUajzqyAKgwJr8cvBCn4K2fG_SXHBxmCajCDAi9Tv2h8Ld2aEbojmCh_BkD0L9nxMZ0glLIvtsiMNpH9-8/s1139/cmiyc2023_yaml_error.png)

Luckily you can easily tune any of the checks that yamllint performs. To hide these errors you can set the max line length to 130 and run yamllint again using the command:

* yamllint -d "{extends: default, rules: {line-length: {max: 130}}}" cmiyc\_2023\_01\_street.yaml

This time, the file validated without any warnings. So it looks like the CMIYC challenge file is a valid YAML file. That doesn't mean that there isn't anything sneaky in it, but it makes data parsing a much easier task.

Next, let's quickly glance at the yaml contents. Opening up the file again, I see that it has 260424 lines. But each user entry has a variable number of fields associated with it. To get a quick idea of how many hashes I'm dealing with I used grep on PasswordHash. I then did a quick grep to see how many users there were by leveraging the fact that the YAML secondary categorty will start with a " - ".

[![Showing both of my greps returned the same number of expected password hashes](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjENGlmJbKK2FP8fexUhGBCV-SvpFtR4YOd9ehsfdlYRFZs1sh2TECAs6MvQaQ3S2qfyjd_8vMqGBsFvL3TzLy2bzwgm7FN0lt_6NboNrY3bHR0DLwpGrn-ICPxJSUeCAIzdOMCq0Vxu2gum1Z3zelfjAK0RInL1nDs1ScvPearcNF8v_mxPGkZBDAJNw/w400-h43/cmiyc2023_hash_count.png "I still remember when KoreLogic hid hashes by just pasting them into random files.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjENGlmJbKK2FP8fexUhGBCV-SvpFtR4YOd9ehsfdlYRFZs1sh2TECAs6MvQaQ3S2qfyjd_8vMqGBsFvL3TzLy2bzwgm7FN0lt_6NboNrY3bHR0DLwpGrn-ICPxJSUeCAIzdOMCq0Vxu2gum1Z3zelfjAK0RInL1nDs1ScvPearcNF8v_mxPGkZBDAJNw/s1622/cmiyc2023_hash_count.png)

Luckily the two numbers matched so that means there I'm looking to crack at least 29,847 password hashes. It also means that every user probably has one password hash associated with them.

So now we have the file, and looked around a bit, it seems like it's time to extract the hashes and crack some passwords! My default "Quick and Dirty" approach is to write a short awk script such as the following:

* cat cmiyc\_2023\_01\_street.yaml | grep PasswordHash: | awk -F": " '{print "1:"substr($2,2, length($2)-2)}' > greped\_password\_hashes.txt

The problem with this approach is that it dumps all the hashes into the same file, doesn't separate them by type, and I lose all that user and metadata associated with them. The loss of metadata is a real problem since I suspect it will play a very important role in actually cracking hashes for this contest. I'd really like to have a better way to create hash-lists and manage cracking sessions! This leads us to the next section of this writeup!

### Creating a JupyterLab Notebook:

JupyterLab notebooks are a way to organize and document all the random code you write while analyzing data. The name Jupyter stands for the programing/scripting languages it supports: [Julia, Python, R]. I think a better description of JupyterLab is that it's a stone soup. If you are on your own and doing a task only once, then it doesn't really add a whole lot. You're just drinking muddy water and it's a lot of extra pain to set it up and use it. The thing is, you are vary rarely on your own, and almost no task is done only once. Heck, I've probably only written one hello world program from scratch in my life. Every other program I've worked on since then I've copied off previous efforts. The documentation JupyterLab provides makes it easier to remember what you've done and build upon it for future efforts.

Long story short, I've never regretted starting a Jupyter Notebook. Somehow that soup is full of delicious ingredients at the end of the day!

Installing Jupyter is super easy. I primarily use Python (I reall...