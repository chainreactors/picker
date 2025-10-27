---
title: Tailscale自建(Headscale)记录 - potatso
url: https://www.cnblogs.com/potatso/p/18914979
source: 博客园 - potatso
date: 2025-06-07
fetch_date: 2025-10-06T22:50:17.585236
---

# Tailscale自建(Headscale)记录 - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Tailscale自建(Headscale，derp)记录](https://www.cnblogs.com/potatso/p/18914979 "发布于 2025-06-06 21:27")

1. 下载依赖
   直接下载headscale的deb安装包即可。
   <https://github.com/juanfont/headscale/releases/download/v0.26.1/headscale_0.26.1_linux_amd64.deb>
2. 配置
   通过deb可以一键安装，省去很多麻烦，安装后提示的内容如下

```
 headscale package has been successfully installed.

 Please follow the next steps to start the software:

    sudo systemctl enable headscale
    sudo systemctl start headscale

 Configuration settings can be adjusted here:
    /etc/headscale/config.yaml
```

修改配置文件 `/etc/headscale/config.yaml`中你需要修改的部分，一般就是监听地址和dns

```
修改以下的节点信息
server_url: http://XXX.XXX.XXX.XXX:8080  # 这里填写你的实际外网地址,域名或ip都可以
listen_addr: 0.0.0.0:8080
metrics_listen_addr: 0.0.0.0:9090
ip_prefixes:
  - fd7a:115c:a1e0::/48
  - 10.1.0.0/16
randomize_client_port: true
# 修改对自己来说方便的DNS，可以保持默认
dns_config:
	nameservers:
		- 223.5.5.5
# 建议关闭Magic DNS，否则有可能造成客户端无法正常上网
magic_dns: false
# 修改Socket存储位置
unix_socket: /var/run/headscale/headscale.sock
```

根据提示，复制命令到server执行即可。在这之前需要新建一个用户

```
headscale users create thinkpad
```

# 各终端加入节点方法

## Windows

tailscale login --login-server [http://你的域名或ip:8080](http://xn--ip-0p3cj1pytflqs6w7a:8080)

# 获取返回的命令

headscale -n 命名空间 nodes register --key nodekey:上面这行命令返回结果的key

# 到Headscale服务器上执行返回的命令

## Linux

我的系统是linux，在客户端只需要执行

```
sudo tailscale up --login-server=http://xxxx:58080 --accept-routes=true --accept-dns=false
[sudo]  的密码：

To authenticate, visit:

	http://0.0.0.0:58080/register/-4S61FkilWFRm1Z1iH6es4Tn
```

# 自建derp服务器

直接使用前人配置好的docker镜像即可

<https://hub.docker.com/r/javaow/tailscale-derp>

Headscale 的本地 YAML 文件目前还不支持`InsecureForTests`这个配置项，所以没办法，目前只能使用在线 URL 了。

```
{
  "Regions": {
    "901": {
      "RegionID": 901,
      "RegionCode": "ali-sh",
      "RegionName": "Aliyun Shanghai",
      "Nodes": [
        {
          "Name": "901a",
          "RegionID": 901,
          "DERPPort": 443,
          "HostName": "xxxx",
          "IPv4": "xxxx",
          "InsecureForTests": true
        }
      ]
    }
  }
}
```

配置说明：

HostName 直接填 derper 的公网 IP，即和 IPv4 的值相同。

InsecureForTests 一定要设置为 true，以跳过域名验证。

需要把这个 JSON 文件变成 Headscale 服务器可以访问的 URL，比如在 Headscale 主机上搭个 Nginx，或者上传到对象存储（比如阿里云 OSS）。

一样的修改Headscale 的配置文件

```
# /etc/headscale/config.yaml
derp:
  server:
    # 不启用官网自带的derp
    enabled: false
  urls:
    - https://xxxxx/derp.json
  paths:
    # - /etc/headscale/derp.yaml
  # paths: []
```

# 检查

成功后的样子

```
tailscale netcheck

Report:
	* Time: 2025-06-07T06:44:23.298840441Z
	* UDP: true
	* IPv4: yes, xxxxx:49849
	* IPv6: no, but OS has support
	* MappingVariesByDestIP:
	* PortMapping: UPnP
	* CaptivePortal: false
	* Nearest DERP: Aliyun ChengDu
	* DERP latency:
		-  cd: 10.4ms  (Aliyun ChengDu)
```

posted @
2025-06-06 21:27
[potatso](https://www.cnblogs.com/potatso)
阅读(439)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025