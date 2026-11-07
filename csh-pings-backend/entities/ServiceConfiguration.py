import uuid
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.VerificationRequest import VerificationRequest
    from entities.UserRegistration import UserRegistration


@dataclass
class ServiceConfiguration:
    id: int
    uuid: uuid.UUID
    description: str
    username: str
    verified: bool
    verificationRequests: set[Optional['VerificationRequest']]
    userRegistraions: set[Optional['UserRegistration']]

