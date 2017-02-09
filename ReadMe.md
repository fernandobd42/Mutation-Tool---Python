**This is a project to create a mutation tool to mutate any program. The tool is written in Python, using the library PyQt4 to do the user interface**

# How to use

### On Linux

Just download of the program using:

**HTTP**: git clone https://github.com/fernandobd42/Mutation-Tool---Python.git

**SSH**: git clone git@github.com:fernandobd42/Mutation-Tool---Python.git

**0 (EDIT JSON):**

Before run the program, go to the directory of program and edit the file: <b>operators.json</b>

![Json](https://raw.githubusercontent.com/fernandobd42/images/master/00.PNG)

so, insert the operator you want to find on the program where is <b>op1</b>, and insert the operator you want to replace per <b>op1</b>, where is <b>op2</b>, then insert the extension of file you want to find where is <b>ext</b>

Look, it's possible insert how many <b>operators</b> and <b>extension</b> of file you want, just follow the pattern of json file

**1 (INIT THE PROGRAM):**

Access the directory of the tool by shell, and run: </b>python gui.py</b>
Obs: you need to use the version 2.7 of python
```
➜  Mutation-Tool---Python git:(master) ✗ python gui.py
```
Then, select the directory of the original program. In the case, the directory of the program that you want to do the mutation test

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/01.PNG)

**2 (DO THE MUTATE):**

Just click on the little button <b>'Mutation'</b>

![Insert](https://raw.githubusercontent.com/fernandobd42/images/master/02.PNG)

**3 (RESULT):**

See the result on the shell, its possible to see how many operators were found and how many mutants were created  

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/03.PNG)
