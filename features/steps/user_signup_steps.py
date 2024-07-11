from behave import given, when, then
from flask import Flask, session
import unittest
from app import app, users, User

# Dummy verification code for testing
TEST_VERIFICATION_CODE = "ABC123"

@given('I am on the signup page')
def step_given_on_signup_page(context):
    context.client = app.test_client()
    context.response = context.client.get('/signup')

@when('I enter a valid email "{email}"')
def step_when_enter_email(context, email):
    context.email = email

@when('I enter a valid password "{password}"')
def step_when_enter_password(context, password):
    context.password = password

@when('I enter the confirmation password "{confirm_password}"')
def step_when_enter_confirm_password(context, confirm_password):
    context.confirm_password = confirm_password

@when('I enter the verification code "{verification_code}"')
def step_when_enter_verification_code(context, verification_code):
    with context.client.session_transaction() as sess:
        sess['verification_code'] = TEST_VERIFICATION_CODE
    context.verification_code = verification_code

@when('I click the "Sign Up" button')
def step_when_click_signup_button(context):
    context.response = context.client.post('/signup', data={
        'email': context.email,
        'password': context.password,
        'confirmPassword': context.confirm_password,
        'verificationCode': context.verification_code
    }, follow_redirects=True)

@then('I should see "{message}"')
def step_then_see_message(context, message):
    assert message in context.response.data.decode()

@then('I should be redirected to the login page')
def step_then_redirected_to_login_page(context):
    assert context.response.request.path == '/login'

@then('the new user should be added to the users list')
def step_then_user_added_to_list(context):
    new_user = next((u for u in users if u.email == context.email), None)
    assert new_user is not None