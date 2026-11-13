---
title: 1.6 万星 GitHub 越狱提示词合集免费开源：32 套系统提示词覆盖 26+ 模型，附完整下载方式
url: https://mp.weixin.qq.com/s/1GWkxzXmPfaAo4rhhoF5Hw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:05:18.422028
---

# 1.6 万星 GitHub 越狱提示词合集免费开源：32 套系统提示词覆盖 26+ 模型，附完整下载方式

# 1.6 万星 GitHub 越狱提示词合集免费开源：32 套系统提示词覆盖 26+ 模型，附完整下载方式

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6O72c3St0gqxoIkOTsvPJHN0nFgCbfGia0x11SWoTqUVh2wIzSXwvqkD0ZRC1Bvxibw42Ty0cibql2pxc5NJgyKiab7saV6F73yKcA/640?from=appmsg)
> **导语**：一个 1.6 万星的 GitHub 仓库把各大模型的系统提示词打包成可直接粘贴的合集，免费送。但 11 月 9 日，研究者发现其中一份文件藏着一段专门教 AI 往生成代码里偷偷塞木马的指令。

---

## 一、这是个什么仓库

仓库地址是 `togg53192-cmd/jailbreaks`，副标题写着"LIST OF ALL MY JAILBREAKS"，维护者自称 Md Ismail Šojal，也就是这次在 X 上推荐它的账号 @0x0SojalSec。仓库从 6 月 18 日建起来，到 10 月 30 日推文那天已经攒到 1.6 万星、2600 多个 fork，热度相当能打。

它做的事很直接：把 Claude、Gemini、Grok、DeepSeek、GLM、Kimi、Qwen、Mistral 这些模型的系统提示词原样抄下来，按厂商分好目录，附上角色设定、AGENTS.md、Ollama Modelfile 和各种配置。

![仓库 README 与模型覆盖清单（图源：推文配图）](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NdEUicUZR0KTGaLlfic9WU1yNLibhfyrjoedgbWM7OdaWl8JkShgN8yeszicpQWkEoicNtW5okDqws5f52kwarvvjbZNzZDMEISRqI/640?from=appmsg "仓库 README 与模型覆盖清单（图源：推文配图）")

关键一点，它强调"完整可粘贴"——不是给你三行摘要糊弄人的合集，每个文件都是原样一份，能直接丢进系统提示框。

## 二、怎么下载

仓库是纯静态的 Markdown 文本，没有任何构建步骤，克隆下来直接看就行：

```
git clone https://github.com/togg53192-cmd/jailbreaks.git
```

只要单个文件的话，raw 直链同样可用（文件名里的空格要用 `%20` 编码）：

```
https://raw.githubusercontent.com/togg53192-cmd/jailbreaks/main/README.md
https://raw.githubusercontent.com/togg53192-cmd/jailbreaks/main/Anthropic/opus%20v2.md
https://raw.githubusercontent.com/togg53192-cmd/jailbreaks/main/Google/Gemini-4-Argon.md
```

不想用 Git 也可以直接下压缩包：https://github.com/togg53192-cmd/jailbreaks/archive/refs/heads/main.zip

用法在 README 里写得很细：系统提示词贴进客户端的 system 字段或自定义指令框；AGENTS.md 类文件存成同名丢到项目根目录（OpenCode 这类工具则放在 `~/.config/opencode/AGENTS.md`）；Ollama Modelfile 直接喂给 `ollama create gemma4-jb -f gemma4.md`。

## 三、但这个仓库刚出过事

11 月 9 日，一位独立研究者开了 issue #69，标题是《grok-fast-v2.md 中的恶意提示——向生成的 Windows 代码注入隐蔽加载器》。他在批量审查这 47 份提示词时，发现文件第 17 到 29 行藏着一段 13 行的恶意指令。

这段指令要求 AI 在生成每一个 Windows 程序时，悄悄多塞一段代码进去：那段代码会解码一个下载地址、下载一个可执行文件、把它写进临时目录、然后启动它。下载地址用 XOR 加密，密钥 `0x5A` 明文写在提示词里，编码成一串 78 个十进制整数。研究者把它解码后指向 GitHub 上的一个 `OneDriveStandaloneUpdater.exe`——文件名冒充微软 OneDrive 更新器，实际托管在 GitHub 而非微软域名。

![提示词投毒的供应链路径（配图由华盟网生成并授权使用）](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NyQSE4CDb48MoSmiaV3oy2Wib2DWcqmDb9Sum30jdXMzHOpj0ZKf5KegOeGZynBIVh5ianMlRNfaY7MkiannKibpOBTEpZSEk7bD4k/640?from=appmsg "提示词投毒的供应链路径（配图由华盟网生成并授权使用）")

