**This is a project to create a mutation tool to mutate java programs. The tool is written in Python, using the library PyQt4 to do the user interface**

# How to use

### On Linux

### FIRSTLY

Download of the program using:

**HTTP**: git clone https://github.com/fernandobd42/Mutation-Tool---Python.git

**SSH**: git clone git@github.com:fernandobd42/Mutation-Tool---Python.git

### SECONDLY

Run into the directory Mutation-Tool---Python then Install dependencies/requirements, to do this, just open the terminal and run:

**Firstly** sudo chmod +x aux.sh

**Secondly** sudo ./aux.sh

**Thirdly** during the install, type some 'ENTER', stay attentive

### THIRDLY 

**0 (EDIT JSON):**

Before run the program, go to the directory of program and edit the file: <b>operators.json</b>.

Note the first operator with "name": "Original", this operator is used as the model of original program to be compared with the mutants. That's why the "op1" and the "op2" are equals. So don't changed the program to the result be the model of original progam.

![Json](https://raw.githubusercontent.com/fernandobd42/images/master/00.PNG)

so, insert the name of operator where is <b>name</b>, then insert the operator you want to find on the program where is <b>op1</b>, and insert the operator you want to replace per <b>op1</b>, where is <b>op2</b>

Look, it's possible insert how many <b>operators</b> you want, just follow the pattern of json file.

**1 (EDIT screenshot.py):**

In screenshot.py file alter manually the <b>path</b> of java main file (the current path where is java file that has main class) where is red. Set the right path to program run rightly.

![Screenshot](https://raw.githubusercontent.com/fernandobd42/images/master/01.PNG)

**2 (INIT THE PROGRAM):**

Access the directory of the tool by shell, and run: <b>python gui.py</b><br>
Obs: you need to use the version 2.7 of python.
```
➜  Mutation-Tool---Python git:(master) ✗ python gui.py
```
***1.1 (Select the Project):*** Select the directory of the <b>original program</b>. In the case, the directory of the program that you want to do the mutation test.

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/02.PNG)

***1.2 (Select the Json File):*** Then, select the <b>json file</b>. In case the json file that has the operators.

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/03.PNG)

***1.3 (Select the Main Java File):*** Then, select the <b>main java file</b> (the java file that has the main class). In case the java file will be executed.

![Init](https://raw.githubusercontent.com/fernandobd42/images/master/04.PNG)

**3 (DO THE MUTATION):**

Just click on the little button <b>'Mutation'</b>.

![Mutate](https://raw.githubusercontent.com/fernandobd42/images/master/05.PNG)

**4 (RESULT):**

Its possible to see the result on the <b>shell</b> and on <b>MutateTool.log</b>, being possible to see how many operators were found and how many mutants were created. Also it is possible to see the image of each mutant program running on images directory that locate in the same directory of mutation tool.

![Result](https://raw.githubusercontent.com/fernandobd42/images/master/06.PNG)

See on the below image the result of comparating images do by the tool:
Firstly, see the quantity of mutants that have the same interface of the original program, in other words, which mutants survived. 
After, see the names of images that have the same interface to be possible confirm whether the tool really is correct. 
After, see the quantity of mutants that have a different interface of the original program, in other words, which mutants died. 
After, see the names of images that have the different interface to be possible confirm whether the tool really is correct. 
Lastly, see how many operators past by json not found in the original program.

![Result](https://raw.githubusercontent.com/fernandobd42/images/master/07.PNG)
