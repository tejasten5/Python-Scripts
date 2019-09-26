import requests
import json
import re

phNo = "+93 (122)-(789)-621-89-789"
name = "afghanistan"
s1 = r""
pattern = "3-3-3-2-3"


def check(name, phNo):
    phNo = phNo.strip(" ")
    if phNo.startswith('+'):
        code1 = phNo.split(" ")[0]
        if code1.startswith("+"):
            code1 = code1.replace("+", "")
        num = phNo.replace(code1, "")
        response = requests.get(
            "https://restcountries.eu/rest/v2/callingcode/" + code1)
        d = json.loads(response.text)
        for i in d:
            nm = i['name']
        if nm == name.title():
            return True
        else:
            return False


def removeParanthesis(phNo):
    if"(" and ")" in phNo:
        phNo = phNo.replace("(", "")
        phNo = phNo.replace(")", "")
    return phNo


def code(result, name):
    if(result == 'False'):
        response = requests.get(
            "https://restcountries.eu/rest/v2/name/"+name)
        if response.status_code == 200:
            return "Country is", name
    else:
        return False


def check_pattern(no, pattern):
    li = []
    s1 = r''
    for i in pattern.split('-'):
        li.append(i)
    for i in range(len(li)):
        s = r'(\d{%s})-' % (li[i])
        s1 = s1+s
    s1 = s1.rstrip("-")
    b = re.findall(s1, no)
    if len(b) == 0:
        return False
    else:
        return True


new_phNo = removeParanthesis(phNo)
checkPattern = check_pattern(new_phNo, pattern)
valid = check(name, phNo)

print("Remove Paraenthesis->", new_phNo)
print("Pattern check_pattern->", checkPattern)
print("Valid country n code->", valid)
