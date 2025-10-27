---
title: 再读《软件随想录》/《黑客与画家》/《软技能》
url: https://jiajunhuang.com/articles/2024_09_06-reread_3_books.md.html
source: Jiajun的技术笔记
date: 2024-09-07
fetch_date: 2025-10-06T18:20:00.442320
---

# 再读《软件随想录》/《黑客与画家》/《软技能》

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [再读《软件随想录》/《黑客与画家》/《软技能》](#%25E5%2586%258D%25E8%25AF%25BB%25E3%2580%258A%25E8%25BD%25AF%25E4%25BB%25B6%25E9%259A%258F%25E6%2583%25B3%25E5%25BD%2595%25E3%2580%258B%252F%25E3%2580%258A%25E9%25BB%2591%25E5%25AE%25A2%25E4%25B8%258E%25E7%2594%25BB%25E5%25AE%25B6%25E3%2580%258B%252F%25E3%2580%258A%25E8%25BD%25AF%25E6%258A%2580%25E8%2583%25BD%25E3%2580%258B)
* [《软件随想录》](#%25E3%2580%258A%25E8%25BD%25AF%25E4%25BB%25B6%25E9%259A%258F%25E6%2583%25B3%25E5%25BD%2595%25E3%2580%258B)
* [不要陷入技术口水战](#%25E4%25B8%258D%25E8%25A6%2581%25E9%2599%25B7%25E5%2585%25A5%25E6%258A%2580%25E6%259C%25AF%25E5%258F%25A3%25E6%25B0%25B4%25E6%2588%2598)
* [乔尔测试](#%25E4%25B9%2594%25E5%25B0%2594%25E6%25B5%258B%25E8%25AF%2595)
* [自动从用户那里收集错误报告](#%25E8%2587%25AA%25E5%258A%25A8%25E4%25BB%258E%25E7%2594%25A8%25E6%2588%25B7%25E9%2582%25A3%25E9%2587%258C%25E6%2594%25B6%25E9%259B%2586%25E9%2594%2599%25E8%25AF%25AF%25E6%258A%25A5%25E5%2591%258A)
* [任务切换有害论](#%25E4%25BB%25BB%25E5%258A%25A1%25E5%2588%2587%25E6%258D%25A2%25E6%259C%2589%25E5%25AE%25B3%25E8%25AE%25BA)
* [《黑客与画家》](#%25E3%2580%258A%25E9%25BB%2591%25E5%25AE%25A2%25E4%25B8%258E%25E7%2594%25BB%25E5%25AE%25B6%25E3%2580%258B)
* [《软技能》](#%25E3%2580%258A%25E8%25BD%25AF%25E6%258A%2580%25E8%2583%25BD%25E3%2580%258B)
* [把自己当作一家企业](#%25E6%258A%258A%25E8%2587%25AA%25E5%25B7%25B1%25E5%25BD%2593%25E4%25BD%259C%25E4%25B8%2580%25E5%25AE%25B6%25E4%25BC%2581%25E4%25B8%259A)
* [设定目标](#%25E8%25AE%25BE%25E5%25AE%259A%25E7%259B%25AE%25E6%25A0%2587)
* [人际交往能力](#%25E4%25BA%25BA%25E9%2599%2585%25E4%25BA%25A4%25E5%25BE%2580%25E8%2583%25BD%25E5%258A%259B)
* [债务](#%25E5%2580%25BA%25E5%258A%25A1)

# 再读《软件随想录》/《黑客与画家》/《软技能》

最近重读了这三本书。上一次读大概还是在10年前，有了这些年的工作经验，再看这些书，感触颇深。

---

## 《软件随想录》

### 不要陷入技术口水战

比如你喜欢用什么编辑器，喜欢用什么编程语言，喜欢用什么操作系统，这些都是个人喜好，没有对错之分。不要陷入无意义的口水战。
而是要看什么场景用什么工具，对症下药。例如，UNIX程序员喜欢文本模式，Windows程序员喜欢图形界面。UNIX文化老是吐槽Windows
注册表，但是UNIX的配置文件到处都是。又或者C语言高效，Python是玩具等等。这些都是无意义的争论。

应该在合适的场景使用合适的工具，比如UNIX的文化来源于哪里呢？UNIX来源于他是面向程序员的操作系统，而Windows是面向用户的操作系统。
文本对程序员是友好的，但是你要一个老奶奶来用编辑器编辑配置文件，那就很折磨人了。

要快速迭代时，用Python，要高效时，用Go，嵌入式用C，开发浏览器页面就得用JS等等。

### 乔尔测试

* 你们用源代码管理系统吗？
* 你们能一键编译吗？
* 你们做每日编译吗？
* 你们有bug数据库吗？
* 你们在写新代码前修改以前的代码吗？
* 你们的进度表是最新的吗？
* 你们有软件规格书吗？
* 程序员的工作环境是安静的吗？
* 你们使用了能买到的最好工具吗？
* 你们有测试人员吗？
* 你们面试时会要求应聘人员写代码吗？
* 你们做过走廊可用性测试吗？

是就给你的团队加上1分，否则就是0分。得分越高，团队越好。12分是完美的，11分尚可，10分或更低就意味着开发团队出了很严重的问题。

这一篇文章写于2000年，现在看来，这些问题都是很基础的问题，但是很多团队还是做不到。里面的很多东西，也成了现在的基础设施，
比如源码管理系统，今天的git；编译，今天的CI/CD；bug数据库，今天的issue tracker等等。

### 自动从用户那里收集错误报告

这不就是现在的Sentry/Crashlytics等等吗？

### 任务切换有害论

多个任务并行，不断切换，的确会降低效率。

---

## 《黑客与画家》

黑客是一种文化，是一种态度，是一种精神。黑客是对技术的热爱，是对技术的追求，是对技术的探索。

思想自由比言论自由更重要。

此外还可以阅读 Raymond. Eric S. 的 How to become a hacker。

---

## 《软技能》

软技能是什么？软技能是与技术无关的技能。

### 把自己当作一家企业

我们习惯了打工，领取月薪。如果换个视角，会更好。把自己当作一家企业，现在的雇主只是你的第一个客户，你可以有更多的客户。
作为一个企业，就要想办法提高自己的价值，提高自己的收入。因此需要思考品牌，市场，销售等等。

### 设定目标

要有中期目标和短期目标。中期目标是你的职业规划，比如5年后，10年后你想成为什么样的人。短期目标一般是最近的几个月，比如
你想学习什么技术，你想做什么项目等等。

我个人一般会设置5年规划，以及每年定目标。然后再拆分成每个月的目标。

### 人际交往能力

说到底，计算机程序是为人服务的，工作中写文档、写邮件、开会、沟通其实都是和人打交道。甚至写代码也是为了给人用。
所以千万不要想着“我只想安安静静的写代码”。

### 债务

不要背负债务。

---

##### 相关文章

* [MySQL EXPLAIN中的filesort是什么？](/articles/2018_05_15-mysql_filesort.md.html)
* [数据库索引设计与优化](/articles/2018_05_13-mysql_index.md.html)
* [如何调试？](/articles/2018_05_08-how_to_debug.md.html)
* [Docker CE 18.03源码阅读与分析](/articles/2018_04_14-docker_ce_18_analysis.md.html)
* [容器时代的日志处理](/articles/2018_04_12-docker_logging.md.html)
* [Golang和Thrift](/articles/2018_04_10-golang_thrift.md.html)
* [折腾Kubernetes](/articles/2018_04_05-kubernetes.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [goroutine 切换的时候发生了什么？](/articles/2018_03_29-goroutine_schedule.md.html)
* [Prometheus 数据类型](/articles/2018_03_19-prometheus.md.html)
* [Gin源码阅读与分析](/articles/2018_03_16-gin_source_code.md.html)
* [如何面试-作为面试官得到的经验](/articles/2018_03_10-interview.md.html)
* [自己写一个容器](/articles/2018_03_09-write_you_a_container.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [软件开发之禅---大事化小，各个击破](/articles/2018_02_26-zen_of_dev.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。