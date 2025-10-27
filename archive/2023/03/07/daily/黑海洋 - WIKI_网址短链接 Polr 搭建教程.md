---
title: 网址短链接 Polr 搭建教程
url: https://blog.upx8.com/3255
source: 黑海洋 - WIKI
date: 2023-03-07
fetch_date: 2025-10-04T08:49:18.096043
---

# 网址短链接 Polr 搭建教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 网址短链接 Polr 搭建教程

发布时间:
2023-03-06

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
18505

`Polr`是一个开源的短链接软件，也就是不存在收费的问题，而且功能也是足够强大，不仅能够随机生成、自定义生成短链接，还支持`API`、二维码，同时还拥有一系列管理、统计功能(来源、时间、访问次数等等)，可以说是现在市面上最强大的一个短链开源项目。

这里就讲一下它的搭建过程。

### 截图

![](https://cnboy.org/wp-content/uploads/c4ca4238a0b9238-3.jpg)![](https://cnboy.org/wp-content/uploads/c81e728d9d4c2f6-2.jpg)

### 安装方法

**准备工作:**
1，安装了Web环境的服务器一台，可以用lnmp、lamp一键包或者宝塔之类的面板来搭建web环境。
2，一个足够短的漂亮的域名，并做好解析。

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

**复制

```
cp .env.setup .env
```

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

[取消回复](https://blog.upx8.com/3255#respond-post-3255)

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