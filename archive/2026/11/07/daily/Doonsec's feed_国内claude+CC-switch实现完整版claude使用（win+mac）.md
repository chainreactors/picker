---
title: 国内claude+CC-switch实现完整版claude使用（win+mac）
url: https://mp.weixin.qq.com/s/ovEDPs7ybBlOgaUVACTSig
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:08:00.757494
---

# 国内claude+CC-switch实现完整版claude使用（win+mac）

# 国内claude+CC-switch实现完整版claude使用（win+mac）

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

国内claude+CC-switch实现完整版claude使用（win+mac）一、物料二、下载与配置1、claude code desktop下载2、boluo中转配置3、CC-switch配置三、claude配置四、mac配置的区别

## 一、物料

**CC-switch** 官网下载地址：https://ccswitch.io/zh/

**claude code desktop** 官网下载地址：https://claude.com/product/claude-code

**菠萝中转站** 这是我自己用的一款认为非常好的中转站，各大模型都支持，具有多种分组，支持不一样的级别和消耗，地址：https://boluotoken.com/sign-up?aff=d3W5

## 二、下载与配置

### 1、claude code desktop下载

首先判断是否需要安装使用CLI，如有需要，先安装npm，访问：Node.js — 下载 Node.js® 进行下载，选择带有LTS的版本，比如：

![image-20261107222428763](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib22wZrxNQn8tTHiaibJHEgmrMhkpc2icth5BIHe1ye5Tibkp2u9SExYlQibMsKuWf8RmaicQhXib4rrX4LIHuZYmQg1Jicj7EBNEic9cP1M/640?wx_fmt=png&from=appmsg)

然后按照他给的命令执行即可，如果报错不用怕，切换上面的使用选项更换下载命令重新尝试即可，如果尝试2-3次都会出现不正常的信息，那就不用管，继续下面的步骤就行。

完成上面的之后，则直接：`npm install -g @anthropic-ai/claude-code` 即可，完事验证一下 `claude --version` ，如下：

![image-20261107222113521](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib05ibOjCM2jtsFdGtDicDq3naRTdJFk1GHiba5ChzSexjd0GQ1ibmmCLGal8HUXJ8EqYticBeF8jVDvIhHD75QbiaN8RTdSsYSDsdyAs/640?wx_fmt=png&from=appmsg)

接下来安装桌面版的agent工具，首先做好代理（部分地方无法下载），然后访问上面提供的**claude code desktop** 官网下载地址，win和mac都一样，点击download即可。

![image-20261107221439855](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib0P1FicDEJyLqj55icSZXvbwWibrlcMMicxQicZDLewME9xibW8pQAgZ89VCWLxib72G8kaX8Dt0MtgbeMXm3SZyBRsWRgXA3CQgE7lTA/640?wx_fmt=png&from=appmsg)

如果不代理节点是不允许下载的：

![image-20261107221626630](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib0icNRILicMPgwSjBXgibKGgjxrKia7U26X8ndejicZej4bjWIU0m8zbNJrIM7yLbIa9RzdxKnzZxA5x02TKBibPmYmxRwFQsapYgshM/640?wx_fmt=png&from=appmsg)

下载好之后双击“Claude Setup.exe”安装即可，安装好之后就不要动了，彻底退出claude。

### 2、boluo中转配置

点击这里boluo网站 进入，直接使用github登录即可。进来之后进入API密钥界面：

![image-20261107223052468](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib2zKb63NdKjBjWASzjOLia2KokqWS8gjuNQuXFA1SdibhBU5Qm8icYDTsvFAkFLKf8mjQsDeumCg6hQogLq3TCbiaJTe1yIIEB3Uhw/640?wx_fmt=png&from=appmsg)

点击右上角“创建API密钥"，其中名称自己随便写就好，分组选择“claude-kiro”，如图：

![image-20261107223155002](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib1mNTDZfzlV3bNEc6GuXT4a86Mv6FN2l1tw71HAGkkVwyFlf7ZB1m0qMXNe02ZEwl8tLouEAFRcUfN5VF1NPCzicSvz9NzqDWao/640?wx_fmt=png&from=appmsg)

然后保存更改，此时会出现一个分组，就是你刚刚申请的，然后去充值token，在钱包页面

![](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib1lJCA29ibcPnBmXsYiblibBGCPu5I68kmvo6icWWr6ASHTicEfZAcRpRoL4uHxcjicgTEgypJlibUbVclK7a53TYWO4YAL2CzM50NOg8/640?wx_fmt=png&from=appmsg)

