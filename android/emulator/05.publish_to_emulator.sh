#sudo cp ./scripts/*.* ./mnt_sdcard
${ANDROID_SDK}/platform-tools/adb -e push $1 /sdcard/sl4a/scripts

