# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

# How to Run Each Task

- Download the zip folder first then extract it (clicking extract all)

- Open the inner folder containing all the tasks from task 2 to task 6

- Then, go to terminal and type dir on terminal to make sure you're in the correct folder

- Type py --version to check if python is there or not (if not, then reopen terminal)

- Create an environment called venv and install the dependencies by typing the link below

    py -m venv venv
.\venv\Scripts\python.exe -m pip install pandas dash plotly pytest

- Once that's done, to run task 2, type on terminal below

    .\venv\Scripts\python.exe .\task_2\data_merge.py

- To run task 3, type below

     .\venv\Scripts\python.exe .\task_3\app.py

- To run task 4, type below

     .\venv\Scripts\python.exe .\task_4\appStyled.py

- To run task 5, type below

     .\venv\Scripts\python.exe -m pytest .\task_5\test_app.py -v

- To run task 6, first if you haven't done it, you must install Git and to do that, type exactly below on terminal

     winget install --id Git.Git -e --source winget

- After installing git, type

     & "C:\Program Files\Git\bin\bash.exe" ./task_6/execute_tests.sh

- Check its exit status and it should return 0 meaning all tests passed
