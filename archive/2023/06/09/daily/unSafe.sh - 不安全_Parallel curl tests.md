---
title: Parallel curl tests
url: https://buaq.net/go-167924.html
source: unSafe.sh - 不安全
date: 2023-06-09
fetch_date: 2025-10-04T11:45:54.426381
---

# Parallel curl tests

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

![](https://8aqnet.cdn.bcebos.com/1045fc7f8d5e531d8ac0dd7fb73c479c.jpg)

Parallel curl tests

The curl test suite was born in November 2000. We wrote our own custom
*2023-6-8 23:35:19
Author: [daniel.haxx.se(查看原文)](/jump-167924.htm)
阅读量:37
收藏*

---

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/cheetah.jpg)

The curl test suite was born in November 2000. We wrote our own custom system, dedicated for us.

In May 2001 we changed the file format for individual tests and this is still today the format we use. During the Twenty-two years that have passed we have added some 1600 test cases to the collection and we make sure that they can run on virtually any platform and that each test case themselves specify what curl features they require to work so that builds with those features disabled can skip those tests.

Only a thorough test suite provides the necessary confidence you need to promise to users that we keep existing behaviors and yet we still can and do repeatedly rewrite, refactor and replace large chunks of the internals.

## Synchronous in a single thread

In 2000 we all had single cores and single CPUs. We made the test suite run the tests one by one, in a serial fashion. Some are quick, some take a little longer. While CPUs certainly have grown significantly faster over the lifetime of curl, the amount of test cases have also grown.

Today, on my fast modern machine, running all test cases in the main test suite takes about 10 minutes. If we run them with valgrind enabled (it then invokes all curl related commands and functions with [the valgrind tool](https://valgrind.org/) to monitor that it doesn’t do any serious memory violations or leaks), the same process takes close to 30 minutes.

This might not sound terribly bad, but it also not unusual to run the tests on slower machines that spend two or maybe even five times longer to completion. If you want to run the tests on a few different build combinations to make sure they are all happy, you may need to rerun the set a number of times. It all adds up.

This is a rather ineffective use of time and available system resources. In researching and measuring the current state of curl testing, Dan Fandrich figured out that in a normal test round the CPU is idle 80% of the time! And that’s just one core.

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/05/Screenshot-2023-05-10-at-09-37-50-curl-Parallel-Testing-Proposal-curl.parallel.testing.proposal-2.pdf.png)

Illustration from Dan’s “curl Parallel Testing Proposal”

## Going parallel

In March 2023, Dan brought his [curl Parallel Testing proposal](https://github.com/curl/curl/files/11023995/curl.parallel.testing.proposal.pdf) (11 page PDF) to us, outlining an idea on how to convert the current single-threaded serial test runner into one that runs many separate worker processes and can run several test cases in parallel.

The general idea being that even on a single-core machine, running tests in parallel has the chance to speed up the process a lot. Because of that 80% number if nothing else.

Most (curl) developers of course also have machine with several or even many cores, making parallelism an even better idea.

We all loved the idea, gave Dan our thumbs up and arranged to fund his work on this improvement.

## Port numbers

curl does Internet transfers, and for testing curl we have a set of test servers implemented that curl can talk to and get response back from. The specific tests control exactly how these servers respond and act for each test. To make sure that curl speaks the protocols correctly and consistently in both good and bad situations.

A challenge with this is that the test suite actually has to fire up and run actual networking servers on the local machine for this purpose. Each such server has to listen to a dedicated TCP or UDP port for as long as the tests are still going.

Luckily, we reworked the port number use for test servers recently. Using fixed port numbers for test servers was problematic already with single threaded tests because you could not run a separate test case in a different shell on the same machine etc. They would also sometimes collide with other random services running on developers’ machines.

Since August 2020 all test servers listen on random port numbers. A fundamental criteria for being able to run tests in parallel.

## Landed

After a lot of hard work to refactor the test internals, it can now fire up N worker processes, where each such process can run its own set of test servers, then make sure the main scheduler hands out test cases to all of the workers and collects and outputs the test results from all of them. On June 5, Dan merged the commits to master that made it possible for all of us to start test (!) driving this.

## First impressions

Dan recommends maybe 7 workers per core, but it might be a little bit limited to how much system memory you have since every such worker might end up running a fairly large amount of test servers. It also depends on if you run the tests with or without valgrind.

I ran a first simple test shot on my machine using 80 workers. A full valgrind enabled round with 1606 tests completed in 87 seconds. That is more than **twenty times faster** than previously.

## Some further polish needed

There are still some issues left that make the parallel test setup a little shakier than the normal serial style, so we do not yet enable this by default for people. We will work on fixing those issues and iron out the last wrinkles so that we can soon get everyone onboard on this.

But man, this is a good step forward!

## How?

```
make -sj
cd tests
make -sj
./runtests.pl -j80
```

## tech, open source and networking

文章来源: https://daniel.haxx.se/blog/2023/06/08/parallel-curl-tests/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)