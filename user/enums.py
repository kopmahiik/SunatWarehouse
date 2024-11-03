from django.db.models import TextChoices


class UserTypeChoices(TextChoices):
    ADMIN = "ADMIN", "Админ"
    OWNER = "OWNER", "Владелец"
