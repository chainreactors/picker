---
title: 朝鲜黑客组织利用人脸深度伪造技术分析
url: https://mp.weixin.qq.com/s/zWtKXcvNVQbr13B1Qii0Lg
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:05:57.362251
---

# 朝鲜黑客组织利用人脸深度伪造技术分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpZpOUqsxBZzoH5PnrgicOy6S7L58zVwV4CBUiafItSUQ1vrFwIbL5Wk1YmOkeHMrQA3kEdH22qcGUb5jlaicSJOMJpSX60icNjrzM/0?wx_fmt=jpeg)

# 朝鲜黑客组织利用人脸深度伪造技术分析

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

BlueNoroff是朝鲜 Lazarus Group 旗下以经济利益为核心目标的子组织，公开归属于朝鲜侦察总局（Reconnaissance General Bureau, RGB），该组织目前持续针对加密货币和 Web3 生态系统攻击。

近期，该攻击组织通过被篡改的 Calendly 日历邀请发送拼写仿冒的 Zoom 会议链接，启动了多阶段攻击链，攻击者在受害者系统中维持了长达 66 天的持久化权限，受害者为北美Web3加密货币公司员工。

## 以下为该组织的社会工程学与深度伪造的结合情况。

###

BlueNoroff 构建了一套闭环的社会工程学攻击体系。

在这套体系中，被窃取的受害者资产包括视频录像、个人数据、浏览器数据和 Telegram 会话，会被直接用于冒充受害者发动新一轮攻击。

在本次入侵中，攻击者伪装成一家国际咨询律所的法律主管，该律所专注于金融科技、加密货币和 iGaming 领域，以 Calendly 预约作为初始接触手段。攻击流程始于受害者收到攻击者发送的 Calendly 邮件邀请，会议被安排在五个月后的 2026 年 1 月 23 日。当受害者确认预约后，系统会自动生成 Google Meet 日历邀请，攻击者随后秘密修改事件详情，将合法会议链接替换为拼写仿冒的 Zoom URL。这种初始接触模式完全符合 BlueNoroff 假会议攻击的公开战术手法。

后续扩大调查发现的证据进一步证实了这一模式。有受害者在 LinkedIn 公开披露其身份被用于诈骗，发布的截图显示攻击者从被入侵的 Telegram 账户发送消息，向新目标发送 Calendly 链接发起 "叙旧" 会议。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqTET8zwjBZvEYwU0iavq2hf0AI0pPYUjnibicoc1ZOicfhtzBQSsZib2r1bXdrJfDnsbs31iaNuDjiazQvboKRlRfFrFb0c32DDlxbQI/640?wx_fmt=png&from=appmsg)

攻击者与主要受害者的假会议定于 2026 年 1 月 23 日 17:00 UTC 举行。遥测数据显示，受害者在四分钟内三次点击恶意 URL，这符合典型的社会工程学场景，即受害者误以为 Zoom 客户端故障而反复点击链接。

攻击者注册的拼写仿冒域名在视觉上与合法 Zoom 子域名几乎无法区分，URL 结构包含会议 ID 和密码参数，完全复刻了真实 Zoom 的 "加入会议" 链接格式。

假会议界面中出现的所有人物，几乎都是此前攻击中被窃取视频和图像的受害者。这形成了一个自我强化的凭证窃取与身份冒充循环，每一次成功入侵都会为后续攻击提供更具欺骗性的诱饵素材。

海外安全研究员从攻击者托管基础设施中恢复了超过 950 个文件，包含 8 组完整的 ExifTool 元数据转储，覆盖图像、视频和项目文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrZlIhvsUxIlMQsQz31QBS0dHAOVRX2ZYOhfgeo0GpL4mPyH2CaxHz5dfX9f1DNicYnYmahlSTiacJ6AaYrLnh5637AXjssOEKSE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrJyml89TKwOYXN99VgVEUbo1Sn4MfwqrwAPEYUMvA5YTEDaKvuZQRwxjdQgQjmmUetgRXzrBvXVLG8q8yT9x9ibYZRy0FC170Q/640?wx_fmt=png&from=appmsg)

分析结果显示，攻击者建立了一套结构化的媒体生产流水线，结合 AI 生成肖像图像、屏幕录制的受害者视频和专业视频编辑工具，批量制造用于假会议诱饵页面的虚假参与者内容。

攻击者共制作了三种不同类型的 "假参与者"，形成了梯度化的欺骗效果：

#### 类型 1：真实人物，被盗视频素材

