import sys
import subprocess

def print_error(error):
    print(f"Error: {e}")
    sys.exit(1)

def install_django():
    try:
        subprocess.run(["pip", "install", "django"], check=True)
    except subprocess.CalledProcessError as e:
        print_error(e)
        
def save_requirements():
    try:
        subprocess.run(["pip", "freeze"], check=True, text=True, encoding="utf-8", stdout=subprocess.PIPE) as cmd:
            with open("requirements.txt", "w") as file:
                    file.write(cmd.stdout)
                    
        print("Successfully created requirements.txt")
    except subprocess.CalledProcessError as e:
        print_error(e)

def create_django_project(project_name, app_name):
    try:
        subprocess.run(["django-admin", "startproject", project_name], check=True)
        
        subprocess.run(["python", "startapp", app_name], check=True, cwd=project_name)
        
        print(f"Django project '{project_name}' with app '{app_name}' created successfully")
    except subprocess.CalledProcessError as e:
        print_error(e)
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python create_django_project.py <app_name>")
        sys.exit(1)
        
    install_django()
        
    project_name = "mysite"
    app_name = sys.argv[1]
    create_django_project(project_name, app_name)
    
    save_requirements()