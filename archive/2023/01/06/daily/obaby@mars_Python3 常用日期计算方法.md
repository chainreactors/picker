---
title: Python3 常用日期计算方法
url: https://h4ck.org.cn/2023/01/python3-%e5%b8%b8%e7%94%a8%e6%97%a5%e6%9c%9f%e8%ae%a1%e7%ae%97%e6%96%b9%e6%b3%95/
source: obaby@mars
date: 2023-01-06
fetch_date: 2025-10-04T03:08:38.571248
---

# Python3 常用日期计算方法

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# Python3 常用日期计算方法

2023年1月5日
[2 条评论](https://h4ck.org.cn/2023/01/10931#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

后台做数据分析汇总的时候需要处理各种时间段，每天的零点、每周的第一天最后一天、每月的第一天最后一天等，不知道有没有现成的可用库来处理。搜索的基本也是各种其他人写的方法，我这里汇总了一下（抄了一些代码）。

日期处理一般会用到下面几个库：time，datetime，calendar。一般通过这几个库来处理时间也够用了。

## time 模块

该模块包括使用时间执行各种操作所需的所有与时间相关的功能，它还允许我们访问多种用途所需的时钟类型。

**内置函数:**

请看下表，它描述了时间模块的一些重要内置功能。
![在这里插入图片描述](https://img-blog.csdnimg.cn/3a782c88eed84378b2bad9175c1b50a6.png)
**代码格式化:**

在用示例解释每个函数之前，先看一下所有合法的格式化代码的方式：

![在这里插入图片描述](https://img-blog.csdnimg.cn/be8ef83e8292470395ac079edb862483.png)

struct\_time 类具有以下属性：

![在这里插入图片描述](https://img-blog.csdnimg.cn/ad917830b0b2499c9a4ffa5807a9a1e5.png)

## datetime 模块

与time模块类似，datetime模块包含处理日期和时间所必需的所有方法。

**内置功能：**

下表介绍了本模块中的一些重要功能：

![在这里插入图片描述](https://img-blog.csdnimg.cn/e92b4bc8e2a140629cd6715ec888ae00.png)

## **calendar模块**

该模块定义了很多类型，主要包括：Calendar、TextCalendar、HTMLCalendar，其中 Calendar 是 TextCalendar 和 HTMLCalendar 的基类，这些类有着十分丰富的日历处理方法。

同时ISO 8601标准还规定了 0 和 负数年份。0年指公元前1年， -1年指公元前2年，依此类推。

具体代码：

```
import math
from datetime import datetime, timedelta, date
import calendar

def get_today_zero_time():
    """
    获取当前零点时间
    """
    time_now = datetime.now()
    zero_time = time_now - timedelta(hours=time_now.hour) - timedelta(minutes=time_now.minute) - timedelta(
        seconds=time_now.second) - timedelta(microseconds=time_now.microsecond)
    return zero_time

def get_current_hour():
    """
    获取当前整点时间
    """
    time_now = datetime.now()
    time_now_hour = time_now - timedelta(minutes=time_now.minute) - timedelta(seconds=time_now.second) - timedelta(
        microseconds=time_now.microsecond)
    return time_now_hour

def get_last_five_minutes_time():
    """
    获取上一个整五分钟时间
    """
    time_now = datetime.now()
    mins = math.floor(time_now.minute /5) *5
    time_now_hour = time_now - timedelta(minutes=time_now.minute) - timedelta(seconds=time_now.second) - timedelta(
        microseconds=time_now.microsecond) + timedelta(minutes=mins)
    return time_now_hour

def get_month_start_time():
    now = datetime.now().date()
    this_month_start = datetime(now.year, now.month, 1)
    this_month_end = datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    return this_month_start

def get_month_first_and_last_day(year, month):
    # 获取当前月的第一天的星期和当月总天数
    weekDay, monthCountDay = calendar.monthrange(year, month)
    # 获取当前月份第一天
    firstDay = date(year, month, day=1)
    # 获取当前月份最后一天
    lastDay = date(year, month, day=monthCountDay)
    # 返回第一天和最后一天
    return firstDay, lastDay

def get_past_month_first_and_last_day():
    if  date.today().month ==1:
        lastMonthFirstDay = date(date.today().year-1, 12, 1)
    else:
        lastMonthFirstDay = date(date.today().year, date.today().month - 1, 1)
    lastMonthLastDay = date(date.today().year, date.today().month, 1) - timedelta(1)
    return lastMonthFirstDay, lastMonthLastDay

def get_year_first_and_last_day(now_time):
    this_year_start = datetime(now_time.year, 1, 1)
    this_year_end = datetime(now_time.year + 1, 1, 1) - timedelta(days=1)
    return this_year_start, this_year_end

def get_this_week_start_and_end_day():
    today = date.today()
    return  today - timedelta(days=today.weekday())

def get_past_week_start_and_end_day():
    today = date.today()
    # threeWeeksAgo_start = today - timedelta(days=today.weekday() + 21)
    # threeWeeksAgo_end = today - timedelta(days=today.weekday() + 15)
    # twoWeeksAgo_start = today - timedelta(days=today.weekday() + 14)
    # twoWeeksAgo_end = today - timedelta(days=today.weekday() + 8)
    last_week_start = today - timedelta(days=today.weekday() + 7)
    last_week_end = today - timedelta(days=today.weekday() + 1)
    return last_week_start, last_week_end

def get_week_start_and_end_day_at_date(q_date):
    last_week_start = q_date - timedelta(days=q_date.weekday() + 7)
    last_week_end = q_date - timedelta(days=q_date.weekday() + 1)
    return last_week_start, last_week_end

if __name__ == "__main__":
    print(get_last_five_minutes_time())
    print(get_month_start_time())
    print(get_today_zero_time() - get_month_start_time())
    print(get_month_first_and_last_day(get_today_zero_time().year, get_month_start_time().month))
    print(get_past_month_first_and_last_day())
    print(get_past_week_start_and_end_day())
```

参考链接：

http://www.bryh.cn/a/63810.html

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Python3 常用日期计算方法》](https://h4ck.org.cn/2023/01/10931)
\* 本文链接：<https://h4ck.org.cn/2023/01/10931>
\* 短链接：<https://oba.by/?p=10931>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Python](https://h4ck.org.cn/tags/python)

[Previous Post](https://h4ck.org.cn/2023/01/10966)
[Next Post](https://h4ck.org.cn/2023/01/10911)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年6月6日

#### [Python tools for VS2012](https://h4ck.org.cn/2013/06/5227)

2019年3月1日

#### [由apscheduler引发的django.db.utils.InternalError: (1054, u”Unknown column ‘rms.go\_datetime’ in ‘field list'”)](https://h4ck.org.cn/2019/03/6374)

2025年4月2日

#### [南墙 WAF 系列（二）– 网站证书自动更新](https://h4ck.org.cn/2025/04/20086)

### 2 comments

1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r) **[Teacher Du](https://dusays.com)**说道：

   [2023年1月9日 16:51](https://h4ck.org.cn/2023/01/10931#comment-90947)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 108") Microsoft Edge 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   来学习啦！

   [回复](#comment-90947)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年1月9日 18:21](https://h4ck.org.cn/2023/01/10931#comment-90951)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      杜老师客气啦~~~

      [回复](#comment-90951)

### 发表回复 [取消回复](/2023/01/10931#respond)

您的邮箱地址不会被公开。 必填项已用 ...