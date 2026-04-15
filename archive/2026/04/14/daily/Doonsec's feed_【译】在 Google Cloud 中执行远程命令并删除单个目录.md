---
title: 【译】在 Google Cloud 中执行远程命令并删除单个目录
url: https://mp.weixin.qq.com/s/6-c6LJhsxrpYRzq08LtuLg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:40:11.459790
---

# 【译】在 Google Cloud 中执行远程命令并删除单个目录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibzdnXlkbJFJSVtss52qTSUNab9o21ic6IAkVzDyMqFia3Ln986uTrBnCyyia2vneo4txJdAicETKAuEpia8VOyicKq9uBsDWLLlBVv5A/0?wx_fmt=jpeg)

# 【译】在 Google Cloud 中执行远程命令并删除单个目录

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

在测试一个私有漏洞赏金计划时，我遇到了一个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZiby7ZIibOytgozMofbP77WNK6Jj4R1seOgDPVw193IibmT06MvTYJDsa94QysI0AsnUGNgMJialPAR7HhDIwqbvg2QdSde7MRSmSB4/640?wx_fmt=png&from=appmsg)

## **介绍**

你好，我是 **RyotaK** （ **@ryotkak）** ），GMO Flatt Security Inc. 的一名安全工程师。

前段时间，我参加了**谷歌云 VRP 漏洞测试活动，** 由谷歌组织的现场黑客活动。

在此次事件中，我发现谷歌云的某项服务存在远程命令执行漏洞。由于该漏洞现已修复，我想在本文中分享其技术细节。

## **太长不看**

Google Cloud 有一款名为 Looker 的产品，该产品具有管理 Git 存储库的功能。

当用户删除目录时，Looker 对目标目录的验证存在缺陷，导致可能误删包含代码仓库本身的目录。由于其他 Git 操作可以同时执行，因此在删除目录的过程中也可能触发其他 Git 相关操作。

利用这种竞争条件，攻击者可以在 Looker 服务器上执行任意命令。

虽然使用 Kubernetes 将实例隔离，但 Looker 服务帐户权限中的错误配置可能会允许权限提升，从而访问同一 Kubernetes 集群中的其他实例。

在向谷歌报告漏洞后，他们修复了远程命令执行漏洞和权限提升漏洞。

## **关于 Looker**

Looker 是 Google Cloud 旗下的一款商业智能 (BI) 和数据分析平台。它通过交互式仪表板和报告，帮助企业探索、分析和可视化数据。Looker 可连接到各种数据源，使用户能够创建自定义数据模型并执行分析。

Looker 有两种部署方式：云托管和自托管。由于我能获得用于 Google Cloud VRP bugSWAT 活动的自托管 Looker 实例，所以我专注于对自托管 Looker 进行逆向工程。

## **技术细节**

### **Looker 中的 Git 集成**

Looker 提供了一项名为 LookML 的功能，用于管理 Git 仓库（Looker 称之为项目）中的模型文件。用户可以向 Git 仓库推送或拉取更改，Looker 会自动应用这些更改。

为了与外部 Git 服务集成，Looker 通常使用 JGit 库（Git 的纯 Java 实现）。但是，当远程 Git 仓库通过 SSH 配置时，Looker 会使用原生的 Git 命令行工具，而不是 JGit。

它会在 Looker 服务器上的特定目录下创建检出的存储库，并针对该目录执行 Git 命令。

```
      def self._cli_git_command(working_directory, command_words)
        [...]
              command_with_dir = "cd #{working_directory} && #{command}"
              Looker::Log.log_block_latency(:git, "_cli_git_command: command: #{command_with_dir}") do
                Open3.capture3(command_with_dir)
              end
        [...]
```

除了标准的 Git 操作外，Looker 还提供了一个通过 Web 用户界面管理文件的功能。用户可以通过 Looker 界面创建、编辑和删除文件或目录。

### **目录删除中的验证不当**

当用户删除目录时，Looker 会执行以下代码：

```
    post("/api/internal/projects/:project_id/delete_dir") do |_project_id|
      [...]
        dir_path_array = body["dir_path_array"]
        @project.delete_dir(dir_path_array)
      [...]
```

```
      def delete_dir(dir_path_array)
        dir_name = dir_path_array.reject(&:empty?).join("/")
        dir_name = validate_dir_name(dir_name)
        dir_path = File.join(path, dir_name)
        [...]
        FileUtils.rm_rf(dir_path)
```

