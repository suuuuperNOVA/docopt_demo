# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [--arg4=<arg4>]
Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is an optional option)
""" 

from docopt import docopt


def main(opt_):
    print(opt_)
    print(type(opt_))
    print(opt_['--arg4'])


if __name__ == "__main__":
    opt = docopt(__doc__)
    main(opt)