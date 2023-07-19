# Pyhton-Weather-App
This is a python weather app which is CLI (command-line-interface) based, and can also be used as a backend for Android/IOS or Web Application

## Packages required
1. python-dotenv
2. requests

# NOTE : 
`It is recommended from my side to create a virtual environment before running this and installing all the packages in that virtual environment`

## To Run
Make a `.env` file and add an environment variable in the application or add the variable in system environment with the name `API_KEY` and assign it to your API key

---

`API Key` is not provided in the repo

---
## Important : 
If `API_KEY` is getting used as a system environment variable and `.env` file is not being used then comment out `load_dotenv()` in the `9th` line