print("Hello, CHel!")
print("Buy!")

import platform
import sys

info = 'OS info is \n {}\n\n python version is {} {}'.format(platform.uname(),  sys.version, platform.architecture())

print(info)
