# RadianceEquirectangular
This repository presents a script with which one can render [Radiance](https://www.radiance-online.org) equirectangular luminance-based images using the rtrace command.

This work is built upon the workflow presented by [Dion Moult](https://thinkmoult.com/create-360-vr-panoramas-with-radiance.html) using the modified version of .cal file created by [Mark J. Stock](http://markjstock.org/).


![sphere2](https://user-images.githubusercontent.com/47574645/140939877-2a10de78-d97a-4a97-a885-effacf5d4054.jpg)
*Equirectangular synthetic image of an office rendered using this method, source: [Author](https://github.com/maqorbani)*

Please note that this script works with MacOS and Linux systems. However, bear in mind that you can still employ [Linux kernel-WSL](https://docs.microsoft.com/en-us/windows/wsl/install) on a Windows machine to render your desired images. Moreover, this is the recommended solution for windows renderings since rtrace command only supports single-core process.

Also note that the Radiance software must be installed on the system in /usr/local/radiance directory.
