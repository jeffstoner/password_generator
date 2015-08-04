
from __future__ import print_function
import random
import string
from optparse import OptionParser

def generate(len=15, alphaNumOnly=False):
    """ generate - Generates a random string of characters of the specified length and character domain
        :param length: The number of characters the resulting password should be (int)
        :param alphaNumOnly: Flag to restrict the password to alphanumeric characters or to include punctuation (boolean)
        :return: A string in the character domain selected
    """
    if len <=0:
        # smart-ass
        return ''

    if alphaNumOnly:
        # restrict to ASCII letters and numbers
        pool = string.ascii_letters + string.digits
    else:
        # Use ASCII letters, numbers and printable punctuation characters
        pool = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.SystemRandom().choice(pool) for _ in range(len))

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-l", "--length", dest="len", help="The length of the password to generate", default=15)
    parser.add_option("-a", "--alphanum", dest="alphanum", action="store_true", help="Generate a password using only Alpha-Numeric characters", default=False)

    (args, unused) = parser.parse_args()

    print(generate(len=int(args.len), alphaNumOnly=args.alphanum))
