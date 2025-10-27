---
title: Prism：也许是目前理想的WordPress代码高亮方案
url: https://www.uedbox.com/post/103216/
source: 体验盒子
date: 2024-12-24
fetch_date: 2025-10-06T19:40:14.422689
---

# Prism：也许是目前理想的WordPress代码高亮方案

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

# Prism：也许是目前理想的WordPress代码高亮方案

* 发表于 2024年12月23日
* [WordPress](https://www.uedbox.com/design/wordpress/)

目录表

Toggle

* [Prism](#Prism)
* [配置Prism](#%E9%85%8D%E7%BD%AEPrism)
* [上传至站点](#%E4%B8%8A%E4%BC%A0%E8%87%B3%E7%AB%99%E7%82%B9)
* [添加 php 函数加载 Prism](#%E6%B7%BB%E5%8A%A0_php_%E5%87%BD%E6%95%B0%E5%8A%A0%E8%BD%BD_Prism)
* [启用代码高亮](#%E5%90%AF%E7%94%A8%E4%BB%A3%E7%A0%81%E9%AB%98%E4%BA%AE)
* [进一步优化](#%E8%BF%9B%E4%B8%80%E6%AD%A5%E4%BC%98%E5%8C%96)

# Prism

Prism js 是一个轻量级的语法高亮 js / css，广泛使用在各大站点中。

官网：<https://prismjs.com/download.html>

# 配置Prism

从官网下载配置页面，自定义主题、需要解析的代码语言和插件，配置完成分别下载js和css文件。

如下是我的定义：

* 主题：OKAIDIA
* 语言：python+java+go+c+bash+git+javascript+css+sql+mysql
* 插件：line higlight+line numbers

![Prism：也许是目前理想的WordPress代码高亮方案](https://www.uedbox.com/wp-content/uploads/2024/12/image.png)

# 上传至站点

上传到当前使用主题的根目录即可

# 添加 php 函数加载 Prism

进入WordPress后台，找到模板函数（functions.php），在末尾追加如下代码：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | function add\_custom\_prism\_files() {  // 引入自定义的Prism CSS文件  wp\_enqueue\_style('custom-prism-css', get\_template\_directory\_uri() . '/prism.css');    // 引入自定义的Prism JavaScript文件  wp\_enqueue\_script('custom-prism-js', get\_template\_directory\_uri() . '/prism.js', array(), false, true);  }  add\_action('wp\_enqueue\_scripts', 'add\_custom\_prism\_files'); |

# 启用代码高亮

如上面所看到的PHP代码效果，只需要在文章编辑页面，新建一个区块选择“自定义HTML”，然后用<pre class=”line-numbers” ><code class=”language-php”>和</code></pre>包裹代码即可：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | <pre class="line-numbers" ><code class="language-php">  function add\_custom\_prism\_files() {  // 引入自定义的Prism CSS文件  wp\_enqueue\_style('custom-prism-css', get\_template\_directory\_uri() . '/prism.css');    // 引入自定义的Prism JavaScript文件  wp\_enqueue\_script('custom-prism-js', get\_template\_directory\_uri() . '/prism.js', array(), false, true);  }  add\_action('wp\_enqueue\_scripts', 'add\_custom\_prism\_files');  </code></pre> |

# 进一步优化

现在基本已经实现想要的效果了，不过每次都要使用html代码来启用代码高亮展示，代码段多了难免有些麻烦，于是，我继续在模板函数（functions.php）中新增了一个函数，用于将默认的代码块转换成prism高亮代码块，大致逻辑如下：

1. 匹配包含
   `<pre class="wp-block-code"><code>`
   标签的代码块（wp默认代码块）替换为
   `<pre class="line-numbers"><code class="language-' . $language . '">`
2. 上面的
   `$language`
   变量匹配代码中第一行中的字符作为prism需要识别的高亮语言，然后删除第一行

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | /\*\*  \* prism.js将默认的代码块转换成prism  \*/  function process\_code\_blocks( $content ) {  $pattern = '/<pre class="wp-block-code"><code>(.\*?)<\/code><\/pre>/s';  $content = preg\_replace\_callback( $pattern, function( $matches ) {  $code = html\_entity\_decode($matches[1]);  if (preg\_match('/(.+?)\n(.\*)/s', $code, $first\_line\_matches)) {  $language = trim($first\_line\_matches[1]);  $code = $first\_line\_matches[2];  } else {  $language = 'plaintext';  }    // 构造新的代码块  $new\_code\_block = '<pre class="line-numbers"><code class="language-' . $language . '">' . htmlspecialchars($code) . '</code></pre>';    // 返回新的代码块  return $new\_code\_block;  }, $content );    return $content;  }  add\_filter( 'the\_content', 'process\_code\_blocks' ); |

现在打开WordPress的编辑器，只需要使用默认的代码块，然后在第一行写明需要高亮的语言即可

点赞(1)

打赏

分享

标签：[Prism](https://www.uedbox.com/post/tag/prism/) , [WordPress](https://www.uedbox.com/post/tag/wordpress/) , [代码高亮](https://www.uedbox.com/post/tag/%E4%BB%A3%E7%A0%81%E9%AB%98%E4%BA%AE/)  原文连接：**[Prism：也许是目前理想的WordPress代码高亮方案](https://www.uedbox.com/post/103216/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/post/69909/ "两个生成式AI 平台推荐，生产力亲测") [解决 the "listen ... http2" directive is deprecated](https://www.uedbox.com/post/119302/ "解决 the ")

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
* [Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

* [2025 BT磁力搜索引擎大...