set -e

python3.5 -m pytest test/
python3.5 -m pylint src/ test/
python3.5 -m pytest --cov=./ test/
