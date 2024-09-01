Create a GitHub Repository:

Navigate to GitHub and create a new repository named datafun-03-analytics.
Initialize the repository with a default README.md.
Clone the Repository to Your Local Machine:

Open PowerShell.
Navigate to your Documents folder, then to project folder.
Clone the repository with: git clone https://github.com/yourusername/datafun-03-analytics.git.
Open the Project in Visual Studio Code:

Navigate into the project directory with: cd datafun-03-analytics.
Open the folder in Visual Studio Code by selecting File > Open Folder... and choosing the datafun-03-analytics folder.
Add and Configure the .gitignore File:

In Visual Studio Code, create a .gitignore file if it doesn’t already exist.
Add the following lines to the .gitignore file to ignore the .vscode/ and .venv/ directories:

Save the file to ensure these directories are not tracked by Git.


# datafun-03-project

## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
```