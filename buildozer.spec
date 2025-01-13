[app]

# (str) Title of your application
title = Smart Download Handler

# (str) Package name
package.name = smartdownloadhandler

# (str) Package domain (needed for android/ios packaging)
package.domain = org.sekula

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,certifi,hostpython3,libffi

# (str) Presplash of the application
presplash.filename = data/presplash.png

# (str) Icon of the application
icon.filename = data/app_icon.png

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = android.permission.READ_EXTERNAL_STORAGE,android.permission.WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 19

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

# (str) Version of your application
version = 1.0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[android]
# Android SDK path
android.sdk_path = /root/.buildozer/android/platform/android-sdk

# Android NDK path
android.ndk_path = /root/.buildozer/android/platform/android-ndk-r25b

# NDK API level
android.ndk_api = 19
