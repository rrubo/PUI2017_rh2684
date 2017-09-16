# PUI2017_rh2684

### Homework 1 for PUI2017 - description<br /><br />

##### 1. Setting up the environment<br /><br />

<p>Since I am using Windows OS, the whole process was different for me. First, I had to install and set up Git Bash, which is the default terminal I am using now. In order to keep my files synchronized everywhere, I chose Google Drive as my LOCAL path, where I created the both gittest_rh2684 and PUI2017 folders.</p><br /><br />

<p>After I created the PUI2017 folder, I set up the environmental variable by typing:</p><br />

	PUI2017=/c/Users/ruham/Googledrive/PUI2017
	
<p>After which, I put the variable into the .bashrc file by typing:</p><br />

	echo 'PUI2017='/c/Users/ruham/Googledrive/PUI2017'' >> ~/.bashrc

<p>Furthermoe, I created an <b>alias</b> for <b>pui2017</b> to be equal to the environmental variable created earlier. I did that by typing:</p><br />

	alias pui2017='cd $PUI2017'
	echo 'alias pui2017='cd $PUI2017'' >> ~/.bashrc
	
<p>See the screenshot of the .bashrc file below:</p><br />
<a href="/ruham/Googledrive/PUI2017/HW1/bashrc.png" target="_blank"><img src="/ruham/Googledrive/PUI2017/HW1/bashrc.png" alt="bashrc screen of Ruben Hambardzumyan" style="max-width:100%;"></a><br />




