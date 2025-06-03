import os

path = "./NYT-recipes"
for filename in os.listdir(path):
    initial = os.path.join(path, filename)
    print(initial)

    if filename.find("(with_Video)") != -1 :
        update = filename.replace("(with_Video)", "", 1)

    

    update = os.path.join(path, filename.replace(" ", "_"))
    print(update)
    os.rename(initial, update)