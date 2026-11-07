import uuid
from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass
from entities.UserRegistration import UserRegistration
from entities.WebNotification import WebNotification

if TYPE_CHECKING:
    from entities.Application import Application

@dataclass
class Route:
    id: int
    uuid: uuid.UUID
    name: str
    description: str
    application: Optional['Application']
    userRegistrations: set[UserRegistration]
    webNotifications: set[WebNotification]
