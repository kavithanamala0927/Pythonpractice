import os
print (os.path.join("C:\\", "Users", "Kavitha", "Desktop"))
print (os.path.join('usr', 'bin', 'spam'))
myFiles = ["docs.txt", "pdfs.pdf", "pngs.png", "csvs.csv"]
for file in myFiles:
    print (os.path.join("C:/Users/Kavitha/Desktop", file))
