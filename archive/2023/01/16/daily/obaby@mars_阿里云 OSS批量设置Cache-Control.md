---
title: 阿里云 OSS批量设置Cache-Control
url: https://h4ck.org.cn/2023/01/%e9%98%bf%e9%87%8c%e4%ba%91-oss%e6%89%b9%e9%87%8f%e8%ae%be%e7%bd%aecache-control/
source: obaby@mars
date: 2023-01-16
fetch_date: 2025-10-04T03:58:52.512321
---

# 阿里云 OSS批量设置Cache-Control

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 阿里云 OSS批量设置Cache-Control

2023年1月15日
[9 条评论](https://h4ck.org.cn/2023/01/11023#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/3a3c8c155d2945c24076ec9ff2683583.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/3a3c8c155d2945c24076ec9ff2683583.jpg)

阿里云的服务器带宽一向都是小水管，为了加快加载速度把大量的图片都上传到了oss上。本地文件通过litespeed设置缓存，但是oss上的文件却没有一个统一的入口设置浏览器缓存。如果通过后台设置，需要每个文件都要去处理。而插件也没看到设置浏览器Cache-Control的地方。不过好在阿里云提供了一个命令行工具ossutil64（能简单解决的，就没必要去写代码啦~~） 。

可以通过下面的命令进行浏览器头设置（https://help.aliyun.com/document\_detail/120056.html?spm=a2c4g.11186623.0.0.43e877864L0FLp）：

```
./ossutil64 set-meta oss://examplebucket/src Cache-Control:no-cache#X-Oss-Object-Acl:private -r
```

在使用之前需要配置oss的各种信息，通过以下命令配置：

```
./ossutil64 config
```

如果对于目录操作，可以添加以-u参数，否则在遇到错误之后就直接退出了，如下：

```
sh h4ck_set_oss_cache_control.sh
Total 30430 objects. Setted meta on 3537 objects, when error happens.
Error: oss: service returned error: StatusCode=403, ErrorCode=AccessDenied, ErrorMessage="You do not have read permission on this object.", RequestId=63C37D2B73254F37344E4010, Bucket=h4ck-img, Object=wp-content/uploads/2012/08/KuaiBo.png
```

提示KuaiBo.png这个文件权限有问题，但是实际去找事找不到这个文件的，因为涉黄被阿里云给删除了~~~ ![laugh](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh.gif)

通过-u参数就可以让错误发生的时候继续执行了，如下：

```
root@blog:~/sh# sh h4ck_set_oss_cache_control.sh
Error occurs, message: oss: service returned error: StatusCode=403, ErrorCode=, ErrorMessage="", RequestId=63C37EB124DBA9393709C74E, Bucket=h4ck-img, Object=wp-content/uploads/2012/08/KuaiBo.png. See more information in file: ossutil_output/ossutil_report_20230115_121834.report
FinishWithError: Total 30430 objects. Setted meta on 30422 objects, Error 8 objects.

847.976347(s) elapsed
```

每次上传之后都需要设置新文件的浏览器头，如果全部跑一边也太费事了（847秒）。于是准备写个定时任务来每天处理新上传的文件，只处理当前月份的目录即可：

```
cur_month=`date +%m`
echo "Set h4ck image oss cache:"
echo $cur_month
echo oss://h4ck-img/wp-content/uploads/2023/$cur_month
/bin/ossutil64 set-meta oss://h4ck-img/wp-content/uploads/2023/$cur_month Cache-Control:max-age=1557600 -r -u -f
```

现在执行速度就快多了（6秒）：

```
root@blog:~/sh# sh update_2023_upload_oss_cache_control.sh
Set h4ck image oss cache:
01
oss://h4ck-img/wp-content/uploads/2023/01
Succeed: Total 1088 objects. Setted meta on 1088 objects.

6.419401(s) elapsed
```

通过crontab -e命令添加定时任务，每天2点执行：

```
0 2 * * * /root/sh/update_2023_upload_oss_cache_control.sh
```

缓存效果检验：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230115131454.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230115131454.jpg)

可以看到是从磁盘加载的，并且cache-control也生效了。nice~~~

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《阿里云 OSS批量设置Cache-Control》](https://h4ck.org.cn/2023/01/11023)
\* 本文链接：<https://h4ck.org.cn/2023/01/11023>
\* 短链接：<https://oba.by/?p=11023>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Linux](https://h4ck.org.cn/tags/linux)[oss](https://h4ck.org.cn/tags/oss)

[Previous Post](https://h4ck.org.cn/2023/01/11094)
[Next Post](https://h4ck.org.cn/2023/01/11006)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2014年12月8日

#### [蛋疼的gravatar（感谢GFW）](https://h4ck.org.cn/2014/12/5734)

2022年9月15日

#### [WordPress 评论显示IP归属地插件–WP-UserAgent[增强版]](https://h4ck.org.cn/2022/09/10469)

2023年2月22日

#### [百度CDN加速阿里云OSS](https://h4ck.org.cn/2023/02/11269)

### 9 comments

1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r) **[小熊](https://www.saphead.cn/)**说道：

   [2023年1月15日 14:43](https://h4ck.org.cn/2023/01/11023#comment-91145)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 108") Microsoft Edge 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我怕房子没啦，大佬

   [回复](#comment-91145)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年1月15日 16:28](https://h4ck.org.cn/2023/01/11023#comment-91146)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 108") Google Chrome 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      确实有这个风险~~~

      [回复](#comment-91146)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2023年1月16日 00:29](https://h4ck.org.cn/2023/01/11023#comment-91161)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 108") Microsoft Edge 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   记得ECS有个内网地址可以直通OSS，不算流量而且没有带宽限制！

   [回复](#comment-91161)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年1月16日 08:37](https://h4ck.org.cn/2023/01/11023#comment-91173)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      使用oss内网的endpoint地址就可以了，内网速度还是很快的。网站备份也可以直接备到oss上。不过公网流量还是要收费的，之所以做缓存是不想每次加载都去oss在请求一遍了。 ![heart](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/heart.gif)

      [回复](#comment-91173)

      1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

         [2023年1月17日 09:28](https://h4ck.org.cn/2023/01/11023#comment-91197)

         ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

         ![Microsoft Edge 109](https://h4ck.org.cn/wp-content/plugins/wp-use...