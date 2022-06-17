# Day 37: pixel habit checker

Week: Week 4

# **Overview**

---

- We are going to use the online API Pixela to build a graphical habit checker.
- A visualize graph that allow user to see the clustered or varies over space

![Untitled](Day%2037%20pixel%20habit%20checker%20cf813da27bac4cd6b4210c42e394b4ee/Untitled.png)

# **Features**

---

- by modify the code, we can:
    - create a user
    - create a graph
    - add a pixel value to the graph
    - update a pixel value
    - delete a pixel value to the graph

# Learnt Concept

---

- HTTP Header :
    - A data block that can hide the user sensitive information(TOKEN, API_Key)
    - Instead of sending the information to the parameter, put those info in Header is safer.

```
if you send your key in parameter:
https://pixe.la/v1/users/testingkun99/graphs/graph1/token=Dkhnfdldskgkn

this is safer:
https://pixe.la/v1/users/testingkun99/graphs/graph1
```

- HTTP Request:
    - POST
    - PUT
    - DELETE

# Issue and Solution

---

- 

# Usage/**Installation**

---

1. Make sure your computer install python 3
2. Download the folders
3.  In the folder directory, activate the virtual environment:

**Mac OS / Linux**

```bash
source venv/bin/activate

```

**Windows**

```bash
venv\Scripts\activate
```

After you've done that you should be able to run the `main.py` program.