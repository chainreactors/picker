---
title: Pandas Errors: What encoding are my logs in&#x3f;, (Fri, Aug 23rd)
url: https://isc.sans.edu/diary/rss/31200
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-24
fetch_date: 2025-10-06T18:06:33.507513
---

# Pandas Errors: What encoding are my logs in&#x3f;, (Fri, Aug 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31196)
* [next](/diary/31204)

# [Pandas Errors: What encoding are my logs in?](/forums/diary/Pandas%2BErrors%2BWhat%2Bencoding%2Bare%2Bmy%2Blogs%2Bin/31200/)

**Published**: 2024-08-23. **Last Updated**: 2024-08-23 12:26:15 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Pandas%2BErrors%2BWhat%2Bencoding%2Bare%2Bmy%2Blogs%2Bin/31200/#comments)

While trying to process some of my honeypot data, I ran into the following error in my Python script:

**"Exception has occurred: ValueError**
values should be unique if codes is not None"

I received the error while tring to merge two Pandas DataFrames [1]:

```

cowrie_data = cowrie_data.merge(df, on=["dates", "src_ip", "input", "outfile", "username", "password"], how="outer")
```

When looking for solutions, I found very little information outside some documentation [2]. The data being joined was data from two different honeypots. It included Cowrie [3] data from 6 different JSON keys:

* dates (converted to "%Y-%m-%d" format from the "timestamp" key)
* src\_ip (source IP address)
* input (commands submitted to Cowrie in SSH/telnet session)
* outfile (storage file paths for files uploaded/downloaded to the honeypot, usually malware)
* username (username submitted to Cowrie during SSH or telnet session authentication attempt)
* password (password submitted to Cowrie during SSH or telnet session authentication attempt)

I didn't know what data may be causing the issue, so I decided to tweak my "pd.merge" statement to merge the DataFrames, starting with only one row and expanding the dataset a row at a time until an error occured.

```

row_number = 0
while row_number < len(cowrie1) and row_number < len(cowrie2):
    try:
        data = cowrie1[0: row_number + 1].merge(cowrie2[0: row_number + 1], on=["dates", "src_ip", "input", "outfile", "username", "password"], how="outer")
    except:
        print(row_number)
        print("row: ", cowrie1[0: row_number + 1])
        print("row: ", cowrie2[0: row_number + 1])
        break
    row_number += 1
```

**![](https://isc.sans.edu/diaryimages/images/2024-08-23_figure1_v3.PNG)
Figure 1: Contents of DataFrames attempted to be merged at the time an exception occurred.**

An error eventually occurred, but the data didn't look unusual. However, when looking at the specific data field, I saw something unexpected.

**![](https://isc.sans.edu/diaryimages/images/2024-08-23_figure2_v2.PNG)
Figure 2: Samples of data that caused the exception.**

**![](https://isc.sans.edu/diaryimages/images/2024-08-23_figure3_v4.PNG)
Figure 3: Samples of data that caused the exception from a different experiment.**

How did the null bytes "**\x00**" get into the dataset? What did this look like in the original Cowrie JSON logs? This error was surprising since the scripts were used to proces about a month of data from half a dozen different honeypots. This error had never occured from that dataset, but presented when expanding the timeframe from a one month to a four month period. This script also exported the data to a SQLite file before joining the two DaraFrames. I was unable to find the data in the SQLite when searching for the null bytes. I was also unable to find the data when looking at the JSON logs. I used the raw timestamp, as seen in Figure 3, to help find the specific log data that generated the error.

Once I had the exact timestamp, I was able to find the log:

**![](https://isc.sans.edu/diaryimages/images/2024-08-23_figure4.PNG)
Figure 4: Raw Cowrie logs that eventually generated the python error**

I now had my culprit and determined why I was never able to find the exact same string within the logs. Tthe same data in the SQLite database looked very different as well.

**![](https://isc.sans.edu/diaryimages/images/2024-08-23_figure5.PNG)
Figure 5: BLOB data shown in SQLite database**

To resolve the error, I removed the null bytes using "replace".

```

log_data[each_key] = yielded_json[each_key].replace('\x00','') # added .replace('\x00','') on 8/17/24 to replace null bytes for pandas merge issues
```

**![](https://isc.sans.edu/diaryimages/images/2024-08-23_figure6(1).PNG)
Figure 6: Data represented in SQLite database without null values.**

Some takeaways:

* Data changes. The error may not occur today, but may in the future
* Use more logging
* Use more exception handling
* Test with a variety of data

I also hope that unlike my earlier attempts to troubleshoot, someone finds this article in their own Google search when they run into the same error.

[1] <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>
[2] <https://pydocs.github.io/p/pandas/1.4.2/api/pandas.core.algorithms.safe_sort.html>
[3] <https://github.com/cowrie/cowrie>

--
Jesse La Grew
Handler

Keywords: [dataframe](/tag.html?tag=dataframe) [pandas](/tag.html?tag=pandas) [python](/tag.html?tag=python) [unicode](/tag.html?tag=unicode)

[0 comment(s)](/diary/Pandas%2BErrors%2BWhat%2Bencoding%2Bare%2Bmy%2Blogs%2Bin/31200/#comments)

* [previous](/diary/31196)
* [next](/diary/31204)

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