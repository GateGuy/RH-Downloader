# RH Downloader

This is a Windows program that automatically downloads a patch from RomHacking.net or SMW Central and applies it to a copy of the correct rom on your computer with just a few key presses.

<img src="https://github.com/GateGuy/RH-Downloader/blob/master/screenshot.png?raw=true" width="480" height="715" />

## How does it work?
- Run the executable ("RH Downloader.exe") and follow the onscreen instructions to input the site of choice and patch ID, and it will download the patch, look in the user's rom folder for the correct rom, make a copy, unzip the rom (if necessary), verify the rom's hash codes using RHDN's online hasher (this can be disabled to speed up the process), apply the patch using an online patcher, and finally download the new rom (and optionally compress it in a ZIP archive). For example, if you wanted to download the Zelda 1 hack "Zelda Challenge: Outlands" (which has an ID of 10, found in the hack's URL), you would run the program and specify "RomHacking.net" (option #1) and an ID of 10.
- This program uses Python 3.6.4 and Selenium with a Chrome driver to open the necessary pages in Chrome. The Chrome driver is included in the release, and Python + all dependencies are wrapped in the executable via PyInstaller, so no setup is necessary, though you do need to have Chrome installed.

## Features
- Supports both hacks and translations.
- Compatible with any patch format that works with the online patcher (IPS, UPS, APS, BPS, RUP, PPF, xdelta, MOD).
- This program is designed to be quick and easy with no preparation on the user's part:
    - The original rom doesn't have to have the exact same name as listed on the original site (example: "Legend of Zelda, The - A link ToThe Past (U) [!]" will still be identified as "The Legend of Zelda: A Link to the Past").
    - The correct original rom will be auto-detected using both the original name and the name of the recommended rom (example: a hack of the Japanese version of Mega Man 2 will search for roms named similarly to "Mega Man 2" or "Rockman 2 - Dr. Wily no Nazo").
    - Console directories can be detected under several different names (example: "Super Nintendo Entertainment System" can also be "Super Nintendo", "SNES", "Super Famicom", etc.).
    - Searches through subdirectories in your rom folder (useful if you like to separate your roms by region, for example).
    - Original roms can optionally be stored as ZIP archives; you don't have to manually unzip a rom just to apply a patch.
    - The user can choose to save the patched rom as a ZIP archive instead of having to compress it themselves.
- The program will only ask for user input when necessary:
    - If it fails to find the original rom or rom directory, it will ask the user to type it in manually.
    - If a downloaded patch contains multiple patch files, it will ask the user which one to apply.
    - When downloading a translation, it will ask what the output should be named according to RHDN (which often has names in both the source and target languages).
    - The program can assume the answers to several questions so you don't have to answer those questions (for example, if the program only finds one matching original rom, it can assume that rom is correct without asking you). You can change what the program assumes in the config.
- Catches all errors that I could think of (giving an invalid answer to a question will re-ask the question, entering an invalid or empty ID will simply skip the ID, downloads will time out if they don't start within 8 seconds, and so on).

## FAQ
### Is this a rom downloader?
- No. This program does not download roms, nor does it refer to any means of obtaining roms. It only downloads a patch file and applies it to the appropriate rom on your computer. You are responsible for obtaining a legal copy of any rom you want to patch.
### Can I see what it looks like?
- Here's a video that shows the program being used to download and apply a patch: https://drive.google.com/open?id=1TP6Sdt6M2P7bKIedCnygu0x-ZanF6eyG. There's also a screenshot at the top of this readme.
### What does this access/affect on my computer?
- All downloaded files are stored in either the output folder (which is a folder named "output" in the same directory as the program) or a temp folder (which is stored in this same directory and is optionally deleted after the program is finished). This temp folder contains the downloaded patch (extracted if necessary) and a copy of the original rom from your rom folder. Other than that, all that is accessed on your computer is the original rom that will be patched.
### Does this support batch downloading (can I download multiple patches at a time)?
- To prevent excessive traffic toward the compatible sites, batch downloading is not supported. You can still run the program once for each patch you want to download.
### While running the program, I got a popup from Windows Defender Firewall.
- This only happens the first time you run it (and if you move/rename it). It's trying to open Selenium, which is used to access Chrome. Just click "Allow Access" and it'll work.
### Are there configurable settings? How do I change them?
- User config can be found in the included downloader_config.py; just open it with a text editor. You will need to set your rom folder (example: "D:/Roms") in this config. If you want to restore the config to default settings, just delete it and restart the program.

## Known issues
- Does not support large disc-based systems. It uses an online auto-patcher to apply patches, and discs are too big for it to handle (at least from what little testing I've done with disc-based games).
- Does not support hacks that require you to apply multiple patches to one rom (very few hacks do this).

I hope this makes the process of getting rom hacks a lot faster!
