from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Application import Application

@dataclass
class ExternalToken:
    id: int
    application: Optional['Application']
    token: str
    note: str
