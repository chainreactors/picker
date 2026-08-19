---
title: 用 AVL Code 手搓一个基于 FPGA 的 TF 卡仿真器
url: https://mp.weixin.qq.com/s/vF7CsJYakIi-zqSWo0c5uA
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:55:35.804944
---

# 用 AVL Code 手搓一个基于 FPGA 的 TF 卡仿真器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkicPwm7hDQ5g1vibaobG5OlrSbDoibaAltiaVREtNgGHQtNgf7dYKKTibNtzT5vkRDkicQptusLr9xuw9JJs7pElicMGOubrdFzN5mEmM/0?wx_fmt=jpeg)

# 用 AVL Code 手搓一个基于 FPGA 的 TF 卡仿真器

Esoul
Esoul

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

本文原载于安天AVL Code编程智能体技术blog，发布日期为2026-08-16，原文地址为：https://www.avlcode.cn/blog/fpga-tf-card-emulator/

![用 AVL Code 手搓一个基于 FPGA 的 TF 卡仿真器](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk9YpIGqqcGrialDLSm8ibe5QRDdYicicniaXibmhAgnfuIRzKtyfJH754T8vhQovVxQEdQbG4syL3Mf4BrbcZkR2hYznKsj39qUdEA54/640?wx_fmt=other&from=appmsg)

## 起因

最近正在分析分析一个设备的 bootloader 工作机理，板子是上电从 TF 卡引导的，调试过程反复插拔烧写 TF 卡，操作繁琐不说万一弄坏设备上的卡槽就悲剧了。现在很多开发板都用 TF 卡启动，例如树莓派、i.MX 系列，以及香橙派等基于国产瑞芯微、全志、海思芯片的板子等等。咱们极客 DIY 过程也都有同样的问题。

打开 AVL Code[1] 和 AI 讨论，得知典型 TF 卡槽插拔寿命 500~1000 次，确实很容易损坏。AI 建议开发调试尽量走 USB 或以太网。这不废话嘛，调试底层的一级 bootloader（FSBL，First Stage Bootloader）没得选呀！进一步追问，给出的解决方案是用延长线/转接头把卡引出到机壳外，插拔磨损转移到转接头上。

循着早期单片机在线仿真器的思路，问 AVL Code 有没有 TF 卡仿真器，或者类似的工具，可以不插拔卡联机更新卡内容。给出的答案是：

1. SD 卡仿真器（专用硬件），这类产品市面上零售很少，多为芯片厂内部开发验证用，贵且难买。
2. 用 FPGA 做 SD 卡仿真，没有现成的产品，自己做要有 FPGA 开发能力，成本高，调试门槛高……

用 FPGA 手撕一个 SD 卡仿真器，有用又有趣，不错的主意！AI 在手，今非昔比，此手撕非彼手撕，嘿嘿。

准备

继续和 AI 聊，作为测试 bootloader 用的调试工具，最小系统需包含“PHY + 命令引擎 + 状态机 + RAM + 联机数据接口”这几个部分。

针对这几部分让 AVL Code 检索相关的开源项目。发现有个优质项目实现了前三部分即“PHY + 命令引擎 + 状态机”：WangXuan95/FPGA-SDfake[2]。仔细查看原来是国人 FPGA 大神 WangXuan 的作品，质量有保证。而且人家已经上硬件测试过，仿真的 SD 卡放到读卡器里能被 Windows 识别，甚至读出预先准备的文件。当然他这个不能在线更新卡的内容，仿真 SD 卡的扇区数据是以 ROM 形式预先嵌入的，改变内容还要重新综合生成 bit 文件并重新配置 FPGA。

关于 RAM 模块，AVL Code 说因为跨时钟域（SD 卡读取 RAM 时钟和上位机写 RAM 时钟），要用双端口 RAM。双端口 RAM 可以用 FPGA 厂商的 IP 生成器生成，也可以用 Verilog 的描述由综合工具自动推导。为了确保 Verilog 描述的 RAM 最终实现时能映射到 BRAM，必须严格遵循厂商推荐的写法。AVL Code 还说有 Xilinx 推荐的标准模板。正好我要用 Xilinx 的 FPGA，OK，让它找来模板，依葫芦画瓢，避免跑偏。