####

第一种媒体资产是此前受害者的真实预录视频。这些.mp4 文件是在早期攻击中通过 HTML 诱饵页面窃取的实际摄像头画面。当受害者加入假会议时，页面会通过 getUserMedia API 捕获其实时摄像头流，并将数据传输到攻击者服务器进行录制。

这些原始视频会经过后期处理，部分通过 Microsoft Clipchamp 进行剪辑，部分通过 FFmpeg 进行格式转换，然后存储在攻击者服务器中供重复使用。当受害者在会议中看到自己的朋友或同事时，他们看到的是真实人物的真实视频，只是这些视频是在当事人完全不知情的情况下被盗取的。

#### 类型 2：AI 生成静态头像

####

第二种媒体资产是 AI 生成的头像图像，用作假 Zoom 通话中的静态头像占位符。

在所有 950 多个文件中仅检测到 OpenAI ChatGPT GPT-4o 这一种 AI 生成系统。通过文件中嵌入的 C2PA（内容来源与真实性联盟）加密签名清单，确凿地识别出 8 张 AI 伪造的 PNG 图像。C2PA 是 OpenAI 在图像生成时嵌入的防篡改内容溯源标准。

分析的 8 张 AI 生成图像中，有 7 张是 1024×1024 像素的头像文件，文件名遵循 "名 - 姓。格式" 的命名规范，每张图像都配有一个同名的视频文件。这一发现提供了强有力的证据，证明这些 AI 生成肖像被用作 "会说话的头像" 深度伪造生产流水线的面部来源。第 8 张 AI 生成图像是用于 HTML 诱饵页面的会议图标。

尽管图像是 AI 生成的，但可以确认这些头像的文件名对应真实存在的个人，攻击者正在冒充这些人的身份。在会议界面中，这些头像会显示为关闭视频的参与者，无需为每个人准备视频素材，就能让会议看起来有多名真实参与者。

#### 类型 3：深度伪造合成视频

####

第三种也是技术含量最高的媒体资产是深度伪造合成视频。这类视频将 AI 生成的面部叠加到真实的人体和动作源上，实现高度逼真的效果。

通过 ExifTool 元数据重建的生产流水线揭示了这类视频的制作过程。攻击者首先使用 ChatGPT/GPT-4o 生成合成面部，然后利用 Windows 虚拟机通过 Game DVR/Game Bar 录制屏幕内容作为身体和动作源。这些动作大多是攻击者本人或其他操作员模拟的自然视频通话行为，包括点头、微笑、注视镜头和手势等。

随后，攻击者在 Adobe Premiere Pro 2021 中将 AI 面部与真实动作视频进行合成，项目文件 target.prproj 共引用了 73 条此类视频。合成完成后，通过开源视频软件套件 FFmpeg 导出最终成品。最终生成的视频展示了一个拥有 AI 生成面部的虚拟人物，使用真实捕获的人类身体动作执行逼真的会议行为。

### 攻击者媒体库：950 + 文件的深度伪造素材库

###

从攻击者托管基础设施中总共恢复了 950 多个文件，其中 740 个来自 2026 年 3 月 24 日的抓取数据（分布在 6 个文件夹），256 个来自更早的抓取数据（分布在 2 个文件夹）。

在已识别的 100 名目标中，36 人有真实视频记录（.mp4/.mov 格式），5 人有静态头像（.jpg/.jfif 格式），48 人被标记为 "已归档"，即此前托管但当前无法直接访问的内容，不过攻击者可能仍保留了副本。另有 1 条记录使用.mov 格式并提供了直接访问链接。

这种分布模式表明，攻击者维护着一个不断增长的媒体库，并根据作战需求轮换活跃诱饵素材。他们会归档旧资产，但保留这些内容以备未来使用。

进行的早期数据抓取与后期文件夹在组成和结构上完全一致，证实攻击者会持续迭代更新其媒体库。这符合长期作战活动的特征，即不断吸收新的受害者素材并刷新诱饵内容。

攻击者能够根据特定目标的职业网络，在假 Zoom 或 Teams 会议中填充目标认识的行业人物。这种能力构成了一种极具威力的社会工程学武器，如果没有提前了解这种攻击手法，几乎无法被察觉。

攻击者托管基础设施上的内容被组织成多个独立的操作文件夹，每个文件夹在生产流水线中承担特定功能：

