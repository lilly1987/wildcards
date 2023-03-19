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
    print(f"card i : {match.group(2)}")
    if match.group(2) in cards :
        #print(f"y")
        r=random.choice(cards[match.group(2)])        
    else :
        #print(f"n")        
        r= match.group(2)
    print(f"card r : {r}")
    return r
    #return cards[match.group(2)] if match.group(2) in cards else match.group(2)

def card_loop(text):
    bak=text
    for i in range(1, 50):
        tmp=recard.sub(card, bak)
        if bak==tmp :
            tmp=sub_loop(text)
        if bak==tmp :
            return tmp
        bak=tmp
    return bak
    
    
def card_load():
    global cards 
    cards = {}
    path=os.path.dirname(__file__)
    #print(f"path : {path}")
    #path=os.path.join(path)
    #print(f"path : {path}")
    t_path=path+"\\wildcards\\**\\*.txt"
    #print(f"path : {path}")
    files=glob.glob(t_path, recursive=True)
    #print(f"files : {files}")
    
    for file in files:
        basename = os.path.basename(file)
        file_name = os.path.splitext(basename)[0]
        if not file_name in cards:
            cards[file_name]=[]
        #print(f"file_name : {file_name}")
        f = open(file, 'r', encoding='UTF8')
        lines = f.readlines()
        for line in lines:
            line=line.strip()
            if line.startswith("#") or len(line)==0:
                continue
            cards[file_name]+=[line]
            #print(f"line : {line}")
    print(f"cards : {cards}")
    
def run(text):

    card_load()
    
    bak=text
    #print(f"text : {text}")
    result=card_loop(text)
    print(f"result : {result}")
    return result
    
# ============================================================

# 테스트용
test="a{__b__|{c|}|{__d__|e|}|f|}g____ __my__"

#m = p.sub(sub, test)
#print(m)

run(test)
