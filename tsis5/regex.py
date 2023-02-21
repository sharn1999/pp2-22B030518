import re 
def check(match):
    if match:
        print('Match found: ', match.group())
    else:
        print("No match")
# text = 'abbbbbbbbbcacfgh' 

# pattern = r'a(b*)'
# matching = re.search(pattern, text)
# check(matching)



# text = 'abbbb' 

# pattern = r'a(b){2,3}'
# matching = re.search(pattern, text)
# check(matching)



# text = 'aa_adaf_aaa edfkefskeamd' 

# pattern = r'[a-z]+_[a-z]+'
# matching = re.search(pattern, text)
# check(matching)



# text = 'FAdsadasDD fes' 

# pattern = r'[A-Z]{1,1}+[a-z]+'
# matching = re.search(pattern, text)
# check(matching)



# text = 'FAdsadabsDD fes' 

# pattern = r'a.*b'
# matching = re.search(pattern, text)
# check(matching)



# text = 'FAdsa ,.,dabsDD,   fes' 

# pattern = r'[ .,]'
# matching = re.sub(pattern, ';', text)
# print(matching)


# text = 'good_block_оыы' 

# res = re.sub(r'(?:^|_)(.)', lambda x: x.group(1).upper(), text)

# print(res)


# text = 'goodGoodVerygood' 

# res = re.findall(r'[a-z]+|[A-Z][a-z]*', text)

# print(res)


# text = 'goodGoodVerygood' 

# res =  re.sub(r'([A-Z])', r' \1', text)

# print(res)


# text = 'goodGoodVerygood' 

# res =  re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

# print(res)