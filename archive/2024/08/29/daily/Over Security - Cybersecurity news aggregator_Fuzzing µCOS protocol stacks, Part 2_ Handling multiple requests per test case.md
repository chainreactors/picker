---
title: Fuzzing µCOS protocol stacks, Part 2: Handling multiple requests per test case
url: https://blog.talosintelligence.com/fuzzing-ucos-protocol-stacks-part-2/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-29
fetch_date: 2025-10-06T18:07:32.817874
---

# Fuzzing µCOS protocol stacks, Part 2: Handling multiple requests per test case

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2024/08/VulnDeepDive--1--2.png)

# Fuzzing µCOS protocol stacks, Part 2: Handling multiple requests per test case

By
[Kelly Patterson](https://blog.talosintelligence.com/author/kelly/)

Wednesday, August 28, 2024 12:00

[Vulnerability Deep Dive](/category/vulnerability-deep-dive/)

So far in this series, [I’ve developed a fuzzer for the µC/HTTP-server](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-1/). As described in the previous post, this fuzzer reads from a file to enable compatibility with AFL++. That implementation only fuzzes a single request at a time. Although that single request fuzzer uncovered a few security vulnerabilities, there are complex and interesting object interactions and internal state transitions that occur when multiple requests are received in a single session.

I wanted to be able to fuzz those interactions and transitions by providing a single test case file containing multiple requests. So, this time, I’ll discuss why this approach is more challenging than simply substituting a socket file descriptor with a typical file descriptor, and I’ll describe the feature I added to the open-source library [libdesock](https://github.com/fkie-cad/libdesock) to support multiple requests.

# Reading from a socket vs. reading from a file

It’s a bit confusing thinking about solving this problem because socket communication is two-way communication with a request-response pattern, while reading from a file occurs one way. In a networking client/server model, the client will typically make a request of the server, and the server will respond before the client sends another request.

The µC/HTTP-server works in a single thread so it completely processes and responds to the first request before ever reading from the socket descriptor for a second time.

Our goal is to simulate multiple requests from the client using a single test case file. But what happens if we include two requests within the same test case file? The server code will read the available data from the file until it reaches EOF or fills the buffer.

For instance, suppose a test case file contains two complete HTTP requests. The buffer size of the µC/HTTP-server is 1,460 bytes and the length of our two requests combined are only 841 bytes. This means the entire test case fits within the buffer and is read into memory at once. The µC/HTTP-server will process the first HTTP request and then discard the remaining data in the buffer. Then, when the server code reads from the test case file again, it will have reached EOF while only actually processing the first request.

To address this, we need a way to instruct the server to stop reading the file after processing the first request. This can be achieved by using a delimiter in the test case file. The delimiter should be a unique value that is unlikely to appear anywhere else in the request.

# libdesock

To implement this strategy of using a delimiter to indicate where one request ends and another begins, I added a feature to an existing library called libdesock. The purpose of this library is to de-socket a network application to enable fuzzing. This is because fuzzers typically provide their test inputs via stdin while network applications expect their inputs from network connections. Typically, a network server application will call the libc functions `socket`, `listen`, `accept` and then `read/recv`.

Libdesock operates by leveraging the Linux dynamic linker feature, `LD_PRELOAD`. When the `LD_PRELOAD` environment variable is set to the path of a shared object file, it instructs the dynamic linker to load that shared object before all others. As a result, when the dynamic linker searches for a symbol being called in the executable, it will first look in the shared object specified by the `LD_PRELOAD` environment variable. Normally, the symbols for the functions `socket`, `listen`, `accept` and `read/recv` are found within libc.so and executed from there. However, when `LD_PRELOAD` is set to `libdesock.so`, those symbols are found within the libdesock library and executed there instead. This allows libdesock to alter the behavior of those calls. By intercepting these calls, libdesock cleverly redirects recv/read to stdin rather than a network socket.

## Multiple request feature

Originally, the libdesock code would read up to the size of the buffer used from stdin. This leads to the same issue as mentioned above when attempting to read multiple requests from an input file (stdin in this case):

> “For instance, suppose a test case file contains two complete HTTP requests. The buffer size of the µC/HTTP-server is 1460 bytes and the length of our two requests combined are only 841 bytes. This means the entire test case fits within the buffer and is read into memory at once. The µC/HTTP-server will process the first HTTP request and then discard the remaining data in the buffer. Then, when the server code reads from the test case file again it will have reached EOF while only actually processing the first request.”

To address this, I added a feature to the libdesock read code to look for a request delimiter while reading. If the delimiter is found, it returns all the data read before encountering the delimiter. On the next call to read, it will begin reading after the delimiter and search for another delimiter. This approach works for fuzzing multiple requests in most networked applications because these applications typically run a processing loop where `read/recv` is called, the data is processed, and then `read/recv` is called again. This loop continues until the connection is closed. As mentioned in the [first blog post](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-1/), it was necessary to modify the executable for fuzzing so that it would...