**`validate_dir_name`** 方法确保保留目录不会被篡改：

```
      def validate_dir_name(dir_name)
        [...]
        if path_array.include?(Looker::Model::Project::DOT_GIT)
          raise(InvalidFileNameError.new("New path cannot include .git"))
        else
          nil
        end
        File.join(path_array.map do |s|
          Looker::Utils.sanitize_file_or_dir_name(s)
          HellToolJava
        end)
      end
```

由于如果 **`.git`** 目录损坏或被删除，可能会欺骗 Git 使用伪造的 Git 配置，因此 **`validate_dir_name`** 方法会检查要删除的目录是否包含 **`.git`** ，如果包含，则会引发错误。

例如，考虑一个具有以下结构的存储库：

```
--- .git directory (Can't be controlled by the user) ---
.git/
    HEAD
    config
...
--- worktree (Controllable by the user) ---
HEAD
config
objects/
refs/
```

如果 **`.git`** 目录被删除，则针对此存储库执行的下一个 Git 命令将找不到 **`.git`** 目录，并将在工作树目录中查找 Git 配置。

因此，如果工作树包含类似于 **`.git`** 目录内容的文件，则 Git 命令将使用这些配置。

![A diagram showing how Git recognize the worktree directory as the .git directory when the actual .git directory is deleted](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibxFeuPKlNFyqWcUnEwt7DTtgYVcTKZribh6Ddics2DTXwCf5xLI748AMFfcwuZcuYN2IUdmCXTld43GjnsdI3PZMzuS2z5ic4NCWo/640?wx_fmt=png&from=appmsg)

A diagram showing how Git recognize the worktree directory as the .git directory when the actual .git directory is deleted

例如，如果将以下配置作为 **`config`** 文件放置在工作树中，并且删除了 **`.git`** 目录，则在运行 **`git status`** 或类似命令时，将触发 **`fsmonitor`** 钩子并执行 **`whoami`** 命令：

```
[core]
        bare = false
        worktree = "."
        fsmonitor = "whoami"
```

让我们回到 **`validate_dir_name`** 方法。它会正确检查要删除的目录是否包含 **`.git`** ：

```
      def validate_dir_name(dir_name)
        [...]
        if path_array.include?(Looker::Model::Project::DOT_GIT)
          raise(InvalidFileNameError.new("New path cannot include .git"))
        else
          nil
        end
        File.join(path_array.map do |s|
          Looker::Utils.sanitize_file_or_dir_name(s)
          HellToolJava
        end)
      end
```

但是，此检查无法捕获 **`dir_name`** 为 **`/`** 情况。

**`validate_dir_name`** 方法返回后， **`delete_dir`** 方法通过连接基本路径和 **`dir_name`** 来构建要删除的完整路径：

```
      def delete_dir(dir_path_array)
        dir_name = dir_path_array.reject(&:empty?).join("/")
        dir_name = validate_dir_name(dir_name)
        dir_path = File.join(path, dir_name)
        [...]
        FileUtils.rm_rf(dir_path)
```

因此，将 **`dir_path_array`** 指定为 **`["/"]`** 会导致 **`dir_name`** 为 **`/`** ，而要删除的完整路径则变为存储库目录本身。

也就是说，即使攻击者能够删除整个代码库目录，上述攻击也需要工作树中存在伪造的 Git 配置文件。这意味着如果整个代码库被删除，攻击就无法进行。

……或者并非如此？

### **FileUtils.rm\_rf 的内部结构**

**`FileUtils.rm_rf`** 方法是 Ruby 标准库中的一个方法，它可以递归地删除文件和目录。

通过对其内部代码的追踪，可以发现以下代码：

```
  def remove_entry(path, force = false)
    Entry_.new(path).postorder_traverse do |ent|
      begin
        ent.remove
      rescue
        raise unless force
      end
    end
```

如图所示，它使用 **`Entry_.postorder_traverse`** 方法以后序遍历目录树（在处理目录本身之前处理目录的所有子目录）。

如果我们欺骗 Looker 删除存储库中包含数千个文件和子目录的目录，会发生什么？

确实，删除所有文件和目录需要相当长的时间。如果我们能在删除 **`.git`** 目录之后、整个仓库删除完成之前触发删除某个目录，我们仍然有机会对部分删除的仓库执行 Git 命令。

