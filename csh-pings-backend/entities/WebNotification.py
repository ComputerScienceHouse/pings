import uuid
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from entities.Route import Route

@dataclass
class WebNotification:
    id: int
    uuid: uuid.UUID
    username: str
    route: Optional['Route']
    body: str
    date: datetime.datetime
    unread: bool
