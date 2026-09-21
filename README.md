## Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## How to Run Each Task

- 1). Download the zip folder first then extract it (clicking extract all)

- 2). Open the inner folder containing all the tasks from task 2 to task 6

- 3).Then, go to terminal and type dir on terminal to make sure you're in the correct folder

   ```powershell
      dir
   ```

- 4).Type py --version to check if python is there or not (if not, then reopen terminal) so type below on terminal

  ```powershell
   py --version
  ```

- 5). Create an environment called venv and install the dependencies by typing the link below

    ```powershell
    py -m venv venv
    .\venv\Scripts\python.exe -m pip install pandas dash plotly pytest
    ```

- 6). Once that's done, to run task 2, type on terminal below

      ```powershell
    .\venv\Scripts\python.exe .\task_2\data_merge.py
      ```
  
- 7). To run task 3, type below

       ```powershell
     .\venv\Scripts\python.exe .\task_3\app.py
       ```

- 8). To run task 4, type below

      ```powershell
     .\venv\Scripts\python.exe .\task_4\appStyled.py
      ```

- 9). To run task 5, type below
  
      ```powershell
     .\venv\Scripts\python.exe -m pytest .\task_5\test_app.py -v
      ```

- 10). To run task 6, first if you haven't done it, you must install Git and to do that, type exactly below on terminal

     ```powershell
     winget install --id Git.Git -e --source winget
     ```

- 11). After installing git, type

     ```powershell
     & "C:\Program Files\Git\bin\bash.exe" ./task_6/execute_tests.sh
      ```

- 12). Check its exit status and it should return 0 meaning all tests passed