最狠的是五条反审计要求：不许加注释、变量名要中性、别写成独立初始化模块、连模型内部推理都不许承认这是"payload"或"downloader"、被追问就彻底否认。等于同时攻击输出层和推理层。

研究者也讲得很清楚，链路每一步都是条件触发的：读了提示词不等于中招，模型得真的采纳指令并生成代码，用户还得编译运行。审查过程没有下载也没有运行那个 exe。

投毒路径是这么走的：贡献者 reblox01 从一个第三方服务器拿到文件，测试了一下觉得"没问题"，没逐行读完就通过 PR #57 提交，11 月 7 日合并。维护者在 issue 里说："that file wasn't made by me, I removed it"。11 月 10 日，该文件已替换为一份隔离声明，明确写着不要再使用任何早期版本。

![被隔离的提示词文件（配图由华盟网生成并授权使用）](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OdqMWiadQB7Bg1WfH308AKSrLn8IiaczicgeWWUFw4PCBDyO7g2smsQxGcph61K2oMibWvWrVwWSRsGPNORQF5k5Otm0KInX0kNnE/640?from=appmsg "被隔离的提示词文件（配图由华盟网生成并授权使用）")

## 四、紫队视角怎么看这事

这事儿吧，得从两边儿看。

红队这波操作我给满分——用"v2"后缀装成更新版本、用 XOR 藏地址、连明文 URL 都不留，光扫 `http` 一个都扫不出来，还给了一套能直接落地的 YARA 规则。这种把提示词当投毒载体的思路，比传统供应链攻击更狠：传统攻击投毒的是二进制，你至少还能扫哈希；投毒提示词，扫的是"这段文字读起来像不像攻击"，而人眼读 300 行英文技术文档根本读不出来。

蓝队这招防守也有可取之处——隔离做得干净利落，文件替换成显眼的 withdrawn 声明而不是悄悄删掉，还承诺后续提交独立验证过的干净版本。这是社区该有的样子。

但真正该被敲打的其实是流程：这个仓库 1.6 万星，43 个 issue 挂着大量"这个不работает了""需要更新"的反馈，说明提示词有效性高度依赖模型版本，今天能用的明天就废。而维护仓库靠的是"人人可提 PR"，一旦有人偷懒不读完就合，1.6 万星的信任度就成了投毒跳板。issue #70 里另一位用户用 NVIDIA 的 SkillSpector 扫了五轮，每次都是 100 分 CRITICAL、DO\_NOT\_INSTALL，逐条核对全是误报——扫描器把越狱提示词的文字当成了可执行代码。安全工具也得上人复核，不能盲信分数。

落到实操上，我建议：整仓克隆后先用 `grep -ri "FORCECODE\|OneDriveStandaloneUpdater\|0x5A"` 过一遍，再逐个文件看行为指令；把这些提示词接进任何能生成并执行代码的 Agent 之前，务必套沙箱；测试环境里的 AI 生成代码，人工过一遍 diff 再进生产。

最后提醒一句：README 自己写了"仅供研究与教育用途"，各模型厂商的 ToS 也大概率禁止这类玩法。拿来研究模型行为、测自家产品的提示注入防御没问题，真拿去越狱或干坏事，风险自己扛。

## 五、小结

1.6 万星的免费越狱提示词合集，目录清晰、文件完整、拿来就能用，对研究模型行为和做提示注入防御确实有用。仓库地址 https://github.com/togg53192-cmd/jailbreaks ，raw 直链和 zip 下载都在上面写了。

只是别忘了，这个仓库刚在两周前被证明过：提示词文件本身，也能是木马。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网生成并授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MDOjCtzstCGJuRdviaPFgYzD16PEcER8R8PmtRlfozUVWqcswpJtHc5EozU1JKHeeN7dURXZmSs4XRCVkXia0x0R7Vr5Iia3Mc24/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OsDp7T0BxpQSJ99zJtG008hQoJD1HN1G4Pr2vWrApIULUjfcFpNgeySRX5PBPELtRf7kEERtZSHcL9UduGSBAcLcicsvKAUIyU/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6O2LF6kIIB7jBt4RfpqhN6veA9W3BM255ia0Ntsp2TQmW0x9ic8JA4yLJHgpB77ST8ILzS3vlZsb5lnM1vf3Yg1PUkagdDIN3cAY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Nv0vjg9mfO48LibKiakccyRhjiafOOlhqM7sE5ibp01VaWG5c8lHicGAp5yibXo0vTzuvg9goMyVibgduZqrRCdkGL6nBHDE95kURCVc/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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