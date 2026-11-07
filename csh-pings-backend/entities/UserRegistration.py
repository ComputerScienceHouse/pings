import uuid
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
from entities.ServiceConfiguration import ServiceConfiguration

if TYPE_CHECKING:
    from entities.Route import Route

@dataclass
class UserRegistration:
    id: int
    uuid: uuid.UUID
    username: str
    route: Optional['Route']
    serviceConfiguration: ServiceConfiguration