另一部分就是和 PC 通信联机加载数据的接口逻辑。首先和 AVL Code 一起确定了使用 UART 接口，它给我估算了一下，加载 100KB 数据约 10 秒，完全能接受。对于调试初级 Bootloader 来说，100KB 足够了，更大的数据量 FPGA 的片上 RAM 容量也不够了。UART 实现简单占用资源少，开源设计很成熟，价格便宜量又足。

单纯 UART 模块的 Verilog 开源设计不是问题，一抓一大把。可是这里是要把 UART 的一维数据流按地址和数据写到 RAM 中，还需要个通信协议解析、串并转换状态机。最好能找到相似的解决方案参考一下。AVL Code 找到了几个可参考的开源项目。看起来质量靠谱的大多是比较重量级的，把 UART 通信转换成 AXI 或 Wishbone 标准总线，这对于我们简单地写 BRAM 有点费力不讨好，还消耗更多逻辑资源。经过和 AVL Code 几轮拉扯，终于找到了一个叫做 UART2BUS 的开源项目，虽然叫做 bus 其实它出来的恰恰是简单的地址、数据以及读写信号：HexSDR/uart2bus[3]。人家定义了一整套、确切说是两套上位机通信协议（一种是 ASCII 字符的命令协议，另一种是更高效的二进制协议），有清晰文档描述，功能完备且轻量级！

最后还有一部分是上位机程序，按照和 FPGA 上 UART 模块约定的协议推送数据，必要的话还要进行数据校验。AVL Code 自告奋勇说它可以写个 Python 程序实现这个功能。根据经验这样的任务 AI 工具应该轻车熟路毫无压力。

至此，详细方案已定。

开发实现

讨论任务规划时，AVL Code 说用 FPGA 做 TF 卡仿真这条路难度很大，预计工作量以数周计。其实得益于前期充分的讨论和调研，几乎各个组件都找到了开源项目参考。整体开发工作更像是一个拼接缝合的过程。当然，细节是魔鬼，来自不同组件的拼接和调整适配，以及充分的验证这也是比较考验能力的地方。

虽然用 AVL Code 已经有一段时间了，但用它开发 Verilog 还是头一次，估计用 AVL Code 做硬件开发的小伙伴也不多，究竟表现如何还要拭目以待。

首先，它下载并分析已有参考代码，很快它说已经掌握了整体情况。有趣的是，由于我习惯按开发板来组织项目存放目录，AVL Code 从工作文件夹路径中得知了我要用的开发板型号，多次提到它根据芯片的资源数量确定了参数配置，例如 BRAM 的容量等等。

然后它例行地制定了执行步骤，按典型 Verilog 项目建立了目录结构。很快就完成了修改适配各个模块的代码，当然这一步的正确性还有待后续闭环验证。

然后，它开始编写验证 Testbench，并且检测到了系统已安装的开源仿真器 iverilog，用来运行仿真。这一步花的时间比较多。毕竟这是它从头编写的模块，并且与 DUT 的时序相关。中间犯过一些语法低级错误，也有状态死锁导致的仿真超时，基本它都能找到问题自己解决。

最终完成的 Testbench 包含完整的 PC 模型（ASCII + 二进制 UART 收发）和 SD 主机模型（初始化序列、R1/R2/R3/R6/R7 校验、CRC7/CRC16 校验、1 位/4 位/多块读、SCR 检查）。AVL Code 还设计了真实 115200 波特率的精确仿真和用于大数据量验证的快速仿真方案。兼顾了精度和测试覆盖。验证还算完备吧。

中间关于原始 UART2BUS 下载协议扩展和下载数据长度等用户层协议细节，和 AVL Code 进行了多轮拉扯，最终达到了我的要求。

仿真验证通过的 RTL 代码一共 7 个 Verilog 文件，建立 Vivado 工程后综合一次通过，目测资源使用也都符合预期。

