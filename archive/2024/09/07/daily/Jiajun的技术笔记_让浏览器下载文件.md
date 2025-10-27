---
title: 让浏览器下载文件
url: https://jiajunhuang.com/articles/2024_09_06-browser_download_file.md.html
source: Jiajun的技术笔记
date: 2024-09-07
fetch_date: 2025-10-06T18:19:59.583510
---

# 让浏览器下载文件

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

* [让浏览器下载文件](#%25E8%25AE%25A9%25E6%25B5%258F%25E8%25A7%2588%25E5%2599%25A8%25E4%25B8%258B%25E8%25BD%25BD%25E6%2596%2587%25E4%25BB%25B6)
* [前端的处理](#%25E5%2589%258D%25E7%25AB%25AF%25E7%259A%2584%25E5%25A4%2584%25E7%2590%2586)
* [总结](#%25E6%2580%25BB%25E7%25BB%2593)

# 让浏览器下载文件

不知道你是不是遇到过这样的需求，想要从服务器将一个文件发送给用户。原来我以为，直接遵循这么几步就可以：

* 将文件内容写入到响应体中
* 设置响应头中的 `Content-Type` 为 `application/octet-stream`
* 设置响应头中的 `Content-Disposition` 为 `attachment; filename=xxx`

搞定，从后端来说，的确是这样就可以。

但是真正使用的时候，不一定能触发下载。因为浏览器是否会自动触发文件下载，有多种因素影响：

* `Content-Disposition` 头，服务端需要设置为 `attachment`，这样浏览器才会提示下载
* 浏览器本身的设置，如果设置了不自动下载，那么即使服务端设置了 `attachment`，也不会自动下载
* 如果前端代码是通过AJAX请求的，那么即使服务端设置了 `attachment`，也不会自动下载，必须要在前端代码中做特殊处理
* 如果服务器防火墙对下载做了限制，可能会被阻止下载

不过最常见的因素，是第一点和第三点。第一点是服务端设置不对，第三点是前端代码没有处理好。

## 前端的处理

写前端代码之前，我是不知道前端还需要做特殊处理的。我以为只要服务端设置了 `attachment`，浏览器就会自动下载。
不过实际上并非如此。

前端需要做如下处理：

```
$http.get('/download')
    .then(function (response) {
        var retData = response.data;

        const blob = new Blob([retData], {type: 'application/octet-stream'});
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'audit_log.csv';
        a.click();
    });
```

这里的关键点是：

* 将返回的二进制数据转换为 `Blob` 对象
* 通过 `URL.createObjectURL` 创建一个 URL
* 创建一个 `a` 标签，设置 `href` 为上面创建的 URL，设置 `download` 为文件名
* 触发 `a.click()` 事件

这样就可以触发下载了。

> 什么是Blob对象？Blob对象表示一个不可变、原始数据的类文件对象。Blob表示的数据不一定是一个JavaScript原生格式。
> File接口基于Blob，继承了blob的功能并将其扩展使其支持用户系统上的文件。

## 总结

多学点前端知识，对后端开发也是有好处的。以前我就是纯粹的后端开发，对前端的知识了解的不多，以为只要服务端设置了对应的
头部，服务器就可以自动控制下载。实际上也不是这么简单的。

---

##### 相关文章

* [Golang中实现禁止拷贝](/articles/2018_11_12-golang_nocopy.md.html)
* [人生如戏，全靠演技 -- 《日常生活中的自我呈现》读后感](/articles/2018_11_11-the_presentation_of_self_in_everyday_life.md.html)
* [数据库事务](/articles/2018_11_10-transaction.md.html)
* [Golang的反射](/articles/2018_11_10-golang_reflection.md.html)
* [把网站去掉CSS之后](/articles/2018_11_09-drop_css.md.html)
* [处理并发的方式](/articles/2018_11_07-concurrency.md.html)
* [常见的索引方式](/articles/2018_11_02-index.md.html)
* [Golang 实践经验](/articles/2018_11_01-golang_practice.md.html)
* [高性能MySQL笔记第一章](/articles/2018_10_23-high_performance_mysql_chap1.md.html)
* [面试的一些技巧](/articles/2018_10_21-interview_techniques.md.html)
* [HTTP/2 简介](/articles/2018_10_13-http2.md.html)
* [独立运营博客一年的一些数据分享](/articles/2018_09_24-blogging_one_year.md.html)
* [To B(usiness) 和 To C(ustomer)](/articles/2018_09_22-to_b_to_c.md.html)
* [常见的软件架构套路](/articles/2018_09_16-common_software_archtecture_pattern.md.html)
* [Cookie 中的secure和httponly属性](/articles/2018_09_16-cookie_secure_httponly.md.html)

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