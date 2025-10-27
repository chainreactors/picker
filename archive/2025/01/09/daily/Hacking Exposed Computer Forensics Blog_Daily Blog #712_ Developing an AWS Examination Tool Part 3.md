---
title: Daily Blog #712: Developing an AWS Examination Tool Part 3
url: https://www.hecfblog.com/2025/01/daily-blog-712-developing-aws.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-09
fetch_date: 2025-10-06T20:26:09.729065
---

# Daily Blog #712: Developing an AWS Examination Tool Part 3

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog)

Daily Blog #712: Developing an AWS Examination Tool Part 3

# Daily Blog #712: Developing an AWS Examination Tool Part 3

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 08, 2025
•

[ai programming](https://www.hecfblog.com/search/label/ai%20programming?&max-results=8)
[aws](https://www.hecfblog.com/search/label/aws?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVvQEc421H5Ot05Uemb5lFYC9wNqnW_OwJdUdEIQqVJIW4La7QmYOqzIYGYK30Thg2MsOHMfOIRhcLzTgu4nhowMzEXEfinnhHPSoQTnsdXzP0pXVvvocsUT5DNz6fCZa0at728ixebEBHLMU_hO8fok5Mejv-SChTz455FAg-aVyU0e8EUIlI6PzpRA8/w640-h640/awsenum3.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVvQEc421H5Ot05Uemb5lFYC9wNqnW_OwJdUdEIQqVJIW4La7QmYOqzIYGYK30Thg2MsOHMfOIRhcLzTgu4nhowMzEXEfinnhHPSoQTnsdXzP0pXVvvocsUT5DNz6fCZa0at728ixebEBHLMU_hO8fok5Mejv-SChTz455FAg-aVyU0e8EUIlI6PzpRA8/s1024/awsenum3.webp)

**Hello Reader,**

Today, I went down a rabbit hole of prompting and ended up adding a ton of new features to our application. Here’s what the latest version now includes:

### New Features:

* **AWS Organization Scanning**: Detects other AWS accounts in the organization of the accessed account.
* **Cross-Account Role Assumption**: Verifies if the account key can assume the AWS Organizations role to enumerate other accounts.
* **Parallel Region Scanning**: Uses multiprocessing to scan all regions simultaneously for every accessible account.
* **CloudTrail Logs**: Identifies CloudTrail logs in each account and displays their locations in a dedicated GUI tab. Also checks if they are only stored by AWS (default storage).
* **VPC Flow Logs**: Lists VPC Flow logs in a separate GUI tab, showing where they are stored.
* **EC2 Metadata**: Adds detailed metadata for EC2 instances, snapshots, and EBS volumes.
* **CloudWatch Log Groups**: Provides support for CloudWatch Log groups.
* **Lightsail Instances**: Adds enumeration support for Lightsail instances.

### A Different Approach:

Rather than listing the many individual prompts I used to add these features (and the iterative process of fixing errors), I decided to take a new approach. I asked the model to create a single prompt that could recreate the current state of this program. Here's what it generated:

---

### Generated Prompt

Create a Python-based GUI application for enumerating AWS resources across multiple accounts and regions. The application should have the following specifications:

#### **Core Requirements**:

1. **GUI Framework**:

   * Use PySide6 for the interface.
   * Include a tabbed layout for different resource types.
   * Show real-time progress with progress bars.
   * Provide a resource tree view for navigation.
   * Include a log window for status messages.
2. **AWS Integration**:

   * Support both AWS profile and direct API key authentication.
   * Enable AWS Organizations support for multi-account scanning.
   * Implement cross-account role assumption.
   * Use boto3 with retry logic and error handling.
   * Support parallel processing of regions.
3. **Resource Types to Enumerate**:

   * **EC2 Resources**:
     + Instances (metadata: type, IPs, key name, platform).
     + Volumes (size, type, encryption, IOPS).
     + Snapshots (size, source, encryption).
     + Security groups.
   * **Storage**:
     + S3 buckets (with region mapping).
     + EBS volumes (with attachments).
   * **Database**:
     + RDS instances.
     + Lightsail databases.
   * **Logging & Monitoring**:
     + CloudTrail configurations.
     + CloudWatch Log Groups.
     + VPC Flow Logs.
     + Organization-wide logging detection.
4. **Data Export**:

   * Support for exporting in Excel, JSON, or text format.
   * Include metadata and a hierarchical structure in the export.
   * Use the AWS Account ID and timestamp as the default filename for uniqueness.
5. **Progress Tracking**:

   * Display overall, per-account, and region-specific progress.
   * Show status messages for operations.

#### **Technical Specifications**:

1. **Multiprocessing**:

   * Use Python’s multiprocessing to handle parallel region scanning.
   * Implement proper process cleanup and progress communication.
2. **Error Handling**:

   * Implement exponential backoff for API calls.
   * Handle permission issues gracefully.
   * Display clear error messages in the GUI.
3. **Security**:

   * Ensure secure credential handling.
   * Support AWS profiles and direct API key input.
   * Implement minimum required permissions.
4. **GUI Features**:

   * Tab-based views for resource types (EC2, storage, database, logging).
   * Progress dialogs with multiple progress bars.
   * Resource tree view for navigation.
   * Color-coded status indicators.
5. **Dependencies**:

   * **boto3/botocore**: AWS SDK.
   * **PySide6**: GUI framework.
   * **pandas**: Data handling.
   * **openpyxl**: Excel export.
6. **File Structure**:

   * `aws_enumerator.py`: Main application.
   * `requirements.txt`: Dependency list.
   * `README.md`: Project documentation.
   * License file.

---

### Progress So Far:

The best part? I still haven’t written a single line of code myself! The application now has a polished interface and works as described. I've also updated the README file and `requirements.txt`, so everything is ready for you to try.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXjYJoe51OhW5CuDcfqRq7wOjZd5ef7-04vcDpm5Jgvo3McPI-exZD_-L_Vhou1tuWJZrcnzQ_k_g08XinJnyuY468xQsC6zJBplI3bsSOLwhdzQ7BqjqrLIMhFm-_l3hyphenhyphen0TJsnJdCRx3RhhTjzSZ0mUZd3NQmYiKzfmggcAu5Jbvs3lLJJG5Eff363DU/w640-h398/example1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXjYJoe51OhW5CuDcfqRq7wOjZd5ef7-04vcDpm5Jgvo3McPI-exZD_-L_Vhou1tuWJZrcnzQ_k_g08XinJnyuY468xQsC6zJBplI3bsSOLwhdzQ7BqjqrLIMhFm-_l3hyphenhyphen0TJsnJdCRx3RhhTjzSZ0mUZd3NQmYiKzfmggcAu5Jbvs3lLJJG5Eff363DU/s1001/example1.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOmvdwWS3F0QKVp4qFXV6h8Z9RuBRNQ3moSFfPEeOPOOC2vx5CqoNwp2Ypx7m9amy7YmZI0d8VW8uowTRsTM0e74DEqORmTbyGZogRICG_VT4_QaOXNYdhBOlN6GZjNDdOKp1hunTl2dMXfOeE82WWwml87AS5Cki5FWzqf-OJ1ZQ1vEZtwKWqa6G1PpQ/w640-h216/example2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOmvdwWS3F0QKVp4qFXV6h8Z9RuBRNQ3moSFfPEeOPOOC2vx5CqoNwp2Ypx7m9amy7YmZI0d8VW8uowTRsTM0e74DEqORmTbyGZogRICG_VT4_QaOXNYdhBOlN6GZjNDdOKp1hunTl2dMXfOeE82WWwml87AS5Cki5FWzqf-OJ1ZQ1vEZtwKWqa6G1PpQ/s1003/example2.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnYivNmwLcot7zpSZs102MbP0zzIUj_J6Ve0GlmFv_LfAuyttJYghEift6kFKyDeqy9ylay2DoHguD3WwU9oXQTkD88FT993dMQujmsyxMclnTvUDFJWL5izUusX-yEHjLK_sfpKYAkfW8vHF7CxopDRaHD6G-zwHYAdvVmsFLbXiwg2I7ZIgzrrqnnz8...