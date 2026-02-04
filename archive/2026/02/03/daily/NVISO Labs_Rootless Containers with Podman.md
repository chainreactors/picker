---
title: Rootless Containers with Podman
url: https://blog.nviso.eu/2026/02/03/rootless-containers-with-podman/
source: NVISO Labs
date: 2026-02-03
fetch_date: 2026-02-04T04:06:22.101353
---

# Rootless Containers with Podman

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

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

# Rootless Containers with Podman

[Dimitris Vagiakakos](https://blog.nviso.eu/author/dimitris-vagiakakos/ "Posts by Dimitris Vagiakakos")

[Application Security](https://blog.nviso.eu/category/application-security/)

February 3, 2026February 3, 2026
11 Minutes

![](https://blog.nviso.eu/wp-content/uploads/2026/01/Rootless_Containers_BP_Dimitris-1-1024x535.png)

In modern digital infrastructure, containerization has become one of the most significant technologies, offering automation, portability, and resilience of services across cloud and on-premises environments. Containers can simplify backup processes and enhance upgrade safety while significantly reducing recovery times following system incidents or failed updates.
This article provides an overview of the container technology and focuses on Podman, a modern, daemonless container engine. Podman serves as the primary, Red Hat supported container solution in Red Hat Enterprise Linux and is widely available across major Linux distributions such as Fedora, Debian, Ubuntu, Arch, and SUSE.

Podman offers several features, including the ability to run containers without requiring root permissions on the host. This article will explore Podman’s security benefits, how it technically differs from other popular container engines such as Docker and practical ways it can be used to harden a company’s infrastructure built on it.

## **Overview of Containers and Their Security Implications**

Containers represent a complete runtime environment for applications, packaging code, libraries, settings, and other userland dependencies into isolated “boxes” that behave consistently across different platforms while sharing the host’s kernel rather than running their own.
This isolation reduces the risk of system-wide dependency conflicts and simplifies deployment pipelines.
By using a simple YAML file to define multiple containers, system administrators can design and manage their own services and maintain them securely, making backups and migrations easier as the application data typically resides in volumes or external storage (such as databases or object storage) that can be backed up independently of the container images reliably.
For example, a container can “contain” an operating system (but uses the host’s kernel), a service (e.g. a web server), a database, or even an entire application.

```
#Template of a Compose YAML file for both Podman and Docker with nginx web server
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:Z
```

```
#Template of a Compose YAML file for both Podman and Docker with nginx web server
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:Z
```

Traditional GNU/Linux software installation often includes manual dependency management which can lead to broken applications after system upgrades. Many newer software versions require specific library versions and other dependencies, making updates more difficult. As a result, many companies run older legacy servers with outdated operating systems, increasing their attack surface.
Containers mitigate these side-effects by segregating the application’s environment from unintended external factors or dependencies. The designed segregation enables operators to manage the desired state (apply or roll-back updates), thus improving company’s patch management while reducing the overall risk posture.

## Core Container Architecture

As discussed previously, containers are built from images that package everything needed to run applications, such as web servers, Linux distributions, or databases. Key components of container architecture include:

* Image download and verification processes, to ensure integrity,
* Storage volumes, mapped to host directories for persistent data storage,
* Network port bindings that enable controlled communication between containers and external systems,
* Assignment to dedicated virtual networks for segmentation and isolation,
* Unique container identifiers used for policy enforcement, monitoring, and auditing purposes,
* Optional resource limiting features that help manage container resource usage and ensure host system stability.

As containers use images containing everything needed and volumes store application data separately, this approach helps system administrators back up volumes and move them to other systems with reduced downtime, easing migrations, especially when the applications and the orchestration are designed to support such changes.

If an image supports multiple architectures (such as x86\_64 and ARM), pairing the volume with the correct architecture-specific image ensures the service remains fully functional. This allows services to run smoothly across different hardware platforms without compatibility problems.
Administrators can dynamically reconfigure container networking, increase storage by attaching new volumes, and upgrade by replacing images, supporting effective vulnerability and lifecycle management.

#### Disk Management and Backups

For instance, if a container runs out of space, an administrator can provision and attach additional storage as a new volume and then migrate data with minimal downtime, provided the filesystem, orchestration, and the application itself support such changes, typically requiring less effort than resizing or adding virtual disks to traditional virtual machines.
Multiple disks can also be used as backups. Backup tools such as rsync or tar compression ensure rapid recovery while preserving data integrity. Volumes for simpler or low-traffic services can be backed up by creating tar archives that maintain permissions and ownership, especially for smaller solutions. Administrators can quickly switch disks by updating volume mappings with limited downtime.

#### Upgrading Containers

When upgrading software, companies can design their application data formats to be architecture-agnostic, so that new container images can reuse existing volumes across different platforms, making upgrades smoother. If problems occur after upgrading, as has already been discussed, it is simple to roll back to a previous image and restore the prior state.
These rapid rollback capabilities and isolated environments increase resilience against cyberattacks, protecting legacy s...