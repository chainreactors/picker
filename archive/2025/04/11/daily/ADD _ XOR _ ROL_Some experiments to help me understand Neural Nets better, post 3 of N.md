---
title: Some experiments to help me understand Neural Nets better, post 3 of N
url: http://addxorrol.blogspot.com/2025/04/some-experiments-to-help-me-understand_10.html
source: ADD / XOR / ROL
date: 2025-04-11
fetch_date: 2025-10-06T22:04:14.567099
---

# Some experiments to help me understand Neural Nets better, post 3 of N

# [ADD / XOR / ROL](http://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Thursday, April 10, 2025

### Some experiments to help me understand Neural Nets better, post 3 of N

What is this? After my first post on the topic, 9 months elapsed before I posted again, and now I am posting within days of the last post?

Anyhow, [after my last](https://addxorrol.blogspot.com/2025/04/some-experiments-to-help-me-understand.html) post I could not resist and started running some experiments trying to see whether I could induce "overfitting" in the neural networks I had been training - trying to get a heavily overparametrized neural network to just "memorize" the training points so it generalizes poorly.

In the experiments I ran in previous posts, one of the key advantages is that I know the "true distribution" from which we are drawing our training data -- the input image. An overfit network would hence find ways to color the points in the training data correctly, but somehow not do so by drawing a black ring on white background (so it would be correct on the training data but fail to generalize).

So the experiment I kicked off was the following: Start with a network that has many times more parameters than we have training points: Since we start with 5000 training points, I picked 30 layers of 30 neurons for a total parameter count of approximately 27000 parameters. If von Neumann said he can draw an elephant with 4 parameters and make it wriggle it's trunk with 5, he'd certainly manage to fit 5000 training points with 27000 parameters?

Anyhow, to my great surprise, there was no hint of overfitting:

The network very clearly learns to draw a circle instead of fitting individual points. That is somewhat surprising, but perhaps this is just an artifact of our training points being relatively "dense" in the space, 5000 training points out of 1024\*1024 is still 0.4%, that's a good chunk of the total space.

As a next step, I trained the same network, but with ever-reduced quantities of training data: 2500 points, 1250 points, 625 points, and 312 points. Surely training on 312 data points using 27000 parameters should generate clear signs of overfitting?

At 2500 points, while there is a noticeable slowdown in the training process, the underlying concept seems to be learnt just fine:
As we drop much lower, to 625 points, we can see how the network is struggling much more to learn the concept, but ... it still seems to have a strong bias toward creating a geometric shape resembling the ring instead of overfitting on individual points?

It appears that the learning process is slowed down - by epoch 6000 the network hasn't managed to reproduce the entire circle yet - and training seems to be less stable - but it looks as if the network is moving into the right direction. What happens if we halve the training points once more?

It's a bit of a mystery - I would have expected that by now we're clearly in a regime where the network should try fit individual points, we gave it just 0.02% of the points in the space. The network is clearly struggling to learn, and by epoch 6000 it is far from "ready" -- but it's certainly working towards a ring shape.

These experiments raise a number of questions for me:

1. It seems clear to me that the networks have some form of baked-in tendency to form contiguous areas - perhaps even a geometric shape - and the data needs to become very very sparse in order for true overfitting to occur. It's really unclear to me why we see the emergence of shapes here -- it would certainly be easy for the network to just pick the 312 polytopes in which the training points reside, and their immediate neighbors, and then have a steep linear function with big parameters to color just the individual dots black. But that's not what is happening here; there's some mechanism or process that leads to the emergence of a shape.

2. It almost seems like there is a trade-off -- if you have less data, you need to train longer, perhaps much longer. But it's really not clear to me that we will not arrive at comparatively good approximations even with 312 data points.

As a next step, I am re-running these experiments with 20000 epochs instead of 6000, to see if the network trained on very sparse training data catches up with the networks that have more data over time.

Posted by

[halvar.flake](https://www.blogger.com/profile/12486016980670992738 "author profile")

at
[12:36 AM](http://addxorrol.blogspot.com/2025/04/some-experiments-to-help-me-understand_10.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=14114712&postID=6608347225856704535&from=pencil "Edit Post")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/14114712/6608347225856704535)

[Newer Post](http://addxorrol.blogspot.com/2025/05/some-experiments-to-help-me-understand.html "Newer Post")

[Older Post](http://addxorrol.blogspot.com/2025/04/some-experiments-to-help-me-understand.html "Older Post")
[Home](http://addxorrol.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://addxorrol.blogspot.com/feeds/6608347225856704535/comments/default)

## Blog Archive

* ▼
  [2025](http://addxorrol.blogspot.com/2025/)
  (6)
  + ►
    [July](http://addxorrol.blogspot.com/2025/07/)
    (2)
  + ►
    [May](http://addxorrol.blogspot.com/2025/05/)
    (1)
  + ▼
    [April](http://addxorrol.blogspot.com/2025/04/)
    (2)
    - [Some experiments to help me understand Neural Nets...](http://addxorrol.blogspot.com/2025/04/some-experiments-to-help-me-understand_10.html)
    - [Some experiments to help me understand Neural Nets...](http://addxorrol.blogspot.com/2025/04/some-experiments-to-help-me-understand.html)
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
 ...