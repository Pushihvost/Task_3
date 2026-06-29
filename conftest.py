import pytest
from selenium import webdriver
from data.urls import BASE_URL
from api.user_api import UserApi
from helpers.generators import generate_user

@pytest.fixture
def authorized_user():

    user_api = UserApi()

    user_data = generate_user()

    create_response = user_api.create_user(user_data)

    access_token = create_response.json()['accessToken']

    yield {
        'user': user_data,
        'token': access_token
    }

    user_api.delete_user(access_token)

@pytest.fixture(params=["Firefox", "Chrome"])
def driver(request):

    if request.param == "Firefox":
        driver = webdriver.Firefox()

    elif request.param == "Chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()
