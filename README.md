PERSONAL SITE


All listings and news objects are added through an admin panel and display dinamycally.
The admin panel includes several options when adding a new object such as Featured. 
If an object is checked as featured it will be displayed on the home page.

The contact page sends an email with the information provided after validating the form.
In addition, a new Contact object is created with the same data and a "complete" uncheck field. This
helps to monitor what inquiries have been adressed.

The media files uploaded from the admin panel are hosted using Amazon S3 buckets.

The site is hosted in heroku using the free tier service and periodically goes to sleep.
This, unfortunately, causes the app to reset. I have an app pinging the site every 30min
but their policy forces to app to go to sleep after 6 six hours. I will try to keep it as
updated as possible.
