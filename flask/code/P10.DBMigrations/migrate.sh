#!/bin/sh

MONGOURI="mongodb://root:jala@localhost:27017/traveler?authSource=admin"

echo "\nBefore Migration"
pymongo-migrate show -u $MONGOURI -m ./migrations/

echo "\nRunning Migration"
pymongo-migrate migrate -u $MONGOURI -m ./migrations/

echo "\nAfter Migration"
pymongo-migrate show -u  $MONGOURI -m ./migrations/

echo "\nMigration Graph"
pymongo-migrate graph -u  $MONGOURI -m ./migrations/
