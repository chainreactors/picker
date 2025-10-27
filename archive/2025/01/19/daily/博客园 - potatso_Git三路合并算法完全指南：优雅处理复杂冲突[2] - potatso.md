---
title: Git三路合并算法完全指南：优雅处理复杂冲突[2] - potatso
url: https://www.cnblogs.com/potatso/p/18678518
source: 博客园 - potatso
date: 2025-01-19
fetch_date: 2025-10-06T20:04:32.896930
---

# Git三路合并算法完全指南：优雅处理复杂冲突[2] - potatso

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

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Git三路合并算法完全指南：优雅处理复杂冲突[2]](https://www.cnblogs.com/potatso/p/18678518 "发布于 2025-01-18 15:45")

在使用git作为协作工具时，常常因为不熟悉git的三路合并算法而出现冲突，导致不敢随便提交代码，这里就来为大家解释下git三路合并算法的完全指南。

# 三路合并

三路合并算法的名称源于其合并过程中涉及的三个代码版本。在标准的Git开发流程中，开发者从生产分支fork出新分支进行开发，完成开发后提交Pull Request，经过代码审查后，管理员将代码合并回生产分支。这个过程涉及三个关键版本：原始基础版本、开发分支版本和目标分支版本。如下图所示：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e5675148d43d4c21bb18771192966fd2.png#pic_center)

虽然通过diff可以清晰地看到分支间的代码差异，但Git的合并场景往往更为复杂。考虑这样一个常见场景：当生产分支新增了一个补丁A，而开发分支在合并时没有这个补丁时，Git面临一个关键的判断 —— 补丁A的缺失是开发者有意为之，还是应该保留在最终的合并结果中？正是这种复杂性，促使Git引入了"参考点"（基础版本）的概念。通过比较两个分支相对于参考点的变更，Git才能准确理解代码的增删意图，从而实现智能的自动合并。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a379db694a0246b08d4d4b079baad904.png#pic_center)

通过比较两个分支相对于参考点的变更，Git才能准确理解代码的增删意图，从而实现智能的自动合并。

在三路合并的核心机制中，Git通过比较三个关键版本来做出合并决策：两个待合并分支以及它们的共同祖先（参考点）。这就像两个作者在协同写作一本书：一个负责第一章，另一个负责第二章。共同祖先就像是初始的目录大纲，清晰地界定了每个作者的工作范围。通过对比最终内容与这份大纲的差异，我们就能准确判断每位作者的贡献，从而轻松地将两人的工作整合成完整的书稿。这正是Git三路合并算法的精妙之处。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/baad402745274d2a84c6906d94e491bc.png#pic_center)

Git在进行三路合并时，以行为基本单位进行比较。通过对比两个分支与参考点的差异，Git会按照以下规则决定最终的合并结果：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/33d1217020c8444cb33af4b637d5c564.png#pic_center)

1. **无变更保留** - 当某一行在所有版本（生产分支、开发分支、参考点）中完全相同时：

   * 直接保留该行内容
   * 不记录任何变更历史
2. **单方变更采纳** - 当某一行只在其中一个分支有修改时：

   * 保留修改后的内容
   * 记录对应的commit信息
   * 例如：生产分支修改而开发分支未变，或反之
3. **双方冲突标记** - 当某一行在两个分支都发生修改时：

   * Git无法自动判断保留哪个版本
   * 标记为冲突区域
   * 需要开发者手动解决冲突

# 递归三路合并

让我们通过一个复杂场景来理解递归三路合并的必要性。假设有以下情况：

1. 你从生产分支创建了一个开发分支A并开发新功能
2. 同时，另一个团队成员从生产分支创建了开发分支B，也在开发新功能
3. 开发分支B先完成并合并到了生产分支
4. 你在开发分支A上继续开发，但没有及时同步生产分支的更新
5. 当你完成开发并尝试合并时：
   * 如果使用简单的三路合并，Git只会看到：
     + 参考点（初始fork点）
     + 当前的生产分支（包含B的改动）
     + 你的开发分支A
   * 这样会丢失一些重要的历史信息，比如分支B是如何被合并的
   * 在复杂的代码冲突情况下，这可能导致错误的合并结果

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/77446eb9b30e44e780c6ba0fc98f2e3f.png#pic_center)

为了避免这种情况，我们通常会在开发过程中定期从生产分支拉取（pull）最新代码。这时就会发生一个有趣的现象：由于开发分支和生产分支之间发生了多次相互合并，它们之间会出现多个共同的祖先节点，而不是像简单三路合并中只有一个共同祖先（初始fork点）。这就是Git引入递归三路合并算法的原因 —— 它需要分析这些共同祖先节点，找到最佳的合并策略。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ef29c8b9efb74fb49f48d863ce7e33bd.png#pic_center)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3f8bd7dccc9f4ce29225858d738a7f28.png#pic_center)

当两个分支经过多次相互合并后，每个合并点都代表着一个重要的历史节点：在这个时刻，两个分支的代码是完全一致的。这些合并历史形成了多个共同祖先节点，它们都可以作为后续合并的潜在参考点。

Git在处理这种情况时采用了一个巧妙的方法：它会先分析所有的共同祖先节点，将它们的内容合并在一起，创建出一个虚拟的合并基准点。这个虚拟基准点综合了所有祖先节点的信息，能够更准确地反映代码的演进历史。

有了这个虚拟基准点后，Git就可以像普通的三路合并一样，将它作为参考点，与两个待合并分支进行比较，最终完成合并操作。这就是递归三路合并的核心思想。

"递归"一词准确描述了这个过程：当Git发现多个共同祖先时，它会递归地向上查找这些祖先的共同祖先，直到找到它们的最初交汇点。然后，Git会自底向上地将这些祖先逐层合并，最终创建出一个包含所有历史信息的虚拟基准点。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8e60775ba08942bd9557cafe46815df3.png#pic_center)

如上图所示，整个递归过程可以分解为以下步骤：

1. 首先，Git需要合并C8和C9两个分支，发现它们有两个共同祖先C4和C7
2. Git会向上追溯，找到C4和C7的共同祖先C1
3. 基于C1、C4和C7的内容，Git创建一个虚拟的合并基准点
4. 最后，Git使用这个虚拟基准点作为参考，对C8和C9进行三路合并

# 代码回退导致的丢代码情况

## git revert

为啥有时候`git revert`后，可能会导致一系列稀奇古怪的事情发生。讲解一下。

假设你开发的一个补丁A，被合入主线分支后，管理员发现有bug，直接使用`git revert`回退你的补丁。看过上一篇博客的朋友们都知道，`git revert`命令就是反向补丁，并重新提交一次commit。

这时候你比垂头丧气，反而继续在你自己的开发分支上把BUG修复，然后再次提交一次commit。这时候你本该先同步分支，而你却没有。让我们用一张图来说明。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a284b51a0e114dfbb79837ea8abcbfd6.png#pic_center)

根据三路合并的原理，让我们分析一下为什么会丢代码：

1. **三方版本确定**：

   * 共同祖先：补丁A合入后的版本（包含依赖代码和功能代码）
   * 主线分支：revert后的版本（补丁A的所有代码都被删除）
   * 你的分支：修复版本（只修改了功能代码，依赖代码未动）
2. **合并冲突分析**：
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/edc2a37f0f0e489a9d016a9ce1e87a3a.png#pic_center)

   * 对于功能代码：因为你修改了这部分，Git会检测到冲突（一边是删除，一边是修改），提示你解决
   * 对于依赖代码：
     + 在共同祖先中：存在
     + 在主线分支中：被删除（revert导致）
     + 在你的分支中：存在（未修改）
     + 根据三路合并规则：主线删除胜出，这部分代码会丢失
3. **问题后果**：
   当你只关注解决功能代码的冲突时，很容易忽略依赖代码的丢失。最终合入主线的代码因为缺少必要的依赖，可能会导致编译或运行失败。

# 优雅的冲突解决之道

在实际开发中，我们经常会遇到需要在多个方案中选择一个的情况。比如，两个开发者针对同一个功能提供了不同的实现方案。如果采用普通的合并方式，Git会报告冲突，要求我们手动解决。但实际上，如果我们已经确定要使用其中一个方案，Git提供了更优雅的解决方式。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3b3018423c654020ab0abd939acfe7ff.png#pic_center)

Git提供了两个特殊的合并策略来处理这种情况：

1. **ours策略**：

   ```
   git merge -s ours their-branch
   ```

   使用这个命令时，Git会在发生冲突时自动选择我们当前分支的代码。
2. **theirs策略**：

   ```
   git merge -s theirs our-branch
   ```

   相反，这个命令会在发生冲突时优先选择对方分支的代码。

这种方式特别适用于以下场景：

* 两个开发者提供了不同的实现方案，经过评审后决定采用其中一个
* 需要批量处理冲突，并且已经确定采用哪个版本
* 在代码重构时，需要统一采用新的或旧的实现方式

## 取消合并

当你在解决合并冲突的时候很烦躁，突然就想到，就不应该合并这个分支。可是这时候你已经解决一半的冲突了。这时可以使用`git merge --abort`命令取消合并。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e591de4a87ac4fc3951673129542b0e6.png#pic_center)

让我们来理解Git是如何管理合并过程的：

1. **合并状态的标识**：

   * 当Git开始合并时，会创建一个特殊的引用`MERGE_HEAD`，指向要合并的分支
   * `HEAD`继续指向当前分支
   * 这两个引用共同标识了当前的合并状态
2. **合并过程的控制**：

   * 在解决冲突时，需要使用`git add`来标记已解决的文件
   * Git会阻止在合并未完成时执行某些操作（如push/pull）
   * 这种限制确保了代码仓库的一致性
3. **取消合并的方式**：

   * `git merge --abort`：安全地回到合并前的状态
   * 这个命令会清理合并状态，删除`MERGE_HEAD`
   * 虽然也可以用`git reset`强制回退，但`--abort`更安全且符合Git的设计理念。因为在push/pull代码的过程中，git会检测这个特殊的分支是否存在来确定你是否还有未解决的冲突。如果冲突还未解决就继续加入新的代码，那岂不是乱上加乱。

# 结语

Git的合并策略是一个精心设计的系统，它不仅仅是简单的文本对比和合并。通过理解三路合并算法的原理，我们可以更好地处理复杂的合并场景，避免代码丢失的风险。而在日常开发中，合理使用Git提供的各种合并工具和命令，如`ours/theirs`策略、`merge --abort`等，能够帮助我们更优雅地解决合并冲突，提高开发效率。

记住，合并冲突不是问题的终点，而是代码协作的必经之路。掌握这些合并策略，让我们在团队协作中游刃有余。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d49a45b5a1fb4a27ba4302c069800874.png#pic_center)

posted @
2025-01-18 15:45
[potatso](https://www.cnblogs.com/potatso)
阅读(161)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025