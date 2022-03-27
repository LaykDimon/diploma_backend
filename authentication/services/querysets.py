from authentication.models import User


class CustomUserQueryset:

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.objects.filter(id=user_id)

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.objects.filter(email=email)

    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        new_user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)

        return new_user