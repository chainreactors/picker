---
title: dom xss->半自动化 - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/16921374.html
source: 博客园 - 飘渺红尘✨
date: 2022-11-25
fetch_date: 2025-10-03T23:44:10.565560
---

# dom xss->半自动化 - 飘渺红尘✨

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [dom xss->半自动化](https://www.cnblogs.com/piaomiaohongchen/p/16921374.html "发布于 2022-11-24 11:47")

前几天看了两篇文章，觉得很不错，写一笔，就当笔记记录。

　　第一篇文章:<https://jinone.github.io/bugbounty-dom-xss/>

　　作者写了自己通过自动化挖dom xss，差不多赚了3w刀左右。他分享了一些不错的漏洞案例。这里很感谢作者，无私分享思路出来，也给大家有了喝口汤的机会。

　　中国需要多一些这样的热爱分享的白帽子，一方面是推动安全测试水位，另一方面是带来更多的思路给他人。看这篇文章，给了我一些启发。在相当内卷的今天，选择适合自己的漏洞挖掘赛道很重要。就像不是人人都适合挖rce，一个道理。

　   第一篇文章的细节点:

　　访问:

```
https://example.com/xsspath'%22?xssparam%27%22=xssvalue%27%22#xsshash'%22
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124111717725-1188572471.png)

结论:

```
location.search 会对'"编码
location.hash 不会对'编码
location.pathnme 不会对'编码
location.href hash和pathname中的'不会被编码 包含search,hash和pathname

{ 这三个可以跳出单引号
location.href
location.hash
location.pathname
}
```

　　因为作者文章中提到有自动化挖掘。这里就调研了下市面上的工具，记录下:

　　通过查看作者写的文章，以及自己对dom xss的理解，简单写下半动化的粗略思路

**dom xss半自动化简单思路:**

```
{
n个source
n个sink
如果有某个source和某个sink同时存在

疑似dom xss，命中
}

只检索applocation/javascript和text/html
```

　 关于dom xss的探测，多疑似，那么误报率就会很高。

　缺陷很明显，需要尽可能的收集javascript和javscipt库的source和sink，吃经验，吃规律，需要熟悉一定的规律。

　工具1:Dom Invader 可以用于检测dom xss和postMessage xss

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124112254846-16170428.png)

 　　检测postmessage+dom xss配置如下:

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124112325825-1342846655.png)

　　和写dom xss的作者聊过一些，这款工具，检测dom xss很不错

　　关于这个插件的学习教程:

```
https://www.youtube.com/watch?v=Wd2R47czzO0&t=156s
https://portswigger.net/blog/introducing-dom-
```

　　这里简单提一嘴，burpsuite很多插件，挖洞使用很方便，有空的话，我讲下burpsuite上一些很好的辅助挖洞神器。

　　这个工具我就一笔带过，他不是本文的重点，本文的重点是另一个工具:

**重点检测工具:semgrep**

semgrep? what?

```
A fast, open-source, static analysis tool for profoundly improving software security and reliability.
一种快速、开源、静态分析工具，可显著提高软件的安全性和可靠性。
我认为它就是grep命令的升级版，更加的强大。
```

　　优势:

```
1.支持本地，命令行运行，很方便
2.支持在线网站上创建和导入/新增规则
3.支持批量检测，无需对代码进行编译
```

　　什么场景下使用他们?

```
1.大量的代码，进行安全缺陷审查
2.漏洞挖掘，web代码审计
3.支持纯文本代码识别和污点跟踪
4.src/众测 部分代码需要
5.发现某个漏洞特征，使用semgrep事半功倍
```

　安装:

```
三种安装方式
# Using Homebrew
$ brew upgrade semgrep

# Using pip
$ python3 -m pip install --upgrade semgrep

# Using Docker
$ docker pull returntocorp/semgrep:latest
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124113011250-893406095.png)

　这里我使用的是第二种，pip安装。

　referer: https://github.com/returntocorp/semgrep

**semgrep基础使用:**

　1.命令行cl使用