72rmb，可充值200刀额度；180rmb，可充值500刀额度。充值好之后就可以进行下一步了

### 3、CC-switch配置

CC-Switch是款免费的开源工具，它可以提供傻瓜式的界面，让我们自由切换模型，集中管理各种AI工具。安装时选择想要安装的目录即可，安装好将其打开。如下图，刚安装好的只有每个模型默认的官方模型供应商，下图是我修改配置了一些信息之后：

![image-20261107222718615](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib2P92hJTdoDkico5h7ib2bKdtcZu854z4c0oumEg6rHoAvSV0hCLIEicUypicdNiamJCnXqgvF1Liapk3v9FVFvrKnyxOsvQb9TAQ4O4/640?wx_fmt=png&from=appmsg)

我们可以看到，**这里有两个选项，分别是给cli和agent版本做的中转，如果没有下载cli，则只用配置Claude Desktop，如果下载了cli，则二者都需要配置**。这里用下载了cli的来展示。

复制boluo里的分组API密钥，在CC-switch界面选择Claude Desktop，并点击右上角添加供应商，然后选择“自定义配置”，则可进入如下界面，并按照如图提示填写：

![image-20261107223742831](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib3mK8Og22eVCetLXibF5mal7P5U1CgNQvLbFXTu9vhdPdicic1LSBB5O2WXGANLibiaGSpxKxBnULTFNIpGDibAKx8WOibor86CJ2lRhA/640?wx_fmt=png&from=appmsg)

填写好之后，点击下面的“获取模型列表”，然后添加你想用的模型即可，这里是原生Claude系列模型，默认选择“直连”即可。

![image-20261107223902716](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib06wWqicwCx2PNP9mRJkQdIum0ULvIsmudorCTQbHEy5cSib2Tiatjgy7GsAu5iapxCrVJa8ibRvdJwNbw9SAy3m2Ht070V2HZXDbu8/640?wx_fmt=png&from=appmsg)

完事之后点击保存。

接下来再在CC-switch界面选择Claude Code，重复完成上述配置即可，不一样的是，claude code配置需要做模型映射，配置为如下即可：

![image-20261107230227830](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib3P7R7dgBq7WwyI0rE7ca9IXDSnlEqnNSycOfGen0CEXYkfwI9n46ljYsvaOXBa3yuvicvNM8XcsBuHP8XeST7Nib2enqRWRM4h4/640?wx_fmt=png&from=appmsg)

配置完成之后给两个配置都打开路由：

![image-20261107224105364](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib09Uh2icoLxhXOc0iallwRMbWiaKKe16phOmk2XKYH9fOuqnwX4b7ljMqCFcWs3oL2zXcu4NCKxEQLGoO3sJ3Hcm6sCFAErljcIVg/640?wx_fmt=png&from=appmsg)

再进入“设置”检查一下，路由是否为 本地的 15721 端口

![image-20261107224146528](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib2JqWKXr75YJUkPK8Wndujibsp9jbZYtZK3u4sIsRiciassOcRFRGrOAxKTGd2XxBncw9bBFpyfGsqWcZBDaJpKZicx2AbuYG9cXVk/640?wx_fmt=png&from=appmsg)

## 三、claude配置

初次打开应该会直接进入这个界面，不用你再尝试登陆。

![image-20261107224337515](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib21UJ9gNwNVQj6hdrqJjcTgCrxkk6jFiaUjknamnla5dEzicibD83Sn56DD7tic8KWlMIPDYnvMsUSqpcOdW2LblVT67ZoPOXiaYicRc/640?wx_fmt=png&from=appmsg)

但是现在还不能直接用，因为claude自身原因，这里不展开了，需要配置他的网关路由，点击界面左上角的三条横线：

我这里是汉化过后的（下面会将如何汉化），所以看起来是中文，英文步骤为：Help → Troubleshooting → Enable Developer mode，在帮助的里面有一个打开开发者的功能需要打开，此时应该会重启

![image-20261107225111468](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib2jW1CSAfYGwBJJlsyHLOlqxmNrzHxN2RzpJVicWO6mMo0d0iabnibPV2PNpKk2UibXricrO4hfEsiaC0EuibU52ibRticibhExF4PC6wFoc/640?wx_fmt=png&from=appmsg)

