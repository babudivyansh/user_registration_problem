import pytest
from user_registration import UserRegistration


@pytest.fixture
def user_obj_true():
    return UserRegistration("Divyansh", "Babu", "a@yahoo.com",
                            "91 9005202790", "A123@aaa")


@pytest.fixture
def user_obj_false():
    return UserRegistration("divyansh", "babu", "abc.@gmail.com",
                            "919005202790", "A123@aa")


def test_f_name_and_l_name_validation_success_fail(user_obj_true, user_obj_false):
    assert user_obj_true.f_name_and_l_name_validation() is True
    assert user_obj_false.f_name_and_l_name_validation() is False


def test_email_validation_success_fail(user_obj_true, user_obj_false):
    assert user_obj_true.email_validation() is True
    assert user_obj_false.email_validation() is False


def test_mobile_number_validation_success_fail(user_obj_true, user_obj_false):
    assert user_obj_true.mobile_number_validation() is True
    assert user_obj_false.mobile_number_validation() is False


def test_password_validation_success_fail(user_obj_true, user_obj_false):
    assert user_obj_true.password_validation() is True
    assert user_obj_false.password_validation() is False
