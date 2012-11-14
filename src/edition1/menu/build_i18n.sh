#!/bin/sh
#
# Shell script to manage .po files.
#
# Run this file in the folder main __init__.py of product
#
# Copyright 2010 mFabrik http://mfabrik.com
#
# http://plone.org/documentation/manual/plone-community-developer-documentation/i18n/localization
#

CATALOGNAME="edition1.menu"

# List of languages
LANGUAGES="en nl"

# Create locales folder structure for languages
install -d locales
for lang in $LANGUAGES; do
    install -d locales/$lang/LC_MESSAGES
done

# Assume i18ndude is on your path
command -v i18ndude &>/dev/null || { echo "I require i18ndude but I cannot find it. Aborting." >&2; exit 1; }


#
# Do we need to merge manual PO entries from a file called manual.pot.
# this option is later passed to i18ndude
#
if test -e locales/manual.pot; then
        echo "Manual PO entries detected for the $CATELOGNAME domain"
        MERGE="--merge locales/manual.pot"
else
        echo "No manual PO entries detected for the $CATALOGNAME domain"
        MERGE=""
fi

# Rebuild .pot
echo "Rebuilding the .pot file for $CATALOGNAME"
i18ndude rebuild-pot --pot locales/$CATALOGNAME.pot $MERGE --create $CATALOGNAME .

# Compile po files
for lang in $(find locales -mindepth 1 -maxdepth 1 -type d); do

    if test -d $lang/LC_MESSAGES; then

        PO=$lang/LC_MESSAGES/${CATALOGNAME}.po

        # Create po file if not exists
        touch $PO

        # Sync po file
        echo "Syncing $PO"
        i18ndude sync --pot locales/$CATALOGNAME.pot $PO

    fi
done
