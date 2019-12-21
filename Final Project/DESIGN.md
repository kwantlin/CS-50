WeSet Design Document


WeSet as a website runs primarily on SQLite and Flask/Python functionality, using both what I learned through the Web Track as well as coding techniques gained from googling - and well cited!

First, let's talk about the basic process of setting up an account. I drew inspiration from the Finance pset to finish this aspect, since I found the interaction simple and no frills were
necessary - get that user signed up and onto the good stuff!

After you're all signed in, the fun can begin. With no classes entered, you can't really get matches for anything, so you make your way over to preferences, just as the blankindex template
indicates. Preferences is neatly organized into sections based on type of information - Harvard-themed of course for that second section. You'll notice that I used a combination of select-boxes,
text-boxes, and check-boxes to collect information from the user. The variation makes sense for each category and minimizes time that a user needs to spend feeding in the right info; for example,
it would be much more tedius to have a selectbox of times of day for meetings, especially since I need to specify what I mean my morning, afternoon, etc. to make it uniformly clear to all users.
Thus a checkbox system with the choices lined up like a timeline makes sense to a typical user and allows them to easily select a combination of times. The information then gets collected into
a SQL entry in the "myusers" database, where my "pref" function also let's the form remember if information was entered previously - a really complicated process it turns out! Many lines of code
are dedicated to the simplest system of "form memory" I could research, and the effect is definitely very helpful. Imagine if every time you went to your preferences, it was a completely blank
form, which upon update would input blank values in fields unless I re-inputted everything - bothersome! Upon hitting "Update", you are brought to an updated "index" of your matches.

This page is used to display two categories of matches. The first category is used to select all users in the database other than yourself such that you have some time preference and location in
common, and you are also both actively searching for a match (the "Searching?" checkbox in preferences). This was designed to facilitate random meetups for meeting new friends perhaps outside
your concentration or class but just may have similar study environment preferences - fun! I designed this as one of my two list categories since almost all of my friends on campus enjoy random-
match scenarios and also like to occasionally just meet up with a friend to get productive, and with WeSet this is now easily accomplished. The sizing of this category signals that indeed the
innovative usefulness of WeSet lies in this random matching for productive work sessions, since matches by class may form more organically (though this type of match is accounted for in the
next category). The House of each matched individual is noted because from experience, House tends to matter a lot in terms of convenience, and now you can know before you reach out to someone
without having to go on a wild Facebook search - pretty useful huh ;)

The second category of matches requires, for each class you're in, matches based on that class, concentration, and similar meeting times. This is pretty strict to be useful - matches with a lot
in common are different from the first category but you'll be happy with the suitability of the match once you start working, especially if you plan to collaborate together.

Note that for both categories, full name and contact info (users choose the type themselves) is always displayed since otherwise the platform could not otherwise facilitate contacting matches.
I also meet my criteria for a "better" outcome due to implementing a vertical and horizontal scroll on all the match lists, which allows the dashboard to be very usable, even if my database
were to eventually grow to include all of Harvard's population (easy to search since alphabetical), thus meeting my criteria for a "better" outcome. Note that you can scroll for a short list
and search for a longer one. Had I found packages that worked with my existing ones, I would have also collected location information to create a map with markers and tooltips to display users,
perhaps filterable by a selectbox. However, I'm pretty satisfied with my "better" outcome and hope that with additional learning, I will one day achieve this ambitions "best" outcome.

Lastly, let's chat about design - what a cute page! Elements are all styled to be simple and readable, while also giving off productivity vibes with the notebook aesthetic - sure to get a user
interested in the site and the interactions. Even the font was chosen to fit this handwritten aesthetic - always a nice touch in our digital age - while maintaining readability. The colors are
tied together to fit the notebook theme as well, allowing your matches to be displayed on little sticky-note tabs and arranged to be easily read. Note also that, on desktop at least, the sticky
tabs are all top aligned, completing the style effect of the page seamlessly.


