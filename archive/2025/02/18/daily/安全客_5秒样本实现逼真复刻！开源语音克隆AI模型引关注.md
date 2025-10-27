---
title: 5秒样本实现逼真复刻！开源语音克隆AI模型引关注
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787881&idx=1&sn=e59478758aa820931a73f3826fc11a09&chksm=8893bd86bfe4349053f9f6a8fba14473762349398034e238d7cfc9b0a285f0227a4dc7708583&scene=58&subscene=0#rd
source: 安全客
date: 2025-02-18
fetch_date: 2025-10-06T20:39:36.636078
---

# 5秒样本实现逼真复刻！开源语音克隆AI模型引关注

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4LovnrYpgT6KJicW2XXFUan47TVee60gLAVvmEMMSjZrnicicd7lyKhpNRQIje8ATBCv9jL6p3O92ng/0?wx_fmt=jpeg)

# 5秒样本实现逼真复刻！开源语音克隆AI模型引关注

安全客

近日，人工智能初创企业Zyphra发布两款开源文本转语音（TTS）模型，这两款模型具备强大的语音克隆能力，**理论上仅需 5 秒样本音频，就能精准克隆目标语音。实际测试中，用不到半分钟的录制语音，便生成了高逼真度的语音克隆效果。**

**01**

**公司背景与模型研发**

Zyphra 于 2021 年由丹尼・马蒂内利（Danny Martinelli）与克里蒂克・普塔拉思（Krithik Puthalath）共同创立，旨在构建先进多模态智能体系统 MaiaOS。公司此前已发布 Zamba 系列小型语言模型，并在技术优化上取得进展，如创新树形注意力机制。此次发布的 Zonos TTS 模型，是其技术发展的重要里程碑。

Zonos 模型的规模达到 16 亿参数，其训练数据来源于超过 20 万小时的海量语音数据。这些数据不仅涵盖了中性语调的语音内容，典型代表如有声读物的旁白，还囊括了各种 “极具表现力” 的语音样本。从语种分布来看，英语数据占据主导地位，同时也包含了大量的中文、日语、法语、西班牙语以及德语数据。Zyphra 明确表示，所有这些数据均通过合法合规的网络渠道获取，并未借助任何数据中介机构。

**02**

**模型架构：创新与传统结合**

Zonos 模型体系由两款不同架构的模型构成。其中一款采用了在当前生成式人工智能领域广泛应用的完全基于 Transformer 的架构，这种架构凭借其强大的并行计算能力和对序列数据的高效处理能力，在各类自然语言处理任务中表现卓越。另一款则是 Zyphra 自主创新的混合模型，它巧妙地融合了 Transformer 架构与曼巴状态空间模型（SSM）架构。

值得一提的是，**Zyphra 宣称该混合模型是全球首个应用于 TTS 领域的此类架构**，这一创新尝试为语音合成技术的发展注入了新的活力。尽管 Transformer 架构在当前处于主流地位，但随着技术的不断发展，像曼巴这样的新兴替代架构正逐渐崭露头角，展现出独特的优势和潜力。

**03**

**模型测试：效果显著但仍有提升空间**

为了全面、深入地评估 Zonos 模型的性能表现，研究团队选用了配备英伟达 RTX 6000 Ada 代显卡的专业设备，并在本地成功启动了 Zyphra 的 Zonos 演示程序。具体测试过程中，研究人员精心准备了时长在 20 至 30 秒之间的朗读音频片段，同时搭配一段约 50 字的文本提示，将这些数据一同输入到 Zonos - v0.1 的 Transformer 模型和混合模型中，在整个测试过程中，所有超参数均保持默认设置，以确保测试结果的客观性和公正性。

测试结果显示，**当使用时长为 24 秒的样本片段时，模型所克隆出的声音在初次聆听时，足以使熟悉目标语音的亲友产生混淆，难以分辨真伪。**然而，在向测试参与者揭示该音频是由人工智能生成的事实后，他们经过仔细辨别，指出克隆语音在节奏和速度方面与真实语音存在一定偏差，并表示如果音频时长进一步增加，他们有信心能够更轻易地识别出其非真实性。

**真人样本：**

**使用非混合模型生成的AI音频：**

在性能指标方面，根据 Zyphra 官方宣称，其混合 Transformer - 曼巴模型相较于纯 Transformer 模型，运行速度提升约 20%。在实际测试环境中，对于较短的文本提示，这种速度提升效果并不十分显著，但在生成语音的音质方面，两款模型展现出了明显的差异。**混合模型生成的音频在音质上更为精致，声音的平滑度和连贯性更好，**但从另一个角度来看，这种过度的精致化在一定程度上削弱了克隆声音应有的真实感，使得语音听起来略显生硬和不自然。

**使用混合模型生成的AI音频：**

