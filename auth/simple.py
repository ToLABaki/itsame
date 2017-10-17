import core

class User(core.User):
    def _register(self, password):
        return self.__setitem__("password", password)

    def _authenticate(self, password):
        if password is None:
            raise core.FailedToAuthenticate("Password for user %s can't be empty" \
                    % self.username)

        if self.__getitem__("password").decode() != password:
            raise core.FailedToAuthenticate("Failed to authenticate user %s" % \
                    self.username)
