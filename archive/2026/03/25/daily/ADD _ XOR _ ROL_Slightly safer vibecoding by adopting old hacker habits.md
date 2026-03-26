---
title: Slightly safer vibecoding by adopting old hacker habits
url: http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html
source: ADD / XOR / ROL
date: 2026-03-25
fetch_date: 2026-03-26T04:30:19.346313
---

# Slightly safer vibecoding by adopting old hacker habits

# [ADD / XOR / ROL](http://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Tuesday, March 24, 2026

### Slightly safer vibecoding by adopting old hacker habits

I have seen a lot of public discussion around supply-chain attacks on the Python ecosystem, prompt injection risks when using coding agents, and general worries about the security implications of "vibe coding" for the development machine.

In some of these discussions I find myself puzzled as to what problem is being solved - and it took me a while to realize that my failure to understand lies in the development setup that I tend to use.

In this blog post I'll quickly explain my development setup.

The setup is pretty simple:

1. The actual development happens on a rented server (or a VM on that server).
2. In order to do development, I SSH into that server with key-forwarding for my github keys enabled.
3. I perform my development on the server by attaching to a screen or tmux session.
4. I used to just use vim with various extensions, but with the advent of coding agents I also use claude code etc. nowadays.
5. I avoid keeping secrets inside the development VM or on the development server.
6. I let the agent churn away on problems for extended periods of time while I am detached from the tmux/screen.

A setup like this reduces a large number of supply-chain attacks to - at worst - compromise the development VM.

There is still a significant risk of the github key forwarding being abused to compromise the upstream main repository.

The way around this is a bit cumbersome, but not much different from what many open-source projects already do: You keep a main repository, and you \*fork\* a development repository from it. Then you do all your development on the dev repository, and when you're done in your development branch, you issue a cross-repository pull request.

Obviously, a human needs to go through that PR with a fine comb - but this is something you want to do for insider risk etc. anyhow, so your risk profile changes only marginally.

In a setup like this, the main secret that you'll lose in a supply chain attack are your Claude credentials. And you don't need to worry about prompt injection into your coding agent too much, and can just focus on writing code.

Interestingly, the development model of "SSH into a machine and attach to a screen session" was popularized by the hacker subculture (as in "computer break-in" subculture) since historically it was never a good idea to have data on machines you physically own. SSH'ing into a random machine in a different country that law enforcement couldn't easily get access to was a reasonable way of keeping your hands clean. I mainly switched to that development model because I almost always need long-running compute and was travelling a lot, and with agent-first development the model is seeing a bit of a resurgence.

Posted by

[halvar.flake](https://www.blogger.com/profile/12486016980670992738 "author profile")

at
[9:02 PM](http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=14114712&postID=4869525190488162593&from=pencil "Edit Post")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/14114712/4869525190488162593)

