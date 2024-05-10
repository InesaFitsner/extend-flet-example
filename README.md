
# extend-flet-example
Integrating existing Flutter packages into Flet app example

### if python interpreter is not selected
Virtualenv
Executable:     /Users/inesa/Library/Caches/pypoetry/virtualenvs/flet-spinkit-E2zIzyoK-py3.11/bin/python
command shift p -> select interpreter -> enter interpreter path -> <Executable>

## Connect Python and Flutter

### run python app
poetry run flet run (in current dir)
should show red rectangle "unknown control"

### Unset FLET_VIEW_PATH

printenv | grep FLET
(check if environment variables are there)

You will get output with values of environment variables with FLET is their name were set before :
FLET_VIEW_PATH=<path>
FLET_WEB_PATH=<path>

Unset FLET_VIEW_PATH:
If FLET_VIEW_PATH is not enmpty, unset it by running this commands:
export FLET_VIEW_PATH=

### build macos app
(you have to be in the folder were your main.py is)
poetry run flet build macos

### run compiled app
(you have to be in the folder were your main.py is, or use full path)
open build/macos/flet_spinkit_app.app
