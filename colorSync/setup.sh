#! /usr/bin/env sh

DIR=$(dirname "$0")
cd "$DIR" || exit

. ../scripts/functions.sh

SOURCE="$(realpath .)"
DESTINATION="$(realpath ~/Library/ColorSync/Profiles/)"

info "Copying ColorSync Profiles..."
mkdir -p "${DESTINATION}"
find * -maxdepth 0 -not -name "$(basename ${0})" | while read fn; do
    fn=$(basename "${fn}")
    symlink "$SOURCE/$fn" "$DESTINATION/$fn"
done

success "Finished configuring services."