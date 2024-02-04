# import sys
# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "class_work_django_orm.settings")
# django.setup()


import django_setup

from learning.models import User, Task


def add_user(login, email, role):
    if role in User.Role:
        user = User(
            login=login,
            email=email,
            role=role
        )
        user.save()
        return user

def add_task(name, description):
    task = Task(
        title=name,
        description=description
    )
    
    task.save()
    return task


def add_user_task(task_id, user_id):
    task = Task.objects.get(id=task_id)
    user = User.objects.get(id=user_id)
    user.tasks.add(task)
    return user.tasks


def change_task_status(task_id, status):
    task = Task.objects.get(id=task_id)
    task.status = status

def main():
    while True:
        ask = int(input("Add user - 1\nAdd task - 2\nAdd to user task - 3\nChange status of the task - 4\nExit - 0\n"))

        match ask:
            case 1:
                name = input("Name: ")
                email = input("Email: ")
                role = input("Role (admin/user):")
                print(add_user(name, email, role))
            case 2:
                title = input("Title: ")
                description = input("Description:")
                print(add_task(title, description))
            case 3:
                user_id = int(input("User id: "))
                task_id = int(input("Task id: "))
                print(add_user_task(task_id, user_id))
            case 4:
                task_id = int(input("Task id: "))
                status = input("New status: ")
                print(change_task_status(task_id, status))
            case 0:
                break



if __name__ == "__main__":
    main()
