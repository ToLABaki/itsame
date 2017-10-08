class User:
    def __init__(self, db, username, password=None):
        self._db = db
        self.username = username
        if password:
            self._register()
        self._authenticate()

    def _register(self):
        raise NotImplementedError("Registration is not implemented")

    def _authenticate(self):
        raise NotImplementedError("Authentication is not implemented")

    @property
    def set_username(self, new):
        if self._db.rename(self.username, new):
            self.username = new
            return True
        return False

    def __delitem__(self, key):
        return self._db.hdel(self.username, key)

    def __getitem__(self, key):
        return self._db.hget(self.username, key)

    def __setitem__(self, key, value):
        return self._db.hset(self.username, key, value)

    def __len__(self):
        return self._db.hlen(self.username)

    def __repr__(self):
        return self._db.hgetall(self.username)

    def keys(self):
        return self._db.hkeys(self.username)

    def has_key(self, key):
        return self._db.hexists(self.username, key)
