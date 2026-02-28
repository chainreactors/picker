---
title: 使用 Python 通过 Telnet 连接到 EVE-NG 中已启动的 Cisco CSR1000V 路由器节点
url: https://mp.weixin.qq.com/s/RB4JYeRjo72wVDH3MsuEsA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:52:51.969832
---

# 使用 Python 通过 Telnet 连接到 EVE-NG 中已启动的 Cisco CSR1000V 路由器节点

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Dibzmm9niba06lWp1vib6ZNBxAEtic0ib6Iprxxedl5ZHCic0LfpBkZcwM8coDSsnH8Zau65OVwUQUW2Fe1VMqMfPYDFiasK46MnozEic4thqdImQB8/0?wx_fmt=jpeg)

# 使用 Python 通过 Telnet 连接到 EVE-NG 中已启动的 Cisco CSR1000V 路由器节点

原创

Lino
Lino

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

各位同学，大家好！我是你们的 Python 讲师 Lino。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba046q4FDbQfExp0oJUn8gM3rGLyQwOB3cph3OBt2RJUCdO34m9Y6FbWItGib3goJDib5ApbmmbTeAk6gwKrkUaUiaxxZRHXiat2eEqw/640?wx_fmt=png&from=appmsg)

EVE-NG 为每个运行中的节点分配一个临时的 Telnet 端口（通常从 30000 开始递增，也可能在 40000+ 范围）.

Python 标准库中的 `telnetlib` 模块可以轻松实现 Telnet 连接。下面提供两种常用方式：

1. 交互式连接（推荐初次使用，像普通 Telnet 客户端一样手动输入命令）
2. 自动化脚本（发送命令、读取输出，适合批量配置或自动化测试）

## 环境准备

* Python 3.x（推荐 3.8+）
* 无需额外安装包，telnetlib 是标准库
* 如果你在 Windows 上运行，确保系统已启用 Telnet 客户端（可选，仅用于对比测试）

## 方法一：交互式 Telnet 连接（最简单，手动操作）

```
```
import telnetlib
import sys

# 修改这里为你的实际参数
HOST = "192.168.194.128"          # 如果在本机运行 EVE-NG，使用 127.0.0.1
                            # 如果远程连接，改为 EVE-NG 服务器的 IP
PORT = 32771                # 替换为节点实际的 Telnet 端口

try:
    # 建立连接
    tn = telnetlib.Telnet(HOST, PORT, timeout=10)

    # 可选：等待首次提示（CSR1000V 首次启动可能进入 setup 模式）
    # tn.read_until(b"Would you like to enter the initial configuration dialog? [yes/no]: ", timeout=10)
    # tn.write(b"no\r\n")

    print("连接成功！现在可以直接输入命令（输入 exit 退出）")
    print("="*50)

    # 进入交互模式，像普通 Telnet 一样操作
    tn.interact()

except Exception as e:
    print(f"连接失败: {e}")
    sys.exit(1)
finally:
```
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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