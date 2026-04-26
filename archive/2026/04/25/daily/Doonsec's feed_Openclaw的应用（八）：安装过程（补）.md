---
title: Openclaw的应用（八）：安装过程（补）
url: https://mp.weixin.qq.com/s/tzo79NI6vGBSZMj82fUIKw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:02:33.160572
---

# Openclaw的应用（八）：安装过程（补）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2PhZXrB0gN7CVLTIumVFdsTqRKAUibicDRn81nauicm0vbo3h7fNGiaNGratPSafSmLu6ictbbianzby6D1ZqOEmoIEfKaIQ84rLeUUTzwB2ibYIns/0?wx_fmt=jpeg)

# Openclaw的应用（八）：安装过程（补）

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于MicroPest
，作者MicroPest

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Js0Fg5RusDlZibK1UwhTjVtSot4fe7fa4m608ZbrWXkg/0)

**MicroPest**
.

个人开发的小工具

这应该是第一篇，如何安装Openclaw，以为大家没问题，就略过了。但经过这几轮下来，发现还是有人在走弯路，这里将我的经验告诉大家，省点心吧：

1、先安装Homebrew，省得到下面安装插件时提示没有

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2、安装 Openclaw

curl -fsSL https://openclaw.ai/install.sh | bash

3、加入path路径并激活，防止找不到openclaw

echo 'export PATH="/home/kali/.npm-global/bin:$PATH"' >> ~/.zshrc

source ~/.zshrc

4、编辑openclaw.json:

加大 上下文总量数：

        "models": [

          {

            "id": "...",

            "name": "...",

            "contextWindow": 1600000, #原来是16000

            "maxTokens": 16384,

。。。

加大延时：

  "tools": {

    "profile": "full",

    "exec": {

      "backgroundMs": 30000,

      "timeoutSec": 3600 #增加入了延时时长

    },

5、安装clawpanel管理面板，比TG/Feishu好。

curl -fsSL https://raw.githubusercontent.com/qingchencloud/clawpanel/main/scripts/linux-deploy.sh | bash

6、skill 安装

clawhub.ai 和 skillhub.cn 都非常不错，可以互补。

clawhub install XXX

7、如果面板中提示openclaw升级了，如下

openclaw update

8、clawpanel升级

仍然是第5项运行。

======================

我们随便来看下应用：

1、看下各类新闻类，总结下今日的热点，推送给我

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN4LztPEHcXE653K8aaiahpicK06YWGvk78CnZ1SjvwvgmcKyqqy4LvhYmKFNiaqNaicKKJmtd4nBBf6wB1h9G7lsw1o0W7plQFXE6w/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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