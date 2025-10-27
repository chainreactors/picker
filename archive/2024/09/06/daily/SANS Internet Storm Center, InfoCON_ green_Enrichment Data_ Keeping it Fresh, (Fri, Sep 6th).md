---
title: Enrichment Data: Keeping it Fresh, (Fri, Sep 6th)
url: https://isc.sans.edu/diary/rss/31236
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-06
fetch_date: 2025-10-06T18:29:49.868480
---

# Enrichment Data: Keeping it Fresh, (Fri, Sep 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31232)
* [next](/diary/31240)

# [Enrichment Data: Keeping it Fresh](/forums/diary/Enrichment%2BData%2BKeeping%2Bit%2BFresh/31236/)

**Published**: 2024-09-06. **Last Updated**: 2024-09-05 23:58:02 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Enrichment%2BData%2BKeeping%2Bit%2BFresh/31236/#comments)

I like to enrich my honeypot data from a variety of sources to help understand a bit more about the context of the attack. This includes the types of networks the attacks are coming from or whether malware submitted to a honeypot is new. I use a variety of sources to enrich my cowrie data using cowrieprocessor [1]:

* Internet Storm Center / DShield API [2]
* URLhaus [3]
* SPUR [4]
* VirusTotal [5]

I was curious how often the data changed and how "fresh" the data needs to be in order to be accurate. In a previous diary I went into details about VirusTotal data and vendor comparisons [6].

## Data Collection

Data was pulled from the above sources using my cowrieprocessor script [1]. The script keeps a local copy of most enrichment data, which means I can always go through the JSON files at a later date to extract different information. The data I have goes back as far as May 2022. My honeypots schedule this data enrichment to happen once a day for attacks that happened the previous day. This means a minimum gap of time of 24 hours between enrichment data queries. This process was scheduled to run more frequently in 2022 and 2023 and may have a smaller gap between enrichment queries of 6-12 hours.

## VirusTotal Data

I extracted the following fields for comparison:

* **ID** (file hash)
* **Malicious** (number of vendors/engines that label the file as malicious)
* **Suspicious**  (number of vendors that label the file as suspicious)
* **Undetected** (number of vendors that did not have any detection)
* **Harmless** (number of vendors that label the file as harmless)
* **Timeout** (number of vendors that had a timeout)
* **Confirmed-timeout** (number of vendors that confirmed the timeout)
* **Failure** (number of vendors where a failure was reported)
* **Type-unsupported** (number of vendors that did not support the indicator type)
* **Type\_tag** (type of file)
* **Type\_description** (type description)

More details about the VirusTotal data fields can be found in their documentation [7]. The data was reviewed to look for hashes that showed a wide range of total "malicious" indicators as determined by different products.

| Date | Time | Hash | Malicious | Suspicious | Type Description |
| --- | --- | --- | --- | --- | --- |
| 12/29/2023 | 120001 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 1 | 0 | ELF |
| 12/29/2023 | 180002 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 1 | 0 | ELF |
| 12/30/2023 | 003001 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 1 | 0 | ELF |
| 3/3/2024 | 003001 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 2 | 0 | ELF |
| 4/21/2024 | 003002 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 2 | 0 | ELF |
| 7/18/2024 | 003001 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 22 | 0 | ELF |
| 8/10/2024 | 003002 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 26 | 0 | ELF |
| 8/13/2024 | 003002 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 25 | 0 | ELF |
| 8/15/2024 | 003003 | 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a | 25 | 0 | ELF |

**Figure 1: VirusTotal results over time for hash 062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a [8].**

| Date | Time | Hash | Malicious | Suspicious | Type Description |
| --- | --- | --- | --- | --- | --- |
| 12/21/2023 | 180002 | 47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c | 1 | 0 | ELF |
| 12/22/2023 | 003002 | 47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c | 1 | 0 | ELF |
| 4/7/2024 | 003001 | 47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c | 2 | 0 | ELF |
| 7/31/2024 | 003002 | 47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c | 29 | 0 | ELF |

