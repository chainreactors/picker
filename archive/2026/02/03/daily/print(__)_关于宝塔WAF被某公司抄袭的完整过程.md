---
title: 关于宝塔WAF被某公司抄袭的完整过程
url: https://www.o2oxy.cn/4502.html
source: print("")
date: 2026-02-03
fetch_date: 2026-02-04T04:06:36.306057
---

# 关于宝塔WAF被某公司抄袭的完整过程

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# 关于宝塔WAF被某公司抄袭的完整过程

作者: print("")
分类: [未分类](https://www.o2oxy.cn/category/uncategorized)
发布时间: 2026-02-03 21:18
阅读次数: 710 次

## 大家好，我是宝塔WAF的作者。

## 我今天本来在愉快的修bug 同事给我发了一张图片

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/微信图片_2026-02-03_192052_395.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_2026-02-03_192052_395.png)

我一眼看过去这不是我的代码吗。
然后就通过Demo 进去看了下，
发现是我写的代码

通过文件管理功能把代码下载了下来。
如下：

代码文件 ：<https://www.o2oxy.cn/wp-content/uploads/2026/02/b3ne5A.tar.gz>

MD5 :<https://www.o2oxy.cn/wp-content/uploads/2026/02/b3ne5A.tar.gz_md5.txt>

# 如下是对比结果：

请大家看看

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/ScreenShot_2026-02-03_193446_628.png))](https://www.o2oxy.cn/wp-content/uploads/2026/02/ScreenShot_2026-02-03_193446_628.png%29)

代码对比 直接上图把

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/cc.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/cc.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/city.pnbg_.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/city.pnbg_.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/city.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/city.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/header.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/header.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/ipinfo.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/ipinfo.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/lib.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/lib.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/public.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/public.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/request_check.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/request_check.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/route.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/route.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/ScreenShot_2026-02-03_193633_039.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/ScreenShot_2026-02-03_193633_039.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/white_black.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/white_black.png)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/xss.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/xss.png)

### 说几个有意思的东西把！

request\_check.lua  直接是我的代码复制过来。发现改不动就注释了

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/222.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/222.png)

还有遗留代码

```
-- 遍历/www/server 目录判断是否存在monitor 目录
function public.is_monitor()
    -- 判断缓存中是否存在
    if ngx.shared.safewaf:get("is_monitor") and ngx.shared.safewaf:get("is_monitor") == "1" then
        return true
    end
    local server_list = public.listdir("/www/server")
    for _, v in ipairs(server_list) do
        if v == "monitor" then
            ngx.shared.safewaf:set("is_monitor", "1")
            return true
        end
    end
    ngx.shared.safewaf:set("is_monitor", "0")
    return false
end

```

我同事说的垃圾代码函数

```
function cc.renjiyanzheng(type)
    local mod_name = 'cc_renjiyanzheng'
```

不是，我这个函数应该没人有雷同把？

当看到这里的时候相信大家已经看出来了，这个项目完全是复制了宝塔WAF 的代码，然后把项目名字改了下，

# 维权（大家喜闻乐见、当个乐子就可以）

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/1.jpg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/1.jpg)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/2.jpg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/2.jpg)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/3.jpg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/3.jpg)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/4.jpg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/4.jpg)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/5.jpg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/5.jpg)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/6.jpg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/6.jpg)

# 后续 GM-蜗牛就把我剔出来了

# 强行洗白

说好的拉群。我没见到。但是我看到了这个

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/7.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/7.png)

