# Useful-Scripts

bw.py: This is used in conjuction with launchd om Mac, it gets activated as soon as something is changed in Desktop folder which given in script. It moves the original file in a sub folder and creates a Gray scale image and save it in the same folder i.e. Desktop. The launchd script to run this is given below which was stored in "~/Library/LaunchAgents/" with a file ending with .plist name :

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    	<key>EnableGlobbing</key>
    	<true/>
    	<key>Label</key>
    	<string>desktop.blackwhite</string>
    	<key>ProgramArguments</key>
    	<array>
    		<string>/usr/local/bin/python3</string>
    		<string>/Users/akash/personal/Useful-Scripts/bw.py</string>
    	</array>
    	<key>RunAtLoad</key>
    	<true/>
    	<key>StandardErrorPath</key>
    	<string>/tmp/desktop.blackwhite.err</string>
    	<key>StandardOutPath</key>
    	<string>/tmp/test.stdout</string>
    	<key>WatchPaths</key> 
    	<array> 
    		<string>/Users/akash/Desktop</string>
    	</array>
    </dict>
    </plist>
