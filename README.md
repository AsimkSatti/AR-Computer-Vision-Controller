# AR-Computer-Vision-Controller
How to control an Agumented Reality enviroment in Unity with Python's Computer Vision Library

Creating a truely all miniputable AR enviorment.
Using Unity,Voforia's tracking capabilites are amazing, however very limiting 
if you would like to pass the boundries on what you can track, or how you can display your obj, making your AR seem 
almost cinematic with essentially no limits then this is it.

I leave the creativity to you, but this code is designed in mind that you already have OSC and the folders correctly 
installed in Unity. If not go here ->https://github.com/jorgegarcia/UnityOSC

All the python modules are accessible through pip, the game enviroment and Computer Vision algo can run simultaneously but not simultaneosly withthe AR camera
*only one program per camera

Run your python program after starting your AR in Unity

The example I did found the center of my face or multiple faces and moved my 3D Objects on top.

You can track or match anything you can with cv2's Computer Vision library to then Superimpose or interact with your enviroment
Try chnaging out the haarcascades, or see what you can minipulate with other objects


Modulator must be inside your OSC folders and then attatched to the OBJ
The data would likely have to be scaled down to a factor where the values are meaningful in your Modulator
Use the OSCHelper to track messages and debug.log in the console
 
Coming: Interactivity with objects and enviroment with single camera
