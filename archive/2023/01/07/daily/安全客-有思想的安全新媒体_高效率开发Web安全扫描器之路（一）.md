---
title: 高效率开发Web安全扫描器之路（一）
url: https://www.anquanke.com/post/id/283900
source: 安全客-有思想的安全新媒体
date: 2023-01-07
fetch_date: 2025-10-04T03:14:37.489960
---

# 高效率开发Web安全扫描器之路（一）

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 高效率开发Web安全扫描器之路（一）

阅读量**1116990**

发布时间 : 2023-01-06 14:00:19

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 一、背景

经常看到一些SRC和CNVD上厉害的大佬提交了很多的漏洞，一直好奇它们怎么能挖到这么多漏洞，开始还以为它们不上班除了睡觉就挖漏洞，后来有机会认识了一些大佬，发现他们大部分漏洞其实是通过工具挖掘的，比如说下面是CNVD上面的白帽子大佬

![]()

我想成为大佬要怎么做

我一直觉得自己是一个有梦想的人，我也想有一天自己的ID能出现在排行榜中，于是我凭借着自己那一点开发知识，认真研究了一下市面上的安全工具，以及怎么开发安全工具。

## 安全工具分析

经过我得研究发现市面上的安全工具其实只有两类，一类是面向某个漏洞的工具比如SQLMap，另外一个一类是综合扫描工具，比如AWVS；

作为一个只想挖漏洞的我，我更偏向于综合型的扫描器开发，可是综合型的扫描器开发难度真的很大，要清晰地了解各种漏洞的原理，而且还需要把他们使用代码去实现，如果是我一个人从头开发我压根做不到啊。

但我并不打算放弃，我准备集结天下之利器，为我扫描器所用；理想是有了，但现实是我要怎么实现，这可真实苦恼了我。

## 二、 要做的东西

我想要做的扫描器核心目的就是要使用简单，另外就是我可以随心所欲的修改；我希望是我只要给他一个URL地址，它就可以帮我扫描网站的漏洞，以及这个主机本身的漏洞

细致的拆解了一下，我觉得最需要的功能有这几个

![]()

1. 能自动收集URL地址，爬虫收集和爆破收集
2. 能从URL中提取主机IP
3. 能快速检测常见的热门POC
4. 能自动识别网站的指纹信息
5. 能对IP进行端口快速扫描
6. 能对端口的banner识别出服务
7. 能检测出SQL注入漏洞
8. 能检测出反射性XSS漏洞
9. 能够通过指纹信息，使用对应的POC工具
10. 能够快速扩展功能，且不影响整体逻辑

第一版本差不多就是这些功能吧，功能虽然不算多，但如果完全从头开始实现开发时间可不少。

## 三、思路分析

为了达到高效率的同时又能自主可控，我决定做一个有水平的缝合侠，简单理解就是我要把很多工具巧妙的融入到我开发的工具来，这里需要考虑的第一个问题是每个工具的使用方法、输入的参数、输出的结果都是不一样的，工具A的结果工具B不一定认识。

要解决这个问题，说简单也简单说难也难，总之我是摸着石头过河成功了；原理是自己给每个工具做一个壳，外部要调用工具A需要先调用工具A的壳，然后才会传到工具A，当工具A返回了结果，工具A的壳也会最先拿到，然后将结果解析出来并按照统一的格式输出就可以了。

![]()

通过这个简单的办法，我相当于把其他的安全工具变成了我得一个函数，我需要的时候调用这个函数就可以了。

按照我前面提到的需求，我梳理了一下要试用的工具有这几个:

序号

| 序号 | 需求 | 工具 |
| --- | --- | --- |
| 1. | 爬去URL的有 | RAD |
| 2. | 爆破URL的有 | DIRMAP |
| 3. | 提取主机IP | 正则 |
| 4. | 快速检测热门POC | xray |
| 5. | 识别网站的指纹 | dismap |
| 6. | 对IP端口快速扫描 | masscan |
| 7. | 能对端口的banner识别出服务 | nmap |
| 8. | 能检测出SQL注入漏洞 | sqlmap |
| 9. | 能检测出反射性XSS漏洞 | xsser |

这些工具都是比较常见的工具，我第一步需要对他们的使用方法熟悉，以xray工具为例

xray的使用命令如下所示

