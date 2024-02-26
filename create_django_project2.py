import argparse
import subprocess


def create_django_project(project_name, app_name):
    """
    Creates a Django project and app.

    Args:
        project_name: The name of the project you want to create.
        app_name: The name of the app to create.
    """

    # Check if virtual environment is active
    if not any(env in os.environ for env in ["VIRTUAL_ENV", "CONDA_PREFIX"]):
        print("Please activate a virtual environment before running the script.")
        return

    # Check if Django is installed
    try:
        import django
    except ImportError:
        print("Django is not installed. Please install it using 'pip install django'.")
        return

    # Create the Django project using django-admin
    subprocess.run(["django-admin", "startproject", project_name])

    # Navigate to the project directory
    os.chdir(project_name)

    # Create the app
    subprocess.run(["python", "manage.py", "startapp", app_name])

    print(
        "Project '{}' and app '{}' created successfully!".format(project_name, app_name)
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Django project and app")
    parser.add_argument("project_name", help="The name of the project to create")
    parser.add_argument("app_name", help="The name of the app to create")
    args = parser.parse_args()
    create_django_project(args.project_name, args.app_name)
