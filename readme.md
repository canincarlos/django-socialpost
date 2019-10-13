# Django Social Post

This is a simple Django application to register links, and assign them different copy with which to be packaged and distributed on Twitter.

There are likely many others, much fancier, but this was fun to build and is able to do specifically what I'm lookin' for.

A cronjob is set to run `tweet.sh` every three hours; while the file `tweet.py` has an internal randomizer yield 2 out 3 success rate. In such a case a link will be pushed to twitter along with proper text copy.

### Future Feature
Being able to attach images to posts

Would need to upload image and then retrieve/store image id/location on Twitter for future use.
