# Simple runner for train in colab
__requires__ = 'g2p-seq2seq==6.2.2a0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('g2p-seq2seq==6.2.2a0', 'console_scripts', 'g2p-seq2seq')()
    )
