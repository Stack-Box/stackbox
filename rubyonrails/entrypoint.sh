#! /bin/sh

# Prepare DB (Migrate - If not? Create db & Migrate)
sh prepare-db.sh

# Start Application
bundle exec puma -C config/puma.rb