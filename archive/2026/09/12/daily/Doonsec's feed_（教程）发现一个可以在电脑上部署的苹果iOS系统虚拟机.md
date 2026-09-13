---
title: （教程）发现一个可以在电脑上部署的苹果iOS系统虚拟机
url: https://mp.weixin.qq.com/s/hq5bDDZI73QqmVM_iWwnDA
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:12.625559
---

# （教程）发现一个可以在电脑上部署的苹果iOS系统虚拟机

# （教程）发现一个可以在电脑上部署的苹果iOS系统虚拟机

像梦又似花

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

直接就是越狱版本，还是开源的。这以后就不用买苹果手机了？

仓库地址：https://github.com/34306/vphone-aio

![](https://mmbiz.qpic.cn/mmbiz_jpg/01RLQI6qOeDUyIjYX7v5ibFYet6hNZtH67RbIXgEvgEhdU0vBUnrJEIyUQFosVEhnR41Hbnff2v0A5vTnEN9SlgkTr2L2ToaHfhkjImEvvRQ/640?wx_fmt=jpeg)

好了进入教程环节：

**vphone-aio**

有人又在 X（Twitter）上随机转发了这个项目，我的仓库再次爆火。我更推荐使用 vphone-cli，它更新更好、支持更完善。目前 vphone-cli 仓库已经支持 iOS 27。

一条脚本运行 vphone（iOS 26.1），已经越狱并安装了完整的 bootstrap。

请按以下步骤操作：

1. 安装前置依赖：

   ```
   brew install git-lfs wget zstd libimobiledevice
   ```
2. 关闭 SIP，并设置 `amfi_get_out_of_my_way=1`
3. 下载或克隆本仓库（可能需要一些时间，对我来说 12GB 大约需要 20 分钟）
4. 如果缺少任何分片文件，脚本会自动下载。你也可以手动下载：

   ```
   for p in aa ab ac ad ae af ag; do
     wget -O "vphone-cli.tar.zst.part_${p}" \
       "https://github.com/34306/vphone-aio/raw/refs/heads/main/vphone-cli.tar.zst.part_${p}?download="
   done
   ```
5. 运行 `vphone-aio.sh` 脚本
6. 确保你的设备有超过 128GB 的可用空间（推荐）
7. 等待合并完成。完成后会解压整个文件夹（大约需要 15 分钟）
8. 合并完成后，可以删除 `.git` 和分片文件
9. 连接 VNC（使用 RealVNC 或屏幕共享）：`vnc://127.0.0.1:5901`
10. 享受吧！
11. SHA-256 校验和

用于验证下载的文件是否损坏：

```
3c966247deae3fff51a640f6204e0fafc14fd5c76353ba8f28f20f7d1d29e693  vphone-cli.tar.zst.part_aa
c7d11bbbe32dda2b337933c736171cc94faab2c7465e75391fa49029f3b6f1b1  vphone-cli.tar.zst.part_ab
f422949080e7f141f32f35f8ea20c1fedffc2b97eadf0390645114feef6bb1aa  vphone-cli.tar.zst.part_ac
f3acfa47145207b8962ba4d20fb83eb4646934cca768906e65609d7fdde564e7  vphone-cli.tar.zst.part_ad
efdca69df80386b0aa7af8ac260d9ac576ed1f258429fd4ac21b5bbb87cd78fe  vphone-cli.tar.zst.part_ae
4628852da12949361d3ea6efcf8af1532eb52194cc43a4ab4993024267947587  vphone-cli.tar.zst.part_af
8bd1551511eb016325918c2d93519829be04feb54727612e74c32e4299670a88  vphone-cli.tar.zst.part_ag
```

你可以手动验证：

```
shasum -a 256 vphone-cli.tar.zst.part_a*
```

# 预览

#

#

# 致谢

* wh1te4ver (Hyungyu Seo) 提供了非常详细的教程：https://github.com/wh1te4ever/super-tart-vphone-writeup
* Lakr233 提供了 非 tart 版本的 vphone (vphone-cli)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/biachO2ia6rWDwdCSxVdTQ1dAqoicGYf8ricD6BuiaEU64urHUGmkzsUDfD8rqWibx2KXE40wesg6s5AInjvy5FjqCWQ/0?wx_fmt=png)

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