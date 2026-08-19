---
title: Tracking Timezone Changes in Digital Wellbeing
url: https://www.stark4n6.com/2026/08/tracking-timezone-changes-in-digital.html
source: Instapaper: Unread
date: 2026-08-18
fetch_date: 2026-08-19T03:00:34.219821
---

# Tracking Timezone Changes in Digital Wellbeing

[Skip to main content](#main)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKbEuDpbWt2h4R7y02WrWiCmAG90SxVmMkXsEXZE0k3gAACuFYgfUVuTHkKpfowS3WWbkh6XGjqMXh77QkxuZv0osjeusHJnR_ehrMU9r8RaAa3a2R61zmMgl3wLsGpQxSh7rCRX4oQEM/s1600/1947245.png)

Search

### Search This Blog

### Tracking Timezone Changes in Digital Wellbeing

Posted by

[Kevin Pagano](https://www.blogger.com/profile/13417965550116928863 "author profile")

[August 17, 2026](https://www.stark4n6.com/2026/08/tracking-timezone-changes-in-digital.html "permanent link")

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhhAojAlL9NSaYRhQ4uz0wVvQUTHdHRcPapDLlHrCg9qJUUZ-XuWRckUUgBC6oUR3nTmyq8-rba2O8Mu5yZ8B1EOqccMelw-SR6E3apvsiF0jO8vtNcHkmhg-6KcpJcFHxqWl8pQFq7fLoPTWyWW35hf1hdiDhpLpqiqw_P9YRpm5cc_0EPECaPnEX0Nbs=w640-h350)](https://blogger.googleusercontent.com/img/a/AVvXsEhhAojAlL9NSaYRhQ4uz0wVvQUTHdHRcPapDLlHrCg9qJUUZ-XuWRckUUgBC6oUR3nTmyq8-rba2O8Mu5yZ8B1EOqccMelw-SR6E3apvsiF0jO8vtNcHkmhg-6KcpJcFHxqWl8pQFq7fLoPTWyWW35hf1hdiDhpLpqiqw_P9YRpm5cc_0EPECaPnEX0Nbs)

In working through some sample evidence during training I came across that Digital Wellbeing, specifically Samsung's iteration of it, tracks when a device's timezone changes. I didn't see this anywhere in Josh Hickman's [excellent blog](https://thebinaryhick.blog/2025/08/06/not-strange-bedfellows-samsungs-rubin-digital-wellbeing/) but I know it's been part of questions in previous CTF challenges.

The database in question can be found at path:

/data/data/com.samsung.android.forest/databases/dwbCommon.db\*

The table in question is the **Logging** table. There is more to unwrap here (maybe for a future blog) but today's focus is specifically on the timezone changes. If we filter the "key" column we can see some entries that show previous and new timezones as well as the timestamp when these events occurred.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/a/AVvXsEjVBsQoBuHa01YH1aYYOCV6gVCThUceZF-nOQGYR467g-2ROhnYi6QRU6t8ljOauD5Mdco5pvZf7v_vBXRLNJLWKAI-0XHDCnaefdzGmLN6TXyJdc4H8YW0ES3PbRht5wNy6zRzf3mpu928LclLVuRh14Ag_3j4NqBrJjsD8ZxAasxL8upd8y-39yO4n5E=s1600)](https://blogger.googleusercontent.com/img/a/AVvXsEjVBsQoBuHa01YH1aYYOCV6gVCThUceZF-nOQGYR467g-2ROhnYi6QRU6t8ljOauD5Mdco5pvZf7v_vBXRLNJLWKAI-0XHDCnaefdzGmLN6TXyJdc4H8YW0ES3PbRht5wNy6zRzf3mpu928LclLVuRh14Ag_3j4NqBrJjsD8ZxAasxL8upd8y-39yO4n5E) |
| ***Figure 1: Logging table filtered on timezone***   A simple query to filter and reorganize things, and a few lines with Python turns this into a nice little output from ALEAPP.    |  | | --- | | [![](https://blogger.googleusercontent.com/img/a/AVvXsEgFY1WfUa7z7DMp-TKli3Gc10vE-UbAVobPZIBaoZxjsuiZUJhuZ7AocbUcGlWQMKB8DUtOOJXf0yUws7YvnJRY7lVPk82DopucwoK7Tew-T2UZLoBkmEHKWMJfOfVXKGRTIn_YgofxKxpduZE8mlua8HJOlnlMBmzSG5ZnNAxPXG5790Fk8xLrerLJo6E=s1600)](https://blogger.googleusercontent.com/img/a/AVvXsEgFY1WfUa7z7DMp-TKli3Gc10vE-UbAVobPZIBaoZxjsuiZUJhuZ7AocbUcGlWQMKB8DUtOOJXf0yUws7YvnJRY7lVPk82DopucwoK7Tew-T2UZLoBkmEHKWMJfOfVXKGRTIn_YgofxKxpduZE8mlua8HJOlnlMBmzSG5ZnNAxPXG5790Fk8xLrerLJo6E) | | ***Figure 2: Digital Wellbeing timezone changes in LAVA report*** |  This is just yet another pattern of life/usage that could be useful in your investigations. It is now in the current ALEAPP code and bundle version as of v2026.3.0. |

Download 🔗: <https://github.com/abrignoni/ALEAPP>

[Digital Wellbeing](https://www.stark4n6.com/search/label/Digital%20Wellbeing)
[Samsung](https://www.stark4n6.com/search/label/Samsung)
[timezone](https://www.stark4n6.com/search/label/timezone)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_rv98XOSpQWTx_-D_OwQHINXes6_8Q4J2QRmauiB7JMXfh6dp50JzZY1zhNlD0O0yYr01eKAj2jcAFv1S06jcx2ifxvmj1Pm18gESACkCmMdSldHhX_EO_prxaQJoeQ6FuCjeXLNkb0g/s150/FullColor_1024x1024_300dpi.jpg)

### Archive

* [August 20263](https://www.stark4n6.com/2026/08/)
* [July 20263](https://www.stark4n6.com/2026/07/)
* [June 20264](https://www.stark4n6.com/2026/06/)
* [April 20261](https://www.stark4n6.com/2026/04/)
* [March 20262](https://www.stark4n6.com/2026/03/)
* [February 20261](https://www.stark4n6.com/2026/02/)
* [December 20251](https://www.stark4n6.com/2025/12/)
* [November 20252](https://www.stark4n6.com/2025/11/)
* [October 20253](https://www.stark4n6.com/2025/10/)
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
* [November 20222](https://www.stark4n6.com/2022/11/)
* [October 20221](https://www.stark4n6.com/2022/10/)
* [September 20222](https://www.stark4n6.com/2022/09/)
* [August 20223](https://www.stark4n6.com/2022/08/)
* [June 20228](https://www.stark4n6.com/2022/06/)
* [May 20224](https://www.stark4n6.com/2022/05/)
* [April 20224](https://www.stark4n6.com/2022/04/)
* [March 20223](https://www.stark4n6.com/2022/03/)
* [February 20221](https://www.stark4n6.com/2022/02/)
* [January 20225](https://www.stark4n6.com/2022/01/)
* [December 20212](https://www.stark4n6.com/2021/12/)
* [November 20211](https://www.stark4n6.com/2021/11/)
* [October 20217](https://www.stark4n6.com/2021/10/)
* [September 20211](https://www.stark4n6.com/2021/09/)
* [August 20214](https://www.stark4n6.com/2021/08/)
* [July 20211](https://www.stark4n6.com/2021/07/)
* [June 20214](https://www.stark4n6.com/2021/06/)
* [May 20215](https://www.stark4n6.com/2021/05/)
* [April 20214](https://www.stark4n6.com/2021/04/)
* [March 20212](https://www.stark4n6.com/2021/03/)
* [February 20211](https://www.stark4n6.com/2021/02/)
* [January 20213](https://www.stark4n6.com/2021/01/)
* [December 20207](https://www.stark4n6.com/2020/12/)
* [November 20206](https://www.stark4n6.com/2020/11/)
* [October 20203](https://www.stark4n6.com/2020/10/)
* [August 20201](https://www.stark4n6.com/2020/08/)
* [June 20205](https://www.stark4n6.com/2020/06/)
* [March 20201](https://www.stark4n6.com/2020/03/)
* [October 20191](https://www.stark4n6.com/2019/10/)
* [May 20191](https://www.stark4n6.com/2019/05/)
* [April 20195](https://www.stark4n6.com/2019/04/)
* [March 20191](https://www.stark4n6.com/2019/03/)
* [February 20194](https://www.stark4n6.com/2019/02/)
* [January 20193](https://www.stark4n6.com/2019/01/)
* [December 20181](https://www.stark4n6.com/2018/12/)
* [November 20183](https://www.stark4n6.com/2018/11/)
* [September 20181](https://www.stark4n6.com/2018/09/)

Show more
Show less

### Popular Posts

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjINtsVXaT2atijYhXs4-3P8g2XTSZAZFty3t4jlBcga1kbpFhoAP-rnKX7q6yXkJFBIaKrzaZC5N-HqplXANJxBdFWZcyV3D0mI-GX07NtU3e1fHdTvDDV0VuStwi_nJMEApWOttGpeQAK...