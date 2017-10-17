from multiprocessing import Process
import core

core.do_imports()
for api in core._api_mains:
    p = Process(target=api)
    p.start()
