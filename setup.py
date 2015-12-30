import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "djinn",
    version = "4.0.0",
    author = "Shreyas Iyer",
    author_email = "shreyasiyer14@gmail.com",
    description = ("A 3D game engine built using pygame and opengl."),
    license = "MIT",
    keywords = "3dgameengine engine opengl",
    url = "http://packages.python.org/",
    packages=['djinn','djinn/scenes/textures', 'djinn/scenes/sample_textures/', 'djinn/scenes', 'djinn/player', 'djinn/window/', 'djinn/scenes/shapes', 'djinn/physics'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
