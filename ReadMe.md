**This is a project to create a mutation tool to mutate java programs. The tool is written in Python, using the library PyQt4 to do the user interface**

# How to use

### On Linux

Just download of the program using:

**HTTP**: git clone https://github.com/fernandobd42/Mutation-Tool---Python.git

**SSH**: git clone git@github.com:fernandobd42/Mutation-Tool---Python.git

**0 (EDIT JSON):**

Before run the program, go to the directory of program and edit the file: <b>operators.json</b>

![Json](https://raw.githubusercontent.com/fernandobd42/images/master/00.PNG)

so, insert the name of operator where is <b>name</b>, then insert the operator you want to find on the program where is <b>op1</b>, and insert the operator you want to replace per <b>op1</b>, where is <b>op2</b>

Look, it's possible insert how many <b>operators</b> you want, just follow the pattern of json file

**1 (EDIT screenshot.py):**

In screenshot.py file alter manually the path of java main file ( the path where have main java file is) where is red, to program run right

![Screenshot](https://raw.githubusercontent.com/fernandobd42/images/master/01.PNG)

**2 (INIT THE PROGRAM):**

Access the directory of the tool by shell, and run: <b>python gui.py</b><br>
Obs: you need to use the version 2.7 of python
```
➜  Mutation-Tool---Python git:(master) ✗ python gui.py
```
***1.1 (Select the Project):*** Select the directory of the original program. In the case, the directory of the program that you want to do the mutation test

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/02.PNG)

***1.2 (Select the Json File):*** Then, select the json file. In case the json file that has the operators

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/03.PNG)

***1.3 (Select the Main Java File):*** Then, select the Main java file ( the java file ). In case the java file will be executed

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/04.PNG)

**3 (DO THE MUTATE):**

Just click on the little button <b>'Mutation'</b>

![Insert](https://raw.githubusercontent.com/fernandobd42/images/master/05.PNG)

**4 (RESULT):**

Also the result on the shell or in MutateTool.log, it is possible to see how many operators were found and how many mutants were created. Also is possible to see the image of each mutant program running on images directory that locate in the same directory of mutation tool.

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/06.PNG)
