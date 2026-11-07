import datetime
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.ServiceConfiguration import ServiceConfiguration


@dataclass
class VerificationRequest:
    id: int
    serviceConfiguration: Optional['ServiceConfiguration']
    token: str
    expire: datetime.datetime
