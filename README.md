# FractionsChallenges

Write a command line program  that will take operations on fractions as an input and produce a fractional result.

## Prerequisites

Python 3.7 or higher 


## Installation:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies 

```bash
pip install -r requirements.txt
```
## Description:

For this project different instruction had been added with the goal of running e2e test, unit test and execute the main CLI application


Action | Command Line Instruction 
----------------- | -------------
Execute the CLI application   |  python3 runner.py -i '1/2 + 1/4 (Or any other operation under the challenge scope)'  
Run e2e tests  | python3 runner.py -i e2e  
Run unit test and open the html coverage | python3 runner.py -i unit_html  
Run unit test and show coverage report from terminal | python3 runner.py -i unit_html 
Get help | python3 runner.py -h


## Notes:
If your path variable for calling python is different than "python3" the code needs to be updated on runner.py line 22 and change for yours (py, python, etc..), no support for windows .ps1 or .bat for automatically open the html report this has to be done manually after executing unit_html command htmlcov -> index.html.


## Deployment process:

For the deployment of this project, we must create a pipeline in any ci/cd tools such as (Gitlab CI/CD, TravisCi, Jenkins, etc..) and establish different stages inside the pipeline: starting with a lint, then the unit tests, integration tests and finally the deployment process where we can add the necessary steps to publish our application in a package manager such as ``` pip ``` or in any other plataform where we want our application. 

