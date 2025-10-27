---
title: 轻量级代码审计工具: Semgrep
url: https://buaq.net/go-172081.html
source: unSafe.sh - 不安全
date: 2023-07-15
fetch_date: 2025-10-04T11:51:32.645569
---

# 轻量级代码审计工具: Semgrep

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

![](https://8aqnet.cdn.bcebos.com/fd3d3ac1f58d26f6c7368c3f72b3956c.jpg)

轻量级代码审计工具: Semgrep

什么是 Semgrep？Semgrep 是一个开源的静态代码分析工具，旨在帮助开发人员和安全专家发现和修复软件代码中的安全漏洞、代码质量问题和最佳实践违规等。Se
*2023-7-14 17:6:0
Author: [xz.aliyun.com(查看原文)](/jump-172081.htm)
阅读量:62
收藏*

---

什么是 Semgrep？

> Semgrep 是一个开源的静态代码分析工具，旨在帮助开发人员和安全专家发现和修复软件代码中的安全漏洞、代码质量问题和最佳实践违规等。Semgrep 支持多种编程语言，包括但不限于 Python、JavaScript、Go、Java、PHP 等。
>
> 以下是 Semgrep 的一些主要特点和优势：
>
> 1. **易于使用**: Semgrep 的语法简单直观，使用 YAML 或者纯文本格式的规则定义，使得规则编写和理解变得容易。您可以根据特定的需求编写自定义规则，或者使用社区维护的规则库。
> 2. **快速扫描**: Semgrep 使用高效的静态分析算法，能够在大型代码库中进行快速扫描。它具有可扩展性，适用于小型项目和大型企业应用程序。
> 3. **广泛的规则库**: Semgrep 提供了一个丰富的规则库，涵盖了安全漏洞、常见的代码错误、最佳实践和性能问题等多个方面。您可以直接使用这些规则，也可以根据自己的需求进行定制和扩展。
> 4. **多语言支持**: Semgrep 支持多种流行的编程语言，如 Python、JavaScript、Go、Java 等。这使得它成为跨多个技术栈的团队或项目的理想选择。
> 5. **集成和扩展性**: Semgrep 可以与各种 CI/CD 工具和代码编辑器集成，例如 GitLab、GitHub Actions、Jenkins 等。此外，Semgrep 还提供了 API 和 CLI 接口，使您能够轻松集成到现有的工作流程中。
> 6. **可定制性**: Semgrep 允许您根据自己的需求创建自定义规则。您可以使用 Semgrep 提供的丰富的模式匹配语法来编写适合特定代码风格和规范的规则。
> 7. **活跃的社区**: Semgrep 拥有活跃的开源社区支持，社区维护了大量的规则库，并定期更新和改进 Semgrep 的功能和性能。

以上介绍来自于 ChatGPT :heart\_eyes:，本文的主要目的是讲解 Semgrep 使用方法以及注意事项。

Semgrep 的官方文档提供了详细的安装教程 。可参考 [Semgrep Privacy Policy - Semgrep](https://semgrep.dev/docs/getting-started/)

安装 semgrep

```
python3 -m pip install semgrep
semgrep --version
```

更新 semgrep

```
python3 -m pip install --upgrade semgrep
```

Semgrep 的语法非常简单，把官方的教程过一遍就可以入门了，学习成本比 CodeQL 要小很多。

* [Learn - Semgrep](https://semgrep.dev/learn)

## 在终端使用

使用 semgrep 命令行操作时，可以通过 --help 查看 semgrep 支持的功能。

```
└─$ semgrep --help
Usage: semgrep [OPTIONS] COMMAND [ARGS]...

  To get started quickly, run `semgrep scan --config auto`

  Run `semgrep SUBCOMMAND --help` for more information on each subcommand

  If no subcommand is passed, will run `scan` subcommand by default

Options:
  -h, --help  Show this message and exit.

Commands:
  ci                   The recommended way to run semgrep in CI
  install-semgrep-pro  Install the Semgrep Pro Engine
  login                Obtain and save credentials for semgrep.dev
  logout               Remove locally stored credentials to semgrep.dev
  lsp                  [EXPERIMENTAL] Start the Semgrep LSP server
  publish              Upload rule to semgrep.dev
  scan                 Run semgrep rules on files
  shouldafound         Report a false negative in this project.
```

每一种模式对应不同的功能，其中最重要的是 scan 功能，用于扫描指定的源码，其他功能会在后续进行介绍。

```
└─$ semgrep scan --help
Usage: semgrep scan [OPTIONS] [TARGETS]...

  Run semgrep rules on files

  Searches TARGET paths for matches to rules or patterns. Defaults to searching entire
  current working directory.

  To get started quickly, run

      semgrep --config auto .

  This will automatically fetch rules for your project from the Semgrep Registry. NOTE:
  Using `--config auto` will log in to the Semgrep Registry with your project URL.

  For more information about Semgrep, go to https://semgrep.dev.

  NOTE: By default, Semgrep will report pseudonymous usage metrics to its server if you
  pull your configuration from the Semgrep registry. To learn more about how and why
  these metrics are collected, please see https://semgrep.dev/docs/metrics. To modify
  this behavior, see the --metrics option below.

Options:
  --replacement TEXT              An autofix expression that will be applied to any
                                  matches found with --pattern. Only valid with a
                                  command-line specified pattern.
...
```

### 使用官方规则库（Registry）进行扫描

官方维护了一个规则库（Registry）以便用户提交、查找以及选择特定的规则去扫描项目：[Explore - Semgrep](https://semgrep.dev/explore)。其中包含了社区规则以及专业规则（Pro），社区规则存储在 github 仓库中 [returntocorp/semgrep-rules: Semgrep rules registry](https://github.com/returntocorp/semgrep-rules)。

Registry，根据常见的扫描需求，定制了一些扫描集合，例如 OWASP-TOP-10、CWE-TOP-25 等。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170224-26776598-2225-1.png)

或是根据语言进行分类：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170237-2e115656-2225-1.png)

假如我们需要扫描 PHP，可以在 Registry 中进行搜索，查找结果包括 PHP 相关的规则集合，以及其中的所有规则：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170245-32ff718e-2225-1.png)

可以看到官方为 PHP 归纳了三个规则集合，分别是 php、php-laravel、phpcs-security-audit。

```
└─$ semgrep --config "p/phpcs-security-audit" /mnt/share/project/ctf_archives/test/baijiacms

┌─────────────┐
│ Scan Status │
└─────────────┘
  Scanning 2787 files tracked by git with 10 Code rules:
  Scanning 748 files with 10 php rules.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:03

┌──────────────────┐
│ 89 Code Findings │
└──────────────────┘

    /mnt/share/project/ctf_archives/test/baijiacms/includes/baijiacms/common.inc.php
       php.lang.security.exec-use.exec-use
          Executing non-constant commands. This can lead to command injection.
          Details: https://sg.run/5Q1j

          654┆ system('convert'.$quality_command.' '.$file_full_path.' '.$file_full_path);
            ⋮┆----------------------------------------
       php.lang.security.weak-crypto.weak-crypto
          Detected usage of weak crypto function. Consider using stronger alternatives.
          Details: https://sg.run/KlBn

          372┆ $seed = base_convert(md5(microtime() . $_SERVER['DOCUMENT_ROOT']), 16, $numeric ? 10 : 35);
            ⋮┆----------------------------------------
         1049┆ $package['sign'] = strtoupper(md5($string1));
...
┌──────────────┐
│ Scan Summary │
└──────────────┘
Some files were skipped or only partially analyzed.
  Partially scanned: 2 files only partially analyzed due to parsing or internal Semgrep errors

Ran 10 rules on 748 files: 89 findings.

A new version of Semgrep is available. See https://semgrep.dev/docs/upgrading
```

### 使用本地规则库进行扫描

离线使用时，可以将 semgrep 官方维护的社区规则库下载到本地，使用 `--config` 参数指定规则库的路径进行扫描。

```
└─$ semgrep --config /mnt/share/Tools/web/code_audit/semgrep-rules/php /mnt/share/project/ctf_archives/test/baijiacms

┌─────────────┐
│ Scan Status │
└─────────────┘
  Scanning 2788 files tracked by git with 57 Code rules:
  Scanning 748 files with 40 php rules.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:12

┌──────────────┐
│ Scan Summary │
└──────────────┘
Some files were skipped or only partially analyzed.
  Partially scanned: 2 files only partially analyzed due to parsing or internal Semgrep errors
  Scan skipped: 5 files larger than 1.0 MB, 195 files matching .semgrepignore patterns
  For a full list of skipped files, run semgrep with the --verbose flag.

Ran 57 rules on 748 files: 257 findings.

A new version of Semgrep is available. See https://semgrep.dev/docs/upgrading
```

semgrep 提供了 -o 参数可以输出到文件，但无论是否加不加 `--force-color / --no-force-color` 参数，输出到文件中的内容都会带上颜色字符，导致在文件中查看并不方便，确实有点坑，但借助 sed 可以消除这些字符。

```
semgrep scan --config /mnt/share/Tools/web/code_audit/semgrep-rules/php /mnt/share/project/ctf_archives/test/baijiacms --no-force-color  --dataflow-traces | sed 's/\x1B\[[0-9;]*[mK]//g' > result.txt
```

## 在 vscode 中使用

vscode 中的 semgrep 插件主要用于配置规则文件路径、排除文件等，配置项如下：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170300-3b865af2-2225-1.png)

其中 configuration 可以配置规则文件路径用于离线场景下的扫描，如果没有指定， semgrep 会从官方社区获取规则文件内容。

配置完后，vscode 会根据配置规则自动扫描当前 workspace，扫描结果会直接显示在 vscode 的 problem 窗口中，为了方便观察漏洞类型，可以切换树视图。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170313-43754854-2225-1.png)

树视图下的第一列显示了匹配的规则名：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170347-57eba42c-2225-1.png)

如果同时安装了对应语言的插件，Problem 窗口也会出现其他的错误信息，此时可以通过关键词过滤出 semgrep 条目。

## 在 Semgrep Cloud Platform (SCP) 中使用

Semgrep 云平台提供了所有 semgrep 的支持，其良好的查询以及结果展示功能是终端以及 vscode 插件所不具备的，缺点在于必须在线使用。

![](http...