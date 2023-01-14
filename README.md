<img src = "/AIR_CURSOR.png" alt="aircursor" align="center" width="900" />
<img alt="GitHub repo file count" src="https://img.shields.io/github/directory-file-count/vrag99/Air-Cursor">

# About Our Project

Hey there ! You are reading about our first ever project , AIR CURSOR.

It is our approach towards promoting lethargy XD.
You just need to raise your finger to control your computer.

Seriously though, you can point ,click ,zoom in/out, minimize maximize the windows and even control the volume of the system.

It also has a privacy feature to safeguard your Content from the peeping toms of this intruding world.
## How we made it
Python is the only language that we used in making this project( let's keep it simple shall we ? )

The modules that we used include OpenCV, Mediapipe , PyAutoGUI, numpy, pycaw, multithreading along with the included modules.

All of us made separate functionalities of the cursor which were then incorporated into a main file. The privacy feature of the project was implemented as a Daemon process, which required us to use multithreading module.

We collaborated on the project using Github and Git, which was a first experience for us.
Not to mention that we did not know how to run a simple for loop a week ago in python.

## Challenges Faced

This is a good time to mention that we tried using multiprocessing as well so as to improve the performance of the cursor but were unable to do that as the code initialised Tensorflow recursively, which made it even slower.

We were not able to make the code more modular because of multiple infinite loops.