再次打开之后就会和下面这张图一样出现一个开发者的功能：

![image-20261107225153546](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib0Tw7jLnIh3VIIB3BGcqDibrfARniaOniaUnRoSjqIfWSZtLiagOTJpmLsb5rCzDPCTBeUqmyibuhfq85oogFOFypFCOOrnccg2YCrc/640?wx_fmt=png&from=appmsg)

接下来我们就要进入开发者里，Developer → Configure Third-Party Inference，选择Configure Third-Party Inference，在我这里中文就是“配置第三方推理”，他会进入一个操作面板，需要在里面按照如下配置：

```
 Connection:          Gateway
 Gateway base URL:    http://127.0.0.1:15721
 Gateway API key:     PROXY_MANAGED
 Gateway auth scheme: bearer
```

![image-20261107225404072](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib3ibjPjrYhlNBnEBibYYLzDY5RtFxjrYib70qDC0AHQdWl6FY8IxqeF7T919dOlAVQhEGEkhFjhuWbSjQYgf5O8YZNWqOZnpAQAx0/640?wx_fmt=png&from=appmsg)

填 `PROXY_MANAGED` 可以让 CC Switch 完全托管密钥，切换供应商时自动跟随。也可以填你自己的固定 key，但切换供应商后需要手动改。

往下滑，就可以看到刚才在cc-switch中配置的模型：

![image-20261107225418666](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib08bNqO1eliarc6flicw7cGneJ57PyHYuiaia8F2gxG30IcOVMwrjPzkJjRH6MqkddibyL7aCQUHHybr4CXUdPG9YdkV520FCPlT3f8/640?wx_fmt=png&from=appmsg)

点击save and 重启，他会自动重启，此时就不会再报错说当前模型不支持使用了，就可以正常使用了，其他操作和codex差不多

![image-20261107225614696](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib1eicfR7Cq0zicPMPibxiaegyH1dQ8vNkibMtk7ePjk1P15ZEFeASEWB5KuEODuJdbicW5GHZRRBBte9DKib3bCUAnziclgPGx2NhsVRjc/640?wx_fmt=png&from=appmsg)

## 四、mac配置的区别

mac的下载和配置整理下来大致步骤和上面都是一样的，只有cc-switch配置有点不一样，如下：

mac确实有点和win不一样，我在操作时，mac会遇到cc-switch中的claude Desktop配置无法路由，但是Claude Code支持路由：

![image-20261107230013598](https://mmbiz.qpic.cn/mmbiz_png/vCc73Oa3tib1TXnAwpibm8icyMt1MG79MtIuzjgmHVKSzNcjdBYtAJsdRWOjDa8kmdcgiclBeFwsNibl9GgV2ZG1uysVtOIeTFIc4GOJ1DIX6OvU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib268d6vlwDclohcbNOiaE49oK8X6Y5ib9lzdzgerkwIblI3GrNJCicPH5XZolDcfM2xtJr551KggNR1WcqKcgrgpRT7xZBLtjvoPs/640?wx_fmt=png&from=appmsg)

此时只需和上面一样，把二者都先配置好，然后给claude code配置做好路由，claude desktop就默认保持直连就好。其他没有什么不一样，完事之后mac也可以使用啦：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib1XWb77WOHJpF3hSQEC4HbUnibUiaxlVRu6911iaqJiaAOuVIIib5m3C26LZFKZTY4EsnBAnrmiccfgrkqUYqYyt8qg20ibq7qNdHKlHA/640?wx_fmt=png&from=appmsg)

此外，我们还可以将多种模型接入Claude和codex使用，比如deepseek接入codex和claude，详情参考：[https://mp.weixin.qq.com/s/i2nV0bpUg2S8JNj7AdcOpg](https://mp.weixin.qq.com/s?__biz=MzYyMjI3MDQ3Nw==&mid=2247486780&idx=1&sn=1165ec1a531e65c672ce6540f09b4629&scene=21#wechat_redirect)

学会上面的内容之后，我们可以在任何一个agent里，使用任何其他模型，比如coedx里使用grok、coedx里使用claude等等换着来，比如：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vCc73Oa3tib2D4k2xHmUO6MV2dhhiayIIleEjzl3IkSUAFhRHmtDxtYZDVlRDKictGeHMAjyz1qUBuae4PMtUVAtPJE13zsYF7WUj6ncddhp48/640?wx_fmt=png&from=appmsg)

加油吧骚年！

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

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