---
title: 云安全-对象存储s3/oss/cos测试方式总结
url: https://mp.weixin.qq.com/s/2IXNTswryOqSD9veTK8iMg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:27:12.013480
---

# 云安全-对象存储s3/oss/cos测试方式总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwqWRXM2UX9QFKMZSicP6hHlicqxSDOf2O0fFznlLIbMHXlkvs9QKenRPw/0?wx_fmt=jpeg)

# 云安全-对象存储s3/oss/cos测试方式总结

原创

selfiv

溪於security

![]()

在小说阅读器中沉浸阅读

> 参考来源：
>
> * • https://wiki.teamssix.com/
> * T Wiki 遵循 CC BY-NC 4.0 (opens new window)国际许可协议
> * • https://github.com/HXSecurity/TerraformGoat
> * TerraformGoat 是一个支持多云的云场景漏洞靶场搭建工具
>
> 本公众号分享的网络安全技术仅供合法授权测试与防御研究使用，严禁任何未经授权的渗透测试行为！！

# 概览

对象存储（Object-Based Storage），也可以叫做面向对象的存储，国内阿里云将其称为OSS，腾讯云则是COS，本质上都是一样的。

Amazon S3 (Simple Storage Service) 简单存储服务，是 Amazon 的公开云存储服务，与之对应的协议被称为 S3 协议，目前 S3 协议已经被视为公认的行业标准协议，因此目前国内主流的对象存储厂商基本上都会支持 S3 协议。

‍

在 Amazon S3 标准下中，对象存储中可以有多个桶（Bucket），然后把对象（Object）放在桶里，对象又包含了三个部分：Key、Data 和Metadata。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwSqSM0baD2TGsiaAwncXyUyljBYvF5gNx7lLrExX83ia9pibjn7wvcYODg/640?wx_fmt=png&from=appmsg)

image

* • Key是对象在存储桶中的唯一标识符，用以区分各个不同的对象，例如 `https://teamssix.s3.ap-northeast-2.amazonaws.com/aaa00e12j34kj` 这里的 `aaa00e12j34kj` 即Key
* • Data就很好理解，即存储的数据本身
* • Metadata 即元数据，可以简单理解成数据的标签、描述之类的信息，不同于传统的文件存储直接将这类元信息封装在文件本身，对象存储采用这种方式可以大大加快对象的排序、分类和查找

‍

操作和使用s3的方式通常包括以下几种：

* • AWS 图形化控制台操作
* • AWS cli工具
* • AWS SDK操作
* • **AWS提供的Restful Api操作**

‍

值得注意的是，**Minio**是将**Amazon S3的API协议原封不动地搬到本地（或私有云）环境里面的一套对象存储服务**，可用二进制单文件/Docker一键启动。

而Minio因默认安全策略不严格，往往比各大云厂商提供的S3服务更容易出现因配置不当导致的安全问题。

‍

S3常见攻击面各厂商拆解，打勾即为可利用：

| 攻击方式／厂商 | Google Cloud Storage | Microsoft Azure Storage | 华为云 OBS | Amazon S3 | 腾讯云 COS | 阿里云 OSS |
| --- | --- | --- | --- | --- | --- | --- |
| Bucket 公开访问 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bucket 名称爆破 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 特定的 Bucket 策略配置 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Bucket Object 遍历 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 任意文件上传 | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| 文件覆盖 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| AccessKeyId、SecretAccessKey 泄露 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bucket 接管 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| Bucket ACL 可写 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Object ACL 可写 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bucket 策略可写 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

# 创建s3服务

这里我们参照wiki，自己来创建一个阿里云的s3服务的Bucket，来到阿里云的OSS控制台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwE7o7gxeIF9EdgXDGkEnLpmydLMmTsH2Gib6vf92IodhjXS0E7VXoVPw/640?wx_fmt=png&from=appmsg)

配置过程中，可以打开阿里云的文档，选择适合自己的配置方式，我这里只是一个测试桶，就全部默认配置了

注意这里Bucket默认权限配置是只允许私有的，也就是读写都需要进行身份验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwtIolh8ZROhibVtG2THL2b2kls4eYp7N8N4QyqQ3lveL8gOjwFsPh2qw/640?wx_fmt=png&from=appmsg)

