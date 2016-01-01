#DJINN-IV Game Engine. 
![Build] (https://travis-ci.org/djeof-1/DJINN-IV.svg?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/ce4e118f40f94c3f81a26ba3204cea61/badge.svg)](https://www.quantifiedcode.com/app/project/ce4e118f40f94c3f81a26ba3204cea61)
![License](https://poser.pugx.org/pugx/badge-poser/license?format=plastic%22%3E)
<br />
![Image](https://avatars1.githubusercontent.com/u/13732949?v=3&u=9e161249d86f665b78a1da2194ac28258f086e70&s=140)
<br />
##About DJINN
DJINN IV is a full-fledged 3D game engine, built with OpenGL and Pygame, for Python programming language (Python 2.7 is supported at the moment. Further support will be introduced in future releases) . DJINN IV is a relatively easier to use engine compared to others available in the market, because not only Physics is taken care of for your game, but also other event handling, graphical rendering, textures, and loads more. DJINN IV has a new algorithm for collision detection, to make it seem as realistic as possible, but still to be implemented. This engine, with decent 3D game graphics, is heavily suitable for FPS, SPS, and TPS, as well as MMORPG, and others.
<br />
##Why DJINN? <br />
 Now, we know that there are plenty of professional-quality engines available in the market right now, and that too for free (Consider UDK, Cocos-2Dx, Box2D, etc.) But, the problem is that these engines mostly target C,C++, JavaScript, or HTML5. Very few engines actually are totally built in, and support Python. Also, the engines which are built have a bit cryptic source code, which makes it difficult for the novice developers to contribute to. But, DJINN being totally built using Python, Pygame, and PyOpenGL, makes contributing easier, because of clean organization of source files, and cleaner syntax (Python!). This helps in overall maintainance of the code, as well as makes the bug tracking easier. <br />
 
Considering the small size of the entire engine, it is a nifty tool that can help save you hours of time. Low level integration is on our TODO list, and soom in future releases, it will be implemented. Hardware acceleration will also be implemented. 

  DJINN-IV is an open source game engine, and contributers are welcome to help make DJINN one of the most desirable tools for game developers and enthusiasts.
  
<b><u>REQUIREMENTS:</u></b>

1) Pygame <br />
2) PyOpenGL <br />
3) PyOpenGL accelerate
  
<br />
<b><u>INSTALLATION:</u></b>
<br />

1) Download the repository as a .ZIP file, and extract it somewhere. Open up the terminal, and change your working directory to the extracted folder. Now, in the terminal type: <br />`chmod +x PRE-INSTALL.sh`<br/>`./PRE-INSTALL.sh` <br />

2) The above commands install the necessary dependencies on your system, for the engine to work upon. <br />

3) Next, you have to install the game engine onto your system, so as to make it work globally. For this, type in the following command in the terminal: <br />
`sudo python setup.py install`<br />

4) This will install djinn on your system, and now it is ready to use. Check the test/example files, in 'tests' folder, to learn about how DJINN actually works,and how to make it work.


