from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
from entities import *

if TYPE_CHECKING:
    from entities.Application import Application

@dataclass(frozen=True)
class Maintainer:
    id: int
    application: Optional["Application"]
    username: str
