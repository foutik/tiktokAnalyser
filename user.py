
class User(object):
    def __init__(self, json_dict):
        # pass json author
        self.username = json_dict.get("uniqueId", None)
        self.userId = json_dict.get("id", None)
        self.signature = json_dict.get("signature", None)
        self.verified = json_dict.get("verified")
        self.secret = json_dict.get("secret")

