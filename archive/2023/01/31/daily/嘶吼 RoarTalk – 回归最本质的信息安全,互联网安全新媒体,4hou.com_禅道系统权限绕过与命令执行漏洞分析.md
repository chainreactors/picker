---
title: 禅道系统权限绕过与命令执行漏洞分析
url: https://www.4hou.com/posts/mXr9
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-31
fetch_date: 2025-10-04T05:12:37.832659
---

# 禅道系统权限绕过与命令执行漏洞分析

禅道系统权限绕过与命令执行漏洞分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 禅道系统权限绕过与命令执行漏洞分析

盛邦安全
[技术](https://www.4hou.com/category/technology)
2023-01-30 16:37:35

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)219164

收藏

导语：本文以安全研究为目的，分享对该漏洞的研究和复现过程，仅供学习和参考。

**漏洞概述**

禅道是第一款国产的开源项目管理软件，也是国内最流行的项目管理软件。该系统在2023年初被爆出在野命令执行漏洞，官方已于2023年1月12日发布了漏洞修复补丁。该漏洞是由于禅道项目管理系统权限认证存在缺陷导致，攻击者可利用该漏洞在未授权的情况下，通过权限绕过在服务器执行任意命令。

本文以安全研究为目的，分享对该漏洞的研究和复现过程，仅供学习和参考。由于传播、利用此文档提供的信息而造成任何直接或间接的后果及损害，均由使用者本人负责，文章作者不为此承担任何责任。

影响范围

|  |  |
| --- | --- |
| 禅道系统 | 影响版本 |
| 开源版 | 17.4以下的未知版本<=version<=18.0.beta1 |
| 旗舰版 | 3.4以下的未知版本<=version<=4.0.beta1 |
| 企业版 | 7.4以下的未知版本<=version<=8.0.beta1 8.0.beta2 |

复现环境

操作系统：macOS 13.1

运行环境：nginx1.5 php7.4 mysql5.7

软件版本：zentaopms-zentaopms\_18.0.beta1

**权限绕过-漏洞分析**

权限绕过的关键点在module/common/model.php文件中checkPriv函数，此函数是检查权限的函数，验证当前登陆用户是否有访问module与method的权限。分析代码后得知在没有访问权限时会抛出异常，但是代码中并没有终止程序，只是输出权限不足的内容。具体代码如下：

```
public function checkPriv(){        try        {            $module = $this->app->getModuleName();            $method = $this->app->getMethodName();            if($this->app->isFlow)            {                $module = $this->app->rawModule;                $method = $this->app->rawMethod;            }
            $beforeValidMethods = array(                'user'    => array('deny', 'logout'),                'my'      => array('changepassword'),                'message' => array('ajaxgetmessage'),            );            if(!empty($this->app->user->modifyPassword) and (!isset($beforeValidMethods[$module]) or !in_array($method, $beforeValidMethods[$module]))) return print(js::locate(helper::createLink('my', 'changepassword')));            if($this->isOpenMethod($module, $method)) return true;            if(!$this->loadModel('user')->isLogon() and $this->server->php_auth_user) $this->user->identifyByPhpAuth();            if(!$this->loadModel('user')->isLogon() and $this->cookie->za) $this->user->identifyByCookie();
            if(isset($this->app->user))            {                if(in_array($module, $this->config->programPriv->waterfall) and $this->app->tab == 'project' and $method != 'browse') return true;
                $this->app->user = $this->session->user;                if(!commonModel::hasPriv($module, $method))                {                    if($module == 'story' and !empty($this->app->params['storyType']) and strpos(",story,requirement,", ",{$this->app->params['storyType']},") !== false) $module = $this->app->params['storyType'];                    $this->deny($module, $method);                }            }            else            {                $uri = $this->app->getURI(true);                if($module == 'message' and $method == 'ajaxgetmessage')                {                    $uri = helper::createLink('my');                }                elseif(helper::isAjaxRequest())                {                    die(json_encode(array('result' => false, 'message' => $this->lang->error->loginTimeout))); // Fix bug #14478.                }
                $referer = helper::safe64Encode($uri);                die(js::locate(helper::createLink('user', 'login', "referer=$referer")));            }        }        catch(EndResponseException $endResponseException)        {            echo $endResponseException->getContent();        }    }
```

其中commonModel::hasPriv()函数是内置公共的验证权限，代码中可以看出无权限访问就会执行deny 方法，而deny 最后验证的结果是无权限则执行helper::end()，该方法是直接抛出异常，就会进入上面的try  cache逻辑。

