# AnalyzeRepositoriesMethods
This script analyzes each given repository's methods in all commits and store functions in a CSV file which are modified and have additional parameters in comparison to previous commits. CSV file's rows include: Commit Hash,File Name,Old Function Signiture and New Function Signiture

## Table of contents
* **[Requirements](#requirements)**
* **[Install](#install)**
* **[Tutorial](#tutorial)**


## REQUIREMENTS
You Should Install followings:

- Python3
- Git

Now you need to add pydriller library to your python's libraries. Just run the following command in cmd:

```
pip install pydriller
```

## INSTALL

Just run the following command in cmd:

```
clone 
```

## INSTALL

Simply run the script in cmd:

```
python src.py
```
## Tutorial

Now you need to enter an address. This may be a remote URL or a local one. For remote URL, enter a repositories' address like: https://github.com/ishepard/pydriller.git . For a local address, insert the root repository's address that contains .git directory. this address should be relative.

If everything goes right, you'll this message: "CSV FILE CREATED SUCCESSFULLY" and the CSV file would be created beside your script.
If commits contain no method's modification in defined condition, you'll see this message: "No Result! Test Other Repositories" .
If something goes wrong or you enter the address wrong, you'll see this message: "Execution Failed. Check your address and try again"
