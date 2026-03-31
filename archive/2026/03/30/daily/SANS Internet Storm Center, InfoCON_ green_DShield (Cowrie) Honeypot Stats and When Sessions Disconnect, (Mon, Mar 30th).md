---
title: DShield (Cowrie) Honeypot Stats and When Sessions Disconnect, (Mon, Mar 30th)
url: https://isc.sans.edu/diary/rss/32840
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-30
fetch_date: 2026-03-31T04:37:22.884823
---

# DShield (Cowrie) Honeypot Stats and When Sessions Disconnect, (Mon, Mar 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32838)
* [next](/diary/32842)

Click HERE to learn more about classes Jesse is teaching for SANS

# [DShield (Cowrie) Honeypot Stats and When Sessions Disconnect](/forums/diary/DShield%2BCowrie%2BHoneypot%2BStats%2Band%2BWhen%2BSessions%2BDisconnect/32840/)

**Published**: 2026-03-30. **Last Updated**: 2026-03-30 18:53:05 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/DShield%2BCowrie%2BHoneypot%2BStats%2Band%2BWhen%2BSessions%2BDisconnect/32840/#comments)

A lot of the information seen on DShield honeypots [1] is repeated bot traffic, especially when looking at the Cowrie [2] telnet and SSH sessions. However, how long a session lasts, how many commands are run per session and what the last commands run before a session disconnects can vary. Some of this information could help indicate whether a session is automated and if a honeypot was fingerprinted. This information can also be used to find more interesting honeypot sessions.

To get an idea of what that variety looks like, I reviewed about 3 years of data from 6 honeypots. Some of the honeypots have been running for different periods of time, but it should give a good overview of different attacks seen on telnet/SSH honeypots. Since I already made a python script [3] that summarizes some of this data for me, it made the process a bit easier. Before going into the details, some of the basic information:

**Data Timeframe:** 4/13/2022 - 3/21/2026
**Number of Sessions:**1,206,566

|  | **Min** | **Max** | **Median** | **Mean** | **Range (Max-Min)** |
| --- | --- | --- | --- | --- | --- |
| **Number of Commands Per Session** | 0 | 27742 | 17.49 | 20.0 | 27742 |
| **Duration of Sessions (Seconds)** | 0.041 | 1563.38 | 17.42 | 22.80 | 1563.38 |

**Figure 1: Basic statistics for Cowrie session durations and number of commands run per session.**

In most sessions, we see about 20 commands and a session lasts for about 20 seconds.

## Number of Commands Per Session

When a Cowrie session is allowed through, the client connection has the option of running commands. They client may decide to disconnect, run an automated script or run commands manually. Most of the time, there are usually under 30 commands run per session, but there are some sessions that have had over 25,000 commands run in a single session.

