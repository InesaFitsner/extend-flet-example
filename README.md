
# extend-flet-example

Integrating existing Flutter packages into Flet app example

## Create Flet Dart package

```
flutter create --template=package <package_name>
```

Flet Dart package should consist of the following files:
```
└── <package_name>
    ├── lib
    │   ├── <package_name>.dart
    │   └── src
    │       ├── create_control.dart
    │       └── <control_name>.dart
    └── pubspec.yaml
```

## Create Flet Python control and app that uses it

## Connect Python and Flutter

### Unset FLET_VIEW_PATH

Check if environment variables are there:

```
printenv | grep FLET
```


You will get output with values of environment variables with FLET is their name were set before :
FLET_VIEW_PATH=<path>
FLET_WEB_PATH=<path>

Unset FLET_VIEW_PATH:
If FLET_VIEW_PATH is not enmpty, unset it by running this commands:

```
export FLET_VIEW_PATH=
```

### create pubspec.yaml in the same directory as main.py

```yaml
dependencies:
  flet_spinkit:
    path: {absolute-path-to-flet-dart-package-folder}
```
### build macos app
(you have to be in the folder were your main.py is)

```
poetry run flet build macos
```

To show more logs:
```
poetry run flet build macos -v
```

### run compiled app
(you have to be in the folder were your main.py is, or use full path)

```
open build/macos/flet_spinkit_app.app
```

### if you need to upgrade flet version

- change flet dependency to a new version in both python/pyproject.toml and flutter/flet_spinkit/pubspec.yaml
- while in python folder, run:
  ```
  poetry lock
  ```
  ```
  poetry install
  ```
- now build macos app and run compiled app

