Project Starter
===============

I was tired of linking GitHub repositories every time I started on something new, so I decided to automate it as much as I could.

By using the command `project` paired with a (one word) project name, this script will create a new repository and link it with a folder in the directory the command is called from. Additionally a `readme.md` file will be created with the repo.

## Dependencies:

- [pyYAML library (Python)](https://pyyaml.org/)
- [requests library (Python)](https://2.python-requests.org/en/master/)

## Setup:

After cloning th erepository, login credentials must be set in `config.yml`
- **username**: GitHub username
- **token**: [Authorization token sourced from GitHub.](https://github.com/settings/tokens) (Make sure to give Repository access when creating the token!)

**(WIP)** To make the batch file command work from any directory, the filepath must be added to the local PATH variable. This can be achieved by running `setup.py` or executing the `addPath.bat` batch command.