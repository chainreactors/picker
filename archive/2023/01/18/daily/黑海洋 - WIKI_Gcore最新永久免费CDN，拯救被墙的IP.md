---
title: Gcore最新永久免费CDN，拯救被墙的IP
url: https://blog.upx8.com/3190
source: 黑海洋 - WIKI
date: 2023-01-18
fetch_date: 2025-10-04T04:09:21.200307
---

# Gcore最新永久免费CDN，拯救被墙的IP

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Gcore最新永久免费CDN，拯救被墙的IP

发布时间:
2023-01-17

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
42919

首先，我们先明确一下，魔术上网的目的是什么？作为从事计算机程序开发的我，需要在github上查一些资料，用youtube看一些教程。有一句话说的很好，真正的墙不是GFW，而是你的思想。你需要甄别，哪些是有用的知识，看到哪些信息只需呵呵一笑了之。如果你已经科学上网，建议不谈政治，不要被一些别有用心的人带了节奏。皮之不存，毛将焉附。如果你仍然不懂，建议读一下晚清的那段历史，想想1937的南京。庆幸自己现在可以坐在温暖的办公室或家里看这篇文章。

**一、Gcore简介**

说起CDN，很多网友知道有[Cloudflare](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaGljYWlyby5jb20vcG9zdC8yMy5odG1s)，AWS CloudFront，阿里云CDN，腾讯云CDN，百度云CDN等等，对于GCore这家公司，可能有些陌生。Gcore是一家起源于俄罗斯的IaaS服务提供商，最初创立于2011年，现在总部位于卢森堡，在德国、立陶宛、波兰、格鲁吉亚和塞浦路斯设有办事处。该公司在全球拥有约140个PoP，在CDN服务商中算网络体量很大的，据官网描述，网络容量达到100Tbps左右。

Gcore提供免费计划套餐：

* 每个月1T流量
* 每月10亿次请求
* 官方有140+节点加速（免费计划每月那么多）
* 支持SSL
* 支持WebSocket
* 提供DDoS防护，基础 WAF
* 不用绑定信用卡

**二、Gcore账号注册**

