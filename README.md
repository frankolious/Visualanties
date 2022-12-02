# Visualanties <img src="https://user-images.githubusercontent.com/1236067/205092392-d81a75fd-4482-4d4e-854c-d7b73756e1d2.png" width="160" height="160" />

###LAZER LIGHT ACTION PROJECTION - Code/ Temaples/ Gists/ Automations/ Shaders/ Generative Audio Reactive Worlds all live here!
![AFRIKABURNcropped](https://user-images.githubusercontent.com/1236067/205002357-3910cf35-f13c-48f5-ad45-14173a075a74.jpeg)


### A microservice setup for visual artists to create content and pull and prepare useful information to help them better plan events
### Trunk Based Dev (main only) not branching, Super fast CI for building new tek into production.
### this is the model for no more PULL and Merge request.

## lets stay AGILE!

![ ] not done

![x ] done

# Advice On Multi-Repo CI/CD

Published Thursday February 23, 2017. 


A Scrum.org colleague asked for advice on what to think of when helping someone with Continuous Integration (and later Delivery/Deployment). In this case, the person had experience from one team and one source code repo (or very limited set of repos), but was keen to hear about what might (context is king) be the case for multiple teams, multiple repos. Here’s my quick brain dump reply.

There’s a number of questions one could ask, somewhere between 15 and 50 …

Where’s the source hosted? (GitHub? On Prem?)
Dockerized? Modularized or is the final application a big monolithic unity? (Can you deploy and upgrade parts of the full system, without having to take down all of it)
What does deployment look like?
Where are component tests defined (combination of binaries from more than
What tech are we talking about, Apple things (requring Xcode licenses for CI infra), cross platform (win, linux, mac, …), cross architecture (32, 64-bit, MIPS, ARM, …)?
How do they handle versioning today? Semantic versioning? Separate API and ABI versions?
Are they sane around futureproof and backwards compatibility around their APIs? (Ie where the different repos actually meet in runtime)
How many versions of the system do they need to live with - are they in control of all runtime environments where the product is alive, or do they ship to customers that install themselves and can choose for how long? (This can really complicate things.)
Are they doing https://trunkbaseddevelopment.com/ or are they maintaining a business model, with many branches? Do they fix bugs by copy-pasting of the same code on those branches, …
What is their current level of build and test automation?
Where do they store cross-component tests?
How do they handle testdata?
How do they handle their CI and test and prod and other environments? Infrastucture as Code? (“Version control everything”)
How do they handle production data?
What is their thinking around risk / cost ratio for product quality / testing activities and confidence level in their system when the put it into production?
Do they branch by abstraction (with some form of feature toggles) or is there only one version of everything?
Do they need to run A/B testing? Dark launching? Canary?
What monitoring is in place, in test, CI and production …
How do they handle binaries today?
What are their current success ratio in their CI build steps - as you combine repos/artifacts, your quality multiplies meaning that 90% successful commit ratio on 5 repos combined makes your CI setup will be RED ~35% of your time. That’s not good for being able to get things through quickly. Don’t take this lightly, or you end up with the “emergency mode” Nexus Integration Team doing nothing but chasing people down to fix bugs.
What information radiators are in place? What communication channels are setup between teams? (How many teams and repos are we talking about?)
What’s the actual business need(s) - is this all just for fun? :-)
Rules / Principles to Apply

build once => you only pass down binaries downstream to the consumers, may be packaged things like *.jar, *.deb, *.rpm, zip/tar.gz/… (yuk - these has no “real”, useful metadata)
version control everything, ie how your CI environment is set up, how each build step is set up
look at Jenkinsfile (if you have to - simple, stupid solutions)
look at Gocd (if you have to - artful, complex solutions)
Good luck, and whatever you do - iterate over the solution and add to it incrementally!

/ [Fredrik @](https://fredrik.wendt.se/2017/02/23/advice-on-multi-repo-ci-cd/)

