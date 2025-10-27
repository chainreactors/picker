---
title: 谷歌云GCP Firebase Hosting：每月 10G 流量 + 10GB 存储（免费）
url: https://blog.upx8.com/4814
source: 黑海洋 - Wiki
date: 2025-06-05
fetch_date: 2025-10-06T22:53:24.244749
---

# 谷歌云GCP Firebase Hosting：每月 10G 流量 + 10GB 存储（免费）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 谷歌云GCP Firebase Hosting：每月 10G 流量 + 10GB 存储（免费）

发布时间:
2025-06-04

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
86207

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYR7Awwq6SUySGx56cjpEcXO2pyPeak2gqwoZlvk8GD7Crbr1OR-EQzIAuxkrJccNBelK2WnGJKCRGvjPg8H6ApndwhX8WLwaZlcc-yxeo7is7pGtliBcWyhoU9-csGUbV1hUGuCuEXf2_e-CgOw8ebp5Om-tVSAU8lo8F2r4l7O32g_-sS_lu33SNEUQ/w640-h640/Firebase%20%E5%85%8D%E8%B4%B9%E6%89%98%E7%AE%A1%E6%9C%8D%E5%8A%A1%E4%BB%8B%E7%BB%8D.png)
什么是 Firebase 托管？
Firebase Hosting 是 Google 提供的一项服务，用于托管网页、Progressive Web Apps（PWA）以及移动后端内容。它适合部署静态资源文件，如 HTML、CSS、JS、图片等。

Firebase Hosting 的免费额度非常友好，适合开发者、小项目或个人网站白嫖使用。

**项目不绑定结算 无反褥风险**

常见用途

个人博客（搭配 Hugo、Hexo、Astro 等静态博客引擎）

项目展示页 / 简历站点

单页应用（如 React、Vue）

前端 Demo 展示站

免费额度说明 [https://firebase.google.com/pricing?hl=zh-cn](https://blog.upx8.com/go/aHR0cHM6Ly9maXJlYmFzZS5nb29nbGUuY29tL3ByaWNpbmc_aGw9emgtY24)

Firebase 的 Spark 计划（免费层）包含：
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiAwATt3hr99FHhNSIYV2hVqtDLJCb_qNa52cQl8H6RlwzGLZXQkByM-d3lq6RnmfP7_rn9S7qIG6cUS46w4co5U1H2F-t8LSM2Tcd8JCvEya722FJdwuBjqsZw2k3KXkouKPJ38KM1X-wg6ziU7u871a5gUxrw3C_ed8cBE0twXMsKburt21wlijOEgc/w640-h260/1747100588208.jpg)

**1.创建项目
首先登录 [https://console.firebase.google.com](https://blog.upx8.com/go/aHR0cHM6Ly9jb25zb2xlLmZpcmViYXNlLmdvb2dsZS5jb20) 创建一个新项目。注意，创建过程中页面会默认生成一个 Project ID，我们也可以自己填写，它将决定我们的网站托管在 firebase 上的子域名，比如你填入 google，则最后你的博客将托管在 google.web.app域名 - 只不过一旦创建后就不能再修改。**

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0JGzM-LyM83Q5oT-oO_Q_XQWkR-Q5LQ3Q5QsOTPx-s0_Tk0l5cJsjV7-o5jSq3M2Dm1_e4IiL-gTPikC5zYRsbR4I8CiJ4ocpZ1K7nxAHiap_GWtOHC_O9EBEvjOPH-4UW1tlt92E9zO7AUdqaeuPoHsN65prW_vTkLMG9eVM3UACI45EcHNtBGTpjlQ/w640-h410/1747101819111.jpg)

**2.需要一台Linux服务器（推荐debian）安装 Firebase 命令行工具，以次运行下面的命令，进行安装**

```
curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
apt install -y nodejs
npm install -g firebase-tools
```

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtYwT43cHPTCvuNs6OHMk0WHqGpKvwFumrcW9sE8SlUXZwNoRtBnwvN8NbQ-xLkBLZmfNDqyG8H6EVsnpjYpQqfrZsH1ThWXGHzlO_emVb_3qpUpwVkiQ8sZhEKrIGvrS4cWvXxE2G5fSMlXkqn9oiuNY1rj2dGlR7Cdo6oT19DPHVeQACkFr4oDGqdgk/w640-h552/1747108676617.jpg)
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpWuHBssxzBoTXHd5KyB3t_qr-KvCzkgcm9dJpRcINURInRnpRX0fCKaTgB1iyNwTsxnzn9ftTySNyqvIg-yQ80Vfy4oNSIwFUga8CsZrR24lqQz_y3I_xDXLnRpfc0sQdXu3I08DFdUR4duDcCZSpERyZ4QK3FVgxihuc6WLTz1p4I4kcQ2DhMEj7u_4/w640-h506/1747108859398.jpg)
**3.在终端执行下列命令会出现一个授权网址，复制到浏览器授权**

