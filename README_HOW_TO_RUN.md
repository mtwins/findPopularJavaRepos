## How to Run the Scripts in this Repository

We developed and ran all of these scripts using Python 3 and the [Pycharm](https://www.jetbrains.com/pycharm/) / [IntelliJ](https://www.jetbrains.com/idea/) IDEs. Having Python 3 installed is a prerequisite to running the scripts. You can download Python 3 [here](https://www.python.org/downloads/).

_IMPORTANT: Reference instructions in the directory level README files to learn how to run a certain script._

For our project we ran the scripts in this order:
1) The scripts in the scripts/getRepositories directory to get the top/trending Java repositories
2) The scripts in the pmd and utils directories to get code smell data using the PMD tool for the Java repositories selected
3) The scripts/godClassCalc.py script to calculate god class metrics for the three static code analysis tools we used
4) The scripts in the scripts/repositoryMetrics directory to get metrics for the repositories we used in the project