```
./xray_linux_amd64 webscan --url "http://192.168.1.100/" --json-output /tmp/11.json
```

当xray执行完毕之后，他会将结果输出到指定位置，但是数据格式并不是我所期望的，我需要将它的格式读入，然后再转换成我所需要的格式。

这里我用PHP写了一个简单的脚本，他做了这几件事情：

1. 定义了参数来源位置和结果输出位置
2. 获取参数中的URL，并执行xray工具
3. 获取xray的执行结果，并解析成自定义格式
4. 将最终的结果写入到输出位置

代码示例如下所示

```
<?php
//获取输入的参数
$inputFile = "/data/share/input_".getenv("xflow_node_id").".json";
$outputFile = "/data/share/output_".getenv("xflow_node_id").".json";

//没有input,直接返回
if (!file_exists($inputFile)) {
    var_dump($outputFile, json_encode(['code' => 0, 'msg' => "{$inputFile}文件不存在", 'data' => []], JSON_UNESCAPED_UNICODE));
    return 0;
}
//读取上游数据
$inputData = json_decode(file_get_contents($inputFile), true);

$url = $inputData['url'];
$data = execTool($url);

//将结果写入到指定位置,供蜻蜓平台导入数据
file_put_contents($outputFile, json_encode($data, JSON_UNESCAPED_UNICODE));

//将工具执行
function execTool($url)
{

    $hash = md5($url);
    $resultPath = "/tmp/{$hash}/tool.json";
    //清理之上一轮的结果
    if (file_exists($resultPath)) unlink($resultPath);
    //创建文件夹
    if (!file_exists(dirname($resultPath))) {
        mkdir(dirname($resultPath), 0777, true);
    }

    $result = [];

    $toolPath = "/data/tools/xray";
    if (!file_exists($toolPath)) die("xray 工具目录不存在:{$toolPath}");

    $path = "cd $toolPath && ";
    // 通过系统命令执行工具
    $cmd = "{$path} ./xray_linux_amd64 webscan --url \"{$url}\" --json-output {$resultPath}";
    echo $cmd;
    exec($cmd, $result);

    $toolResult = file_exists($resultPath) ? file_get_contents($resultPath) : '[]';
    $toolResult = json_decode($toolResult, true);
    print_r($toolResult);
    return $toolResult;
}
```

再来sqlmap封装的例子，首先需要知道sqlmap的使用的方法，如下所示

```
sqlmap -u "http://192.168.1.100/index.php?id=1"  --batch  --random-agent
```

当sqlmap执行完毕之后，我需要知道他的执行结果在什么位置,并将结果解析出来，按照规范化的格式输出到指定地址。

这里我同样用PHP写了一个脚本，做了这几件事情：

1. 定义了参数来源位置和结果输出位置
2. 获取参数中的URL，并执行sqlmap工具
3. 获取sqlmap的执行结果，并解析成自定义格式
4. 将最终的结果写入到输出位置

```
<?php
//获取输入的参数
$inputFile = “/data/share/input“.getenv(“xflow_node_id”).”.json”;
$outputFile = “/data/share/output“.getenv(“xflow_node_id”).”.json”;
//没有input,直接返回
if (!file_exists($inputFile)) {
file_put_contents($outputFile, json_encode([]));
return 0;
}
//读取上游数据
$list = json_decode(file_get_contents($inputFile), true);
print_r($inputFile);
print_r($list);
$data = [];
//处理数据
foreach ($list as $val) {
$url = $val[‘url’];
$toolPath = “/data/tools/sqlmap/“;

print_r("开始扫描URL:{$url}".PHP_EOL);
execTool($url, $toolPath);

//录入检测结果
$tempList = writeData($toolPath, $url);
print_r("扫描URL:{$url}完成".PHP_EOL);
print_r($tempList);
$data = array_merge($data, $tempList);
}

print_r($data);
//将结果写入到指定位置,供蜻蜓平台导入数据
file_put_contents($outputFile, json_encode($data, JSON_UNESCAPED_UNICODE));

function writeData($toolPath, $url)
{

$arr = parse_url($url);
$file_path = $toolPath . 'result/';
$host = $arr['host'];
$outdir = $file_path . "{$host}/";
$outfilename = "{$outdir}/log";

//sqlmap输出异常
if (!is_dir($outdir) or !file_exists($outfilename) or !filesize($outfilename)) {
    print_r("sqlmap没有找到注入点: $url");
    return [];
}
$ddd = file_get_contents($outfilename);
print_r($ddd);

exec("rm -rf $outdir");

return [["raw" => $ddd]];
}

function execTool($v, $toolPath)
{

$arr = parse_url($v);
$blackExt = ['.js', '.css', '.json', '.png', '.jpg', '.jpeg', '.gif', '.mp3', '.mp4'];
//没有可以注入的参数
if (!isset($arr['query']) or (strpos($arr['query'], '=') === false)) {
    print_r(["URL地址不存在可以注入的参数".PHP_EOL, $v]);
    return false;
}
$file_path = $toolPath . 'result/';
$cmd = "cd {$toolPath}  && python3 ./sqlmap.py -u '{$v}' --batch  --random-agent --output-dir={$file_path}";
exec($cmd);
return true;
}
```

