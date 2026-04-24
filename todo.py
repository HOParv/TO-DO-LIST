print("TO-DO LIST")
print("To exit press ctrl + c")
tarea = []

while True:
    ntarea = input("\033[31mPlease write your tasks here:\033[0m ")

    tarea.append(ntarea)
    print("\033[34m CURRENT LIST \033[0m")
    for item in tarea:
        print(item)