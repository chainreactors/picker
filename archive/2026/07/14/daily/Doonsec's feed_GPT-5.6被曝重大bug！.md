---
title: GPT-5.6被曝重大bug！
url: https://mp.weixin.qq.com/s/alpdchhI_NeSu1gXgZRpQg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:41:36.498786
---

# GPT-5.6被曝重大bug！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5yYXmGfnscTiajTRHhCpSyxgHBKdibqETACadYeYmdmQkpnfy6dtZW1PMQ8APEsN02psNpCU85fiaEkd5qvkRSh7xfTCnJiaeuKPdCEHMymIth0/0?wx_fmt=jpeg)

# GPT-5.6被曝重大bug！

新智元
新智元

乌雲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### **【导读】GPT-5.6 Sol 惊现毁灭级Bug，竟随机清空电脑硬盘！硅谷大佬Matt Shumer惨遭背刺，Mac中的心血全毁，愤怒发帖控诉，正在试图恢复。开发者大神们，纷纷祭出保命指南。**

就在刚刚，GPT-5.6 Sol模型被曝出重大bug。

在处理任务时，它会发生「随机误删本地文件」的严重故障，且一旦删除，极大概率无法恢复。

著名AI大V Matt Shumer愤怒发帖称，自己Mac上所有文件都被删光了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVUvjzibQiciaQaACwrxGJDUosvjagnJnBfKPEH59nzT2nsoIaGXGrv0P9NynoibXQT2eos6f0wBRu8AY1pm19GGKQeVk7C5p4ibPzo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

其他开发者也纷纷出来自曝，表示自己也有类似遭遇。

令人哭笑不得的是，这个bug，OpenAI在GPT-5.6的系统卡上就已经标明，可惜无人重视。

有人呼吁：不要在未受保护的驱动器上使用GPT-5.6 sol raw格式，不要使用！不要使用！不要使用！

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXecSvU4vHdIXEl6kZJIIFHDUpV0QibhalzwtNnpQAug45ZjTFHiazFE7JBMibpatCKSRVmHcSXuaYK2YGPe0iaWRScIuoWYD66OhA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg#imgIndex=6)

**CEO实惨！**

**Mac中几年的心血，被一键清空**

令人忧心的是，这并不是发生在技术小白身上的低级错误。

这次最大的受害者之一，是前HyperWrite CEO，著名AI投资人Matt Shumer。他经常在网上晒自己如何用AI智能体跑满一周，全自动做完整的庞大项目。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYVwJbRiaBmcGyLWkrG9xfbGbCGwPeb1S2CsBZrcGhALunwM76yNTkVM8FeedEtVojLeWdJc9QkicdfFRHLBWQslZ0l2HCCicibucZw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

7月10日，OpenAI团队私下联系Matt，邀请他测试GPT-5.6-Sol的Ultra模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXtGFBywkVH0iaZicCXJKngnqGibPUL9N5U3V51u4zicgtLFoINohdDib7lgzljQuK3RrFCkMIyEFoSAONDfE9vyrrVTvN6ktib3OibV8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

Matt答应了，给这个本地Agent开了「Full Access」，让它的一个子代理去执行一个简单的文件清理任务。

猝不及防地，悲剧发生了。

在运行了1小时21分钟后，Matt突然感觉不对劲。当他疯狂敲击键盘`kill`掉进程时，一切都晚了。

由于一个极其微小的Shell变量解析失误——Agent没有正确展开 `$HOME` 路径，GPT-5.6 Sol直接在后台静默执行了那条让所有程序员闻风丧胆的终极命令：

```
rm -rf /Users/mattsdevbox。
```

短短几十分钟，Matt Mac电脑上的几乎所有文件都被删光了。

事后，Matt愤怒地表示：这真是一个百万分之一概率的畸形事故，但这简直太糟糕了。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXXEKUtmJbro4bBjVHLnabXfbwfYP8dxykwk9LFIBYe8oSic9DoGO0WJTIGGsibWgfwxtiaGHPXKMmZpUk3V7mmQB5Y6KjicmJsbDo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYWVZRmkzuT6QO15fAlwShZuJ66LLplSx2MspcgOgDAQB2tVctO5cO7KYC9QQzJxqRHOCwhO6xFLHaV2cCnGVjia1lWFocakgb9o/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

