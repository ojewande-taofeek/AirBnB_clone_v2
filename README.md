<center> <h1> 0x02. AirBnB clone - MySQL </h1> </center>

---
<br>
<center> <h2>Background Context</h2> </center>
Environment variables will be your best friend for this project!

    * HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
    * HBNB_MYSQL_USER: the username of your MySQL
    * HBNB_MYSQL_PWD: the password of your MySQL
    * HBNB_MYSQL_HOST: the hostname of your MySQL
    * HBNB_MYSQL_DB: the database name of your MySQL
    * HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
<br>
<center><h2>Resources</h2></center>
<strong>Read or watch:</strong>
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/OG2OW5Pbjs-ds3ZHT0ow4g">cmd module</a></li>
<li><a href="https://intranet.alxswe.com/concepts/66"><strong>package concept page</strong></a></li>
<li><a href="https://intranet.alxswe.com/rltoken/g0tzN6ea1hWCj5OF99HB9w">unittest module</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/F6YRBSrkkkTTMVc66iaMgA">args/kwargs</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/GYWCmxokUZKAr-T93iQPcQ">SQLAlchemy tutorial</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/m4ogDCoKVm3Us0FybYh1tA">How To Create a New User and Grant Permissions in MySQL</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/FJCSaX1TCf0HAOzhsH_eWA">Python3 and environment variables</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/bWxESLJVYGNonjOYg8fOVg">SQLAlchemy</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/n6ePnCDwnbQMbxGgeoe1VA">MySQL 8.0 SQL Statement Syntax</a></li>
</ul>
<br>
<center><h2>Learning Objectives</h2><center>
At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/3nWKduPHOPRUFGNEtT-SMw">explain to anyone</a>, <stong>without the help of Google</strong>:
<br>
<center><h2>General</h2></center>

    * What is Unit testing and how to implement it in a large project
    * What is *args and how to use it
    * What is **kwargs and how to use it
    * How to handle named arguments in a function
    * How to create a MySQL database
    * How to create a MySQL user and grant it privileges
    * What ORM means
    * How to map a Python Class to a MySQL table
    * How to handle 2 different storage engines with the same codebase
    * How to use environment variables
<br>
<center><h2>Copyright - Plagiarism</h2></center>

    * You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
    * You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
    * You are not allowed to publish any content of this project.
    * Any form of plagiarism is strictly forbidden and will result in removal from the program.

<center><h2>Requirements</h2></center>
    
    * Python Scripts
    * Allowed editors: vi, vim, emacs
    * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    * All your files should end with a new line
    * The first line of all your files should be exactly #!/usr/bin/python3
    * A README.md file, at the root of the folder of the project, is mandatory
    * Your code should use the pycodestyle (version 2.8.*)
    * All your files must be executable
    * The length of your files will be tested using wc
    * All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
    * All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    * All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    * A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
<center> <h2>Python Unit Tests</h2> <center>

    * Allowed editors: vi, vim, emacs
    * All your files should end with a new line
    * All your test files should be inside a folder tests
    * You have to use the unittest module
    * All your test files should be python files (extension: .py)
    * All your test files and folders should start by test_
    * Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    * All your tests should be executed by using this command: python3 -m unittest discover tests
    * You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    * All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
    * All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    * All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    * We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

<center><h2>SQL Scripts</h2></center>
    
    * Allowed editors: vi, vim, emacs
    * All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
    * Your files will be executed with SQLAlchemy version 1.4.x
    * All your files should end with a new line
    * All your SQL queries should have a comment just before (i.e. syntax above)
    * All your files should start by a comment describing the task
    * All SQL keywords should be in uppercase (SELECT, WHERE…)
    * A README.md file, at the root of the folder of the project, is mandatory
    * The length of your files will be tested using wc

<center><h2>GitHub</h2></center>

<strong>There should be one project repository per group. If you clone/fork/whatever a partner’s project repository with the same name before the second deadline, you risk a 0% score.</strong>

<center><h2>Comments for your SQL file:</h2></center>

```
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