![A diagram showing the order of directory deletion](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibwvicZPpYFNswWQNucFCgDsiaSIice4YYYNNWC8aF3wkibzx3qPia0nUicg1GOPgXRmZ4bme0WCjQyCicfKdbJUgt5V8IhwLXCmoCwHu8/640?wx_fmt=png&from=appmsg)

A diagram showing the order of directory deletion

### **控制删除令**

**`Entry_.postorder_traverse`** 内部使用 **`Dir.children`** 方法列出目录内容，该方法使用 **`readdir`** 系统调用读取目录条目。

**dir.c 第 952 行**

```
while ((dp = READDIR(dirp->dir, dirp->enc)) != NULL) {
  const char *name = dp->d_name;
  [...]
```

由于 **`readdir`** 返回的条目顺序取决于文件系统的实现，并且可能会有所不同，因此无法保证在删除过程中处理文件和目录的顺序。

幸运的是，从攻击者的角度来看，在 ext4 文件系统上， **`readdir`** 返回的目录顺序具有一定的确定性。这使得攻击者可以通过精心命名目录来影响删除顺序。

因此，我可以通过以下方式“喷洒”目录名称，以确定哪个目录名称能够确保在删除过程中首先处理 **`.git`** 目录：

```
.git/
aaa/
aab/
    dir1/
        file1
        file2
        file3
        ...
    dir2/
        file1
        file2
        file3
        ...
    ...
    dir10000/
        ...
aac/
...
ccb/
ccc/
```

通过将许多文件和目录放在特定目录下，并测量触发删除后存储库不可用所需的时间，我可以找到最佳目录名称，以便首先删除 **`.git`** 目录，从而创建一个窗口来触发针对部分删除的存储库的 Git 操作。

### **远程命令执行**

现在我们可以控制 **`.git`** 目录删除的时间，我们可以尝试在 Looker 服务器上执行任意命令。

攻击步骤如下：

1. 创建一个包含伪造的 Git 配置的工作树的 Git 存储库，以便使用 **`fsmonitor`** 钩子执行任意命令。
2. 创建一个包含许多文件和子目录的随机名称目录，然后尝试使用 **`POST /api/internal/projects/:project_id/delete_dir`** API 删除存储库本身。
3. 测量仓库不可用所需的时间。如果时间过长，则返回步骤 2（这表明 **`.git`** 目录没有先被删除）。
4. 找到最佳目录名称后，再次准备仓库，并持续调用触发 Git 操作的端点（例如， **`git status`** ）。在我的测试中，每秒 1 次请求就足够了。
5. 调用 **`POST /api/internal/projects/:project_id/delete_dir`** API 删除仓库目录。这将首先删除 **`.git`** 目录，但完成整个大型目录的删除需要一些时间。
6. 此时，步骤 4 中触发的 Git 操作将尝试使用部分删除的存储库，导致使用工作树中的 Git 配置并执行任意命令。

我使用以下 Git 配置来测试命令执行：

```
[core]
        bare = false
        worktree = "."
        fsmonitor = "echo \"$(whoami) $(uname -a)\" > ../output/pwned.model.lkml"
```

在删除仓库期间执行 **`git status`** 后，会执行 **`whoami`** 和 **`uname -a`** 命令，并将输出写入 **`../output/pwned.model.lkml`** ，这是我可以正常访问的另一个仓库。

![The Looker Web UI showing the result of whoami and uname -a commands](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibx5CiaueJ7ML68UOrmjJichh4t1lOvxEYLp7MdxHBYd2v9dHqicvOwm7u8zcqq6jEtymLicLxoTo7axbKb4GsxIQnqPmoYIGUQHb58/640?wx_fmt=png&from=appmsg)

The Looker Web UI showing the result of whoami and uname -a commands

### **对其他 Looker 实例的权限提升**

此时，我询问 Google Cloud 团队是否可以进一步调查该漏洞的影响，他们欣然批准了。

在获得 Looker 实例的反向 shell 后不久，我注意到该实例被隔离在 Kubernetes pod 中，从而限制了对其他 Looker 实例的影响。

然而，在检查挂载在 **`/var/run/secrets/kubernetes.io/serviceaccount`** 的 Kubernetes 服务帐户凭据时，我发现权限过多：

```
{
  "kind": "SelfSubjectAccessReview",
"apiVersion": "authorization.k8s.io/v1"...