# RadianceEquirectangular

This repository presents a script with which one can render [Radiance](https://www.radiance-online.org) equirectangular luminance-based images using the rtrace command.

This work is built upon the workflow presented by [Dion Moult](https://thinkmoult.com/create-360-vr-panoramas-with-radiance.html) using the modified version of .cal file created by [Mark J. Stock](http://markjstock.org/).

![sphere2](https://user-images.githubusercontent.com/47574645/140939877-2a10de78-d97a-4a97-a885-effacf5d4054.jpg)
*Equirectangular synthetic HDR image of an office rendered by Radiance using this method, source: [Author](https://github.com/maqorbani)*


Please note that this script works with MacOS and Linux systems. However, bear in mind that you can still employ [Linux kernel-WSL](https://docs.microsoft.com/en-us/windows/wsl/install) on a Windows machine to render your desired images. Moreover, this is the recommended solution for Windows renderings since rtrace command only supports single-core process on Windows.

Also note that the Radiance software must be installed on the system in /usr/local/radiance directory.


## How it works
## Method 1 (using default values):

Substitute your .rad file for Geo.rad and your Octree file for render.oct files in the root directory. To initiate the rendering, simply run main.py by calling: python3 main.py

## Method 2 (using command line arguments):

The command line options are as follows:

-o set the Octree file 

-r set the Rad file

-n set the number of CPU cores for rendering

-x set the x resolution. the y resolution is always the x resolution divided by 2

-p set the camera's position. This option is followed by three floats that are: X, Y, Z positions

--quality set the quality preset. Options are: LOW, MEDIUM, HIGH

--mesh set the mesh detail preset. Options are: LOW, MEDIUM, HIGH

--lvar set the light value variance variability preset. Options are: LOW, MEDIUM, HIGH

--indir set how indirect the lighting is in the rendering. Options are: 1, 2, 3

--output set the output file name. 

example: 

python3.10 main.py -o render.oct -r Geo.rad -p 5.00 3.00 1.50 -n 4 -x 2048 --quality HIGH --output out.HDR