剩下的就是上板验证了。

到这里实验用的开发板闪亮登场，它，就是——就是——ebaz4205！驰名中外的矿渣 FPGA 板，某鱼改造好的开发板只要 50 块钱，甚至比一个山寨下载器都便宜！这个板子笔者先后买过至少 10 块，很多随手送给身边的小伙伴了。

主芯片虽然是 Zynq，但这里只把它当作纯 FPGA 来用。如 AVL Code 前边所说，这个芯片的逻辑资源足够用，主要限制是片上 BRAM 数量，最终实现了 128KB 容量，可以仿真 256 个 TF 卡扇区（每扇区 512 字节）。板子 IO 数量也很充足，IO 都是 3.3V 标准，外接一个 USB 转串口小板就能和上位机连接。

可是、但是、可但是……如何实现 TF 卡的仿真接口呢？

大神 WangXuan 项目是用自己画的 PCB 实现了 SD 卡接口，他开源了 PCB 设计文件，但他没有做 TF 卡形态，并且画板和 PCB 打板也超出了本项目的范围。于是诉诸万能的某宝，找到了这个：

![TF 卡延长板 PCB：卡形金手指一端引出为可焊接的焊盘](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk8x5kvd8VmNUyDuhHJsYAgZbADu2lMRaOd3c4aOibaNfq5fYeANElxyWStlWXIcWIUywPdYWriaeuEfuiaX9PheKGP3rmoY4HV72E/640?wx_fmt=other&from=appmsg)

还有这个：

![TF 测试卡套、延长卡与 TF 卡实物](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkic1M4xPiaHl8Tm4icE4iaxia9d6bLzxiaXnC8YfvNKePqibKDrU2lplJ7IlZHnbsRyVc01W8ztr7Fd92rfOMX1eYY0xFkuSvZSrLNtEM/640?wx_fmt=other&from=appmsg)

价格便宜量又足，但需要稍加改造。我们仿真的 TF 卡不涉及高速信号，25MHz 用杜邦线飞线是没问题的。参照 WangXuan 的电路图飞线焊接，于是就有了这个：

![延长板与开发板排座之间的杜邦线飞线焊接，热熔胶加固](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkic3BwhZSBd1fOjSJDaibaoDibIh8Q25LHIqkWNY864BiaUMmadx08P0sicNRmh1ZdqhhVBmz8IoyiaL7XJwMqJrIKibtoXIlBm514JRM/640?wx_fmt=other&from=appmsg)

（其实还手工改制了另一版，整体看起来更考究一些……，然并卵，不知道哪里焊接短路还是断路了，竟然不好用！）

上板测试

上板测试比较顺利，一方面因为仿真验证比较充分了，另一方面因为最复杂的 SDHC 协议这块是基于大神的高质量代码实现的。否则 SDHC 协议这里可能会有一场恶战，开发调试搞上几周都是有可能的，期间可能还要陷入到读 SD 卡通信协议文档的痛苦煎熬中……

PC 机 Windows 读取实验，下载位流配置 FPGA，然后用 Python 程序推送仿真数据：

![PowerShell 中运行 load_sd_image.py，经 COM10 以 115200 波特推送 98304 字节镜像](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkibWicH04JumaF93oEaFLq7VuK4AwZvGW4K874gzGP1OT4Oj1vxRrDUmFwaeMXF9aZRDVkgRHtXqHL5e8qj4U6rT8ZUH4jXMv1aY/640?wx_fmt=other&from=appmsg)

插入读卡器，Windows 成功识别到了卡，由于只初始化了某些扇区，没有文件系统，所以提示格式化：

![Windows 资源管理器识别出仿真卡（E 盘）并提示需要格式化](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk8CNzwUN2JpqocVdHA0bThA3jTciaHnEDCCunAhtnuxojGictMB7QhQmn79H48XXHVCs7e2RNzmq3Yf6qQ3ibl7v1G0vhIS3Io7Mk/640?wx_fmt=other&from=appmsg)

用 WinHex 磁盘工具查看扇区内容，推送下载的内容以及位置完全正确：