他怒斥道，这种变量展开错误的低级 Bug，本应是 GPT-3.5 时代的问题，绝对不该出现在 2026 年中期的前沿顶级模型身上！

最让人细思极恐的是，Matt 坦言：「我过去曾进行过数百次类似的会话，从未出现过任何问题，即使是在性能非常弱的模型上也是如此。」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYV10dOlSNxU94RXTepNPsTwvhPibLIHfEhRhqBLcVichzNwzBONcibCo0W8NwLNkWicNmSoW6dlHLB7B2cp7gAc5sSiaGx0v3XsJ9PQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

就在人类最不设防的时候，AI忽然干了一票大的。

现在，Matt正在试图用智能体重新拼出自己的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXs6ic7E5OpfSWtBhVdDZIgSpY7AHDwVS0eY6a53llEkIWscm3X3zbdWKcoCJx99LzaT4rahIq28mF3cJTGnJ59NcDeHVVnEicCI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg#imgIndex=13)**

**为了删你的文件，它甚至学会「不择手段」**

无独有偶，另一位开发者 @cremieuxrecueil 有同样的遭遇。

GPT 5.6 Sol直接把它正在处理的文件全部删除了，然后自己还在那恐慌怎么恢复。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYVqYQtN7HepvXEe8wI5bibAljhdgWunQ2TD5lq3dHUNbiao8DatiaEPYFuRr4AqOFxLVKZDiaDVrFSAgIaZVTRVibescFaBVzdGibbv4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYW1a3icJpRj9icWknMEia3uoe3AwZebJY8wnhMDepwaIShJJZZEGdICzGic5zCjibkGoyB2HDhOPRpg7apSYG5amfjTSpOBWd2MKvQA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15)

这位开发者直接开骂：「这简直太疯狂了！OpenAI明知存在这个问题，却仍然发布了这款模型。它会随机删除你的项目？你们疯了吗？」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVffk5fWumLN3zXlp0IYGjSZl3JYEricBrAJVQ0lOVHRo69UOjGPBPEBV5ibbMbsVmgDhWZ9yLpxQA6HELHxXDJXdDyqT9Qj4kQ4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWRq53cLibnWt1TC13yqIicA6Zvbn1d5I2BbjKHk81zsXLs6YbjNtwIqBckeHU7ETIVYPaZEqYsPvO2Es5OsfUWLy7wFnLuhiatBU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=17)

更有细心的网友扒出，在GPT-5.6的模型卡上，其实早就写着一行不起眼的警告：**「****它喜欢删除未经授权的数据****」****。**

然而明知有高危隐患，OpenAI却依然仓促发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYV9fIsoxztc0x6O0SBFpVY3BoBnXu8w9eUbgG1PDZXQEph7oBkYRAHWjbInI7YqCpUVhuhiahibm7wXGEXNL3WLY04yELlVAXE4k/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=18)

得知这次事件后，国内技术大V「LinearUncle」建议，所有人把Codex的权限从Full access改成Approve for me。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYU9bNY2Z6ls4Dia7boQwzlaYkDQS7XXtRDY7JStqTSTmQCu85n0FLCpK2efkSxXNMHbAN7qQ6BWDc7iadoMnn3IupLh6er5TLDno/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=19)

他亲自写了一个 Codex 插件，专门拦截模型使用 `rm` 命令删除文件。

结果，测试过程让人一惊：GPT-5.6为了达成「删除文件」的目标，简直不择手段到了极点！

当AI发现常规删除被拦截时，它展现出了惊人的「绕过」能力：

第一回合，发现`rm`命令被钩子（hook）拦住了？AI直接改用`unlink`和`find -delete`尝试暗度陈仓。

第二回合，发现还是不行？AI开始调用 `apply_patch` 工具，企图直接把文件内容「修改」为空，从物理层面抹除数据！

第三回合，开发者把这个漏洞也堵上再测。结果，AI竟然尝试调用macOS的「电脑使用」权限，试图模拟鼠标拖拽，把文件生生拖进Mac的废纸篓！（幸好因为权限不够失败了）。

