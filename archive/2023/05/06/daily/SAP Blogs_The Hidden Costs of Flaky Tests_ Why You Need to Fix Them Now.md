---
title: The Hidden Costs of Flaky Tests: Why You Need to Fix Them Now
url: https://blogs.sap.com/2023/05/05/the-hidden-costs-of-flaky-tests-why-you-need-to-fix-them-now/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:33.920624
---

# The Hidden Costs of Flaky Tests: Why You Need to Fix Them Now

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* The Hidden Costs of Flaky Tests: Why You Need to F...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164818&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The Hidden Costs of Flaky Tests: Why You Need to Fix Them Now](/t5/technology-blog-posts-by-sap/the-hidden-costs-of-flaky-tests-why-you-need-to-fix-them-now/ba-p/13570977)

![haeuptle](https://avatars.profile.sap.com/d/0/idd099b643170a795cffeb57f54e74f97436f5a5f26bb8d41fc62037e69aae99a0_small.jpeg "haeuptle")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[haeuptle](https://community.sap.com/t5/user/viewprofilepage/user-id/40145)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164818)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164818)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570977)

‎2023 May 05
1:29 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164818/tab/all-users "Click here to see who gave kudos to this post.")

1,187

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [Java](https://community.sap.com/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [Research and Development](https://community.sap.com/t5/c-khhcw49343/Research%2520and%2520Development/pd-p/708931460062032886984100414137377)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [Java

  Programming Tool](/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [Research and Development

  Topic](/t5/c-khhcw49343/Research%2Band%2BDevelopment/pd-p/708931460062032886984100414137377)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (6)

Flaky tests (aka fragile, brittle or instable tests) are tests that fail or pass intermittently without any changes to the codebase. They are a common problem in software development and can be frustrating to deal with. However, it is important to be disciplined with flaky tests because they can lead to a number of issues.

## Why it is important to deal with a flaky, fragile or instable test suite

It is important to be disciplined with flaky tests because fixing flaky tests is essential for ensuring a stable and reliable testing process. Eliminating flaky tests is not only important to prevent time waste, but is also crucial to improving developers’ confidence in the tests.

* Firstly, flaky tests can cause a loss of trust in the test suite. If tests are failing, it can be difficult to know whether a failure is due to a genuine issue or a flaky test. This can lead to developers ignoring test failures.

* Secondly, flaky tests can slow down the development process. If developers are spending time investigating false positives or ignoring test failures, it can take longer to identify and fix genuine issues. This can lead to slower development cycles, lower productivity and a slower time to market.

![](/legacyfs/online/storage/blog_attachments/2023/05/rapid_test_results.png)

Rapid Test Results from <https://imgs.xkcd.com/comics/rapid_test_results.png>  under Creative Commons BY-ND 2.5

## Why is flakiness extremely critical when moving to Continuous Delivery?

Keep in mind that the robustness of tests and the maintainability is a major factor for the productivity of a development team. With the move to Continuous Delivery the aim is to execute tests more often and potentially with every change. If your test suite of system tests fails in 20% of the changes, that slows you down enormously. And you need a lot of time to investigate upcoming issues. Therefore, if you choose your test strategy and a tool for system testing, the robustness of your test suite should be one of the most important criterias.

## The Top 5 Strategies for Avoiding Flaky Tests

So what are good practices for avoiding, identifying and reducing flakiness.

### Best Practices for Writing Code and Tests to Reduce Flakiness

In this chapter, we’ll explore some best practices for writing tests that are reliable, deterministic, and less prone to flakiness. By following these best practices, you can ensure that your tests are testing the right things, catching real-world issues, and providing valuable feedback to your development team.

* [Balanced Test Strategy](https://blogs.sap.com/2021/12/06/shared-language-for-talking-about-test-strategy/): Have a lot more stable unit, component and isolated integration tests than system or scenario tests. Probably the most important to avoid flakiness.

* **Test Isolation:** Test Isolation is a essential technique for keeping lower level tests effective, maintainable, robust and fast. Testing with the real implementation can have the advantage to find more bugs and avoid that test code gets out of sync with the real implementation. Based on the architecture and design of the code you need to decide where to isolate and where to use the real implementation. E.g. it does not make sense to isolate from value objects. Test isolation is especially important to isolate from slow, fragile, expensive dependencies or dependencies, which would make the setup of the tests extremely complicated. Besides, it helps to simulate behaviour, which otherwise would be hard to test or verify. The Clean Code books and the Open Source repository contain a lot of guidance on how to apply test isolation and write stable tests. You can find more details in the blog [Clean Code: Writing maintainable, readable and testable code](https://blogs.sap.com/2022/12/21/clean-code-writing-maintainable-readable-and-testable-code/)

* [Testable Architecture](https://blogs.sap.com/2021/12/15/testability-critical-but-sometimes-forgotten/): There are also some basic patterns you can consider when defining your architecture.

### How to Identify and Fix Flaky Tests

By identifying and fixing flaky tests, developers can ensure that the test suite is reliable and trustworthy. This can lead to faster development cycles, a quicker time to market, and a more robust codebase. There are several strategies, which can help with reducing flakiness.

* **Keep the mainline running:** Keeping the mainline running is a very important principle for reducing flakiness and staying productive because it helps ensure that the test suite is always in ...