然后又找了群里的一群人在自导自演了一些戏

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/88.jpeg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/88.jpeg)

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/77-scaled.jpeg)](https://www.o2oxy.cn/wp-content/uploads/2026/02/77-scaled.jpeg)

感觉像是碟中谍一样的。把我踢出群里，又在群里随便加几个群友。装作自己是受害者一样。

# 结语

[![](https://i.imgur.com/4fAMBxm.jpeg)](https://i.imgur.com/4fAMBxm.jpeg)

### **好的项目是需要时间和精力去打磨的。而不是抄袭+踩着别人的肩膀往上爬。**

上次已经抄袭过了一次了。这次又来了。

### 声明一下。我没有收到任何道歉+认错，反而只是一味的洗白。

关于上次的文章链接：[宝塔又被抄袭了？ GMSSH？](https://www.v2ex.com/t/1152822#r_16634483)

喜闻乐见的评论了

[![](https://www.o2oxy.cn/wp-content/uploads/2026/02/44.png)](https://www.o2oxy.cn/wp-content/uploads/2026/02/44.png)

# 版权声明

本文为原创文章，版权归作者所有，未经允许不得转载

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4502.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [关于宝塔WAF被某公司抄袭的完整过程](https://www.o2oxy.cn/4502.html)
* [《机器学习》（西瓜书）课后习题 第一章](https://www.o2oxy.cn/4471.html)
* [React2Shell CVE-2025-55182 复现](https://www.o2oxy.cn/4460.html)

* [通过python 把图片变为字符串](https://www.o2oxy.cn/1201.html "通过python 把图片变为字符串")
* [django之CSFR](https://www.o2oxy.cn/1640.html "django之CSFR")
* [语法分析-上下文无关文法简单理解](https://www.o2oxy.cn/4312.html "语法分析-上下文无关文法简单理解")
* [Java Tomcat内存马—入门到入土](https://www.o2oxy.cn/3930.html "Java Tomcat内存马—入门到入土")
* [django ORM 多对多的主机管理](https://www.o2oxy.cn/1582.html "django ORM 多对多的主机管理")
* [Django 配置HTML 模板操作](https://www.o2oxy.cn/1601.html "Django 配置HTML 模板操作")
* [密码保护：某客服CMS代码审计](https://www.o2oxy.cn/2881.html "密码保护：某客服CMS代码审计")
* [Django 开发主机管理系统](https://www.o2oxy.cn/1450.html "Django 开发主机管理系统")
* [Spring Cloud Function 漏洞复现](https://www.o2oxy.cn/4029.html "Spring Cloud Function 漏洞复现")
* [docker 部署PHP+ nginx环境](https://www.o2oxy.cn/1651.html "docker 部署PHP+ nginx环境")

标签云

[Apache2.4.50](https://www.o2oxy.cn/tag/apache2-4-50)
[Apache ShenYu](https://www.o2oxy.cn/tag/apache-shenyu)
[APISIX](https://www.o2oxy.cn/tag/apisix)
[APISIX Dashboard](https://www.o2oxy.cn/tag/apisix-dashboard)
[cc5](https://www.o2oxy.cn/tag/cc5)
[CNVD-2021-49104](https://www.o2oxy.cn/tag/cnvd-2021-49104)
[CNVD-2022-60632](https://www.o2oxy.cn/tag/cnvd-2022-60632)
[CobaltStrike](https://www.o2oxy.cn/tag/cobaltstrike)
[CobaltStrike xss](https://www.o2oxy.cn/tag/cobaltstrike-xss)
[CommonsCollections5](https://www.o2oxy.cn/tag/commonscollections5)
[Confluence CVE-2021-26084](https://www.o2oxy.cn/tag/confluence-cve-2021-26084)
[CVE-2017-18349](https://www.o2oxy.cn/tag/cve-2017-18349)
[CVE-2021-4034](https://www.o2oxy.cn/tag/cve-2021-4034)
[CVE-2021-37580](https://www.o2oxy.cn/tag/cve-2021-37580)
[CVE-2021-41277](https://www.o2oxy.cn/tag/cve-2021-41277)
[CVE-2021-41773](https://www.o2oxy.cn/tag/cve-2021-41773)
[cve-2021-42013](https://www.o2oxy.cn/tag/cve-2021-42013)
[CVE-2021-43798](https://www.o2oxy.cn/tag/cve-2021-43798)
[CVE-2021-44228](https://www.o2oxy.cn/tag/cve-2021-44228)
[CVE-2021-45232](https://www.o2oxy.cn/tag/cve-2021-45232)
[CVE-2021-45232 RCE](https://www.o2oxy.cn/tag/cve-2021-45232-rce)
[CVE-2022-22954](https://www.o2oxy.cn/tag/cve-2022-22954)
[CVE-2022-22965](https://www.o2oxy.cn/tag/cve-2022-22965)
[CVE-2022-39197](https://www.o2oxy.cn/tag/cve-2022-39197)
[CVE-2023-28432](https://www.o2oxy.cn/tag/cve-202...