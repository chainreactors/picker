---
title: 禁用WordPress 6.7 中延迟加载图像的自动调整大小
url: https://www.uedbox.com/post/69783/
source: 体验盒子
date: 2024-12-03
fetch_date: 2025-10-06T19:39:20.586354
---

# 禁用WordPress 6.7 中延迟加载图像的自动调整大小

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# 禁用WordPress 6.7 中延迟加载图像的自动调整大小

* 发表于 2024年12月02日
* [WordPress](https://www.uedbox.com/design/wordpress/)

WordPress 6.7 为[延迟加载的图片添加了
`sizes=“auto”。`](https://core.trac.wordpress.org/ticket/61847)此功能最近[添加到 HTML 规范中](https://github.com/whatwg/html/pull/8008)，它允许浏览器在从
`srcset`
 列表中选择源时使用图像的渲染布局宽度，因为延迟加载的图像在知道布局之前不会加载。

目录表

Toggle

* [Background 背景](#Background_%E8%83%8C%E6%99%AF)
* [Implementation details 实现细节](#Implementation_details_%E5%AE%9E%E7%8E%B0%E7%BB%86%E8%8A%82)
* [Functions added 添加的功能](#Functions_added_%E6%B7%BB%E5%8A%A0%E7%9A%84%E5%8A%9F%E8%83%BD)
* [禁用图片大小自动添加](#%E7%A6%81%E7%94%A8%E5%9B%BE%E7%89%87%E5%A4%A7%E5%B0%8F%E8%87%AA%E5%8A%A8%E6%B7%BB%E5%8A%A0)
  + [禁用wp\_img\_tag\_add\_loading\_attr](#%E7%A6%81%E7%94%A8wp_img_tag_add_loading_attr)
  + [补充：移动端图片自适应](#%E8%A1%A5%E5%85%85%EF%BC%9A%E7%A7%BB%E5%8A%A8%E7%AB%AF%E5%9B%BE%E7%89%87%E8%87%AA%E9%80%82%E5%BA%94)

## Background 背景

响应式图像属性、
`srcset`
 和
`sizes`
 已在 [WordPress 4.4](https://make.wordpress.org/core/2015/11/10/responsive-images-in-wordpress-4-4/) 中添加。引用当时的开发说明：

> *为了帮助浏览器从源集列表中选择最佳图像，我们还包含一个等效*
> `于`
>
> `(max-width: {{image-width}}px) 100vw, {{image-width}}px`
> *.虽然此默认值对于大多数网站都是开箱即用的，但主题应根据需要使用*
> `wp_calculate_image_sizes`
> *过滤器自定义 default*
> `sizes`
> *属性。*

在选择要从
`srcset`
获取的正确文件时，设置默认
`sizes`
值很重要，因为它在知道布局之前告诉浏览器图像的预期布局是什么。如果没有任何值，浏览器将使用默认的
`100vw`
值，并假设图像旨在填充视口的整个宽度，从而导致许多字节浪费。WordPress 多年来一直附带的默认值可确保图像布局受其
`width`
属性的约束。这有帮助，但在许多情况下仍然不正确，因为图像的布局可能受内容宽度或它们嵌套的任何块的限制。

尽管鼓励主题使用
`wp_calculate_image_sizes`
过滤器提供更准确的
`sizes`
属性值，但这样做具有挑战性。现在，浏览器能够自动将渲染的布局应用于延迟加载图像
`的大小`
，
`sizes`
值将 100% 正确，从而减少浪费的字节。

## Implementation details 实现细节

[HTML 规范](https://html.spec.whatwg.org/multipage/images.html#sizes-attributes)允许延迟加载的图像省略
`大小`
、显式设置
`sizes=“auto”`
或将
`大小`
设置为以
`“auto`
”开头的字符串，后跟有效的源大小列表。为了将其作为[已经支持](https://caniuse.com/mdn-html_elements_img_sizes_auto)此功能的浏览器的渐进增强功能，WordPress 将在
`wp_filter_content_tags（）`
期间将
`auto`
添加到内容图像的
`sizes`
属性以及
`wp_get_attachment_image（）`
生成的任何图像标记之前。这将导致不支持新
`auto`
值的浏览器回退到以前的
`大小`
列表。

如果图片包含
`loading=“lazy”`
，WordPress 只会将
`auto`
添加到
`sizes`
值中。否则，支持
`sizes=auto`
的浏览器将无法验证
`sizes`
值并应用默认值
`100vw`
，这将导致从
`srcset`
属性中选择大于需要的图像。在 WordPress 生成标记后更改图像加载值的任何自定义实现都应使用新的
`wp_img_tag_add_auto_sizes（）`
函数来更正
`sizes`
属性。

## Functions added 添加的功能

* **`wp_img_tag_add_auto_sizes`** – 向 HTML
  `img`
  字符串添加自动大小。
* **`wp_sizes_attribute_includes_valid_auto`**– 测试图像上是否已存在 auto，以确保它不会被多次添加。

## 禁用图片大小自动添加

在更新WordPress 6.7后发现，站内多数图片都显示不正常，主要是宽高混乱了，禁用它。

### 禁用wp\_img\_tag\_add\_loading\_attr

在function.php中添加

|  |  |
| --- | --- |
| 1  2  3  4 | // 去除图片自动添加sizes，导致图片变形  add\_filter('wp\_img\_tag\_add\_loading\_attr', function($value, $tag, $context) {  return false;  }, 10, 3); |

### 补充：移动端图片自适应

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17 | // 自适应图片大小原创来自  function uedbox\_remove\_width\_height\_attribute($content)  {  preg\_match\_all("/<[img|IMG].\*?src=[\'|\"](.\*?(?:[\.gif|\.jpg|\.png\.bmp]))[\'|\"].\*?[\/]?>/", $content, $images);  if (!empty($images)) {  foreach ($images[0] as $index => $value) {  $new\_img = preg\_replace('/(width|height|sizes)="\d\*"\s/', "", $images[0][$index]);  $content = str\_replace($images[0][$index], $new\_img, $content);  }  }  return $content;  }  // 判断是否是移动设备浏览  if (wp\_is\_mobile()) {  // 删除文章内容中img的width/height/sizes属性  add\_filter('the\_content', 'uedbox\_remove\_width\_height\_attribute', 99);  } |

点赞(2)

打赏

分享

标签：[WordPress](https://www.uedbox.com/post/tag/wordpress/)  原文连接：**[禁用WordPress 6.7 中延迟加载图像的自动调整大小](https://www.uedbox.com/post/69783/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[王慧文清华产品课](https://www.uedbox.com/post/69774/ "王慧文清华产品课") [如何知道移动应用程序是否是使用 Flutter 制作的？](https://www.uedbox.com/post/69899/ "如何知道移动应用程序是否是使用 Flutter 制作的？")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![体验盒子 Sunrise 主题](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

体验盒子 Sunrise 主题](https://www.uedbox.com/post/5694/ "体验盒子 Sunrise 主题")

[![WordPress宠物！](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress宠物！](https://www.uedbox.com/post/4600/ "WordPress宠物！")

[![WordPress 3.0.1官方中文版发布啦](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress 3.0.1官方中文版发布啦](https://www.uedbox.com/post/1397/ "WordPress 3.0.1官方中文版发布啦")

[![WordPress 3.0.1 wp-admin/plugins.php模块跨站脚本漏洞](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress 3.0.1 wp-admin/plugins.php模块跨站脚本漏洞](https://www.uedbox.com/post/1565/ "WordPress 3.0.1 wp-admin/plugins.php模块跨站脚本漏洞")

[![wordpress添加Ctrl+Eenter快捷回复方法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

wordpress添加Ctrl+Eenter快捷回复方法](https://www.uedbox.com/post/1771/ "wordpress添加Ctrl+Eenter快捷回复方法")

[![WordPress中Pre标签自动换行兼容IE/Opera/Firefox/Chrome](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress中Pre标签自动换行兼容IE/Opera/Firefox/Chrome](https://www.uedbox.com/post/154/ "WordPress中Pre标签自动换行兼容IE/Opera/Firefox/Chrome")

[![WordPress自动添加关键词优化的代码](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

WordPress自动添加关键词优化的代码](https://www.uedbox.com/post/2448/ "WordPress自动添加关键词优化的代码")

[![wordpress猜解密码脚本](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

wordpress猜解密码脚本](https://www.uedbox.com/post/4524/ "wordpress猜解密码脚本")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/post/119352/ "🔥 最新免费域名资源大全 | 永久免费域名获取")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

* [最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")
* [NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")
* [Nginx 利用 fail2ban 自动封禁乱扫的 ...