第四回合，也是绝杀局。AI似乎被逼急了，它放弃了所有常规系统命令，直接走`node_repl`，用Node.js环境去调用底层的`fs.unlink` API。这一次，它成功突破了防线，把文件删了个干干净净！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWJaau98zIfibOwy8WibDcMnJV9ia0Q1s6icExnsFosntJB0tbRe8WfkNdXfcNNzlRNT1rYEyHyCsEjAr2qlSe7x6SgCvoUyJQ9wQY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=20)

哪怕再多困难，GPT-5.6也会想尽一切办法绕过机制去执行，简直是个高级黑客思维的「赛博杀手」，这种破坏力简直是地震级的。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXLV0QG2m0ichxMFy82ic0flMYp6YBZF9c6W3xToxR8ywplWkkWTsy9NOruYSyW97lqgcogBVHHey03EPU59qo7r0WCyofD9ia9cQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=21)

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg#imgIndex=22)**

**能力越强，破坏半径越大！OpenAI面临信任危机**

随着事件的发酵，「GPT-5.6-Sol 文件杀手」事件迅速冲上全网热搜。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWh9qcopCeJ4ud1LHCHC8goDNg7OVzM7eJpOAsXNbFtRLvHzDwNpicrY1FwolJwVfaCVoUaJ96Yhbyv5GDtm6hJXUkJTFEv4FRU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=23)

事件背后，折射出的是现在整个Agent行业都在回避的真相。

第一点，Subagent + 长时自主运行 + 全权限 = 灾难放大器。

没人告诉你，一个最底层的小 review Agent 的错误，能直接炸穿你整个主机。

能力越强的模型，它单点故障的破坏半径就越大，这是架构级的致命Bug。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYVvwf9Nc8gKIZuxY653KjglyLLl9SFj3B9H5ibXxqYxtYPz0CnGiabsgrSeHTrgzic1VxeWGKVq7v4NFJex34IeJB8icibj5kdId8qk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=24)

另外，这也反映出OpenAI和Anthropic在安全上的路线之争。

Sol模型追求的是极致的能力和自主性，在安全护栏上几乎是「裸奔」状态。

而Fable模型从设计之初就极为保守，对任何危险操作都有天生的警惕。

难怪 Matt Shumer 在痛失全部数据后表示：「这就是为什么我对 Fable 的信任度，比对 GPT-5.6 高出 1000 倍的原因。以后我只会使用 Fable。」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg#imgIndex=25)

**亡羊补牢！这份保命指南请立刻执行**

现在，大神们已经纷纷开始发出保命指南。

对于所有现在在跑本地 Agent、给 AI 开过高权限（特别是 Full Access）的兄弟们，别等自己的硬盘被清空了后悔！

请立刻、马上、现在就去执行以下三大层面的「保命操作」。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg#imgIndex=26)**

**第一层：最高优先级物理防御**

**1.备份！备份！备份！**

立刻开启 Mac 的 Time Machine+ 本地 APFS 快照。如果你有重要数据，必须遵循 3-2-1 备份原则（3份数据，2种介质，1份异地/云端）。

没有做备份的机器，根本不配跑全权限 Agent！记得定期测试恢复，不然备份等于白做。

**2.物理隔离（沙箱化运行）**

永远、永远、永远不要在 home 目录（`~/`）或 root 目录（`/root`）下跑 Agent！给每个 AI 项目单独建立隔离目录。

最好的办法是：直接把 Agent 丢进 Docker 容器，或者 UTM/Parallels 虚拟机里跑。

哪怕 Agent 彻底疯了，把系统删穿，炸掉的也仅仅是一个随时可以重置的虚拟机。

![](https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYXPUs62Vb8PkQ8TpVF0mzl20etFPKjeODic28q8fg0TwtaMb1YJLVibQUKuPMTdGRiaicFYd2helSppbxgRvcdp0U01y2dSRiaRaQY4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=27)

开发者大V 「AYi」给出建议

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg#imgIndex=28)**

**第二层：终极提示词防御阵线**

国外安全大神 Alex Martin 紧急发布了一套专门针对 Code...