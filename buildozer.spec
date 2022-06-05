[app]

# (str) Title of your application
title = Kulife

# (str) Package name
package.name = kulife

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = txt,jpeg,py,png,gif,ico,jb,zip,otf,eot,scss,svg,ttf,woff,woff2,css,js,html,jpg,kv,atlas,db,ini,mp3,wav,xml,docx,html,rels,kv,webp,so


# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0
android.add_src = %(source.dir)s/java/
# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements # https://github.com/kivymd/KivyMD/archive/master.zip
# comma separated e.g. requirements = sqlite3,kivy
requirements = kivy==2.0.0,kivymd==0.104.1,python3,pyjnius,plyer,requests,urllib3,chardet,idna,Image,PIL,watchdog

#pymongo,certifi,ipaddress,certifi,pymongo-auth-aws,dnspython,pyOpenSSL,service-identity,python-snappy,zstandard,pymongocrypt,backports.pbkdf2,monotonic

# python3 -m buildozer -v android debug
# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = /home/jbsidis/Escritorio/_a/bbay.png
presplash.filename = splash.png

# (str) Icon of the application
#icon.filename = /home/jbsidis/Escritorio/_a/xbay.png
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all) portrait
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
 author = Kulife Team

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF
android.presplash_color = white

# (list) Permissions
#android.permissions = INTERNET #SEND_SMS,RECORD_AUDIO, 
android.permissions = CHANGE_WIFI_STATE, INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE, ACCESS_MEDIA_LOCATION, WAKE_LOCK, CAMERA, FLASHLIGHT,GLOBAL_SEARCH,BIND_PRINT_SERVICE,REQUEST_IGNORE_BATTERY_OPTIMIZATIONS

# (int) Target Android API, should be as high as possible.
android.api = 29

# (int) Minimum API your APK will support.
android.minapi = 21
android.arch = armeabi-v7a

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
warn_on_root = 1
#buildozer --profile demo android debug
