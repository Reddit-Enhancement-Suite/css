CSS_FILE=${1:-'../css/RESUpdatesTest.css'}
echo $CSS_FILE

set -e

source credentials.sh

#git pull

if [ $(basename $(pwd)) == 'reddit' ];  then
	pushd ..
else
	if [ $(basename $(pwd)) == 'aws-cloudflare' ];  then
		pushd ..
	fi
fi


pushd aws-cloudflare
source ../setup-virtualenv.sh
source bin/activate
export PYTHONPATH=$(pwd):$PYTHONPATH
FILE=$CSS_FILE
python pushtohosting.py $FILE
popd




pushd reddit
source ../setup-virtualenv.sh
source bin/activate
export PYTHONPATH=$(pwd):$PYTHONPATH
FILE=$CSS_FILE
python updatesubreddit/stylesheets.py $FILE
popd

popd #Back to original folder
