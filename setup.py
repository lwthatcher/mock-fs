"""Setup for mock-fs"""

from distutils.core import setup
import mockfs

setup(
    name='mock-fs',
    version=mockfs.__version__,
    description='Mock file-system. Avoid actually using this.',
    author='Lawrence Thatcher',
    author_email='lwthatcher@msn.com',
    url='https://github.com/lwthatcher/mock-fs',
    packages=['mockfs']
)