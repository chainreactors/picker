---
title: 一家玩具公司的服务器被捅穿了，而攻击者只用了六步
url: https://mp.weixin.qq.com/s/7b_U4qPzXaMczArQQmEqbQ
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:06:08.421176
---

# 一家玩具公司的服务器被捅穿了，而攻击者只用了六步

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SQGvsuoDbxibXC30JAPflvicwrlibiawmIPibZuFVCdBic6rL69S1mlqJqowPlJxbQuHoAIKiaj9aCibqL6a7vAwWut8smyCKcd6h0YEOZQTOEmATJY/0?wx_fmt=jpeg)

# 一家玩具公司的服务器被捅穿了，而攻击者只用了六步

原创

漫路修行
漫路修行

微痕鉴远

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxicW42R5XBrmbuzJVoafTQguggIkc189CpkEMlhIgMiafpEJqMcvKNruyopOaZClypchYUiaWzfmajU4lNLy7e1a8oy0YCHWyKafY/640?wx_fmt=png&from=appmsg)

想象一下这个场景：你是一家玩具公司的安全运维，某天早上 IT 部门告诉你，电商网站好像「有点不对劲」——数据库里多了一些莫名其妙的记录，网站响应也变得不太正常。你不确定这到底是程序 bug，还是有人摸进来了。

这就是 Slingshot 抛给我们的情景。Slingway Inc. 是一家「行业领先」的玩具公司，他们的电商服务器出现了可疑活动，数据库可能被篡改。作为被临时请来的 SOC 分析师，你的任务是在一个 Elastic Stack 实例里翻日志，把攻击者的每一步操作都还原出来。

最终你会发现，这个攻击者并不特别高明——但他非常系统。从最初的端口扫描到最后的数据库篡改，整个攻击链环环相扣，一共六步，每一步都在利用上一步的成果。而他留下的痕迹，全都被 Elastic Stack 忠实地记录在了日志里。

SOC 分析师的日常工作，说白了就是在海量日志里找「不对劲」的东西。一条正常的用户请求和一次攻击行为，在单条日志层面可能看不出区别——都是 HTTP GET 请求，都返回了 200。真正的差异藏在行为模式里：同一个 IP 在一分钟内发了 2000 个请求，User-Agent 里带着扫描工具的名字，请求的路径全是字典里的常见路径……这些模式需要分析师从整体上把握，而不是逐条翻看。

这篇文章会完整复盘这次攻击的全部六个阶段。如果你是做安全运维的，或者对 SOC 日志分析感兴趣，接下来的内容应该能帮你建立一套「从日志里追踪攻击者」的思路。

## 案件背景与调查环境

##

Slingway Inc. 的 IT 团队报告说，可疑活动始于 2023 年 7 月 26 日。他们提供了一套 Elastic Stack（也就是我们常说的 ELK——Elasticsearch、Logstash、Kibana 三件套）实例，里面包含攻击时间段的 Web 服务器日志。

为什么选 Elastic Stack 做调查工具？因为它在 SOC（安全运营中心）场景下有一个很核心的优势：所有日志集中存储、统一检索。不管你面对的是 Apache 访问日志、认证日志还是应用日志，全部灌进 Elasticsearch 之后，就可以用 Kibana 的 Discover 界面做灵活过滤和时间线回放。对于事件响应来说，这种「上帝视角」是还原攻击链的基础。

登录 Kibana 之后，首先要做的当然是定位攻击者。在日志里按 IP 地址做聚合统计，很快就能发现一个异常来源——10.0.2.15。这个 IP 在短时间内对服务器发起了大量请求，行为模式明显不是正常用户。接下来，我们把所有过滤条件都锁定在这个 IP 上，开始逐步还原他的每一步操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxib2ggeUacK5YjbNKvBTaibjLFict9FibxQg8icfEaMapEj7lFyKmBCbcKicm1hicC5rcxMicCOJzY2PRbJfYPuFNNMbWrcF7sY6eC21JY/640?wx_fmt=png&from=appmsg)

在 Kibana Discover 中按 transaction.remote\_address 过滤，锁定攻击者 IP 10.0.2.15

