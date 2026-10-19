---
title: 低分飘过 CISP-PTE：7 道实操题，和考后才明白的几件事
url: https://mp.weixin.qq.com/s/3a2lcVkhxd_niaQinLgprQ
source: Doonsec's feed
date: 2026-10-18
fetch_date: 2026-10-19T07:07:09.125828
---

# 低分飘过 CISP-PTE：7 道实操题，和考后才明白的几件事

# 低分飘过 CISP-PTE：7 道实操题，和考后才明白的几件事

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前言

　　2022 年，我还在读大二。那一年，我用攒下的生活费和奖学金报了 CISP-PTE，前后花了近一万块——对当时的我来说，不是小数目。现在回头看，那是我第一次为自己的职业方向花钱，也是我入行安全后拿的第一个证书。

　　从大一开始学渗透，前前后后快一年，我原以为基础还算扎实，结果考场上还是被新题型打了个措手不及。6 个 key 加 17 分，低分飘过。分数不算好看，但走出考场那一刻，心里还是挺复杂的：有侥幸，也有不甘，更多的是终于把一件事做完的踏实。

　　这篇文章最早写于考完之后，这次重新整理了一遍：先聊聊这场考试给我的几点感悟，以及这几年在安全方向上的新打算；后面是我整理的 7 道实操题讲解——SQL 注入、文件上传、文件包含、命令执行、日志分析，以及两道代码审计，希望能帮到正在备考的你。

　　文章有点长，建议先收藏，慢慢看。

## 一、CISP-PTE考试感悟

**先说 CISP-PTE 是什么。**

　　CISP-PTE，全称“注册信息安全专业人员—渗透测试工程师”，由中国信息安全测评中心推出。它和纯理论认证不太一样，考试重点在实操：给你一个模拟环境，让你自己去挖漏洞、拿 key。也正因为贴近实际工作，很多人把它当作安全入行的“第一张证书”，在安全服务、渗透测试岗位的招聘里也经常被提到。说“必考”可能有点绝对，但如果你想在国内做渗透测试，这张证书确实是很值得优先考虑的一块敲门砖。

**再说考试本身。**

　　从难度上看，选择题比较简单，但基础题里的 SQL 注入比较难。题目是一个登录系统，弱口令、万能密码都试了，还是进不去；答案的 key 就在根目录下，用 sqlmap 读文件也读不出来，只好放弃。剩下的 4 道都做了，难度不大。

　　综合题是真的难，考的是 Linux 环境下的内容。考前预测可能是 Win2008 或 Linux 环境，刚好那天分批考：上午考 Linux，下午考 Win2008。轮到我做的时候非常痛苦，硬着头皮拿到前两个 key 就撤了。

　　第一个 key 是连上数据库、改掉网站后台密码后登录拿到的；第二个是通过文件包含和伪协议 Base64 编码读出来的；第三个 key 需要用蚁剑连上去，在 key 目录下提权才能拿到，最后蚁剑怎么都传不上去，只能放弃。所以只拿到两个 key 就交卷了，选择题拿了 17 分。最后 6 个 key 加 17 分，低分飘过，实属不易。

**考完之后，我想明白了几件事。**

　　考完之后，我最大的感受是：兴趣是最好的老师，但真正拉开差距的，是坚持和耐心。这个道理不分行业。不管大家以后做哪一行，都应该每天把学到的东西复盘一遍，转化成自己的能力，养成及时做笔记、做总结的习惯。很多时候，人与人的差距不在能力本身，而在于是否愿意多角度思考、把一件事做透。认准一个方向持续深耕，每个人都能成为别人眼里的专家。

　　说到做笔记，顺便推荐一下我平时用的工具——语雀。它的目录是树形的，像一本书，想看哪一部分直接点，不用一层层翻，找东西很快。它还能接 MCP，用 AI 帮忙整理和优化笔记，挺省事的。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grRY7Cy0megwYkPbe58FGdqTU5VibXTY2bpCko1YTEtmY14XWxagHA2eMkicJ1lPMGycPv7QTn9r7uyYmxppeUFj6JxicO8dBrMicc/640?wx_fmt=png&from=appmsg)

**接下来，我想往哪里走。**

　　接下来，我会开始准备软考信息安全方向的复习。等工作稳定下来、手头宽裕一些，也会继续考一些信息安全相关的证书。听做逆向的朋友说，逆向方向的工作前景不错，但要先学好汇编。以后有时间，我会认真补一补逆向的知识，多一门技术，也就多一条出路。

　　另一个方向是 Web 安全和安全服务，路子很宽。以后可以去做甲方安全工程师、乙方安全服务工程师，甚至往安全管理方向转型。相关领域包括 Web 安全、AI 安全、小程序与 App 安全、内网渗透、云安全、二进制安全、IoT 安全、无线安全、代码审计、漏洞挖掘、逆向工程、免杀与红蓝攻防、应急响应，以及等保测评、安全评估和甲方安全建设等。

