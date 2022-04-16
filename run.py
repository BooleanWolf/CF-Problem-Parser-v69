import filecmp
import sys
import os
import time


comm = f"echo Executing your solution: {ProbTitle}"
os.system(comm)


if sys.argv[1].lower() == "-t":
    os.system("g++ sol.cpp -o sol.exe")
    for i in range(numOfTestCases):
        os.system("echo --------------------------------------------------")
        comm = f"echo                    Testcase - {i+1}                   "
        os.system(comm)
        os.system("echo --------------------------------------------------")
        start_time = time.time()
        comm = f"sol.exe < input{i+1}.txt > myoutput{i+1}.txt"
        os.system(comm)
        end_time = time.time()
        comm0 = f"cat input{i+1}.txt"
        comm1 = f"cat myoutput{i+1}.txt"
        comm2 = f"cat output{i+1}.txt"

        os.system("echo ----------------------")
        os.system("echo Input:-")
        os.system("echo ----------------------")
        os.system(comm0)
        os.system("echo ----------------------")
        os.system("echo Expected Output:-")
        os.system("echo ----------------------")
        os.system(comm2)
        os.system("echo ----------------------")
        os.system("echo Your Output:-")
        os.system("echo ----------------------")
        os.system(comm1)

        # comparing two files
        os.system("echo ----------------------")
        os.system("echo Result")
        os.system("echo *****************************")
        myout = f"myoutput{i+1}.txt"
        out = f"output{i+1}.txt"
        result = filecmp.cmp(myout, out)
        if(result):
            comm = f"echo Congratulations!! TestCase {i+1} Passed"
            os.system(comm)
        else:
            comm = f"echo Oooops! :-(  :-( TestCase {i+1} Failed"
            os.system(comm)
        os.system("echo ...........................")
        times = f"echo Time Taken {end_time - start_time}"
        os.system(times)


if sys.argv[1].lower() == "-c":
    os.system("g++ sol.cpp -o sol.exe")
    os.system("echo ----------------------")
    os.system("echo Enter your input:-")
    os.system("echo ----------------------")
    comm = "sol.exe"
    os.system(comm)


if sys.argv[1].lower() == "-pyt":
    for i in range(numOfTestCases):
        os.system("echo --------------------------------------------------")
        comm = f"echo                    Testcase - {i+1}                   "
        os.system(comm)
        os.system("echo --------------------------------------------------")
        start_time = time.time()
        comm = f"python sol.py < input{i+1}.txt > myoutput{i+1}.txt"
        os.system(comm)
        end_time = time.time()
        comm0 = f"cat input{i+1}.txt"
        comm1 = f"cat myoutput{i+1}.txt"
        comm2 = f"cat output{i+1}.txt"

        os.system("echo ----------------------")
        os.system("echo Input:-")
        os.system("echo ----------------------")
        os.system(comm0)
        os.system("echo ----------------------")
        os.system("echo Expected Output:-")
        os.system("echo ----------------------")
        os.system(comm2)
        os.system("echo ----------------------")
        os.system("echo Your Output:-")
        os.system("echo ----------------------")
        os.system(comm1)

        # comparing two files
        os.system("echo ----------------------")
        os.system("echo Result")
        os.system("echo *****************************")
        myout = f"myoutput{i+1}.txt"
        out = f"output{i+1}.txt"
        result = filecmp.cmp(myout, out)
        if(result):
            comm = f"echo Congratulations!! TestCase {i+1} Passed"
            os.system(comm)
        else:
            comm = f"echo Oooops! :-(  :-( TestCase {i+1} Failed"
            os.system(comm)
        os.system("echo ...........................")
        times = f"echo Time Taken {end_time - start_time}"
        os.system(times)
