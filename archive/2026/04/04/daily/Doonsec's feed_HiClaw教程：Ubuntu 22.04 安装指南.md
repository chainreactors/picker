---
title: HiClaw教程：Ubuntu 22.04 安装指南
url: https://mp.weixin.qq.com/s/6tixPgpm-i0M2w39m4q4dA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:33:28.041894
---

# HiClaw教程：Ubuntu 22.04 安装指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnC2J9hUicHMShmLuzA6B7ucv34BlzHvISOCV7LptLXaa1YvEt5ymB35eMTFDc9JBqyjogYMAdzPpO5eB6PYNGrpgRhqcPqIB6w/0?wx_fmt=jpeg)

# HiClaw教程：Ubuntu 22.04 安装指南

HiClaw
HiClaw

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

## 1. 更新系统

先更新软件包索引并安装最新补丁：

apt update -y

## 2. 配置 Swap（可选）

内存紧张时可启用 Swap 分区缓解。建议 8GB（仅限非关键场景，物理内存够用则跳过此步）：

# 创建 8G swap 文件
sudo fallocate -l 8G /swapfile

# 设置权限
sudo chmod 600 /swapfile

# 格式化为 swap
sudo mkswap /swapfile

# 启用 swap
sudo swapon /swapfile

# 写入 fstab（开机自动挂载）
echo "/swapfile swap swap defaults 0 0" | sudo tee -a /etc/fstab

# 设置 swappiness 为 30
sudo sed -i '/vm.swappiness/d' /etc/sysctl.conf
echo "vm.swappiness = 30" | sudo tee -a /etc/sysctl.conf

## 3. 重启生效

reboot

## 4. 安装 Docker

推荐使用 linuxmirrors.cn 的一键安装脚本，自动配置国内源：

bash <(curl -sSL https://linuxmirrors.cn/docker.sh)

安装完成后验证：

docker --version
docker compose version

![](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImlWoQaPSBKr6N2Y5Tw6VP8RZh08uGD5pj3LuNT2BpccGS3JbXPfk7w3icFg282hgJib2PboJK43pdYhOrwTIKC2IDWLPMgxBc2VQ/640?wx_fmt=other&from=appmsg)

## 5. 安装 HiClaw

运行官方安装脚本：

bash <(curl -sSL https://higress.ai/hiclaw/install.sh)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImns9psibpyLico8oyVeAibaO9EZIrFLPjhcdKxPkozcmaIUqLFr00mUhOjJaUjD4vUauM5or4vVwuHpLD8ic94ricwgcm4wcvrHYaFM/640?wx_fmt=other&from=appmsg)

### 5.1 配置 AI 服务商

安装程序会引导你配置 AI 服务商。本文以 MiniMax Coding Plan 为例：

• 订阅地址：https://platform.minimaxi.com/subscribe/token-plan?code=GoU2vXae4D&source=link

• Base URL：`https://api.minimaxi.com/v1`

![](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImkQgUDkd6rlewy0m25QA6uiafKtaUdtpgFMX6QVjAq7nK9CLu627jJtMjSjuXu5dqXTicO8E8SBjW9qbuMkWvm7GD3OeVyicBwvao/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImmEFb7icwDv5le9UwhrKeqggORl1uepE4KicWdOGS5FZgdaAxjiaVBr0YFAMUmMutnKE4HUoolNLA0d8qdbNv0Fcic5nHHvtGDKj5s/640?wx_fmt=other&from=appmsg)

如果不需要配置自定义域名，后续步骤直接回车即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImmp9hso9rdssNtlb0dzh3ThiaCUcIXOBdvsfgVsmwCNSDSoFlQA7PABy5KJsaM0rt7E6KQgR5B6ibu4NxPJ772llVYtSiaDibgaQmQ/640?wx_fmt=other&from=appmsg)

### 5.2 选择 Runtime

可以选择 CoPaw 或 OpenClaw 作为运行环境，根据实际需求选择：

![](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImlXFicIibEYArSXommsibWXbKib7tGia2V1cHsaAO5gOEbliaickCNob0iaP3TbogQd7ELicGvnficwsErJJuumyr5UZ86hn2vibq7HPZ1kGI/640?wx_fmt=other&from=appmsg)

其余步骤保持默认，回车确认即可：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImnLVTayXBZwaIv300ytlV2gsBC3WGLOL1bhbfBX15aZg9nWcVyF1WVc7FhS038Opk2mrOTf10BQialCyVEvM2wggbjta4FYCdkE/640?wx_fmt=other&from=appmsg)

## 6. 安装完成

看到以下界面即表示安装成功：

![](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnGW7x9kMLia5wNBNoFhhJ43JRXNTwR7cIibUkAQibJx4FklUsBibAeW0icOOvOhHCMNjzBQHib0jeUjaqGerjUq7jhdroDia1N13ryGs/640?wx_fmt=other&from=appmsg)

## 7. 更多资料

Ima 知识库：搜索「HiClaw深度实践」获取完整文档和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImn13mxfzKGIt5QT2dnI2El11kPWuY3j3vuE3kyQFxlic0Hd3Cib6xEbwAf9fOtJycW8MpOPw2ZxHYNyOW3kibthuyvbjRhPYM9w2U/640?wx_fmt=other&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

爱唠叨的Nil

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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