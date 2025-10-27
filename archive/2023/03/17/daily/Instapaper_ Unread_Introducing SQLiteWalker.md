---
title: Introducing SQLiteWalker
url: https://www.stark4n6.com/2023/03/introducing-sqlitewalker.html
source: Instapaper: Unread
date: 2023-03-17
fetch_date: 2025-10-04T09:53:54.069242
---

# Introducing SQLiteWalker

[Skip to main content](#main)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKbEuDpbWt2h4R7y02WrWiCmAG90SxVmMkXsEXZE0k3gAACuFYgfUVuTHkKpfowS3WWbkh6XGjqMXh77QkxuZv0osjeusHJnR_ehrMU9r8RaAa3a2R61zmMgl3wLsGpQxSh7rCRX4oQEM/s1600/1947245.png)

Search

### Search This Blog

### Introducing SQLiteWalker

Posted by

[Kevin Pagano](https://www.blogger.com/profile/13417965550116928863 "author profile")

[March 15, 2023](https://www.stark4n6.com/2023/03/introducing-sqlitewalker.html "permanent link")

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtqoq707bT7xa7wC-R8cJpyhVTPXnN4YgLaKuAsFvKKpnRqCqAyV9IOHJGazjxN0gpN9dqCdAGWxTH32i4hy5Cesdm0p3AAkDuzqQ7Cg2iAc0_lvt4U0BlaZH5oV84Yuyo-QIqiMpCc8uwls6WH_GMCE5OUNSiNA9kWGl0NOC2H-uWCujVXdvRJGja/w640-h270/SQLiteWalker.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtqoq707bT7xa7wC-R8cJpyhVTPXnN4YgLaKuAsFvKKpnRqCqAyV9IOHJGazjxN0gpN9dqCdAGWxTH32i4hy5Cesdm0p3AAkDuzqQ7Cg2iAc0_lvt4U0BlaZH5oV84Yuyo-QIqiMpCc8uwls6WH_GMCE5OUNSiNA9kWGl0NOC2H-uWCujVXdvRJGja/s2992/SQLiteWalker.png)

In my continued research of mobile devices, I always wanted to find a way to quickly hunt for files to research. Because mobile devices (both Android and iOS) rely heavily on SQLite databases I figured why not make a script to pull these databases out from the filesystem for further analysis.

The premise behind my script was to spurred on by Eric Zimmerman's [SQLECmd](https://github.com/EricZimmerman/SQLECmd) which has a -hunt switch that allows for finding database files from a folder structure. Using the -verbose option spit out a large log of what was found but it wasn't formatted exactly how I wanted it and it ran slower than I anticipated. And so in a galaxy far far away, SQLiteWalker was born!

Download link: <https://github.com/stark4n6/SQLiteWalker>

Simply put, it looks for magic header details for SQLite databases and extracts the files. Currently, SQLiteWalker can handle folder or .zip input formats. The only other required field is an output path for the exported files and reports. The only optional switch is quiet mode which will not output file paths to the console (it will still write them to the report file).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi9m7zLs10zFd_KOyTmZDPp4mxMxEoHIvTHn7yNR0_pCEI8DxYt8GyCaBF01An4jFe3dS7iLBkAP2lSFK6OkhzcmAold2u-2LIkF8yANZ3kbGnxtL4jFV9prFgmIwGcAbufmM1bayvmtoDt_JpfBerkZZ2qCG2kRJPPhlb2qNxf8TdIUKOzNUmlkA92=w640-h198)](https://blogger.googleusercontent.com/img/a/AVvXsEi9m7zLs10zFd_KOyTmZDPp4mxMxEoHIvTHn7yNR0_pCEI8DxYt8GyCaBF01An4jFe3dS7iLBkAP2lSFK6OkhzcmAold2u-2LIkF8yANZ3kbGnxtL4jFV9prFgmIwGcAbufmM1bayvmtoDt_JpfBerkZZ2qCG2kRJPPhlb2qNxf8TdIUKOzNUmlkA92)

***Figure 1: Command line switch options***

Here is what the script looks like after it finishes. As you can see below you will get final runtimes, count of databases found, as well as error counts (if applicable).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhuv2HzRRIIvgnx4KvpPybL78TIE3ZEU2bT_-JvkjFR3BXHWSHJSKSVbKcUd9wYkozA_gYWrS6hlSX_vR_dclwtoRmZbTSCOL5gaOx4Lv6Lnn-GEZIze508e3KjQKbKVl5ITmdmVBbW7R3g-z5vebEFF2hzMEy3xUY72pYIomR97DKn8kLHTUVhvsnq=w640-h190)](https://blogger.googleusercontent.com/img/a/AVvXsEhuv2HzRRIIvgnx4KvpPybL78TIE3ZEU2bT_-JvkjFR3BXHWSHJSKSVbKcUd9wYkozA_gYWrS6hlSX_vR_dclwtoRmZbTSCOL5gaOx4Lv6Lnn-GEZIze508e3KjQKbKVl5ITmdmVBbW7R3g-z5vebEFF2hzMEy3xUY72pYIomR97DKn8kLHTUVhvsnq)

***Figure 2: Finish line of SQLiteWalker***

At the output path we get a folder named "SQLiteWalker\_Out" appended by the date/time the script was kicked off. Inside the folder we get at least two, but sometimes three items:

1. Exported/Recreated folder structure with original database files
2. File list report containing:

* File name
* File path
* Table structure

3. Error list report (if applicable) containing:

* File name
* File path
* Error

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhuOmEZpMdFbmZ2KiDlIUagMFNCA6RRy6kbgwnnIla78YGla_suLvVFNzvxtzoZOUkW27Bvbhx6RGjZXVsRFjAbhbQSxJtpWofDmUT4EI6e7RcEhb3zEed7nuvLUswh0WpaP-_M6mvXDk2kloBudI1_-_HB36do7axIHhvb69mWTqpiCFGDGr5uAFWE=w400-h261)](https://blogger.googleusercontent.com/img/a/AVvXsEhuOmEZpMdFbmZ2KiDlIUagMFNCA6RRy6kbgwnnIla78YGla_suLvVFNzvxtzoZOUkW27Bvbhx6RGjZXVsRFjAbhbQSxJtpWofDmUT4EI6e7RcEhb3zEed7nuvLUswh0WpaP-_M6mvXDk2kloBudI1_-_HB36do7axIHhvb69mWTqpiCFGDGr5uAFWE)

***Figure 3: Sample output folder***

Here is a look at the db\_list.tsv file in TimelineExplorer:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhzRuTkvxyDFLFJFVcBuJWGvQutTJl9qMW4DP6V0Z1HhlbLqnlBr2XH_1jwyVXA8V2aeG3Sk8VxPSEdQk4L0vJrE1mYAzVjAqmqp74FlIwHTN8MRXZbmSuANVcilLyrS45BLE9Bclhzn6EeqE7qIl0juoOr992c4OrMeUMyMY_3pRMWwxEER6gOOXC8=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhzRuTkvxyDFLFJFVcBuJWGvQutTJl9qMW4DP6V0Z1HhlbLqnlBr2XH_1jwyVXA8V2aeG3Sk8VxPSEdQk4L0vJrE1mYAzVjAqmqp74FlIwHTN8MRXZbmSuANVcilLyrS45BLE9Bclhzn6EeqE7qIl0juoOr992c4OrMeUMyMY_3pRMWwxEER6gOOXC8)

