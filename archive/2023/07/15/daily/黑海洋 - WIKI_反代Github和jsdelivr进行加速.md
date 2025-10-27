---
title: 反代Github和jsdelivr进行加速
url: https://blog.upx8.com/3689
source: 黑海洋 - WIKI
date: 2023-07-15
fetch_date: 2025-10-04T11:53:58.220397
---

# 反代Github和jsdelivr进行加速

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 反代Github和jsdelivr进行加速

发布时间:
2023-07-14

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
14199

![2023-07-13T12:39:11.png](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2023/07/13/1689251953.png "2023-07-13T12:39:11.png")

## 使用方法

在PHP安装“fileinfo”扩展，然后在网站目录新建一个名为gh.php的文件，将下面的代码复制粘贴进去。然后访问：你的域名/gh.php?url=你要代理的URL地址

使用方法示例：https://blog.upx8.com/pic.php?url=https://cdn.jsdelivr.net/gh/notetoday/img/usr/uploads/2023/04/15/1681560702.png

## 代码

```
<?php
if (isset($_GET['url']) == false) {
 die("请将参数填写完整，在当前路径后加上?url=反代的链接");
}

$token = (string) rand(100, 99999);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $_GET['url']);
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
if (isset($_SERVER['HTTP_REFERER']) == true) {
 curl_setopt($ch, CURLOPT_REFERER, $_SERVER['HTTP_REFERER']);
}
$data_down = curl_exec($ch);
if ($data_down === FALSE) {
 die("代理时发生错误");
}
curl_close($ch);
file_put_contents($token, $data_down);

// 使用finfo扩展获取文件的MIME类型
$finfo = new finfo(FILEINFO_MIME);
$mime_type = $finfo->file($token);

header('Content-Type: ' . $mime_type);
unlink($token);
echo $data_down;
?>
```

**相关方案：[Cloudflare Worker Proxy 反向代理（jsdelivr、github加速）](https://blog.upx8.com/3662)**

使用方法示例：https://gh.7761.cf/https://raw.githubusercontent.com/hadis898/Linux-tools/main/vps.sh

[取消回复](https://blog.upx8.com/3689#respond-post-3689)

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