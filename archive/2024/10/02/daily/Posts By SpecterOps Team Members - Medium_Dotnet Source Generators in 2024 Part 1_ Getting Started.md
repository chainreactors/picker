---
title: Dotnet Source Generators in 2024 Part 1: Getting Started
url: https://posts.specterops.io/dotnet-source-generators-in-2024-part-1-getting-started-76d619b633f5?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-10-02
fetch_date: 2025-10-06T18:55:22.960987
---

# Dotnet Source Generators in 2024 Part 1: Getting Started

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F76d619b633f5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fdotnet-source-generators-in-2024-part-1-getting-started-76d619b633f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fdotnet-source-generators-in-2024-part-1-getting-started-76d619b633f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-76d619b633f5---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-76d619b633f5---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Dotnet Source Generators in 2024 Part 1: Getting Started

[![Jonathan Owens](https://miro.medium.com/v2/resize:fill:64:64/1*NcRudyjrwDx6UPl-YDD_6Q.png)](https://dragoqcc.medium.com/?source=post_page---byline--76d619b633f5---------------------------------------)

[Jonathan Owens](https://dragoqcc.medium.com/?source=post_page---byline--76d619b633f5---------------------------------------)

17 min read

·

Oct 1, 2024

--

6

Listen

Share

## Introduction

In this blog post, we will cover the basics of a source generator, the major types involved, some common issues you might encounter, how to properly log those issues, and how to fix them.

Source Generators have existed since .NET 5 was first introduced in late 2020. They have seen numerous improvements since that initial release, including the creation of newer Incremental Source Generators.

***TLDR: Source generators in .NET enable you to inspect user code and generate additional code on the fly based on that analysis. The example in this blog post may seem a bit redundant, but as you use more advanced patterns, you can generate hundreds of lines of code, helping to reduce boilerplate and repetitive code across your projects. Source generators are also great for lowering runtime reflection use, which can be expensive and slow down your applications.***

**Update**: I updated the stated reason a source generator must target the .NET standard and removed some redundant code from the examples.

While developing a C# library to perform messaging between various process components or between processes, I encountered an issue where client programs using this new messaging library would need to add a list of all the “Messenger types.” I had heard of source generators and experimented with them a small amount before encountering this problem, so I figured I could dive in and devise a working solution to handle this and inject the list of “Messenger types” as a property automagically.

![]()

I have also been learning various programming paradigms and interesting practices. Vertical Slice architecture and aspect-oriented programming (AOP) are the two relevant to this blog. Vertical slices focus on grouping things that will change together, typically by the feature they represent, regardless of the layer they belong to. The goal of the slices is to minimize coupling between slices and maximize coupling in a slice (i.e., things in a feature depend on each other while trying not to rely on other slice features). This keeps the code base modular and makes it easy to update, remove, or add new slices, as the changes shouldn’t directly affect existing slices. [[You can read more on vertical slices here](https://www.jimmybogard.com/vertical-slice-architecture/)]

AOP is a programming paradigm that aims to increase modularity by allowing the separation of cross-cutting concerns. Typically, in C#, this is implemented by creating attributes that are then placed on classes, methods, etc., to introduce or modify the decorated code. So, with these things in mind, I wanted to look at creating a feature that worked with vertical slices using AOP, and given my newfound challenge of automatically injecting a list of objects into my messenger app at build time, I had just the target goal in mind to combine all of it together.

With that brief overview of why I started messing with source generators, let’s take a quick step back and cover the basics of what a source generator is, what it lets you do, and what it doesn’t.

## What is a Source Generator?

According to Microsoft: “*Source generators aim to enable compile-time metaprogramming, that is, code that can be created at compile time and added to the compilation. Source generators will be able to read the contents of the compilation before running, as well as access any additional files, enabling generators to introspect both user C# code and generator-specific files. Generators create a pipeline, starting from base input sources and mapping them to the output they wish to produce. The more exposed, properly equatable states exist, the earlier the compiler will be able to cut off changes and reuse the same output.*”

Press enter or click to view image in full size

![]()

Figure 1 — [Source Generator dataflow](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/media/source-generators/source-generator-visualization.png), Microsoft

Simply put, source generators in .NET are library projects that you can add to a solution or include in existing NuGet packages. They are meant to be utilized only during the build process to add new code to a project.

[[Read more about common source generator use cases here](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview)].

## What Are Source Generators Not Meant to Do

Microsoft calls out two main concepts as areas where generators are not meant to be used. The first area is adding language features. Microsoft states: “*Source generators are not designed to replace new language features: for instance, one could imagine records being implemented as a source generator that converts the specified syntax to a compilable C# representation. We explicitly consider this to be an anti-pattern; the language will continue to evolve and add new features, and we don’t expect source generators to be a way to enable this. Doing so would create new ‘dialects’ of C# that are incompatible with the compiler without generators.*”

In this regard, I agree with the team that allowing any .NET developer to start adding new features to the language opens up the possibility of competing features, confusing requirements, and incompatibility with the .NET compiler; which will only serve to confuse and push developers away from source generators altogether.

The second is in code modification; the Microsoft documentation also states, “*There are many post-processing tasks that users perform on their assemblies today, which here we define broadly as ‘code rewriting’. These include, but are not limited to:*

* *Optimization*
* *Logging injection*
* *IL Weaving*
* *Call site ...