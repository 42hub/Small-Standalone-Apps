import time

print 'We will start soon installing python 3'
print 'do ctrl + c to kill the process'
print ''
print ' NOTE : If you want to run a python 2 program use "/usr/bin/python"'
time.sleep(5)

import os
try:
	if os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"') == 0:
		if os.system('python3 -m pip install --upgrade virtualenv') == 0:
			if os.system('brew install python3') == 0:
				print "Sucsessfully installed !"
        if os.system('alias python=/usr/local/bin/python3') == 0:
          print "Python 3 set as default !"
			else:
    		print "Invalid Password or killed prosess !"
		else:
		  print "Invalid Password or killed prosess !"
	else:
		print "Invalid Password or killed prosess !"
except:
	print "Invalid Password or Abort action prosess started !"


