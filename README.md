# Codeforce Problem Parser v69

## Developed by Tamim(BooleanWolf)

**The Scraping code was from kerolloz's api.**

# About It

So basically this is a problem parsing script and also you can easily test your code against the testcase with just one command. You can also run your code agains your own custom testcase.

# How to use it

### You can also watch a video here if you want,

First of all,

1. Clone the repository.

```
git clone https://github.com/BooleanWolf/CF-Problem-Parser-v69.git
```

2. Install the dependencies by running the command

```
pip install -r requirements.txt
```

3. Then in the cfprob.py file you need to set the Directory to your own directory (set the variable myCPDirectory = Your Own Directory ) and dont forget to add doble \\ ! This is all you have to modified

4. Put the template you use in the template.cpp

5. Now you are ready to code! :D

# Command

1. To parse a problem from codeforce, run the following command,

```
python cfprob.py contestnumber problemLetter
```

For example:-

```
python cfprob.py 123 A
```

-- You can the get the contest number in the url of the problem. For example:-
if the url is:- https://codeforces.com/problemset/problem/141/A
then the contestNumber is 141 and it's a "A problem.

2. A folder with all necessary files will be created in your directory. Now

```
cd theProblem
```

3. Now you will a sol.cpp file, this is where you will write your code.
4. To run the code, in your problem directory

```
python run.py -t                                                 // This will run your code against the codeforces testcase
```

```
python run.py -c                                                // This will run your code agains the custom testcase
```

5. And you are done!

Feel free to knock me, if you see any bug or you think it can be developed!
Facebook: https://www.facebook.com/mdtamim.sarkar.58

### HAPPY HACKING
