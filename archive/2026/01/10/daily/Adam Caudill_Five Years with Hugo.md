---
title: Five Years with Hugo
url: https://adamcaudill.com/2026/01/10/five-years-with-hugo/?utm_source=atom_feed
source: Adam Caudill
date: 2026-01-10
fetch_date: 2026-01-11T03:41:07.260953
---

# Five Years with Hugo

# [Adam Caudill](https://adamcaudill.com/)

* [Exposera](https://exposera.com/u/adamcaudill "Exposera")

*Security Leader, Researcher, Developer, Writer, & Photographer*

* [Home](https://adamcaudill.com/)
* [Blog](https://adamcaudill.com/blog/)
* [Research](https://adamcaudill.com/research/)
* [Speaking](https://adamcaudill.com/speaking/)
* [Photography](https://adamcaudill.com/photography/)
* [Writing](https://adamcaudill.com/writing/)
* [About](https://adamcaudill.com/about/)

# Five Years with Hugo

A look back at 5 years of experience publishing with Hugo.

Today
|
8 minute read
|
[Administrivia](https://adamcaudill.com/categories/administrivia)

Table of Contents

1. [Writing Friction](#writing-friction)
2. [Markdown All The Things](#markdown-all-the-things)
3. [Themes & Design](#themes--design)
4. [Frequent Changes](#frequent-changes)
5. [Hosting](#hosting)
6. [Easy Extensibility](#easy-extensibility)
7. [What else would I use?](#what-else-would-i-use)
8. [Will I switch again?](#will-i-switch-again)

During a break over Christmas 2020, I rebuilt this site, moving from WordPress to [Hugo](https://gohugo.io/). After more than 5 years of publishing with Hugo, I’d like to share what I’ve learned, what’s worked, what hasn’t, and why for once, I’m happy with the platform I’m using.

This review builds on two recent articles, *[Five Hundred](https://adamcaudill.com/2026/01/02/five-hundred/)*, a retrospective of 500 posts to this site, and *‌[Lessons Learned from 20 Years & Why You Should Blog](https://adamcaudill.com/2026/01/04/lessons-learned-from-20-years-why-you-should-blog/)*, a look back at 20 years of publishing here, and the value of writing & blogging more generally. In this post, I will be diving into publishing with Hugo specifically, what’s good, what’s not, and what you should think about if you are considering it.

## Writing Friction [#](#writing-friction)

In the *[Lessons Learned](https://adamcaudill.com/2026/01/04/lessons-learned-from-20-years-why-you-should-blog/)* post I spoke about the need to carefully consider the friction of the tools you use, as any bit of friction can reduce the motivation and time dedicated to writing. As such, I should address this first and foremost.

In 2012, I [moved to Octopress](https://adamcaudill.com/2012/04/12/moving-to-octopress/), and away from WordPress, there were a variety of reasons for this, though security and performance were major factors. By the end of 2015, I moved back to WordPress. The reason? Friction. With static state generation, the process of creating a new post was slower, took more time & effort, and as a result, I did so less frequently.

By 2020, I was ready to embrace that friction. When I switched from WordPress to Hugo, I knew that each post would take more time, that I wouldn’t post as often. Yet, this isn’t a flaw for me, it’s a feature.

During the 2010s, I posted here 146 times, with an average length of 817 words. So far, in the 2020s, I’ve posted 52 articles, with an average length of 1,629 words. I post less often, though each sees greater effort and more depth, each is a greater investment to ensure that it’s worth the time to read.

While I will loudly caution people to watch for friction, and warn that it can lead to less motivation to spend limited free time writing, it’s not always a flaw. If you are already going to spend several hours (or more) on an article, the additional friction of using a static generator really does become insignificant.

Hugo works great if you don’t mind the friction; at this point, the friction isn’t a problem for how I write today.

## Markdown All The Things [#](#markdown-all-the-things)

Hugo supports various formats for content, though the best support is for [Markdown](https://www.markdownguide.org/), and is what this site uses exclusively. When I switched this site from WordPress to Octopress in 2012, I had manually converted a decade’s worth of content to Markdown from the HTML that WordPress generates. Thankfully, after that all content has been in Markdown.

Even when I switched from Octopress back to WordPress, I took advantage of the fact that WordPress supports Markdown as well. This made later moves much, much easier.

I could explain why you do want to write in Markdown, for a variety of reasons, though Anil Dash recently [documented the success of Markdown](https://www.anildash.com/2026/01/09/how-markdown-took-over-the-world/) quite well, as such, you should read his article if you want a deeper dive.

## Themes & Design [#](#themes--design)

Hugo has a [rich collection of themes](https://themes.gohugo.io/) available, many of these are remarkably well designed and impressive contributions from their talented designers. I selected a clean and simple theme, [Kiera](https://themes.gohugo.io/themes/hugo-kiera/), and spent a week extending it, expanding the features, redesigning the home page, adding the sidebar, and countless other changes.

Hugo builds on the [Go Template](https://pkg.go.dev/html/template) system, which allows the themes to be quite robust and flexible, supporting extensive embedded logic. While this doesn’t offer the degree of flexibility that I would truly like – such as having full access to Go[1](#fn:1) - it does work well and can do almost anything one would need.

The template files are HTML[2](#fn:2), and easy to edit and customise for your particular desires, it’s one of the easier and more pleasant templating systems that I’ve worked with.

## Frequent Changes [#](#frequent-changes)

The team behind Hugo are constantly working to improve the framework, fix bugs, add features, improve flexibility, and address design constraints. As I write this, on the 10th day of January, there have already been 4 releases this year.

This constant change does come at a price though, as there is a steady stream of new deprecation warnings that are added, signalling the future change or removal of some feature. There are also infrequent but very real breaking changes that slip in, without any clear warning. Over the last 5 years, there’s been at least two of these breaking changes each year, leaving the site broken in some way.

Thankfully, most of these breaking changes have been in less important areas, or places where I’m leveraging functionality that’s very much non-standard (as is my wont to do).

To help detect these issues, I’ve found it to be quite useful to use two different GitHub Actions jobs in the repository that houses this site, one performs a build against the version of Hugo that I’m currently using, and the other builds against the latest version. While this won’t catch all issues, it does surface many issues before they start breaking deployments.

## Hosting [#](#hosting)

To keep the costs low, avoid maintaining another server, and ensure good performance, I opted to use Cloudflare Pages to host the site. This integrates cleanly with GitHub, it supports preview URLs, including for branches, which is an ideal way to get feedback before publishing, and allows me to write on any device, even without a local build environment, as it’s built on Cloudflare’s servers.

While there are quite a few providers that now offer similar services for static or otherwise edge-deployed sites, at the time Cloudflare offered the best features and the lowest price.

One beauty of Hugo and other static generators is that the site can be hosted anywhere. I intentionally don’t perform any edge compute, so this site could be hosted on a Raspberry Pi if I wanted. This adds great flexibility to move the site should the need arise, without needing to change or rebuild anything.

## Easy Extensibility [#](#easy-extensibility)

One thing I love about Hugo and other static generators, is that I can easily extend the build process to add new functionality that isn’t part of the framework itself. I’ve done this to add [automated related content](https://adamcaudill.com/2021/09/06/hugo-content-based-related-content/), [genera...