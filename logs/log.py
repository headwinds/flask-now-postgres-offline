import sys
import getopt
import logging

opts, args = getopt.getopt(sys.argv[1:], "1:", ["log="])

log_level = "INFO"
for opt, arg in opts:
    if opt in ("-1", "--log"):
        log_level = getattr(loggin, arg.upper())

logging.basicConfig(filename='./demo.log', level=logginf.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

for i in range(0, 100):
    if i % 5 == 0:
        logging.debug('Found a number divible by 5: {0}'.format(i))
    else:
        logging.info('At number {0}'.format(i))
logging.warning('Finished sequence')