| 文件夹路径 | 文件数量 | 内容描述 | 检测到的 AI 内容 |
| --- | --- | --- | --- |
| /dynamic/ | 254 | 处理完成的 MP4 视频、JPG 照片和 PNG 肖像，会议参与者媒体的 "成品" 文件夹 | 7 张 AI 生成 PNG 肖像（C2PA 认证） |
| /webcam/ | 185 | 来自摄像头捕获和屏幕录制的 MP4 视频和图像，包含可疑的 morph.jpg+morph.mp4 文件对 | 无 AI 生成元数据 |
| /onlineimgs/ | 130 | 从网站和社交平台抓取的头像照片（分辨率 200×200 至 960×1280） | 无 AI 生成元数据 |
| /video-scrape/ | 140 | 抓取的真实视频（139 个 MP4，1 个 MOV），其中 17 个通过 Microsoft Clipchamp 网页编辑器编码 | 无 AI 生成元数据 |
| /logo/ | 14 | 品牌标志、会议图标和背景图片，授权的 Shutterstock 库存照片 | 1 张 AI 生成 PNG（会议图标，C2PA 认证） |
| /Wartr/ | 17 | 项目营销素材，在 Adobe Photoshop CS6/2021 中编辑的 Shutterstock 库存照片 | 无 AI 生成元数据 |
| scraped\_data/onlineimgs/ | 123 | 早期版本的头像照片抓取数据（与 /onlineimgs/ 几乎相同） | 无 AI 生成元数据 |
| scraped\_data/onlinevideos/ | 133 | 早期版本的视频抓取数据（与 /video-scrape/ 几乎相同），包含 macOS 屏幕录制 | 无 AI 生成元数据 |

###

###

### 完整深度伪造生产流水线

###

对攻击者托管媒体的深度元数据分析，揭示了一套精密的四阶段生产流水线，用于批量制造假会议参与者视频：

#### 阶段 1：AI 肖像生成

攻击者使用 ChatGPT/GPT-4o 生成合成面部图像，输出 1024×1024 像素的 PNG 头像。每张图像都以被克隆的真实人物姓名命名，作为后续深度伪造视频的 "面部源"。

#### 阶段 2：源视频捕获

原始视频素材通过三种方式获取，所有方式均通过元数据确认：

1. 运行 Windows 10 的 VMware 虚拟机屏幕录制（使用 Microsoft Game DVR/Game Bar）
2. macOS 主机原生屏幕录制
3. 直接摄像头捕获

这一阶段捕获的内容包括身体动作、背景和音频，将与 AI 生成的面部进行合成。

#### 阶段 3：视频编辑与合成

原始捕获素材在 Adobe Premiere Pro 2021（版本 15.0）中进行组装。通过元数据识别出两个 Premiere 项目文件，主项目文件 target.prproj 被 117 个视频引用，测试项目文件 test.prproj 被 6 个视频引用。最终编码使用 FFmpeg 完成，部分抓取的视频（51 个文件）还通过 Microsoft Clipchamp 进行了额外编辑。

#### 阶段 4：部署

完成的素材被整理到上述文件夹结构中，并由 HTML 诱饵页面引用。/dynamic/ 文件夹存放最终成品，包括配对的 AI 肖像和配套深度伪造视频，其他文件夹存放真实抓取的素材，包括真实头像照片和已识别目标的摄像头录像。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrsEOw84OQib9EJaDWGsh7uyteNOMiacZwH5iaOUnenibszbYXXR7eiaTdJWez26NMx9iaBUktCftv9PdxREMIz7JcFNk4SpDl04FlyU/640?wx_fmt=jpeg&from=appmsg)

### 深度伪造操作员画像

###

嵌入在视频文件中的元数据，泄露了负责媒体生产流水线的实际威胁操作员的身份信息：

| 属性 | 具体值 | 信息来源 |
| --- | --- | --- |
| macOS 用户名 | king | 所有 Premiere Pro 项目路径：/Users/king/Documents/Adobe/Premiere Pro/15.0/ |
| 主要硬件 | Apple MacBook Pro（MacBookPro18,1） | 屏幕录制元数据 |
| 主机操作系统 | macOS 15.5 | 屏幕录制元数据 |
| 客户机操作系统 | Windows 10（VMware 虚拟机） | Game DVR/Game Bar 屏幕捕获元数据 |
| 主要 Premiere 项目 | target.prproj | 被 73 个视频引用 |
| 次要 Premiere 项目 | test.prproj | 被 6 个视频引用 |
| 活动时间段 | 2025 年 5 月至 2026 年 1 月 | 最早 / 最晚视频源时间戳 |

