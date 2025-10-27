---
title: Finding Honeypot Data Clusters Using DBSCAN: Part 2, (Fri, Sep 13th)
url: https://isc.sans.edu/diary/rss/31194
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-14
fetch_date: 2025-10-06T18:30:33.163290
---

# Finding Honeypot Data Clusters Using DBSCAN: Part 2, (Fri, Sep 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31188)
* [next](/diary/31196)

# [Finding Honeypot Data Clusters Using DBSCAN: Part 2](/forums/diary/Finding%2BHoneypot%2BData%2BClusters%2BUsing%2BDBSCAN%2BPart%2B2/31194/)

**Published**: 2024-09-13. **Last Updated**: 2024-09-13 14:45:14 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Finding%2BHoneypot%2BData%2BClusters%2BUsing%2BDBSCAN%2BPart%2B2/31194/#comments)

In an earlier diary [1], I reviewed how using tools like DBSCAN [2] can be useful to group similar data. I used DBSCAN to try and group similar commands submitted to Cowrie [3] and URL paths submitted to the DShield web honeypot [4]. DBSCAN was very helpful to group similar commands, but it was also very useful when trying to determine whether commands from one honeypot were seen in another. How much overlap in attack data is there between honeypots? Is there any targeting based on the hosting location of the honeypot?

Once the data is separated into clusters and the appropriate EPS and Minsample values are selected, comparing the data in a table can help hightlight differences..

```

# query to pull out cluster with minsample=3, EPS=0.5

select sum(AWS), sum(Azure), sum("Digital Ocean"), sum(GCP), sum(Residential), sum(AWS + Azure + "Digital Ocean" + GCP + Residential) as total,
count(input) , "cluster-EPS(0.5)-MINS(3)" from commands group by "cluster-EPS(0.5)-MINS(3)";
```

![](https://isc.sans.edu/diaryimages/images/2024-09-13_figure1_v2.PNG)
**Figure 1: Cluster showing number of similar commands run on honeypots, highlighting gaps in other honeypot reports.**

Looking at cluster 9 can give us more details on what may have been different.

```

# select command data from cluster 9
select input, sum(AWS), sum(Azure), sum("Digital Ocean"), sum(GCP), sum(Residential), sum(AWS + Azure + "Digital Ocean" + GCP + Residential)
as total from commands where "cluster-EPS(0.5)-MINS(3)"=9;

# input value seen
apt update && apt install sudo curl -y && sudo useradd -m -p $(openssl passwd -1 233QPpqY) system && sudo usermod -aG sudo system
```

Going back to the source data, more information can be seen about the particular commands.

**![](https://isc.sans.edu/diaryimages/images/2024-09-13_figure2.PNG)
Figure 2: Commands that only showed up from the Azure honeypot.**

**![](https://isc.sans.edu/diaryimages/images/2024-09-13_figure3.PNG)
FIgure 3: Differences between the commands is the password used**

The original goal was to group similar commands, which worked well in this instance. The commands were all the same, except for the password used. In addition, the comparison of the cluster data helped demonstrate which information from one honeypot may not be in another.

Within the command clusters, there were other differences noted in my dataset:

| Command | Honeypot |
| --- | --- |
| ```  apt update && apt install sudo curl -y && sudo useradd -m -p $(openssl passwd -1 233QPpqY) system &&  sudo usermod -aG sudo system ``` | Azure |
| ```  echo "Dolphinscheduler@2022\nkeSBVXNe9Y9k\nkeSBVXNe9Y9k\n"|passwd ``` | Digital Ocean |
| ```  lscpu && echo -e "CRN63r9D\nCRN63r9D" | passwd && curl https://ipinfo.io/org --insecure -s &&  free -h && apt ``` | Azure |
| ```  openssl passwd -1 233QPpqY ``` | Azure |

**Figure 4: Commands or types of commands seen that were unique to a honeypot.**

Some of the commands above are more unqiue due to the general commands used. In other examples, such as the second example from Digital Ocean, the password used is more of an outlier than others. There were many instances of "Dolphinscheduler@2022" that were not seen within other honeypots, although the general command was seen within other honeypots with different passwords used. The length of this password helped highlight this particular command as being unique, but it did generate its own cluster with different passwords that were similarly formatted.

**![](https://isc.sans.edu/diaryimages/images/2024-09-13_figure4.PNG)
Figure 5: Examples of "Dolphinscheduler@2022" seen within Digital Ocean honeypot commands.**

These honeypot comparisons were part of a research project for a Master's in Cyber Security Degree with SANS.edu [5]. The custom package created to extract and compare local honeypot data is available on GitHub [6]. This includes how the cluster features were created and used [7].

[1] [https://isc.sans.edu/diary/Finding+Honeypot+Data+Clusters+Using+DBSCAN+Part+1/31050](https://isc.sans.edu/diary/Finding%2BHoneypot%2BData%2BClusters%2BUsing%2BDBSCAN%2BPart%2B1/31050)
[2] <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html>
[3] <https://github.com/cowrie/cowrie>
[4] <https://isc.sans.edu/honeypot.html>
[5] <https://www.sans.edu/cyber-security-programs/masters-degree/>
[6] <https://github.com/jslagrew/dshield-parser/tree/main/examples>
[7] <https://github.com/jslagrew/dshield-parser/blob/main/examples/url-command-clustering.py>

--
Jesse La Grew
Handler

Keywords: [dbscan](/tag.html?tag=dbscan) [dshield](/tag.html?tag=dshield) [honeypot](/tag.html?tag=honeypot) [python](/tag.html?tag=python)

[0 comment(s)](/diary/Finding%2BHoneypot%2BData%2BClusters%2BUsing%2BDBSCAN%2BPart%2B2/31194/#comments)

* [previous](/diary/31188)
* [next](/diary/31196)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)