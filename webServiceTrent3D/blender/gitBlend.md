Git LFS	https://git-lfs.github.com/
Fork	https://www.blender.org/download/
Git Installation
The installation of the tools are quite easy. Just follow the general instructions and use the defaults paths to keep it simple. To avoid issues in a later state of this tutorial open your command line tool by using the short keys ‘Win + R’, type in ‘cmd’ and press ‘Enter’.

In the command line window we check if Tortoise Git and Git Lfs has been installed properly by using the following commands:

git --version
git lfs --version
If you get version information like git version 2.11.0.windows.1 or git-lfs/2.9.0 (GitHub; windows amd64; go 1.12.7; git 8ab05aa7) everything seems to be fine. If you get an error message most likely the PATH variable of Windows is not set properly for either Tortoise Git or Git Lfs.

Create your first Git repository
To create your first repository you should create a new project folder and navigate in the command line window to this folder using the ‘cd’ command. In my example I will create a snowman project and create a folder snowman. This project folder snowman acts as a root folder for the Git repository. Once you reached the project folder type in the following command to create the repository:

git init
You should get the following message: Initialized empty Git repository in D:/gdrive/blender/Winter/Snowman/.git/

However to show the .git folder in the windows explorer you have to enable the view of hidden files and folders in the folder settings of your system. Once you can see these hidden files and folders you can take a look in the .git folder and view information about the configuration and description of your newly created repository.

To setup the Git Lfs you can either check the newest Getting Started from Git Lfs website or use the following commands:

git lfs install --local
git lfs track *.blend, *.png, *.jpg, *.jpeg, *.tif, *.gif, *.bmp, *.svg
git add .gitattributes
git commit -m "added .gitattributes"
git lfs install –local sets lfs smudge and clean filters in the local repository’s git config. It also installs a pre-push hook to run git-lfs-pre-push for the current repository.

git lfs track *.blend, … creates the file named .gitattributes and adds the from now on tracked file extensions.

git add .gitattributes stages the file to the repository.

git commit -m “added .gitattributes” adds the file to the repository

Repository Status
If you added a new file, like we will do in the next chapter or if there are uncommited changes you can get information about the current repository by using the following code.

git status
With this command git shows you exactly what is going on in your git repository.

Add .blend file to the Git repository
To initially add a new file to the respository the add command is used. Due to the track configuration the blend file is added to the git repository whereas the lfs module handles the file.

git add Snowman.blend
git commit -m "initial commit"
Like we did before with the .gitattributes file you add your blend project now to the repository.

Commit the Blender Project
After adding the blend file to the respository we want to commit changes to the respository. This can be done with these commands:

git add Snowman.blend
git commit -m "added carrot"
Furthermore in the Git tool Fork you can add the repository and view the commit history. In File -> Open Repository you can browse to your project folder and open the repository. Afterwards it should look similar to the picture below:

fork repository view
Viewing the repository in the Git tool Fork
Rename Blender Project
Just in case you have to change the name of your project or you copy&paste the complete project folder in order to start a new project but not from scratch it is possible to rename the Blender project file by using the following commands.

git status
git add newProject.blend
git commit --dry-run -a
Batch Script
Finally I want to provide you a short batch script which contains the previously explained commands. Feel free to download batch file below, place it into your project folder and just double click. As long as the steps in the chapter Git Installation worked find you are good to go.