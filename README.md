# Introduction

Generate an HTML/JS/CSS project starter for the [50 Projects in 50 Days](https://50projects50days.com/) course from Traversy Media.

The program takes the name of the project folder, and optionally the folder location you would like to create the project, then outputs all the required files.

# Usage

Use the command:

```
python generate-project-starter.py project_location/project_name
```

Where project_name represents both the name of the project and project_location is the folder location, here are some examples.

To generate a project named "Card_Project" in the same folder as the generate-project-starter.py file, use this command:

```
python generate-project-starter.py Card_Project
```

To generate a project named "Top_Level" in the parent folder, so that it is seperate from this project folder, use this command:

```
python generate-project-starter.py ../Top_Level
```

To generate a project with spaces in the name, wrape the project name in quotes.

You can modify the gen_project.bat file to make it easier to use in another folder!

# Requirements

Project uses Python 3.6+, and was bult using Python 3.10

It is suggested you create a [Virtual Environment](https://docs.python.org/3/library/venv.html) for the project.

Install any required python packages using the command:

```
python -m pip install -r requirements.txt
```
