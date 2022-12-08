 <img src="https://user-images.githubusercontent.com/1236067/205092392-d81a75fd-4482-4d4e-854c-d7b73756e1d2.png" width="160" height="160" align="centered" />

 # Visualanties [![.github/workflows/main.yml](https://github.com/frankolious/Visualanties/actions/workflows/main.yml/badge.svg)](https://github.com/frankolious/Visualanties/actions/workflows/main.yml) [![open in collaboratory](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/frankolious/Visualanties/blob/main/getting_started_with_Visualanties.ipynb) [Open Figma Ideas ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)](https://www.figma.com/file/bYTNJkb8p1iBB3xUQnBK4u/IDEA-GENERATION?node-id=1%3A322&t=CW35bxcjSYKEAfOM-1) 


### LAZER LIGHT ACTION PROJECTION - Code | Temaples | Gists | Automations | Shaders | Generative Audio Reactive Worlds all live here!
![AFRIKABURNcropped](https://user-images.githubusercontent.com/1236067/205002357-3910cf35-f13c-48f5-ad45-14173a075a74.jpeg)



_This is for visual artists, live performers and event organisers to create content and pull and prepare useful information to help them better plan events._

#### Advice On Multi-Repo CI/CD


This will probably be a baby monolith with async API services fragmented in from the edge ESI. SSR services for the monolith. Think FastAPI.




<hr>


###  Build out Scaffolding to be containerized
- This is a cloud based development environment.
###  [Collaboratory](https://github.com/frankolious/Visualanties/blob/main/getting_started_with_Visualanties.ipynb)

 - fire it up [![open in collaboratory](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/frankolious/Visualanties/blob/main/getting_started_with_Visualanties.ipynb)

### Github Codespaces


Build out python project scaffolding

* [makefile](https://github.com/frankolious/Visualanties/blob/main/Makefile)
* [requirements.txt](https://github.com/frankolious/Visualanties/blob/main/requirements.txt)
* virtual environment venv
    * python_library
* Dockerfile
* Command-line-tool
* Microservices

1. Create a virtual enviroment, 
 - this eliminates you having conflicts with whatever system you are running.
2. Edit ~/.bashrc   
    - this invokes the virtualEnv but calling venv/bin/activate from the ~/.bash (bourne again shell)
3. 
4. 

will try add a badge that automates all of this later

### AWS CLOUDSHELL / LINODE


### Command-Line Tools

### Microservices

### Containerized Continous Delivery

<hr>

## lets stay AGILE! [figma Project IDEAs ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)](https://www.figma.com/file/bYTNJkb8p1iBB3xUQnBK4u/IDEA-GENERATION?node-id=1%3A322&t=CW35bxcjSYKEAfOM-1) 

![THINGS TO START SEEING THIS WHOLE PICTURE](Planning/IDEA%20GENERATION.jpg)
[ x ] KANBAN BOARD - i tried to group ideas or features or whatever they are by colour. Its more about ideas then sorting.




### The Rendering Context
The _canvas_ is initially blank. To display something on the canvas element, we have to use a scripting language. This scripting language should access the rendering context and draw on it.

The canvas element has a DOM method called getContext(), which is used to obtain the rendering context and its drawing functions. This method takes one parameter, the type of context 2d.

The following code is to be written to get the required context. You can write this script inside the body tag as shown below.

On executing, the above code will produce the following output −


For more example on HTML-5 2D Canvas, check out the following link HTML-5 Canvas.

### WebGL Context
HTML5 Canvas is also used to write WebGL applications. To create a WebGL rendering context on the canvas element, you should pass the string experimental-webgl, instead of 2d to the canvas.getContext() method. Some browsers support only 'webgl'.

On executing, the above code will produce the following output −

<hr>

A Scrum.org colleague asked for advice on what to think of when helping someone with Continuous Integration (and later Delivery/Deployment). In this case, the person had experience from one team and one source code repo (or very limited set of repos), but was keen to hear about what might (context is king) be the case for multiple teams, multiple repos. Here’s my quick brain dump reply.

There’s a number of questions one could ask, somewhere between 15 and 50 …

Where’s the source hosted? (GitHub? On Prem?)
Dockerized? Modularized or is the final application a big monolithic unity? (Can you deploy and upgrade parts of the full system, without having to take down all of it)
What does deployment look like?
Where are component tests defined.

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
version control everything, ie how your CI environment is set up, how each build step is set up look at Jenkinsfile (if you have to - simple, stupid solutions) look at Gocd (if you have to - artful, complex solutions)

/ [Fredrik @](https://fredrik.wendt.se/2017/02/23/advice-on-multi-repo-ci-cd/)

# AUTOMATING DOCUMENTATION
## Conversion
To enable the combination of documentation in different formats to ease management and rendering, you might need to convert to create a unified format.

[Pandoc](http://pandoc.org/) - One of my favorite tools. Converts between a wide variety of markup formats, but no API specification formats.

[Swagger2Markup](https://github.com/Swagger2Markup/swagger2markup) - Converts Swagger to AsciiDoc or Markdown.

[API Spec Converter](https://lucybot-inc.github.io/api-spec-converter/) - Converts between Swagger (V1 and 2), Open API 3, API Blueprint, RAML, WADL, and others.

[apib2swagger](https://github.com/kminami/apib2swagger) - Converts API Blueprint to Swagger.

[swagger2blueprint](https://github.com/apiaryio/swagger2blueprint) - Converts Swagger to API Blueprint.

[Apimatic Transformer](https://apimatic.io/transformer) - Converts between a wide variety of specifications including Postman.

[apiary2postman](https://github.com/thecopy/apiary2postman) - Convert API Blueprint to Postman.

[Blueman](https://github.com/pixelfusion/blueman) - Convert API Blueprint to Postman.

[apib2json](https://github.com/o5/apib2json) - Convert API Blueprint to JSON.

## Transclusion
Transclusion is a term that I use to mean including the contents of one document in another. You might call it linking, inclusion, cross-referencing, or something else. But for our purposes, it will be how we include a variety of sources of information (API references and linking explanatory text) into a series of files for rendering. Many markup languages will do this for you by default, while others will need 'encouragement'.

Markdown doesn't include other files by default, but you have options with 

[hercule](https://github.com/jamesramsay/hercule), 
[MultiMarkdown](http://fletcher.github.io/MultiMarkdown-5/transclusion.html) or, as part of your rendering pipeline, a static site generator like Jekyll.

[Asciidoctor](http://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#include-files) is a widely used toolchain for Asciidoc seamlessly handles including other sources.

[reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/directives.html#including-an-external-document-fragment) can include external files by default.

If you want to enter the topic-based world, then dita includes cross-referencing for code and text. Docbook has text objects and includes.

Planning is all part of the puzzle
How far can we push the browser.
can we take on some of the processing leg work?
can canvas cooK?
[D3js](https://d3js.org/)
[threejs](https://threejs.org/examples/#webgl_instancing_performance)
gave us 10000 instnaced suzanne monkey heads  with 1 gpu call at about 25=60 frames. BUt yes its all code. maybe the worlds and everything we do here needs to be code only
[cable.gl] webgl live coding editor
[undev](https://interactiveimmersive.io/blog/technology/why-you-should-check-out-cables-gl/)

undev is a Berlin / Cologne based development and design studio for interactive experiences using modern web technologies. We push the boundaries of what’s possible using WebGL, Web Audio and WebVR.
