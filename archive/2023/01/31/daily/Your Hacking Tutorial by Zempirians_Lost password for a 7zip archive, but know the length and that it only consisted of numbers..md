---
title: Lost password for a 7zip archive, but know the length and that it only consisted of numbers.
url: https://www.reddit.com/r/HowToHack/comments/10ord7s/lost_password_for_a_7zip_archive_but_know_the/
source: Your Hacking Tutorial by Zempirians
date: 2023-01-31
fetch_date: 2025-10-04T05:16:35.140244
---

# Lost password for a 7zip archive, but know the length and that it only consisted of numbers.

[跳到主要内容](#main-content)

打开菜单
打开导航

前往 Reddit 主页

r/HowToHack
A chip

A close button

[登录](https://www.reddit.com/login/)登录 Reddit

展开用户菜单
打开设置菜单

[![r/HowToHack 图标](https://styles.redditmedia.com/t5_2uxyh/styles/communityIcon_sjak3ovn3qtc1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=60deb89b51148be32456b72f023ef962333cb264)

转到“HowToHack”](/r/HowToHack/)

[r/HowToHack](/r/HowToHack/)

![subreddit 的横幅](https://styles.redditmedia.com/t5_2uxyh/styles/bannerBackgroundImage_u92cjw2h2qtc1.png)

![r/HowToHack 图标](https://styles.redditmedia.com/t5_2uxyh/styles/communityIcon_sjak3ovn3qtc1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=60deb89b51148be32456b72f023ef962333cb264)

[r/HowToHack](/r/HowToHack/)

Welcome! This is your open hacker community designed to help you on the journey from neophyte to veteran in the world of underground skillsets. Ask, Answer, Learn.
Visit us on discord
https://discord.gg/ep2uKUG

---

成员数

在线人数

•

[deleted]

# Lost password for a 7zip archive, but know the length and that it only consisted of numbers.

So I lost my password to a 7zip archive, this happened because I lost my phone and I happened to make the password my phone's IMEI number. I have no record of what the IMEI was written or saved anywhere, so I don't know exactly what it is.

However, IMEI numbers are 15 digits long and the phone was a Tracfone Moto e6 which has the model XT2005DL. Knowing these things I can narrow down what the password was, for example the first few digits, first two being 35 and maybe I can find the next few also since the first 8 digits are the same for each model of phone from what I've read. I'm trying to find a way to brute force the rest of it.

I use linux on my laptop so I've been looking for programs that do this, and found one called John the ripper. I used the 7z2john script to extract the password hash from the 7zip archive, but don't know where to go from there.

Last night I ran "john --format=7z HashOfArchive.hash" and left it to see what would happen, and it looks like it first runs through a wordlist and then goes to ASCII mode which I assume is just going through ascii character combinations trying to bruteforce the hash.

Is it a reasonable solution to make my own wordlist? For example, if I know the password is 15 digits long and looks something like "35123456xxxxxxx", can I just make a wordlist file that looks like "351234560000001, 351234560000002, etc..."? That way it isn't bruteforcing using all ascii characters, just numbers, and only the set of number I need.

I appreciate any answers, and while it does suck to lose a lot of files hopefully even if I can't get them back I can at least learn something trying, lol.

阅读更多内容

 共享

是 Reddit 新用户？

创建账户，畅游精彩的社区世界。

通过电子邮件地址继续

通过手机号继续

继续操作即表示您同意我们的
[用户协议](https://www.redditinc.com/policies/user-agreement)
并确认您已了解
[隐私政策](https://www.redditinc.com/policies/privacy-policy).

公共

任何人均可在此社区中浏览内容、发帖和评论

0
0

## 热门帖子

---

* [Reddit

  reReddit：2023年1月30日的热门帖子

  ---](https://www.reddit.com/posts/2023/january-30-1/global/)
* [Reddit

  reReddit：2023年1月的热门帖子

  ---](https://www.reddit.com/posts/2023/january/global/)
* [Reddit

  reReddit：2023年的热门帖子

  ---](https://www.reddit.com/posts/2023/global/)

[Reddit 规则](https://www.redditinc.com/policies/content-policy)

[隐私政策](https://www.reddit.com/policies/privacy-policy)

[用户协议](https://www.redditinc.com/policies/user-agreement)

[辅助功能](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)
[Reddit, Inc. © 2025。保留所有权利。](https://redditinc.com)

展开“导航”

折叠“导航”

![](https://id.rlcdn.com/472486.gif)