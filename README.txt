README

There are 7 user types: Local/County Government, State/Federal Government, Community-Based Organization,
Medical Center, Private Business, Researcher, and Public. Each user type has unique preferences
defined by interviews conducted with persons identified as a specific user type.
For "hybrid" users (i.e. not one specific type or a mix of types), I suggest the user take a
questionnaire that will define his or her unique preferences. They will be identified in the system as a
"public" user and their preferences will be customized using the set_weight function in Person. The brute
force algorithms and general_PRs function will still accurately match their preferences.

Currently we utilize a content-based filtering system to recommend documents. As more user activity and user
data is collected I suggest transitioning to a collaborative filtering system.
A content-based system places items into categories based on their characteristics. This system will then take into
account the user preferences (or sometimes user behavior history) and use this data together to recommend items
to the user. We have implemented this system through the weighting of keywords for documents (categorizing
items) and weighting of keywords for users (preferences) and the general_PRs function that takes these two inputs
and outputs a list of recommended documents (items). The next step may be to implement a collaborative filtering
system. This recommendation system bases it's suggestions on user history and/or the behavior and history of
'similar' users. For example, if a user with a high preference for economics clicks articleA, then articleA
may be of interest to other users with a high preference for economics and thus the system is more likely to recommend
this article (I suggest by increasing the article's weight in the economic category). Similarly, if we add 'like'
or 'dislike' buttons to each article, then a 'like' will increase the article's weight in the appropriate
categories (based on the liking user's preferences) and a dislike will decrease the article's weight in the
appropriate categories (based on the disliking user's preferences).

Overall, this project increases user efficiency and utility by decreasing search time, and reduces information
overload by recommending articles to read.
