from distutils.core import setup
setup(
    name='sensorflow',
    packages=['sensorflow'],
    version='2.3',
    description='Python driver for sensorflow devices',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/Sensorflow/client-python',
    download_url='https://github.com/Sensorflow/client-python/archive/master.zip',
    keywords=['sensor', 'data'],
    classifiers=['Topic :: Adaptive Technologies'],
    install_requires=['protocol-buffers-stream']
)