# PUI2017_rh2684

### Homework 1 for PUI2017 - description<br /><br />

##### Setting up the environment<br /><br />

<p>Since I am using Windows OS, the whole process contained differences for me. First, I had to install and set up Git Bash, which is the default terminal I am using now. In order to keep my files synchronized everywhere, I chose Google Drive as my LOCAL path, where I created the both gittest_rh2684 and PUI2017 folders.</p><br />

<p>After I created the PUI2017 folder, I set up the environmental variable by typing:</p><br />

	PUI2017=/c/Users/ruham/Googledrive/PUI2017
	
<p>After which, I put the variable into the .bashrc file by typing:</p><br />

	echo 'PUI2017='/c/Users/ruham/Googledrive/PUI2017'' >> ~/.bashrc

<p>Furthermoe, I created an <b>alias</b> for <b>pui2017</b> to be equal to the environmental variable created earlier. I did that by typing:</p><br />

	alias pui2017='cd $PUI2017'
	echo 'alias pui2017='cd $PUI2017'' >> ~/.bashrc
	source .bashrc
	
<p>See the screenshot of the .bashrc file below:</p>
<a href="https://github.com/rrubo/PUI2017_rh2684/blob/master/HW1_rh2684/HW1/bashrc.png" target="_blank"><img src="https://github.com/rrubo/PUI2017_rh2684/blob/master/HW1_rh2684/HW1/bashrc.png" alt="bashrc file screenshot - Ruben Hambardzumyan" style="max-width:100%;"></a><br />

<p>Below is the screenshot of the bash window with verifying commands:</p>
<a href="https://github.com/rrubo/PUI2017_rh2684/blob/master/HW1_rh2684/HW1/pui2017.png" target="_blank"><img src="https://github.com/rrubo/PUI2017_rh2684/blob/master/HW1_rh2684/HW1/pui2017.png" alt="bash interface screenshot - Ruben Hambardzumyan" style="max-width:100%;"></a><br />

<p>Then, I proceeded to creating a repository on GitHub called <b>PUI2017_rh2684</b> and copy pasted the Git code to the bash to syncronize it with the local PUI2017 folder. By adding the screenshots to the local folder HW1, I typed:</p><br />

	git add *
	git commit *
	git push

<p>This done, I proceeded to editing this markdown file, which you now reed (thanks for that, by the way!). I edited the file several times, thus, there are several commits of this file.<br />
Now, the environment is ready!</p>




