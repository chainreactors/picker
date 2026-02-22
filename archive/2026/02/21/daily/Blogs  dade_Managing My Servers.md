---
title: Managing My Servers
url: https://0xda.de/blog/2026/02/managing-my-servers/
source: Blogs  dade
date: 2026-02-21
fetch_date: 2026-02-22T04:10:08.084562
---

# Managing My Servers

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2026/02/managing-my-servers/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

7 minutes

# [Managing My Servers](https://0xda.de/blog/2026/02/managing-my-servers/)

I’ve been spending a fair amount of time building out documentation around my home network as well as my various services I’m running on the internet. Drawing architecture diagrams, mapping out what services are on which servers, documenting backup processes for each service, that sort of thing. But one thing that I keep coming back to is trying to understand the criteria for my perfect server. Sure I have TrueNAS running my storage server, and it’s great at what it does. But what about the compute?

Professionally, I’ve long been an advocate of the “Servers are cattle, not pets” mentality – though maybe I’d like to figure out a better way to express this. But the idea is that no server should be a snowflake, and that servers should be easily disposed of and replaced. This seems to be the underlying mentality powering the rise of Kubernetes, which does a great job at decoupling the workload from the underlying server.

## Kubernetes

Kubernetes, though, is a matryoshka doll of complexity. Under every stone is another layer of complexity to manage. Plus, while there are various projects like Flux to enable gitops for kubernetes, a lot of the workflows seem to be heavily based on running commands to install software. `helm install <blahblahblah>`. Everything is configured with yaml files everywhere, which makes me feel like it’s reasonably declarative. Yet still the seemingly standard process is “just helm install it, bro.” So it becomes easy for a cluster to quickly separate from a purely declarative abstract machine, and instead it accumulates a bunch of state. Which is okay because it’s made up of multiple nodes and the state has some consensus mechanism and redundancy so that any node failing is considered safe. But it just feels too imperative to me. Too much like managing an Ubuntu VM, but with way more moving parts.

Fundamentally, Kubernetes solves a bunch of problems that I want to care about. A bunch of problems that I do care about, at work. Load balancing, horizontal scaling, security policies, everything is a container. Neat. But at home, it kind of sucks. There’s a bunch of complexity, a bunch of imperative configuration, and the gitops workflow feels pretty clunky and slow. This might be a user error, so if you love gitops for kubernetes, please write a rebuttal and send it to me. I would genuinely love to be better educated on it.

That doesn’t even hit on one of my most important things – managing a k8s cluster is an added layer of complexity on top of managing the underlying nodes. So you still need to make sure the underlying nodes are updating regularly, have access secured, offload the logs to centralized logging, etc. One promising candidate to relieve this overhead is [Talos](https://www.talos.dev/), a very minimal operating system designed purely for running kubernetes. Managing talos nodes is, again, imperative. You run commands to update things. But if you’re already going all in on kubernetes, Talos does seem like a really nice way to minimize attack surface and alleviate overhead around patching and access control. I have a 4-node Talos cluster in my closet right now.

## NixOS

So then I think, maybe I should just install NixOS on all my servers. I really like the declarative nature of Nix, and if you do it right you can pretty easily decouple services from servers, allowing you to redeploy a service to any of your servers, or deploy it in parallel to multiple of your servers. But you don’t really get any sort of scaling with this, and keeping services available is a bit harder and more manual. Plus, if I’m being brutally honest, the [dependency management story for NixOS kind of sucks](https://jade.fyi/blog/pinning-packages-in-nix/). Pinning a package to a specific version is difficult. Stable can quickly get out of date, and unstable is often some random release candidate. While you can absolutely override versions for individual packages, it’s definitely not very intuitive and it is either a lot of overhead, or has a high risk of breaking randomly in the future. I would love something more like python’s dependency declarations for packages. The package namespace in nixpkgs seems globally unique, so in theory I should be able to just do `listmonk~=6.0` and have a high degree of confidence that redeploying gives me the latest version but without going up to `7.0`. I understand why NixOS doesn’t have this, but I can still wish.

Plus, running containers on NixOS is an interesting situation. You can enable docker, but it doesn’t seem like you can very easily define which containers you want to launch. I’d love to be able to just point NixOS at my docker compose files that I already have, and have that get built into the next deployment. It handles the restart conditions, the container dependencies, etc. Many people will say that you don’t need docker if you’re using NixOS because it achieves many of the same goals. That’s totally fair. Except I already have a bunch of docker compose files, and most of the apps I want to install ship with a docker compose file, very few of them ship with a nix file I can just import. There are tools like [compose2nix](https://github.com/aksiksi/compose2nix) which can take a compose file and output nix files, which could meet my needs, but then I’m introducing this intermediary tool anytime I want to deploy a new service, and that just feels kind of clunky.

Maybe the answer here is that I need to go all-in on NixOS and just configure my services entirely as Nix and accept the adoption costs as one-time costs to get things configured. I mean, I’m still kind of at the mercy of nixpkgs configurations, but it’s a git repo and if something sucks, I can just open a PR to improve it. But this high adoption cost combined with the kinda bad dependency management experience does make me reconsider if this is the route I want to go. I do appreciate how tightly nix flakes are integrated with GitOps, and I also appreciate the NixOS configuration management story (certainly more than configuration management on ubuntu or any other operating system that isn’t designed to be completely declarative or completely ephemeral).

## CoreOS

There’s another option, one I haven’t experimented with so I can’t speak first hand to it yet, but that looks somewhat promising. That is [CoreOS](https://fedoraproject.org/coreos/), a container optimized operating system. It is a minimal operating system that auto-updates. Pretty easy to treat this as a dumb and ephemeral underlying operating system. My first introduction to CoreOS was a post by Thomas Letan called “[I cannot SSH into my servers anymore (and that’s fine)](https://soap.coffee/~lthms/posts/i-cannot-ssh-into-my-server-anymore.html)”, and it looks fairly promising.

But the caveat with this is that it has a similar problem to the NixOS problem – I pretty much will always have to translate service definitions into podman’s quadlet syntax. Updating containers would have to be entirely manual, since [Dependabot does support docker-compose](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories) but doesn’t support podman-quadlet. While I don’t necessarily want every container to automatically update, I would like to have a better solutio...