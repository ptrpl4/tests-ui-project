# Basic sceleton for Selenium projects

Deps:
- pytest
- selenium
- pytest-xdist

## Python Setup
python v3.8+
[pipenv](https://docs.pipenv.org/).
install `pip install pipenv`

## WebDriver Setup

[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
[geckodriver](https://github.com/mozilla/geckodriver/releases)

ChromeDriver and geckodriver must be installed on the
[system path](https://en.wikipedia.org/wiki/PATH_(variable)).

### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)

### WebDriver Setup for *NIX

To install ChromeDriver and geckodriver on Linux, macOS, and other UNIX variants,
simply move them to the `/usr/local/bin/` directory:

```bash
$ mv /path/to/ChromeDriver /usr/local/bin
$ mv /path/to/geckodriver /usr/local/bin
```

This directory should already be included in the system path.
For troubleshooting, see:

* [Setting the path on macOS](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
* [Setting the path on Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)

### Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

```bash
$ ChromeDriver
$ geckodriver
```

You may or may not see any output.
Just verify that you can run them without errors.
Use Ctrl-C to kill them.

## Project Setup
Run `pipenv install` to install the dependencies.
To activate this project's virtualenv, run `pipenv shell`
Alternatively, run a command inside the virtualenv with `pipenv run ...`
Run `pipenv run python -m pytest tests/test_pytest.py` to check pytest is working