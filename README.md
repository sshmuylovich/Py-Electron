# Py-Electron

This library is based on the strong need for an easy-to-use GUI creation option in Python. 

## Existing Frameworks
### PyQT
PyQT is an awesome framework but has its limitations when scaled up to larger projects. Being based off the Qt framework, PyQT beats Electron in raw speed and efficiency. Furthermore, [Electron uses nearly 4x the RAM as PyQT](http://roryok.com/blog/2017/08/electron-memory-usage-compared-to-other-cross-platform-frameworks/). Additionally, Electron app installs often bundle the Chrome download, making them far larger than Qt app downloads. And last off, Python is far more secure than Javascript. Open-source libraries like PyArmor have world-class security (with PyArmor having no good unpackers available to the open internet as of 3.6.0). Most open source javascript code can be easily deobfuscated. For instance, the widely used Obfuscator.io has been unpacked multiple times, a notable example of which is [Sd's unpacking repository](https://github.com/sd-soleaio/deobfuscator-io) 

PyQT, however, has two marked disadvantages to Electron: firstly, it's not as easy to make visual changes to a PyQT program. Electron, however, accepts UI changes in HTML/CSS, meaning you don't need extensive knowledge of Qt to make small changes to an application's graphics. With Electron, you can make use of countless examples of Javascript or CSS widgets online, whereas in PyQT you mainly have to recreate them yourself due to a lack of community support and existing examples. Secondly, PyQt is difficult to package. PyInstaller is an easy option, but it depends on the build machine's c binaries when compiling, which leads to heavy issues with earlier operating systems. The authors of f-man, a Python packaging library, claim that in Python, "Packaging, code signing, installers, and automatic updates require months of work." Lastly, PyQT requires a commercial license that can cost up to $550 per developer. In StackShare's ranking of GUI frameworks, PyQT has 58 followers whereas Electron has 4,500. The vast majority of third-party Desktop apps (Discord, Slack, Atom being a few examples) use Electron whereas few commercial and widely-distributed apps use PyQt.

### Tkinter
 Tkinter, although one of Python's most commonly used frameworks, has been criticized for its lack of support of modern graphics and extensive CSS, both things which Electron allows developers to work with.

## The Need for a Python Solution
This library is aimed at creating an alternative to Electron that works seamlessly in Python, allowing Python developers to not need to learn Electron in order to build cross-platform desktop apps. Furthermore, its usage of users' local Chrome install means that PyElectron apps will require far less space than traditional applications. 