官方注册地址：[https://auth.gcore.com/login/signup?lang=en](https://blog.upx8.com/go/aHR0cHM6Ly9hdXRoLmdjb3JlLmNvbS9sb2dpbi9zaWdudXA_bGFuZz1lbg)

注册很简单，只需要一个邮箱，打开上述注册地址，填入邮箱及密码注册后，会收到一封激活邮件，激活一下账号即可。

![01.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668168488556704.webp "01.webp")**三、使用Gcore CDN进行流量中转**

1、远程服务器端使用本站提供的[魔术上网](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaGljYWlyby5jb20vcG9zdC8xMi5odG1s)。

Bash

```
bash <(curl -sL https://raw.githubusercontent.com/hiifeng/v2ray/main/install_v2ray.sh)
```

* 本教程中我所使用的伪装域名：example.ifeng.ml
* 伪装路径：/example
* Nginx监听端口：2083

2、首次登录，我们会看到如下界面，服务我们选择CDN。

![02.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668168504637617.webp "02.webp")

3、选择免费计划。

![2-1.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668168710593381.webp "2-1.webp")

4、服务激活后，会出现如下界面。选择“Create CDN resource”。![03.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668168521283568.webp "03.webp")

5、选择“Accelerate and protect entire site”。

![04.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668168535511115.webp "04.webp")

6、输入加速和保护的站点（伪装域名）。例如：example.ifeng.ml

![05.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169213150462.webp "05.webp")

7、提示添加dns记录，由于我们安装v2ray时，已经将伪装域名解析到vps服务器，所以已经直接扫描出来，直接点击“Confirm”即可。如果记录为空，请检查域名填写是否正确，dns是否正常解析。在这里也可以手动添加dns记录。

![06.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169230665992.webp "06.webp")

8、提示修改域名解析服务器，我们直接点击“Confirm”。

![07.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169245424724.webp "07.webp")

9、出现“Quick options setup”，我们先点击“Confirm”，然后点击“Open resource settings”。

![08.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169262305757.webp "08.webp")

10、出现资源设置界面，首先设置回源协议，回源协议默认时http，由于我们在第1步安装v2ray时，选择了tls，所以，这里改为https后保存。

![09.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169279143669.webp "09.webp")

如果在安装v2ray+VMESS+websocket+TLS+Nginx时，没有使用默认443端口，例如我使用了2083，请点击上图中的“Edit this group”修改端口。

![10.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169299555704.webp "10.webp")

11、设置伪装域名的cname记录，首先点击页面左侧的“DNS”，然后点击页面右侧你需要设置的域名。

![11.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169312429642.webp "11.webp")**备注：如果你的域名使用gcore的dns服务，就不用设置cname记录，12-13步无需操作。**

12、点击伪装域名行后面的“铅笔”按钮，然后点击左侧的“CDN Integration”按钮，copy主机别名（例如：cl-gl97cbfeaa.gcdn.co）后关闭窗口。

![12.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169346273943.webp "12.webp")13、进入你的域名的管理页面，先删除伪装域名的A记录和AAAA记录，然后新增一个cname记录。例如，我的域名管理使用的是Cloudflare。

![13.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169418401749.webp "13.webp")

**注意：如果你和我一样，域名管理也使用的是Cloudflare，请关闭proxy，使用dns only模式。**

14、然后再次点击页面左侧的“CDN”，点击“CDN resources”后，再点击页面右侧你的域名，再次进入资源设置界面。

![14.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169491309651.webp "14.webp")15、打开Enable HTTPS，请申请ssl证书。这个设置的作用是，客户端到Gcore节点之间数据使用加密传输。

![15.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169511850049.webp "15.webp")

**注意：证书颁发大约需要十几分钟时间，你可以刷新页面查询证书颁发状态，如果按钮上显示“Abort Let's Encrypt certificate issuing”，说明正在颁发证书，请耐心等待。如果按钮上显示“Revoke Let's Encrypt certificate”，说明证书颁发成功。**

![16.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169530645327.webp "16.webp")![17.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169544913093.webp "17.webp")

16、在浏览器上打开伪装域名加路径，页面会显示Bad Request。说明套Gcore CDN成功。

![18.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169571594105.webp "18.webp")

**四、Gcore CDN优选IP**

经过我的测试，使用Gcore CDN免费套餐，Gcore默认分配的ipv6节点拒绝访问。同时ipv4节点出现减速现象。因此，优选ip是必要的。 不过网上已经有人分享了优选IP的方法，其中不良林的方法我认为是最好用的。

1、打开优选ip网页（[https://api.buliang0.cf/gcore](https://blog.upx8.com/go/aHR0cHM6Ly9hcGkuYnVsaWFuZzAuY2YvZ2NvcmU)），将节点信息copy进去，然后提取节点。将提取的节点考出。

![19.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169681907774.webp "19.webp")

2、下载优选工具（[https://github.com/bulianglin/demo/blob/main/nodesCatch-V2.0.rar?raw=true](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2J1bGlhbmdsaW4vZGVtby9ibG9iL21haW4vbm9kZXNDYXRjaC1WMi4wLnJhcj9yYXc9dHJ1ZQ)），解压后运行nodesCatch.exe。右键从剪贴板导入节点。

![20.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169718798023.webp "20.webp")

“测延迟内核”和“测下载内核”均选择Xray，然后按Ctrl+A键，全选节点后点击鼠标右键，选择“测试服务器连接速度”。

![21.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169750845327.webp "21.webp")

当窗口底部出现“测速执行完成”时，点击测试结果进行排序，将超时和重复的节点删除。

![22.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169780832447.webp "22.webp")

然后按Ctrl+A键，全选节点后点击鼠标右键，选择“测试服务器下载速度”，当窗口底部出现“测速执行完成”时，按照测试结果进行排序，下载速度最快的即为优选出来的IP。

![23.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668169961111403.webp "23.webp")

我们在使用[https://www.speedtest.net](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuc3BlZWR0ZXN0Lm5ldC8)进行测速，结果如下图，基本可以把我的宽带跑满了。（备注：我的宽带下行200M，上行30M）

![24.webp](https://www.hicairo.com/zb_users/upload/2022/11/202211111668170175687327.webp "24.webp")

**五、其他说明**

1、Gcore CDN免费版套餐不支持ipv6回源。

2、如果你的回源端口不是默认的443或80端口，套CDN后，使用浏览器打开伪装域名测试，在输入网址时，最后不需要加":port"。例如本例中，在没套CDN前，我输入的网址是https://example.ifeng.ml:2083/example,套CND后，需要去掉端口，使用https://example.ifeng.ml/example访问。

[取消回复](https://blog.upx8.com/3190#respond-post-3190)

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