## Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## How to Run Each Task

- 1). Download the zip folder first then extract it (clicking extract all)

- 2). Open the inner folder containing all the tasks from task 2 to task 6

- 3).Then, go to terminal and type dir on terminal to make sure you're in the correct folder

    `dir`

- 4).Type py --version to check if python is there or not (if not, then reopen terminal) so type below on terminal

    `py --version`

- 5). Create a virtual environment called venv

     `py -m venv venv`

- 6). Then install the dependencies

     `.\venv\Scripts\python.exe -m pip install pandas dash plotly pytest`

- 7). Once that's done, to run task 2 (processing the data), type on terminal below

      `.\venv\Scripts\python.exe .\task_2\data_merge.py`
  
- 8). To run task 3 (basic dashboard), type below

       `.\venv\Scripts\python.exe .\task_3\app.py`

- 9). To run task 4 (the styled dashboard), type below

      `.\venv\Scripts\python.exe .\task_4\appStyled.py`

- 10). To run task 5 (the tests), type below
  
      `.\venv\Scripts\python.exe -m pytest .\task_5\test_app.py -v`

- 11). To run task 6, first if you haven't done it, you must install Git and to do that, type exactly below on terminal

     `winget install --id Git.Git -e --source winget`

- 12). After installing git, type (run the test script)

     `& "C:\Program Files\Git\bin\bash.exe" ./task_6/execute_tests.sh`

- 13). Check its exit status and it should return 0 meaning all tests passed
