---
title: Number Usage in Passwords: Take Two, (Thu, Apr 9th)
url: https://isc.sans.edu/diary/rss/32866
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-09
fetch_date: 2026-04-10T04:47:43.907896
---

# Number Usage in Passwords: Take Two, (Thu, Apr 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32864)
* [next](/diary/32870)

Click HERE to learn more about classes Jesse is teaching for SANS

# [Number Usage in Passwords: Take Two](/forums/diary/Number%2BUsage%2Bin%2BPasswords%2BTake%2BTwo/32866/)

**Published**: 2026-04-09. **Last Updated**: 2026-04-09 00:58:14 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Number%2BUsage%2Bin%2BPasswords%2BTake%2BTwo/32866/#comments)

In a previous diary [1], we looked to see how numbers were used within passwords submitted to honeypots. One of the items of interest was how dates, and more specifically years, were represented within the data and how that changed over time. It is often seen that years and seasons are used in passwords, especially when password change requirements include frequenty password changes. Some examples we might see today:

* `Spring2026!`
* `Spring26`
* `April2026`
* `April@2026`
* `AprilShowers26`
* `Bloom2026`
* `Easter2026!`
* `Passover2026`

How is this data represented within passwords submitted to honeypots? Are bots updated to incorporate new year values at certain intervals?

**Date range of data:** 4//21/2024 - 3/29/2026
**Number of unique passwords:** 496,562

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure1.png)
Figure 1: Top 10 contiguous numbers used in passwords submitted to sample of DShield honeypots.**

When looking at contiguous numbers used within passwords, we see similar data from a couple of years ago. The top two contigious numbers seen within passwords submitted to honeypots were "123" and "1". However, rather than many of the other high volume contiguous numbers representing a subset of "123456", the passwords included other numbers such as "100000", "19", "69", "200".

It turns out that this activity was related to a potential DDoS or stress testing of and endpoing using ICMP. "100000" was the desired number of packets sent to the destionation host and the other numbers represented each octet of the destination IP.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure2.PNG)
Figure 2: Passwords submitted to honeypots that were supposed to be commands run once access was gained to the honeypot.**

The source IP [147.45.47.117](/ipinfo.html?ip=147.45.47.117) was attempting these commands between 11/18/2024 and 11/24/2024. The activity was seen on honeypots distributed in GCP, Digital Ocean, Azure and a residential honeypot. This was not seen on samples from an AWS honeypot.

Other activities from this source were seen between 11/14/2024 and 12/1/2024. Most of the sessions from this host are repeated attempts to download a script from [45.125.66.215](/ipinfo.html?ip=45.125.66.215) and install it as a service.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure3_v2.PNG)
Figure 3: Repeated attempts to setup and install a service using a downloaded script from [45.125.66.215](/ipinfo.html?ip=45.125.66.215).**

Unfortunately, the file was not downloaded by any of the honeypots, so there was not a file to reference.

Okay, back to passwords and number usage. Let's take a look at number frequency use in the passwords submitted to honeypots.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure3.PNG)
Figure 4: Individual number frequency used within passwords submitted to honeypots.**

Similar to the previous review, generally the lower the number, the more frequently it's used in a password. The most common digits used are "0", "1", "2" and "3". What about 4-digit numbers?

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure4.PNG)
Figure 5: Top 10 numbers used within passwords submitted to honeypots only containing 4 digits.**

This was also similar to the previous review. "1234" is still the most common and usually the most prevelant year seen is the prior year. We do see "2026" in this list, but since there's only a few months of data, it hasn't quite hit the volume of the previous year. One of the curiousities from this data is when these years get introduced. For example, when does "2026" start getting used within a password submitted to a honeypot?

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure6.PNG)
Figure 6: Heatmap of years used within passwords and when they showed up in honeypot data.**

Overall, it appears that 4-digit numbers representing years show up more prevalently in the year in which that data was submitted to a honeypot. From Figure 6, we see that "2025" shows up most frequently in data captured from honeypot logs in 2025. This also appears similar for "2024". An item that was surprising when looking at the data, is that there were already some hits for "2027".

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure7.PNG)
Figure 7: Passwords containing year and their volume over time, showing a small number of submissions containing "2027".**

| Year contained in password | First seen in samples | Example password |
| --- | --- | --- |
| 2024 | 11/1/2023  (found in expanded dataset) | `sysadmin2024` |
| 2025 | 4/5/2024 | `@dm1n2025` |
| 2026 | 5/6/2024 | `@2026` |
| 2027 | 8/11/2024 | `2027` |

**Figure 8: Passwords containing recent years, when they first appeared in the dataset along with some example passwords.**

Most of the passwords containing what could be a year are introduced the year before. However, that may vary widely from the beginning to the end of the previous year. There are also many other "future" years seen within the dataset.

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure8.PNG)
**Figure 9: Heatmap of future years used within passwords from data collection, showing "2023" was heavily used in the data collected near the end of 2024.**

| Year contained in password | First seen in samples | Example password | Password submission source |
| --- | --- | --- | --- |
| 2028 | 4/27/2024 | `020283` | [27.47.108.14](/ipinfo.html?ip=27.47.108.14) |
| 2029 | 4/27/2024 | `220291` | [27.47.108.14](/ipinfo.html?ip=27.47.108.14) |
| 2030 | 4/21/2024 | `1020304050` | [124.220.63.230](/ipinfo.html?ip=124.220.63.230) |
| 2031 | 4/24/2024 | `19820313` | [103.174.9.66](/ipinfo.html?ip=103.174.9.66) |
| 2032 | 4/24/2024 | `19820320` | [103.174.9.66](/ipinfo.html?ip=103.174.9.66) |
| 2033 | 4/27/2024 | `110220330` | [27.47.108.14](/ipinfo.html?ip=27.47.108.14) |
| 2034 | 8/11/2024 | `2034` | [45.90.13.172](/ipinfo.html?ip=45.90.13.172) |
| 2035 | 5/5/2024 | `235842035` | [185.161.248.247](/ipinfo.html?ip=185.161.248.247) |
| 2036 | 4/27/2024 | `3203672` | [27.47.108.14](/ipinfo.html?ip=27.47.108.14) |
| 2037 | 8/11/2024 | `2037` | [45.90.13.172](/ipinfo.html?ip=45.90.13.172) |
| 2038 | 4/27/2024 | `020384` | [27.47.108.14](/ipinfo.html?ip=27.47.108.14) |
| 2039 | 4/27/2024 | `220391` | [27.47.108.14](/ipinfo.html?ip=27.47.108.14) |
| 2040 | 4/24/2024 | `19820402` | [103.174.9.66](/ipinfo.html?ip=103.174.9.66) |

**Figure 10: Passwords containing future years, when they first appeared in the dataset along with some example passwords.**

In the cases where a future year is being used, the passwords likely have nothing to do with that year. However, there are a few examples that could be dates:

* `19820313`: 03/13/1982
* `19820320`: 03/20/1982
* `19820402`: 04/02/1982

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure9.PNG)
**Figure 11: In most cases, the years are used at the end of the password, rather than in the middle or beginning of the password.**

From the examples, focusing on a 4-digit number that's added to the end of a password could give us more representative examples of a number used intentionally to represent a year. Passwords containing "2027" for example, have a very different distribution on where they appear in the passwords. We see a much high...