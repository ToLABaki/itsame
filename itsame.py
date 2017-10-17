import core

core.do_imports()
for api in core._api_mains:
    api()
