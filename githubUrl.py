import sys
import json
import yaml
import requests

def main():

	# Load authorization info from YAML file
	with open("config.yml", "r") as ymlFile:
		cfg = yaml.load(ymlFile, Loader=yaml.CLoader)

	# Base url
	url = "https://api.github.com/user/repos"

	# Set auth values and build repository payload
	username = str(cfg["username"]) 
	token = str(cfg["token"])
	repo = {
		"name": str(sys.argv[1]),
		"description": "Created via GitHub API",
		"auto_init": "true"
	}

	# Records GitHub API response in txt file. Used for debugging
	response = open("response.txt", "w")

	with requests.Session() as session:

		# Create new repository in Github
		r = session.post(url, auth=(username, token), data=json.dumps(repo))
		response.write(r.text)

	response.close()

	# Print username to command line for shell code to use
	print(username)

main()