```
firebase login --no-localhost
```

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhycR5nkoe8nxykowAaidQ98stzv93U39G43Bs5hVkOeaVXpEqJS3w3NgErCppU6NbTA24wd5jbW9K9wBg80KUoJdfI4edm-jg1rtmoqzv4Wk3AHo6nPoGD4BsK74kg-Y7VrFhyphenhyphenY9TTjFQfcuA_A65ZNDrQ8hri6rwEx9P0fp54fRQpUria_xTKA7uvu1A/w640-h286/1747124678898.jpg)
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxHfEetx-dKM8Rozvydo3asfRGHcPVwZ6lQVFjsJnxbHWsp7akCv2nMrXBfxV2iIali60fXpXdtaRgs7PYbfie2qfgvheA2jxW6qgFO2aIIjjORP1kRZpnZl6d1rDFzvlNHnZmvVcOPgAsVJa5b7Fn_m-FIG20wgokPbiQYmBg3FnBNrAV8x0Aou9xJ4M/w640-h510/1747124785265.jpg)

**得到授权码后回到服务器黏贴上回车确认，至此已经完成授权。**
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoFjr7MmNLch33WDgmuaFkG6a9VxtYm0U4YMAtOJ5WD7_kZ1Hv80CrvBg8SrIxMWrEdOsRWeGgBde_WffFbpmvjTBZmssZsYlCkRu9T1HGNHCYe3OE07XKwS_ekJEOThge__PKVerylm4k0QZUvE_gpzr9_rwtlwwwrM7mE_JdmViWHC2a9O-sjdzTiBA/w640-h124/1747124865713.jpg)

**4.初始化项目，选择现有的项目，再选择刚刚创建的项目，一直回车，到github步骤选择n，不从github更新（如需要更新可以自己研究）**

```
firebase init hosting
```

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi89FlxFD0IlL7H82K17WayF8BkkgpNDdDVdW9HZTjwbOJ7IDlevqUd-bsBSZwqpy6dJNM_X96669tABZkzICvOf9bJUGoB1O770PZ6aJxZ6hyvlPbXBSDGZFUO0OGgRz2rOtPWdeCbCi904VIVezORTLekrC0dMk4vpNMxFxLr3AfQx095Q0RggsvPu-Q/w630-h640/1747125174814.jpg)

**5.默认root下面会多1个 public文件夹（此目录很关键）帮静态文件放在这个里面，再进行部署网站**
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMn1Pc-H7mVEHlVJaZ3MW48qN8VoIFpv_jQAig_r-Ipwu-lQV2TvBwmZsPTdgamFlai6hnlJMWeqUqP2Uqz1xQNJ16LPu4m1iMFssDvACGGauklT0vhjO-dElkIdHF4tbLlr3ZPZvkpKJOMwoookHTqMuPRdmxHfGis8vekZVj3xwXOoF-OWvFR-DIKec/w640-h138/1747125329277.jpg)

```
firebase deploy
```

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKKDjCO2wiN4WS4oZ4ozlwA6_eXQlxsgqj-6t8AwAE0EhJsJ1Zzjxh7pJyyJOUgnVa-sY1uhEY54dqK3siyt1n1Pa9ijt_l1FZZDTm-1bQs-V6dgrVsrC_GMiXQo6BC5a6UKmgFLeDKng8_TgUPDvmENUy5qteJoLyidBE_OYUHFC8g_HQlwszLY_queU/w640-h326/1747125476435.jpg)

**部署完成后，Firebase 会提供一个像图中这样的链接**
**你也可以在面板绑定你自己的域名**

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSnUZmvgalUceQc6JPv5l9xZrBq_XpD82KMgvdGoUSs_tcPxVOicpqk0emqLnX4D9F4BxlLhfbfujbmqDb70LBrwUcKJlLwds3QQuqaDNHncp5Znwvu21yzQCoDaaxodyHqghjrfnsbR5y8KgHlGaZn6qJx7itZNr1lNtW-9v19syk6Bu24NkUDqZyNSY/w640-h366/1747125659853.jpg)
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLHRaGEeue3iP6nmEGPaROX6UF2D-XNK62sOJSc9TJ1F8_8Gm5GnGMSL2KB571u1V28BxXabaE7EzPoOR84f-kbZ52mCdT4bDNJoupWfdKuIIhhBOuRBPX-4bOOeOaAGa0HzWc1byWHHtgPTYwcZ_lDAEK7vwyzARa7utouZ1v9KeSds2fLJq_02cI6mE/s1641/1747125793486.jpg)

**6.注意事项 Firebase Hosting 不支持动态后端 ，免费层并不是为大流量网站准备**

[取消回复](https://blog.upx8.com/4814#respond-post-4814)

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