[Older Post](http://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html "Older Post")
[Home](http://addxorrol.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://addxorrol.blogspot.com/feeds/4869525190488162593/comments/default)

## Blog Archive

* ▼
  [2026](http://addxorrol.blogspot.com/2026/)
  (1)
  + ▼
    [March](http://addxorrol.blogspot.com/2026/03/)
    (1)
    - [Slightly safer vibecoding by adopting old hacker h...](http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html)

* ►
  [2025](http://addxorrol.blogspot.com/2025/)
  (7)
  + ►
    [December](http://addxorrol.blogspot.com/2025/12/)
    (1)
  + ►
    [July](http://addxorrol.blogspot.com/2025/07/)
    (2)
  + ►
    [May](http://addxorrol.blogspot.com/2025/05/)
    (1)
  + ►
    [April](http://addxorrol.blogspot.com/2025/04/)
    (2)
  + ►
    [March](http://addxorrol.blogspot.com/2025/03/)
    (1)

* ►
  [2024](http://addxorrol.blogspot.com/2024/)
  (4)
  + ►
    [December](http://addxorrol.blogspot.com/2024/12/)
    (1)
  + ►
    [July](http://addxorrol.blogspot.com/2024/07/)
    (2)
  + ►
    [January](http://addxorrol.blogspot.com/2024/01/)
    (1)

* ►
  [2023](http://addxorrol.blogspot.com/2023/)
  (1)
  + ►
    [December](http://addxorrol.blogspot.com/2023/12/)
    (1)

* ►
  [2021](http://addxorrol.blogspot.com/2021/)
  (1)
  + ►
    [February](http://addxorrol.blogspot.com/2021/02/)
    (1)

* ►
  [2020](http://addxorrol.blogspot.com/2020/)
  (4)
  + ►
    [September](http://addxorrol.blogspot.com/2020/09/)
    (1)
  + ►
    [August](http://addxorrol.blogspot.com/2020/08/)
    (1)
  + ►
    [May](http://addxorrol.blogspot.com/2020/05/)
    (1)
  + ►
    [March](http://addxorrol.blogspot.com/2020/03/)
    (1)

* ►
  [2019](http://addxorrol.blogspot.com/2019/)
  (1)
  + ►
    [August](http://addxorrol.blogspot.com/2019/08/)
    (1)

* ►
  [2018](http://addxorrol.blogspot.com/2018/)
  (3)
  + ►
    [October](http://addxorrol.blogspot.com/2018/10/)
    (1)
  + ►
    [March](http://addxorrol.blogspot.com/2018/03/)
    (1)
  + ►
    [February](http://addxorrol.blogspot.com/2018/02/)
    (1)

* ►
  [2017](http://addxorrol.blogspot.com/2017/)
  (1)
  + ►
    [August](http://addxorrol.blogspot.com/2017/08/)
    (1)

* ►
  [2016](http://addxorrol.blogspot.com/2016/)
  (3)
  + ►
    [October](http://addxorrol.blogspot.com/2016/10/)
    (1)
  + ►
    [September](http://addxorrol.blogspot.com/2016/09/)
    (1)
  + ►
    [January](http://addxorrol.blogspot.com/2016/01/)
    (1)

* ►
  [2015](http://addxorrol.blogspot.com/2015/)
  (3)
  + ►
    [December](http://addxorrol.blogspot.com/2015/12/)
    (2)
  + ►
    [May](http://addxorrol.blogspot.com/2015/05/)
    (1)

* ►
  [2014](http://addxorrol.blogspot.com/2014/)
  (2)
  + ►
    [January](http://addxorrol.blogspot.com/2014/01/)
    (2)

* ►
  [2013](http://addxorrol.blogspot.com/2013/)
  (3)
  + ►
    [June](http://addxorrol.blogspot.com/2013/06/)
    (1)
  + ►
    [March](http://addxorrol.blogspot.com/2013/03/)
    (1)
  + ►
    [January](http://addxorrol.blogspot.com/2013/01/)
    (1)

* ►
  [2012](http://addxorrol.blogspot.com/2012/)
  (1)
  + ►
    [July](http://addxorrol.blogspot.com/2012/07/)
    (1)

* ►
  [2011](http://addxorrol.blogspot.com/2011/)
  (2)
  + ►
    [September](http://addxorrol.blogspot.com/2011/09/)
    (1)
  + ►
    [March](http://addxorrol.blogspot.com/2011/03/)
    (1)

* ►
  [2010](http://addxorrol.blogspot.com/2010/)
  (3)
  + ►
    [March](http://addxorrol.blogspot.com/2010/03/)
    (1)
  + ►
    [February](http://addxorrol.blogspot.com/2010/02/)
    (1)
  + ►
    [January](http://addxorrol.blogspot.com/2010/01/)
    (1)

* ►
  [2009](http://addxorrol.blogspot.com/2009/)
  (17)
  + ►
    [December](http://addxorrol.blogspot.com/2009/12/)
    (1)
  + ►
    [November](http://addxorrol.blogspot.com/2009/11/)
    (3)
  + ►
    [October](http://addxorrol.blogspot.com/2009/10/)
    (1)
  + ►
    [September](http://addxorrol.blogspot.com/2009/09/)
    (2)
  + ►
    [August](http://addxorrol.blogspot.com/2009/08/)
    (1)
  + ►
    [July](http://addxorrol.blogspot.com/2009/07/)
    (4)
  + ►
    [March](http://addxorrol.blogspot.com/2009/03/)
    (2)
  + ►
    [February](http://addxorrol.blogspot.com/2009/02/)
    (1)
  + ►
    [January](http://addxorrol.blogspot.com/2009/01/)
    (2)

* ►
  [2008](http://addxorrol.blogspot.com/2008/)
  (34)
  + ►
    [December](http://addxorrol.blogspot.com/2008/12/)
    (2)
  + ►
    [November](http://addxorrol.blogspot.com/2008/11/)
    (5)
  + ►
    [October](htt...