　　说回我自己，接下来最想深耕的是安全建设、Web 安全、AI 安全和安全运营；安全管理是更往后的事，等这几块做扎实了再考虑。方向不用一下子铺得太开，先把手上的工作做好，再一步一步来。

　　建议大家趁大学和毕业后的五年内，抓紧学习、补齐短板，提前规划好自己的职业方向。同时想清楚：你的竞争力在哪里？别人是否愿意为你的能力买单？只有不断提升实力，培养一项不可替代的能力，才能在自己所在的行业真正站稳脚跟。

　　考试的情况就先聊到这里。下面，我把之前在实操练习中做过的套题重新讲解一遍，知识点会更全面，希望对备考的同学有帮助。

## 二、CISP-PTE实操练习题讲解

### 1. SQL注入

#### （1）第一种解法

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grFm7zhtOk4Rkib6TbUOIUnalneHLCcBVb0CCT83kwYYcF0BEicsjUNPLtG1D0haJ0wIgLTFNtk9xG580HtxLBt2QmQ9IicbdDSfE/640?wx_fmt=png&from=appmsg)

　　我们进入答题，通过提示，答案就在这个/tmp/360/key路径下。

```
http://192.168.230.131:81/vulnerabilities/fu1.php?id=1
```

　　标题提示了注入点，id 参数存在括号注入，所以注入的时候要记得加括号。

```
select * from article where id= (‘1’)
```

　　我们在后面加上 ')，发现报错。

```
http://192.168.230.131:81/vulnerabilities/fu1.php?id=1’)
```

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grgicuccl5fGVWO6r3icF3K5FMo3yCwhMpRibYZy0gs3dnkLxp4bqS8Bv3W1kZqNp4LX5frYUG6w0CN8iadMzMEhFuxHicufxR28erc/640?wx_fmt=png&from=appmsg)

　　没有回显，再加上单引号，出现了回显

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqya7UjNu9ESmcdO47pGRnMqUQ9X41g2C8j5mV8bfB3SnFKd4aYjvibx03NTXsW4FsrhVsUbyIAns26jV9erpCO03Az33rDAQ7c/640?wx_fmt=png&from=appmsg)

　　说明存在 SQL 注入。再看看是否存在过滤，判断字段个数时，注入以下语句http://192.168.230.131:81/vulnerabilities/fu1.php?id=1’) order by 4--

　　回显出这个语句，说明空格被过滤了select \* from article where id= (‘1’)orderby4--‘)

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grLhHY9NdZCsWKESlMnUTyk05S6UpkLeUPQpFGUYPzIsuOVhMhz0CrMhWXo2HBVZ7FjoN7l7cPbuGN10dLXgz8yAmr8kSDKeB4/640?wx_fmt=png&from=appmsg)

　　我们用注释符绕过空格，把后面的（-- ）换成 # 试试。

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqdEm1CYZoVJWTaqBiaDH1pnje1Tr8FZJePKj3GgVhWM0XOdoxO0KwR87BQRulUe0wkRrJaRyYQetib5k2yoQ7m62kg55qtmxkWc/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gocmPg0pXNeOyeDDG004o7k4CPPj1wN9V29iatGb1BZLxSa4FAooDbLQ24y96ZicWtmxtJJI0Kz9DQI9TrVX7zZKw64Lsxa9JnD4/640?wx_fmt=png&from=appmsg)

　　没有回显，说明 # 也被过滤了，再改成 Base64 编码绕过试试。

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqK732VUPmzY9O6oQHVGDgh007sSe7F5Aq9FeC9ibIYfic7IK8O1bLIWOvF9V8Nuulvckay76Yd0ChjekVg3Qa01VH8wOHia6uIZc/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gpeq1MyBudjkQcWicVlDhicrm5p79icC0iaGwvAAwkIib4SFgMwdVCPvs423y4kJcIZwb80XfQFE1vVNMvY3ibxjy98HAqsAic1KJo2KU/640?wx_fmt=png&from=appmsg)

　　发现报错，可能字段数不对，改成 4 试试

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1goamby8yvtnJCykwLW8k8U54t43CbmDvPZbDzA3UQJSeXhHXRszrk2rN4IdYDL5GWKFFWxYTUHcqfIdm0ribTKrf93wbFq1p6IY/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gp2MMrwfCuf90VHicucMGXTK94azUgpEVrRRCdgiawdpmj56FPscibAwO4PsQPZVJzEdIYlFFDnKlAVUeWOrdaM9FqC2lGNpibib2C0/640?wx_fmt=png&from=appmsg)

　　出现回显，说明存在 4 个字段，绕过后用联合查询看看数据

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gq9kAmQHvL6N9mYsOONbHbxEsxFUKlibLsBkdbWepP6IpjFI7rz8CSzS6qrXibk1KrKnNh7X4sTbYjWAZsTB6mYNVauYkCue2QiaU/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqfuaMQO4SneicEhia6z0g6nqo45VdqIoHpyekRicBOEMOzopDo1EeqGdvAw0Xq0iapVCvbYAhrSCXOACiaQoPTryRQLs2XhDjnwSxk/640?wx_fmt=png&from=appmsg)

