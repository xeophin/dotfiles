#! /usr/bin/env sh

DIR=$(dirname "$0")
cd "$DIR"

. ../scripts/functions.sh

SOURCE="$(realpath .)"
DESTINATION="$(realpath ~/Library/Services/)"

info "Configuring services..."
mkdir -p "${DESTINATION}"
find * -maxdepth 0 -not -name "setup.sh" | while read fn; do
    fn=$(basename "${fn}")
    symlink "$SOURCE/$fn" "$DESTINATION/$fn"
done

success "Finished configuring services."
