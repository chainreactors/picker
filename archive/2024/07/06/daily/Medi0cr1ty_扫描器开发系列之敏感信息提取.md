---
title: 扫描器开发系列之敏感信息提取
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484418&idx=1&sn=6c817b22ceb098263582d84d8f9b2298&chksm=c067c32af7104a3cc06e64a7d45f77d377b850a5df7757696ad64b8f398df0ade7a6417a9591&scene=58&subscene=0#rd
source: Medi0cr1ty
date: 2024-07-06
fetch_date: 2025-10-06T17:44:26.406887
---

# 扫描器开发系列之敏感信息提取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSd9Ox3GtKkpSdRf0ovV2XPibaWe3Lubz9rL1kadEE2pia2nR0G1OlysheA/0?wx_fmt=jpeg)

# 扫描器开发系列之敏感信息提取

原创

duckbubi

Medi0cr1ty

### 0x01 写在前面

整体思路：在扫描器的上层代理(使用proxify)做流量镜像储存到es,通过kb做可视化,方便做扫描器整体的流量回溯,敏感信息识别等(使用trufflehog)

1. 1. 这是剥离出来,通用的方案。如果自己的扫描器需要缝合proxify和trufflehog的话,还有非常多的bug fix的活得干,当然也可以选择将结果输出至自己的系统即可。
2. 2. 该方案一行代码也不需要写(bash不算.)

### 0x02 方案介绍

**ES部署**

密码根据自己的需求设置，版本需要选择7.x是因为proxify用的依赖也是7.x的版本，如果需要用更高版本的需要自己修改并重新编译下proxify

```
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=true" \
  -e "ELASTIC_PASSWORD=jjfujj" \
  docker.elastic.co/elasticsearch/elasticsearch:7.17.10
```

**proxify配置‍‍‍‍‍‍‍‍‍‍**

选择0.0.13版本,新版本bug挺多,选新版本需要自己fix下。

```
https://github.com/projectdiscovery/proxify/releases/tag/v0.0.13
```

配置proxify流量储存到es

```
❯ cat ~/.config/proxify/export-config.yaml
kafka:
  addr:""
  topic:""
elastic:
  addr:"127.0.0.1:9200"
  ssl:false
  ssl-verification:false
  username:"elastic"
  password:"jjfujj"
  index-name: "jj"
```

启动

```
./proxify -store-resposne=/tmp/proxify_logs/
```

**trufflehog配置**

下载最新版即可,他是支持直接扫描es的,支持的es是8.x,和上面冲突,且es扫描也有bug需要修,这也是上面为什么让proxify吐出来一份响应的原因。

```
https://github.com/trufflesecurity/truffleHog
```

敏感信息扫描以及通知

```
./trufflehog filesystem /tmp/proxify_logs/ --no-verification --json | jq -r -c '{rule_name:.DetectorName,data:.Raw,filepath:.SourceMetadata.Data.Filesystem.file}' | while read result; do curl -H "Content-Type: application/json" -d $'{"msgtype":"markdown", "markdown":{"content":"bingo:'"${result//\"/\\\"}"'"}}' 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXXXXX'; done
```

定时通知扫描并清理proxify日志

```
*/2 * * * * /path/to/trufflehog.sh
*/2 * * * * find /tmp/proxify_logs/ -type f -mmin +5 -exec rm -f {} \;
```

**可视化**

```
docker run -d -p 5601:5601 -e "ELASTICSEARCH_USERNAME=elastic" \
  -e "ELASTICSEARCH_PASSWORD=jjfujj" \
  --link elasticsearch:elasticsearch \
  docker.elastic.co/kibana/kibana:7.17.10
```

### 0x03 功能验证

trufflehog提供了非常多敏感信息验证代码

```
cd trufflehog/pkg/sources/

python3 -m http.server 8889

#测试浏览走proxify代理进行验证‍‍‍‍‍

curl -x 'http://127.0.0.1:8888' 'http://127.0.0.1:8889/git_test.go'
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSdpsn6HF0libQEjxibxtNdQJFImRReOKribHYlxJOOKMnmG23gicSTq9xt3A/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSdzZ85mZsVOBFTv3QYbsjxVIjmbXUpicibun3u06xd1luLHtwW8Ee4L7xQ/640?wx_fmt=jpeg&from=appmsg)

后续所有接口重放/漏洞扫描的流量走proxify的代理即可

### 0x04 写在后面

* • 需要大量正则匹配(性能消耗)的工作放到端上做对日站的体验影响非常大,非常难受。
* • 修别人的bug真难受,需求不复杂的话不如自己造轮子。
* • 实际上开发/运维领域有很多现成的系统也可以完成该需求，不过对于这样一个小的需求来说，过于臃肿了，规则维护也比较麻烦。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

Medi0cr1ty

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过