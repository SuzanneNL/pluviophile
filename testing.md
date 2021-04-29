To return to the README file, click [here]( https://github.com/SuzanneNL/pluviophile/blob/master/README.md).
# TESTING 
## Table of contents

- [**Automated testing**](#Automated-testing)
    - [Validating](#Validating)
- [**Testing user stories**](#Testing-user-stories)
- [**Manual testing**](#Manual-testing)
- [**Resolved issues**](#Resolved-issues)
- [**Unresolved issues**](#Unresolved-issues)
- [**Browsers**](#Browsers)
- [**Responsiveness**](#Responsiveness)

## Automated testing
### Validating
- HTML code was validated by the [W3C Markup Validation Service](https://validator.w3.org/) and beautified using [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html). I used the page source for checking, because Django's templating language wasn't recognized. No major errors were found. I missed a few closing tags, and on the account page, this caused a bit of a problem. I corrected these. I was also warned about empty headers for the Open Weather Map modal, but they are supposed to be empty when a user doesn't use the modal. 
- CSS code was validated by the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/), and beautified using [Freeformatter CSS Beautifier](https://www.freeformatter.com/css-beautifier.html). No errors were found. 
- Javascript code was validated by [JSHint](https://jshint.com/), and beautified using [BeautifyTools Javascript Beautifier](http://beautifytools.com/javascript-beautifier.php). I missed quite a number of semicolons, and my indentation was a bit sloppy. I corrected that.
- Python code was validated and corrected when necessary. In the terminal, I ran:
```
python3 -m flake8
``` 
This gave an overview of all the errors/warnings. I had written many lines that were too long. With the help of an online [Python formatter](https://www.tutorialspoint.com/online_python_formatter.htm) and common sense, I was able to correct this. One thing that needed to be corrected was also a CharField in my profiles app that I had set to blank=True and null=True. However (and I knew this), a CharField should not be set to null=True. I therefore set the default to an empty string, like so:
```
blank=True, default=''
```
There are still a few warnings, like lines that are too long in settings.py and in migration files, but I will not edit those. Also, I kept a few files with unused imports (like models.py for the home app and tests.py for all apps), because I could use them later. Finally, in the like and bookmark views, I left the liked and bookmarked variables even though they don't have to be there and aren't used. They make the function more understandable though, and they're not doing any harm to the views. 

## Testing user stories
### As the creator of this website...

#### As the creator of this website...
1. **I want my website to have a clear structure, so that it is easy to navigate.**
    - The website has a clear structure. The navigation bar can redirect users to different parts of the website. Cancel buttons are always present on pages where users can perform CRUD operations. 
    - Users are redirected to relevant pages after they perform CRUD operations. When a user adds a thread, for example, he is redirected to that thread page. And when he deletes this thread, he is sent back to the forum page.
    - A user will only be able to see and visit pages that are relevant to him, as explained in the paragraph 'Structure' of the README file.
    - A 'back to top' button on pages that can get quite long, allows users to go back to the top of the page.
    - Links in content on pages also redirect users to other pages, such as being redirected to the Sign Up page from the Sign In page is a user hasn't got an account yet, or going to user profiles via the forum and thread pages.
2. **I want my website to give feedback to users, so that it is easy to navigate.**
    - Forms give feedback when a user doesn't correctly fill in a fields.
    - Django messages (Bootstrap toasts) give feedback after user actions with color and text (like red for error, green for success). For example, after signing in, the user sees a green success message notifying the user that he has signed in successfully. I decided to automatically close success/info toasts with a bit of a delay, because they hang over the dropdown menu when a user clicks on his username (for going to his profile or account or for signing out). Error/warning messages are more important, so users have to close those themselves.
    - Hover effects such as a pointer or changing colors of/in a button also give feedback to the user, about whether or not something can be clicked.
3. **I want my website to inform and entertain users with blog posts about rain.**
    - In the blog part of the website, users will find several blog posts with rain related topics. Users can like these blog posts with the like button, or bookmark them so that they can read them again later.
4. **I want my website to connect members of the pluviophile community.**
    - Users can communicate with each other via the forum. They can introduce themselves, respond to different threads. They also have public profiles, that they manage themselves. They can decide what information they would like to show there. 
5. **I want to let my registered users manage content they created themselves.**
    - Users can create content for the forum (threads and comments), and their profile. They can edit and delete this content whenever they want. They can also like and bookmark blog posts and they can also undo these actions. Other users (except for superusers) do not have these rights. Users can only edit and delete their own content. They however cannot delete their own accounts or delete information about donations they've made. 
6. **I want to protect the work of users by not giving rights to edit and delete content or information of others.**
    - As I stated above, users can only edit and delete their own content. Trying to access edit and/or delete pages for other users content, will result in being redirected to an error page. 
7. **I want to prevent guest users to upload content and also see content that is not meant for them.**
    - Guest users do not have access to the blog, forum, donation and profiles apps. They cannot even see these apps in the navigation bar. Trying to access a page from one of these apps results in the user being redirected to the login page. 
8. **I want to warn users when they try to delete their content, as a form of defensive programming.**
    - Users always get redirected to a confirm deletion page after clicking on delete for a part of content. They can always cancel. Only after confirming their choice, will their content be deleted. 
9. **I want superusers to have CRUD rights over all the content on this website, in case users behave in an unwanted fashion.**
    - Superusers have CRUD rights over content created by users, except for donation content. I don't think it is responsible for a superuser to be able to edit financial content. 
10. **I want to be financially supported by members in the form of a voluntary donation.**
    - Registering is free, users do not have to pay a registration fee. However, they will see the 'donate' option in the navigation bar. When they click on this, they will see why the website asks for a small donation. They can be redirected to a page where they can fill out their credit card details, for a donation of € 5,-. If they submit this form, the credit card is charged and a donation is made. Users can make multiple donations if they want. The donation option doesn't disappear after a user has made a donation. 

As a user in general...
1. **I enjoy the rain.**
    - The website is intended for people who have an interest in or love the rain. On this website they can read about it and talk about it. There is also a rain animation, just for fun.
2. **I enjoy reading about rain related topics.** 
    - The blog contains several blog posts about rain related topics. If a user enjoys a blog post, he can like it and/or bookmark it. 
3. **I enjoy taking part in rain related conversations.** 
    - The forum serves as a platform where users can join in on conversations about rain related topics. Users can create threads and/or comment on threads, as soon as they register.
4. **I want to be able to easily navigate the website.** 
    - As explained above, the website has different elements in place (navigation bar, URL's in content, buttons) to facilitate navigation. 

As a guest user...
1. **I want to get an idea of what the website has to offer.**
    - The home page shows a definition of the word 'Pluviophile', and sees three cards that explain what the website offers (profiles, forum, blog). The user also has access to the Make it rain! animation and the Find the rain functionality. 
2. **I want to be able to sign up, so that I can get access to the blog, forum, profiles and donation pages.**
    - Users can either click the button under the welcome text or use the navigation bar to go to the Sign Up page, where they can register with a username and an e-mail address. As soon as they have registered, they get access to the blog, forum, donation and profiles apps. 

As a logged in user...
1. **I want to read, like and bookmark blog posts.**
    - Users that are signed in can read all the blog posts. At the bottom of each blog post they see two icons: a bookmark for bookmarking the blog post and a heart for liking the blog post. Bookmarks can be found on the account page. Users can also see who liked a blog post by clicking 'show likes'. 
2. **I want to be a part of the forum.**
    - Users that are signed in can read all content on the forum. They can start threads and comment on threads. The number of posts they make (either creating threads or commenting on threads) influences their activity status. 
3. **I want to update my profile.**
    - Users can write a biography, add a date of birth and add their country on their profile page. There will be a default avatar, but they can update it with their own image. This information and this avatar are then visible for all signed in users.
4. **I want to manage content that I have created.**
    - Users can edit and delete the content that they create in both the forum and profiles app. They however cannot update or delete their donation details. If they have bookmarked a blog post, they can remove the bookmark. Also, they can unlike blog posts that they have liked, at any time. 
5. **I can, for the most part, decide what information other users see about me.** 
    - Users will choose their own username. This will be visible for other users as soon as a user likes a blog post or joins in on a conversation on the forum. Also, users can visit the profile that is created automatically when he signs up. Here, users can see information about the specific user's activity, like his activity status (a number of drops, based on the number of posts) or when he was last signed in. Some of this information is also visible on the forum. However, a user can write his own biography, select his own date of birth, select his own country and upload his own avatar. These are things that he has control over.
6. **I want to see my private information details on my account page.**
    - When users click on their username in the navigation bar, they see that they can go to their account page. On the account page, a user sees his username and his e-mail address, as well as the option to change his password. Users can find their bookmarks underneath this personal information. And, if a user has made a donation, he can see his donation details, and the total amount he donated. All of this is only visible for the logged in user. Superusers/admin will also see a table with all the donations (by all users).
7. **I want to be able to update my password.**
    - Like I said above, users can update their password. This is handled by Django allauth. 
8. **I want to have the possibility to make a donation.**
    - Signed in users see 'Donate' in the navigation bar. If a user clicks on this, he will see a short text explaining why the website asks for a small donation. A user can then make a donation of € 5,-. Donation details for that specific donation will be shown on the donation success page. All donations can also be found on the account page. 
9. **I want to be able to log out.**
    - When a user clicks on his username in the navigation bar, he sees the option 'Sign Out'. When he clicks on this, the user will be redirected to a page asking him to confirm his wish to sign out. When he does, he is signed out and redirected to the home page as a guest user. 

## Manual testing
Manual testing was done on different devices (see Responsiveness).

### Navigation bar
The navigation bar is visible on all pages (except the Make it rain! page) and fixed to the top, so it stays visible as the user scrolls down. It redirects users to different parts of the website. The items in the navigation bar vary, based on whether a user is logged in or not. As a guest user, one sees Home, Find the rain, Make it rain!, Sign In and Sign Up. 
Once signed in, the options Sign Up and Sign In have disappeared. Instead, users see Forum, Blog and Donate. They also see their own username with their avatar next to it. Clicking on the username opens a dropdown menu, that shows options to be redirected to the Profile and Account page or to sign out. 

### Footer
- The icon sticks to the bottom of the page, even when there is little content on the page.
- The icons and the name SuzanneNL in the footer have a hover effect: the mouse turns into a pointer and the color of the icons/text change.
- When a user clicks on one of these icons or SuzanneNL, he is redirected to the corresponding website in a new tab. 

### Home
- Users see a definition of Pluviophile and a background image that is also visible on many other pages (but not all). There's a join button and are three cards that inform about the profiles app, the forum app and the blog app. If the user is logged in, the join button has disappeared. Instead, in each card, the user sees a button to be redirected to that app. 

### Find the rain
- Clicking on this in the navigation bar, will open a modal with a call to enter a city. This works with Open Weather Map API. After entering a city, the user will see what the weather is for that specific city, and a message about whether or not it's raining there. This is based on the weather code. If the API call is unsuccessful (f.e. if the user enters a city name that doesn't exist), an error messsage is visible. 

### Make it rain!
- Clicking on this in the navigation bar, will open a page with a Javascript rain animation. The animation can be opened at any time, and will redirect back to the previous page when it is closed. If a user comes from a different website, the user will be redirected to the home page.

### Sign Up, Sign In, Sign Out with Django Allauth
- Django Allauth handles signing up, signing in and signing out actions, and it works as intended. For example, when a user tries to sign up with a username that already exists in the database, an error message is displayed under the username field. Or when a username doesn't meet the requirements, an error message under the field in the form will display what the requirements are. When a user tries to log in with incorrect credentials, he will be redirected to the sign in page, where an error is shown that the username and/or password the user specified were incorrect. 
- Django Allauth uses django messages to inform a user if signing up, signing in and signing out have been successful, on the next page. 
- Django Allauth redirects a user to a confirmation page when he tries to sign out. 

### Forget Password with Django Allauth
- When a user tries to sign in but doesn't remember his password, he can click on 'Forgot password'. This redirects him to a form where he has to fill in his e-mail address. An e-mail with a reset link is then sent to the user's e-mail address. That is, if it exists in the database. If not, the user sees an error message: 'The e-mail address is not assigned to any user account'.

### Reset Password with Django Allauth
- On the account page, the user sees that he can update his password. Clicking on this will send him to a form where he has to fill in his old password, and his new password twice. Django Allauth will throw errors if the user makes a mistake (like not correctly repeating the new password) or fills in a new password that doesn't meet the requirements. If the changing of the password was successful, a success message is shown.

### Forum app - View, paginate and sort threads
- A user sees all threads that have been created on the forum page. He sees the number of threads that have been created. For each thread that has been created, he sees a section with the title, the user who created it, when it was created, how many comments the thread has and who created the last comment, and when this was done. If there are no comments, he sees 'No comments' yet. A user can click on the usernames in such a thread section, and then be redirected to that users profile page.
- Threads are paginated per 5 threads.
- Threads can be sorted by date, ascending and descending, and by title, also ascending and descending (alphabetical order). By default, they are ordered by date descending. 
- Clicking on 'Start a new thread' will redirect the user to a form where he can add a new thread. 

### Forum app - Add thread
- A user can fill out the form. He has to fill in both fields: title and description. There are no requirements, except for the fact that the title cannot exceed 60 characters, and the description cannot exceed 2000 characters. 
- A user can either click Cancel, which will redirect him to the forum page. Or he can click 'Start thread', which will send him to the freshly added thread detail page. A success message is visible in the top right of the screen. On the thread page, the user will see his title and description, as well as some of his information. As he is the creator of that thread, he will also see an edit and delete button. 

### Forum app - Edit thread
- After clicking on 'Edit thread' the user gets redirected to the edit thread page. He sees the same form as on the add thread page, but the content is already filled in, in the form fields. 
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user clicks 'Edit thread', any changes he has made will be saved. He will then be redirected to the thread page. A success message is visible in the top right of the screen. 

### Forum app - Delete thread
- After clicking on 'Delete thread' the user gets redirected to a page where he's asked to confirm his wish to delete the thread.
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user confirms, the thread gets deleted from the database and the user is redirected to the forum page. A success message is visible in the top right of the screen. Also, his thread will no longer be visible on the forum page, as it doesn't exist in the database anymore. 

### Forum app - View and paginate comments
- A user sees comments that have been added to a thread on the thread page. Next to the paginator, he sees the number of comments that have been added, and what page he is on. 
At the top of each page, he will see the thread section, which contains the title, the description, when it was created, if and when it was edited and information about the user who created the thread.
For each comment that has been added, the user sees a section with the comment itself, the user who added it, when it was added, and if (and when) it was edited. If there are no comments, he sees 'There are no comments yet', and one button to 'Drop a comment'. If there are comments, there will be a button above and below the comments. 
A user can click on the usernames in the thread or in a comment section, and then be redirected to that users profile page.
The information that a user sees from other users is their username, a flag (if the user has selected his country on the profile page), his avatar, a number of blue drops representing how active the user is, and when the user joined the website. Superusers always get 5 golden drops by the way. 
- Comments are paginated per 5 threads.
- Comments are ordered by date (old to new).  
- Clicking on 'Drop a comment' will redirect the user to a form where he can add a new comment. 

### Forum app - Add comment
- A user can fill out the form, which is just one field. There are no requirements, except for the fact that the post cannot exceed 2000 characters, and that it cannot be left blank. 
- A user can either click Cancel, which will redirect him to the thread page. Or he can click 'Add comment', which will also send him to the thread page. A success message is visible in the top right of the screen. On the thread page, the user will see that his comment has been added. As he is the creator of that comment, he will also see an edit and delete button for it. 

### Forum app - Edit comment
- After clicking on 'Edit' at the bottom of a comment, the user gets redirected to the edit comment page. He sees the same form as on the add comment page, but the content is already filled in, in the form field. 
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user clicks 'Edit thread', any changes he has made will be saved. He will then be redirected to the thread page. A success message is visible in the top right of the screen. 

### Forum app - Delete comment
- After clicking on 'Delete' at the bottom of a comment, the user gets redirected to a page where he's asked to confirm his wish to delete the comment.
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user confirms, the comment gets deleted from the database and the user is redirected to the thread page. A success message is visible in the top right of the screen and of course the comment will no longer be visible on the thread page, as it doesn't exist in the database anymore. 

### Blog app - View, paginate and sort blog posts
- A user sees all blog posts that have been created on the blog page. He sees the number of blog posts that have been created. For each blog post that has been added, he sees a card with the first image, the author who wrote it, when it was uploaded, the title and the first 30 words of the blog post. A user can click on the image and on the 'read blog post' button to go to the blog post.
- Blog posts are paginated per 4 blog posts.
- Blog posts can be sorted by date, ascending and descending, and by title, also ascending and descending (alphabetical order). By default, they are ordered by date descending. 
- At the top of the first page, superusers can see a button 'Add Blog Post'. Clicking this will redirect the superuser to a form where he can add a new blog post. 

### Blog app - Add blog post
- At the top of the form, the user sees a button to display instructions. Unfortunately, the process isn't very user friendly. A rich text editor might be implemented in the future. But if the user follows the instructions, a blog post can be added. 
- A user can fill out the form, which consists of multiple fields. There are no requirements, except for the fact that the fields with an asterix are required. 
- A user can either click Cancel, which will redirect him to the blog main page. Or he can click 'Add blog post', which will send him to the fleshly created blog post page. A success message is visible in the top right of the screen. All superusers will see an edit and delete button at the bottom of the blog post, and they can all edit and delete the blog post. 
On the blog main page, the user will see that his blog post has been added. 

### Blog app - Edit blog post
- After clicking on 'Edit blog post' the user gets redirected to the edit blog post page. He sees the same form as on the add blog post page, but the content is already filled in, in the form fields. 
- If the user clicks on cancel, nothing happens and the user gets redirected to the blog post page. If the user clicks 'Edit blog post', any changes he has made will be saved. He will then be redirected to the blog post page. A success message is visible in the top right of the screen. 

### Blog app - Delete blog post
- After clicking on 'Delete blog post' the user gets redirected to a page where he's asked to confirm his wish to delete the blog post.
- If the user clicks on cancel, nothing happens and the user gets redirected to the blog post page. If the user confirms, the post gets deleted from the database and the user is redirected to the blog main page. A success message is visible in the top right of the screen. Also, the blog post will no longer be visible on the blog main page, as it doesn't exist in the database anymore. 

### Blog app - Like blog post
- At the bottom of the page, users see a white heart icon. Clicking on this icon will result in adding a like. 
- This will reload the page. A success message is visible in the top right of the screen. The heart will now be red. Clicking it will result in removing the like.
- This will reload the page. A success message is visible in the top right of the screen. The heart will be white again.
- Users can only like an article once. Next to the heart, it says how many likes the blog post has gotten. If there are likes, users see a small button 'Show likes'. If a user clicks on this he will see a list of users who have liked the article. These users can not be clicked.

### Blog app - Bookmark blog post
- At the bottom of the page, users also see a white bookmark icon. Clicking on this icon will result in adding a bookmark. 
- This will reload the page. A success message is visible in the top right of the screen. The bookmark will now be blue. Clicking it will result in removing the bookmark.
- This will reload the page. A success message is visible in the top right of the screen. The bookmark will be white again.
- Users can only bookmark an article once. Articles that have received a bookmark from a user, will be shown on the account page. 

### Donation app 
- When a user clicks on Donate in the navigation bar, he will see an explanation why the website asks for donations. If he proceeds and clicks 'Make donation', he will be redirected to the charge page. 
- As soon as he opens this page, a payment intent of € 5,- will be sent to Stripe.
- A user must fill in his full name, e-mail address and credit card information. Stripe provides credit card information to test the form:
```
There are several test cards you can use to make sure your integration is ready for production. Use them with any CVC, postal code, and future expiration date.

4242424242424242 - This succeeds and immediately processes the payment.
4000000000003220 - 3D Secure 2 authentication must be completed for a successful payment.
4000000000009995 - Always fails with a decline code of insufficient_funds.
```
These credit card numbers work as intended.
- When the processing of a payment is successfully handled by Stripe, the donation is created in the database and the user gets redirected to the donation success page where he can see details from the donation: date, amount and donation number. Each donation receives a unique donation number. A success message is visible in the top right of the screen. This page can only be accessed by the donor. 
- All donation details, for each donation, will also be visible on the account page.
- A webhook process is in place for when the payment processing doesn't succeed immediately. 

### Profile app - Profile page
- A user can go to his profile by clicking on his username in the navigation bar and clicking on 'Your profile' in the dropdown menu. Of course, he could also click on his username if it is displayed somewhere in the forum. 
- Users can visit each other's profiles, by clicking on usernames on the blog.
- For his own profile, he will see an 'Edit profile' profile button. 
- Default information is the date he joined, the number of threads and comments he has posted/created, and an activity status in blue drops, based on the aforementioned numbers. It will also have a default avatar. For the country and date of birth, it will say 'Unknown'. There will not be a flag next to his username. And it will see that the user hasn't written a bio yet.
- Superusers will have (Admin) behind their username in the page title. They will also have a status of 5 golden drops. 

### Profile app - Edit profile
- After clicking on 'Edit profile' the user gets redirected to the edit profile page. He sees a form and if he added content to his profile in the past, the content is already filled in, in the form fields. If not, these fields are left empty.
- A user can select his date of birth. A datepicker is used, but he can also manually type it. This date cannot be in the past. An error will be displayed if the user tries to submit the form with a date in the future, or today. The field is still optional, though. 
- A user can select his country. If he submits the form, then from that point on, a small flag will be visible next to his username on the profile and on thread pages. He can always unselect his country, then the flag disappears.
- If the user clicks on cancel, nothing happens and the user gets redirected to the profile page. If the user clicks 'Edit profile', any changes he has made will be saved. He will then be redirected to the profile page. A success message is visible in the top right of the screen. 

### Profile app - Account
- A user can go to his account page by clicking on his username in the navigation bar and clicking on 'Your account' in the dropdown menu. 
- The user sees this account details and a button to be redirected to a page where he can update his password. This is handled by Allauth, as I described at the beginning of this section. 
- The user also sees his bookmarks, if he has any. These are the titles of the blog post he bookmarked, which he can click to go to the blog post.
- If the user has donated to Pluviophile, a donation table gets created. For each donation, a row is added, showing exactly when the donation was made, which details the user gave (name, e-mail address), the amount (always € 5,-) and the donation number. 

### Django Messages
- Django messages (Bootstrap toasts) give feedback after user actions with color and text (like red for error, green for success). They disappear when a user closes the message box, or when a user goes to a different page. 

### Buttons
- All buttons have hover effects and redirect users to different pages or hide/show information. There are no broken buttons or links. 

## Resolved issues
**1: Class name in models = Class name in views**<br>
The first bug I encountered was when I was creating a page for starting a thread. I had a model called Thread ('class Thread'), and I also named my class based view Thread (so also 'class Thread'). Apparently this made Django confuse the two. It gave me an error, stating that: "type object 'Thread' has no attribute '_meta'". Changing the name of the view to ThreadView solved the error. 

**2: Threads with PK of 10 and higher**<br>
I was adding new threads to my forum, but when I reached 10 threads, and so a pk of 10, I got an error: "NoReverseMatch at /forum/start_thread/ Reverse for 'thread' with arguments '('1', '1')' not found. 1 pattern(s) tried: ['forum/thread/(?P<pk>[0-9]+)$']"

It seemed like it was looking for two separate arguments, 1 and 0 or 1 and 1 or 1 and 2 etc. 
This was my model:
```
class Thread(models.Model):
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('thread', args=(str(self.id)))
```

Underneath self from self.id, I got a notification that: "Instance of 'Thread' has no 'id' memberpylint(no-member)".

I concluded that the problem was in the id-part. Switching to pk, solved the issue:
```
    def get_absolute_url(self):
        return reverse('thread', kwargs={'pk': self.pk})
```
This way, it accepted pk's of higher than 10. I later used this same code for my blog posts, because I saw the same error with 'id'. I didn't encounter any errors on the website itself, probably because I never added more than 9 blog posts.

**3: Comparing date created and date edited**<br>
When a thread gets created, it receives two date time fields. One for date created and one for date edited:
```
class Thread(models.Model):
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
```
I thought these DateTimeFields would be identical when the thread gets created. And I thought that when a user edits a thread, only the field 'date_created' would get updated. 
The issue was this: I wanted my template to display the date_edited value only when this was different from the date created (and therefore actually edited). So I used the following if statement in my template:
```
{% if thread.date_created != thread.date_edited %}
     <p>edited on: {{ thread.date_edited }}</p>
{% endif %}
```
I thought this was an easy thing to do, but apparently there's a very small difference (perhaps a few milliseconds) between the two timestamps when a thread gets created. Therefore, even when a thread hadn't been edited by a user, both dates and times were displayed.
I therefore had to filter the two timestamps to the second. With the following if statement, the problem was resolved:
```
{% if thread.date_created|date:"D, d M, Y, H:i s" != thread.date_edited|date:"D, d M, Y, H:i s" %}
     <p>edited on: {{ thread.date_edited }}</p>
{% endif %}
```

**4: Going back to the thread to which a user added a comment**<br>
I had written the following view for adding a comment:
```
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "forum/add_comment.html"
    fields = ['post']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
```
After submitting the form for adding a comment, it produced the following error: "IntegrityError at /forum/thread/26/add_comment/ NOT NULL constraint failed: forum_comment.thread_id"

I therefore added the pk as the id:
```
def form_valid(self, form):
    form.instance.thread_id = self.kwargs['pk']
    form.instance.creator = self.request.user
    return super().form_valid(form)
```

I was now able to add comments, but was redirected to a thread with the pk of the comment. I fixed this by setting the success URL:
```
def get_success_url(self):
    return reverse_lazy('thread', kwargs={'pk': self.kwargs['pk']})
```

**5: Going back to the thread after a user edits a comment**<br>
I wrote the following view for editing a comment in a thread:
class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = "forum/edit_comment.html"
    form_class = CommentForm

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')

After editing a comment, I got an error: "NameError at /forum/edit_comment/4 name 'thread' is not defined". This was because in the Comment model, I had written the get_absolute_url function, for when a new instance of the model gets created:
class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name="comments",
                               on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "On '%s' by %s" % (self.thread, self.creator)

    def get_absolute_url(self):
        return reverse('thread', kwargs={'pk': thread.pk})

I wanted a user to go back to the thread after editing a comment, but 'thread' was not defined according to the error. So I tried defining it again:
```
def get_absolute_url(self):
    thread = models.ForeignKey(Thread, related_name="comments", on_delete=models.CASCADE)
    return reverse('thread', kwargs={'pk': thread.pk})
```
This is kind of funny to see in hindsight, because I just copied from the model, and that's not how I should have defined it. Anyway, I got an error that there is no pk for the thread. Because I was still learning and testing, to see what happens, I also wrote self.pk:
```
def get_absolute_url(self):
    thread = models.ForeignKey(Thread, related_name="comments", on_delete=models.CASCADE)
    return reverse('thread', kwargs={'pk': self.pk})
```
This, of course, sent me to a thread but not the one where I came from, but the one with the same pk as the comment I just edited. 

I then started looking into maybe hiding the thread.pk somewhere in a field of the CommentForm. But after some research on Google, I found a very nice trick on StackOverflow. You can add ?next={{ request.path }} to the link that directs to the edit comment page:
```
<a href="{% url 'edit_comment' comment.pk %}?next={{ request.path }}">Edit comment</a>
```
And then wrote the get_success_url as follows in the view:
```
def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))
```
This works: it sends a user back to the thread page. As I'm writing this, nearly at the end of my project, I'm thinking that there should be better ways to do this. But at this stage of my project, I have to follow the advice I've seen in coding memes that 'if it works, don't touch it!'.

**6: Cancel buttons in edit and delete comment templates**<br>
When a user edits or deletes threads, there's always a cancel button, that redirects the user back to the thread itself. I tried to do the same in the edit and delete comment templates. For example, in the delete comment template, I had written:
```
<button class="btn btn-danger" type="submit">Yes, delete comment</button>
<a class="btn btn-secondary" href="{% url 'thread' thread.pk %}">Cancel</a>
```
This however, threw an error when I was trying to access the delete comment page: "NoReverseMatch at /forum/comment/delete/9 Reverse for 'thread' with arguments '('',)' not found. 1 pattern(s) tried: ['forum/thread/(?P<pk>[0-9]+)$']".
Simply deleting the cancel button solved the issue and I got access to the page again. I then placed ?next={{ request.path }} (see my previous resolved bug) behind the URL that redirects to the delete comment page.
And then on that page, I redirect the user to the same success URL as the one that a user is redirected to after confirming the deletion:
```
<a class="btn btn-secondary" href="{{ view.get_success_url }}">Cancel</a>
```
And that worked: clicking the cancel button, makes the user go back to the thread page (without the comment being edited of course). 

**7: Displaying the number of threads and comments created by a user who commented on a thread page**<br>
All users get an activity status (a number of drops) based on the number of posts (either comments or threads) they created on the forum. I was able to display these numbers on the public profile page without any problems. And I was also able to display this information on the thread page for the user who created the thread as follows in the view:
```
class ThreadView(LoginRequiredMixin, DetailView):
    model = Thread
    template_name = "forum/thread.html"
    ordering = ['date_created']

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        current_thread = self.get_object()
        page = self.request.GET.get('page')
        comments = Paginator(self.object.comments.all(), 5)
        context['threads_by_thread_creator'] = Thread.objects.filter(
                                               creator=current_thread.creator)
        context['comments_by_thread_creator'] = Comment.objects.filter(
                                                creator=current_thread.creator)
        
        context['all_threads_on_forum'] = Thread.objects.all()
        context['all_comments_on_forum'] = Comment.objects.all()
```
And as follows in the template:
```
<small>Threads: {{ threads_by_thread_creator.count }}</small><br>
<small>Comments: {{ comments_by_thread_creator.count }}</small>
```
I was not able to work out however, how to display this for the creator of a comment. This is because I loop through the comments, and cannot get the pk of a specific comment that I'm displaying on the tempalte, in views.py:
```
current_comment = Comment.pk  # This doesn't work
context['threads_by_comment_creator'] = Thread.objects.filter(creator=current_comment.creator)
context['comments_by_comment_creator'] = Comment.objects.filter(creator=current_comment.creator)

```
I spoke with tutor support for hours, but the tutors were not able to figure it out either. I then looked at 'annotate' and context processors but was still not able to solve this. I therefore chose a different approach:
In the template, inside the comment div, I call all the threads and comments created on the forum, and filter with an if statement as follows:
```
{% for obj in all_threads_on_forum %}
{% if obj.creator == comment.creator %}
<span class="count-this">{{ obj.creator }}</span>
{% endif %}
{% endfor %}
{% for obj in all_comments_on_forum %}
{% if obj.creator == comment.creator %}
<span class="count-this">{{ obj.creator }}</span>
{% endif %}
{% endfor %}
```
With jQuery I then count the number of spans created (=the number of posts created by the comment creator), and based on that number, I display the status of the user:
```
$(document).ready(function(){
    $(".elements").each(function(ind, val){
        var nTotalComment = $(val).find(".count-this").length;
        if (nTotalComment < 5) {
            $(val).find(".count").html("status 1")
        }
        else if (nTotalComment < 10) {
            $(val).find(".count").html("status 2")
        }
        else if (nTotalComment < 20) {
            $(val).find(".count").html("status 3")
        }
        else if (nTotalComment < 25) {
            $(val).find(".count").html("status 4")
        }
        else {
            $(val).find(".count").html("status 5")
        }
    });
});

</script>
{% endblock %}

```
I decided to use this approach for the thread creator as well, for consistency on that template.  
It doesn't feel like the most elegant approach, and I know that logic shouldn't be handled in the template, but I was very happy to get the result I wanted. I would love to learn how I could have done this differently. 

**8: Stripe payment unsuccessful**<br>
In my project, users can donate 5 euros to Pluviophile. I was following the Boutique Ado project and I could see in Stripe that when I opened my charge page, a payment intent got created in Stripe - as it should. But the payment didn't succeed in Stripe after submitting the form. With the JS code present, the form wouldn't get processed at all. The submit button and card-section would get disabled, and then the page would get stuck and nothing else would happen.
When I changed the id of the form (and therefore skipped the JS code), the donation did get created in my own database, and I did go to the 'donation succeeded' page. Which showed me that there was nothing wrong with the POST part of my view. 
So I thought there was a problem with my Javascript. I checked my console, but there were no errors.
I went to the next step in the Boutique ado project: adding the overlay. With the overlay added to my code, when I clicked the submit button, the overlay would appear, but it wouldn't go away. So I concluded that something was going wrong AFTER the payment intent was created, and AFTER the submit button and card-section would get disabled and also AFTER the overlay would appear, but BEFORE the payment was supposed to succeed.
I was sure that the problem was in this part of my code:
```
stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
```
But it was identical to the boutique ado project. Stripe told me that:
the status of the PaymentIntent was: 'requires_payment_method'.
I checked my clientSecret, which is saved in my env.py file, and it looked fine. 
I checked my terminal for errors, and there were none. I checked my console again for errors, and there were none. With the help from tutor support, I found out that I had a filter on in my console (accidentally), which prevented me from seeing all errors. When I fixed this, I could see that the problem had to do with the public and secret keys from Stripe: "Uncaught IntegrationError: Invalid value for stripe.confirmCardPayment intent secret: value should be a client secret of the form ${id}_secret_${secret}. You specified: intent.client_secret."
So I checked where my keys were being passed on to the template, and found that the problem was in my view. I had put quotation marks around the client secret and public key. Removing them resolved the issue. 

**9: Setting the logged in user as donor of a new donation, when form submission fails**<br>
I was at the end of the webhooks videos from the Boutique Ado project, and I ended up having one final issue. I was trying to pass through the logged in user as the donor in the 'handle_payment_intent_succeeded' function in the webhook handler, for when the donation doesn't exist in my database yet and needs to be created. To test this, the submit button in Javascript was disabled.

In the CI videos, it was said that I could use request.user to get the donor, because the request object was added to the init method at the top. So I first tried this:
```
try:
    donation = Donation.objects.create(
    donor = request.user,
    donor_full_name=billing_details.name,
    email=billing_details.email,
    stripe_pid=pid,
)
```
But this gave me an error in Stripe: "Webhook received: payment_intent.succeeded | ERROR: name 'request' is not defined".

Then I used self.request.user:
```
try:
    donation = Donation.objects.get(
        donor = self.request.user,
        donor_full_name__iexact=billing_details.name,
        email__iexact=billing_details.email,
        stripe_pid=pid,
    )
```
This have me a different error. In my terminal I could see: "TypeError: 'AnonymousUser' object is not iterable'". In Stripe, I didn't get a message but a bunch of HTML code.

After looking at different Stackoverflow posts, where people advised to check if the user is authenticated, I tried the following:
```
if self.request.user.is_authenticated:
    billing_details = intent.charges.data[0].billing_details
    # Clean data in the shipping details
    for field, value in billing_details.address.items():
        if value == "":
            billing_details.address[field] = None
    donation_exists = False
    attempt = 1
    while attempt <= 5:
        try:
            donation = Donation.objects.get(
                donor = self.request.user,
                donor_full_name__iexact=billing_details.name,
                email__iexact=billing_details.email,
                stripe_pid=pid,
            )
[etc]
return HttpResponse(
            content=f'Webhook received: {event["type"]} | ERROR: User error',
            status=500)
```
Also, I made sure that only logged in users could access these pages with @login_required.
I tried this code but got an internal server error in the terminal: 
```
08/Apr/2021 14:12:59] "POST /donation/wh/ HTTP/1.1" 200 50
Internal Server Error: /donation/wh/
[08/Apr/2021 14:13:31] "POST /donation/wh/ HTTP/1.1" 500 74
[08/Apr/2021 14:13:32] "POST /donation/wh/ HTTP/1.1" 200 44
```
And in Stripe I saw the message: "Webhook received: payment_intent.succeeded | ERROR: User error." 
This 'Error: User error' was the error I wrote myself, in case a user wasn't authenticated.

I did some more research and someone mentioned that users might get logged out for a bit when working with Stripe, but I checked my cookies and the 'sessionid' didn't disappear. 

I also tried changing the location of the if statement (where it is in the CI video):

```
        if self.request.user.is_authenticated:
            donation_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    donation = Donation.objects.get(
                        donor = self.request.user,
                        donor_full_name__iexact=billing_details.name,
                        email__iexact=billing_details.email,
                        stripe_pid=pid,
                    )
[etc]
        return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: User error',
                status=500)
```
This gave the exact same errors.

I also tried:
```
if self.request.user.username != 'AnonymousUser':
```
This gave the following error: "TypeError: 'AnonymousUser' object is not iterable".

Trying this code:
```
username = self.request.user.username
        if username != 'AnonymousUser':
```
Gave the exaxt same error: "TypeError: 'AnonymousUser' object is not iterable". And trying this:
```
username = self.request.user
        if username != 'AnonymousUser':
```
gave me the, by now familiar, type error: "TypeError: 'AnonymousUser' object is not iterable". 
I then started working with tutor support and from the charge view the tutor printed in the terminal who the charging user was when the charge page is opened:
```
def charge(request):
    
    print(f"CHARGE USER: {request.user}")

```
Then, from the webhook handler, he  printed in the terminal who the WH user was:
```
class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
        print(f"WH USER: {self.request.user}")

```
This showed as the logged in users username 'Pieter' as charge user (the logged in user), but 'AnonymousUser' as the wh user:
```
CHARGE USER: Pieter
[09/Apr/2021 15:09:20] "GET /donation/charge/ HTTP/1.1" 200 8269
[09/Apr/2021 15:09:21] "GET /static/js/stripe_elements.js HTTP/1.1" 304 0
[09/Apr/2021 15:09:21] "GET /static/css/donation.css HTTP/1.1" 304 0
WH USER: AnonymousUser
```
We tried working around this by creating an extra session variable, but this didn't get picked up. After several hours, and when the shift of the tutor finished, he gave me advice to look at the Boutique ado project, where information from the metadata is used to decide who the user is, and where information gets connected with the UserProfile. 
I was confused at first, because I didn't want to connect it to the UserProfile, and I hadn't added metadeta, but I decided to use that approach and try to connect it to the User object. 
I was able to retrieve the email from the payment intent's billing details. Then I used that to get the logged in user. And then if the logged in user wasn't AnonymousUser, the user will be the User object with the same e-mail address as the one in the billing details.
```
user_email = intent.charges.data[0].billing_details.email
if self.request.user != 'AnonymousUser':
    user = User.objects.get(email=user_email)
```
Then I set that user as the donor:
```
donation = Donation.objects.create(
    donor=user,
    donor_full_name=billing_details.name,
    email=billing_details.email,
    stripe_pid=pid,
)
```
This is how the webhook finally worked! 
I checked this also with the deployed website. When the payment process goes without issues, on Stripe I can see that the payment_intent has succeeded and a message: 'SUCCESS: Verified donation already in database'. When I disable the form submission, I can see on Stripe that the payment_intent has succeeded but a different message: 'SUCCESS: Created donation in webhook'. Both charges then are successful. And for both donations, an instance of the Donation model gets created in the database. 

There is one catch: if the user uses a different e-mail address in the donation form, than the one he registered with, then the donation doesn't get created in the database, and an internal server error occurs. This is an unresolved issue. One could argue that since the user signed up with an e-mail address, the user shouldn't have to fill out his e-mail address again on the donation form. But sometimes donations are made with someone else's credit card, under someone else's name, for example by a parent. Then the confirmation e-mail would have to go to the e-mail address of the credit card holder. This is why I chose to not automatically use the users e-mail address as a placeholder, or remove the field altogether. 

**10: Success message after deleting a blog post, comment or thread.**<br>
I tried to display a success message after deleting an item. However, SuccessMessageMixin for DeleteView doesn't work. According to StackOverflow (https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) the reason for this is that SuccessMessageMixin hooks to form_valid, which is not present on DeleteView to push its message to the user. The solution is to write a function for the delete success message, which I did as follows:
```
from django.contrib import messages

class DeleteBlogPostView(AdminRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = "blog/delete_blog_post.html"
    success_message = "Your blog post was deleted successfully"
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBlogPostView, self).delete(request, *args, **kwargs)
```

**11: Slug for profiles**<br>
I decided to use slugs for the URL's of profile pages. A slug gets created based on the username. If I have a user with a username of testuser, then the slug is testuser. This presented the following issue: when a new user signs up that is identical to another users username, except it has a dot in it (or something else that would get removed when creating a slug), like test.user, then based on its unique username, the user would get accepted by Django. But when the slug is created, the dot gets removed, and then the slug is not unique. Testing this gives the following error: "IntegrityError at /accounts/signup/ UNIQUE constraint failed: profiles_profile.slug". Checking in the admin panel, I saw that the user gets created, but the profile doesn't get created. I therefore used uuid to add an id to the slug, if the slug already exists.

**12: Date of birth**<br>
With the help of StackOverflow, I had written a small function to only accept a date of birth in the past:
```
def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth >= datetime.date.today():
            raise forms.ValidationError("Select a date in the past")
        return date_of_birth
```

This worked fine, as long as the date was filled in. When I tried to delete the date of birth from a profile (since the field is optional), Django threw the following error: ">=' not supported between instances of 'NoneType' and 'datetime.date'".
A small if statement in the function resolved the issue:
```
def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth:
            if date_of_birth >= datetime.date.today():
                raise forms.ValidationError("Select a date in the past")
            return date_of_birth
```

## Unresolved issues
**1: Go to last page of a paginated view**<br>
One of the biggest bugs is caused by the pagination. For example, when the comments are sorted from old to new and the user is on the last page of a paginated thread, and he adds a comment from that last paginated page, then after adding the comment, he is redirected to the first page, which is where he sees the old comments. I would have liked for him to be redirected to the last (paginated) page, where he would see his comment. I have thought about this, for example storing the previous page, and using that as a success URL. But let's say that the new comment by this user, is the 6th or the 11th or the 16th and therefore creates a new page in the pagination, then that wouldn't work. I think I would need to do some math, calculating the number of comments and add one, and then use that in the success URL. But I need more time, which unfortunately, I don't have. It also wasn't something I thought about before building the forum app. An easy fix would be to remove the pagination, which is something I've seen on different forums. But this is not an option if the page gets long because the page doesn't scroll down, see unresolved issue number 2. The easiest fix is ordering the comments from new to old. That way, the user will always see his new comment at the top of the thread page. I don't like it, but it will work for now.
Although, when a user edits a comment, he will always be redirected to the first page after submitting. I would have liked for him to be redirected to the paginated page where he was before on, the thread page.

**2: Scroll down after user action**<br>
After liking or bookmarking a blog post, the page gets refreshed and the users end up at the top of the page. A success message is visible. I would like for the page to scroll down after liking/bookmarking, to where the like and bookmark icons are. I think I would need Ajax for this functionality, but I don't know much Ajax yet.

**3: Last login**<br>
The last login details on the users profile page only shows the date of actually logging in. A user could stay logged in thanks to the cookie and browse the website a day or many days later. Therefore this does not really represent when the user was last browsing the website.


**4: Sorting threads by activity and blog posts by popularity**<br>
I would like to have had the options to sort threads by activity (most recent comment) and sort blog posts by how popular they are (number of likes). I tried this as follows in the ForumView:
```
allowed_sort_fields = {'date_created': {'default_direction': '-',
                                        'verbose_name': 'Date'},
                        'title': {'default_direction': '',
                                     'verbose_name': 'Title'},
				'comments__date_created': {'default_direction': '',
                                     'verbose_name': Activity'}
                        }
```
The problem was that if the two most recent comments were in the same thread, that that specific thread would be displayed twice on the forum. I need to sort with each threads last comment (only the last!). Something similar happened with blog posts. It should be possible, I just need more time and maybe some advice on how to solve this.

**4: TextField instead of CharField**<br>
In the Thread model, I should have set the description field to be a TextField instead of a CharField. Same goes for the biography field in the Profile model. This would look a lot better on the add and edit thread/profile forms. However, I have already added data to the database, and I'm close to submitting the project, so at this point, I will not change my model. 

## Browsers
The final version of the website was tested in different browsers. The website works correctly in Chrome, Ecosia, Opera, Firefox, Microsoft Edge. I used Broswerstack to test some functionality in Safari, but I did not have enough time and I did not want to use a real login. It seemed to work correctly. And with the CSS code being prefixed, I assume it works correctly.
The website does not work correctly in Internet Explorer.

## Responsiveness
- Whilst building this website, testing to see if the website adjusts itself to the size of the device was mostly done with the Chrome DevTool. Media queries are in place to adapt elements to different screen sizes. 
- At the final stage, the website was tested on my personal devices (Lenovo Ideapad 110, HP Pavilion P6330NL with Lenco Monitor (1920px x 1080px), Huawei P30, Samsung Galaxy S4 mini), and my family's and friends' devices. The website was displayed as intended. 
To return to the README file, click [here]( https://github.com/SuzanneNL/pluviophile/blob/master/README.md).
# TESTING 
## Table of contents

- [**Automated testing**](#Automated-testing)
    - [Validating](#Validating)
- [**Testing user stories**](#Testing-user-stories)
- [**Manual testing**](#Manual-testing)
- [**Resolved issues**](#Resolved-issues)
- [**Unresolved issues**](#Unresolved-issues)
- [**Browsers**](#Browsers)
- [**Responsiveness**](#Responsiveness)

## Automated testing
### Validating
- HTML code was validated by the [W3C Markup Validation Service](https://validator.w3.org/) and beautified using [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html). I used the page source for checking, because Django's templating language wasn't recognized. No major errors were found. I missed a few closing tags, and on the account page, this caused a bit of a problem. I corrected these. I was also warned about empty headers for the Open Weather Map modal, but they are supposed to be empty when a user doesn't use the modal. 
- CSS code was validated by the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/), and beautified using [Freeformatter CSS Beautifier](https://www.freeformatter.com/css-beautifier.html). No errors were found. 
- Javascript code was validated by [JSHint](https://jshint.com/), and beautified using [BeautifyTools Javascript Beautifier](http://beautifytools.com/javascript-beautifier.php). I missed quite a number of semicolons, and my indentation was a bit sloppy. I corrected that.
- Python code was validated and corrected when necessary. In the terminal, I ran:
```
python3 -m flake8
``` 
This gave an overview of all the errors/warnings. I had written many lines that were too long. With the help of an online [Python formatter](https://www.tutorialspoint.com/online_python_formatter.htm) and common sense, I was able to correct this. One thing that needed to be corrected was also a CharField in my profiles app that I had set to blank=True and null=True. However (and I knew this), a CharField should not be set to null=True. I therefore set the default to an empty string, like so:
```
blank=True, default=''
```
There are still a few warnings, like lines that are too long in settings.py and in migration files, but I will not edit those. Also, I kept a few files with unused imports (like models.py for the home app and tests.py for all apps), because I could use them later. Finally, in the like and bookmark views, I left the liked and bookmarked variables even though they don't have to be there and aren't used. They make the function more understandable though, and they're not doing any harm to the views. 

## Testing user stories
### As the creator of this website...

#### As the creator of this website...
1. **I want my website to have a clear structure, so that it is easy to navigate.**
    - The website has a clear structure. The navigation bar can redirect users to different parts of the website. Cancel buttons are always present on pages where users can perform CRUD operations. 
    - Users are redirected to relevant pages after they perform CRUD operations. When a user adds a thread, for example, he is redirected to that thread page. And when he deletes this thread, he is sent back to the forum page.
    - A user will only be able to see and visit pages that are relevant to him, as explained in the paragraph 'Structure' of the README file.
    - A 'back to top' button on pages that can get quite long, allows users to go back to the top of the page.
    - Links in content on pages also redirect users to other pages, such as being redirected to the Sign Up page from the Sign In page is a user hasn't got an account yet, or going to user profiles via the forum and thread pages.
2. **I want my website to give feedback to users, so that it is easy to navigate.**
    - Forms give feedback when a user doesn't correctly fill in a fields.
    - Django messages (Bootstrap toasts) give feedback after user actions with color and text (like red for error, green for success). For example, after signing in, the user sees a green success message notifying the user that he has signed in successfully.
    - Hover effects such as a pointer or changing colors of/in a button also give feedback to the user, about whether or not something can be clicked.
3. **I want my website to inform and entertain users with blog posts about rain.**
    - In the blog part of the website, users will find several blog posts with rain related topics. Users can like these blog posts with the like button, or bookmark them so that they can read them again later.
4. **I want my website to connect members of the pluviophile community.**
    - Users can communicate with each other via the forum. They can introduce themselves, respond to different threads. They also have public profiles, that they manage themselves. They can decide what information they would like to show there. 
5. **I want to let my registered users manage content they created themselves.**
    - Users can create content for the forum (threads and comments), and their profile. They can edit and delete this content whenever they want. They can also like and bookmark blog posts and they can also undo these actions. Other users (except for superusers) do not have these rights. Users can only edit and delete their own content. They however cannot delete their own accounts or delete information about donations they've made. 
6. **I want to protect the work of users by not giving rights to edit and delete content or information of others.**
    - As I stated above, users can only edit and delete their own content. Trying to access edit and/or delete pages for other users content, will result in being redirected to an error page. 
7. **I want to prevent guest users to upload content and also see content that is not meant for them.**
    - Guest users do not have access to the blog, forum, donation and profiles apps. They cannot even see these apps in the navigation bar. Trying to access a page from one of these apps results in the user being redirected to the login page. 
8. **I want to warn users when they try to delete their content, as a form of defensive programming.**
    - Users always get redirected to a confirm deletion page after clicking on delete for a part of content. They can always cancel. Only after confirming their choice, will their content be deleted. 
9. **I want superusers to have CRUD rights over all the content on this website, in case users behave in an unwanted fashion.**
    - Superusers have CRUD rights over content created by users, except for donation content. I don't think it is responsible for a superuser to be able to edit financial content. 
10. **I want to be financially supported by members in the form of a voluntary donation.**
    - Registering is free, users do not have to pay a registration fee. However, they will see the 'donate' option in the navigation bar. When they click on this, they will see why the website asks for a small donation. They can be redirected to a page where they can fill out their credit card details, for a donation of € 5,-. If they submit this form, the credit card is charged and a donation is made. Users can make multiple donations if they want. The donation option doesn't disappear after a user has made a donation. 

As a user in general...
1. **I enjoy the rain.**
    - The website is intended for people who have an interest in or love the rain. On this website they can read about it and talk about it. There is also a rain animation, just for fun.
2. **I enjoy reading about rain related topics.** 
    - The blog contains several blog posts about rain related topics. If a user enjoys a blog post, he can like it and/or bookmark it. 
3. **I enjoy taking part in rain related conversations.** 
    - The forum serves as a platform where users can join in on conversations about rain related topics. Users can create threads and/or comment on threads, as soon as they register.
4. **I want to be able to easily navigate the website.** 
    - As explained above, the website has different elements in place (navigation bar, URL's in content, buttons) to facilitate navigation. 

As a guest user...
1. **I want to get an idea of what the website has to offer.**
    - The home page shows a definition of the word 'Pluviophile', and sees three cards that explain what the website offers (profiles, forum, blog). The user also has access to the Make it rain! animation and the Find the rain functionality. 
2. **I want to be able to sign up, so that I can get access to the blog, forum, profiles and donation pages.**
    - Users can either click the button under the welcome text or use the navigation bar to go to the Sign Up page, where they can register with a username and an e-mail address. As soon as they have registered, they get access to the blog, forum, donation and profiles apps. 

As a logged in user...
1. **I want to read, like and bookmark blog posts.**
    - Users that are signed in can read all the blog posts. At the bottom of each blog post they see two icons: a bookmark for bookmarking the blog post and a heart for liking the blog post. Bookmarks can be found on the account page. Users can also see who liked a blog post by clicking 'show likes'. 
2. **I want to be a part of the forum.**
    - Users that are signed in can read all content on the forum. They can start threads and comment on threads. The number of posts they make (either creating threads or commenting on threads) influences their activity status. 
3. **I want to update my profile.**
    - Users can write a biography, add a date of birth and add their country on their profile page. There will be a default avatar, but they can update it with their own image. This information and this avatar are then visible for all signed in users.
4. **I want to manage content that I have created.**
    - Users can edit and delete the content that they create in both the forum and profiles app. They however cannot update or delete their donation details. If they have bookmarked a blog post, they can remove the bookmark. Also, they can unlike blog posts that they have liked, at any time. 
5. **I can, for the most part, decide what information other users see about me.** 
    - Users will choose their own username. This will be visible for other users as soon as a user likes a blog post or joins in on a conversation on the forum. Also, users can visit the profile that is created automatically when he signs up. Here, users can see information about the specific user's activity, like his activity status (a number of drops, based on the number of posts) or when he was last signed in. Some of this information is also visible on the forum. However, a user can write his own biography, select his own date of birth, select his own country and upload his own avatar. These are things that he has control over.
6. **I want to see my private information details on my account page.**
    - When users click on their username in the navigation bar, they see that they can go to their account page. On the account page, a user sees his username and his e-mail address, as well as the option to change his password. Users can find their bookmarks underneath this personal information. And, if a user has made a donation, he can see his donation details, and the total amount he donated. All of this is only visible for the logged in user. Superusers/admin will also see a table with all the donations (by all users).
7. **I want to be able to update my password.**
    - Like I said above, users can update their password. This is handled by Django allauth. 
8. **I want to have the possibility to make a donation.**
    - Signed in users see 'Donate' in the navigation bar. If a user clicks on this, he will see a short text explaining why the website asks for a small donation. A user can then make a donation of € 5,-. Donation details for that specific donation will be shown on the donation success page. All donations can also be found on the account page. 
9. **I want to be able to log out.**
    - When a user clicks on his username in the navigation bar, he sees the option 'Sign Out'. When he clicks on this, the user will be redirected to a page asking him to confirm his wish to sign out. When he does, he is signed out and redirected to the home page as a guest user. 

## Manual testing
Manual testing was done on different devices (see Responsiveness).

### Navigation bar
The navigation bar is visible on all pages (except the Make it rain! page) and fixed to the top, so it stays visible as the user scrolls down. It redirects users to different parts of the website. The items in the navigation bar vary, based on whether a user is logged in or not. As a guest user, one sees Home, Find the rain, Make it rain!, Sign In and Sign Up. 
Once signed in, the options Sign Up and Sign In have disappeared. Instead, users see Forum, Blog and Donate. They also see their own username with their avatar next to it. Clicking on the username opens a dropdown menu, that shows options to be redirected to the Profile and Account page or to sign out. 

### Footer
- The icon sticks to the bottom of the page, even when there is little content on the page.
- The icons and the name SuzanneNL in the footer have a hover effect: the mouse turns into a pointer and the color of the icons/text change.
- When a user clicks on one of these icons or SuzanneNL, he is redirected to the corresponding website in a new tab. 

### Home
- Users see a definition of Pluviophile and a background image that is also visible on many other pages (but not all). There's a join button and are three cards that inform about the profiles app, the forum app and the blog app. If the user is logged in, the join button has disappeared. Instead, in each card, the user sees a button to be redirected to that app. 

### Find the rain
- Clicking on this in the navigation bar, will open a modal with a call to enter a city. This works with Open Weather Map API. After entering a city, the user will see what the weather is for that specific city, and a message about whether or not it's raining there. This is based on the weather code. If the API call is unsuccessful (f.e. if the user enters a city name that doesn't exist), an error messsage is visible. 

### Make it rain!
- Clicking on this in the navigation bar, will open a page with a Javascript rain animation. The animation can be opened at any time, and will redirect back to the previous page when it is closed. If a user comes from a different website, the user will be redirected to the home page.

### Sign Up, Sign In, Sign Out with Django Allauth
- Django Allauth handles signing up, signing in and signing out actions, and it works as intended. For example, when a user tries to sign up with a username that already exists in the database, an error message is displayed under the username field. Or when a username doesn't meet the requirements, an error message under the field in the form will display what the requirements are. When a user tries to log in with incorrect credentials, he will be redirected to the sign in page, where an error is shown that the username and/or password the user specified were incorrect. 
- Django Allauth uses django messages to inform a user if signing up, signing in and signing out have been successful, on the next page. 
- Django Allauth redirects a user to a confirmation page when he tries to sign out. 

### Forget Password with Django Allauth
- When a user tries to sign in but doesn't remember his password, he can click on 'Forgot password'. This redirects him to a form where he has to fill in his e-mail address. An e-mail with a reset link is then sent to the user's e-mail address. That is, if it exists in the database. If not, the user sees an error message: 'The e-mail address is not assigned to any user account'.

### Reset Password with Django Allauth
- On the account page, the user sees that he can update his password. Clicking on this will send him to a form where he has to fill in his old password, and his new password twice. Django Allauth will throw errors if the user makes a mistake (like not correctly repeating the new password) or fills in a new password that doesn't meet the requirements. If the changing of the password was successful, a success message is shown.

### Forum app - View, paginate and sort threads
- A user sees all threads that have been created on the forum page. He sees the number of threads that have been created. For each thread that has been created, he sees a section with the title, the user who created it, when it was created, how many comments the thread has and who created the last comment, and when this was done. If there are no comments, he sees 'No comments' yet. A user can click on the usernames in such a thread section, and then be redirected to that users profile page.
- Threads are paginated per 5 threads.
- Threads can be sorted by date, ascending and descending, and by title, also ascending and descending (alphabetical order). By default, they are ordered by date descending. 
- Clicking on 'Start a new thread' will redirect the user to a form where he can add a new thread. 

### Forum app - Add thread
- A user can fill out the form. He has to fill in both fields: title and description. There are no requirements, except for the fact that the title cannot exceed 60 characters, and the description cannot exceed 2000 characters. 
- A user can either click Cancel, which will redirect him to the forum page. Or he can click 'Start thread', which will send him to the freshly added thread detail page. A success message is visible in the top right of the screen. On the thread page, the user will see his title and description, as well as some of his information. As he is the creator of that thread, he will also see an edit and delete button. 

### Forum app - Edit thread
- After clicking on 'Edit thread' the user gets redirected to the edit thread page. He sees the same form as on the add thread page, but the content is already filled in, in the form fields. 
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user clicks 'Edit thread', any changes he has made will be saved. He will then be redirected to the thread page. A success message is visible in the top right of the screen. 

### Forum app - Delete thread
- After clicking on 'Delete thread' the user gets redirected to a page where he's asked to confirm his wish to delete the thread.
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user confirms, the thread gets deleted from the database and the user is redirected to the forum page. A success message is visible in the top right of the screen. Also, his thread will no longer be visible on the forum page, as it doesn't exist in the database anymore. 

### Forum app - View and paginate comments
- A user sees comments that have been added to a thread on the thread page. Next to the paginator, he sees the number of comments that have been added, and what page he is on. 
At the top of each page, he will see the thread section, which contains the title, the description, when it was created, if and when it was edited and information about the user who created the thread.
For each comment that has been added, the user sees a section with the comment itself, the user who added it, when it was added, and if (and when) it was edited. If there are no comments, he sees 'There are no comments yet', and one button to 'Drop a comment'. If there are comments, there will be a button above and below the comments. 
A user can click on the usernames in the thread or in a comment section, and then be redirected to that users profile page.
The information that a user sees from other users is their username, a flag (if the user has selected his country on the profile page), his avatar, a number of blue drops representing how active the user is, and when the user joined the website. Superusers always get 5 golden drops by the way. 
- Comments are paginated per 5 threads.
- Comments are ordered by date (old to new).  
- Clicking on 'Drop a comment' will redirect the user to a form where he can add a new comment. 

### Forum app - Add comment
- A user can fill out the form, which is just one field. There are no requirements, except for the fact that the post cannot exceed 2000 characters, and that it cannot be left blank. 
- A user can either click Cancel, which will redirect him to the thread page. Or he can click 'Add comment', which will also send him to the thread page. A success message is visible in the top right of the screen. On the thread page, the user will see that his comment has been added. As he is the creator of that comment, he will also see an edit and delete button for it. 

### Forum app - Edit comment
- After clicking on 'Edit' at the bottom of a comment, the user gets redirected to the edit comment page. He sees the same form as on the add comment page, but the content is already filled in, in the form field. 
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user clicks 'Edit thread', any changes he has made will be saved. He will then be redirected to the thread page. A success message is visible in the top right of the screen. 

### Forum app - Delete comment
- After clicking on 'Delete' at the bottom of a comment, the user gets redirected to a page where he's asked to confirm his wish to delete the comment.
- If the user clicks on cancel, nothing happens and the user gets redirected to the thread page. If the user confirms, the comment gets deleted from the database and the user is redirected to the thread page. A success message is visible in the top right of the screen and of course the comment will no longer be visible on the thread page, as it doesn't exist in the database anymore. 

### Blog app - View, paginate and sort blog posts
- A user sees all blog posts that have been created on the blog page. He sees the number of blog posts that have been created. For each blog post that has been added, he sees a card with the first image, the author who wrote it, when it was uploaded, the title and the first 30 words of the blog post. A user can click on the image and on the 'read blog post' button to go to the blog post.
- Blog posts are paginated per 4 blog posts.
- Blog posts can be sorted by date, ascending and descending, and by title, also ascending and descending (alphabetical order). By default, they are ordered by date descending. 
- At the top of the first page, superusers can see a button 'Add Blog Post'. Clicking this will redirect the superuser to a form where he can add a new blog post. 

### Blog app - Add blog post
- At the top of the form, the user sees a button to display instructions. Unfortunately, the process isn't very user friendly. A rich text editor might be implemented in the future. But if the user follows the instructions, a blog post can be added. 
- A user can fill out the form, which consists of multiple fields. There are no requirements, except for the fact that the fields with an asterix are required. 
- A user can either click Cancel, which will redirect him to the blog main page. Or he can click 'Add blog post', which will send him to the fleshly created blog post page. A success message is visible in the top right of the screen. All superusers will see an edit and delete button at the bottom of the blog post, and they can all edit and delete the blog post. 
On the blog main page, the user will see that his blog post has been added. 

### Blog app - Edit blog post
- After clicking on 'Edit blog post' the user gets redirected to the edit blog post page. He sees the same form as on the add blog post page, but the content is already filled in, in the form fields. 
- If the user clicks on cancel, nothing happens and the user gets redirected to the blog post page. If the user clicks 'Edit blog post', any changes he has made will be saved. He will then be redirected to the blog post page. A success message is visible in the top right of the screen. 

### Blog app - Delete blog post
- After clicking on 'Delete blog post' the user gets redirected to a page where he's asked to confirm his wish to delete the blog post.
- If the user clicks on cancel, nothing happens and the user gets redirected to the blog post page. If the user confirms, the post gets deleted from the database and the user is redirected to the blog main page. A success message is visible in the top right of the screen. Also, the blog post will no longer be visible on the blog main page, as it doesn't exist in the database anymore. 

### Blog app - Like blog post
- At the bottom of the page, users see a white heart icon. Clicking on this icon will result in adding a like. 
- This will reload the page. A success message is visible in the top right of the screen. The heart will now be red. Clicking it will result in removing the like.
- This will reload the page. A success message is visible in the top right of the screen. The heart will be white again.
- Users can only like an article once. Next to the heart, it says how many likes the blog post has gotten. If there are likes, users see a small button 'Show likes'. If a user clicks on this he will see a list of users who have liked the article. These users can not be clicked.

### Blog app - Bookmark blog post
- At the bottom of the page, users also see a white bookmark icon. Clicking on this icon will result in adding a bookmark. 
- This will reload the page. A success message is visible in the top right of the screen. The bookmark will now be blue. Clicking it will result in removing the bookmark.
- This will reload the page. A success message is visible in the top right of the screen. The bookmark will be white again.
- Users can only bookmark an article once. Articles that have received a bookmark from a user, will be shown on the account page. 

### Donation app 
- When a user clicks on Donate in the navigation bar, he will see an explanation why the website asks for donations. If he proceeds and clicks 'Make donation', he will be redirected to the charge page. 
- As soon as he opens this page, a payment intent of € 5,- will be sent to Stripe.
- A user must fill in his full name, e-mail address and credit card information. Stripe provides credit card information to test the form:
```
There are several test cards you can use to make sure your integration is ready for production. Use them with any CVC, postal code, and future expiration date.

4242424242424242 - This succeeds and immediately processes the payment.
4000000000003220 - 3D Secure 2 authentication must be completed for a successful payment.
4000000000009995 - Always fails with a decline code of insufficient_funds.
```
These credit card numbers work as intended.
- When the processing of a payment is successfully handled by Stripe, the donation is created in the database and the user gets redirected to the donation success page where he can see details from the donation: date, amount and donation number. Each donation receives a unique donation number. A success message is visible in the top right of the screen. This page can only be accessed by the donor. 
- All donation details, for each donation, will also be visible on the account page.
- A webhook process is in place for when the payment processing doesn't succeed immediately. 

### Profile app - Profile page
- A user can go to his profile by clicking on his username in the navigation bar and clicking on 'Your profile' in the dropdown menu. Of course, he could also click on his username if it is displayed somewhere in the forum. 
- Users can visit each other's profiles, by clicking on usernames on the blog.
- For his own profile, he will see an 'Edit profile' profile button. 
- Default information is the date he joined, the number of threads and comments he has posted/created, and an activity status in blue drops, based on the aforementioned numbers. It will also have a default avatar. For the country and date of birth, it will say 'Unknown'. There will not be a flag next to his username. And it will see that the user hasn't written a bio yet.
- Superusers will have (Admin) behind their username in the page title. They will also have a status of 5 golden drops. 

### Profile app - Edit profile
- After clicking on 'Edit profile' the user gets redirected to the edit profile page. He sees a form and if he added content to his profile in the past, the content is already filled in, in the form fields. If not, these fields are left empty.
- A user can select his date of birth. A datepicker is used, but he can also manually type it. This date cannot be in the past. An error will be displayed if the user tries to submit the form with a date in the future, or today. The field is still optional, though. 
- A user can select his country. If he submits the form, then from that point on, a small flag will be visible next to his username on the profile and on thread pages. He can always unselect his country, then the flag disappears.
- If the user clicks on cancel, nothing happens and the user gets redirected to the profile page. If the user clicks 'Edit profile', any changes he has made will be saved. He will then be redirected to the profile page. A success message is visible in the top right of the screen. 

### Profile app - Account
- A user can go to his account page by clicking on his username in the navigation bar and clicking on 'Your account' in the dropdown menu. 
- The user sees this account details and a button to be redirected to a page where he can update his password. This is handled by Allauth, as I described at the beginning of this section. 
- The user also sees his bookmarks, if he has any. These are the titles of the blog post he bookmarked, which he can click to go to the blog post.
- If the user has donated to Pluviophile, a donation table gets created. For each donation, a row is added, showing exactly when the donation was made, which details the user gave (name, e-mail address), the amount (always € 5,-) and the donation number. 

### Django Messages
- Django messages (Bootstrap toasts) give feedback after user actions with color and text (like red for error, green for success). They disappear when a user closes the message box, or when a user goes to a different page. 

### Buttons
- All buttons have hover effects and redirect users to different pages or hide/show information. There are no broken buttons or links. 

## Resolved issues
**1: Class name in models = Class name in views**<br>
The first bug I encountered was when I was creating a page for starting a thread. I had a model called Thread ('class Thread'), and I also named my class based view Thread (so also 'class Thread'). Apparently this made Django confuse the two. It gave me an error, stating that: "type object 'Thread' has no attribute '_meta'". Changing the name of the view to ThreadView solved the error. 

**2: Threads with PK of 10 and higher**<br>
I was adding new threads to my forum, but when I reached 10 threads, and so a pk of 10, I got an error: "NoReverseMatch at /forum/start_thread/ Reverse for 'thread' with arguments '('1', '1')' not found. 1 pattern(s) tried: ['forum/thread/(?P<pk>[0-9]+)$']"

It seemed like it was looking for two separate arguments, 1 and 0 or 1 and 1 or 1 and 2 etc. 
This was my model:
```
class Thread(models.Model):
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('thread', args=(str(self.id)))
```

Underneath self from self.id, I got a notification that: "Instance of 'Thread' has no 'id' memberpylint(no-member)".

I concluded that the problem was in the id-part. Switching to pk, solved the issue:
```
    def get_absolute_url(self):
        return reverse('thread', kwargs={'pk': self.pk})
```
This way, it accepted pk's of higher than 10. I later used this same code for my blog posts, because I saw the same error with 'id'. I didn't encounter any errors on the website itself, probably because I never added more than 9 blog posts.

**3: Comparing date created and date edited**<br>
When a thread gets created, it receives two date time fields. One for date created and one for date edited:
```
class Thread(models.Model):
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
```
I thought these DateTimeFields would be identical when the thread gets created. And I thought that when a user edits a thread, only the field 'date_created' would get updated. 
The issue was this: I wanted my template to display the date_edited value only when this was different from the date created (and therefore actually edited). So I used the following if statement in my template:
```
{% if thread.date_created != thread.date_edited %}
     <p>edited on: {{ thread.date_edited }}</p>
{% endif %}
```
I thought this was an easy thing to do, but apparently there's a very small difference (perhaps a few milliseconds) between the two timestamps when a thread gets created. Therefore, even when a thread hadn't been edited by a user, both dates and times were displayed.
I therefore had to filter the two timestamps to the second. With the following if statement, the problem was resolved:
```
{% if thread.date_created|date:"D, d M, Y, H:i s" != thread.date_edited|date:"D, d M, Y, H:i s" %}
     <p>edited on: {{ thread.date_edited }}</p>
{% endif %}
```

**4: Going back to the thread to which a user added a comment**<br>
I had written the following view for adding a comment:
```
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "forum/add_comment.html"
    fields = ['post']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
```
After submitting the form for adding a comment, it produced the following error: "IntegrityError at /forum/thread/26/add_comment/ NOT NULL constraint failed: forum_comment.thread_id"

I therefore added the pk as the id:
```
def form_valid(self, form):
    form.instance.thread_id = self.kwargs['pk']
    form.instance.creator = self.request.user
    return super().form_valid(form)
```

I was now able to add comments, but was redirected to a thread with the pk of the comment. I fixed this by setting the success URL:
```
def get_success_url(self):
    return reverse_lazy('thread', kwargs={'pk': self.kwargs['pk']})
```

**5: Going back to the thread after a user edits a comment**<br>
I wrote the following view for editing a comment in a thread:
class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = "forum/edit_comment.html"
    form_class = CommentForm

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')

After editing a comment, I got an error: "NameError at /forum/edit_comment/4 name 'thread' is not defined". This was because in the Comment model, I had written the get_absolute_url function, for when a new instance of the model gets created:
class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name="comments",
                               on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "On '%s' by %s" % (self.thread, self.creator)

    def get_absolute_url(self):
        return reverse('thread', kwargs={'pk': thread.pk})

I wanted a user to go back to the thread after editing a comment, but 'thread' was not defined according to the error. So I tried defining it again:
```
def get_absolute_url(self):
    thread = models.ForeignKey(Thread, related_name="comments", on_delete=models.CASCADE)
    return reverse('thread', kwargs={'pk': thread.pk})
```
This is kind of funny to see in hindsight, because I just copied from the model, and that's not how I should have defined it. Anyway, I got an error that there is no pk for the thread. Because I was still learning and testing, to see what happens, I also wrote self.pk:
```
def get_absolute_url(self):
    thread = models.ForeignKey(Thread, related_name="comments", on_delete=models.CASCADE)
    return reverse('thread', kwargs={'pk': self.pk})
```
This, of course, sent me to a thread but not the one where I came from, but the one with the same pk as the comment I just edited. 

I then started looking into maybe hiding the thread.pk somewhere in a field of the CommentForm. But after some research on Google, I found a very nice trick on StackOverflow. You can add ?next={{ request.path }} to the link that directs to the edit comment page:
```
<a href="{% url 'edit_comment' comment.pk %}?next={{ request.path }}">Edit comment</a>
```
And then wrote the get_success_url as follows in the view:
```
def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))
```
This works: it sends a user back to the thread page. As I'm writing this, nearly at the end of my project, I'm thinking that there should be better ways to do this. But at this stage of my project, I have to follow the advice I've seen in coding memes that 'if it works, don't touch it!'.

**6: Cancel buttons in edit and delete comment templates**<br>
When a user edits or deletes threads, there's always a cancel button, that redirects the user back to the thread itself. I tried to do the same in the edit and delete comment templates. For example, in the delete comment template, I had written:
```
<button class="btn btn-danger" type="submit">Yes, delete comment</button>
<a class="btn btn-secondary" href="{% url 'thread' thread.pk %}">Cancel</a>
```
This however, threw an error when I was trying to access the delete comment page: "NoReverseMatch at /forum/comment/delete/9 Reverse for 'thread' with arguments '('',)' not found. 1 pattern(s) tried: ['forum/thread/(?P<pk>[0-9]+)$']".
Simply deleting the cancel button solved the issue and I got access to the page again. I then placed ?next={{ request.path }} (see my previous resolved bug) behind the URL that redirects to the delete comment page.
And then on that page, I redirect the user to the same success URL as the one that a user is redirected to after confirming the deletion:
```
<a class="btn btn-secondary" href="{{ view.get_success_url }}">Cancel</a>
```
And that worked: clicking the cancel button, makes the user go back to the thread page (without the comment being edited of course). 

**7: Go to last page of a paginated view**<br>
Due to time restrictions (this is my last resolved bug), I will copy and paste the text for a bug that was in the 'unresolved' section, and then add my solution. It's a bug that I encountered after adding more than 5 comments with pagination (by 5) in place:
<br><em>
One of the biggest bugs is caused by the pagination. For example, when the comments are sorted from old to new and the user is on the last page of a paginated thread, and he adds a comment from that last paginated page, then after adding the comment, he is redirected to the first page, which is where he sees the old comments. I would have liked for him to be redirected to the last (paginated) page, where he would see his comment. I have thought about this, for example storing the previous page, and using that as a success URL. But let's say that the new comment by this user, is the 6th or the 11th or the 16th and therefore creates a new page in the pagination, then that wouldn't work. I think I would need to do some math, calculating the number of comments and add one, and then use that in the success URL. But I need more time, which unfortunately, I don't have. It also wasn't something I thought about before building the forum app. An easy fix would be to remove the pagination, which is something I've seen on different forums. But this is not an option if the page gets long because the page doesn't scroll down, see unresolved issue number 2. The easiest fix is ordering the comments from new to old. That way, the user will always see his new comment at the top of the thread page. I don't like it, but it will work for now.
Although, when a user edits a comment, he will always be redirected to the first page after submitting. I would have liked for him to be redirected to the paginated page where he was before on, the thread page.
</em><br>
Right before my deadline, I was still very annoyed by this bug. So I decided to give it one last try. I updated the success_url for the AddCommentView:
```
def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))
```
I realized that I could go to a set paginated page like so:
```
<a href="{% url 'add_comment' thread.pk %}?next={{ request.path }}?page=2" class="btn btn-blue">Drop a comment</a>
```
This brought me to the second page.
The next step was taking a piece of code from the pagination section:
```
<a href="{% url 'add_comment' thread.pk %}?next={{ request.path }}?page={{ comments.paginator.num_pages }}" class="btn btn-blue">Drop a comment</a>
```
This worked. But I paginate by 5 comments. So if I create number 6, 11, 16, 21 etc, a new page needs to be created and that then doesn't work. I got sent to the page before the last (freshly created) page. So the last step was to do a little bit of math in the get_context_data function of the view:
```
import math
comments_count = self.object.comments.count()
calc_next_page = (comments_count + 1) / 5
next_page = math.ceil(calc_next_page)
```
And then using that next_page in the template as follows:
```
<a href="{% url 'add_comment' thread.pk %}?next={{ request.path }}?page={{ next_page }}">Drop a comment</a>
```
This will always redirect to the last page of the thread. Also, I used the code for the current page from my paginator in the URL for the edit comment buttons, like so:
```
<a href="{% url 'edit_comment' comment.pk %}?next={{ request.path }}?page={{ comments.number }}">Edit</a>
```
I did not update the cancel buttons on the add and edit comment pages (because of my deadline).

**8: Displaying the number of threads and comments created by a user who commented on a thread page**<br>
All users get an activity status (a number of drops) based on the number of posts (either comments or threads) they created on the forum. I was able to display these numbers on the public profile page without any problems. And I was also able to display this information on the thread page for the user who created the thread as follows in the view:
```
class ThreadView(LoginRequiredMixin, DetailView):
    model = Thread
    template_name = "forum/thread.html"
    ordering = ['date_created']

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        current_thread = self.get_object()
        page = self.request.GET.get('page')
        comments = Paginator(self.object.comments.all(), 5)
        context['threads_by_thread_creator'] = Thread.objects.filter(
                                               creator=current_thread.creator)
        context['comments_by_thread_creator'] = Comment.objects.filter(
                                                creator=current_thread.creator)
        
        context['all_threads_on_forum'] = Thread.objects.all()
        context['all_comments_on_forum'] = Comment.objects.all()
```
And as follows in the template:
```
<small>Threads: {{ threads_by_thread_creator.count }}</small><br>
<small>Comments: {{ comments_by_thread_creator.count }}</small>
```
I was not able to work out however, how to display this for the creator of a comment. This is because I loop through the comments, and cannot get the pk of a specific comment that I'm displaying on the tempalte, in views.py:
```
current_comment = Comment.pk  # This doesn't work
context['threads_by_comment_creator'] = Thread.objects.filter(creator=current_comment.creator)
context['comments_by_comment_creator'] = Comment.objects.filter(creator=current_comment.creator)

```
I spoke with tutor support for hours, but the tutors were not able to figure it out either. I then looked at 'annotate' and context processors but was still not able to solve this. I therefore chose a different approach:
In the template, inside the comment div, I call all the threads and comments created on the forum, and filter with an if statement as follows:
```
{% for obj in all_threads_on_forum %}
{% if obj.creator == comment.creator %}
<span class="count-this">{{ obj.creator }}</span>
{% endif %}
{% endfor %}
{% for obj in all_comments_on_forum %}
{% if obj.creator == comment.creator %}
<span class="count-this">{{ obj.creator }}</span>
{% endif %}
{% endfor %}
```
With jQuery I then count the number of spans created (=the number of posts created by the comment creator), and based on that number, I display the status of the user:
```
$(document).ready(function(){
    $(".elements").each(function(ind, val){
        var nTotalComment = $(val).find(".count-this").length;
        if (nTotalComment < 5) {
            $(val).find(".count").html("status 1")
        }
        else if (nTotalComment < 10) {
            $(val).find(".count").html("status 2")
        }
        else if (nTotalComment < 20) {
            $(val).find(".count").html("status 3")
        }
        else if (nTotalComment < 25) {
            $(val).find(".count").html("status 4")
        }
        else {
            $(val).find(".count").html("status 5")
        }
    });
});

</script>
{% endblock %}

```
I decided to use this approach for the thread creator as well, for consistency on that template.  
It doesn't feel like the most elegant approach, and I know that logic shouldn't be handled in the template, but I was very happy to get the result I wanted. I would love to learn how I could have done this differently. 

**9: Stripe payment unsuccessful**<br>
In my project, users can donate 5 euros to Pluviophile. I was following the Boutique Ado project and I could see in Stripe that when I opened my charge page, a payment intent got created in Stripe - as it should. But the payment didn't succeed in Stripe after submitting the form. With the JS code present, the form wouldn't get processed at all. The submit button and card-section would get disabled, and then the page would get stuck and nothing else would happen.
When I changed the id of the form (and therefore skipped the JS code), the donation did get created in my own database, and I did go to the 'donation succeeded' page. Which showed me that there was nothing wrong with the POST part of my view. 
So I thought there was a problem with my Javascript. I checked my console, but there were no errors.
I went to the next step in the Boutique ado project: adding the overlay. With the overlay added to my code, when I clicked the submit button, the overlay would appear, but it wouldn't go away. So I concluded that something was going wrong AFTER the payment intent was created, and AFTER the submit button and card-section would get disabled and also AFTER the overlay would appear, but BEFORE the payment was supposed to succeed.
I was sure that the problem was in this part of my code:
```
stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
```
But it was identical to the boutique ado project. Stripe told me that:
the status of the PaymentIntent was: 'requires_payment_method'.
I checked my clientSecret, which is saved in my env.py file, and it looked fine. 
I checked my terminal for errors, and there were none. I checked my console again for errors, and there were none. With the help from tutor support, I found out that I had a filter on in my console (accidentally), which prevented me from seeing all errors. When I fixed this, I could see that the problem had to do with the public and secret keys from Stripe: "Uncaught IntegrationError: Invalid value for stripe.confirmCardPayment intent secret: value should be a client secret of the form ${id}_secret_${secret}. You specified: intent.client_secret."
So I checked where my keys were being passed on to the template, and found that the problem was in my view. I had put quotation marks around the client secret and public key. Removing them resolved the issue. 

**10: Setting the logged in user as donor of a new donation, when form submission fails**<br>
I was at the end of the webhooks videos from the Boutique Ado project, and I ended up having one final issue. I was trying to pass through the logged in user as the donor in the 'handle_payment_intent_succeeded' function in the webhook handler, for when the donation doesn't exist in my database yet and needs to be created. To test this, the submit button in Javascript was disabled.

In the CI videos, it was said that I could use request.user to get the donor, because the request object was added to the init method at the top. So I first tried this:
```
try:
    donation = Donation.objects.create(
    donor = request.user,
    donor_full_name=billing_details.name,
    email=billing_details.email,
    stripe_pid=pid,
)
```
But this gave me an error in Stripe: "Webhook received: payment_intent.succeeded | ERROR: name 'request' is not defined".

Then I used self.request.user:
```
try:
    donation = Donation.objects.get(
        donor = self.request.user,
        donor_full_name__iexact=billing_details.name,
        email__iexact=billing_details.email,
        stripe_pid=pid,
    )
```
This have me a different error. In my terminal I could see: "TypeError: 'AnonymousUser' object is not iterable'". In Stripe, I didn't get a message but a bunch of HTML code.

After looking at different Stackoverflow posts, where people advised to check if the user is authenticated, I tried the following:
```
if self.request.user.is_authenticated:
    billing_details = intent.charges.data[0].billing_details
    # Clean data in the shipping details
    for field, value in billing_details.address.items():
        if value == "":
            billing_details.address[field] = None
    donation_exists = False
    attempt = 1
    while attempt <= 5:
        try:
            donation = Donation.objects.get(
                donor = self.request.user,
                donor_full_name__iexact=billing_details.name,
                email__iexact=billing_details.email,
                stripe_pid=pid,
            )
[etc]
return HttpResponse(
            content=f'Webhook received: {event["type"]} | ERROR: User error',
            status=500)
```
Also, I made sure that only logged in users could access these pages with @login_required.
I tried this code but got an internal server error in the terminal: 
```
08/Apr/2021 14:12:59] "POST /donation/wh/ HTTP/1.1" 200 50
Internal Server Error: /donation/wh/
[08/Apr/2021 14:13:31] "POST /donation/wh/ HTTP/1.1" 500 74
[08/Apr/2021 14:13:32] "POST /donation/wh/ HTTP/1.1" 200 44
```
And in Stripe I saw the message: "Webhook received: payment_intent.succeeded | ERROR: User error." 
This 'Error: User error' was the error I wrote myself, in case a user wasn't authenticated.

I did some more research and someone mentioned that users might get logged out for a bit when working with Stripe, but I checked my cookies and the 'sessionid' didn't disappear. 

I also tried changing the location of the if statement (where it is in the CI video):

```
        if self.request.user.is_authenticated:
            donation_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    donation = Donation.objects.get(
                        donor = self.request.user,
                        donor_full_name__iexact=billing_details.name,
                        email__iexact=billing_details.email,
                        stripe_pid=pid,
                    )
[etc]
        return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: User error',
                status=500)
```
This gave the exact same errors.

I also tried:
```
if self.request.user.username != 'AnonymousUser':
```
This gave the following error: "TypeError: 'AnonymousUser' object is not iterable".

Trying this code:
```
username = self.request.user.username
        if username != 'AnonymousUser':
```
Gave the exaxt same error: "TypeError: 'AnonymousUser' object is not iterable". And trying this:
```
username = self.request.user
        if username != 'AnonymousUser':
```
gave me the, by now familiar, type error: "TypeError: 'AnonymousUser' object is not iterable". 
I then started working with tutor support and from the charge view the tutor printed in the terminal who the charging user was when the charge page is opened:
```
def charge(request):
    
    print(f"CHARGE USER: {request.user}")

```
Then, from the webhook handler, he  printed in the terminal who the WH user was:
```
class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
        print(f"WH USER: {self.request.user}")

```
This showed as the logged in users username 'Pieter' as charge user (the logged in user), but 'AnonymousUser' as the wh user:
```
CHARGE USER: Pieter
[09/Apr/2021 15:09:20] "GET /donation/charge/ HTTP/1.1" 200 8269
[09/Apr/2021 15:09:21] "GET /static/js/stripe_elements.js HTTP/1.1" 304 0
[09/Apr/2021 15:09:21] "GET /static/css/donation.css HTTP/1.1" 304 0
WH USER: AnonymousUser
```
We tried working around this by creating an extra session variable, but this didn't get picked up. After several hours, and when the shift of the tutor finished, he gave me advice to look at the Boutique ado project, where information from the metadata is used to decide who the user is, and where information gets connected with the UserProfile. 
I was confused at first, because I didn't want to connect it to the UserProfile, and I hadn't added metadeta, but I decided to use that approach and try to connect it to the User object. 
I was able to retrieve the email from the payment intent's billing details. Then I used that to get the logged in user. And then if the logged in user wasn't AnonymousUser, the user will be the User object with the same e-mail address as the one in the billing details.
```
user_email = intent.charges.data[0].billing_details.email
if self.request.user != 'AnonymousUser':
    user = User.objects.get(email=user_email)
```
Then I set that user as the donor:
```
donation = Donation.objects.create(
    donor=user,
    donor_full_name=billing_details.name,
    email=billing_details.email,
    stripe_pid=pid,
)
```
This is how the webhook finally worked! 
I checked this also with the deployed website. When the payment process goes without issues, on Stripe I can see that the payment_intent has succeeded and a message: 'SUCCESS: Verified donation already in database'. When I disable the form submission, I can see on Stripe that the payment_intent has succeeded but a different message: 'SUCCESS: Created donation in webhook'. Both charges then are successful. And for both donations, an instance of the Donation model gets created in the database. 

There is one catch: if the user uses a different e-mail address in the donation form, than the one he registered with, then the donation doesn't get created in the database, and an internal server error occurs. This is an unresolved issue. One could argue that since the user signed up with an e-mail address, the user shouldn't have to fill out his e-mail address again on the donation form. But sometimes donations are made with someone else's credit card, under someone else's name, for example by a parent. Then the confirmation e-mail would have to go to the e-mail address of the credit card holder. This is why I chose to not automatically use the users e-mail address as a placeholder, or remove the field altogether. 

**11: Success message after deleting a blog post, comment or thread.**<br>
I tried to display a success message after deleting an item. However, SuccessMessageMixin for DeleteView doesn't work. According to StackOverflow (https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) the reason for this is that SuccessMessageMixin hooks to form_valid, which is not present on DeleteView to push its message to the user. The solution is to write a function for the delete success message, which I did as follows:
```
from django.contrib import messages

class DeleteBlogPostView(AdminRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = "blog/delete_blog_post.html"
    success_message = "Your blog post was deleted successfully"
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBlogPostView, self).delete(request, *args, **kwargs)
```

**12: Slug for profiles**<br>
I decided to use slugs for the URL's of profile pages. A slug gets created based on the username. If I have a user with a username of testuser, then the slug is testuser. This presented the following issue: when a new user signs up that is identical to another users username, except it has a dot in it (or something else that would get removed when creating a slug), like test.user, then based on its unique username, the user would get accepted by Django. But when the slug is created, the dot gets removed, and then the slug is not unique. Testing this gives the following error: "IntegrityError at /accounts/signup/ UNIQUE constraint failed: profiles_profile.slug". Checking in the admin panel, I saw that the user gets created, but the profile doesn't get created. I therefore used uuid to add an id to the slug, if the slug already exists.

**13: Date of birth**<br>
With the help of StackOverflow, I had written a small function to only accept a date of birth in the past:
```
def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth >= datetime.date.today():
            raise forms.ValidationError("Select a date in the past")
        return date_of_birth
```

This worked fine, as long as the date was filled in. When I tried to delete the date of birth from a profile (since the field is optional), Django threw the following error: ">=' not supported between instances of 'NoneType' and 'datetime.date'".
A small if statement in the function resolved the issue:
```
def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth:
            if date_of_birth >= datetime.date.today():
                raise forms.ValidationError("Select a date in the past")
            return date_of_birth
```

## Unresolved issues
**1: Scroll down after user action**<br>
After liking or bookmarking a blog post, the page gets refreshed and the users end up at the top of the page. A success message is visible. I would like for the page to scroll down after liking/bookmarking, to where the like and bookmark icons are. I think I would need Ajax for this functionality, but I don't know much Ajax yet.

**2: Last login**<br>
The last login details on the users profile page only shows the date of actually logging in. A user could stay logged in thanks to the cookie and browse the website a day or many days later. Therefore this does not really represent when the user was last browsing the website.


**3: Sorting threads by activity and blog posts by popularity**<br>
I would like to have had the options to sort threads by activity (most recent comment) and sort blog posts by how popular they are (number of likes). I tried this as follows in the ForumView:
```
allowed_sort_fields = {'date_created': {'default_direction': '-',
                                        'verbose_name': 'Date'},
                        'title': {'default_direction': '',
                                     'verbose_name': 'Title'},
				'comments__date_created': {'default_direction': '',
                                     'verbose_name': Activity'}
                        }
```
The problem was that if the two most recent comments were in the same thread, that that specific thread would be displayed twice on the forum. I need to sort with each threads last comment (only the last!). Something similar happened with blog posts. It should be possible, I just need more time and maybe some advice on how to solve this.

**4: TextField instead of CharField**<br>
In the Thread model, I should have set the description field to be a TextField instead of a CharField. Same goes for the biography field in the Profile model. This would look a lot better on the add and edit thread/profile forms. However, I have already added data to the database, and I'm close to submitting the project, so at this point, I will not change my model. 

## Browsers
The final version of the website was tested in different browsers. The website works correctly in Chrome, Ecosia, Opera, Firefox, Microsoft Edge. I used Broswerstack to test some functionality in Safari, but I did not have enough time and I did not want to use a real login. It seemed to work correctly. And with the CSS code being prefixed, I assume it works correctly.
The website does not work correctly in Internet Explorer.

## Responsiveness
- Whilst building this website, testing to see if the website adjusts itself to the size of the device was mostly done with the Chrome DevTool. Media queries are in place to adapt elements to different screen sizes. 
- At the final stage, the website was tested on my personal devices (Lenovo Ideapad 110, HP Pavilion P6330NL with Lenco Monitor (1920px x 1080px), Huawei P30, Samsung Galaxy S4 mini), and my family's and friends' devices. The website was displayed as intended. 