其他复杂功能我们也暂不开启，只是用于演示，创建好之后，进入该Bucket的控制台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5Gw6Muic7LFria95tH6esWQbEDggibD3Tc1lhdcdjoLKzicM8c256cwy03ibng/640?wx_fmt=png&from=appmsg)

我这里为了演示，需要在权限控制中开启允许公共访问，也就是无需携带身份信息即可读/写

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5Gwg0BjcobEwvXHQga9brdrUBsDGnXPXLOUcbrsib1jDAo6WPyVYvrZhMw/640?wx_fmt=png&from=appmsg)

接下来，上传一个文件，进入上传图片的页面，这里就可以配置对象的权限了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5Gw8aZMroo6p4Uh4OibNHwmUptviaMzGkhDicDVkFibBBhnnNYFYQMUv8FaPg/640?wx_fmt=png&from=appmsg)

继承自Bucket或者私有，都可以理解为私有权限，也就是读写都需认证，公共读即可读不可写，公共读写即无需认证即可读取/写入，我这里配置为公共读

访问域名可以选择阿里云自带的公网域名，也可以选择配置自己的域名（需要自己填好域名解析信息），我这里选择用阿里云的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwXPBVhUsicUWdUUicCLtl3iajtGoN0IF3cNpVg0Cxk7w8pyHf92wnPFBBQ/640?wx_fmt=png&from=appmsg)

访问链接，就拿到我们刚刚上传的图片了

‍

# Bucket爆破

这里指的是爆破Bucket的名称，通常来说Bucket名称爆破很像子域名爆破，因为s3存储url总是类似这样

`https://[bucket_name].s3.ap-northeast-2.amazonaws.com/key`

当然，并不局限于这种形式，如果是自建域名/自建minio，也可以是 `xxxs3.baidu.com` 这种域名

我们可以通过页面返回的内容来判断是否爆破成功，如Bucket不存在会显示为NoSuchBucket，各家会有小差异

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwSYlOcZp03p0oKHqzIsKheIBUgv7hav1ujqYOwUwe8d6OmJlOcdibicNA/640?wx_fmt=png&from=appmsg)

如图，阿里云，该桶存在则显示为AccessDenied（不同厂商的返回内容可能有差异，有的会直接404 403）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwqCj6m2m65JicW3GKg1klGT6d8rs6iaoI3S3onfc638vNLtVLWBFhtsicg/640?wx_fmt=png&from=appmsg)

桶存在的另一种情形是直接列出桶内所有文件（安全配置不当的情况），将key值拼接到url上即可访问对应文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5Gwia9pWaFUa02Dz0NibUkYxoekDXiaKPqWT2AXq5yg325jZavzBiaGfGpLVA/640?wx_fmt=png&from=appmsg)

tips. Bucket爆破也不一定就等于子域名爆破，也可能是下面这种形式

```
baidu-prod.s3.oss.com
aliyun-img.s3.oss.com
tencent-test.s3.oss.com
company-xxx.s3.oss.com
```

如果我们发现了一个叫做`xxx-prod`的Bucket，就去想一想会不会有`xxx-test`、`xxx-dev`，也许能发掘到一些隐形的资产

# Bucket Object遍历

也就是上面说过的，存在列出桶内所有文件的页面，即可批量遍历提取桶内所有文件，可通过特定工具，例如ossx.py、ossFileBrowser

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5Gwia9pWaFUa02Dz0NibUkYxoekDXiaKPqWT2AXq5yg325jZavzBiaGfGpLVA/640?wx_fmt=png&from=appmsg)

测试思路：

* • 通过上传图片等功能，定位到s3的域名

• 信息收集，子域名爆破

# Bucket接管

如果我们打点过程中，在上传图片功能处，或者子域名收集时，发现这样的站点提示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwWicv5ibsllfGD0ZmfQic9oLI3j75licbvyZeWa7tDo4vtfaFRytUShghew/640?wx_fmt=png&from=appmsg)

则该站点可能存在存储桶接管，危害即我们可以接管这个子域名，指向我们控制的桶

可以先通过`nslookup -qt=cname s3.xxx.com`获取到站点的cname记录，判断下是哪家厂商，接下来去对应厂商，创建标签中的名字的桶，即可接管该存储桶，一般来说AWS的桶比较容易出现接管问题

接管存储桶需满足如下条件：

