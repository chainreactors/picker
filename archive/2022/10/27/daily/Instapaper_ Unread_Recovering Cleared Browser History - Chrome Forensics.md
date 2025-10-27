---
title: Recovering Cleared Browser History - Chrome Forensics
url: https://www.inversecos.com/2022/10/recovering-cleared-browser-history.html
source: Instapaper: Unread
date: 2022-10-27
fetch_date: 2025-10-03T21:03:54.161837
---

# Recovering Cleared Browser History - Chrome Forensics

[Skip to main content](#main)

### Search This Blog

# [@inversecos](https://www.inversecos.com/)

my research :D

### Recovering Cleared Browser History - Chrome Forensics

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[October 25, 2022](https://www.inversecos.com/2022/10/recovering-cleared-browser-history.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjes_w04ny8KT-yk16_rz9f-Jb9_TNEgJEgXQ9Eco1ag9utDpWAydu27qGmq4QBN6sp3HY61amOjhIXRELHSF1kxtICIszyqupBklRP55iGrb6tycz_-xuoGk0aC6sVqAvlcKIF7gLZBSSOeyg4J2X4mgKEi4We6n8hhxwvHEpmx9n4AkzSGvrZar3ytw/s16000/COVER.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjes_w04ny8KT-yk16_rz9f-Jb9_TNEgJEgXQ9Eco1ag9utDpWAydu27qGmq4QBN6sp3HY61amOjhIXRELHSF1kxtICIszyqupBklRP55iGrb6tycz_-xuoGk0aC6sVqAvlcKIF7gLZBSSOeyg4J2X4mgKEi4We6n8hhxwvHEpmx9n4AkzSGvrZar3ytw/s2067/COVER.png)

**Hello naughty sysadmin... I've been watching your search history this Summer O\_o**

How do you detect when a user deletes their chrome history and is there a way to forensically recover it? The answer is… it depends. 😈

A good indicator for recovering what a user was doing when they deleted their chrome browser history is by checking inside the C:\Users\<name>\AppData\Local\Google\Chrome\User Data\Default\Sessions folder. The two files you need to look at are named:

* Session\_<Webkit/Chrome date>
* Tabs\_<Webkit/Chrome date>

The session file stores session information and the tabs file stores what tabs they had opened. In a certain situation when a user CLEARS their Chrome history, what they were browsing can persist within these files.

There are a few potential cases that could have occurred, and we will go through all of them:

* A user cleared their history and did not use Chrome since
* A user clears their history and re-opened ONE new session
* A user clears their history and re-opened several sessions since

**Scenario 1: User cleared their history and did not use Chrome since**When a user clears their Chrome history (by all time or even by the last hour) and has not opened Chrome since, everything they were looking at during the session is STILL STORED inside the session files. This is great news because the session file is dated with the exact Webkit/Chrome timestamp in the name of the file. Why is this the case? I don't work for Google so I have nfi.

In this instance the files I’m looking at were named:

* Session\_13311227045752079
* Tabs\_13311227047407569

Using this time converter (<https://www.epochconverter.com/webkit>), you can see the time when the user “exited” the session was at 2022-10-26T03:04:05Z. You can see a full timeline of what the user did by viewing the contents of the file. Please note there are no corresponding “timestamps” captured within this file unfortunately. This is what the file looks like:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsCyIVRAwFv85ibVUrjFZqLMQ6vlGCXTuE9RjeYdq2XcvPBSlhbz4mTNUSfckm2IIZCNQRS0fi4yT-DsnOFixbZ4u1PBuYl8hbafDmiWg1Jj8BofW6GgQ5yosdF-mCt4lqQHoNlsBN-N4G4yyIkvZrsupywsmQAPz81hj0BEfQOUO2YMrFMX_B9NMEvA/s16000/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsCyIVRAwFv85ibVUrjFZqLMQ6vlGCXTuE9RjeYdq2XcvPBSlhbz4mTNUSfckm2IIZCNQRS0fi4yT-DsnOFixbZ4u1PBuYl8hbafDmiWg1Jj8BofW6GgQ5yosdF-mCt4lqQHoNlsBN-N4G4yyIkvZrsupywsmQAPz81hj0BEfQOUO2YMrFMX_B9NMEvA/s1437/2.png)

Does this look like a flipping mess? Yes. I know, but it's actually well structured and I'll show you what it looks like in a timeline output. This is a full timeline of what our strange sysadmin was looking at:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUWwfG5MNfunq-qxP3tpbS2ukiB__DxZ6tY56XtrneYQlhAfWHZJgRPJeL_zSYigxaj2pcl5XkB44L4xkX41SrYm7LlcscLribR4p3OQscBRODgoWjkqx-DBCivhulJZph8Cx3MlZSRN3UoL0zi68dCQ_H-zGnRprGBAAvFeM5Pm72Oq4RZ_LCYCWqkQ/s16000/3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUWwfG5MNfunq-qxP3tpbS2ukiB__DxZ6tY56XtrneYQlhAfWHZJgRPJeL_zSYigxaj2pcl5XkB44L4xkX41SrYm7LlcscLribR4p3OQscBRODgoWjkqx-DBCivhulJZph8Cx3MlZSRN3UoL0zi68dCQ_H-zGnRprGBAAvFeM5Pm72Oq4RZ_LCYCWqkQ/s1199/3.png)

In the case of this user, they were searching “Naruto Feet Pics” UwU and this is what they were looking at. They opened a Google search for “Naruto feet pics” and then this image is what they proceeded to “click”. The image source is <https://www.deviantart.com/tag/temaritoes>.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiW5TMHBWQscvq7acMVoVYYEkTyqlK0-WwJToT6cN_WnHxsAlmLtbshZUHtFcflppv6VJqC-xrman-rlXhhBnWfzA2ZrgsHlT0JSFHygixPs94nMWJWKmJOA0Uo4n6zqrgfCAVrPdZ0e02qZh-ETNI_Z15AjCpTon_rdz-GYMgWfUtPSRlGsCnN5DpYCg/s16000/Screen%20Shot%202022-10-26%20at%203.06.10%20pm.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiW5TMHBWQscvq7acMVoVYYEkTyqlK0-WwJToT6cN_WnHxsAlmLtbshZUHtFcflppv6VJqC-xrman-rlXhhBnWfzA2ZrgsHlT0JSFHygixPs94nMWJWKmJOA0Uo4n6zqrgfCAVrPdZ0e02qZh-ETNI_Z15AjCpTon_rdz-GYMgWfUtPSRlGsCnN5DpYCg/s1284/Screen%20Shot%202022-10-26%20at%203.06.10%20pm.png)

**Scenario 2: A user clears their history and re-opened ONE new session**

Firstly, how do you even know they did this? Let your girl help you out. In this instance two session files and tab files will exist in the directory!

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiza0DEIQl2t5JoFbNua9sY3gDGTCZ-CYuKygOPdR1Ptd6pQGdBbUuD3A43tnUu3Ex36jjsk3KONvus0LbkP2kvrdft4JUgYxneX44rDJNRdcXitpdaj1gzqLItptUnKgx6jd2GXUCk-goOFPSLoWD6ev2nwTdCEVIwt5AfaxkNfmuBAFoVKUvIhPxC7Q/s16000/4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiza0DEIQl2t5JoFbNua9sY3gDGTCZ-CYuKygOPdR1Ptd6pQGdBbUuD3A43tnUu3Ex36jjsk3KONvus0LbkP2kvrdft4JUgYxneX44rDJNRdcXitpdaj1gzqLItptUnKgx6jd2GXUCk-goOFPSLoWD6ev2nwTdCEVIwt5AfaxkNfmuBAFoVKUvIhPxC7Q/s761/4.png)

Now one of these sessions will correspond to the previously “deleted” files

This is sadge days T\_T, because the actual content of the “cleared” session will be deleted other than evidence that the history was cleared. The only data you can go off from this is:

* Session cleared date you pull from the session Webkit/Chrome epoch name

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjF-dTdGljiPlZ5WQ7QnxSc8-f-ijW6_EI5Jz_KzWtM9im3gurWd88YtBBkG_Kojgd5-_mbfbDuI9iFNs-hwy-TdReDMV5Svi947q_Ir3BvqGETVITCVnCAnuW5yu9ekndR4kq0amadaFp_HX0ucO0rMniErMNVORYDTt_HHbM1Wpu6Ws2iAGuw_DnsVw/s16000/5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjF-dTdGljiPlZ5WQ7QnxSc8-f-ijW6_EI5Jz_KzWtM9im3gurWd88YtBBkG_Kojgd5-_mbfbDuI9iFNs-hwy-TdReDMV5Svi947q_Ir3BvqGETVITCVnCAnuW5yu9ekndR4kq0amadaFp_HX0ucO0rMniErMNVORYDTt_HHbM1Wpu6Ws2iAGuw_DnsVw/s818/5.png)

You have some other options like considering pulling from Volume Shadow Copies or looking at Chrome crash dumps (if any). But the data itself appears to be nulled in these files.

**Scenario 3: A user clears their history and re-opened several sessions since**

This is GG for us forensically. Previously, the Favicons file would store potentially “cleared” websites a user visited. But I found this to be very inconsistent and not in line with the results I got during my testing:

* C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Favicons

The only location I found consistently referencing “deleted” search terms was inside this file:

* C:\Users\<name>\AppData\Local\Google\Chrome\User Data\Default optimization\_guide\_prediction\_model\_downloads/b0b608bd-983f-4cf9-aee4-99fc96c39371/global-entities\_metadata

It appears that when you “search” certain terms, Google tries to optimise your searches and stores some of this data inside here. Unfortunately, it also stores a whole lot of other nonsensical uninteresting things, so I’m not sure this is a good forensic artefact.

goodbye & thank u for your time! <3

[browser forensics](https://www.inversecos.com/search/label/browser%20forensics)
[chrome cleared files](https://www.inversecos.com/search/label/chrome%20cleared%20files)
[chrome forensics](https://www.inverseco...