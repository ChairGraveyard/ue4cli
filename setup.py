from setuptools import setup

setup(
	name='ue4cli',
	version='0.0.15',
	description='Command-line interface for Unreal Engine 4',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Software Development :: Build Tools',
		'Environment :: Console'
	],
	keywords='epic unreal engine',
	url='http://github.com/adamrehn/ue4cli',
	author='Adam Rehn',
	author_email='adam@adamrehn.com',
	license='MIT',
	packages=['ue4cli'],
	zip_safe=True,
	install_requires = ['shellescape'],
	entry_points = {
		'console_scripts': ['ue4=ue4cli.cli:main']
	}
)
