---
title: 给面试官一点小小的 gpt 震撼
url: http://xargin.com/the-death-of-baguwen/
source: No Headback
date: 2023-03-27
fetch_date: 2025-10-04T10:45:44.725822
---

# 给面试官一点小小的 gpt 震撼

[No Headback](http://xargin.com)

* [Home](http://xargin.com/)
* [Readings](http://xargin.com/readings/)
* [WeChat](http://xargin.com/wechat/)
* [Github](http://github.com/cch123)
* [Friends](http://xargin.com/friends/)

# 给面试官一点小小的 gpt 震撼

Mar 26, 2023

4 min read

ai 工具最近越来越越火了，在公司内给同事们简单做了个分享，有同事已经觉得可能晚上要睡不着觉了 orz。

技术和工具日新月异，最近每一周感觉技术世界都在发生巨变，而还在那些传统岗位上的我们的工作，半年后，一年后，两年后，又有多少价值呢？

虽然有些写代码的程序员还在嘴硬，坚持自己所做的事情做到“资深”，就不会被 ai 取代，可能还是太高估这个行业大多数人日常工作的含金量了。我个人认为不出两年，it 行业就会发生巨变。后面还会有具体的分享。

从目前很多“大佬”的动作来看，大家都想在这一波浪潮中不落于人后，加入 aigc 创业的大军中去，不管他们的目的是沽名钓誉，还是真的想做点事情推动人类的生产力进步，还是要祝福他们。

周末闲来无事，在曾经一个 Go 圈子里专攻面试的群里看到有人分享了这么个案例：

![](http://xargin.com/content/images/2023/03/141679828185_.pic.jpg)

嗯，放在两周前看到我会比较震撼。

放在现在嘛，我动了动歪脑筋，既然 chatgpt 可以生成面试题，那么 chatgpt 自然也就可以生成面试题的答案。在 ai 浪潮的冲击下，我们传统的面试可以轻易被颠覆。具体要怎么实现呢？

我们先来看一个案例：

[Samantha.x64

The first Web3 bot creator platform, Join DC and follow up to get whitelisted: https://discord.gg/RnqnZzNmBE

![](https://telegram.org/img/apple-touch-icon.png)Telegram

![](https://cdn5.telegram-cdn.org/file/HVkLkP4lAlPmV7-JNqmJfJ3GCiuJnw3PsZkQkgfEgri6GHPJLzpD6oCuIACWGwM8Ehce0rYcyJuNEBjF3b6A4rNxGgo6rok8nwPzVMVvtg7F0rIX7XDlHKqeyBHklPLAeexzv_brDqQvySj3GQw0OhIc7gQC8m3SeuWTqJGIH0xk_3o4dd8M5iV3Cj-KN2BawxJLU9AS0traDlYsCfFzc14WnvV3pkCMSXcijcsgjrtzozkoczyCMRuqz1SFwnuaeYdIaz1__eD6KWW61JaBI0py9a9ZH9zo3_UsamwFbZCvo_r1ZjHz6Ds-YkkxG0YjuZ6853-uKhM8zlYo09xFsw.jpg)](https://t.me/samantha_x64_bot)

上面这个是一个用 ai 技术实现的聊天机器人，可以做到识别用户语言，然后把文字发给 chatgpt，然后把 chatgpt 返回的内容用 tts 重新转回语言发给用户。

基本的功能是帮助我们来练习口语，能够避免和没什么共同话题的外教尬聊的场景。基本的技术是 speech recognition，text to speech，然后就是简单的 chatgpt 的 api。

chatgpt 的 api 自不用说，这里的 speech recognition 和 text to speech 目前也有基于机器学习的新成果。

speech recognition 使用 openai 开源的 <https://github.com/openai/whisper>，whisper 可以实现多语言的语音识别，我实际实验下来，英文的识别率还是挺准的。

然后是 text to speech，mozilla 开源的 tts 工具 <https://github.com/mozilla/tts>，效果和真人说话已经没有太大的差别了。

当然，我们只是为了给面试官一点震撼，这里 tts 还用不上。只要有 speech recognition 和 chatgpt 的接口就够了。

这意味着什么呢？意味着当**我们参加远程视频面试时，可以通过录音将面试官的问题识别为文字，并将文字发给 chatgpt 自动生成答案**。

听起来是不是有点小可怕？

我在很早之前其实也就说过，能够从互联网上检索到的知识，和那些已经被标准化的知识(比如 inf 领域的 cncf)对我们来说没有任何意义，因为使用正儿八经的技术搜索引擎对于中文区的程序员稍微有些门槛，所以我们会把那些八股文当回事，但现如今，chatgpt 这种 ai 工具让人与信息的距离进一步缩短，传统的生产关系没有跟上技术的发展，就会变成很可怕的事情。

按照前述理论，任何人都可以低门槛做出一个线上面试作弊机器人。

好好想想，面试到底该问什么问题吧。

![Xargin]()

#### Xargin

[More posts](/author/xargin/)

If you don't keep moving, you'll quickly fall behind

Beijing

[Previous Post](/winter-is-coming/)

[Next Post](/complete-deah-for-middleplatform/)

Powered by [Ghost](https://ghost.org/)

[No Headback](http://xargin.com)

![](/content/images/2021/05/wechat.png)