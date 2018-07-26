import os
import shutil

src = "C:\\Users\\dogu2\\Downloads"
dst = ("C:\\Users\\dogu2\\Desktop\\Zipler")
exeler = ("C:\\Users\\dogu2\\Desktop\\exeler")
pdfler = ("C:\\Users\\dogu2\\Desktop\\pdfler")
torrentler = ("C:\\Users\\dogu2\\Desktop\\torrentler")
os.chdir(src)

for exe in os.listdir(src):
    print(exe.endswith(".exe"))
    if exe.endswith(".exe"):
        shutil.move(exe, exeler)
        print(exe + " TAŞINDI")

for pdf in os.listdir(src):
    print(pdf.endswith(".pdf"))
    if pdf.endswith(".pdf"):
        shutil.move(pdf, pdfler)
        print(pdf + " TAŞINDI")

for torrent in os.listdir(src):
    print(torrent.endswith(".torrent"))
    if torrent.endswith(".torrent"):
        shutil.move(torrent, torrentler)
        print(torrent+" TAŞINDI")




