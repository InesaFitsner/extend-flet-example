# extend-flet-example
Integrating existing Flutter packages into Flet app example

# if python interpreter is not selected
Virtualenv
Executable:     /Users/inesa/Library/Caches/pypoetry/virtualenvs/flet-spinkit-E2zIzyoK-py3.11/bin/python
command shift p -> select interpreter -> enter interpreter path -> <Executable>

# connect python and flutter

## run python app
poetry run flet run (in current dir)
should show red rectangle "unknown control"

## Unset FLET_VIEW_PATH

printenv | grep FLET
(check if environment variables are there)
Output:
FLET_VIEW_PATH=/Users/inesa/Documents/projects/flet-dev/flet/client/build/macos/Build/Products/Release
FLET_WEB_PATH=/Users/inesa/Documents/projects/flet-dev/flet/client/build/web

Unset FLET_VIEW_PATH:
export FLET_VIEW_PATH=

## build macos app
inesa@Inesas-Air flet_spinkit_app % poetry run flet build macos

## run compiled app
open /Users/inesa/Documents/projects/InesaFitsner/extend-flet-example/python/flet_spinkit_app/build/macos/flet_spinkit_app.app

