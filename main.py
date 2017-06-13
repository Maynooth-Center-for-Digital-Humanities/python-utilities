import codecs
import os
import unicodedata
import re


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def remove_tags(input_str):
    return re.sub("<.*?>", " ", input_str)

def scandir(myp,targetp):
    BLOCKSIZE = 1048576  # or some other, desired size in bytes
    for filename in os.listdir(myp):
        print(filename)
        if not filename.startswith('.'):
            if os.path.isfile(myp+filename):
                sourceFileName = myp + filename
                targetFileName = targetp + filename +".txt"
                with codecs.open(sourceFileName, "r", "latin-1") as sourceFile:
                    with codecs.open(targetFileName, "w", "utf-8") as targetFile:
                        while True:
                            contents = sourceFile.read(BLOCKSIZE)
                            if not contents:
                                break
                            targetFile.write(remove_accents(remove_tags(contents)))
            else:
                mp = myp+filename+"/"
                tp = targetp+filename+"/"
                try:
                    os.stat(tp)
                except:
                    os.mkdir(tp)
                scandir(mp,tp)


mypath = "data/input/hn/"
targetpath = "data/output/processed-hannah3/"

scandir(mypath,targetpath)


