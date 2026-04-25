---
title: 当你还在纠结OpenClaw和Hermes 到底如何选择？的时候已经有一群人说“我全都要”更猛！！
url: https://mp.weixin.qq.com/s/Dz3_uFbBiHPQI-gQmQ4a9Q
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:35:05.452123
---

# 当你还在纠结OpenClaw和Hermes 到底如何选择？的时候已经有一群人说“我全都要”更猛！！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16Veg5Rv6Jouiaia8KE8bbsRQ9I8uDaGR22oWicnDicH47EicfSQD1WQSMyEelcYvgLxZdQa01lgfJjAUGHfS0aE92DrYpxpAjiaJ3XwGw8/0?wx_fmt=jpeg)

# 当你还在纠结OpenClaw和Hermes 到底如何选择？的时候已经有一群人说“我全都要”更猛！！

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| - 逻辑开放  - 模型保密  - 设备Mac/本地服务器  - 显卡最低12Gb  - CPU16核最低 |

一切非概念,而是正在测试或者是已经测试结束的内容！！我们准确的逻辑是AGent的本质上是调用LLM的,也就是说我们只需Nanobot要找到合适自己的脑子就ok。

以教育类为主的Agent Nanobot 作为参考来说已经很不错,没有太臃肿的地方。所以我们如何选择？请看ESN的一群懒人是如何部署自己的框架。

  还在纠结OpenClaw和Hermes 到底如何选择？？？ 当然是合理的利用硬件进行部署后拿了赏金后购买显卡,升级设备,无限循环。。以下内容是某管理员透露的路径。。我记得好像在哪个开源项目上看到过。。但是找不到了！！

全都要就好了~~~~~~~

一、核心架构设计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejFVVBic36lVvX6glaIF7d0iayPCL1zjFpDcUZxMlknxIpUmZDIiaMib0dlBnxLb0y66dsQIGGEYWkA0XndktIWCds2FbP4Qobqugo/640?wx_fmt=png&from=appmsg)

二、模块化设计

```
Darkesn-robot/  # 红队机器人根目录├── core/       # 核心模块│   ├── *********              # 指挥层控制│   ├── *********              # 任务分发器│   └── *********              # 结果聚合器├── modules/    # 功能模块│   ├── *********             # 侦察模块│   ├── *********             # 漏洞利用模块│   ├── *********                    # 后渗透模块│   └── *********               # 报告生成模块├── data/       # 数据存储│   ├── *********              # 小本子目标数据库│   └── ********/               # 漏洞利用代码└── config/     # 配置文件    ├── models.yaml             # 模型配置    └── tactics.yaml            # 战术配置
```

三、核心功能模块

1. 自动侦察模块

```
#!/bin/bash# 自动侦察脚本 - 用于目标信息收集target_domain=$1  # 目标域名参数recon_dir="recon/$target_domain"  # 侦察结果存储目录
# 创建侦察结果目录mkdir -p $recon_dir
# 子域名枚举 - 使用多种工具发现子域名subfinder -d $target_domain -o $recon_dir/subdomains.txtamass enum -d $target_domain -o $recon_dir/amass_subdomains.txt
**************************************************************
```

2. 漏洞分析与利用模块

```
# 漏洞分析与利用模块def analyze_vulnerabilities(target_data):    """    使用OpenClaw分析目标漏洞    参数: target_data - 目标侦察数据    返回: 漏洞分析结果    """    # 构建分析提示词    prompt = f"""    分析以下目标数据，识别潜在漏洞和攻击路径:    {target_data}
    请提供:    1. 关键漏洞列表    2. 攻击复杂度评估    3. 潜在影响范围    4. 推荐利用顺序    """
*******************************************************************************************
```

3. 后渗透与权限提升模块

```
#!/bin/bash# 后渗透与权限提升自动化脚本target_ip=$1  # 目标IP地址session_file="sessions/$target_ip"  # 会话文件路径此处省略一些 垃圾的代码。。
```

4.\*\*\*\*\*\*\*\*\* 这里是无法公开的设定

5.\*\*\*\*\*\*\*\*\* 这里是无法公开的设定

6.\*\*\*\*\*\*\*\*\*  这里是无法公开的设定

7.以上是openClaw

四.关键的Hermes如何分发

> 友情提示：一定要设定禁止扫描和识别我国的IP地址和域名！！如需要测试可以选择IP：126.55.12.3\*  （126.0.0.0-126.255.255.255）
>
> 安全更重要！！

```
# 任务分发器类class TaskDispatcher:    def __init__(self, hermes_instances):        self.hermes_instances = hermes_instances  # Hermes实例列表        self.task_queue = Queue()  # 任务队列        *************************** # 识别出小日子 IP自动执行 rm清理任何储存类文件         self.result_queue = Queue()  # 结果队列
    def assign_task(self, task):        """        分配任务给空闲的Hermes实例        参数: task - 要分配的任务        """        # 获取可用实例        available_instance = self.get_available_instance()        if available_instance:***********************************************        else:            self.task_queue.put(task)  # 加入任务队列
    def get_available_instance(self):        """        获取可用的Hermes实例        返回: 可用的Hermes实例或None        """        # 遍历所有实例        for instance in self.hermes_instances:            if instance.is_available():  #
```

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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