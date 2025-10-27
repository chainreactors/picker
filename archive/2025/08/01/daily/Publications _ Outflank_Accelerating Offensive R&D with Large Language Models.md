---
title: Accelerating Offensive R&D with Large Language Models
url: https://www.outflank.nl/blog/2025/07/29/accelerating-offensive-research-with-llm/
source: Publications | Outflank
date: 2025-08-01
fetch_date: 2025-10-07T00:15:18.702610
---

# Accelerating Offensive R&D with Large Language Models

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [Accelerating Offensive R&D with Large Language Models](https://www.outflank.nl/blog/2025/07/29/accelerating-offensive-research-with-llm/ "Accelerating Offensive R&D with Large Language Models")

[Kyle Avery](https://www.outflank.nl/blog/author/kyleavery/ "Posts by Kyle Avery")
 |
July 31, 2025

At Outflank, we continually seek ways to accelerate our research and development efforts without compromising quality. In this pursuit, we’ve begun integrating large language models (LLMs) into our internal research workflows. While we’re still exploring the full potential of AI-powered offensive tooling, this post highlights how we’ve already used AI to speed up the delivery of traditional offensive capabilities.

By leveraging AI as a research accelerator, we can dedicate more time to refining, testing, and hardening the techniques that ultimately make it into [our OST offering](https://outflank.nl/ost). This post is a case study of our AI-assisted exploration of the “trapped COM object” bug class.

James Forshaw [described](https://googleprojectzero.blogspot.com/2025/01/windows-bug-class-accessing-trapped-com.html) the idea of trapped COM objects earlier this year. Subsequently, IBM X-Force Red [weaponized the technique](https://www.ibm.com/think/x-force/fileless-lateral-movement-trapped-com-objects) for lateral movement, which further piqued our interest. Their lateral movement POC has five high-level steps:

1. Set the registry keys required for reflective .NET execution (**`AllowDCOMReflection`** and **`OnlyUseLatestCLR`**)
2. Hijack the COM registration for `StdFont` so it points to the `System.Object` class
3. Create an instance of the `WaaSRemediationAgent` class over DCOM
4. Access the type library reference for `stdole` and resolve the `StdFont` class to create a “trapped” instance of `System.Object`
5. Use .NET reflection on the **`System.Object`** instance to invoke **`Assembly.Load`**

Both blog posts utilize the **`WaaSRemediationAgent`** COM class, which runs in a service with Protected Process Light (PPL). This attribute ultimately prevents the .NET runtime from loading into the `WaaSMedicSvc` service on Windows 11, rendering the approach ineffective on updated endpoints. This limitation is specific to the chosen COM class, however, rather than inherent to the bug class itself. Therefore, we attempted to identify an alternative COM class that met the requirements for lateral movement without relying on a PPL host process. In the remainder of this post, we’ll detail our journey to discover such alternatives.

## Discovering Trapped COM Objects

We utilize a private framework inspired by collaborative architectures like [Argusee](https://www.darknavy.org/blog/argusee_a_multi_agent_collaborative_architecture_for_automated_vulnerability_discovery/) for this type of research. We divided our process into two phases for the sake of explanation, but in practice, a single harness handles the entire workflow.

### Enumeration

There are essentially two requirements for a lateral movement candidate in this bug class:

1. DCOM-enabled
2. Exposes a command/code execution capability

We built a simple C# program to hunt for these candidates by enumerating COM classes and dumping the results to JSON. Our collector discovers registered COM classes in the Windows registry and records various metadata, including method signatures, privilege levels, and referenced type libraries. While it’s straightforward to check if a class supports DCOM, determining whether it can actually execute code is more challenging. The resulting JSON gives us enough information to spot promising targets, but it cannot guarantee lateral movement opportunities. For this example, we simply filter for the referenced type library used by Forshaw to execute a .NET assembly.

Of course, there are other hijackable classes, as well as different code execution methods, that we can discover with a combination of filters. Since we aren’t [training a model](https://www.blackhat.com/us-25/briefings/schedule/#training-specialist-models-automating-malware-development-46238) for this project, the gap between “mostly automated” and “fully automated” is huge. As such, the harness provides each POC to our team for manual review, followed by further automated testing. We found this collaborative approach to be significantly more straightforward.

### Validation

We used [GPT-4.1](https://openai.com/index/gpt-4-1/) to generate lateral movement POCs with the following prompts:

#### *System*

```
You are an expert Windows security researcher.

Your task is to analyze the provided example COM client code and generate similar working code for a different COM class with the same pattern.

Important guidelines:
1. Generate COMPLETE, WORKING C/C++ code - not templates or pseudocode
2. Include all necessary headers, imports, and dependencies
3. Use the exact CLSIDs, interface IDs, and type library GUIDs provided
4. Follow the same technique as the example
5. Add clear comments explaining each step
```

#### *User*

```
Generate working COM client code in C/C++ based on this information:

## Primitive Information
```
{
  "type": "trapped_object",
  "vector": "IDispatch → ITypeInfo → StdOle → StdFont → System.Object → Assembly.Load",
  "generation_hints": {
    "pattern": "IDispatch → ITypeInfo → Type Library → CreateInstance → Trapped Object",
    "critical_steps": [
      "Instantiate the target COM object remotely",
      "Get IDispatch interface and call GetTypeInfo",
      "Navigate to containing type library",
      "Find hijackable class (e.g., StdFont)",
      "Use ITypeInfo.CreateInstance to get trapped object",
      "Access .NET reflection through trapped object"
    ],
    "registry_requirements": [
      "AllowDCOMReflection=1",
      "OnlyUseLatestCLR=1",
      "TreatAs registry key for hijacking"
    ]
  }
}
```

## COM Class Details
```
{
  "clsid": "{2C941FC5-975B-59BE-A960-9A2A262853A5}",
  "prog_id": "IMAPI2FS.MsftFileSystemImage.1",
  "server_path": "C:\\Windows\\System32\\imapi2fs.dll",
  "is_dcom_enabled": true,
  "interfaces": [
    {
      "iid": "2c941fe1-975b-59be-a960-9a2a262853a5",
      "name": "IFileSystemImage",
      "has_idispatch": true
    },
    ...Other attributes and interfaces left out for brevity
  ],
  "referenced_type_libraries": [
    {
      "Name": "stdole",
      "GUID": "00020430-0000-0000-c000-000000000046",
      "Classes": [
        {
          "Name": "StdFont",
          "CLSID": "0be35203-8f91-11ce-9de3-00aa004bb851",
          "ServerType": "InProc",
          "ServerPath": "C:\\Windows\\System32\\oleaut32.dll"
        },
        {
      ...