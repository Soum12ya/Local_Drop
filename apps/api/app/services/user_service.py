from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        data: UserCreate,
    ) -> User:

        existing_user = self.repository.get_by_phone(
            db,
            data.phone,
        )

        if existing_user:
            raise ValueError(
                "A user with this phone number already exists."
            )

        user = User(
            phone=data.phone,
            name=data.name,
            email=data.email,
        )

        return self.repository.create(db, user)

    def get_user(
        self,
        db: Session,
        user_id: int,
    ) -> User | None:

        return self.repository.get_by_id(
            db,
            user_id,
        )

    def update_user(
        self,
        db: Session,
        user_id: int,
        data: UserUpdate,
    ) -> User | None:

        user = self.repository.get_by_id(
            db,
            user_id,
        )

        if not user:
            return None

        if data.name is not None:
            user.name = data.name

        if data.email is not None:
            user.email = data.email

        if data.avatar_url is not None:
            user.avatar_url = data.avatar_url

        return self.repository.update(db, user)