用户名为 "king" 的操作员采用双操作系统工作环境，使用 macOS 作为主系统运行 Adobe Premiere Pro 进行编辑和原生屏幕录制，同时在 VMware 中运行 Windows 10 虚拟机，用于执行或录制假视频通话。

这种将操作员活动隔离在虚拟机中，而在主机上进行编辑的操作安全模式，符合刻意的隔离化设计原则。

### 操作时间分析

###

对调查收集的数据集进行时间戳分析，揭示了攻击者的操作节奏。将时间转换为韩国标准时间（UTC+9）后，操作员活动集中在标准工作日的 08:00 至 18:00，周一至周五，周末活动极少。

每日活动热力图显示，峰值操作时段为 09:00 至 17:00 韩国标准时间。

这种模式与国家支持的组织遵循常规工作日时间表的特征一致，而非机会主义的犯罪活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpdKo04xFmo3jPe8aZnc4GmJF29YPLnxwdEf2XwMPA9xAPgCiceMfvd949NbAcQcNbZcEjykDrNKrSTibvBrppaCJLdeicHry8To4/640?wx_fmt=png&from=appmsg)

### 非 AI 软件工具栈

###

除 AI 生成内容外，通过对攻击者托管媒体文件的元数据分析，还识别出操作员使用的完整非 AI 软件工具栈：

| 工具名称 | 用途 | 引用次数 |
| --- | --- | --- |
| Adobe Premiere Pro 2021（v15.0） | 视频编辑与合成 | 73 个视频文件引用 Premiere 项目元数据 |
| FFmpeg | 视频编码与格式转换 | 所有视频输出的主要编码器 |
| Microsoft Clipchamp | 基于网页的视频编辑 | 51 个文件 |
| Microsoft Game DVR/Game Bar | Windows 屏幕录制（VMware 客户机） | 18 次引用 |
| macOS Screen Recording | macOS 主机屏幕捕获 | 4 次引用 |
| Adobe Photoshop CS6/2021 | 图像编辑 | 53 次引用 |
| paint.net 5.0.13 | Windows 图像编辑 | 1 个图像 |
| Shutterstock（授权库存图像） | 背景图像和营销素材 | 30 次引用 |

##

## 完整攻击链：从假会议到系统完全沦陷

##

深度伪造假会议只是攻击的入口，攻击者随后通过多阶段无文件攻击技术，在不到五分钟内完成了从初始访问到系统完全控制的全过程。

### 阶段 1：HTML 诱饵与摄像头窃取

###

点击仿冒诱饵 URL 后，受害者被定向到攻击者托管的 HTML 页面。该页面托管了一个完全独立的嵌入式 JavaScript 应用程序。我们分析了 12 个恢复的 HTML 样本，其中 6 个是 Zoom 品牌，6 个是 Microsoft Teams 品牌。所有样本都共享相同的底层框架和 C2 基础设施，仅在品牌和每次部署的配置上有所不同。

HTML 诱饵执行五个核心恶意功能：

1. **伪造的会议界面**

   页面呈现 Zoom 或 Teams 会议大厅的精确复制品，填充有 CDN 托管的假参与者头像和预录视频片段，模拟活跃的会话。然而这个 "会议" 中没有任何实时参与者。参与者磁贴使用循环播放预录视频的<video>元素或静态头像的<img>元素呈现，同时随机的 "活跃发言者" 指示器每 3 到 5 秒在参与者之间循环，以创造实时对话的错觉。
2. **基于浏览器的摄像头和麦克风访问**

   接下来，页面以加入会议为借口调用 getUserMedia API，捕获受害者自己的实时摄像头画面。一个单独的、隐蔽的 getUserMedia 调用独立于可见的预加入摄像头预览处理窃取流。
3. **视频窃取**

   受害者的摄像头画面被实时窃取到攻击者控制的基础设施。Zoom 变体 POST 到托管 C2 上的相对 /upload 路径。Teams HTTP POST 变体使用硬编码的url。Teams WebSocket 变体通过持久 WSS 连接流式传输。使用 443 端口的 WSS 在操作上具有重要意义。单个长连接取代了每个块的 HTTP 请求，减少了网络日志噪音，并且如果不进行深度数据包检查，WSS 流量与标准 HTTPS 无法区分。
4. **操作系统指纹识别**

   页面在加载时通过 navigator.userAgent 静默枚举受害者的操作系统，在 Windows、macOS 和 Linux 代码路径之间分支执行。
5. ...