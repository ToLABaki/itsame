import core

class Dummy(core.User):
    def _register(self, password):
        return self.__setitem__("password", password)

    def _authenticate(self, password):
        if self.__getitem__("password").decode() != password or password is None:
            raise core.FailedToAuthenticate(self.__getitem__("password") + " vs " + password)
