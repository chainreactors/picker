---
title: 网址短链接 Polr 搭建教程
url: https://buaq.net/go-152243.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:19.820838
---

# 网址短链接 Polr 搭建教程

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/7fddbc932adc4bfa35c1dd9367dc8d6c.jpg)

网址短链接 Polr 搭建教程

Polr是一个开源的短链接软件，也就是不存在收费的问题，而且功能也是足够强大，不仅能够随机生成、自定义生成短链接，还支持API、二维码，同时还拥有一系列
*2023-3-6 22:33:0
Author: [blog.upx8.com(查看原文)](/jump-152243.htm)
阅读量:56
收藏*

---

`Polr`是一个开源的短链接软件，也就是不存在收费的问题，而且功能也是足够强大，不仅能够随机生成、自定义生成短链接，还支持`API`、二维码，同时还拥有一系列管理、统计功能(来源、时间、访问次数等等)，可以说是现在市面上最强大的一个短链开源项目。

这里就讲一下它的搭建过程。

### 截图

![](https://cnboy.org/wp-content/uploads/c4ca4238a0b9238-3.jpg)

### 安装方法

**准备工作:**

**Github地址：**https://github.com/cydrobolt/polr

**1. 添加网站并下载程序**
添加域名，并进入网站根目录，使用命令：

**复制

```
cd /www/wwwroot/website.com
#下载官方源码
git clone https://github.com/cydrobolt/polr.git
mv polr/{.,}* ./

#下载汉化文件（网上流传的汉化版本，无法支持二维码功能，此处博主依据最新版 Polr 自行汉化了一个，功能正常使用。）
cd resources && rm -rf views && wget https://github.com/honorcnboy/Porl-CHN/releases/download/1.0.0/porl_views_1.0.tar.gz
tar zxvf porl_views_1.0.tar.gz
cd ..
```

**2. 下载并安装composer**

**复制

```
#在/root目录下安装Composer
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

#进入网站根目录运行
cd /www/wwwroot/website.com
composer install --no-dev -o
```

此时如果出现错误，请仔细检查，一般都是因为PHP禁用函数未解除，或是缺少PHP扩展造成的。

3.**编辑文件**
将`.env.setup`创建一个名为`.env`的副本。

**4、网站设置**

在宝塔面板上点击网站-设置-伪静态，设置为：`laravel5`，保存。然后到 网站目录-运行目录 ，选择`/public`，保存。再回到 伪静态 ，填入以下代码。同时，设置好SSL：

**复制

```
location / {
            try_files $uri $uri/ /index.php$is_args$args;
}
```

**5、 重启`Nginx`，将网站下所有文件的权限改成777，所有者www**

![](https://cnboy.org/wp-content/uploads/eccbc87e4b5ce2f-2.jpg)

**6、 进入`http://website.com/setup`完成各项设置**

![](https://cnboy.org/wp-content/uploads/a87ff679a2f3e71-1.jpg)![](https://cnboy.org/wp-content/uploads/e4da3b7fbbce234-1.jpg)

**现在就可以正常使用了！！！**如果出现错误，删除网站重新搭建即可。

## 其他配置

**1、一些细节点说明**

1. 如果是使用`Cloudflare`，不要开启CDN（小云朵），会造成重定向次数太多，无法正常访问。如果非要开启CDN，见下面第3条进行设置。

2. 不要关闭 防跨站攻击 ，否则网站无法正常访问。

**2、修改设置**
是的，你没看错设置仅能通过`.env`这个文件修改。

**3、通过CDN获取真实IP**
若使用`Cloudflare`，请在`vender/autoload.php`的第`6`行加入：

**复制

```
if (isset($_SERVER["HTTP_CF_CONNECTING_IP"])) {
  $_SERVER['REMOTE_ADDR'] = $_SERVER["HTTP_CF_CONNECTING_IP"];
}
```

其他`CDN`请自行查找。

**4、设置时区**
在`.env`文件的最后加入（时区自行根据需要设置即可）：

**复制

```
APP_TIMEZONE=Asia/Shanghai
```

文章来源: https://blog.upx8.com/3255
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)