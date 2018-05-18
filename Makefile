release:
	./setup.py sdist && ./setup.py build && twine upload dist/* && git push && git push --tags

build:
	./setup.py build

test:
	./setup.py build && ./setup.py test


clean:
	rm -rf dist/ && rm -rf build/ && rm -rf deps/ && rm ecapy/eca.so && rm -rf ecapy.egg-info

