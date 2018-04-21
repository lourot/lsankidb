set -e

python3.5 -m unittest discover -v
python3.5 -m pylint src/ test/
