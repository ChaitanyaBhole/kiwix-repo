# kiwix-repo
A repo on how to use the repos made available by https://github.com/kiwix and how to download the zim file for offline usage.

https://kiwix.org/


### FAQs
https://www.kiwix.org/en/documentation

### Content - Zim Files
https://www.kiwix.org/en/downloads/kiwix-content-packages/

https://wiki.kiwix.org/wiki/Content_in_all_languages

https://library.kiwix.org/?lang=eng

https://ftp.nluug.nl/kiwix/zim/?utm_source=pocket_reader

### Downloading content - Direct or using torrent client
wget or curl command can get you the zim file for eg :

wget https://download.kiwix.org/zim/wikipedia_en_all.zim

https://download.kiwix.org/zim/wikipedia_en_all.zim.torrent


### Kiwix - Clients
### Linux
https://download.kiwix.org/release/kiwix-desktop/kiwix-desktop_x86_64.appimage 
#### command for appimage to Run 
sudo chmod a+x kiwix-desktop_x86_64_2.0-rc4.appimage
./kiwix-desktop_x86_64_2.0-rc4.appimage

https://flathub.org/apps/details/org.kiwix.desktop


### Windows
http://download.kiwix.org/release/kiwix-desktop/kiwix-desktop_windows_x64.zip

### MacOS
https://download.kiwix.org/release/kiwix-desktop-macos/kiwix-desktop-macos.dmg

### Firefox
https://addons.mozilla.org/en/firefox/addon/kiwix-offline/
#Chrome
https://chrome.google.com/webstore/detail/kiwix/donaljnlmapmngakoipdmehbfcioahhk

### Mobile - clients
### Android
https://play.google.com/store/apps/details?id=org.kiwix.kiwixmobile

### iOS
https://itunes.apple.com/us/app/kiwix/id997079563

### windows mobiles
https://www.microsoft.com/en-us/p/kiwix-js/9p8slz4j979j



## Use the following packages to serve the information in .zim files i.e self-host kiwix and zim files on a device

### Kiwix-Serve , Kiwix-Manage, Kiwix-Search, Kiwix-Read
### windows
https://download.kiwix.org/release/kiwix-tools/kiwix-tools_win-i686.zip

### ARM devices
https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-armhf.tar.gz

https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-x86_64.tar.gz
https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-i586.tar.gz

### Kiwix Hotspot installation
https://www.kiwix.org/en/documentation/how-to-set-up-kiwix-hotspot/

### Local deployment/running steps - The Service
Kiwix-Serve - serve .zim files over the HTTP protocol within your local network
#Navigate to the directory where all the .zim files are downloaded and execute the following to 
#broadcast wikipedia on http://localhost:8181/
sudo ./kiwix-serve -d -p 8181 -v $(ls | grep .zim)
sudo ./kiwix-serve -d -p 8181 -v *.zim

##### To get access logs
sudo ./kiwix-serve -d -p 8181 -v $(ls | grep .zim) > kiwix.log
sudo ./kiwix-serve -d -p 8181 -v *.zim > kiwix.log

##### Kill daemonized process
sudo kill $(ps -e | grep kiwix-serve)

## serve multiple zim files
https://zer09er.blogspot.com/2020/04/how-to-install-and-configure-kiwix.html
https://www.rickmakes.com/offline-wikipedia-on-wired-raspberry-pi-using-kiwix/

###  Content - mirrors
https://www.mirrorservice.org/sites/download.kiwix.org/zim/wikipedia/
https://ftp.fau.de/kiwix/zim/stack_exchange/

# PS : Before using kiwix and/or downloading/sharing content i.e zim files, read the respective license(s)
