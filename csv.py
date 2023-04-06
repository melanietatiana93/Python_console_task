import csv

def show_menu():
    print('1. Ver tareas')
    print('2. Agregar tarea')
    print('3. Editar tarea')
    print('4. Eliminar tarea')
    print('5. Salir')

def get_choice():
    while True:
        choice = input('Ingresa el número de opción que deseas: ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print('Opción inválida, por favor inténtalo de nuevo.')

def show_tasks():
    with open('tasks.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print('Tareas:')
        for row in reader:
            print(f"{row['id']}: {row['title']} ({row['status']})")

def add_task():
    title = input('Ingresa el título de la tarea: ')
    status = input('Ingresa el estado de la tarea: ')
    with open('tasks.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, status])
    print('Tarea agregada exitosamente.')

def edit_task():
    task_id = input('Ingresa el ID de la tarea que deseas editar: ')
    title = input('Ingresa el nuevo título de la tarea: ')
    status = input('Ingresa el nuevo estado de la tarea: ')
    rows = []
    with open('tasks.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == task_id:
                rows.append([task_id, title, status])
            else:
                rows.append(row)
    with open('tasks.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    print('Tarea editada exitosamente.')

def delete_task():
    task_id = input('Ingresa el ID de la tarea que deseas eliminar: ')
    rows = []
    with open('tasks.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] != task_id:
                rows.append(row)
    with open('tasks.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    print('Tarea eliminada exitosamente.')

def main():
    while True:
        show_menu()
        choice = get_choice()
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print('¡Hasta pronto!')
            break

if __name__ == '__main__':
    main()
