# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json

import pytest

from HW_14.task_1 import Project
from HW_14.user_class import User


@pytest.fixture
def project():
    return Project([User('14', 'Peter', '2'), User('154', 'Luisa', '3')])


@pytest.fixture
def admin():
    return User('14', 'Peter', '2')


@pytest.fixture
def user():
    return User('136', 'Brus', '3')


def test_login(project, admin):
    project.login(admin.u_id, admin.name)
    assert project.admin == admin


def test_add_user(project, user, admin):
    project.login(admin.u_id, admin.name)
    project.add_user(user.u_id, user.name, user.level)
    assert user in project.users_lst


def test_del_user(project, admin):
    project.login(admin.u_id, admin.name)
    project.del_user(project.users_lst[1].u_id, project.users_lst[1].name, project.users_lst[1].level)
    assert len(project.users_lst) == 1


if __name__ == '__main__':
    pytest.main(['-v'])
