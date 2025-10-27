---
title: Spec-tac-ula Deserialization: Deploying Specula with .NET
url: https://trustedsec.com/blog/spec-tac-ula-deserialization-deploying-specula-with-net
source: TrustedSec
date: 2024-10-18
fetch_date: 2025-10-06T18:56:13.697230
---

# Spec-tac-ula Deserialization: Deploying Specula with .NET

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Spec-tac-ula Deserialization: Deploying Specula with .NET](https://trustedsec.com/blog/spec-tac-ula-deserialization-deploying-specula-with-net)

October 17, 2024

# Spec-tac-ula Deserialization: Deploying Specula with .NET

Written by
James Williams

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/SpeculaDeserialization_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1729002346&s=fde7de41995ce777681f191de0b60712)

Table of contents

* [Finding a Vulnerable App](#Finding)
* [Popping Calc](#Popping)
* [Running Code](#Running)
* [Specula Time](#Specula)
* [XamlAssemblyLoadFromFile](#AssemblyLoad)
* [Wrapping Up](#WrappingUp)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#ba85c9cfd8d0dfd9ce87f9d2dfd9d19f888ad5cfce9f888aced2d3c99f888adbc8ced3d9d6df9f888adcc8d5d79f888aeec8cfc9cedfdee9dfd99f888b9cdbd7ca81d8d5dec387e9cadfd997cedbd997cfd6db9f888afedfc9dfc8d3dbd6d3c0dbced3d5d49f89fb9f888afedfcad6d5c3d3d4dd9f888ae9cadfd9cfd6db9f888acdd3ced29f888a94f4ffee9f89fb9f888ad2cececac99f89fb9f88fc9f88fccec8cfc9cedfdec9dfd994d9d5d79f88fcd8d6d5dd9f88fcc9cadfd997cedbd997cfd6db97dedfc9dfc8d3dbd6d3c0dbced3d5d497dedfcad6d5c3d3d4dd97c9cadfd9cfd6db97cdd3ced297d4dfce "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspec-tac-ula-deserialization-deploying-specula-with-net "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Spec-tac-ula%20Deserialization%3A%20Deploying%20Specula%20with%20.NET%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspec-tac-ula-deserialization-deploying-specula-with-net "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fspec-tac-ula-deserialization-deploying-specula-with-net&mini=true "Share on LinkedIn")

Earlier this year, I gave a talk at [Steelcon](https://www.steelcon.info) on .NET deserialization and how it can be used for Red Team ops. That talk focused on the theory of .NET deserialization, how to identify new vulnerabilities, and some limitations that would need to be overcome while building exploits. Since giving that talk, [Specula](https://trustedsec.com/resources/tools/specula) has been released to the world. I wanted to revisit this topic and show how we can use deserialization to backdoor a workstation with Specula.

## Finding a Vulnerable App

While there are a few public examples of .NET deserialization vulnerabilities we could exploit, we will use a simple 'dummy' app for our proof-of-concept code. Sorry, there will be no free 0days in this post.

```
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;

namespace Deserializer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Please provide a file path.");
                return;
            }

            // Get the file path from the first argument
            string filePath = args[0];

            // Check if the file exists
            if (!File.Exists(filePath))
            {
                Console.WriteLine($"File not found: {filePath}");
                return;
            }

            // Open the file for reading and display its contents
            try
            {
                using (StreamReader reader = new StreamReader(filePath))
                {
                    string content = reader.ReadToEnd();
                    Console.WriteLine("Loaded File...");
                    var fileBytes = Convert.FromBase64String(content);
                    Console.WriteLine("Deserializing...");
                    DeserializePayload(fileBytes);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error reading file: {ex.Message}");
            }
        }

        static object DeserializePayload(byte[] payload)
        {
            using (var memoryStream = new MemoryStream(payload))
            {
                var formatter = new BinaryFormatter();
                try
                {
                    var f = formatter.Deserialize(memoryStream);
                    return f;
                }
                catch (Exception ex)
                {

                    return null;
                }
            }
        }
    }
}
```

This code takes a file path from the command line, does some sanity checking, then p...