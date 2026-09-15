---
title: Codex，5 步装进你的电脑
url: https://mp.weixin.qq.com/s/l6lJChspUfQi0uT1mYnNRw
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:57:24.125054
---

# Codex，5 步装进你的电脑

# Codex，5 步装进你的电脑

红客攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrqpKaYWibGDsAibf0Xpal1kquEwgbYPQAMV8HjzRAAOUY2bFDd6oECL8TXDVGgojBfwgxMMcO0Vlyic2TkWNcHSowiaoUBgVuKoMibo/640?wx_fmt=png)

装Codex，装的过程比想象中麻烦

首先，我的Codex不是从官方下载的，从某项目网提取出的文件，然后整理成打包的安装文件，**支持windows和MAC**，跟官方安装包相差无二，

为什么需要配置？

因为Codex目前不支持太多中文，需要自己去借助一下外力，还有其他插件，如果你想安装，直接后台私信

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVroVWiclK506PJhodGPASVydmMF7IicCE0iaWpwZZx92EtVMJuTiaFP9rR7yXzH1pkmoQMNH8sp8yPTic4wZDB9G6icMKUiaddPRBxLPbg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVroOF5H40OSA1O7Uu6dsibZ7sDZ1ZROld8c7fOiaibklMsBJEfLe7PoBIdN0SPPTvjiaVe8WPZhWDXpQzcqtGiadHhWYB5RSXRpFgZiac/640?wx_fmt=png)

也可扫码 直接找我要

Codex 是 OpenAI 出的命令行编程工具。装完之后，你在终端里打一句话，它自己去读你项目里的文件，然后把代码改掉。

和 ChatGPT 的区别在这儿：ChatGPT 给你一段代码，剩下的复制、粘贴、改路径、处理报错，都得你自己来。Codex 直接动文件。

所以它适合的活是那种「我知道要写什么，但懒得写」的。批量重命名、按格式整理数据、给老脚本加个参数——这类事它干得挺快。

反过来说，如果你连需求都描述不清楚，它也帮不上什么忙。这个后面会讲。

**我拿它干了什么**

说两个具体的，免得听起来太虚。

第一个是归档脚本。我有三百多个日志文件，散在十几个目录里，想按日期重新整理。以前这种活得摸半小时，那天我把要求和目录结构描述了一遍，它写出来大概四十行，我改了两个地方就能跑。

第二个是排查老脚本的报错。以前得一行一行看，现在直接把报错信息贴给它。不过这个不是每次都灵——它改错了方向，连没坏的地方一起动了，最后只能 Git 回滚，重新描述一遍需求才弄对。

所以也不能指望它一次到位。它的价值在于省掉那些磨人的基础劳动，它不会替我们做判断。

**安装，五步**

**1.**装 Node.js

去官网下 LTS 版，双击一路下一步。Codex 依赖它，版本别太老，18 以上都行。装完开个终端验证：

```
node -vnpm -v
```

两行都能显示版本号，就可以往下走。

**2.**装 Codex 本身

Windows 打开 PowerShell，Mac 打开终端，敲一行：

```
npm install -g @openai/codex
```

国内网络这一步可能要等，卡住不动就换个镜像源再装：

```
npm config set registry https://registry.npmmirror.com
```

**3.**确认安装成功

```
codex --version
```

能打印出版本号就算成功。这一步没输出，问题基本都在第 2 步的 PATH 上，往下看报错那节。

**4.**登录

直接运行 codex，它会弹浏览器让你授权，登录一次以后不用再登。

**5.**建个单独的目录再试

这一步很重要，它会改你的文件，所以第一次用找个空目录：

```
mkdir D:\codex-testcd D:\codex-test
```

然后随便给一句需求，看它怎么干活：

```
$ codex "写个脚本，把这目录里所有 txt 文件按行数重命名"
```

**常遇报错**

**1.**codex 不是内部或外部命令

装是装上了，但系统找不到它。先关掉终端重新开一个，多数情况就好了。还不行，执行 npm root -g 看全局包装在哪，把那个目录的上级 bin 加进环境变量。

**2.**装到一半卡住，或者超时

网络问题。换镜像（上面第二条命令），或者挂个稳定的网络环境重试。这种情况换时间重试也有效，不是你的操作错了。

**3.**登录的时候浏览器没反应

终端里其实给了个链接，手动复制到浏览器打开就能完成授权。

**4.**Windows 下各种权限和路径报错

这个最烦。Windows 属于实验性支持，官方自己都建议用 WSL。我试过两个办法：一是不在 C 盘根目录、桌面、下载文件夹里跑，换到普通项目目录就正常了；二是干脆装 WSL，虽然多一步，但后面省事。

**它不好用不好用？**

网上吹嘘成分比较严重。网上讲 Codex 的文章大多只讲好用，

**一，**Windows 支持确实一般。前面说了，官方标注是实验性。Mac 和 Linux 上顺很多。

**二，**它会改文件，而且改的范围有时候超出你的预期。你让它修个 bug，它可能顺手重构了几个函数。用之前先提交一次 Git，改坏了能退回来。这个习惯比什么都重要。

**三，**需求说不清楚，它就自己猜。你说「优化一下这个脚本」，它只能按自己的理解重写。说得越具体，返工越少。我通常会把「要改哪、改成什么样、不要动什么」都写进去。

**四，**它不是免费的。需要 OpenAI 账号，用量受限，具体额度看你自己的订阅情况，别听信「完全白嫖」的说法。国内访问稳定性也一般。

**资料**

我找了一些现成的安装包、图文教程、常见报错处理资料。
不过上面五步自己照着敲也能装，装的过程中卡住了再要也行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrph1ukhhAruAJkWNqGVoNKrybicDFc0qw7f54tF69htWtYan0jaLeiaptIDSUVDU7zxnGetzMm9bqUicEHJibgcNW8xtPH8PoXk2Ys/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqdXDuLu99iajUVcokqyyoNqFXGiadVUNK9EibCNAo4bsiakIs5swU9TxealMAjm3l20USB2dQbnU8ukiaHL9Jxt3eQrd95M7u5Nmek/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqcsbcZqmMfQQ8uibjj3PX4WuxgKy9UVyR0OfJB2yuuw1kzR9uPArWKLse0mRpwZR5sDGZoFN7yj0iaT0OJAhtZclRf7sPOAMEl0/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqHSVgialCRKOGtZaaphVv6lbAtEhKiabdhYBsln1NOWwoxk8ApgmjOZMsU2ZCVjy7TYKhW13LtY1jbG3SXZpZ53uic1w63Qsbthg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVroxOEhTUKI60ia403Usic9ThCKia4iaJPicXbibncmiajAgk6xh8AyLvqTbEBPIAp6r0e8Usr8MicMwjg4FuxesbvLYl2ZTRLUjibK6xYibc/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaPh0yKxE5zleqvXBjCQSwl3YRSgLDiaCJs6thgE7HAEN9bHD2ph3Mg2c349icibwQIyTx6mIvbL2Liatz4PdfGiapVg/0?wx_fmt=png)

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