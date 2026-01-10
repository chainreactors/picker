---
title: 【渗透实战系列】|55-某大型集团渗透测试（全域权限）
url: https://mp.weixin.qq.com/s/F8vALfbG5K_gp4Sr7vZPvQ
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:30:35.059418
---

# 【渗透实战系列】|55-某大型集团渗透测试（全域权限）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rf8EhNshONRJnlknd0eZu4iblI03icHNboppq355GIsCibfpONIjLLGtazibcLiaqlYkfDCB8ibMGbMIrtZj3hyMVxDQ/0?wx_fmt=jpeg)

# 【渗透实战系列】|55-某大型集团渗透测试（全域权限）

hey

Hacking黑白红

![]()

在小说阅读器中沉浸阅读

```
作者：hey原文：https://forum.butian.net/share/4502
```

该文章叙述了某集团因为存在域信任后导致从内网攻破子域后再次接管父域的渗透过程；在文章最后也存在笔者立足于更高维度审视域控的想法，这也是笔者对于接管域控之后如何以业务拟态与角色继承为核心，将自身融入目标组织的日常运作逻辑，模拟用户在工作流程中对各类服务的真实访问路径，形成如同“水坑”式的精准攻击手法的思考。

目录

```
某大型集团渗透测试评估综述   目标渗透路径详细说明信息收集某大型集团制造平台存在Shiro反序列化Shiro反序列化获取服务器权限  平台数据库权限自动化快速收集内网配置文件信息内网突破  内网渗透  横向移动  域内信息收集  子域横移域内的横向  横向到根域BloodHound分析xxxx.LOCALDCSync驻留后门立足于更高维度审视域控
```

# 某大型集团渗透测试评估

## 综述

![QQ截图20250802171509.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNbo0Latsg39oGeAqY85SjbicA2zvAcytf1cyib7Viam5ABS7Bn3JR2f6NCUQ/640?wx_fmt=png&from=appmsg)

## 目标渗透路径详细说明

![未命名绘图.drawio.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNboSia5HbMicBFia9liamhcjww5gnFerkgUCc3qicU6kvuIWtiafVKKRTIZqwSA/640?wx_fmt=png&from=appmsg)

### 信息收集

#### 某大型集团制造平台存在Shiro反序列化

首先在我们拿到一份靶标名单之后我们肯定是先挑软柿子来捏的，目标资产一般来说可将其攻击优先级分为三个梯度：

* 第一梯度：私企、医疗、科技园区、工厂等，这些单位具体业务体量大、互联网暴露面多，属于优先攻击目标。
* 第二梯度：政府单位（如人社厅/局、教育厅/局）、学校、 国企等，这部分单位防护等级高于第一梯度，但其安全意识可能较为薄弱，监控力度往往白天大于晚上，属于一般攻击目标。
* 第三梯度电力、金融等，这些单位安全性高、暴露面少，安全规范和操作规范都高于前两梯度，在护网收尾工作时看看即可。
  此时了解完靶标资产后我们就可以开始做信息收集了。
  ![图片1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNboVWBaeejOtAZbDDzicFhFVNvB2scn6QK0RQfhZVxKb29icUIeHK587BHg/640?wx_fmt=png&from=appmsg)
  想要构建一个上帝视野，前期的信息收集工作是必不可少的，无论是了解一个人、一项业务、还是深入一个系统等，都需要信息。渗透测试的本质是信息收集，而个人直观感受就是意料之外，情理之中。对一个大型目标的攻防，资产测绘部分是最为重要的，此时我一般会通过三个维度对其进行收集：
* 通过爱企查查询控股子公司。通过招标文件以及官网信息查询第三方供应商。通过ICP备案，查询该企业注册的一系列域名以及小程序，app资产。
* 接下来就是一系列的自动化收集工具，我一般会将前一步骤中收集的主要域名资产导入，并进入深化的测绘。总而言之，这个阶段的需求就是对子域名扫描、DNS 查询、端口扫描、指纹识别、漏洞测试。大范围的覆盖性扫描有助于快速定位某些文件泄露，敏感服务。
* 接下来大部分就是根据目标类型区分，比如本次的靶标为制造业，那么肯定会有出售平台、制造平台；那么会不会有别的系统作为同类型业务；可以根据靶标的主要业务对其进行进一步的旁站信息收集

此时在给出的靶标中发现主域名：`xxx.xxx.xxx.xxx`；我们针对主域名进行信息收集；通过网络空间安全测绘平台（鹰图平台、360quake、fofa）进行信息收集；此时发现其子域名下搭建了一个制造平台。

