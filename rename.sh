#/bin/bash

./manage.py rename_tables django_boards punkweb_boards boardprofile category conversation message notification page post report shout subcategory thread userrank
./manage.py rename_tables django_boards punkweb_boards boardprofile_downvoted_by boardprofile_ranks boardprofile_upvoted_by conversation_unread_by conversation_users post_downvoted_by post_upvoted_by thread_upvoted_by thread_downvoted_by
