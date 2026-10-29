---
title: 工具推荐 | OneDragon：SRC挖洞一条龙自动化
url: https://mp.weixin.qq.com/s/I7IOjQa4Sasyz0HA6lJMuA
source: Doonsec's feed
date: 2026-10-28
fetch_date: 2026-10-29T07:49:43.970226
---

# 工具推荐 | OneDragon：SRC挖洞一条龙自动化

# 工具推荐 | OneDragon：SRC挖洞一条龙自动化

原创

迷人安全
迷人安全

迷人安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字关注 · 安全资讯每日更新

TOOL · RED TEAM

🐉 OneDragon

子域名收集 · 全端口扫描 · 目录爆破 · 漏洞扫描 · 一条龙

2026年10月28日

⭐ Star 253Python · MIT10-27 仍在更新

挖 SRC 最累的不是找不到洞，而是信息收集阶段工具换了一个又一个：子域名用 A、端口用 B、目录用 C、漏洞再开 D，结果文件散落一地，换个目标又得从头敲一遍命令。

OneDragon 就是奔着这个痛点来的——把 OneForAll、massdns、masscan、nmap、ffuf、xray、AWVS 爬虫串成一条流水线，一条命令跑完「子域名 → 端口 → 目录 → 漏洞」全流程，结果统一落盘。项目在 GitHub 上收获 253 个 Star，近期仍在持续维护。

01工具介绍

OneDragon 是一个面向授权安全测试、白帽研究和教学场景的自动化流程项目，定位为「安全圈一条龙服务」：助力 SRC 赏金猎人与白帽子，一键实现子域名扫描、全端口扫描、目录扫描、漏洞扫描，适合需要反复做信息收集的挖洞选手。

⭐ **Star / Fork** · 253 / 34，作者持续维护中

🐍 **技术栈** · Python3 + Linux shell 工具链（cat/cut/grep/sed/sort/timeout）

🧩 **集成工具** · OneForAll、massdns、masscan、nmap、ffuf、xray、AWVS 爬虫

🚀 **部署方式** · 源码克隆即用，入口为 start.py（argparse 标准命令行）

📜 **开源协议** · MIT License

02核心特性

🌐 子域名扫描双引擎

集成 OneForAll 做常规收集，再用 massdns 做爆破验证与补充；针对 OneForAll 爆破偶发无结果的问题，作者单独实现了 massdns 爆破与泛解析排除逻辑。

🔌 全端口扫描

masscan 负责大范围快速探测，nmap 接力做服务识别，自动从结果里筛出 Web 服务交给下一阶段。

📂 目录扫描

对所有存活 Web 服务调用 ffuf 做常规目录探测，扫描结果输出 CSV 并自动去重，直接可用于人工筛选。

🐛 漏洞扫描联动

预留 xray 与 AWVS 爬虫联动流程：AWVS 爬虫先把站点爬一遍，再交给 xray 做被动/主动扫描，提升覆盖面。

🗂️ 结果统一聚合

全部产物落到 output/<目标文件>/ 目录，另提供 --summarize-output 一键汇总既有结果，支持 text / json / markdown 三种格式。

⚙️ 配置化演进

新增 config.example.yaml 与 --check-config 校验，正在把硬编码路径、超时、阈值逐步迁入配置文件，并配套 GitHub Actions 维护检查。

03快速上手

环境要求：Linux + Python3。获取项目（方式见文末）解压后进入目录，先装依赖：

# 安装 OneForAll 依赖与结果去重所需的 pandas
 pip3 install -r OneForAll/requirements.txt
 pip3 install pandas

 # 确认外部扫描器可用：massdns / masscan / nmap / ffuf / xray
 # 各工具位于仓库对应目录，确保二进制有执行权限

跑扫描前，建议先做无扫描器的自检（与项目 CI 一致）：

python3 -m compileall start.py module tests
 python3 start.py --help
 python3 start.py --config config.example.yaml --check-config

把已授权的主域名写进项目根目录的目标文件（每行一个），然后一键启动：

# targets.txt 内容示例（仅限已授权目标）
 example.com

 # 启动一条龙流程
 python3 start.py targets.txt

04实战案例：一次 SRC 信息收集全流程

1写入目标

把 SRC 公告中明确授权的根域名单独写进 targets.txt，一个项目一个文件，便于结果隔离。

2跑主流程

执行 python3 start.py targets.txt，流程会依次走完子域名、端口、目录、漏洞四个阶段，全程无需人工干预。

3读输出结果

所有产物在 output/targets.txt/ 下：final-domains-ips.txt 是子域名解析原始结果；urls\_sub.txt 是整理后的子域名 URL；ips\_all.txt 是 IP 列表；ip\_port\_scan\_results.txt 与 urls\_ip.txt 是端口扫描结果及识别出的 Web 服务；urls\_all.txt 是聚合后的 URL 总表；ffuf\_all.csv / ffuf\_redup.txt 是目录扫描结果与去重版。

4一键汇总复盘

扫描结束后用汇总命令生成报告，只读本地结果、不触发扫描器：

python3 start.py --summarize-output targets.txt --summary-format markdown
 # 也可以写入文件
 python3 start.py --summarize-output targets.txt --write-summary --summary-format json

![](https://mmbiz.qpic.cn/mmbiz_png/Oiag47y540y9Z5tENHEyxDHLFlxHMlw5iaibryCJYOsibYlfeva45CPS4xcFVh9gnSfoCcuBhYjymcdBKZMjuU9piarpj4eRbj6icVbR1jDb8HfYA/640?from=appmsg)

▲ OneDragon 自动化挖洞流水线：一条命令串联四大阶段

实战建议：masscan 全端口扫描对网络环境要求较高，最好放在云服务器或独立 VPS 上跑；xray 阶段资源消耗大，可以先只喂 urls\_all.txt 里的高价值目标。作者也提醒：流程依赖多个外部工具，务必先在隔离测试环境验证参数和输出，再用于授权项目。

05适用场景

🎯 SRC 赏金挖洞

对公告授权范围内的资产做周期性信息收集，子域名、端口、目录一次收齐，把精力留给漏洞研判。

🏢 企业暴露面梳理

红队/蓝队对自有资产做攻击面盘点，输出文件结构清晰，方便对接内部资产库。

⚔️ 攻防演练前期侦察

演练授权范围内的自动化踩点，快速建立目标资产清单与 Web 服务清单。

📚 教学与流程学习

代码结构直白（start.py + module/ 分阶段模块），适合作为「如何串联安全工具链」的学习样本。

📦 项目获取方式

关注本公众号，后台回复

20261028

即可获取项目下载地址与完整文档

⚠️ 免责声明：本文介绍的工具仅限用于已获得明确授权的目标与合法合规的安全测试、学习研究场景。任何未授权扫描与攻击行为均与本公众号无关，请遵守《网络安全法》等相关法律法规。

📌 由 **迷人安全** 公众号整理发布

文章内容仅供学习交流，不承担任何法律责任

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/IOUVFMosoqPvCzibggORicOgMhjBp7HVEtlMoDQGga60sr3AsTe5aHRs7bA7yNic8sibicSpXUIzHkWuDoIH3ibESHCQ/0?wx_fmt=png)

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