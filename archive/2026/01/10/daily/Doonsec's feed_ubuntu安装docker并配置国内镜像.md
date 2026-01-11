---
title: ubuntu安装docker并配置国内镜像
url: https://mp.weixin.qq.com/s/Zz356Upd1fMBJKfudw8S_w
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:48.020100
---

# ubuntu安装docker并配置国内镜像

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/meR9vVNE209JID4DiczF8V0INfYSbugqIdjWV9EH15GNOxBlNkvfbaRQLHrKkykqlZXTtQFqpYbFZNW8nB8CX0Q/0?wx_fmt=jpeg)

# ubuntu安装docker并配置国内镜像

原创

qife

网络安全技术点滴分享

![]()

在小说阅读器中沉浸阅读

一、使用官方安装脚本自动安装（简单方便，需要点魔法）

```
# 下载并执行Docker官方安装脚本curl -fsSL https://get.docker.com -o get-docker.shsudo sh get-docker.sh
# 启动Docker服务sudo systemctl start dockersudo systemctl enable docker
```

没有魔法的话可能会报错，如下所示

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqIiaSKAa0GCQA1UkFdEJClvO9WQdHGl48SI8qnIQ61l5bTeUSqNaRSibtQ/640?wx_fmt=png&from=appmsg)

二、手动安装

1.卸载旧版本

```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

2.使用docker仓库进行安装

（1）设置仓库

更新apt包

```
sudo apt-get update
```

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqIcdnLLRX087RISViaiaLrr4oZWUsq0tgvv4vXvma1GdhbVPQ7MoQiaoyDg/640?wx_fmt=png&from=appmsg)

安装apt依赖包

```
sudo apt-get install \    apt-transport-https \    ca-certificates \    curl \    gnupg-agent \    software-properties-common
```

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqI4SI4IjmWHQAUTAZSoJb9jUriaNbuicHPgibaEL5LyJu7hIbbzGVhVPxDg/640?wx_fmt=png&from=appmsg)

添加docker的官方GPG密钥

```
sudo curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqI6s2W80tETg65dOIYessnw7YBJZvibWQZ4P1oHatEgnBiceqEsNgKwiaPw/640?wx_fmt=png&from=appmsg)

设置稳定版仓库

```
echo \  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/ \  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \  sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt-get update
```

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqI6vdAPCwnz2ezP97hO2gkNnDiaW8HbfXtlJMg1NIEhggC0yklPJJQOnA/640?wx_fmt=png&from=appmsg)

再次更新apt包

```
sudo apt-get update
```

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqIhEB0kYFByP4Yo8DOoTNicngODKgA2QN3MtQQyS1boOJB32ic0BocUNMg/640?wx_fmt=png&from=appmsg)

（2）安装最新版本的 Docker Engine-Community 和 containerd

```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqIdXtSmrdoBibW2rzSzXRqXFib9NKQfPAx8Jh0AYibjAnkfPz4h1EibTE5jg/640?wx_fmt=png&from=appmsg)

（3）测试docker是否安装成功

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE209JID4DiczF8V0INfYSbugqIgmN1d4yFeSBzBgPAzrFEwLXkyTQicDArTA8nXbIT3MhwtP8sTv25ShA/640?wx_fmt=png&from=appmsg)

证明docker已安装成功

（4）设置docker国内镜像

如果拉取docker镜像报错，如下所示，则需要设置docker国内镜像

![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208bXiaVQ3xebNZzXGBZc30gxic81ciazZkmo4Qxv1ick3iadHiaBlTJhic2sgvjN8etibb3zdh1vIACpxcARA/640?wx_fmt=png&from=appmsg)

创建或修改/etc/docker/daemon.json，如下所示

```
sudo mkdir -p /etc/docker
```

```
sudo tee /etc/docker/daemon.json <<EOF{    "registry-mirrors": [        "https://docker.1ms.run"    ]}EOF
```

```
//重启docker再拉docker镜像试试sudo systemctl daemon-reloadsudo systemctl restart docker//这个镜像源还是挺稳定的https://1ms.run/
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/meR9vVNE20ichIC5CurLA1tUgYCT4X8zzPpAMjZeqetgGibS4fbibclib7OVichznCM2aa09rdSaRl7buCoexZuVY5w/0?wx_fmt=png)

网络安全技术点滴分享

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/meR9vVNE20ichIC5CurLA1tUgYCT4X8zzPpAMjZeqetgGibS4fbibclib7OVichznCM2aa09rdSaRl7buCoexZuVY5w/0?wx_fmt=png)

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