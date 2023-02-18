import pytest


@pytest.mark.api
def test_user_exists(github_api):
    # 'defunkt' user name also can be used
    user = github_api.get_user('octocat')
    assert user['login'] == 'octocat'


@pytest.mark.api
def test_user_non_exists(github_api):

    r = github_api.get_user('butenko_sergii_123')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    # Note: the total count is valid as for 18.02.2023
    assert r['total_count'] == 31
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("somerepo_non_exist_test")
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char(github_api):
    r = github_api.search_repo("a")
    assert r['total_count'] != 0
