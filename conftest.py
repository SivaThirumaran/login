from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()

    elif browser=='firefox':
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#hoof for adding enviroment info to HTML Reports

def pytest_configure(config):
    config._metadata['Project Name'] = 'OrgFarm'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Siva'

#hoof for delete/modify enviroment info to HTML Reports

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
