OrientExpress for Kodi
==========


## Notice

Moved to [Codeberg](https://codeberg.org/evilwan/hamper) because of policy changes at Github (see
[Github notice](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13) )

Script for controlling some of the options provided by the ExpressVPN command line tool, from within Kodi. As such, this tool is merely a graphical interface for using that command line tool, it is not a replacement or addon.

Not all options of the command line tool are available through this Kodi addon, just some basic use cases are provided.

Note that this tool is in no way affiliated with, or endorsed by, ExpressVPN ([https://www.expressvpn.com/])

Geolocation information is fetched from https://ipinfo.io/json

The logo comes from a website with rights-free images (forgot which one: contact me if you feel that this is an error)

The country flags come from https://flagpedia.net/

The fanart image comes from https://images.wallpaperscraft.com/image/single/train_railway_bridge_122067_1600x900.jpg

Features
-----
- Start and stop ExpressVPN from with Kodi.
- Select VPN server (exit point)
- Display current geo-location.

Screenshots
-----
For now, please use your own imagination...

Prerequisites
------
This addon is merely a graphical interface for the ExpressVPN unix command line tool, so first visit the ExpressVPN website ([https://www.expressvpn.com/]) to download the installer of the command line tool for your operating system. Next install and configure the tool on the system where you run Kodi: verify that you have a working ExpressVPN tunnel before using this addon.

Installation
------
The quickest way is to download this repository as a ZIP file, then install the addon from that ZIP. See [http://kodi.wiki/view/HOW-TO:Install_an_Add-on_from_a_zip_file][1] for more details on installing addons from zip file. Just be sure that the ZIP file contains the directory script.orientexpress in its root (Kodi expects all files below directory "script." + the name of the Kodi addon)

If you want to create your own ZIP file, run shell script package_zip.sh from within the root directory of this repo. No special software is required: just a working bash and zip command line tool. As the addon is written in Python, there is nothing to compile or build.

Usage
------

The tool is rather self-explanatory. The following functions are available:

**Show the current VPN IP configuration

**Show a list of available VPN endpoints (exit servers)

**Connect to a specific endpoint

**Disconnect from VPN

**Connect to the last active VPN endpoint

For any other manipulation of the ExpressVPN setup, please use SSH to connect to your Kodi box and use the expressvpn command line tool.

Settings
--------

**expressvpncmd points to the ExpressVPN commandline tool
**printdebug controls verbose debug logging: set to true to activate the logging in kodi.log

FAQ
---

**Is this plugin available in a Kodi addons repository?** No

**I can't get the OrientExpress plugin to work on Raspberry Pi?** Before asking me for help I suggest reading the following [guide][1].

License
------

OrientExpress for Kodi is licensed under the 3 clause MIT license.

[1]: http://kodi.wiki/view/HOW-TO:Install_an_Add-on_from_a_zip_file
