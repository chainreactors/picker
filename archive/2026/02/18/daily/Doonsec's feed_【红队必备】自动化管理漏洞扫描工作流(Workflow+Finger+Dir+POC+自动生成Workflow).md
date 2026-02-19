---
title: 【红队必备】自动化管理漏洞扫描工作流(Workflow+Finger+Dir+POC+自动生成Workflow)
url: https://mp.weixin.qq.com/s/I_bdJi3A1-fGAwbp8jLc5Q
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:15:53.996361
---

# 【红队必备】自动化管理漏洞扫描工作流(Workflow+Finger+Dir+POC+自动生成Workflow)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwHicJvscHIBJP6BnADurHRbuVO2JJegxWBUBKULx41CVkkJWvMRAe0ZxgPYq9X0bNDwdcqnP8AYyMEXyywzV5Qy9hmRFZTyHjY/0?wx_fmt=jpeg)

# 【红队必备】自动化管理漏洞扫描工作流(Workflow+Finger+Dir+POC+自动生成Workflow)

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

## 工具简介

>     请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**。
>
> ***项目地址在文章底部哦***

DLDL是一款桌面端漏洞扫描工作流管理工具，支持自动关联指纹库与POC库、批量生成扫描配置，适合需要维护大量安全检测规则的安全测试人员。

## 📥 工具使用

### Workflow 管理

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODz0YiaYxShR2VYibZBkibsBd2fJMKj6I6kUhvZ97V4VDDmb3mr0vhMHGuQvLKTfocrVEicXRFhnqqTDaleLZk6PY5u1OiccRYpTK6P8/640?wx_fmt=png&from=appmsg)

### Finger 管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwxuyhmRMK1zfjetaJX0sp5JpBwduyjPHtaib8GT51s2JCKAlhJwVxFOV6X3qbb4Vz2GjaZkz5VSLib04tq0VpU6tylViaDwriatib4/640?wx_fmt=png&from=appmsg)

### Dir管理

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwVx1Vicf7LicicZV424zuxia75aX5JvGYRicDGLWO0FAvt8PoI8bDCSoZiaz54BhV2hDsy1nhZQPia0aoicw4kicHwrUicFicThQRpQAcdoY/640?wx_fmt=png&from=appmsg)

### POC管理

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODz9BmVvVUe06zGc6WmApAoQTDPZmRAiaoypeXDALORzytQBwkPNbv7TkiaSAgD8g0NTYLcDkR5VJWEjccf2NiaDJ6Mbf5SKcXicIWc/640?wx_fmt=png&from=appmsg)

### 自动生成Workflow

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzNibFOoZkMUwfX1kfSB3MQibK0IFZM5ibaj4DM8rry79Dpfu8m60Zs7qy4HX74NWkcSkPrkKTeCl5LibKH8D3NygCAWHwTzLak4P0/640?wx_fmt=png&from=appmsg)

## ✨ 主要功能

| 功能 | 说明 |
| --- | --- |
| 指纹管理 | 导入/编辑指纹识别规则，内置5000+常见产品规则 |
| POC管理 | 导入/编辑漏洞验证代码，支持YAML格式 |
| 自动生成Workflow | 根据指纹关键字自动匹配关联POC，一键生成扫描工作流 |
| 可视化编辑 | Web界面批量增删改Workflow，支持搜索筛选 |
| 配置导入导出 | YAML格式备份与恢复，便于团队协作 |

---

## 🧩 核心概念

使用DLDL前需要理解三个对象：

**Finger（指纹）**

识别目标系统类型和版本。例如识别出目标运行Nginx 1.18.0或Apache 2.4.41。

**POC（漏洞验证代码）**

验证特定漏洞是否存在。例如检测CVE-2021-29441 Nginx RCE漏洞。

**Workflow（工作流）**

将Finger和POC关联的配置文件。定义"识别到某指纹后，调用哪些POC、以什么方式扫描"。

Workflow分三种扫描类型：

| 类型 | 扫描范围 | 示例 |
| --- | --- | --- |
| Root | 目标根路径 | `http://target.com/` |
| Dir | 各级子目录 | `http://target.com/admin/` |
| Base | 指定完整路径 | `http://target.com/manager/html` |

---

## 📝 使用说明

**第一步：导入基础数据**

1. 进入「Finger管理」，导入指纹库YAML文件，点击「保存到文件」
2. 进入「POC管理」，导入POC库YAML文件，点击「保存到文件」

**第二步：自动生成Workflow**

1. 进入「自动生成Workflow」
2. 匹配方式：建议同时勾选"按文件名/名称匹配"和"按全称全文搜索"
3. 扫描类型：根据需求勾选Root/Dir/Base，不确定则全选
4. POC范围：首次使用选"全部POC"
5. 点击「开始生成」，等待任务完成

**第三步：手动调整**

1. 进入「Workflow编辑」
2. 使用搜索框或筛选条件定位需要调整的Workflow
3. 编辑指纹信息、增删POC关联、修改扫描类型
4. 点击「保存到文件」写入`workflow.yaml`

**第四步：启动扫描**

配置目标列表，启动扫描任务查看结果。

---

## 🔧 配置参考

Workflow配置文件为YAML格式，核心结构如下：

```
# 指纹名称
finger_name: "Nginx"

# 关联的POC列表
pocs:
  - "CVE-2021-29441.yaml"
  - "nginx-config-error.yaml"

# 扫描类型：root/dir/base
scan_type: "root"

# 其他指纹规则...
```

---

## ⚠️ 注意事项

**POC命名建议**

文件名中包含产品名可提升自动匹配准确度，例如：

```
CVE-2021-12345_nginx.yaml
CVE-2021-12346_apache.yaml
```

**生成任务卡住**

点击「终止任务」后检查：

* 导入的YAML格式是否正确
* 尝试减少POC范围后重新生成

**备份配置**

定期导出以下文件：

* `finger.yaml` - 指纹配置
* `pocs.yaml` - POC配置
* `workflow.yaml` - 工作流配置

---

## 📚 进阶场景

**针对性测试**

已知目标均为Nginx，只想测试相关漏洞：

1. 「POC管理」中搜索"nginx"并勾选相关POC
2. 「自动生成Workflow」中选择「已选择的POC」
3. 开始生成

**补充漏掉的POC**

发现某指纹应关联某POC但未自动生成：

1. 「Workflow编辑」中搜索该指纹
2. 进入编辑页面，在POC列表中勾选漏掉的项
3. 保存

**批量更新POC库**

POC库更新后重新关联：

1. 「POC管理」导入新库并保存
2. 「自动生成Workflow」重新生成全部Workflow
3. 或在编辑器中手动批量更换

## 📖 项目地址

```
https://github.com/Yn8rt/DLDL
```

## 💻 威胁情报推送群

>   如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。
>
>  如果师傅们想要获取**网络安全相关知识内容**，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
>
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

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