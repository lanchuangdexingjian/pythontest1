def generate_dict_simple(names):
    wordlist = []
    seen = {}
    
    common_suffixes = ['', '123', '1', '!', '@', '2024', '24', '01', '00', '1234']
    
    for name in names:
        name = name.strip()
        if not name or name in seen:
            continue
        
        base_forms = [
            name.lower(),
            name.upper(),
            name.capitalize()
        ]
        
        for form in base_forms:
            if form and form not in seen:
                wordlist.append(form)
                seen[form] = True
                
                for suf in common_suffixes:
                    w = form + suf
                    if w not in seen:
                        wordlist.append(w)
                        seen[w] = True
                
                leet = form.replace('a','4').replace('e','3').replace('i','1').replace('o','0').replace('s','5')
                if leet != form and leet not in seen:
                    wordlist.append(leet)
                    seen[leet] = True
                    for suf in common_suffixes:
                        w2 = leet + suf
                        if w2 not in seen:
                            wordlist.append(w2)
                            seen[w2] = True
    
    return wordlist

# 模拟读取 names.txt（实际使用时可从文件读）
names_content = """admin
root
user
guest
test
ctf
hello
password
qwerty
123456"""

names = [line.strip() for line in names_content.splitlines() if line.strip()]

wordlist = generate_dict_simple(names)

with open("wordlist.txt", "w") as f:
    for w in wordlist:
        f.write(w + "\n")