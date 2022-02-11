from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if re.match("^[a-z]{3,}$", username):
            pass
        else:
            raise UserInputError("Username too short (minimum 3 characters)")

        if re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            pass
        else:
            raise UserInputError("Password too short (minimum 8 characters and has to include numbers)")