import sys

from unifed.frameworks.test import protocol
from unifed.frameworks.test.workload_sim import *


def run_protocol():
    print('Running protocol...')
    protocol.pop.run()  # FIXME: require extra testing here

