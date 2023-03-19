import os, glob, sys
import random
import re

print("wildcards")
print(os.getcwd())

# ============================================================

resub  = re.compile(r"(\{)([^\{\}]*)(\})")
recard = re.compile(r"(__)(.*?)(__)")
cards = {}

def sub(match):
    m=match.group(2).split("|")
    #print(f"sub : {m}")
    return random.choice(m)

def sub_loop(text):
    bak=text
    for i in range(1, 50):
        tmp=resub.sub(sub, bak)
        if bak==tmp :
            return tmp
        bak=tmp
    return bak
    
def card(match):
    #print(f"card2 : {match.group(2)}")
    return match.group(2)

def sub_loop(text):
    bak=text
    for i in range(1, 50):
        tmp=recard.sub(sub, bak)
        if bak==tmp :
            tmp=sub_loop(text)
        if bak==tmp :
            return tmp
        bak=tmp
    return bak
    
    
def card_load():
    cards = {}
    path=os.path.dirname(__file__)
    print(f"path : {path}")
    #path=os.path.join(path)
    #print(f"path : {path}")
    t_path=path+"\\wildcards\\**\\*.txt"
    print(f"path : {path}")
    files=glob.glob(t_path, recursive=True)
    #print(f"files : {files}")
    
    for file in files:
        basename = os.path.basename(file)
        file_name = os.path.splitext(basename)[0]
        print(f"file_name : {file_name}")
        f = open(file, 'r', encoding='UTF8')
        lines = f.readlines()
        for line in lines:
            line.strip()
            print(f"line : {line}")
    
def run(text):
    card_load()
    bak=text
    print(f"text : {text}")
    result=recard.sub(card, text)
    print(f"result : {result}")
    return result
    
# ============================================================

test="a{__b__|{c|}|{__d__|e|}|f|}g____"

#m = p.sub(sub, test)
#print(m)

run(test)
