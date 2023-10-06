#!/bin/bash

DIR=$(dirname "${BASH_SOURCE[0]}")
DB_NAME=db_name
DB_USER=db_user
BUCKET_NAME=bucket_name
DUMP_PATH="$DIR/$DB_NAME_$(date +"%Y-%m-%d@%H-%M").dump"

echo "
started snapshot script ....
DB_NAME=$DB_NAME
DB_USER=$DB_USER
BUCKET_NAME=$BUCKET_NAME
DUMP_PATH=$DUMP_PATH
"

#echo "hello" | cat > $DUMP_PATH

# dump database
pg_dump -U $DB_USER $DB_NAME>$DUMP_PATH -W

# sync to s3
aws s3 cp $SUMP_PATH s3://$BUCKET_NAME 

# remove dump path
rm $DUMP_PATH