![QQ截图20250719143733.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNboJexUibTNvOxcwTHGAuofOqOUIiaJXX8uWPD1dUajAS8jrFzUpZcrvGBQ/640?wx_fmt=png&from=appmsg)
在最初开始做资产暴露面收集时，我一般会去找`title`关键字和`body`关键字；并且将时间拉长至`3`年。

```
title关键字
domain="xxx.com" && (web.title="管理" || web.title="后台" || web.title="登录" || web.title="邮件" || web.title="教务" || web.title="注册" || web.title="访客")
```

```
body关键字
domain="xxx.com" && (web.body="管理" || web.body="后台" || web.body="登录" || web.body="用户名" || web.body="密码" || web.body="验证码" || web.body="系统" || web.body="账号" || web.body="忘记密码")
```

我一般是先在

* hunter：收录快、内容新，特别是有备案的内容，Hunter基本全部能收录，直接使用搜索语法搜索备案归属单位。
* fofa：fofa已经没那么好使了，但是好在数据量还是多。
* 360quake：鹰图的特点在于对已备案资产的收集顶尖。但一些未备案资产、边缘资产，你会发现鹰图不太完全，这时候咱们可以使用quake。因为一些边缘资产、云主机等，可能不会备案，这你要是漏掉了，漏掉的可能就是一些OA系统。
  中跑一遍子域名中的关键资产。
  此外我还推荐两个资产收集平台：
* Zero零零信安：在一些移动资产、小程序搜索方面表现突出；且很容易上手
* 微步情报社区：微步除了威胁情报信息搜索，在资产收集方面也是顶级顶级顶级，主要在端口、whois信息、子域名方面，顶级。

### Shiro反序列化获取服务器权限

既然出现了平台、后台、系统这种关键信息；那我们优先对其进行指纹扫描，发现是`Shiro`框架，那么此时我们就准备尝试爆破密钥，因为本次演习等级较高；知晓对方肯定有蓝队师傅在值守，那么就没打算直接上一键利用工具，掏出二开小工具进行使用

![QQ截图20250801161253.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNboibqK6dEgz5TKMrrEhO7qVhLra1GTEhH1gA2gMW1ModOuWNV5PIs9klA/640?wx_fmt=png&from=appmsg)
![QQ截图20250719144556.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNbotOaAS2cCo5G2JQSnZibsciay3RXaQBaAjia2uvkicbYln1yRj76iaHTulEQ/640?wx_fmt=png&from=appmsg)

注：这里也想针对这个`Shiro`框架的渗透进行一个介绍，有的师傅很奇怪有时候明明可以抓到密钥，有的时候又不可以；这里想说的是大型集团一般会存在`Waf`，如果你没有针对绕过`waf`的爆破脚本那么即使存在密钥；我们常用的工具也是无法获取链子的。这里推荐大家可以对：https://github.com/SummerSec/ShiroAttack2 进行二开，添加绕过`Waf`的功能，这对于当下`Waf`遍地的攻防有着显著的意义。后续我也会写一篇关于`Shiro`反序列化绕过`Waf`的文章进行分享。
![QQ截图20250730195314.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNbox1Jz842lNSsVHibjJeBwS2saauG62oLHVOETcYcwGDSSicF6MCmqDWPw/640?wx_fmt=png&from=appmsg)

#### 平台数据库权限

拿到机器权限后首先要先注意到本机的敏感配置文件，里面有着大量的配置文件，这也是我们获取数据库权限的关键信息

```
dir /s/b *.conf
```

##### 自动化快速收集内网配置文件信息

此时可以编写一个`Go`程序对已经拿下的机器做一个敏感信息的收集，此时我先列出一些配置敏感信息；`Go`编译出来的体积相对较小且灵活。

