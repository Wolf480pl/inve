from setuptools import setup

setup(
    name='inve',
    version='0.0.1',
    install_requires=[
        'virtualenv',
    ],
    entry_points={
        'virtualenv.activate': [
            'inve = inve:InveActivator',
        ],
    },
    package_data={
        "inve": ["inve.sh"],
    },
)