```
 public static function end($content = '')
 {
 throw EndResponseException::create($content);
 }
```

在进入权限检查的流程前需要在$this->app->user 不为空的情况下将 $this->session->user赋值给 $this->app->user ，然后再做权限检查。因此我们还需要构造一个$this->session->user，即写一个session['user']才能进行绕过。所以现在思路很清晰了，只需$this->session->user 存在就可以通过⽤户是否登录的检查，使权限检查的函数如同虚设。 根据这个思路逆推可以得出结论：只要有任意⼀个⽤户session就可以调⽤任意模块的任意⽅法。

经过代码审计发现captcha函数可以直接写入一个自定义key的session，此段代码本意是设置生成一个自定义session的key的验证码，开发者应该是想写一个公共的验证码生成函数让其他开发者做新功能需要的时候可以直接调用，正好可以利用生成一个key为user的session。

```
public function captcha($sessionVar = 'captcha', $uuid = '')    {        $obLevel = ob_get_level();        for($i = 0; $i < $obLevel; $i++) ob_end_clean();
        header('Content-Type: image/jpeg');        $captcha = $this->app->loadClass('captcha');        $this->session->set($sessionVar, $captcha->getPhrase());        $captcha->build()->output();    }
```

通过上述思路可以成功实现权限绕过，不过经过实际测试发现，能绕过访问的皆为公共模块。因为在禅道的功能权限验证中还有一部分是验证userid或level。就好比某些用户有“项目1”的权限，某些用户有“项目2”的权限，所以类似这类的数据任然不能访问获取。

**命令执行-漏洞分析**

实际上整个利用链最关键的一环就在上面的权限绕过上，禅道系统后台本身存在多个sql注入及命令执行漏洞，本文给出一种后台命令执行的方法供参考，其他利用点感兴趣的小伙伴可自行研究。

在权限绕过后，接下来我们需要分析后台命令执行点的位置。通过代码审计，最终锁定在module/repo/model.php文件，其中checkConnection函数会进行SCM=Subversion判断，$client是导致命令注入的参数点，一条完整的函数间调用的利用过程如下所示：

module/repo/model.php->create()

module/repo/control.php->edit ()

module/repo/model.php->update($repoID)->checkConnection()->exec($versionCommand,$versionOutput, $versionResult);

PS：为什么要创建仓库，因为在查看checkConnection调用函数为create和update，但是在create的时候必须经过checkClient 的判断，必须要创建一个文件才行，如果SCM指定为Gitlab就不需要通过checkClient判断。

![1675061020606412.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675061354104629.png "1675061020606412.png")

1.进入创建仓库的函数:module/repo/model.php

```
public function create(){    if(!$this->checkClient()) return false;    if(!$this->checkConnection()) return false;
    $isPipelineServer = in_array(strtolower($this->post->SCM), $this->config->repo->gitServiceList) ? true : false;
    $data = fixer::input('post')        ->setIf($isPipelineServer, 'password', $this->post->serviceToken)        ->setIf($this->post->SCM == 'Gitlab', 'path', '')        ->setIf($this->post->SCM == 'Gitlab', 'client', '')        ->setIf($this->post->SCM == 'Gitlab', 'extra', $this->post->serviceProject)        ->setIf($isPipelineServer, 'prefix', '')        ->setIf($this->post->SCM == 'Git', 'account', '')        ->setIf($this->post->SCM == 'Git', 'password', '')        ->skipSpecial('path,client,account,password')        ->setDefault('product', '')        ->join('product', ',')        ->setDefault('projects', '')->join('projects', ',')        ->get();    $data->acl = empty($data->acl) ? '' : json_encode($data->acl);    if($data->SCM == 'Subversion')    {        $scm = $this->app->loadClass('scm');        $scm->setEngine($data);        $info     = $scm->info('');        $infoRoot = urldecode($info->root);        $data->prefix = empty($infoRoot) ? '' : trim(str_ireplace($infoRoot, '', str_replace('\\', '/', $data->path)), '/');        if($data->prefix) $data->prefix = '/' . $data->prefix;    }
```

当SCM类型指定为Subversion时，后续控制$client才可以完成命令注入。

2.编辑代码仓库进入module/repo/control.php中的edit函数，post传参会进入到update函数。

```
public function edit($repoID, $objectID =...