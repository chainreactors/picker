---
title: Go Mod引用私有库 – 九霄天空-IT技术分享学习
url: https://buaq.net/go-152596.html
source: unSafe.sh - 不安全
date: 2023-03-09
fetch_date: 2025-10-04T08:59:35.973985
---

# Go Mod引用私有库 – 九霄天空-IT技术分享学习

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9bdac8b15112c815430765a69c9daa72.jpg)

Go Mod引用私有库 – 九霄天空-IT技术分享学习

在Go 1.11之后推出了依赖包管理工具Go Modules之后，Go项目可以在 GOPATH 之外的位置创建，当项目中仅使用了公有库作为依赖时，使用 g
*2023-3-8 21:3:17
Author: [turbock79.cn(查看原文)](/jump-152596.htm)
阅读量:32
收藏*

---

在Go 1.11之后推出了依赖包管理工具Go Modules之后，Go项目可以在 GOPATH 之外的位置创建，当项目中仅使用了公有库作为依赖时，使用 go get 或 go mod 更新依赖一切如初，没有任何问题。

由于Go Modules默认使用代理去更新依赖，所以当使用了私有仓库作为依赖时，Go更新依赖的相关命令将不再可用。

* 本文最新状态查看链接：[Go Mod引用私有库](https://turbock79.cn/?p=3570)

## 1. 基础方式：Golang私有项目的路径替换

如果私有项目A依赖另一个私有项目B，且通过go get无法获取权限，可以采用replace方式；

在A项目中的go.mod文件中，加入 replace 操作；

|  |  |
| --- | --- |
|  | module gitlab.example.com/A  replace "gitlab.example.com/B" => "../B |

* Go Get模式下，私有module多级引用: `go get [[email protected]](https://turbock79.cn/cdn-cgi/l/email-protection) [[email protected]](https://turbock79.cn/cdn-cgi/l/email-protection)`

## 2. 高级方式：go mod私有项目的访问

### 2.1. 配置go环境变量

go get通过代理服务拉取私有仓库（企业内部module或托管站点上的private库），而代理服务不可能访问到私有仓库，会出现了404错误. Go提供了一个方便的解决方案：GOPRIVATE环境变量。通过以下配置，可以实现更新私有库依赖。

### 2.2. 设置 Go GOPRIVATE 变量

|  |  |
| --- | --- |
|  | # 配置多个私有项目地址  go env -w GOPRIVATE="gitlab.example.com"  # 其中gitee.com/user 是你的个人账户所在地址 |

* 默认情况下，如果设置GOPRIVATE，会自动设置GONOPROXY和GONOSUMDB配置；
* Golang项目非代理NOPROXY配置

  如果设置GONOPROXY和GONOSUMDB均为none，意味着所有module，不管是公共的还是私有的，都要经过proxy下载，经过sumdb验证；

  |  |  |
  | --- | --- |
  |  | GONOPROXY= "gitlab.example.com"  GONOSUMDB= "gitlab.example.com" |

## 3. [Go到私有仓库的请求认证](https://docs.gitlab.com/ee/user/project/working_with_projects.html#authenticate-go-requests-to-private-projects)

### 3.1. 必要条件

* GitLab 实例必须能够通过HTTPS访问
* 必须拥有私有访问秘钥,或是access token，或是ssh key；

### 3.2. 方法一：Go请求的认证, 创建.netrc文件

* Linux下创建文件`~/.netrc`

  |  |  |
  | --- | --- |
  |  | $ vi ~/.netrc  machine  <gitlab.example.cn>  login <gitlab\_user\_name>  password <personal\_access\_token> |

  其中`<gitlab_user_name>`为gitlab的用户名，`<personal_access_token>`为在gitlab中申请的私有access token，对private级别项目也可生效；
* Windows系统下, Go 读取文件为 `~/_netrc`而不是Linux下的 `~/.netrc`。
* Go命令不会在非安全链接下传输证书，所以它会通过Go创建的https请求完成认证，而不是通过Git创建的认证请求；
* personal\_access\_token申请如下

### 3.3. 方法二：Git请求认证

如果Go无法通过代理获取module,会使用Git。 Git使用`.netrc`文件完成认证请求，但是也可通过其他认证方法。下面也可通过Git配置：

#### 3.3.1. 在请求URL中嵌入认证信息Access\_Token

|  |  |
| --- | --- |
|  | git config --global url."https://${user}:${personal\_access\_token}@gitlab.example.com".insteadOf "https://gitlab.example.com" |

* Git全局配置查看和删除

|  |  |
| --- | --- |
|  | #查看git全局配置  git config --global -l  # 删除url路径替换, 或是修改${GitProject}/.git/config文件中对应url |

#### 3.3.2. 使用SSH替换HTTPS进行认证

* [多ssh认证](https://github.com/golang/go/issues/42751)

The explicit env settings are unnecessary
The tidy should be called before vendor to have a consistent state
You can setup git and ssh configs(~/.ssh/config) so they will automatically use the right profiles:

|  |  |
| --- | --- |
|  | $ ~/.ssh/config  Host github-personal      Hostname github.com #网站地址      User git        #git ssh访问      IdentityFile ~/.ssh/id\_ed25519\_personal  #区别在于指定不通key  Host github-work      Hostname github.com      User git      IdentityFile ~/.ssh/id\_ed25519\_work  # git配置      insteadOf = "https://github.com/work/"      insteadOf = "https://github.com/personal/" |

## 4. [Gitlab Bug: Sub Groups](https://gitlab.com/gitlab-org/gitlab/-/issues/36354)

该问题，建议采用netrc的方式解决；直接可以规避Gitlab中SubGroups的bug问题；例如`gitlab.example.com/subgroup1/subgroup2/project1`；

* 如果非要采用git ssh/https方式改动，可以参考文章[Go Module 工程化实践（二）：go get 取包原理篇](https://studygolang.com/articles/18726?fr=sidebar)

go get的源码实现中，包的查询路径是通过一组正则匹配出来的；下载golang的代码后，查看文件 /usr/lib/golang/src/cmd/go/internal/get/vcs.go； 修改私有仓库正则表达式，并在实例路径`${GOROOT}/src/cmd/go`路径下编译go的二进制文件，拷贝到${GOROOT}/bin路径下即可；

## 5. Golang私有项目的http访问

如果私有库不支持https协议，会报如下的错误。这是因为Go更新依赖时，会强制校验CA证书来确保依赖库的安全性。

|  |  |
| --- | --- |
|  | go: gitee.com/modules/project@v0.0.0-20200320063051-28c4ad7fe2ea: unrecognized import path "gitee.com/modules/project": https fetch: Get "https://gitee.com/modules/project?go-get=1": dial tcp 123.123.123:443: connect: connection refused |

如果私有库不支持https协议，还需要go配置参数或环境变量，使其使用http方式访问

### 5.1. 方法一`go get -insecure`

使用 `go get -insecure`,这种方式不推荐，原因如下：

* 添加 -insecure 参数即表示更新依赖时可以不去校验CA证书，但是这会带来一个问题：范围无法界定(overkill)，所有与要更新依赖相关联的依赖，均不会去做校验，可能会意外更新到不安全的依赖。
* `-insecure` 仅支持 go get 命令，不支持 go mod 命令，因此使用 go mod 命令时是无法更新不支持https协议的私有库的。

### 5.2. 方法二`GOINSECURE`

添加 GOINSECURE 参数,**推荐这种方式**

* 在Go 1.14中增加了新的环境变量，用于指定哪些域名下的仓库不去校验CA证书。
* 使用方式同 GOINSECURE 类似 `go env -w GOINSECURE=gitlab.example.com`

## 6. 版本解决：invalid version: unknown revision 000000000000

在私有仓库中，暂时没有打tag指定版本。这里通过指定分支，实现对应hash值得指定；报错如下： `gitlab.example.cn/[[email protected]](https://turbock79.cn/cdn-cgi/l/email-protection): invalid version: unknown revision 000000000000`

1. 修改go.mod指定库的版本到指定分支

   |  |  |
   | --- | --- |
   |  | //go.mod文件  module gitlab.example.cn/projectA  go 1.16  require (      //因projectB并没有打tag，这里通过指定master分支，自动获取其hash值；也可指定其他分支；      gitlab.example.cn/projectB master  ) |
2. 执行`go mod tidy`命令，自动检出对应版本；

   查看配置自动更新如下：

   |  |  |
   | --- | --- |
   |  | //go.mod文件  module gitlab.example.cn/projectA  go 1.16  require (      //因projectB并没有打tag，这里通过指定分支，自动获取其版本值，版本号-时间戳-提交Hash值；      gitlab.example.cn/projectB v0.0.0-20220523020601-cbdabf7b07db  ) |

## 7. 参考文章

* [Go 1.14解决Go Modules模式下更新私有库问题](https://www.cnblogs.com/hiwz/p/12652153.html)
* [Unable to `go get` go-packages in repositories in nested sub groups deeper than 1](https://gitlab.com/gitlab-org/gitlab/-/issues/36354)
* [Go Module 工程化实践（二）：go get 取包原理篇](https://studygolang.com/articles/18726?fr=sidebar)

赞赏

![](https://turbock79.cn/wp-content/uploads/2020/10/微信收款_副本-1.png)微信赞赏![](https://turbock79.cn/wp-content/uploads/2020/10/支付宝收款_副本-1.jpg)支付宝赞赏

文章来源: https://turbock79.cn/?p=3570
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)