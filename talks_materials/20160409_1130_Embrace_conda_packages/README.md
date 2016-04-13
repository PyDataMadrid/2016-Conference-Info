![PyData_logo](./static/pydata-logo-madrid-2016.png)

## SATURDAY 11:30–12:15
# [Embrace conda packages: the build system we always needed, but never deserved](http://pydata.org/madrid2016/schedule/presentation/4/)

### JUAN LUIS CANO RODRÍGUEZ
#### Audience level: Novice
## Description

Installation problems represent half of your mailing list traffic? Nobody in your team knows how to properly configure the Visual Studio compilers? Forcing your users to download a script full of "sudo" commands? Providing Docker containers and virtual machines as the only sane way to run your software? No more suffering or pain: create conda packages with conda-build and stop worrying today.

## Abstract

From my perspective, scientific software seems to have the more complex build processes ever imagined. The amount of compiled dependencies is overwhelming, even though many packages share a fair amount of them. Still, the landscape of building systems is simply terrifying, every team rolls its own alternative and in the end the only sane approach is to create an Ubuntu-like virtual machine just to run a particular software. The wonderful dream of reproducibility didn't involve debugging arcane CMake scripts at night, compiling PETSc in a million ways or installing everything in root locations just because search paths are hardcoded everywhere.

The idea of this talk is to make some fun at the current situation and try to put it to an end once and for all. conda-build looks like the solution we've always desired to build Python packages with compiled extensions, with its declarative nature and its clear separation of build and testing phases. Yet it is much more than that, since it provides a way to build packages which have nothing to do with Python, which I consider is the closest thing we have to a true cross platform package manager. Combined with cloud services like AppVeyor and Travis CI, we can create a build pipeline that creates cross-platform, relocatable conda packages for Windows, OS X and Linux.

Following my experience with FEniCS, Firedrake and Pyomo, we will also explore how to overcome some conda-build limitations and provide some ideas on how could the developers work them so it becomes the perfect build tool we have always wanted, but never deserved.

<img src="./static/aeropython_name_mini.png" alt="AeroPython" align="center" style="width: 300px;"/>
