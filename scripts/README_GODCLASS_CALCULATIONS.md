## Prerequisite for God Class Calculations
* Static analysis tools (JDeodorant, PMD, Embold)
* List of number of god classes found for each repository

The following specifies how to run the static analysis tools to get the number of god classes.
<br/>
#### Install and Run JDeodorant
1. Go to Preferences in IntelliJ
2. Under Plugins, search for IntelliJDeodorant
3. Click Install.
4. Restart IDE when prompted.
5. Open IntelliJDdeodorant tab and click Refresh under God Class window.
6. Collect the number of god classes shown in the list.

#### Install and Run PMD
1. Follow the instructions in [PMD README](https://github.com/mtwins/findPopularJavaRepos/blob/main/pmd/README_PMD.md) to collect the number of god classes.

#### Install and Run Embold
1. Go to Preferences in IntelliJ
2. Under Plugins, search for IntelliJDeodorant
3. Click Install.
4. Restart IDE when prompted.
5. Right click on a java file and select "Scan all files with Embold".
6. Open Embold tab and click on Code Issues category.
7. Collect the number of god classes shown in the list.


## Instructions to run god class calculations script
1) Enter the number of the god classes found for each repository in the godClassMetricsInput array in god_class_calc.py. The numbers should be entered with comma and trailing space to separate each number.
2) Run the god_class_calc.py script to get metrics for the number of god classes found per repository for this tool.

_Note: This script is meant to be run separately for the data from each static code analysis tool (i.e. once for PMD data, Jdeodorant data, and Embold data)_



#### Command to run script from root directory in terminal
```
python scripts/god_class_calc.py
```
