# PUI2017_rh2684

### Homework 1 for PUI2017 - description<br /><br />

##### 1. Setting up the environment<br /><br />

Since I am using Windows OS, the whole process was different for me. First, I had to install and set up Git Bash, which is the default terminal I am using now. In order to keep my files synchronized everywhere, I chose Google Drive as my LOCAL path, where I created the both gittest_rh2684 and PUI2017 folders.<br /><br />

After I created the PUI2017 folder, I set up the environmental variable by typing:<br />

	PUI2017=/c/Users/ruham/Googledrive/PUI2017
	
After which, I put the variable into the .bashrc file by typing:<br />

	echo 'PUI2017='/c/Users/ruham/Googledrive/PUI2017'' >> ~/.bashrc

Furthermoe, I created an <b>alias</b> for <b>pui2017</b> to be equal to the environmental variable created earlier. I did that by typing:<br />

	alias pui2017='cd $PUI2017'
	echo 'alias pui2017='cd $PUI2017'' >> ~/.bashrc
	
See the screenshot of the .bashrc file below:<br />
![.bashrc screenshot of Ruben Hambardzumyan](C:\Users\ruham\Googledrive\PUI2017\HW1bashrc.png".bashrc screenshot")<br />



