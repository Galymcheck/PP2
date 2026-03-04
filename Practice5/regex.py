import re

print("#1")
pattern = r"ab*"
test_strings = ["a", "ab", "abb", "b", "ba"]

for s in test_strings:
    if re.fullmatch(pattern, s): #returns a match object if he entire string matches the pattern.
        print(s)

print()
print("#2")
pattern = r"ab{2,3}"
test_strings = ["a", "ab", "abb", "abbb", "abbbb"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(s)


print()
print("#3")
text="hello_world this_is_a_test Not_this One_more_test"
pattern = r"[a-z]+(?:_[a-z]+)+"

matches=re.findall(pattern, text)
print(matches)

print()
print("#4")
text="Hello world this is Python"
pattern = r"[A-Z][a-z]+"

matches=re.findall(pattern, text)
print(matches)

print()
print("#5")
pattern=r"a.*b"
test_strings = ["ab", "axxxb", "a123b", "ac", "b"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(s)

print()
print("#6")
text="Hello, world. How are you?"
new_text=re.sub(r"[ ,\.]", ":", text)    #returns a string where matched occurrences are replaced 
print(new_text)                            #with the content of replace variabl

print()
print("#7")
def snake_to_camel(s):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s) #lambda gives access to each match

print(snake_to_camel("this_is_snake_case"))

print()
print("#8")
text="ThisIsCamelCaseString"
parts=re.findall(r"[A-Z][a-z]*", text)
print(parts)

print()
print("#9")
text="ThisIsCamelCaseString"
new_text = re.sub(r"(?<!^)(?=[A-Z])", " ", text) #Negative Lookbehind and Positive Lookahead
print(new_text)

print()
print("#10")
def camel_to_snake(s):
    s=re.sub(r"([A-Z])", r"_\1", s)
    return s.lower()

print(camel_to_snake("thisIsCamelCaseString"))