'''
RH Downloader: Version 1.0

To restore options to their default settings, delete this file and run the
downloader.
'''

# -- MAIN SETTINGS --

'''
The directory that holds your platform folders (NES, SNES, etc.)
If you don't store your roms with this type of folder organization, then when
you try to download a patch, the program will ask you to
manually type your rom directory
'''
romFolder = "D:/Roms"

'''
Do you want to compress the output rom into a zip file? (True or False)
'''
zipOutput = True

# -- PREFERENCES --

'''
Do you want to verify that the original rom has the correct hash codes before
attempting to patch it? (only for patches from RHDN) (True or False)
Disabling this will speed up the program, but it may patch the wrong rom if
your copy isn't exactly what the patch wants.
'''
verifyRom = True

'''
If the original rom does not pass verification, do you want the program to ask
if you should attempt to patch it anyway? (True or False)
'''
allowFailedVerify = False

'''
When searching for the original rom in your rom folder and the program detects
exactly one match, do you want that match to automatically be chosen? Or should
the program ask you if that rom is correct? (True or False)
This can speed up the program (it's one less question you have to answer), but
it may patch the wrong rom in rare situations.
'''
forceSingleMatch = False

'''
When downloading a translation, and names in both the source and target
languages are found (example: "Kirby no Kirakira Kizzu" and "Kirby's Super
Star Stacker"), do you want to name the patched rom under the first name found,
or do you want to be asked which name matches your language? (True or False)
This is required since there is currently no standard for whether the source
language is listed first and the target language is second, or vice-versa.
'''
assumeFirstNameInTranslation = False

'''
Delete the temp folder when the program finishes? The temp folder contains a
copy of the original rom and the extracted patch. (True or False)
'''
deleteTempFolderAfterCompletion = True

# -- ADVANCED SETTINGS --

'''
The URL for the online rom patcher. You shouldn't have to change this, but if
this site ever goes down for some reason, you might be able to use a different
online patcher (like https://www.romhacking.net/patch/).
'''
patcherURL = "https://www.marcrobledo.com/RomPatcher.js/"

'''
The URL for the online rom hasher.
'''
hasherURL = "https://www.romhacking.net/hash/"

'''
Do you want to be able to see the browser window as your patch is downloading
and being applied? (True or False)
'''
showBrowser = False

'''
The location of the Chrome web driver. This script should come with a Chrome
driver, but if it doesn't work (maybe Chrome is updated in the future and this
version stops working), you can add the location of your own driver here, or you
can replace the old Chrome driver with a new one. ("" = Default)
'''
driverLocation = ""

'''
Create Chrome driver log for debugging? (True or False)
'''
verboseDriver = False