![](https://isc.sans.edu/diaryimages/images/2026-03-30_figure1.png)
**Figure 2: There are many telnet/SSH sessions interacting with DShield honeypots that run over 25,000 commands in a single session, but most are much lower.**

**![](https://isc.sans.edu/diaryimages/images/2026-03-30_figure2.png)
Figure 3: Looking at most frequenty occuring number of commands run per telnet/SSH session, the majority are under 50 commads with the most frequent being 22 commands in a session.**

| Commands in session | Sessions found | Percentage | Running total |
| --- | --- | --- | --- |
| 22 | 461,561 | 38.26% | 38.26% |
| 20 | 348,708 | 28.91% | 67.17% |
| 1 | 104,217 | 8.64% | 75.81% |
| 3 | 58,850 | 4.88% | 80.69% |
| 9 | 39,111 | 3.24% | 83.93% |
| 13 | 28,274 | 2.34% | 86.27% |
| 46 | 27,595 | 2.29% | 88.56% |
| 5 | 25,302 | 2.10% | 90.66% |
| 18 | 20,174 | 1.67% | 92.33% |
| 10 | 19,188 | 1.59% | 93.92% |

**Figure 4: The top 10 most commonly seen number of commands run in a session accounts for about 94% of the telnet/SSH sessions.**

Are the sessions with 22 commands similar? To help commands for differnet sessions the commands per session were concatenated and then hashed to arrive at a value that could be compared across sessions. This value would be the same if the same commands were run in the same order. This seemed like a great idea until I found a very small number of similar hashes when looking at sessions with 22 commands. Rather than seeing tens or hundreds of thousands of similar hashes, there were only 4. Looking more closely at the data demonstrated what was missed.

**![](https://isc.sans.edu/diaryimages/images/2026-03-30_figure5_v2.png)
Figure 5: Cowrie sessions with matching command hashes, but with data that changed based on script inputs, in this case, passwords.**

Many attacks will often try to change passwords, but these comamnds will often change since differnet passwords may be successful on a honeypot and new password used could also be different. Trying to simplify the search and ignoring command by command details, 99.95% of sessions with a total command count of 22 may be similar (461,344 out of 461,561).

```

select count(sessions.session) from sessions, commands where sessions.total_commands="22" and sessions.session=commands.session and commands.command LIKE "%Enter new UNIX password:%";
```

The total number of commands run may be a good indicator of bot scripts being run. Even though many sessions may run the same commands in the same order, the duration of the sessions has a wide range.

```

SELECT
    printf('%.10f', min(cast(session_duration as real))),
    printf('%.10f', max(cast(session_duration as real)))
FROM sessions, commands
WHERE sessions.total_commands = "22"
  AND sessions.session = commands.session
  AND commands.command LIKE "%Enter new UNIX password:%"
  AND cast(session_duration as real) != 0;
```

**Minimum Duration:** 1.63 seconds
**Maximum Duration:** 233.05 seconds (a little under 4 minutes)

While a shorter session time may indicate automation, a longer session duration doesn't neccessarily mean that there is a person behind the keyboard.

## Session Durations

Session durations had much more variety than expected. They can range from about a second to upwards of 26 minutes. Taking into account only those command counts where we had at least two sessions:

| Commands in Session | Sessions Found | Min Duration (s) | Max Duration (s) | Duration Range (s) | Mean Duration (s) | Mean Commands/s |
| --- | --- | --- | --- | --- | --- | --- |
| 22 | 461561 | 1.63 | 233.05 | 231.42 | 19.44 | 1.13 |
| 20 | 348708 | 3.13 | 298.86 | 295.72 | 19.53 | 1.02 |
| 1 | 104217 | 0.05 | 1099.30 | 1099.25 | 8.48 | 0.12 |
| 3 | 58850 | 0.04 | 371.12 | 371.08 | 12.32 | 0.24 |
| 9 | 39111 | 0.16 | 1074.53 | 1074.36 | 23.39 | 0.38 |
| 13 | 28274 | 0.35 | 234.83 | 234.47 | 8.37 | 1.55 |
| 46 | 27595 | 3.38 | 217.07 | 213.69 | 113.72 | 0.40 |
| 5 | 25302 | 0.10 | 908.05 | 907.94 | 6.78 | 0.74 |
| 18 | 20174 | 0.63 | 397.26 | 396.63 | 22.19 | 0.81 |
| 10 | 19188 | 0.55 | 582.49 | 581.94 | 59.71 | 0.17 |
| 0 | 16281 | 0.04 | 1563.38 | 1563.34 | 83.30 | 0.00 |
| 15 | 15617 | 0.73 | 211.46 | 210.73 | 20.74 | 0.72 |
| 11 | 6753 | 0.69 | 795.15 | 794.46 | 56.99 | 0.19 |
| 7 | 6742 | 0.09 | 729.69 | 729.60 | 50.52 | 0.14 |
| 4 | 5375 | 0.11 | 990.44 | 990.33 | 42.32 | 0.09 |
| 2 | 5136 | 0.09 | 993.03 | 992.94 | 50.70 | 0.04 |
| 19 | 3310 | 1.29 | 207.76 | 206.47 | 43.97 | 0.43 |
| 6 | 2833 | 0.47 | 992.60 | 992.14 | 43.38 | 0.14 |
| 45 | 2614 | 1.95 | 225.16 | 223.21 | 84.67 | 0.53 |
| 21 | 1538 | 0.42 | 201.84 | 201.42 | 59.18 | 0.35 |
| 17 | 1311 | 0.43 | 197.86 | 197.42 | 53.24 | 0.32 |
| 14 | 1158 | 2.59 | 212.90 | 210.31 | 69.58 | 0.20 |
| 16 | 792 | 6.19 | 197.18 | 190.99 | 68.01 | 0.24 |
| 12 | 778 | 1.05 | 212.98 | 211.93 | 67.56 | 0.18 |
| 8 | 775 | 0.29 | 728.80 | 728.51 | 67.80 | 0.12 |
| 27 | 643 | 0.87 | 220.30 | 219.42 | 132.93 | 0.20 |
| 29 | 289 | 3.62 | 190.15 | 186.54 | 125.45 | 0.23 |
| 30 | 234 | 0.83 | 211.35 | 210.52 | 103.22 | 0.29 |
| 33 | 205 | 0.96 | 207.39 | 206.43 | 136.79 | 0.24 |
| 31 | 103 | 2.36 | 195.15 | 192.78 | 60.91 | 0.51 |
| 25 | 77 | 1.54 | 235.10 | 233.56 | 49.69 | 0.50 |
| 44 | 75 | 69.90 | 78.91 | 9.01 | 73.54 | 0.60 |
| 48 | 61 | 27.76 | 57.52 | 29.75 | 34.34 | 1.40 |
| 28 | 49 | 1.00 | 189.89 | 188.89 | 47.23 | 0.59 |
| 24 | 34 | 1.52 | 226.81 | 225.28 | 68.83 | 0.35 |
|...