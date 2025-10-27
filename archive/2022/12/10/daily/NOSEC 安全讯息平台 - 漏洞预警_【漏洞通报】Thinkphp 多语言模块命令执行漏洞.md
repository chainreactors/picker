---
title: 【漏洞通报】Thinkphp 多语言模块命令执行漏洞
url: https://nosec.org/home/detail/5050.html
source: NOSEC 安全讯息平台 - 漏洞预警
date: 2022-12-10
fetch_date: 2025-10-04T01:03:36.125600
---

# 【漏洞通报】Thinkphp 多语言模块命令执行漏洞

[![](https://nosec.org/home/image/logo.png)](/)

[登录/注册](https://nosec.org/home/caslogin)

[投稿](https://nosec.org/home/caslogin)

[首页](/home/index)
[威胁情报](/home/index/threaten.html)
[安全动态](/home/index/security.html)
[漏洞预警](/home/index/hole.html)

数据泄露

* [新闻浏览](/home/index/leakage.html)
* [图表统计](/home/index/graphshtml)

[专题报告](/home/index/speech.html)
[技术分析](/home/index/skill.html)
[安全工具](/home/index/tool.html)

# 【漏洞通报】Thinkphp 多语言模块命令执行漏洞

![](https://nosec.org/home/image/headImg.png)xiannv  1029天前

![Image](/avatar/uploads/attach/image/4727bf6e57961895d73f51eb746f70bf/%E5%9B%BE%E7%89%87.png)

# 一、      漏洞概述

ThinkPHP 是一个快速、简单的面向对象的轻量级 PHP 开发框架，创立于2006年初，遵循Apache2开源协议发布，是为了敏捷WEB应用开发和简化企业应用开发而诞生的。

如果 Thinkphp 程序开启了多语言功能，攻击者可以通过 get、header、cookie 等位置传入参数，实现目录穿越+文件包含，通过 pearcmd 文件包含这个 trick 即可实现 RCE。

# 二、      影响范围

本次漏洞影响范围如下：

| v6.0.1 < Thinkphp < v6.0.13  Thinkphp v5.0.x  Thinkphp v5.1.x |
| --- |

FOFA Query：

| header="think\_lang" |
| --- |

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（header="think\_lang"）共有 73,302 个相关服务对外开放。中国使用数量最多，共有44,788 个；美国第二，共有 12,295；中国香港特别行政区第三，共有5,009 个；新加坡第四，共有 896 个；日本第五，共有 246 个。

全球范围内分布情况如下（仅为分布情况，非漏洞影响情况）：

![1.png](/avatar/uploads/attach/image/1507c1083e9fc0f407c9c0e73cc0fc91/1.png)

中国大陆地区北京使用数量最多，共有 7,254 个；浙江第二，共有 6,738 个；广东第三，共有 5,249 个；山东第四，共有 2,220 个；上海第五，共有 1,771 个。

![2.png](/avatar/uploads/attach/image/56a6301c9c489e31bb2c97b8a7c6b29c/2.png)

# 三、      漏洞环境

目前 Vulfocus 已经集成 ThinkPHP 环境，可通过以下链接启动环境测试：

[thinkphplang 命令执行漏洞](https://vulfocus.cn/#/dashboard?image_id=5d2d721b-b65b-4055-95dc-1ce70a3a0c56)

也可通过命令：

```
docker pull vulfocus/thinkphp:6.0.12
```

进行拉取运行，也可通过 <http://vulfocus.cn/> 进行测试。

![3.png](/avatar/uploads/attach/image/52f092d77e7719379296a122de1e5931/3.png)

# 四、      漏洞复现

白帽汇安全研究院第一时间对漏洞进行了复现：

![lQLPJxxB9_YVSzzNBgDNCPywuD-IFvqxpWADj5ILNcBJAA_2300_1536.png](/avatar/uploads/attach/image/bc5e584303011ddd442a6a8eb8983f45/lQLPJxxB9_YVSzzNBgDNCPywuD-IFvqxpWADj5ILNcBJAA_2300_1536.png)

![](data:image/png;base64...)

# 五、      修复建议

官方已经针对漏洞发布了安全更新，请及时更新，地址如下：

<https://github.com/top-think/framework/commit/c4acb8b4001b98a0078eda25840d33e295a7f099>

# 六、      参考链接

[1.]  <https://github.com/top-think/framework/commit/c4acb8b4001b98a0078eda25840d33e295a7f099>

[2.]  <https://tttang.com/archive/1865/>

[漏洞](https://nosec.org/home/search/keytag/%E6%BC%8F%E6%B4%9E.html)

[上一篇：
Shell中的幽灵王者—JAVAWEB ......](/home/detail/5049.html)
[下一篇：
通过一个NTLM协议，完成攻防......](/home/detail/5052.html)

浏览: 98880
评论: 0

![](https://nosec.org/home/image/weibo.png)

#### 最新评论

![](/home/image/loading.gif)
评论正在提交，请稍等...

昵称

邮箱

已有账号，[登录](/home/caslogin)评论

提交评论

[x]  有人回复邮件通知我

![](https://nosec.org/home/image/code.png)

## 相关推荐

[Elasticsearch27亿数据泄露，10...](/home/detail/3383.html "Elasticsearch27亿数据泄露，10亿明文，波及中国大厂")

[微软前员工窃取1000万美元买湖景...](/home/detail/4162.html "微软前员工窃取1000万美元买湖景房特斯拉：被判18项重罪")

[美国某电力系统因防火墙漏洞被攻...](/home/detail/2962.html "美国某电力系统因防火墙漏洞被攻击致运行中断")

[微软每天可发现77000个活跃的Web...](/home/detail/4083.html "微软每天可发现77000个活跃的WebShell")

[多家网站未履行网络安全保护义务...](/home/detail/3115.html "多家网站未履行网络安全保护义务遭黑客攻击，贵阳网警：罚！")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)