### Pinterest Download Helper
A script to download the image contents of a Pinterest folder at max resolution


1. Log in on Pinterest, click on an album and open the Chrome console with cmd+shift+i and click on Network->Img
1. Scroll all the way down to make sure that all the images are loaded
1. Right-click on an item in the Network list and select "save all as HAR with content", save to this directory as "source.har"
1. if using shadowsocks, use `export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;`
1. Launch with "python getUrl.py"
1. If some image fail, re-run the sript to retry only the failed images