**Figure 2: VirusTotal results over time for hash 47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c [9].**

| Date | Time | Hash | Malicious | Suspicious | Type Description |
| --- | --- | --- | --- | --- | --- |
| 5/7/2023 | 060002 | 306f0c79ad9ee76e996556f909306fda5704b456d670aa9daeb54760b4b5e4f6 | 2 | 0 | ELF |
| 5/7/2023 | 120001 | 306f0c79ad9ee76e996556f909306fda5704b456d670aa9daeb54760b4b5e4f6 | 3 | 0 | ELF |
| 5/7/2023 | 180002 | 306f0c79ad9ee76e996556f909306fda5704b456d670aa9daeb54760b4b5e4f6 | 3 | 0 | ELF |
| 5/8/2023 | 003002 | 306f0c79ad9ee76e996556f909306fda5704b456d670aa9daeb54760b4b5e4f6 | 3 | 0 | ELF |
| 5/10/202 | 003001 | 306f0c79ad9ee76e996556f909306fda5704b456d670aa9daeb54760b4b5e4f6 | 24 | 0 | ELF |

**Figure 3: VirusTotal results over time for hash 306f0c79ad9ee76e996556f909306fda5704b456d670aa9daeb54760b4b5e4f6 [10].**

This demonstrates that VirusTotal data can take months to have a large increase in malicious hits. The hash from Figure 3 was first submitted on March 10, 2023, so even though it looks like a very quick change in my sample of data, this was approximatey two months from the initial submission. Even if the data looks stable, it may have a dramatic change.

## URLhaus Data

URLHaus can be a good location of malicious URLs that may be used in phishing or other attacks, such as those seen in Cowrie honeypots. The data was reviewed to look for IP addresses that had a reported URL count change over time. In figure 4, the URL count increased by approximately 1 URL a day until it increased more dramatically between 11/8/2022 and 11/11/2022.

![](https://isc.sans.edu/diaryimages/images/2024-09-05_figure4.PNG)
Figure 4: **URLhaus reported URL changes over time for [179.43.175.5](/ipinfo.html?ip=179.43.175.5).**

In figure 5, the IP address URL count almost doubled in a couple of days.

**![](https://isc.sans.edu/diaryimages/images/2024-09-05_figure5.PNG)
Figure 5: URLhaus reported URL changes over time for [193.42.33.81](/ipinfo.html?ip=193.42.33.81).**

##

## SPUR Data

The data compared was retrieved from SPUR, but this kind of WHOIS data is available from a variety of sources. First, I wanted to take a look at how many differences were seen in the registration data by IP address. I limited the information compared to the IP address, organization and location information.

![](https://isc.sans.edu/diaryimages/images/2024-09-05_figure6.PNG)
**Figure 6: Breakdown of IP addresses and how many unique sets of data were seen per IP address.**

Over 3/4 of the IP addresses didn't have any change in the information reported. For the most part, the data doesn't change often. However, there were several IP addresses that had multiple changes. In figure 7, there were changes on average about once a month for the location.

**![](https://isc.sans.edu/diaryimages/images/2024-09-05_figure7.PNG)
Figure 7: IP Address [201.186.40.250](/ipinfo.html?ip=201.186.40.250) showing changes in geographic regions over time.**

In figure 8, the organization changed every couple of months between March and July of 2024. It may have changed more frequently, but was not recorded by my honeypot.

**![](https://isc.sans.edu/diaryimages/images/2024-09-05_figure8.PNG)
Figure 8: IP Address [101.32.114.105](/ipinfo.html?ip=101.32.114.105) showing changes in organization name over time.**

The raw WHOIS information for [101.32.114.105](/ipinfo.html?ip=101.32.114.105) contains information that refers to both organizations listed from the SPUR data.

```

% Information related to '101.32....