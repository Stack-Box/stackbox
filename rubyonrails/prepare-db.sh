#! /bin/sh

# If database exists, migrate. Otherweise setup (create and migrate)
bundle exec rake db:migrate 2>/dev/null || bundle exec rake db:create db:migrate
echo "Done!"