![WinHex 查看仿真卡扇区：0x8800 处以 RK33 开头的数据与推送内容一致](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicwiaGJqbSNRkHvfXZrJew2ZP0EDkn1tDfLXOIVgbvPFEHN0dLNYAr3sIbG5wrZEEBLnflggaz8TPGWl1knX6xgNxiaX4XynrSKk/640?wx_fmt=other&from=appmsg)

图中这个扇区开头的 RK33 是 RK3326 芯片识别 Bootloader 的 Magic number。

下图是 PC 机用读卡器实验的硬件配置。

![读卡器实验硬件配置：ebaz4205 开发板、USB 转串口小板、读卡器与飞线转接板](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk9V0XfJ6K3WaYpmibZbuHicpgbvPuKIqxWHxMR45Slia8sPsKUxqIGkib7jJLiac20Zzz1KsjurLib43AChhvibR63w6LQuPjHgOnXH7Y/640?wx_fmt=other&from=appmsg)

把仿真的 TF 卡插入到目标嵌入式设备，上电开机，目标设备的串口成功打出了一级 Bootloader 的输出信息：

![串口终端打出目标设备 U-Boot TPL/SPL 引导阶段的输出日志](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk8H2fDU0VM22kEvYV2135VqrrkJia1kteXEfibV5D10zuia3yVudhq9KFT40hk4qkibCYJqXbaRRLF7JhMIYy6fgQcam1LBlTZrneA/640?wx_fmt=other&from=appmsg)

成功被目标板识别，并且完成了初级 bootloader 引导！

磨刀不误砍柴功，有了这个神器，但愿从此正向开发，逆向分析都如虎添翼、如有神助、一日千里……

总结和展望

在 AVL Code 的辅助下，检索资料、确定方案和代码开发大约用了 2 天时间，完成了初版的 TF 卡仿真器，可满足基本的嵌入式 Bootloader 调试需求。

目前代码已开源：opengeili/tong[4]。

如前文所述，开发板上主芯片是 Zynq，板上带有 256MB DDR 存储器，后边可以用它的更多资源来实现大容量卡的仿真，还可以实现 TF 卡读写事件捕获分析等高级调试功能。

等有空了继续调戏 AVL Code，嘿嘿。

（本文作者桑胜田，安天联合创始人）

*关联引文：*

*[1]AVL Code官网*

https://www.avlcode.cn

[2]https://github.com/WangXuan95/FPGA-SDfake

[3]https://github.com/HexSDR/uart2bus

[4]https://github.com/opengeili/tong

安天AVL Code官网链接：https://www.avlcode.cn

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk8PT5nqiaDOuVwSp5Yh8bbK9OZSKPOOvVygZmtrGWu1EoQ2WSvouP8ASaN9U4MvwhOlhZyOLia4ILUAZqIrDp3LzOJMaBwqYOY00/640?wx_fmt=jpeg&from=appmsg)

**安天AVL Code网站二维码**

**往期推荐:**

#

# [娃娃抓起，肌肉记忆](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215223&idx=1&sn=4fa3e8305dbed27c15e0530737f250b1&scene=21#wechat_redirect)

# [概率不是意识，越界不是觉醒——从 GPT 攻破 HuggingFace 事件提炼教训清单](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215187&idx=1&sn=06a22e93351cdb5935c9bc9ba81011b9&scene=21#wechat_redirect)

# [仓库已经归档，风险没有归档——Fastjson 1.x 新 RCE 风险观察](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215167&idx=1&sn=38a12d6d5995bf5d3ca53704c6ef6176&scene=21#wechat_redirect)

[AVL Code 的设计如何避免发生“GPT-5.6 一键清空创业者全盘数据”](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215191&idx=1&sn=f8e81d1fd407245191f4157cf0491a14&scene=21#wechat_redirect)

# [用AVL Code验证“Claude Code内置隐藏机制，专门检测中国用户”的传言](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215022&idx=1&sn=77496defba538a08d0885e11cb5d3bbe&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

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
...