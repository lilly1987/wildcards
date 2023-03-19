# wildcards

### ex

- form
a{__b__|{c|}|{__d__|e|}|f|}g____ __my__
 
- to
aeg __quality_my__, __breasts__, { |__character_dress__|__dress_my__}, __shoulder__, {high heels,| } {choker,| } {<lora:__lora_lst__:__rora_num__>,| } NSFW, __NSFW_my__, { |__style_my__,}


### run sample

```
python wildcards.py
```

### python sample

```
import wildcards as w

# 가져올 파일 목록. get wildcards file
w.card_path=os.path.dirname(__file__)+"\\wildcards\\**\\*.txt"

# 실행 run
print(w.run("a{__b__|{c|}|{__d__|e|}|f|}g____ __my__"))
```

### 

```
wildcards.py # modul file
wildcards/*.txt # wildcards file
wildcards/**/*.txt # wildcards file
```
