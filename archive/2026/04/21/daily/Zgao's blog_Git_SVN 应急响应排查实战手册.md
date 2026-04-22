---
title: Git/SVN 应急响应排查实战手册
url: https://zgao.top/git-svn-%e5%ba%94%e6%80%a5%e5%93%8d%e5%ba%94%e6%8e%92%e6%9f%a5%e5%ae%9e%e6%88%98%e6%89%8b%e5%86%8c/
source: Zgao's blog
date: 2026-04-21
fetch_date: 2026-04-22T04:43:40.980427
---

# Git/SVN 应急响应排查实战手册

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# Git/SVN 应急响应排查实战手册

* [首页](https://zgao.top)
* [Git/SVN 应急响应排查实战手册](https://zgao.top:443/git-svn-%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E6%8E%92%E6%9F%A5%E5%AE%9E%E6%88%98%E6%89%8B%E5%86%8C/)

[4月 21, 2026](https://zgao.top/2026/04/)

### Git/SVN 应急响应排查实战手册

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/git-svn-%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E6%8E%92%E6%9F%A5%E5%AE%9E%E6%88%98%E6%89%8B%E5%86%8C/)

当你凌晨三点被电话叫醒，被告知”代码仓库可能被人动过了，用户的加密货币资产黑客全部转移”。你需要的不是恐慌，而是一套系统化的排查流程。本文是我经历过多次代码投毒的真实案例后，写的实战排查手册。

文章目录

[ ]

* [为什么要关注版本控制系统安全](#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E5%85%B3%E6%B3%A8%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8 "为什么要关注版本控制系统安全")
* [代码仓库投毒真实案例](#%E4%BB%A3%E7%A0%81%E4%BB%93%E5%BA%93%E6%8A%95%E6%AF%92%E7%9C%9F%E5%AE%9E%E6%A1%88%E4%BE%8B "代码仓库投毒真实案例")
  + [xz-utils 后门 (CVE-2024-3094)](#xz-utils_%E5%90%8E%E9%97%A8_CVE-2024-3094 "xz-utils 后门 (CVE-2024-3094) ")
  + [PHP git.php.net 入侵](#PHP_gitphpnet_%E5%85%A5%E4%BE%B5 "PHP git.php.net 入侵 ")
  + [Axios npm 供应链攻击](#Axios_npm_%E4%BE%9B%E5%BA%94%E9%93%BE%E6%94%BB%E5%87%BB "Axios npm 供应链攻击 ")
* [Git 应急排查完整命令](#Git_%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5%E5%AE%8C%E6%95%B4%E5%91%BD%E4%BB%A4 "Git 应急排查完整命令")
  + [保留现场](#%E4%BF%9D%E7%95%99%E7%8E%B0%E5%9C%BA "保留现场")
  + [梳理提交时间线](#%E6%A2%B3%E7%90%86%E6%8F%90%E4%BA%A4%E6%97%B6%E9%97%B4%E7%BA%BF "梳理提交时间线")
    - [按时间范围过滤提交](#%E6%8C%89%E6%97%B6%E9%97%B4%E8%8C%83%E5%9B%B4%E8%BF%87%E6%BB%A4%E6%8F%90%E4%BA%A4 "按时间范围过滤提交")
    - [按作者过滤](#%E6%8C%89%E4%BD%9C%E8%80%85%E8%BF%87%E6%BB%A4 "按作者过滤")
    - [按文件路径过滤](#%E6%8C%89%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E8%BF%87%E6%BB%A4 "按文件路径过滤")
    - [搜索提交内容](#%E6%90%9C%E7%B4%A2%E6%8F%90%E4%BA%A4%E5%86%85%E5%AE%B9 "搜索提交内容")
  + [分析具体 commit](#%E5%88%86%E6%9E%90%E5%85%B7%E4%BD%93_commit "分析具体 commit")
  + [追溯代码归属](#%E8%BF%BD%E6%BA%AF%E4%BB%A3%E7%A0%81%E5%BD%92%E5%B1%9E "追溯代码归属")
  + [恢复被删除/隐藏的历史](#%E6%81%A2%E5%A4%8D%E8%A2%AB%E5%88%A0%E9%99%A4%E9%9A%90%E8%97%8F%E7%9A%84%E5%8E%86%E5%8F%B2 "恢复被删除/隐藏的历史")
    - [Reflog 分析](#Reflog_%E5%88%86%E6%9E%90 "Reflog 分析")
    - [查找悬空对象](#%E6%9F%A5%E6%89%BE%E6%82%AC%E7%A9%BA%E5%AF%B9%E8%B1%A1 "查找悬空对象")
    - [直接检查 Git 对象](#%E7%9B%B4%E6%8E%A5%E6%A3%80%E6%9F%A5_Git_%E5%AF%B9%E8%B1%A1 "直接检查 Git 对象")
  + [检查 Git Hooks（持久化后门）](#%E6%A3%80%E6%9F%A5_Git_Hooks%EF%BC%88%E6%8C%81%E4%B9%85%E5%8C%96%E5%90%8E%E9%97%A8%EF%BC%89 "检查 Git Hooks（持久化后门）")
  + [检查 Git 配置](#%E6%A3%80%E6%9F%A5_Git_%E9%85%8D%E7%BD%AE "检查 Git 配置")
  + [验证提交签名](#%E9%AA%8C%E8%AF%81%E6%8F%90%E4%BA%A4%E7%AD%BE%E5%90%8D "验证提交签名")
  + [检查敏感信息泄露](#%E6%A3%80%E6%9F%A5%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2 "检查敏感信息泄露")
  + [平台审计日志](#%E5%B9%B3%E5%8F%B0%E5%AE%A1%E8%AE%A1%E6%97%A5%E5%BF%97 "平台审计日志")
    - [GitHub](#GitHub "GitHub")
    - [GitLab](#GitLab "GitLab")
* [SVN 应急排查](#SVN_%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5 "SVN 应急排查")
  + [客户端排查](#%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%8E%92%E6%9F%A5 "客户端排查")
  + [服务端排查](#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%8E%92%E6%9F%A5 "服务端排查")
  + [SVN 批量日志分析脚本](#SVN_%E6%89%B9%E9%87%8F%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E8%84%9A%E6%9C%AC "SVN 批量日志分析脚本")
* [自动化扫描工具](#%E8%87%AA%E5%8A%A8%E5%8C%96%E6%89%AB%E6%8F%8F%E5%B7%A5%E5%85%B7 "自动化扫描工具")
  + [TruffleHog 凭据泄露扫描](#TruffleHog_%E5%87%AD%E6%8D%AE%E6%B3%84%E9%9C%B2%E6%89%AB%E6%8F%8F "TruffleHog 凭据泄露扫描")
  + [Gitleaks 密钥/凭据检测](#Gitleaks_%E5%AF%86%E9%92%A5%E5%87%AD%E6%8D%AE%E6%A3%80%E6%B5%8B "Gitleaks 密钥/凭据检测")
  + [git-secrets (AWS 官方工具)](#git-secrets_AWS_%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7 "git-secrets (AWS 官方工具)")
  + [detect-secrets (Yelp)](#detect-secrets_Yelp "detect-secrets (Yelp)")
* [应急响应 SOP](#%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94_SOP "应急响应 SOP")
  + [遏制](#%E9%81%8F%E5%88%B6 "遏制 ")
  + [排查](#%E6%8E%92%E6%9F%A5 "排查 ")
  + [影响评估](#%E5%BD%B1%E5%93%8D%E8%AF%84%E4%BC%B0 "影响评估 ")
  + [修复](#%E4%BF%AE%E5%A4%8D "修复 ")
  + [加固](#%E5%8A%A0%E5%9B%BA "加固 ")
* [一键排查脚本](#%E4%B8%80%E9%94%AE%E6%8E%92%E6%9F%A5%E8%84%9A%E6%9C%AC "一键排查脚本")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## 为什么要关注版本控制系统安全

过去几年，供应链攻击已经从”理论威胁”变成了”每季度都在发生的事”。攻击者不再只盯着运行中的服务器，而是把手伸向了更上游的地方——代码仓库。一次成功的代码投毒，影响面可以是数百万台机器。这篇文章不讲理论框架，只讲**拿到一个可能被污染的仓库后，怎么一步步把事情查清楚**。所有命令都是我在实际应急中用过的，拿来就能跑。

## 代码仓库投毒真实案例

在讲排查方法之前，先看看这些年都出过什么事。了解攻击者的手法，才能知道排查时该重点看什么。

### xz-utils 后门 (CVE-2024-3094)

**时间线：** 2021年11月 ~ 2024年3月

这个案例之所以震惊整个安全圈，是因为攻击者花了**两年半**来布局。

攻击者 “Jia Tan” 从 2021 年开始以正常贡献者身份参与 xz-utils 项目，提交了大量合法代码。与此同时，多个马甲账号（Jigar Kumar、Dennis Ens 等）在邮件列表上不断给原始维护者 Lasse Collin 施压，抱怨项目维护速度慢，要求增加新的 co-maintainer。Lasse Collin 最终将维护权交给了 Jia Tan。拿到权限后，Jia Tan 在测试用的二进制文件中藏入了后门代码。

**关键点：这些恶意代码只出现在发布的 tarball 中，不在 GitHub 仓库里**。这意味着看 GitHub 上的源码根本发现不了。后门劫持了 OpenSSH 的 `RSA_public_decrypt` 函数，持有特定 Ed448 私钥的攻击者可以在任何受影响的机器上执行任意命令。

**发现方式：** 微软工程师 Andres Freund 在调试 Debian 预发布系统时注意到 SSH 登录变慢了 500ms，顺藤摸瓜查到了 liblzma。

### PHP git.php.net 入侵

**时间线：** 2021年3月28日

攻击者利用 master.php.net 泄露的凭据，通过 HTTPS + 密码认证直接向 php-src 仓库推送了两个恶意 commit，伪装成 Rasmus Lerdorf（PHP 之父）和 Nikita Popov 的提交。

commit message 写的是 “Fix typo”，实际植入了一个 User-Agent 触发的后门——当 HTTP 请求的 User-Agent 以 `zerodium` 开头时，执行任意 PHP 代码。

**发现方式：** 安全研究人员在代码审查中发现了异常逻辑。

### Axios npm 供应链攻击

**时间线：** 2026年3月

朝鲜关联的攻击者通过社会工程和 RAT 木马获取了 Axios（周下载量 1 亿+）维护者的 npm 账号，绕过 GitHub Actions OIDC 发布机制，直接用长期有效的 npm token 通过 CLI 发布了含跨平台 RAT 的恶意版本。从发布到下架只有 3 小时，但很短的时间内也有大量的开发者中招。

## Git 应急排查完整命令

以下是拿到一个可疑 Git 仓库后的系统排查流程。

### 保留现场

在做任何操作之前，先把证据固定下来：

```
# 完整克隆仓库（包含所有分支、tag、reflog）
git clone --mirror <repo_url> evidence_repo.git

# 如果是本地仓库，直接打包
tar czf evidence_$(date +%Y%m%d_%H%M%S).tar.gz .git/

# 记录当前状态
git log --all --oneline > /tmp/evidence_log.txt
git reflog --all > /tmp/evidence_reflog.txt
git branch -a > /tmp/evidence_branches.txt
```

### 梳理提交时间线

#### 按时间范围过滤提交

```
# 查看事件窗口内的所有提交
git log --all --oneline --since="2024-04-01" --until="2024-04-15" \
  --format="%h | %an <%ae> | %ad | %s" --date=format:"%Y-%m-%d %H:%M:%S"

# 按时间排序，看凌晨是否有异常提交
git log --all --format="%ad | %an | %h | %s" --date=format:"%H:%M" \
  --since="2024-04-01" | sort
```

#### 按作者过滤

```
# 列出所有提交者及其提交数
git shortlog -s -n -e --all

# 查看特定作者的所有提交
git log --all --author="suspicious_user" --format="%H %ad %s" --date=short

# 对比 author 和 committer 是否一致（不一致可能是伪造）
git log --all --format="%H | Author: %an <%ae> | Committer: %cn <%ce> | %s" \
  | awk -F'|' '$2 != $3'
```

**重要：** Git 的 `author` 和 `committer` 字段都可以通过 `GIT_AUTHOR_NAME`、`GIT_COMMITTER_EMAIL` 等环境变量伪造。PHP 后门事件中攻击者就是这样伪装成 Rasmus Lerdorf 的。不能仅凭这些字段判断身份。

#### 按文件路径过滤

```
# 查看特定敏感文件的修改历史
git log --all --follow -- Makefile
git log --all --follow -- .github/workflows/
git log --all --follow -- scripts/
git log --all --follow -- Dockerfile

# 查看哪些 commit 修改了构建相关文件
git log --all --diff-filter=M -- "*.sh" "*.yml" "*.yaml" "Makefile" "Dockerfile"
```

#### 搜索提交内容

```
# 搜索引入了特定字符串的 commit（-S pickaxe 搜索）
git log --all -p -S "eval("
git log --all -p -S "exec("
git log --all -p -S "curl "
git log --all -p -S "wget "
git log --all -p -S "base64"
git log --all -p -S "/dev/tcp/"
git log --all -p -S "zerodium"  # PHP 后门案例中的关键字

# 正则搜索（-G 选项）
git log --all -p -G "password\s*=\s*['\"]"
git log --all -p -G "(api[_-]?key|secret|token)\s*[:=]"

# 搜索 commit message 中的可疑关键字
git log --all --grep="typo" --grep="fix" --oneline  # "Fix typo" 是常见伪装
git log --all --grep="minor" --grep="cleanup" --oneline
```

### 分析具体 commit

```
# 查看某个 commit 的完整变更
git show <commit_hash>

# 查看 commit 修改了哪些文件（不看内容）
git show --stat <commit_hash>

# 对比两个 commit 之间的差异
git diff <commit1>..<commit2>

# 查看某个文件在特定 commit 时的完整内容
git show <commit_hash>:path/to/file

# 大上下文 diff（看更多周围代码）
git diff -U20 <commit1>..<commit2> -- path/to/file
```

### 追溯代码归属

```
# 逐行追溯文件的修改者
git blame path/to/suspicious_file

# 指定行范围
git blame -L 100,120 path/to/suspicious_file

# 显示更详细的信息（包括日期）
git blam...