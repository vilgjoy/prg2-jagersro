# while True:
#     namn = input("Skriv in ditt namn: ")
#     if len(namn) >= 2:
#         break
#     print("Namnet måste vara minst 2 tecken långt.")


def get_name():
    while True:
        name = input("Skriv in ditt namn: ")
        if len(name) >= 2:
            return name
        print("Namnet måste vara minst 2 tecken långt.")


ditt_namn = get_name()
print("hej", ditt_namn)
