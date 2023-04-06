# Python_console_task

## INTRODUCTION

This project is a CRUD application that allows the user to create, read, update, and delete tasks using the Python console. The task information is stored in a CSV file.

## OVERVIEW

When running the program, a menu with available options is displayed: view existing tasks, add a new task, edit an existing task, delete an existing task, and exit the program.

When selecting the option to view existing tasks, the CSV file is read, and the existing tasks are displayed in the console. Each task is shown with its ID, title, and status.

When selecting the option to add a new task, the user is prompted to enter the title and status of the new task. The task information is written to the CSV file.

When selecting the option to edit an existing task, the user is prompted to enter the ID of the task they want to edit, as well as the new title and status of the task. The corresponding task is searched for in the CSV file, its information is updated, and then written back to the CSV file.

When selecting the option to delete an existing task, the user is prompted to enter the ID of the task they want to delete. The corresponding task is searched for in the CSV file, deleted from the CSV file, and then saved.

When selecting the option to exit the program, the program execution is terminated.

This project is a good demonstration of basic skills in Python, such as working with files, data structures, exception handling, and building user interfaces.