```
semgrep --pattern '127.$A.$B.$C' --lang generic /etc/hosts

#lang 是指定某种类型
参考:https://semgrep.dev/docs/supported-languages/ 很详细
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124113111079-190487714.png)

参考:<https://semgrep.dev/docs/getting-started/>

—pattern是一种匹配模式。但是更推荐的是导入yaml，对某段代码/某个项目进行运行漏洞规则文件:

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124113147784-2100009264.png)

**漏洞yaml规则库大全 用于学习编写规则:**

```
https://github.com/returntocorp/semgrep-rules
https://semgrep.dev/playground/new?editorMode=advanced
```

　涉及到的语言众多

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124113249073-1944655314.png)

**污点跟踪 这个适合漏洞挖掘，半自动化:**

　　污点跟踪演示教程:https://semgrep.dev/docs/writing-rules/data-flow/taint-mode/

　　使用污点跟踪半动化检测dom xss:

```
rules:
  - id: domxss-insertAdjacentHTML
    languages:
      - javascript
      - typescript
    message: Found dangerous HTML output
    mode: taint
    pattern-sources:
      - pattern: document.location.href
      - pattern: document.location
      - pattern: window.location
      - pattern: window.location.href
    pattern-sinks:
      - pattern: $X.insertAdjacentHTML(...)
      - pattern: $X.innerHTML(...)
      - pattern: $X.innerHTML = ...
    severity: WARNING
```

　不想聊规则细节，我说下这段yaml哪里来的。

　参考:https://netsec.expert/posts/automating-dom-xss/

　一定要看，这篇文章作者是谷歌的一位安全工程师，这是他写的规则。

　他还写了一个辅助工具，用于爬虫网站上的js:https://github.com/the-xentropy/dump-scripts/blob/main/dump-scripts.py

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124113626941-1824565760.png)

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221124113737793-896543287.png)

　　然后调用semgrep批量检测script目录里的js。

　　这个规则，会漏掉很多dom xss，这里简单调研了下，source和sink非常多，这里只总结了一些常见的，整合了前面的几位作者的思路和官方规则:

　　总结了下用于检测js open redirect\_url和其他类型的dom xss规则:

```
rules:
  - id: dom_xss
    message: dom_xss
    metadata:
      cwe:
        - "dom_xss"
      owasp:
        - A03:2021 - Injection
      asvs:
        section: V5 Validation, Sanitization and Encoding
        control_id: 5.2.4 Dynamic Code Execution Features
        control_url: https://github.com/OWASP/ASVS/blob/master/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v52-sanitization-and-sandboxing
        version: "4"
      category: security
      technology:
        - browser
      subcategory:
        - audit
      likelihood: LOW
      impact: MEDIUM
      confidence: LOW
      references:
        - https://owasp.org/Top10/A03_2021-Injection
      license: Commons Clause License Condition v1.0[LGPL-2.1-only]
    languages:
      - javascript
      - typescript
    severity: WARNING
    mode: taint
    pattern-sources:
      - patterns:
          - pattern-inside: |
              url.split('...')
      - patterns:
          - pattern-inside: |
              getURLParameter('...')
      - patterns:
          - pattern-inside: |
              $PROPS.get('...')
      - patterns:
          - pattern-inside: |
              getUrlParameter('...')
      - patterns:
          - pattern-inside: |
              GetQueryString('...')
      - patterns:
          - pattern-inside: |
              $PROPS.get('...')
      - patterns:
          - pattern-inside: |
              $PROPS.split("...")
      - patterns:
          - pattern-either:
              - pattern-inside: >
                  $PROP = new URLSearchParams($WINDOW. ...
                  .location.search).get('...')

                  ...
              - pattern-inside: |
                  $PROP = new URLSearchParams(location.search).get('...')
                  ...
              - pattern-inside: >
                  $PROP = new URLSearchParams($WINDOW. ...
                  .location.hash.substring(1)).get('...')

                  ...
              - pattern-inside: >
                  $PROP = new
                  URLSearchParams(location.hash.substring(1)).get('...')

      ...