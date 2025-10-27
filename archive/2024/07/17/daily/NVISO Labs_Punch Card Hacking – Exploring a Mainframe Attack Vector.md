---
title: Punch Card Hacking – Exploring a Mainframe Attack Vector
url: https://blog.nviso.eu/2024/07/16/punch-card-hacking-exploring-a-mainframe-attack-vector/
source: NVISO Labs
date: 2024-07-17
fetch_date: 2025-10-06T17:41:11.172491
---

# Punch Card Hacking – Exploring a Mainframe Attack Vector

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Punch Card Hacking – Exploring a Mainframe Attack Vector

[Jonathan Prince](https://blog.nviso.eu/author/jonathan-prince/ "Posts by Jonathan Prince")

[Exploitation](https://blog.nviso.eu/category/exploitation/), [Application Security](https://blog.nviso.eu/category/application-security/)

July 16, 2024July 16, 2024
9 Minutes

Mainframes are the unseen workhorses that carry the load for many services we use on a daily basis: Withdrawing money from an ATM, credit card payments, and airline reservations to name just a few of the high volume workloads that are primarily handled by mainframes. For those that like to see figures to support this claim mainframes are:

* In use by 92 of the top 100 banks and all of the top 10 Insurers worldwide (2020)
* Handle 90% of all credit card transactions.
* Used by 71% of Fortune 500 companies.

Despite the importance of these powerful machines there are few security professionals with an understanding of their intricacies and even fewer actively engaged in penetration testing and research. In this article, we demonstrate an entry level technique for penetration testers to get started using a different twist on a familiar technology to attack these computing giants.

## Hardware, Architecture and Operating System

Today, when referring to mainframe computers, we are almost always talking about IBM hardware running z/OS. z/OS is a 64-bit operating system for IBM z/Architecture released in March 2001 as a successor to OS/390 and the MVS operating system line with its origins dating back to the 1960s. IBM Z maintains a very high level of backwards compatibility and the latest systems are capable of running many unmodified applications written over 5 decades ago. In this blog post we will be focusing on an integral component of z/OS: z/OS UNIX, a subsystem often called Unix System Services (USS). USS is an implementation of the UNIX operating system certified by The Open Group (the certifying body for the UNIX trademark to ensure compliance with established standards) which:

* Allows UNIX applications to run on IBM Z mainframes.
* Provides users with a shell environment, similar to common \*nix shells, often referred to as OMVS (OpenEdition MVS – USS’s predecessor).
* Extends z/OS to offer common network services such as OpenSSH, HTTP servers and FTP.

## Punch Cards? A look at Jobs, JES, and JCL

Before diving into how we can abuse some of these services we will look at a core concept of the z/OS that, somewhat surprisingly, derives directly from job cards like the one pictured here:

![Mainframe Punch Card](https://blog.nviso.eu/wp-content/uploads/2024/07/image-1.png)

Most of the work carried out by a mainframe is performed through the use of jobs. A job is a unit of work, consisting of one or more steps that are executed to perform a task. Originally these jobs were defined using punch cards like the one above, today these physical cards are replaced with files written in Job Control Language (JCL). The management of these jobs and the resources they require is handled by the Job Entry Subsystem (JES). JES receives job submissions, prioritizes them, and schedules them for execution. The execution of jobs is then coordinated by JES to ensure efficient use of system resources by allocating necessary resources and monitoring their progress. On completion, JES manages the job output for collection or distribution to the appropriate destinations.

Let us look at a basic job card written in JCL. The job will create a new file or, as it is described in the mainframe world, allocate a dataset. One of the first hurdles when talking about mainframes is to get handle on all the new terminology and a plethora of acronyms.

//USERJOB JOB ACC-INFO,’User Name’,MSGCLASS=A,
// MSGLEVEL=(1,1),NOTIFY=&SYSUID
//STEP1 EXEC PGM=IEFBR14
//DDNAME DD DSN=USER.DATASET.NAME,
// DISP=(NEW,CATLG),
// UNIT=SYSALLDA,SPACE=(TRK,1)
/\*

Some notes on JCL syntax:

* Lines of JCL begin with the double slash “//”
* A comma is used at the end of a line to continue a JCL statement on a new line.
* The continuation begins with the obligatory “//” and usually an indentation.
* JCL has a maximum line length of 80 characters (this is carried over from the punch cards), but the statements should be limited to 71(the last columns are used for indexes)
* Ends with the optional line “/\*”

Job cards are made up of a series of statements. All job cards use the following three main types of JCL statements:

* One JOB statement to identify the unit of work the operating system is to perform.
  + Identifies the beginning of a job.
  + Specifies the job name (1-8 characters long), in our example “USERJOB”. A common pattern is to use the convention of username + additional character(s) as identifier.
  + May include or require additional positional or named parameters (accounting info, name, msg class/level) depending on the organizational requirements.
* One or more EXEC statements, depending on the number of job steps within the job.
  + Names the step within the job, in our case “STEP1”
  + Declares the program (PGM) to be executed, in this case “IEFBR14”.
* One or more DD statements to identify the input and output data sets (DD = Data Definition)
  + Used to declare data properties, in our example a dataset name (DSN) of “USER.DATA.NAME” and details for the allocation of the new dataset.

At this point it may still be a little unclear exactly what use this has for us. Perhaps a small selection of some common programs we could execute might lead us further into understanding the impact of job submission:

* IEFBR14: Described by IBM to “Do (almost) nothing”, can be used to allocate datasets as above.
* IKJEFT01: Used to invoke Time Sharing Option (TSO) commands. TSO can be considered the native z/OS shell.
* BPXBATCH: Executes UNIX shell commands.
* IEBGENER: Has several uses, most often used to copy datasets/files.
* IXRJCL: Executes REXX, a powerful scripting language.

Now that we have covered the basics, let’s start the fun part.

## Submitting Jobs via FTP

The mainframe FTP service has some additional functionality that can be extremely useful during penetration testing. Let us assume a situation where we have access to an FTP service and a set of valid credentials. This scenario is not uncommon, especially in red team engagements where credentials are often discovered unprotected i...