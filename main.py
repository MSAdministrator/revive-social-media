import sys
from revivesocialmedia import ReviveSocialMedia


def main(argv=None):
    if argv == 'oss':
        ReviveSocialMedia().oss()
    elif argv == 'blog':
        ReviveSocialMedia().blog()
    else:
        raise EnvironmentError('Please provide either oss or blog as input')

if __name__ == '__main__':
    main(argv=sys.argv[1])
