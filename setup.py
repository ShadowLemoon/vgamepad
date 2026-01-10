from setuptools import setup, find_packages
import platform


assert platform.system() in ('Windows', 'Linux'), "vgamepad is only supported on Windows and Linux."

is_windows = platform.system() == 'Windows'

# Note: ViGEmBus installation is now handled at runtime when the user first creates a gamepad object,
# rather than during pip install. This ensures that the MSI installer files are available at the correct path.

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vgamepad',
    packages=[package for package in find_packages()],
    version='0.1.0',
    license='MIT',
    description='Virtual XBox360 and DualShock4 gamepads in python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yann Bouteiller',
    url='https://github.com/yannbouteiller/vgamepad',
    download_url='https://github.com/yannbouteiller/vgamepad/archive/refs/tags/v0.1.0.tar.gz',
    keywords=['virtual', 'gamepad', 'python', 'xbox', 'dualshock', 'controller', 'emulator'],
    install_requires=['libevdev~=0.11'] if not is_windows else [],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Games/Entertainment',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    package_data={'vgamepad': [
        'win/vigem/client/x64/ViGEmClient.dll',
        'win/vigem/client/x86/ViGEmClient.dll',
        'win/vigem/install/x64/ViGEmBusSetup_x64.msi',
        'win/vigem/install/x86/ViGEmBusSetup_x86.msi',
    ]}
)