通过前面xray和sqlmap两个工具封装的例子，你回发现其实每个工具封装的流程都差不多，差一点只是程序的输出结果解析而已，所以到现在位置我解决了扫描器的能力问题。

## 四、动手实践

现在只需要我把几个功能连接起来就行了，这里需要考虑一个新的问题；sqlmap所需要的参数确是具体的多个URL地址，也就是说在调用sqlmap之前，我需要把URL都收集好再调用sqlmap，这里就有数据依赖问题。

这个问题也好办，我们需要准备三张表: 目标表、功能依赖表、数据存放表。

目标表

| ID | URL | create\_time |

功能表

| ID | tool\_name | pre\_tool\_name | create\_time |

数据表

| ID | tool\_name  | url  | result | create\_time |

我们可以首先从目标表中获取一个要扫描的目标，然后读取所有的功能，for循环功能表,只需判断当前有没有依赖问题，或者依赖问题已经解决，那么就可以得到所需的依赖数据，直接执行功能即可。

伪代码如下所示：

执行完成结果可以在结果页面看见，这里是我的执行结果。

![]()

伪代码如下所示：

```
<?php

$id = getTarget();
$toolLst = getToolList();

foreach($toolList as $val){
//判断当前工具上级依赖为空或者上级工具已执行
if($val[‘pre_tool_name’] == ‘’ or 上级工具已经执行){
//开始使用工具对URL扫描
scanUrl();
//保存结果
svaeResult();

} else(){
    //上级工具还没执行完成,先跳过
    continue;
}
}
```

这是我写好的脚本，大家可以简单改改应用，目前我写的脚本已经集成到了蜻蜓安全平台里面，你可以一键复制使用

![]()

<http://qingting.starcross.cn/scenario/detail?id=1931>

目前我已经集成了46常见的款工具，放在GitHub中开源，地址：<https://github.com/StarCrossPortal/QingTing>

---

作者：汤青松
日期：2022-11-29
微信：songboy8888

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**qingsongboy**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283900](/post/id/283900)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全工具](/tag/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7)

**+1**25赞

收藏

![](https://p4.ssl.qhmsg.com/dm/200_200_100/t0165c1e612a26d7a12.jpg)qingsongboy

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhmsg.com/dm/200_200_100/t0165c1e612a26d7a12.jpg)](/member.html?memberId=128405)

[qingsongboy](/member.html?memberId=128405)

这个人太懒了，签名都懒得写一个

* 文章
* **7**

* 粉丝
* **2**

### TA的文章

* ##### [开源dolphin项目-ASM网络资产风险监测系统](/post/id/287246)

  2023-03-15 16:30:19
* ##### [高效率开发Web安全扫描器之路（一）](/post/id/283900)

  2023-01-06 14:00:19
* ##### [GitLab结合fortify实现自动化代码审计实践](/post/id/284200)

  2023-01-05 16:30:23
* ##### [蜻蜓低代码安全工具平台开发之路](/post/id/275235)

  2022-06-27 10:30:50
* ##### [CIS 2021网络安全创新大会《代码安全体系建设》实录](/post/id/270173)

  2022-05-30 15:30:57

### 相关文章

* ##### [SiCat：漏洞检测新工具](/post/id/293257)

  2024-02-18 16:36:45
* ##### [使用 gopacket 从网络捕获及重组数据包](/post/id/288460)

  2023-06-12 15:58:16
* #####...