set -e

source credentials.sh

#git pull

if [ $(basename $(pwd)) != 'reddit' ];  then
	cd reddit
fi
source setup.sh
source bin/activate
export PYTHONPATH=$(pwd):$PYTHONPATH
python updatesubreddit/stylesheets.py ../css/RESUpdatesTest.css
