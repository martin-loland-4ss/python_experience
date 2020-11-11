# Python experience evaluation

Thanks for applying for the position at 4Subsea. To better understand your thoughts on coding practices and experience we want you to take a look on the tasks below.

# Prerequisites

You will need to have python installed on your computer, any version >=3.6 should work fine. Any IDE of your choice.

# Deliverables

You can download this repository to your own computer and work on it there. When you are satisfied with your edits (tasks are described below), zip the contents and send it to the e-mail provided.

Remember to update your name in the *candidate.json* file. If your code requires any external libraries, write them down in the *requirements.txt* file.

It is better to deliver something than nothing, you don't need to complete the tasks to deliver.

# Evaluation

Your delivery will be scored with respect to the following metrics:

- Clear and understandable code
- Analytic approach
- Task scoring (deliverables will be evaulated with test data)

# Tasks

Below are two tasks in order of inceasing complexity. Do your best with the
time you have availible.

## Task 1

**Introduction**

In the data folder you will find a file *dataset_1.csv* with some data. The first column is a date while the second column *value* is either True or False.

**Objective**

Complete function *task_1* in *functions.py*. The function should accept two parameters: dates (list of str) and values (list of True/False). The function should return a list if dates (str) where the three preceeding dates has been False. E.g. in dataset_1 the first date that meet this criteria would be 2020-01-06.

## Task 2

**Introduction**

In the data folder you will find a file *dataset_2.csv*. This file contains results gathered from simulations. The first column is pressure, the second column is the standard deviation of a stress series at a hot spot. The last column is the calulated damage at this hotspot for this stress series.

**Objective**

Complete function *task_2* in *functions.py*. The function should accept a pressure (float) and stress_std (float) as parameters and return an estimated damage (float).

# Testing

You can test your functions by running *python test.py* in a terminal (make sure that the folder that contains test.py is your working directory).

# Details

You are free to add other files and/or functions to complete your tasks. But only the functions task_1 and task_2 will be called during evaluation. Make sure that you use relative paths and include all your necessary files in the zip