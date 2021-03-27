## NextZen PhotoBooker automation testing

```sh

├── common                      //< common classes and methods
│   ├── api                     //< api core classes 
│   |   ├── config              //< general configuration classes
│   |   ├── helpers             //< database helper, support photoBooker request helper, token helper,...
├── tests                       //< test packages home folder
│   ├── api                     //< api tests and related classes
│   Pipfile                     //< required libraries
│   Pytest.ini                  //< Pytest configuration file
│   README.md                   //< Starting guideline
```

## Getting Started

This is the quick and easy getting started assuming you already have git and pip installed.

```sh

# navigate home directory
cd ~/zf-automation-photobooker

# Install the required items
1. Remove your current version of virtualenv (optional)
pip uninstall virtualenv

2. Install pipenv
pip install --user pipenv
pip3 install -U pipenv

3. Testing the installation
pipenv --version

4. Install dependencies
pipenv install Pipfile 
If you have multiple python version use below command
pipenv install --python=/usr/bin/<python_directory> Pipfile

5. Switch to pipenv virtual environment
pipenv shell

If you want to upgrade changes in Pipfile? Just do $ pipenv update. 
For more details please refer https://docs.pipenv.org/en/latest/basics/

6. Run tests 
# To run all the test scenarios:
pytest

# to run scenarios with specific tags:
pytest -m get_colors
```

## Pytest - Test Runner
Method with test_ or _test will be collected, Pytest support several way to run test:
- Run test with method: ```pytest test_class.py```
- Run tests in a package: ```pytest testing/```
- Run tests by marker expressions: ```pytest -m test_post_create_new_customer``` (custom marker is defined by this line of code ```@pytest.mark.<custom_marker_name>```)


## Pytest - Run Test with multiple environments
```ENV=TEST pytest``` OR 
```ENV=DEV pytest```


## Run test with Parallel mode

- Running tests in a Python subprocess

```pytest -d --tx <number of sub processes>*popen//python=python```

## Set system environment variables for running UI smoke tests using Chrome mobile emulation in headless mode
```MOBILE_EMULATION=True HEADLESS=True pytest -d --tx 2*popen//python=python tests/ui -v -m frontend_smoke```

## Set system environment variables for running UI Regression tests using Real Mobile Devices on Sauce Labs
```GRID=True SAUCE_LABS=True pytest -d --tx 2*popen//python=python tests/ui -v -m frontend_regression```

## Report generating
This report required allure cli, please refer this link to install https://docs.qameta.io/allure/#_installing_a_commandline

Follow below step to trigger test and generate report
```sh
# run test with this command
pytest --alluredir=allure_results

# generate report from the results.
allure serve allure_results
```

## IDE

### PyCharm


https://www.jetbrains.com/pycharm/

Debug configuration: https://www.jetbrains.com/help/pycharm/run-debug-configuration-py-test.html

### VSCODE

https://code.visualstudio.com/

Debug configuration: https://code.visualstudio.com/docs/python/testing