## 第一阶段：侦察——Nmap 扫描

##

**调查思路：**想知道攻击者最早干了什么，最直觉的做法就是按时间排序，看最早的请求。在 Kibana 里把 @timestamp 字段设置为「从旧到新」排序，第一条日志就是攻击者的第一个动作。

把时间列从旧到新排列之后，最早的几条日志就暴露了攻击者的第一个工具。

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxicwny0ib1kXWY1Y6TzwKwHZv7BZGyRFib9mFcduGAFpDWibn59UmWuP94iaOLliavof42jnsSLP4w7wLNibicJOkXxibooicIme6YN875Q0/640?wx_fmt=png&from=appmsg)

对 @timestamp 字段设置「Sort Old-New」，让最早的请求排在最前面

看 request.headers.User-Agent 这一列，最早的请求里赫然出现了一个安全人员都非常熟悉的字符串：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbx9Z9gEefDNiaaSJT2y86slNibaSTWzFd4JiaHtzrR1ibeRah2s5vURkuD5NQ6vdZIrEwD0AREU7Hxccr07lvdiaCCNEWHdwlYXYNf0U/640?wx_fmt=png&from=appmsg)

User-Agent 字段中暴露了 Nmap Scripting Engine 的指纹

Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)

Nmap 是网络扫描领域的「瑞士军刀」，几乎是每个渗透测试人员的标配。它的 NSE（Nmap Scripting Engine）模块可以执行各种自动化探测任务——服务版本识别、漏洞检测、操作系统指纹等等。攻击者在动手之前先用 Nmap 对目标做了一次全面侦察，这一步在攻防对抗中非常典型。

对于 SOC 分析师来说，Nmap 扫描是一个重要的信号。它通常意味着有人在「踩点」，是攻击的前奏。很多 Nmap 的默认脚本会在 User-Agent 里自报家门——这倒不是 Nmap 的设计缺陷，而是很多扫描者懒得去修改这个字段。对于防守方而言，监控 User-Agent 中包含「Nmap」「masscan」「nuclei」等关键词的请求，是一个简单有效的预警手段。

**结论：**攻击者对 Slingway 的 Web 服务器执行的第一个操作是 Nmap 扫描。

## 第二阶段：目录枚举——Gobuster 暴力探测

##

**调查思路：**目录枚举工具的特点是对同一个域名在短时间内发起大量请求，尝试猜测隐藏的目录和文件。因为大部分猜测的路径并不存在，所以会返回大量的 404 响应。在日志里过滤 404 状态码，就能定位目录枚举行为。

Nmap 侦察完之后，攻击者的下一步是搞清楚这台服务器上到底有哪些页面和目录。他使用的工具是 Gobuster——一个用 Go 语言编写的高速目录暴力枚举工具。Gobuster 会拿着一份字典，逐行拼接 URL 向服务器发请求，看哪些路径是真实存在的。

这种暴力枚举的典型特征就是会产生海量的 404 响应。我们给过滤条件加上 response.status: 404，一下子筛出了 **1867** 条记录——攻击者尝试了将近两千个路径，绝大多数都返回了「页面不存在」。

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxiclFLCTOGkTWdZwvdaMmoKhr2wBXLaJiaQyNLayI9dYrv33eAibll7eh1qkM8y1A128KUn2KMQib5Wib0II5lcLZ7ia0mDEsfghGuBk/640?wx_fmt=png&from=appmsg)

添加 response.status: 404 过滤条件后，1867 条记录暴露了目录枚举行为

再看看这些 404 请求的 User-Agent，Gobuster 暴露了自己的身份：Mozilla/5.0 (Gobuster)。和 Nmap 一样，Gobuster 默认的 User-Agent 也没有做什么伪装，直接用工具名往日志里写了。

