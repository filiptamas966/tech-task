1. Using any language or framework that you feel more comfortable with; Write an automated test script that asserts that Justin Bieber is either 'playing' or has 'recently played' on 'Capital FM London'.

You should test the Now Playing module (.now_playing_card) on the right side of the page of www.capitalfm.com. This module contains the currently playing track, the recently played tracks and how long ago the track was played.                                                              
(Note: A fully working executable test suite is not necessarily required. We are interested in your 'use of selectors' and choice of 'logic'. A partial Class/Model or Pseudo Code would be sufficient for this task)


Answer:
The attached document (test.py) contains the test. The test was developed under the assumption that the recently played tracks mentioned above refer only to the three songs that are on the main page underneath the “now playing”/”most recently played” song. 


2. Download either the Android or iOS 'Capital FM' App from the Google Play/iOS App Store.
Explore this app.

Identifying business features; What areas of the app would you focus your testing? Why would you prioritise these areas?

Answer:
The areas that I would prioritise are verifying streaming stability and synchronisation with the FM version, and push notifications. The relevant push notifications are very important to be received by the user for engagement. I would verify that notifications are delivered accurately.

I would also be interested to test the news feature of the app, because from what I checked, the Capital app is using ads, links and X (ex-Twitter) previews. These things could cause some issues because they are not totally on the developers’ control. From my experience on the current job I found that generally third-party integrations such as links or ads displays are more likely to cause bugs.


3. What do you consider before deciding to automate a test?

Answer:
When automating a test, I think about how much time it takes to execute the test manually and how often I need to go through a sequence of steps. If I have a long sequence of steps that I must repeat very frequently, I will consider this test a good candidate for automation. However, I think it is also worth considering how long the automation implementation will take. If a test is very difficult to automate and it is not executed very often or it doesn’t require executing too many test steps, then I would prefer to leave it for manual testing.


4. How much testing do you think is enough?

Answer:
In my opinion, enough testing unfortunately does not exist, and continuous testing is necessary to catch as many defects as possible before they are released. In the testing world there are constraints of time, so I think a reasonable testing process should include a both a testing plan with test cases based on the purpose of the feature and which will be executed automatically or manually, and some automated checks, like regression testing.


5.What do you think of the following statement?

“You cannot automate testing, you can automate manual checks but true testing can never be automated.”

Answer:
At this point, I consider this to be true because automated tests can’t reproduce 100% of a user’s behaviour. As much as we want to think that we can automate everything, the truth is that human behaviour is unpredictable and sometimes the preconditions are not exactly the ones that we are expecting. We can automate some of the scenarios that are more common, but I don’t believe we can anticipate 100% of the possible cases.


6. Write a function in Python; that given a key/value pair it will return True if there's an occurrence in a list of dictionaries.

Answer:
The attached document (dict.py) contains the test.
