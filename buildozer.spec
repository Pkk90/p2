[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for Android packaging)
package.domain = org.mykivyapp

# (str) Source code where the main.py lives
source.dir = .

# (list) Application requirements
requirements = python3, kivy, ephem, requests, hijri-converter

# (str) Application entry point
main.filename = myapp.py

# (str) Application versioning (method 1)
version = 1.0

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android API level to require (corresponds to the minimum API your app is compatible with)
android.sdk = 21

# (str) Android NDK version to use
android.ndk = 19b

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path =

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path =

# (bool) Run the app as a service
service.mykivyapp = myapp.py

# (str) Permissions
android.permissions = INTERNET
