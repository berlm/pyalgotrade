#!/usr/bin/env python

# PyAlgoTrade
#
# Copyright 2011-2015 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyalgotrade_python3',
    version='0.1',
    description='Adaptation of Python Algorithmic Trading to python3 for pip',
    long_description='Adaptation of Python Algorithmic Trading by Gabriel Martin Becedillas Ruiz to python3 for pip.',
    author='Mikhail Berlinkov',
    author_email='mberl_upwork@mail.ru',
    url='http://gbeced.github.io/pyalgotrade/',
    download_url='https://github.com/berlm/pyalgotrade',
    packages=[
        'pyalgotrade',
        'pyalgotrade.barfeed',
        'pyalgotrade.bitcoincharts',
        'pyalgotrade.bitstamp',
        'pyalgotrade.broker',
        'pyalgotrade.dataseries',
        'pyalgotrade.feed',
        'pyalgotrade.optimizer',
        'pyalgotrade.stratanalyzer',
        'pyalgotrade.strategy',
        'pyalgotrade.talibext',
        'pyalgotrade.technical',
        'pyalgotrade.tools',
        'pyalgotrade.twitter',
        'pyalgotrade.utils',
        'pyalgotrade.websocket',
    ],
    install_requires=[
        "numpy",
        "pytz",
        "python-dateutil",
        "requests",
    ],
    extras_require={
        'Scipy': ["scipy"],
        'TALib': ["Cython", "TA-Lib"],
        'Plotting': ["matplotlib"],
        'Bitstamp': ["ws4py>=0.3.4", "tornado"],
        'Twitter': ["tweepy"],
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.3',
)