虽然大多数路径都返回了 404，但 Gobuster 也确实帮攻击者找到了几个关键目录。我们把过滤条件换成 response.status: 200（只保留 Gobuster 的请求），发现了 9 条成功响应——其中包括几个常规页面（/contact.php、/index.php、/register.php 等），但有一个目录格外引人注意：

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxibmGI0A31ibibSDsMO7MkMmzPx0Grib8vumpTbv4xnLsyjYDSbPm2aAQUZm5Hz0ficqjvEv5SveH13gXCC9xKwnw3VTiaicaFqC7gAic8/640?wx_fmt=png&from=appmsg)

Gobuster 的 200 响应中，/backups 目录包含了一个可疑的 flag 文件

在 /backups 目录下，Gobuster 发现了一个名为 f1agra76637b62ea99acda12f5859313f539a 的文件——这是攻击者挖到的第一个 flag。一个正式运行的生产环境里出现一个 /backups 目录，本身就是一个严重的安全隐患。很多开发团队会把数据库备份、配置文件备份随手放在 Web 根目录下的某个子文件夹里，以为没人会猜到这个名字。但目录枚举工具恰恰就是干这个的——它不需要「猜」，它用字典穷举。

除此之外，Gobuster 还通过 301 重定向（状态码既不是 200 也不是 404）发现了另一个重要目标。我们给过滤条件加上「非 200 且非 404」的限制：

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbx9CPGSHEgDibs6FmbYj13icicaMCWljw7N7ATK48hKbw3YL8dYnNry7tHytsL2eZ6fyowTE3wS1EvA6iapAjicxgPoUG3abGAwCqKkc/640?wx_fmt=png&from=appmsg)

编辑过滤器，排除 200 和 404 响应，专门查看重定向记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbx8GPXzpHfL164rVibehFjyeiazUv6LKhYNR9jDxYuTXozicAlBQQNwdQLCuJ4VaWteHojVv8K6ibud6poylgibFlicKsIicyqicEO2zGqk/640?wx_fmt=png&from=appmsg)

301 重定向记录中，/admin-login.php 赫然出现——攻击者找到了管理后台入口

/admin-login.php——一个管理后台的登录页面。对于攻击者来说，这就像是在一堵墙上找到了一扇门。下一步要做的，自然就是想办法把门撬开。

**小结：**在目录枚举阶段，攻击者一共发起了 1867 次无效请求，但只需 9 次成功的 200 响应就够他找到突破口。/backups 目录泄露了第一个 flag，/admin-login.php 为下一步暴力破解提供了入口。

## 第三阶段：暴力破解——Hydra 爆破管理员密码

##

**调查思路：**暴力破解登录页面的特征是短时间内对同一个认证端点发起大量 POST 请求，绝大部分返回 401（认证失败）。一旦某个请求返回了 200，就说明爆破成功了。

找到了登录页面之后，攻击者拿出了 Hydra。Hydra 是一个老牌的多协议暴力破解工具，支持 SSH、FTP、HTTP 表单等多种协议的密码爆破。它的特点是速度极快，支持多线程并行尝试，而且内置了大量常见密码字典。

我们把过滤条件设为 response.status: 401，结果跳出来 **486** 条记录——全部来自 /admin-login.php，全部是认证失败。User-Agent 清一色写着：

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxiblic3jwJ5XaGESMFAAam0BLOh4aPhcic2NURAxHk9mtE55pysV55fl4hsiaLNicHPM81mOxadyOUGATmvkaNctlqpzmKHtuMvMAHw/640?wx_fmt=png&from=appmsg)

过滤 401 状态码，486 条失败认证的 User-Agent 全部是 Mozilla/4.0 (Hydra)

Mozilla/4.0 (Hydra)——又是毫不掩饰的自报家门。Hydra 的默认 User-Agent 直接带着工具名，连伪装都没有。

486 次失败之后，有没有成功的那一次？我们把条件改成「Hydra 的请求，但不是 401」，答案立刻浮出水面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbx8Nc6TKNduRU6uuHL5qRI1ScfqDWxJhH5ywZUq1QxYnnapvoRvPnV3zdLCsG4OJheicqjDf5rRjSyIGjbRJxuib6F2gEqe0ArIqE/640?wx_fmt=png&from=appmsg)

排除 401 后，仅剩一条 Hydra 请求——状态码 200，说明密码爆破成功

