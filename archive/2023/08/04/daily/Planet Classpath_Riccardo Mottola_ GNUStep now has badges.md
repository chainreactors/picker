---
title: Riccardo Mottola: GNUStep now has badges
url: http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html
source: Planet Classpath
date: 2023-08-04
fetch_date: 2025-10-04T12:01:51.182169
---

# Riccardo Mottola: GNUStep now has badges

# [The Art is Long](http://multixden.blogspot.com/)

The Den of Multix (aka grey gandalf)

## Thursday, August 03, 2023

### GNUStep now has badges

Finally I got around implementing and committing badge support in [GNUStep](http://www.gnustep.org)! I think it is one of the fine additions Apple did to the original OpenStep spec

While Apple had it since MacOS 10.5, GNUstep didn't and GNUMail had to manage 3 different code paths: One for GNUstep, one for 10.4 Mac and one for 10.5 and later which I implemented myself, since GNUMail originally didn't have it.
First, I with Fred and Richard brought up GNUmail code to match the 10.4 code path, which is generic and just draws the Icon. To do this, I had to change the code, since ImageReps are not writable in GNUstep, so NSCustomImageRep had to be used and it woks both on GNUstep and on Mac.

Later, proper badges support has been added in GNUstep, here the look with [GNUMail](https://www.nongnu.org/gnustep-nonfsf/gnumail/) and with a small test application, which is ported directly from Mac and compiled using xcode [buildtool](https://github.com/gnustep/libs-xcode).

![](data:image/png;base64...)

As we were tried to match certain Apple behaviours, like ellipsis, but also an addition: I made the colors themable.

Here a nice screenshot of the two things working with the *Sonne* [theme](https://gap.nongnu.org/themes/index.html). Thematic was enhanced to handle the badgeColor with its three shades matching the ring, text and badge background.

![](data:image/png;base64...)

Posted by

[Riccardo](https://draft.blogger.com/profile/03313094807656717004 "author profile")

at
[4:36 PM](http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://draft.blogger.com/post-edit.g?blogID=15746899&postID=6885664758992639615&from=pencil "Edit Post")

[Email This](https://draft.blogger.com/share-post.g?blogID=15746899&postID=6885664758992639615&target=email "Email This")[BlogThis!](https://draft.blogger.com/share-post.g?blogID=15746899&postID=6885664758992639615&target=blog "BlogThis!")[Share to X](https://draft.blogger.com/share-post.g?blogID=15746899&postID=6885664758992639615&target=twitter "Share to X")[Share to Facebook](https://draft.blogger.com/share-post.g?blogID=15746899&postID=6885664758992639615&target=facebook "Share to Facebook")[Share to Pinterest](https://draft.blogger.com/share-post.g?blogID=15746899&postID=6885664758992639615&target=pinterest "Share to Pinterest")

Labels:
[badge](http://multixden.blogspot.com/search/label/badge),
[GNUMail](http://multixden.blogspot.com/search/label/GNUMail),
[GNUstep](http://multixden.blogspot.com/search/label/GNUstep),
[icon](http://multixden.blogspot.com/search/label/icon),
[theming](http://multixden.blogspot.com/search/label/theming)

#### 4 comments:

![](//resources.blogblog.com/img/blank.gif "Makaba") Makaba said...
:   Really amazing!
    How can I test it on WindowMaker?
:   [8:47 PM](http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html?showComment=1695408478009#c3956141660909338787 "comment permalink")

    [![](https://resources.blogblog.com/img/icon_delete13.gif)](https://draft.blogger.com/comment/delete/15746899/3956141660909338787 "Delete Comment")

[![](https://resources.blogblog.com/img/blank.gif "Bryant McGill") ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKEnDbb-coqEoLSf8Tk9trfmW8JjmwofQU17qiHotu08g_MDAmetziAZNQQov_km3aBdWK56JmIGrtaoeLCr0Wcn4HLgxj0ir8xe1hT3T4MkfiEC9gN32XItGEY4EOig/s45-c/OhOpXeG9_400x400.jpg)](https://draft.blogger.com/profile/09592966722267299484) [Bryant McGill](https://draft.blogger.com/profile/09592966722267299484) said...
:   The Art IS Long.
:   [5:52 AM](http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html?showComment=1716868339717#c615252912349205283 "comment permalink")

    [![](https://resources.blogblog.com/img/icon_delete13.gif)](https://draft.blogger.com/comment/delete/15746899/615252912349205283 "Delete Comment")

[![](//resources.blogblog.com/img/blank.gif "Kayla")](https://www.kaylawallace.com/) [Kayla](https://www.kaylawallace.com/) said...
:   Hello mate great bblog post
:   [8:56 PM](http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html?showComment=1733428585735#c7779257614195345048 "comment permalink")

    [![](https://resources.blogblog.com/img/icon_delete13.gif)](https://draft.blogger.com/comment/delete/15746899/7779257614195345048 "Delete Comment")

[![](//resources.blogblog.com/img/blank.gif "Isabella")](https://www.isabellanovak.com/) [Isabella](https://www.isabellanovak.com/) said...
:   It's great that GNUstep now has proper badge support.
:   [5:55 PM](http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html?showComment=1740934557859#c3007164292463082212 "comment permalink")

    [![](https://resources.blogblog.com/img/icon_delete13.gif)](https://draft.blogger.com/comment/delete/15746899/3007164292463082212 "Delete Comment")

[Post a Comment](https://draft.blogger.com/comment/fullpage/post/15746899/6885664758992639615)

[Older Post](http://multixden.blogspot.com/2023/07/arcitcfox-421-released.html "Older Post")
[Home](http://multixden.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://multixden.blogspot.com/feeds/6885664758992639615/comments/default)

## Blog Archive

* ▼
  [2023](http://multixden.blogspot.com/2023/)
  (2)
  + ▼
    [August](http://multixden.blogspot.com/2023/08/)
    (1)
    - [GNUStep now has badges](http://multixden.blogspot.com/2023/08/gnustep-now-has-badges.html)
  + ►
    [July](http://multixden.blogspot.com/2023/07/)
    (1)

* ►
  [2021](http://multixden.blogspot.com/2021/)
  (1)
  + ►
    [April](http://multixden.blogspot.com/2021/04/)
    (1)

* ►
  [2020](http://multixden.blogspot.com/2020/)
  (4)
  + ►
    [December](http://multixden.blogspot.com/2020/12/)
    (3)
  + ►
    [October](http://multixden.blogspot.com/2020/10/)
    (1)

* ►
  [2019](http://multixden.blogspot.com/2019/)
  (3)
  + ►
    [December](http://multixden.blogspot.com/2019/12/)
    (1)
  + ►
    [February](http://multixden.blogspot.com/2019/02/)
    (2)

* ►
  [2018](http://multixden.blogspot.com/2018/)
  (8)
  + ►
    [November](http://multixden.blogspot.com/2018/11/)
    (1)
  + ►
    [September](http://multixden.blogspot.com/2018/09/)
    (1)
  + ►
    [August](http://multixden.blogspot.com/2018/08/)
    (1)
  + ►
    [July](http://multixden.blogspot.com/2018/07/)
    (2)
  + ►
    [June](http://multixden.blogspot.com/2018/06/)
    (2)
  + ►
    [March](http://multixden.blogspot.com/2018/03/)
    (1)

* ►
  [2017](http://multixden.blogspot.com/2017/)
  (4)
  + ►
    [August](http://multixden.blogspot.com/2017/08/)
    (3)
  + ►
    [April](http://multixden.blogspot.com/2017/04/)
    (1)

* ►
  [2016](http://multixden.blogspot.com/2016/)
  (4)
  + ►
    [December](http://multixden.blogspot.com/2016/12/)
    (1)
  + ►
    [June](http://multixden.blogspot.com/2016/06/)
    (1)
  + ►
    [May](http://multixden.blogspot.com/2016/05/)
    (1)
  + ►
    [March](http://multixden.blogspot.com/2016/03/)
    (1)

* ►
  [2015](http://multixden.blogspot.com/2015/)
  (9)
  + ►
    [September](http://multixden.blogspot.com/2015/09/)
    (1)
  + ►
    [April](http://multixden.blogspot.com/2015/04/)
    (1)
  + ►
    [March](http://multixden.blogspot.com/2015/03/)
    (2)
  + ►
    [February](http://multixden.blogspot.com/2015/02/)
    (2)
  + ►
    [January](http://multixden.blogspot.com/2015/01/)
    (3)

* ►
  [2014](http://multixden.blogspot.com/2014/)
  (11)
  + ►
    [December](http://multixden.blogspot.com/2014/12/)
    (1)
  + ►
    [October](http://multixden.blogspot.com/2014/10/)
    (3)
  + ►
    [September](http://multixden.blogspot.com/2014/09/)
    (1)
  + ►
    [June](http://multixden.blogspot.com/2014/06/)
    (1)
  + ►
    [May](http://multixden.blogspot.com/2014/05/)
    (1)
  + ►
    [April](http://multixden.blogspot.com/2014/04/)
    (2)
  + ...