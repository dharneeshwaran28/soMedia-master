import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from bs4 import BeautifulSoup

# Registration Page Testing
# Checks if the registration page loads successfully.
@pytest.mark.django_db
def test_registration_page(client):
    response = client.get(reverse('accounts:register'))
    assert response.status_code == 200
    assert 'registration/register.html' in [t.name for t in response.templates]

# Validates the registration form data.
@pytest.mark.django_db
def test_registration_form_valid():
    data = {
        'username': 'testuser',
        'password1': 'testpassword123',
        'password2': 'testpassword123',
        'email': 'dharnee28@gmail.com',
    }
    form = RegistrationForm(data=data)
    assert form.is_valid()

# Tests the registration form submission process.
@pytest.mark.django_db
def test_registration_view_post(client):
    data = {
        'username': 'testuser',
        'password1': 'testpassword123',
        'password2': 'testpassword123',
        'email': 'dharnee28@gmail.com',
    }
    response = client.post(reverse('accounts:register'), data=data)
    assert response.status_code == 302  

    user_exists = get_user_model().objects.filter(username='testuser').exists()
    assert user_exists
    login_successful = client.login(username='testuser', password='testpassword123')
    assert login_successful

# Checks if redirect to homepage
@pytest.mark.django_db
def test_login_link_redirect(client):
    response = client.get(reverse('accounts:register'))
    assert response.status_code == 200  

    soup = BeautifulSoup(response.content, 'html.parser')
    login_link = soup.find('a', text='Login Page')['href']
    
    response = client.get(login_link)

    assert response.status_code == 200
    assert reverse('accounts:login') in response.request['PATH_INFO']