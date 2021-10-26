from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'RoboHashpy',         # How you named your package folder (MyLib)
  packages = ['RoboHashpy'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An api wrapper for RoboHash',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = 'ShadowRanger5',                   # Type in your name
  author_email = 'namankrocks@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/namanko/RoboHashpy',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['Hash','RoboHash'],   # Keywords that define your package best
  install_requires=['requests' ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',
  ],
)