在硬件性能适配方面，当模型在 RTX 4090 显卡上运行时，能够实现每运行一秒大约生成两秒音频的高效转化速度。而 RTX 6000 Ada 显卡，尽管在计算能力上与 RTX 4090 相近，但在将约 50 个单词转换为 18 至 20 秒音频片段的过程中，所需时间约为 9 至 10 秒。此外，值得注意的是，在首次运行模型时，系统存在约一分钟的预热期，在此期间，模型需要将相关数据加载至 GPU 内存中，因此不会立即输出音频结果。

**04**

**部署指南：技术要求与操作流程**

技术爱好者和开发者若想利用 Zonos 模型克隆自身声音，部署过程有一定技术门槛但流程较简便。需准备配备较新型号英伟达显卡的 Linux 设备，显存至少 8GB，6GB 显存设备也可能运行，但效果有差异。操作系统建议选 Ubuntu 24.04 LTS 版本，提前安装最新版 Docker Engine 和英伟达 Container Runtime，掌握 Linux 命令行基本操作。

具体操作步骤如下：

1. 通过 git 命令拉取 Zonos 代码库，在命令行中输入：

```
git clone https://github.com/Zyphra/Zonos.git
```

2. 拉取完成后，进入该文件夹，在命令行中执行：

```
cd Zonos
```

3. 接着，使用 Docker Compose 启动容器，输入命令：

```
docker compose up
```

需注意，根据不同的系统设置，在执行上述命令时，可能需要使用`sudo`或`doas`命令提升权限，以确保命令能够顺利执行。

完成上述操作后，用户可通过访问 “http://localhost:7860”（若为远程运行，则需将localhost替换为实际运行设备的 IP 地址或主机名），打开 Gradio 网页图形用户界面。在该界面中，用户可根据自身需求，灵活选择 Zonos 模型的具体版本，然后上传预先录制好的样本音频，或者直接在界面中进行实时音频录制。同时，输入需要转换为语音的文本内容，并可根据实际情况对诸如音高、语速等超参数进行调整。待所有参数设置完成后，点击 “生成音频” 按钮，即可获取由模型生成的克隆语音。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4LovnrYpgT6KJicW2XXFUan2XqyuLiaYrV8EBbIz2kft1VcwqX5qaAXul5fALZok8wsuPRwVibsOGGw/640?wx_fmt=jpeg&from=appmsg)

Zypher的Zonos演示程序内置了一个用户友好的Gradio控制面板

**05**

**广泛影响：潜在风险与积极意义**

如同其他新兴人工智能技术，Zonos 语音克隆能力带来创新机遇的同时，也引发争议和潜在风险。因其仅需极少量样本音频就能实现理想克隆效果，可能被不法分子利用，如实施诈骗、制造恶意骚扰电话、生成虚假政治信息等。随着技术普及，相关法律纠纷和监管难题已出现，亟待完善法律法规规范应用。

不过，Zonos 语音克隆技术也有积极意义和巨大潜力。在无障碍领域，能帮助声带严重创伤或言语疾病患者找回声音、恢复交流，苹果公司在 iOS 系统引入语音克隆技术也基于此考量。通过技术帮助残障人士打破沟通障碍，提升生活质量和社会参与度，是人工智能造福社会的体现。

Zonos 文本转语音模型的问世，在语音技术领域影响广泛。其强大语音克隆能力、独特架构设计和便捷部署方式，带来新体验和机遇，也促使我们思考技术应用边界和伦理道德约束。未来，随着人工智能技术发展，如何发挥 Zonos 等先进技术优势，防范化解潜在风险，实现技术与社会和谐共生，是科技从业者和社会各界面临的重要使命与挑战。

文章参考：

https://www.theregister.com/2025/02/16/ai\_voice\_clone/

**推荐阅读**

|  |
| --- |
| **01**  ｜[Meta因使用盗版数据训练AI面临集体诉讼](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787829&idx=1&sn=677e98e81db6517c8514fb239ceb0ee3&scene=21#wechat_redirect) |
| **02**  ｜[伪装DeepSeek工具的木马病毒曝光](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787860&idx=1&sn=9df4d802e487ddb74e23a5fbfb301c0f&scene=21#wechat_redirect) |
| **03**  ｜[甲骨文提议将美国所有数据纳入Oracle AI研究](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787867&idx=1&sn=f66e744e1aa867b21fc7993883e6b049&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4LovnrYpgT6KJicW2XXFUankpxrVhA4xnribw8EzHnEl2eBDha0QxYwLcuSccpwSrI6aPuH3qqXlTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4LovnrYpgT6KJicW2XXFUanwO0qyJCWcRBcabpE8MiaGQ6v92R5AcnyldJu4tBluQT8dqgR0XGDicqw/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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