***Figure 4: Sample db\_list.tsv output***

Here is a sample of the error\_list.tsv:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgPT_ktFjb8mG9dtrYczD-7ldisY-IAj5iipYmqA0-U-px88NmtxC6ah5OxnHPRK5K-pGJOH3TphBM_wSCn1wTBC0LSAIG4kPpJhHbzjoDHIduZE1fMzY8yd5yW_LpwluQ0gQu2T1wH5HE78zDZYz4KDI3FkTROh_2tyA0nq_jotoL3dUcFSbzPYvea=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgPT_ktFjb8mG9dtrYczD-7ldisY-IAj5iipYmqA0-U-px88NmtxC6ah5OxnHPRK5K-pGJOH3TphBM_wSCn1wTBC0LSAIG4kPpJhHbzjoDHIduZE1fMzY8yd5yW_LpwluQ0gQu2T1wH5HE78zDZYz4KDI3FkTROh_2tyA0nq_jotoL3dUcFSbzPYvea)

***Figure 5: Sample error\_list.tsv output***

Because I wrote this whole thing in about 2 days time, I'm sure more updates will come in the near future. Some things on my to-do list include .TAR format support as well as working on a GUI.

As always feedback is more than welcomed, feel free to reach out to me on [Twitter](https://twitter.com/KevinPagano3) or [Mastodon](https://infosec.exchange/%40stark4n6) or open an issue on the [Github page](https://github.com/stark4n6/SQLiteWalker) and hopefully I can address it. May the [forensic] force be with you!

[sqlite](https://www.stark4n6.com/search/label/sqlite)
[SQLiteWalker](https://www.stark4n6.com/search/label/SQLiteWalker)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_rv98XOSpQWTx_-D_OwQHINXes6_8Q4J2QRmauiB7JMXfh6dp50JzZY1zhNlD0O0yYr01eKAj2jcAFv1S06jcx2ifxvmj1Pm18gESACkCmMdSldHhX_EO_prxaQJoeQ6FuCjeXLNkb0g/s150/FullColor_1024x1024_300dpi.jpg)

### Archive

* [September 20251](https://www.stark4n6.com/2025/09/)
* [August 20251](https://www.stark4n6.com/2025/08/)
* [July 20254](https://www.stark4n6.com/2025/07/)
* [June 20252](https://www.stark4n6.com/2025/06/)
* [April 20252](https://www.stark4n6.com/2025/04/)
* [March 20259](https://www.stark4n6.com/2025/03/)
* [February 20251](https://www.stark4n6.com/2025/02/)
* [January 20252](https://www.stark4n6.com/2025/01/)
* [December 20242](https://www.stark4n6.com/2024/12/)
* [October 20241](https://www.stark4n6.com/2024/10/)

* [May 20241](https://www.stark4n6.com/2024/05/)
* [April 20242](https://www.stark4n6.com/2024/04/)
* [March 20244](https://www.stark4n6.com/2024/03/)
* [February 20241](https://www.stark4n6.com/2024/02/)
* [January 20243](https://www.stark4n6.com/2024/01/)
* [December 20231](https://www.stark4n6.com/2023/12/)
* [October 20233](https://www.stark4n6.com/2023/10/)
* [September 20232](https://www.stark4n6.com/2023/09/)
* [August 20232](https://www.stark4n6.com/2023/08/)
* [July 20231](https://www.stark4n6.com/2023/07/)
* [June 20232](https://www.stark4n6.com/2023/06/)
* [May 20235](https://www.stark4n6.com/2023/05/)
* [April 20232](https://www.stark4n6.com/2023/04/)
* [March 20236](https://www.stark4n6.com/2023/03/)
* [February 20231](https://www.stark4n6.com/2023/02/)
* [January 20232](https://www.stark4n6.com/2023/01/)
* [December 20223](https://www.stark4n6.com/2022/12/)
* [Nove...