* • 云厂商 **允许第三方创建同名Bucket**
* • Bucket名称是全局唯一的
* • 目标Bucket不存在

‍

# S3 任意文件上传/文件覆盖

如果权限配置不当，例如配置为了公共读写，可能造成任意文件上传与文件覆盖

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GweqavxUQ2PI0uNGBmMZgK0M7fHib7ZW3iciaUbVcqCibhyXOTHibUoSEI8Cg/640?wx_fmt=png&from=appmsg)

访问正常文件，修改为PUT请求方式，在请求体修改数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5Gwq7t6pxSBY7j54BACXrlMLUznM4NHEt4SecJibjr8RaboRNGIJM03wiaA/640?wx_fmt=png&from=appmsg)

再次访问该文件，可以发现文件被覆写了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwyaUibtWrjNekBraFfB7xoibb8QlbTCDRWnsM5mYkJJnm8LGiayLFJb2Zg/640?wx_fmt=png&from=appmsg)

这里测试过程中建议选择自己上传的文件进行PUT覆写测试，不要随便编辑服务器已有的文件

这里危害多半来自于：

* • 桶内敏感数据泄露，例如用户的身份三要素、照片等等
* • 网站引入的js在存储桶汇总，覆盖网站的js，注入恶意代码钓鱼
* • 恶意覆盖正常数据，影响业务运行

# Bucket ACL可写

这里指的是Bucket本身的ACL配置项，也就是说我们可以操作Bucket的权限配置，也是属于错误配置类漏洞，本质上属于将**对象存储的“控制面”暴露给了匿名用户/低权限用户**

部分云厂商安全策略严格，例如阿里云，不会允许存在这种错误配置，也就不存在此类漏洞

‍

我们这里找一台vps，我这里是腾讯云的机器，实际上用哪家无所谓，找到靶场 TerraformGoat 来进行环境搭建，根据vps对应的云厂商选择相应的容器，将容器起起来，进入shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwTbOknD11lz16rgCg5ZdujvQy9iaxUibPLz5WDicSNDJW7TASSWz4zLSIQ/640?wx_fmt=png&from=appmsg)

接下来就可以选择Bucket ACL可写这个漏洞，查看readme文档配置策略，我们这里选择用腾讯云COS存储靶场

进入 /TerraformGoat/tencentcloud/cos/bucket\_acl\_writable 目录，查看配置项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwYaicia6tbYibyeTp0GyMeuianMkWu9Wlod8xSdrKiaWJAbg9YzXywFeo1WA/640?wx_fmt=png&from=appmsg)

需要我们在腾讯云控制台输入secretID和secretKey，那我们去腾讯云，找到两个key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwKqqBn3KibYKKt9bXicbgSuPv40UO8v3skyf2DZQ9FZjBpsJho1MFfclg/640?wx_fmt=png&from=appmsg)

创建API密钥，我这里为了方便直接创建了主账号密钥，自行保存好自己的key，使用完成后请及时销毁，以免余额被盗刷

接下来我们将其写入`terraform.tfvars`配置文件中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwmictyAbYl2s1JYZJ4fKx4Dto3xs6pUyft87iaR4yMLzzUk6WsVib5Blzg/640?wx_fmt=png&from=appmsg)

输入命令`terraform init`进行初始化，`terraform apply`应用即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwRwCLEPGib3WZLRVa8HHRFZOLeUAwhyiaYTBbTwSPn4IUqJBCHV1qLL8Q/640?wx_fmt=png&from=appmsg)

输入yes，这样靶场就启动起来了，给我们提供了一段存储桶的url，访问一下发现acl可读

https://houxian-0s75m-1302944391.cos.ap-beijing.myqcloud.com/?acl

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UxFVo8zKnYzibsUDu8gHydpLsyvHkl5GwxF1t7oHd2KqvCLVuEjiajdqL2SvlibribwWV0u7Qj8B9raBnUAnWMxW6A/640?wx_fmt=png&from=appmsg)

试一下使用PUT方式修改Bucket的ACL策略，原先的策略如下

```
<AccessControlPolicy>
    <Owner>
        <ID>qcs::cam::uin/100015419552:uin/100015419552</ID>
        <DisplayName>qcs::cam::uin/100015419552:uin/100015419552</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
                <ID>qcs::cam::uin/100015419552:uin/100015419552</ID>
         ...