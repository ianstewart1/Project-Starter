Project Starter
===============

I was tired of linking GitHub repositories every time I started on something new, so I decided to automate it as much as I could.

#### Dependencies:

- [pyYAML library (Python)](https://pyyaml.org/)
- [requests library (Python)](https://2.python-requests.org/en/master/)

#### Setup:

After cloning the repository, login credentials must be set in `config.yml`
- username: GitHub username
- token: Authorization token sourced from GitHub. MORE

**(WIP)** To make the batch file command work from any directory, the filepath must be added to the
local PATH variable. This can be achieved by running `setup.py` or executing the `addPath.bat` batch command.