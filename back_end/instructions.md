step 1: activate poetry env "source $(poetry env info --path)/bin/activate"
step 2:


1. https://install.python-poetry.org -o install-poetry.py
2. python3 install-poetry.py
3. echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc 
4. source ~/.zshrc
5. poetry --version

brew install penv - python version management

remove python from the env - poetry env remove python

pyenv install 3.11.9
pyenv local 3.11.9  # Activate Python 3.9 for the current project

poetry env use python3.11


poetry install - 

poetry add lib - add the lib to the pyproject.toml

poetry lock - to generate poetry lock once you have added the libs

- to run the project with poetry environment command - poetry shell


