---
title: PHP代码审计-YXCMS-任意文件删除到任意文件读取利用链
url: https://mp.weixin.qq.com/s/u0FTaslkQsijfriQno4elg
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:50.035670
---

# PHP代码审计-YXCMS-任意文件删除到任意文件读取利用链

# PHP代码审计-YXCMS-任意文件删除到任意文件读取利用链

原创

wolfsec
wolfsec

风铃Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#### 文章中使用的源码以及工具文末获取。

#### 系统部署

解压压缩包，得到如下目录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlv6Auic4ZMnn21HwAWwxwicxHWa5JMCkrI6T9caZvfBYicPDMsWNcA18heYNBibdibsMicOYsIXxRzVtOLWGxbGrart0yHhWJibdF5fA4/640?wx_fmt=png&from=appmsg)

将code目录移动至web根路径下，并更改文件名为yxcms（此步骤可选，非必要），直接访问如下URL：

```
http://ip_address/yxcms
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsYQeZkZfteQKianPIbTt1PRpickm9RmARlAo6wnR6jfqKczuKqBeibN0ULgVhibjPjy8HFyEMXlxib9LHHnib73XC2l5Mxb3zoF0nBk/640?wx_fmt=png&from=appmsg)

接下去就是按照安装向导进行系统安装部署。需要注意的是，第二个步骤中`cache`目录刚开始检查为不可写，原因是`protected`目录中缺少`cache`目录，直接创建`cache`目录就可以解决这个问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZltA3rL8icb5CKwTnnnBUnzoInslgd57ecuibmaxRqhlxHM9t72sCUhMMQCJvelsQtrkJRdVTpKQ6c6PecNO106n1tcT2A3rSMibkI/640?wx_fmt=png&from=appmsg)

其他的安装步骤就比较常规了，这里就不贴出来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvGtlicVNOewKE9HVtEk2dk5qoVed0KfbOuwSicLRgGv0RibslBiaACsmWwtBwGX0HDVNh2WwfhaA3ViajzXCWWODxgl4BatllTzmL4/640?wx_fmt=png&from=appmsg)

后台路径：

```
http://127.0.0.1/yxcms/index.php?r=admin/index/login
```

前台路径：

```
http://127.0.0.1/yxcms/
```

#### 路由分析

代码审计第一步路由分析，先看入口文件`index.php`：

```
<?php
//print_r($_SERVER);
if( !empty($_SERVER['HTTP_X_REWRITE_URL']) ) $_SERVER['REQUEST_URI'] = $_SERVER['HTTP_X_REWRITE_URL'];
@set_time_limit(1000); //函数最久执行时间
@set_magic_quotes_runtime(0);   //关闭特殊字符提交的时候提示数据库错误
header("Centent-Type:text/html;charset=UTF-8");   //设置系统编码格式
header("Pragma: no-cache");  //禁止缓存
 //根目录