```
Key:
  - jdbc
  - redis
  - mysql
  - pgsql
  - postgresql
  - oracle
  - oss.
  - oss.accessKey
  - oss.secretKey
  - secretKey
  - accessKey
  - ak
  - sk
  - mongondb
  - password
  - username
  - mail
  - token
  - datasource
  - accessKeyId
  - accessKeySecret
  - mssql
  - sqlserver
  - aliyun
  - oss
  - kingbase8
  - kingbase
  - SQLite
  - Neo4j
  - access_key
  - access_token
  - admin_pass
  - admin_user
  - algolia_admin_key
  - algolia_api_key
  - alias_pass
  - alicloud_access_key
  - amazon_secret_access_key
  - amazonaws
  - ansible_vault_password
  - aos_key
  - api_key
  - api_key_secret
  - api_key_sid
  - api_secret
  - api.googlemaps AIza
  - apidocs
  - apikey
  - apiSecret
  - app_debug
  - app_id
  - app_key
  - app_log_level
  - app_secret
  - appkey
  - appkeysecret
  - application_key
  - appsecret
  - appspot
  - auth_token
  - authorizationToken
  - authsecret
  - aws_access
  - aws_access_key_id
  - aws_bucket
  - aws_key
  - aws_secret
  - aws_secret_key
  - aws_token
  - AWSSecretKey
  - b2_app_key
  - bashrc password
  - bintray_apikey
  - bintray_gpg_password
  - bintray_key
  - bintraykey
  - bluemix_api_key
  - bluemix_pass
  - browserstack_access_key
  - bucket_password
  - bucketeer_aws_access_key_id
  - bucketeer_aws_secret_access_key
  - built_branch_deploy_key
  - bx_password
  - cache_driver
  - cache_s3_secret_key
  - cattle_access_key
  - cattle_secret_key
  - certificate_password
  - ci_deploy_password
  - client_secret
  - client_zpk_secret_key
  - clojars_password
  - cloud_api_key
  - cloud_watch_aws_access_key
  - cloudant_password
  - cloudflare_api_key
  - cloudflare_auth_key
  - cloudinary_api_secret
  - cloudinary_name
  - codecov_token
  - config
  - conn.login
  - connectionstring
  - consumer_key
  - consumer_secret
  - credentials
  - cypress_record_key
  - database_password
  - database_schema_test
  - datadog_api_key
  - datadog_app_key
  - db_password
  - db_server
  - db_username
  - dbpasswd
  - dbpassword
  - dbuser
  - deploy_password
  - digitalocean_ssh_key_body
  - digitalocean_ssh_key_ids
  - docker_hub_password
  - docker_key
  - docker_pass
  - docker_passwd
  - docker_password
  - dockerhub_password
  - dockerhubpassword
  - dot-files
  - dotfiles
  - droplet_travis_password
  - dynamoaccesskeyid
  - dynamosecretaccesskey
  - elastica_host
  - elastica_port
  - elasticsearch_password
  - encryption_key
  - encryption_password
  - env.heroku_api_key
  - env.sonatype_password
  - eureka.awssecretkey
```

此时收集到的密码对于我们后续做横向移动有着至关重要的作用，根据经验来判断，某些个大型企业内网中机器的密码均存在前几位的重复，举个例子有个集团叫做：万海集团；那么在其内部各个机器的密码很有可能就是集团名字+年份`wanhai2025@!+`或者`whqwe@++!`这种形式；所以大家拿完敏感信息后可以整合成密码本；为后续的横向移动做好准备。

### 内网突破

那先把目光放在这台被拿下的机器上面；在这里建议各位师傅在打下一台机器后不要急着上线`C2`，本机的信息收集还是要老老实实的做一遍，对机子有大致的了解；然后可以翻一下机器上的配置文件，大家有没有发现，这两年的攻防演习中数据分的地位越来越高；往往你可能在内网打得累死累活的也还没拿下域控时，别的队伍直接在外网夸夸刷数据泄露分。所以呢翻翻配置文件看看能不能多拿点数据分呀这样子。
做了一下基础的信息收集；此时发现存在杀毒软件`ESET Security`企业版

![QQ截图20250712202622.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNbot96Nia2fOwMd0ibQiagXictmaW3r0wuxxfOu8KEsictQdH4LE8IwUwHqGwg/640?wx_fmt=png&from=appmsg)

此时无论你上传`Cobalt Strike`还是`Vshell`亦或是`Adaptixde`、`Havoc`的**beacon** 都会被杀掉，还是老老实实的做一遍免杀；在我个人打点时我会优先选择将肉机上线到`Vshell`进行管控，`Vshell`可以直接搭建内网隧道；这对于我们前期做内网信息收集很方便，此时我会选择把`Vshell`当做一个管理端来做内网穿透；然后在进行内网渗透时再把权限转到`Cobalt Strike`,`Cobalt Strike`拥有众多优秀的插件可以让你在内网渗透时事半功倍的进行横向移动。免杀的话可以现在网上搜，实在没有的话在自己动手

![QQ截图20250719145421.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNboq4KRAufCRX8Pw46sTwkHmr0Ju2y87EicgkrJ30Nn5iaFdx856G2cXF8Q/640?wx_fmt=png&from=appmsg)

嘻嘻嘻，好用爱用。上线后搭建隧道在上个免杀的`fscan`开扫；我一般会先爆破一下`rdp`和数据库；再找一台内网机子来做横向移动，不然动静太大入口点机器掉了就糟糕了

![QQ截图20250802172051.png](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONRJnlknd0eZu4iblI03icHNbo2QTnH4vfGtib4KC8ZYDrjXMSTSRuOBxM5jkLDBbI3BOHy8jUM2jcbhg/640?wx_fmt=png&from=appmsg)

### 内网渗透

到了内网那就好办了，因为存在`ESET Security`杀软和深信服态势感知；这个时候可不能...