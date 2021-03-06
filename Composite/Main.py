__author__ = 'yokoi-h'

from Entry import Directory, File, FileTreatmentException

try:
    print("Making root entries...")
    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")

    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)

    bindir.add(File("vi", 10000))
    bindir.add(File("latex", 20000))
    rootdir.printList()

    print("")
    print("Making user entries...")
    yuki = Directory("yuki")
    hanako = Directory("hanako")
    tomura = Directory("tomura")

    usrdir.add(yuki)
    usrdir.add(hanako)
    usrdir.add(tomura)

    yuki.add(File("diary.html", 100))
    yuki.add(File("Composite.java", 200))
    hanako.add(File("memo.tex", 300))
    tomura.add(File("game.doc", 400))
    tomura.add(File("junk.mail", 500))
    rootdir.printList()

except FileTreatmentException as ex:
    print(ex)