define('ROOT_PATH', dirname(__FILE__).DIRECTORY_SEPARATOR);
require( 'protected/core.php' );
?>
```

前面一堆代码，没有路由相关的信息，这边导入了`protected/core.php`，我们直接跟进`core.php`，跟进后发现该程序文件中定义了一些全局变量和函数，这边可以直接拉到代码底部，查看函数调用情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZltVUdFmeZHTwTrJMoHWTSQwqzB2bdcoLXEHG8CctFgeicvXcGEHyQ4QMiaaibh792Sia1qxbicDxHWJ5mBicuwiaO5ZaVia88V5FXOQxe4/640?wx_fmt=png&from=appmsg)

这里调用了`run()`函数，我们在这边打个断点，开始动调，接着访问任意功能点，分析系统路由设置规则。打完断点后，直接访问如下URL：

```
http://192.168.213.1/yxcms/index.php?r=member/index/login
```

接着跟进`run()`函数。

```
function run(){
    require(CP_PATH . 'core/cpConfig.class.php');//加载默认配置
    config( require(BASE_PATH . 'config.php') );//加载全局配置
    cpConfig::set('APP', array_merge(cpConfig::get('APP'), config('APP')));
    defined('DEBUG') or define('DEBUG', cpConfig::get('DEBUG'));
    date_default_timezone_set( cpConfig::get('TIMEZONE') );

    if ( DEBUG ) {
        ini_set("display_errors", 1);
        error_reporting( E_ALL ^ E_NOTICE );//除了notice提示，其他类型的错误都报告
    } else {
        ini_set("display_errors", 0);
        error_reporting(0);//把错误报告，全部屏蔽
    }

    urlRoute();//网址路由解析
    config('_APP_NAME', APP_NAME);
    config( appConfig(APP_NAME) ); //加载app配置
```

在`run()`函数中，我们看到了一个非常亮眼的函数调用：

```
urlRoute();//网址路由解析
```

直接跟进`urlRoute()`函数：

```
function urlRoute(){
    $rewrite = config('REWRITE');
    if( !empty($rewrite) ) {
        if( ($pos = strpos( $_SERVER['REQUEST_URI'], '?' )) !== false ){
            parse_str( substr( $_SERVER['REQUEST_URI'], $pos + 1 ), $_GET );
        }
        foreach($rewrite as $rule => $mapper){
            $rule = ltrim($rule, "./\\");
            if( false === stripos($rule, 'http://')){
                $rule = $_SERVER['HTTP_HOST'].rtrim(dirname($_SERVER["SCRIPT_NAME"]),'/\\').'/'.$rule;
            }
            $rule = '/'.str_ireplace(array('\\\\', 'http://', '-', '/', '<', '>',  '.'), array('', '', '\-', '\/', '(?<', ">[a-z0-9_%]+)", '\.'), $rule).'/i';
            if(preg_match($rule,$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'],$matches)){
                foreach($matches as $matchkey => $matchval){
                    if(('app' === $matchkey)){
                        $mapper = str_ireplace('<app>', $matchval, $mapper);
                    }else if('c' === $matchkey){
                        $mapper = str_ireplace('<c>', $matchval, $mapper);
                    }else if('a' === $matchkey){
                        $mapper = str_ireplace('<a>', $matchval, $mapper);
                    } else {
                        if( !is_int($matchkey) ) $_GET[$matchkey] = $matchval;
                    }
                }
                $_REQUEST['r'] = $mapper;
                break;
            }
        }
        if(empty($_REQUEST['r']) && trim($_SERVER["REQUEST_URI"],'/')) $_REQUEST['nor']=true;
    }
    $route_arr = isset($_REQUEST['r']) ? explode("/", htmlspecialchars($_REQUEST['r'])) : array();
    $app_name = empty($route_arr[0]) ? DEFAULT_APP : strtolower($route_arr[0]);
    $controller_name = empty($route_arr[1]) ? DEFAULT_CONTROLLER : strtolower($route_arr[1]);
    $action_name = empty($route_arr[2]) ? DEFAULT_ACTION : $route_arr[2];
    $_REQUEST['r'] = $app_name .'/'. $controller_name .'/'. strtolower($action_name);

    define('APP_NAME', $app_name);
    define('CONTROLLER_NAME', $controller_name);
    define('ACTION_NAME', $action_name);
}
```

重点代码：

```
    $route_arr = isset($_REQUEST['r']) ? explode("/", htmlspecialchars($_REQUEST['r'])) : array();
    //$route_arr[0]如果为空则值为 DEFAULT_APP = default
    $app_name = empty($route_arr[0]) ? DEFAULT_APP : strtolower($route_arr[0]);
    //$route_arr[1]如果为空则值为 DEFAULT_CONTROLLER = index
    $controller_name = empty($route_arr[1]) ? DEFAULT_CONTROLLER : strtolower($route_arr[1]);
    //$route_arr[1]如果为空则值为 DEFAULT_ACTION = index
    $action_name = empty($route_arr[2]) ? DEFAULT_ACTION : $route_arr[2];
    $_REQUEST['r'] = $app_name .'/'. $controller_name .'/'. strtolower($action_name);
```

`$route_arr`是通过获取 `r` 参数，对其进行 HTML 特殊字符编码，然后按照 `/` 分割成数组获得。

访问URL：http://192.168.213.1/yxcms/index.php?r=member/index/login 得到的数据如下：

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvzQHWSg0otS2vEAqQbLG6N8DGF8BnPxwZVQ3CKTC3HibfuJSBiaanhZEHicyp6qh8xicN02bd4KUth7yzgFibibnNPKic2hIaDDJsBko/640?wx_fmt=png&from=appmsg)

最后得到了三个全局变量：

```
APP_NAME = member
CONTROLLER_NAME = index
ACTION_NAME = login
```

继续步进，看到如下代码：

```
    config('_APP_NAME', APP_NAME);
    config( appConfig(APP_NAME) ); //加载app配置
```

步入`appConfig`：

```
function appConfig($app){
    static $appConfig = array();
    if( !isset( $appConfig[$app]) ){
        if( is_file(BASE_PATH . 'apps/' . $app . '/config.php') ){
            $appConfig[$app] = require(BASE_PATH . 'apps/' . $app . '/config.php');
        }else{
            $appConfig[$app] = array();
        }
    }
    return $appConfig[$app];
}
```

`appConfig($app)` 函数是一个应用配置文件加载函数，在这个函数中可以初步判断操作目录实际上就是`protected/apps/APP_NAME`目录。

然后继续步进，找到引入`Controller`和`Action`的关键代码：

```
        spl_autoload_register( 'autoload' );
        $controller = CONTROLLER_NAME . 'Controller';
        $action = ACTION_NAME;

        if( !class_exists($controller) ) {
            throw new Exception(APP_NAME. '/' .$controller.'.php 控制器类不存在', 404);
        }
        $obj = new $controller();

        if( !method_exists($obj, $action) ){
            throw new Exception(APP_NAME. '/' .$controller.'.php的' . $action.'() 方法不存在', 404);
        }
        $obj ->$action();
    } catch( Exception $e){
        cpError::show( $e->getMessage(), $e->getCode());
    }
```

这段代码是一个典型的 MVC 架构中的控制器路由分发机制，动调得到对应的命名规则。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvM7fZVBZdGUrsDpVjWKqpWLJjjBnibvfelbqafR0E7qoC58KehYO5uibFcRfa9YcJibFRtht9P75MNMZOUDf7YpIPhdmSqOs7swE/640?wx_fmt=png&from=appmsg)

继续步进，当控制器存在的时候，则new一个控制器对象：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsqontq9vfsGyaKCO1ZStUWYN9YLkziaaFpsSichllGZicYKQY6tUml7rmw7eFJHESS0IXqlvxMnz77hg4wicGSaBCmlhkvab2LAp8/640?wx_fmt=png&from=appmsg)

在创建控制器对象后，还会调用控制器的对应方法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsdRoT2RaMvoicnb3JMLsWu18oL1TO85lMoolpGTLa4uq2tYF8WUhBiacw0kTtYTUicicGWYHicvFOdDnkq0mS61tTZGujEh23HbLLU/640?wx_fmt=png&from=appmsg)

到这里直接步入，得到功能相关代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlv0sYIaZPr0kePAFZ9uWibbtzruJWLqqMAYTribxA5AXEcUMeeiacjLoTAKTNTg3zQ9eoljicHWxLVJn7qpSe1nMuYoibCkDbhP0aX4/640?wx_fmt=png&from=appmsg)

到这里，路由分析结束，总结...