with open("source.txt", "a") as file:
    file.write("success copy 'book'copy txt.\n")
    file.write("WARING Copy .\n")

with open("source.txt", "r") as file:
    lines = file.readlines()
    print("___copy past___")
    for line in lines:
        if "WARING" in line:
            print(f"cant copy : {line.strip()}")
        else:
            print(f"Normaly copy : {line.strip()}")
             
with open("source.txt", "r") as source, open("backup.txt", "w") as backup:
    for line in source:
        if "WARING" not in line:
            backup.write(line)


