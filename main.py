import sys
from revivesocialmedia import ReviveSocialMedia
import platform
import os


chrome_driver_map = {
    '91': '91.0.4472.19',
    '90': '90.0.4430.24',
    '89': '89.0.4389.23',
    '88': '88.0.4324.96'
}

def install_package(version=None):
    import pip
    if version:
        version = chrome_driver_map.get(version.split('.')[0])
        package = 'chromedriver-py=={}'.format(version)
    else:
        package = 'chromedriver-py'
    print('Installing {}'.format(package))
    if hasattr(pip, 'main'):
        pip.main(['install', package])
        print('Successfully installed {}'.format(package))
        return True
    else:
        pip._internal.main(['install', package])
        print('Successfully installed {}'.format(package))
        return True
    

def check_mac_chrome_version():
    import plistlib
    if os.path.exists("/Applications/Google Chrome.app"):
        if os.path.exists("/Applications/Google Chrome.app/Contents/Info.plist"):
            pl = plistlib.readPlist("/Applications/Google Chrome.app/Contents/Info.plist")
            pver = pl["CFBundleShortVersionString"]
            if install_package(pver):
                print('Successfully installed correct chromdriver!')
        else:
            print('Unable to find Google Chrome Info.plist!')
    else:
        print('Unable to find Google Chrome.app!')

def main(argv=None):
    if platform.system() == 'Darwin':
        check_mac_chrome_version()
    elif platform.system() == 'Linux':
        install_package()
    if argv == 'oss':
        ReviveSocialMedia().oss()
    elif argv == 'blog':
        ReviveSocialMedia().blog()
    else:
        raise EnvironmentError('Please provide either oss or blog as input')

if __name__ == '__main__':
    main(argv=sys.argv[1])
