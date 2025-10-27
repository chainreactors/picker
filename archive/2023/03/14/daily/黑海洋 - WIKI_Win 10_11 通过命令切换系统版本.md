---
title: Win 10/11 通过命令切换系统版本
url: https://blog.upx8.com/3265
source: 黑海洋 - WIKI
date: 2023-03-14
fetch_date: 2025-10-04T09:30:39.048341
---

# Win 10/11 通过命令切换系统版本

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Win 10/11 通过命令切换系统版本

发布时间:
2023-03-13

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
37058

点击win键，输入CMD，在最佳配置出现的命令提示符处右键，选择以管理员运行。

在打开的窗口中输入命令 dism /online /get-CurrentEdition获取当前系统版本

再使用命令 dism /online /Get-TargetEditions显示可以将当前系统可以升级到的版本
其中

```
Professional为专业版 VK7JG-NPHTM-C97JM-9MPGT-3V66T
ProfessionalEducation为专业教育版 8PTT6-RNW4C-6V7J2-C2D3X-MHBPB
ProfessionalWorkstation为专业工作站版 DXG7C-N36C4-C4HTG-X4T3X-2YV77
ProfessionalCountrySpecific为专业国家特定版本
ProfessionalSingleLanguage为专业单语言版
ServerRdsh为服务器Rdsh版，开启Rdsh后可接受无穷多的RDP远程用户，本地也可以开启一个用户。
IoTEnterprise为嵌入式版本，可以理解为物联网版。
Enterprise为企业版 XGVPP-NMH47-7TTHJ-W3FW7-8HV2C
Education为教育版 YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY
Home Edition为家庭版 YTMG3-N6DKC-DKB77-7M9GH-8HVX7
```

根据个人需求输入相应版本密钥,以教育版转专业工作站版为例 命令如下

```
changepk /productkey DXG7C-N36C4-C4HTG-X4T3X-2YV77
输入后回车，如需要升级文件，等待弹出升级界面并升级完成。若无文件升级，则等待片刻后可通过此电脑右键属性查看系统版本。
升级前务必通过命令dism /online /Get-TargetEditions查看确定可以升级到的版本，再用对应的key转换。
更换版本后很容易出现系统未激活的问题，请自行使用key或工具激活。
```

[取消回复](https://blog.upx8.com/3265#respond-post-3265)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")