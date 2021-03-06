# AnalyzeRepositoriesMethods
This script analyzes each given repository's methods in all commits and store functions in a CSV file which are modified and have additional parameters in comparison to previous commits. CSV file's rows include: Commit Hash,File Name,Old Function Signiture and New Function Signiture

## Table of contents
* **[Requirements](#requirements)**
* **[Install](#install)**
* **[Tutorial](#tutorial)**
* **[Test](#test)**


## Requirements
You should install followings globally:

- Python3
- Git

Now you need to add pydriller library to your python's libraries. Just run the following command in cmd:

```
pip install pydriller
```

## Install

Just run the following command in cmd:

```
git clone https://github.com/kamranjafari93/AnalyzeRepositoriesMethods.git
```

## Tutorial

Simply run the script in cmd in src.py's directory:

```
python src.py
```

Now you need to enter an address. This may be a remote URL or a local one. For remote URL, enter a repositories' address like: https://github.com/ishepard/pydriller.git . For a local address, insert the repository's root address that contains .git directory. This address should be relative.

If everything goes right, you'll this message: "CSV FILE CREATED SUCCESSFULLY" and the CSV file would be created beside your script.

If commits contain no method's modification in defined condition, you'll see this message: "No Result! Test Other Repositories".

If something goes wrong or you enter the address wrong, you'll see this message: "Execution Failed. Check your address and try again".


## Test

This script has been tested on several repositories including: https://github.com/akarnokd/RxJava2Interop and https://github.com/realm/realm-java while the first one has a few commits but the latter one includes a plethora of commits. The results are included for view and download.
