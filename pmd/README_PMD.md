## Instructions to run PMD script
1) Clone the projects you want to analyze to a local project directory(manually or using the utils/clone_repositories.py script) and build them for best results
2) Update the path in getPmdData.sh to point to the local project directory that you cloned the projects into
3) Update the metrics_directory in pmd_automation.py to point to the directory where the pmd analysis results should get stored
4) Download and install PMD from the following [website](https://pmd.github.io/) 
5) Run the script using the command below to get a csv file of the amount of code smells that PMD detected for each of the projects in the project directory specified

### Command to run script from root directory in terminal
```
python3 pmd/pmd_automation.py
```