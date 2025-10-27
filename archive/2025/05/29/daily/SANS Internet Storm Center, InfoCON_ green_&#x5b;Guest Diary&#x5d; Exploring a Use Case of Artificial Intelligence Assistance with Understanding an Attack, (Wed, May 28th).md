---
title: &#x5b;Guest Diary&#x5d; Exploring a Use Case of Artificial Intelligence Assistance with Understanding an Attack, (Wed, May 28th)
url: https://isc.sans.edu/diary/rss/31980
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-29
fetch_date: 2025-10-06T22:29:46.760897
---

# &#x5b;Guest Diary&#x5d; Exploring a Use Case of Artificial Intelligence Assistance with Understanding an Attack, (Wed, May 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31978)
* [next](/diary/31986)

# [[Guest Diary] Exploring a Use Case of Artificial Intelligence Assistance with Understanding an Attack](/forums/diary/Guest%2BDiary%2BExploring%2Ba%2BUse%2BCase%2Bof%2BArtificial%2BIntelligence%2BAssistance%2Bwith%2BUnderstanding%2Ban%2BAttack/31980/)

**Published**: 2025-05-28. **Last Updated**: 2025-05-28 13:48:55 UTC
**by** [Jennifer Wilson, SANS.edu BACS Student](/handler_list.html#jennifer-wilson,-sans.edu-bacs-student) (Version: 1)

[1 comment(s)](/diary/Guest%2BDiary%2BExploring%2Ba%2BUse%2BCase%2Bof%2BArtificial%2BIntelligence%2BAssistance%2Bwith%2BUnderstanding%2Ban%2BAttack/31980/#comments)

[This is a Guest Diary by Jennifer Wilson, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].]

As part of my BACS internship with SANS, I setup and maintained a DShield honeypot instance using a physical Raspberry Pi device.  As I was putting together each of my attack observations that were due, I started to wonder how helpful AI would be. One of the things I wanted to do when I started the internship was to step outside of my comfort zone. While I have read a lot about AI, I have only used it a handful of times. So, I wondered if it would lead me astray? Would it provide valid actionable data?

In this blog post, I will explore how accurate and helpful ChatGPT is with identifying one of the more unique attacks I say over the past few months.

To set the stage, I first noticed this attack after running the cowrieprocessor script [2] on my honeypot. The attack occurred on 2025-04-20 and came from IP address 63[.]212[.]157[.]187. The total attack occurred over a duration of 62.83 seconds. According to AbuseIPDB [3], the IP has been reported 300 times, and it has been marked with a 100% confidence of abuse. This IP has been busy in the world. Along with this basic data, the following commands were captured being ran on the honeypot:

```

# ifconfig
# uname -a
# cat /proc/cpuinfo
# ps | grep '[Mm]iner'
# ps -ef | grep '[Mm]iner'
# ls -la ~/.local/share/TelegramDesktop/tdata /home/*/.local/share/TelegramDesktop/tdata /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
# locate D877F783D5D3EF8Cs
# echo Hi | cat -n
```

Let’s first break down the first 5 commands:

| Command | Use |
| --- | --- |
| `ipconfig` | Displays network configuration in Unix-Like environments. |
| `uname -a` | Displays system information. |
| `cat /proc/cpuinfo` | Displays CPU information. |
| `ps | grep ‘[Mm]iner’` | Searches running processes for the string ‘Miner’ or ‘miner’. |
| `ps -ef | grep ‘[Mm]iner’` | Searches running processes for the string ‘Miner’ or ‘miner’ and provides detailed information for the matching data. |

**Figure 1: Break down of commands the attacker ran and its function**

Ok, those are common commands that an attacker will often run to attempt to discover more information about a system on which they have landed on. Searching specifically for ‘**`[Mm]iner`**’ is interesting. The attacker is trying to discover if the system is currently being used as a crypto miner.

The next two commands caught my attention. The following command is searching to determine if the mentioned paths exist on the file system, including if they are hidden:

```

?ls -la ~/.local/share/TelegramDesktop/tdata /home/*/.local/share/TelegramDesktop/tdata /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*?
```

The **`‘locate D877F783D5D3EF8Cs`**’ command is attempting to locate ‘**`D877F783D5D3EF8Cs`**’ on the file system. But what is ‘**`D877F783D5D3EF8Cs`**’? This is not a string I have seen before. Normally I would run to Google and start searching around to see if I could determine what it is. I got to wonder though, could ChatGPT or another platform provide me with results as well. More importantly would it provide me with accurate results?

I started out simple, as can be seen in the below screenshot from my ChatGPT conversation [4], to see what feedback it would provide.

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure1.PNG)
Figure 2: ChatGPT’s response to ‘What is D877F783D5D3EF8Cs’.**

Given the response that ChatGPT had, I clearly need to be more specific in my request.

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure3.PNG)
Figure 3: ChatGPT’s response to telling it that ‘D877F783D5D3EF8Cs’ was found on a honeypot.**

ChatGPT still seems to be guessing a bit. I want to see if I can get it to give me a more specific answer. Let’s see what happens when I provide it with the full command that was detected on the honeypot. Here is a snippet of what ChatGPT provided back:

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure4.PNG)
Figure 4: ChatGPT’s response to providing the full command that was detected on the honeypot.**

This has gotten me closer to a definite answer. I got curious about what would happen if I gave it the context of the command that was run before it. A snippet of its response is found below:

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure5.PNG)
Figure 5: ChatGPT’s response to providing it the previous ls -la command.**

The responses are now getting more detailed. ChatGPT suggests that the attack I am reviewing is part of a credential harvesting or SMS hijacking campaign [4]. Let’s see if it knows of any connection between the **`‘D877F783D5D3EF8Cs`**’ and Telegram:

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure6.PNG)
Figure 6: ChatGPT’s response when asking about a connection between the string ‘D877F783D5D3EF8Cs’ and Telegram.**

While I only asked ChatGPT [3] about the context of ‘**`D877F783D5D3EF8Cs`**’ in relation to Telegram, it narrowed it down to Telegram Desktop and specifically the folder tdata. Looking back at the ls -la command, one of the folders the attacker was trying to list was **`~/.local/share/TelegramDesktop/tdata`**. Without knowing exactly what the attacker was attempting to do, in the context of the rest of the commands the attacker ran, this seems like a logical response.

Now that I have gotten a logical response from ChatGPT, I always verify that response. A quick Google search led me to several sources that confirmed what ChatGPT was providing me with as a response [5][6][7].

While it took a bit of time probing ChatGPT to get an answer, the more context I gave it the better the result I got back. This would work well for an attack where I understood part of what was happening, but needed clarification on one section, like this attack.

Let’s see what would happen if I drop the ‘s’ off the string ‘**`D877F783D5D3EF8Cs`**’ and ask about just ‘**`D877F783D5D3EF8C`**’ in relation to Telegram. ChatGPT has been dropping it off in most of its responses to me so maybe it is just a typo.

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure7.PNG)
Figure 7: ChatGPT’s response when asking about a connection between the string ‘`D877F783D5D3EF8C`’ and Telegram.**

Now ChatGPT seems very confident in the response it provided [4]. I then did a Google search dropping the ‘s’ off again, I got several of the same references as I did before. One difference being a Medium blog by XIT called “Lesson 10: Stealing Accounts Sessions with Malware” [8]. This could be what the attacker’s goal is. It lines up with what we learned from ChatGPT so far.

When I was testing to see if this attack would make a good example however, I got different responses. ChatGPT believed that the string ‘**`D877F783D5D3EF8Cs`**’ was part of an...