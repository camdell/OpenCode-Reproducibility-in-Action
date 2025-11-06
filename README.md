# Open Code: Reproducibility in Action

## Overview

We all want our code to just work, every time, on every computer. But if you
have ever tried to run a colleague’s script and spent hours chasing down
missing packages or version conflicts, you know it is easier said than done.
Installing tools, managing dependencies, and sharing your environment can
quickly become overwhelming.

Fortunately, you do not need to become a container expert to make your code
more reliable today. Pixi, a programmatic environment management tool, makes
installing packages, managing dependencies, and sharing your environment
simpler and less intimidating.

Today, we will focus on practical strategies to write code that runs
reliably on any machine. You will learn how to set up your environment, manage
packages, and write code that works smoothly across different platforms, all
using Pixi.

## Agenda

### Our Hypothesis

Participants who use our *new studying method "B"*, will perform better
on the test than those who use the traditional studying method "A".

*note that no actual data was collected, this example is entirely synthetic*

### Data Collection Description

We conducted a study to evaluate how a professional training
program influences task performance. Two different training methods, Method A
and Method B, were compared.

A total of 100 adult participants were recruited and were randomly assigned to
one of the two training methods. The training program focused on developing
analytical problem solving skills relevant to participants work.

Each participant tracked the total number of hours they spent actively engaging
with their assigned training materials over a two week period. Training was
self paced, and participants were encouraged to complete between 8 and 15 hours
of practice.

After completing the training, all participants took a standardized performance
assessment designed to measure their ability to apply the skills taught. The
assessment produced a numerical score ranging from 0 to 100 with higher scores
representing better performance.

We recorded the following variables:

| Variable       | Type        | Description                                |
| ---------      | ------      | -------------                              |
| participant_id | Identifier  | Unique numeric ID per participant          |
| method         | Categorical | Assigned training method: A or B           |
| hours          | Continuous  | Total hours participants spent training    |
| score          | Continuous  | Score on the standardized performance test |

Some data irregularities occurred during collection. For example, a few
participants failed to report training hours, one participant reported a
suspiciously high score, and some records contained minor formatting issues
because data was manually entered from survey forms.

### How do We Analyze This?

1. Lets clean up the data raw_training_study.csv
    - filter out participants who did not report their hours
    - filter out scores that are not realisitic
    - ...

2. Save an intermediate copy of the clean data.
    - Share the dataset that has been cleaned

3. Analyze the dataset
    - linear model in R where we examine the effect of `score ~ method*hours`

#### How do we Ensure Reproducibility?

"well, it works on my computer"

1. We need to plan to share
2. The things that we do share, should be *easily* reproducible
3. Verify that the results we obtain are consistent and deterministic

### The Tools

**Git**: allows us to both collaborate and track the history of our code.
    - `git init .` initialize a git repository for a given folder
        - `.` shorthand means the current folder that our terminal is in
    - `git status` (needs to be run from within a git initialized repository)
        - tells you the state of your files in the current repo
    - `git add {...FILES}` or `git add .`
        - this tell git the files that we want to include in our next commit (snapshot).
    - `git commit -m '{MESSAGE}'` saves the current state of the files added via `git add` into a commit (snapshot).
    - `git diff {...FILES}` show the differences between the current state of the files and the last time they were included in a commit (snapshot).

**Pixi**: cross platform tool that allows on to easily create reproducible software environments.

**Python**: general purpose programming language
- pandas for tabular data analysis/cleaning
- Marimo Notebooks for data exploration/iteration

**R**: programming languague to ease working with data and statistical models
