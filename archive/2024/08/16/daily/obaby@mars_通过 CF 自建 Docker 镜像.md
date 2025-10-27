---
title: 通过 CF 自建 Docker 镜像
url: https://h4ck.org.cn/2024/08/17841
source: obaby@mars
date: 2024-08-16
fetch_date: 2025-10-06T18:00:49.513725
---

# 通过 CF 自建 Docker 镜像

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F)

# 通过 CF 自建 Docker 镜像

2024年8月15日
[52 条评论](https://h4ck.org.cn/2024/08/17841#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG495.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG495.jpg)

得益于\*\*\*，目前需要代理的服务越来越多了，至于为什么需要代理，参考前面\*\*\*部分。

昨天现在服务器上安装个 mqtt 的服务，这次不想直接装了，想通过 docker 来装一个，主要是服务器上跑的业务太多了，怕源码安装或者通过其他安装产生一些不必要的麻烦。

结果在服务器运行安装，直接芭比了，这倒是也在意料之内，毕竟这个东西被封已经说了很久了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-192616-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-192616.jpg)

这的确棒棒哒。

既然如此，还是请赛博佛祖出手吧，自建镜像。

1.fork 代理仓库：https://github.com/obaby/CF-Workers-docker.io/

2.登录 cf，在 worker 和 pages 中添加 pages

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-170732-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-170732.jpg)

选择连接到 git，后续是 gitbub的授权流程，按照提示操作即可。

2.选择 fork 的项目点击开始设置

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-170912-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-170912.jpg)

3.一切设置完成后开始部署

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-171009-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-171009.jpg)

4.部署完成之后就到了下面的页面，可以添加自定义域，主要是 cf 自带的域很可能\*\*\*\*

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-171031.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-171031.jpg)

5.自定义域建议直接托管到 cf，这样只需要添加个域名就 ok 了。完全自动。

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-171214.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-171214.jpg)

6.修改 docker 默认源（针对 ubunt，其他系统路径我也不知道，哈哈哈）如果文件不存在直接创建即可：

```
vim /etc/docker/daemon.json
```

文件内容：

```
{
  "registry-mirrors": ["https://docker.obaby.blog"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

将https://docker.obaby.blog 替换为你的源，如果不想换，那就先用我的吧。

重启 docker 服务：

```
systemctl restart docker
```

7.再次通过 docker pull 镜像就一切都 ok 了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-192704.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240814-192704.jpg)

整体感觉 cf 的代理速度还是蛮不错的，非常 nice，嘻嘻。

ps:

刚发现上面的 docker 启动失败了，直接运行：

```
root@opensips:~# docker run rabbitmq
```

会提示下面的错误：

```
Failed to create thread: Operation not permitted (1)
Aborted
```

直接加参数运行吧：

```
docker run --privileged rabbitmq
```

参考链接：https://www.zhaodede.com/news/content/23.html

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《通过 CF 自建 Docker 镜像》](https://h4ck.org.cn/2024/08/17841)
\* 本文链接：<https://h4ck.org.cn/2024/08/17841>
\* 短链接：<https://oba.by/?p=17841>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[cf](https://h4ck.org.cn/tags/cf)[docker](https://h4ck.org.cn/tags/docker)

[Previous Post](https://h4ck.org.cn/2024/08/17856)
[Next Post](https://h4ck.org.cn/2024/08/17835)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年6月14日

#### [也谈轻量云自动快照备份](https://h4ck.org.cn/2024/06/17331)

2022年5月4日

#### [群辉 NAS 降级记](https://h4ck.org.cn/2022/05/10114)

2021年1月20日

#### [Putty OpenSSH SSH-2 private key (old PEM format)](https://h4ck.org.cn/2021/01/7973)

### 52 comments

1. ![](https://gg.lang.bi/avatar/b13ceb6dfd7e6d264f46cec2d79e2cec01a2703a116048e6951a698e42635485?s=64&d=identicon&r=r) **[演员](https://pfzlcx.cn/)**说道：

   [2024年8月15日 10:03](https://h4ck.org.cn/2024/08/17841#comment-118229)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Google Chrome 122](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 122") Google Chrome 122 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   cf免费真好-.-

   [回复](#comment-118229)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年8月15日 10:26](https://h4ck.org.cn/2024/08/17841#comment-118230)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是的，可以部署各种服务。

      [回复](#comment-118230)
   2. ![](https://gg.lang.bi/avatar/abd826c253cc22fb954ec7567526f9a1211deb9905b8477c5b2875e20a2adb0b?s=64&d=identicon&r=r)

      [2024年8月15日 20:59](https://h4ck.org.cn/2024/08/17841#comment-118275)

      ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

      ![Microsoft Edge 105](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 105") Microsoft Edge 105 ![Android 6.0.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 6.0.1") Android 6.0.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      cf代理速度一般在200kb/s左右，好的话能到5m/s，比较稳定，但偶尔会挂(2.9%)。
      但，不管怎么，cf代理github或其它服务非常棒。

      [回复](#comment-118275)
2. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2024年8月15日 10:26](https://h4ck.org.cn/2024/08/17841#comment-118231)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我用你的了，好用，速度快

   [回复](#comment-118231)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年8月15日 10:39](https://h4ck.org.cn/2024/08/17841#comment-118238)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](h...