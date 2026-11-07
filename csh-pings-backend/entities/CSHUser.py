import os

class CSHUser:

    PINGS_ADMINS = {
        username.strip().lower()
        for username in os.getenv("CSH_PINGS_ADMINS", "").split(",")
        if username.strip()
    }

    def __init__(self, attributes):
        self.attributes = attributes
        self.full_name = attributes.get("name")
        self.username = attributes.get("preferred_username")
        self.groups = attributes.get("groups", [])

    def isRTP(self):
        return ("rtp" in self.groups or (self.username or "").lower() in
                self.PINGS_ADMINS)
