
from zipfile import ZipFile

num = 90052 
counter = 0
result = None
all_comments = b""
path = []
with ZipFile("channel.zip", 'r') as testzip:

    while(num != 0):
        counter += 1

        file_name = str(num) + ".txt"
        path.append(file_name)
        with open(file_name, "r") as myfile:
            data = myfile.readline()

        num = data.split()[-1]

        try:
            num = int(num)
        except:
            result = num
            num = 0

#print (file_name)

list_inside = testzip.infolist()
for name in path:
    for inside in list_inside:
        if inside.filename == name:
            all_comments += inside.comment

print(all_comments.decode("utf-8"))
