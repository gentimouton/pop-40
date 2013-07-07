pop-40
======

A top40 web app on App Engine. Keep track of the 40 songs most played in the US, plot who joins/leaves over time, etc.


How to
====

- download the appengine SDK https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
- extract it in ~/appengine
- get the app code from github
- in the pop-40 directory, run ~/appengine/dev_appserver.py .
- go to localhost:8080
- localhost admin is http://localhost:8080/_ah/admin/


Phases
===

phase 1
- fetch weekly (instead of wget -O filename http://www.billboard.com/rss/charts/hot-100)
- store
- display in smart and interesting ways
- link/embed to play each song (grooveshark?)


phase 2
- user accounts
- user comments
- classify songs and artists ("boys band", "woman", "rap", "rock", "piano"). Could be crowd-sourced from users, and only keep the top 5, or ask lastfm. 
- wikipedia/lastfm hover-box
- simple ML to predict the future of songs or artists
- display predictions


phase 3
- users bet on the rank of artists or songs in the next week, month, or 3 months
- points and rewards structure
- bots based on different ML algos also bet, leave comments, and have personalities (e.g. cautious in its predictions, obviously a liar, or hates women)



Libraries
===

- google appengine
- feedparser.py from http://feedparser.googlecode.com/svn/trunk/feedparser/feedparser.py
(doc at http://packages.python.org/feedparser/common-rss-elements.html) 
- jquery
- graph lib for JS?


Similar apps
====

http://www.simexchange.com/frontpage.php
http://www.hsx.com/
