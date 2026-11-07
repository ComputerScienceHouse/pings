import uuid
from entities.Maintainer import Maintainer
from entities.ExternalToken import ExternalToken
from entities.Route import Route
from entities.CSHUser import CSHUser

# from dataclasses import dataclass

# @dataclass
class Application:
    id: int
    uuid: uuid.UUID
    name: str
    description: str
    webURL: str
    published: bool
    maintainers: set[Maintainer]
    externalTokens: set[ExternalToken]
    routes: set[Route]

    def isMaintainer(self, u: CSHUser | str) -> bool:
        uLower = None
        isUMaintainer = False
        if type(u) is CSHUser:
            isUMaintainer = u.isRTP()
            uLower = u.username.lower()
        elif type(u) is str:
            uLower = u.lower()
        for maintainer in self.maintainers:
            if type(u) is CSHUser:
                if uLower == maintainer.username:
                    isUMaintainer = True
            elif type(u) is str:
                if uLower == maintainer:
                    isUMaintainer = True
        return isUMaintainer

