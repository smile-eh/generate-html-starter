import sys
import os

def verify_cmd_args():
    """
    Verify that there are just two system arguments:
        1) The file name of the program
        2) the project name that was requested, which 
            may include a folder location
    """
    if len(sys.argv) != 2:
        print("Error, expected just two arguments.")
        print("Expected a command like python generate-project-starter.py project_location/project_name")
        print(sys.argv)
        return False
    return True

def check_for_path():
    """
    Determine if the second system argment contains a slash.
    If it does, then it means we have to make the project in another folder.
    If it does not, then we make it in our current folder.
    """
    working_directory = ""
    project_name = ""
    if("/" in  sys.argv[1]):
        # arg contains path, set working directory
        split_val = sys.argv[1].rsplit("/", 1)
        working_directory = split_val[0]
        project_name = split_val[1]
        #Set working directory
    else:
        # keep working directory blank
        project_name = sys.argv[1]
    return (working_directory, project_name)

def make_directories(working_directory, project_name):
    if(len(working_directory) > 0):
        # There exists a requested change of directory
        # Check if it exists, make it if it does not
        if not os.path.exists(working_directory):
            os.makedirs(working_directory)
        os.chdir(working_directory)

    #Working directory created.
    #Check if project folder exists, if not make it
    if not os.path.exists(project_name):
        os.makedirs(project_name)
    os.chdir(project_name)

def make_files():
    from templates import index_html, script_js, style_css
    i_f = open("index.html", 'w')
    i_f.write(index_html)
    i_f.close()

    j_f = open("script.js", 'w')
    j_f.write(script_js)
    j_f.close()

    c_f = open("style.css", 'w')
    c_f.write(style_css)
    c_f.close()

def main():
    # Exit if argument errors
    if(verify_cmd_args() == False): return

    #check args, return values
    (working_dir, project_name) = check_for_path()

    #make the directories to work with
    make_directories(working_dir, project_name)

    #make the project starter files
    make_files()

if __name__ == "__main__":
    main()