一条 200 响应，这意味着 Hydra 在第 487 次尝试时成功登录了管理后台。展开这条日志的详细信息，可以看到请求头中的 Authorization 字段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxibTEBYVVNZy6W0WsE55yV1GKzXYJaCibEk0Tc07ic1LHkVE9wOyKYDd0z8iccIyNmfJhlWqZgCSujdQFgNDgbDhqTzxZ5YhxUVskU/640?wx_fmt=png&from=appmsg)

展开日志详情，Authorization 字段的 Base64 值可以直接解码出明文凭据

Basic YWRtaW46YWRtaW4xMjM=——这是 HTTP Basic Authentication 的标准格式。后面的字符串是 Base64 编码，解码后得到 admin:admin123。用户名 admin，密码 admin123。这个密码强度基本等于没设密码——它甚至出现在了大多数密码字典的前 100 行里。用这种密码保护管理后台，等同于给攻击者留了一扇没上锁的门。

**小结：**486 次失败，1 次成功。Hydra 用弱口令字典暴力破解了 admin 账户，凭据是 admin:admin123。一个强密码本可以让暴力破解在有限时间内变得毫无意义——但 admin123 显然不是。

## 第四阶段：上传 Webshell——从浏览器到命令行的跨越

##

**调查思路：**攻击者拿到后台权限后，下一步通常是上传一个 Webshell——一个 PHP 脚本文件，可以让攻击者通过浏览器远程执行系统命令。搜索上传相关的 URL 和已知的 Webshell 文件名，就能定位这一步。

拿到管理员密码之后，攻击者堂而皇之地登录了后台。通过搜索 /admin/\* 路径下的请求，可以看到他浏览了 /admin/upload.php（上传页面）和 /admin/settings.php（设置页面）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxiccBoZwhbsq62qvpX1lT4MZL0CTpTU9IZkF4xYUeIA1kic4JO3luW9YHl4qj6ba5uNV2CibbGOGzooBIIc8f9TNE6KUfZkeZcng8/640?wx_fmt=png&from=appmsg)

过滤 /admin/\* 路径，可以看到攻击者在后台浏览了上传页面和设置页面

然后，他通过上传功能把一个 PHP Webshell 丢到了服务器上。这个文件叫 easy-simple-php-webshell.php，被放在了 /uploads/ 目录下。搜索这个文件名，可以看到攻击者通过这个 Webshell 执行了一系列系统命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbx8iaqFuPOjrM66iaBdXYq26IU75Jsr8dtwgNfgNe2FcBFFvUUyLd6mBibFBgluWyTrwvFbkaYVmxlgwR0CCJIwHxtUT9qKuBSBIQg/640?wx_fmt=png&from=appmsg)

搜索 webshell 文件名，可以看到攻击者通过 URL 参数传递的命令：whoami、ls、pwd、which nc……

从 URL 参数里可以清楚地看到每条命令——whoami、ls、pwd、which nc。这是 Webshell 的典型用法：命令通过 GET 参数传进去，PHP 的 system() 或 exec() 函数在服务器端执行，结果返回到浏览器。攻击者就这样从一个「只能发 HTTP 请求的匿名用户」，变成了一个「可以在服务器上跑任意命令的入侵者」。

他执行的第一条命令是 whoami——查看当前进程以什么用户身份运行。这是所有渗透测试的起手式：先搞清楚自己是谁、有什么权限，然后才能决定下一步做什么。后续的 ls 和 pwd 是在浏览文件系统结构，which nc 则是在检查服务器上有没有安装 netcat——如果有，就可以用它建立反向连接，获得一个交互式 shell。

这个 Webshell 本身还包含了一个 flag：f1aga97e04526418d40ce374f57a88bf2。从文件名「easy-simple」来看，攻击者用的是一个非常基础的开源 Webshell——功能简陋但够用。很多 Webshell 检测方案会扫描上传目录中可疑的 PHP 文件，但这个前提是你要知道上传目录在哪里、以及有没有开启文件上传审计。

**小结：**攻击者通过后台上传了 easy-simple-php-webshell.php...