import bs4
import requests
import sys
import os
from pathlib import Path


myCPDirectory = "E:\\SOLCPP\\"


def split_limit(soup):
    l = soup.split()
    return {
        "value": int(l[0]),
        "unit": l[1]
    }


def group_tests(lst):
    return [{"input": _in, "output": _out} for _in, _out in pairwise(lst)]


def get_sample_tests(souped_html):
    return group_tests(get_tags_contents(souped_html, 'pre'))


def get_tags_contents(souped_html, tag_name, class_name=None):
    return [concat_contents(tag.contents) for tag in souped_html.find_all(tag_name, class_name)]


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def get_statement(soup):
    return concat_contents(soup.find('div', 'header').next_sibling.contents)


def get_content(soup, _class=''):
    element = soup.find('div', _class)
    if not element:
        return None
    tags = element.contents
    tags.pop(0)
    return concat_contents(tags)


def concat_contents(ls):
    return ''.join([str(i) for i in ls])


def parse_problem(problem_link):
    markup = requests.get(problem_link).text
    soup = bs4.BeautifulSoup(markup, "html.parser")
    problem = {
        "title": soup.find('div', 'title').string,
        "timeLimit": split_limit(soup.find('div', 'time-limit').contents[1].string),
        "memoryLimit": split_limit(soup.find('div', 'memory-limit').contents[1].string),
        "statement": get_statement(soup),
        "inputSpecification": get_content(soup, 'input-specification'),
        "outputSpecification": get_content(soup, 'output-specification'),
        "samples": get_sample_tests(soup),
        "note": get_content(soup, 'note'),
    }
    return problem


def isLineEmpty(line):
    return len(line.strip()) < 1


link = "https://codeforces.com/problemset/problem/{contestNumber}/{problemNumber}".format(
    contestNumber=sys.argv[1], problemNumber=sys.argv[2])
problem = parse_problem(link)


# Starting
numOfTestCases = len(problem['samples'])
echo1 = f"Creating the input and output files for {problem['title']}"
echo2 = f"Time Limit: {problem['timeLimit']['value']} seconds."
echo3 = f"Total Testcases Needed to Pass: {numOfTestCases}"
echo = "echo " + echo1
os.system(echo)
echo = "echo " + echo2
os.system(echo)
echo = "echo " + echo3
os.system(echo)


os.system("echo Making Folder....")


# making a nice foldername
folderName = ""
foldername = problem['title'].split(" ")
for i in foldername:
    if i != "A.":
        folderName += i
        folderName += "_"

try:
    os.mkdir(folderName)
    os.system("echo Folder created successfully")
except:
    os.system("echo You have previously made this folder hehe")

fileDirectoryStr = myCPDirectory + folderName
fileDirectory = Path(fileDirectoryStr)

os.system("echo creating testcases...")

# making files for testcases
for i in range(len(problem['samples'])):
    filePathStrInp = myCPDirectory + \
        folderName + "\\input{id}.txt".format(id=i+1)

    filePathStrOut = myCPDirectory + folderName + \
        "\\output{id}.txt".format(id=i+1)

    filePathStrmyOut = myCPDirectory + folderName + \
        "\\myoutput{id}.txt".format(id=i+1)

    filePathInp = Path(filePathStrInp)
    filePathOut = Path(filePathStrOut)
    filePathMyOut = Path(filePathStrmyOut)

    inpFile = open(filePathInp, "w")
    outFile = open(filePathOut, "w")

    sampleinp = problem["samples"][i]['input']

    if "<br/>" in sampleinp:
        sampleinp = sampleinp.replace("<br/>", "\n")

    sampleout = problem["samples"][i]['output']

    if "<br/>" in sampleout:
        sampleout = sampleout.replace("<br/>", "\n")

    print(sampleinp, file=inpFile)
    print(sampleout, file=outFile)
    inpFile.close()
    outFile.close()

    # removing blank lines from testcase
    lines = []
    out = open(filePathInp, 'r')
    lines = out.readlines()
    out.close()
    out = open(filePathInp, 'w')
    t = []
    for line in lines:
        if not isLineEmpty(line):
            t.append(line)
    out.writelines(t)
    out.close()

    lines = []
    out = open(filePathOut, 'r')
    lines = out.readlines()
    out.close()
    out = open(filePathOut, 'w')
    t = []
    for line in lines:
        if not isLineEmpty(line):
            t.append(line)
    out.writelines(t)
    out.close()

    myout = open(filePathStrmyOut, "w")
    myout.close()

    l = f"echo Testcase{i+1} created!"
    os.system(l)


os.system("echo Creating your Cpp and py file")
solcppPathStr = fileDirectoryStr + "\\sol.cpp"
solpyPathStr = fileDirectoryStr + "\\sol.py"
runpyPathStr = myCPDirectory + "\\run.py"

solcppPath = Path(solcppPathStr)
solpyPath = Path(solpyPathStr)
runpyPath = Path(runpyPathStr)

solcpp = open(solcppPath, "w")
solpy = open(solpyPath, "w")
solpy.close()
solcpp.close()
os.system("echo Cpp and py file has been created!!")

os.system("echo Making it code ready")

tempecho = f"cat template.cpp >> {folderName}/sol.cpp"
os.system(tempecho)
tempecho = f"cat sol.py >> {folderName}/sol.py"
os.system(tempecho)

# Run py
runpy = open(runpyPath, "r")
lines = []
lines = runpy.readlines()
runpy.close()

toBeWritten = []
s1 = f"numOfTestCases = {numOfTestCases}\n"
s2 = f"ProbTitle = \"{problem['title']}\"\n"
toBeWritten.append(s1)
toBeWritten.append(s2)
for i in lines:
    toBeWritten.append(i)

runpyPathStr = fileDirectoryStr + "\\run.py"
runpyPath = Path(runpyPathStr)
runpy = open(runpyPath, "w")

runpy.writelines(toBeWritten)

runpy.close()
os.system("echo Ok you are good to Go!! Happy Hacking!")
# making the solvable cpp file