　　报错且没有显示 union 字段，说明 union 被过滤了，试试双写绕过

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gotYL9zg5tYgS1WgOtzQdYNYKSJZIt6jjfrw88LdJRjpn1iaR1608IdIg6ibUtbaKrcx4PY4Umr9MnF2ktRu5Eng6hWpyp51SEAw/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goybBSxiaiapOv3ETaKjfvft1H3n9bbYicGXpF6Qbg19ELL9A6ml9yrbvhYogmpKpsB7CVEwVUcxJKB8PRseN8BDibl2Ps1keV7nibs/640?wx_fmt=png&from=appmsg)

　　回显成功，绕过成功。把 id=1 改成 id=-1 制造报错，看看回显

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1graltdbQs5iaibORCliaPELFtNIUca2aKhEsmfbOHqT5z2PSxyIPeJibkdKoSDZq17toT2LNaTXkGwVWIVD14HrISSz0G8TcdMYjC8/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grEOxI1CD517vVbKzd5CenLI75uPFXVbjJf7Q7Iq8cLpIz0zpNVnHbQhyeVhyzO6xneCGSbhhIkw8icyHhleGk54WnuUbnqrdc8/640?wx_fmt=png&from=appmsg)

　　2、3、4 是回显位置，我们用第 2 个位置注入，这里用到读文件函数 load\_file('/tmp/360/key')

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqN3klPzSopqNIAjhnNG0xBVp8cBTXQFibRSuaM0unt9HMCUSVYkRgujanwvMHGoyGRapicWHlJibIXX2xpZ5Jre53KbHp9ibGfPOU/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grKd7vhyuegDsmnCicZR6woPmZfhicuY9oR9ib3N7GibnVyKicoY5TibN2Lj1SaicAq94ia5RBia2BN8JibMvO8tLs3bjeKq19h9M5CpQKU8/640?wx_fmt=png&from=appmsg)

　　回显成功，拿到 key：8b3h4a7v。这道题主要过滤了空格、注释符 # 和 union 关键字。

#### （2）第二种解法

　　这题也可以用 sqlmap 解，直接调用 --file-read 和 tamper 脚本读文件就行。

　　打开 sqlmap，输入以下命令执行

```
python sqlmap.py -u"http://192.168.230.131:81/vulnerabilities/fu1.php?id=1"--file-read=/tmp/360/key --tamper"space2hash.py"--level3--batch
```

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpElkBuHhPRPau2B9Y6t1GgISDKibibJB6TkvpV3bxE7ZT0nVPejWQBRgQ5jPC5AZKlicXWj6R1icsbR1R82Z7cQxK1qRU6iavSTug0/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gonKvhDO1JIBlvWjY4xxLnAWjFqHrv6JvX1GrWDo3L7ZLoptYax5ibRYQbNC3JSctSEPGfQXpW87zIf942EzNo2IT6BMoEJ9dW0/640?wx_fmt=png&from=appmsg)

　　读到的 key 文件就在图中黄色路径里，找到当前文件的路径查看即可C:\Users\CISP-PTE\AppData\Local\sqlmap\output\192.168.230.131\files

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqoSWg9x2xPBQlibQNHsDVcvxabDjJyOwZf8ia6M6QMN1fpY8jb0sXM8SNQd4mWzNUITB0QibzSFLEF6Z27QsQoMIPtbfL9oJGR6Q/640?wx_fmt=png&from=appmsg)

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grE9jtmokOqLqsZrbgxjHwW3MEyyzbm5RM9rY6WGMYYqU9gKF41jLRg47I90PAO6enjeFuXgYqLIiaRxI5UeoSRf3uCYCeA1ibUk/640?wx_fmt=png&from=appmsg)

　　这样就拿到 key 了。

### 2. 文件上传

（1）http://192.168.230.131:82/vulnerabilities/fu1.php

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1goQBsVVvAoGmY6kNz0ktQ90R7HdMzDID6N5F5cHbdwneSEIbNe9D5Jy29yRG0Eia7W7LqQGJtG79bNOITRrVPfIibDuIianVzo6ib8/640?wx_fmt=png&from=appmsg)

　　我们进入答题

![截图](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqLz2zbIS9S1Zjxaf8LJBAIjSztgqK8MdXDA8106QvhXpr1nHXGIKIB9yAm4mKDZJMLGA3kCEsgVuy65ZxFibrVdR3OFOLVORBo/640?wx_fmt=png&from=appmsg)

　　我们在桌面新建一个包含读文件代码的图片，进行上传：

```
GIF89a

<?php echo file_get_contents('../key.php');?>
```

![截图](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grOg4faATjiadh8YVFwjwnyjjp9wxpEszSa3dO6nDoov7rCFg2GnwLHFRUPUWl4c6ywmpkibGNvvPvzxzdx0VpW3IL5zglvEOmHQ/640?wx_fmt=p...