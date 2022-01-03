from __future__ import print_function

import os
import sys

from setuptools.command.install import install
from setuptools.command.test import test as TestCommand
from setuptools import setup, Command, find_packages
from wheel.bdist_wheel import bdist_wheel
import imp


with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

pip_command="pip3" if  sys.version_info[0]==3 else "pip"

class Install(install):
    """
        custom install command
        usage
            python setup.py install [--pip-args="{pip-args}"]
        notice
            pip-args: use "" to wrap your pip arguments
    """
    description = "install with specific pypi server"
    user_options = install.user_options + [('pip-args=', None, 'args for pip')]

    def initialize_options(self):
        install.initialize_options(self)
        self.pip_args = None

    def finalize_options(self):
        install.finalize_options(self)
        if self.pip_args is None:
            print('pip_args not set, using default https://pypi.org/simple/')

    def run(self):
        for dep in self.distribution.install_requires:
            install_cmd = pip_command+" install {} --disable-pip-version-check --no-cache-dir".format(dep)
            if self.pip_args is not None:
                install_cmd += ' ' + self.pip_args
            os.system(install_cmd)
        install.run(self)


class PyTest(TestCommand):
    """
        pytest
        usage
            python setup.py test [--disable-check] [-a {arg}|--pytest-args={arg}] [--pip-args="{pip-args}"]
        notice
            pip-args: use "" to wrap your pip arguments
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test"),
                    ('disable-check', None, 'skip checking requirement'),
                    ('pip-args=', None, 'args for pip')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''
        self.disable_check = None
        self.pip_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
        if self.pip_args is None:
            print('pip_args not set, using default https://pypi.org/simple/')

    def run(self):
        if self.disable_check is None:
            for dep in self.distribution.install_requires + self.distribution.tests_require:
                install_cmd = pip_command+" install {} --disable-pip-version-check --no-cache-dir".format(dep)
                if self.pip_args is not None:
                    install_cmd += ' ' + self.pip_args
                os.system(install_cmd)
            self.run_tests()
        else:
            print('skip checking requirements')
            self.run_tests()

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        # pytest should pass list object to main, so turn it to list if there's only one option
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


class BdistWheel(bdist_wheel):
    """
        custom bdist_wheel command
        usage
            python setup.py bdist_wheel [--pip-args="{pip-args}"]
        notice
            pip-args: use "" to wrap your pip arguments
    """
    description = "build wheel with specific pypi server"
    user_options = bdist_wheel.user_options + [('pip-args=', None, 'args for pip')]

    def initialize_options(self):
        bdist_wheel.initialize_options(self)
        self.pip_args = None

    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        if self.pip_args is None:
            print('pip_args not set, using default https://pypi.org/simple/')

    def run(self):
        for dep in self.distribution.install_requires:
            install_cmd = pip_command+" install {} --disable-pip-version-check --no-cache-dir".format(dep)
            if self.pip_args is not None:
                install_cmd += ' ' + self.pip_args
            os.system(install_cmd)
        bdist_wheel.run(self)


class Clean(Command):
    """
        custom clean command
        usage:
            python setup.py clean [-e|--egg]
    """
    description = "Cleans build files"
    user_options = [('egg', 'e', "Arguments to clean with .eggs folder")]

    def initialize_options(self):
        self.egg = None

    def finalize_options(self):
        if self.egg is None:
            print('not deleting .eggs folder')

    def run(self):
        cmd = dict(
            build="find ./ -name 'build' -exec rm -rf {} +",
            egg_info="find . -name '*.egg-info' -not -path './venv/*' -exec rm -rf {} +",
            dist="find ./ -name 'dist' -exec rm -rf {} +"
        )
        if self.egg is not None:
            cmd['eggs'] = "find ./ -name '.eggs' -exec rm -rf {} +"

        for key in cmd:
            print('remove {} folder ...'.format(key))
            os.system(cmd[key])


python_2 = sys.version_info[0] == 2
app_home = os.path.dirname(__file__)


def read(fname):
    with open(fname, 'rU' if python_2 else 'r') as f:
        return f.read()


version = imp.load_source('version', os.path.join(app_home, 'version.py')).version

install_req_path = os.path.join(app_home, 'requirements.txt')
install_require = [req.strip() for req in read(install_req_path).splitlines() if req.strip()]

install_lib_req_path = os.path.join(app_home, 'requirements-lib.txt')
install_lib_require = [req.strip() for req in read(install_lib_req_path).splitlines() if req.strip()]

dev_req_path = os.path.join(app_home, 'requirements-dev.txt')
dev_require = [req.strip() for req in read(dev_req_path).splitlines() if req.strip()]

setup(
    name="python-ci-gitlab",
    version=version,
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=install_require + install_lib_require,
    tests_require=dev_require,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=["example", "structure"],
    entry_points={},
    zip_safe=False,
    cmdclass={'install': Install,
              'test': PyTest,
              'bdist_wheel': BdistWheel,
              'clean': Clean}
)
