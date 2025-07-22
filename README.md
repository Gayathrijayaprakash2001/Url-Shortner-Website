# Url-Shortner-Website
URL Shortener is a Django-based web application that allows users to register, log in, and manage shortened URLs. It provides a personalized URL shortening service with authentication, search, pagination, and CRUD operations.

✨ Features
●📝 User Registration & Authentication

 ● Users can sign up, log in, and securely manage their own URLs.

➕ Add URLs with Titles

●Logged-in users can add URLs with custom titles.

 ● ⛔ Limit: Each user can add a maximum of 5 URLs. After that, an error message is shown.

●🔗 Automatic URL Shortening

 ● The original URL is automatically shortened and stored in the MySQL database.

●📋 URL Listing with Pagination

Logged-in users can view a paginated list of their URLs showing:

 ● Title

 ● Original URL

 ● Shortened URL

 ● Date & time added

●🔍 Search Functionality

 ● Search by title or original URL to quickly find specific entries.

●✏️ Edit/Delete URLs

 ● Full control to update or remove URLs from your personal list.

●🔓 Logout Option

 ● Users can securely log out at any time.


🛠️ Tech Stack
  ● Backend: Django

  ● Frontend: HTML, CSS

  ● Database: MySQL

  ● Authentication: Django's built-in auth system
