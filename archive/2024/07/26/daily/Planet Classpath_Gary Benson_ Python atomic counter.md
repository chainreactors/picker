---
title: Gary Benson: Python atomic counter
url: https://gbenson.net/python-atomic-counter/
source: Planet Classpath
date: 2024-07-26
fetch_date: 2025-10-06T17:42:00.508436
---

# Gary Benson: Python atomic counter

[Skip to content](#content)

[gbenson.net](https://gbenson.net/)

# Python atomic counter

[gbenson](https://gbenson.net/author/admin/ "Posts by gbenson")

[Concurrency](https://gbenson.net/category/concurrency/), [GIL](https://gbenson.net/category/python/gil/), [Python](https://gbenson.net/category/python/), [Snippets](https://gbenson.net/category/snippets/)

Thursday 25th July 2024Thursday 25th July 2024
1 Minute

Do you need a thread-safe atomic counter in Python? Use [`itertools.count()`](https://docs.python.org/3/library/itertools.html#itertools.count):

```
>>> from itertools import count
>>> counter = count()
>>> next(counter)
0
>>> next(counter)
1
>>> next(counter)
2
```

I found this in the [decorator](https://pypi.org/project/decorator/) package, labelled *"Atomic get-and-increment provided by the GIL"*. So simple! So cool!

* Tagged
* [atomic](https://gbenson.net/tag/atomic/)
* [concurrency](https://gbenson.net/tag/concurrency/)
* [GIL](https://gbenson.net/tag/gil/)
* [Python](https://gbenson.net/tag/python/)
* [synchronization](https://gbenson.net/tag/synchronization/)
* [threads](https://gbenson.net/tag/threads/)

![](https://secure.gravatar.com/avatar/7f5ceed659dcc3dfbbaabaa442f88548841b5c261110017a8d507eb468d1a875?s=80&d=mm&r=g)

## Published by gbenson

I make things // he/him [View all posts by gbenson](https://gbenson.net/author/admin/)

**Published**
Thursday 25th July 2024Thursday 25th July 2024

## Post navigation

[Previous Post git submodule forgetting](https://gbenson.net/git-submodules/)

[Next Post Too many git branches?](https://gbenson.net/so-many-git-branches/)

### Leave a Reply[Cancel reply](/python-atomic-counter/#respond)

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[Proudly powered by WordPress](http://wordpress.org/)
 |
Theme: Independent Publisher 2 by [Raam Dev](http://raamdev.com/).