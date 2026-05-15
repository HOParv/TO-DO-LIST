import os
print("TO-DO LIST")
print("To exit write exit")
tarea = []

archivo = "tasks.txt"

if os.path.exists(archivo):
    with open(archivo, "r") as f:
        tarea = [línea.strip() for línea in f.readlines()]

else:
    tarea =[]
while True:
    ntarea = input("\033[31mPlease write your tasks here:\033[0m ")

    for i, item in enumerate(tarea, 1):
        print(f"{i}. {item}")
    if ntarea == "exit":
        print("goodbye")
        break
    elif ntarea.lower() == "del":
        if not tarea:
            print("Nothing to delete")
            continue

        try:
            indice = int(ntarea("Enter the number to delete"))
            eliminada = tarea.pop(indice - 1 )
            print(f"Removed {eliminada}")
        except (ValueError, IndexError):
            print("Invalid input")


            tarea.pop(indice)
    else:
        tarea.append(ntarea)

        with open(archivo, "w") as f:
            for item in tarea:
                f.write(item + "\n")
        print("\033[34mCURRENT LIST \033[0m")
        for item in tarea:
            print(item)

#coded by xero