from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def get_by_id(
        self,
        db: Session,
        user_id: int,
    ) -> User | None:

        return db.scalar(
            select(User).where(User.id == user_id)
        )

    def get_by_phone(
        self,
        db: Session,
        phone: str,
    ) -> User | None:

        return db.scalar(
            select(User).where(User.phone == phone)
        )

    def create(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def update(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.commit()
        db.refresh(user)

        return user