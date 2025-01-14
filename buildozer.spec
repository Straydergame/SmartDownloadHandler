[app]
title = Smart Download Handler
package.name = smartdownloadhandler
package.domain = org.sekula
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
presplash.filename = SmartDownloadHandler/data/presplash.png
icon.filename = SmartDownloadHandler/data/app_icon.png
orientation = portrait
android.permissions = android.permission.READ_EXTERNAL_STORAGE,android.permission.WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.debug_artifact = apk
version = 1.0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.sdk_path = /root/.buildozer/android/platform/android-sdk
android.ndk_path = /root/.buildozer/android/platform/android-ndk-r25b
