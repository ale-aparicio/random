![Website Mockup](read.me-pictures/website-mockup.jpg)
# Straw Facts 
**Straw Facts** is a community-based website for all One Piece enthusiasts looking to share their thoughts and theories with others.

The inspiration for the website came from the countless theories roaming around the internet in different forums and websites, so the idea is to have a place where fans and speculators can create, find, and share their theories with everyone and have one place to find everything rather than having the information spread across different platforms.

[Live Project Here!](https://straw-facts.herokuapp.com/)

# Table of Contents
1. [UX](#UX)
    1. [Project Goals](#Project-Goals)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
2. [Data Schema](#Data-Schema)
    1. [Users Collection](#Users-Collection)
    2. [Theories Collection](Theories-Collection)

# UX 
## Project Goals

The main goal of **Straw Facts** is to provide the users with an easy and accessible way to create theories by enabling them to **create, edit, and delete** their theories as they please aswell as access other theories shared by other users.

This is the third project of the Milestone Projects that a learning developer must complete durint their Full Stack Web Development Program at **The Code Institute**.

The requirements for this project are to develop a full-stack website allowing users to manage a common database (in this case, One Piece Theories) using **HTML5, CSS, JavaScript, Python, Flask, and MongoDB.**

## User Goals
The users for this site would be looking for:

* An easy-to-use data management to create theories with **CRUD** conventions to:
    * Create a User Account
    * see their created theories
    * Update their theories
    * Delete their theories

* An easy-to-use user management system
    * Create a user account.
    * See their created theories.
    * Edit their created theories.
    * Delete their created theories.

* A easy to navigate and aesthetically apropriate site

## Developer / Site Owner Goals

* The developer is looking to:
    * Create a community-based application that they themselves would use to find, and create theories for their passion for One Piece and it's many mysteries.

    * Demonstrate their knowledge and practical usage of the variety of softwares, languages, databases, and libraries learned throughout the course. 

    * Deploy a project they are proud of and have invested a lot of time and effort on.

# User Stories

## As a General User, I want to:

1. Be able to easily discover theories.

2. Be able to create my own theories and edit them if I feel the need to as we learn of new information and delete the theory all together if it no longer is relevant or has been proven right or wrong.

## As a Non-Registered user, I want to:

1. To be able to browse through the theories freely.

2. To Create an account when the need to create a theory arises.

## As a Registered user, I want to:

1. Log into my account and gain full access to all that the site has to offer

2. Navigate to my user profile and see the theories I have created.

3. Navigate to the create page and add my own theory into the site.

4. Be able to edit and delete my own theories

## As an Administrative Account holder, I want to:

1. Be able to edit and delete any theory as needed

# Development Planes

When thinking of the design and creation process of the web application the developer noticed several requirements for the functionality of the site and how it would meet the demand from the user stories above. To answer that demand he came up with Development Planes:

## 1. Strategy

* Roles:
    * New Users(None-Registered)
    * Returning Users(Registered)

* Demographic:
    * One Piece Enthusiasts
    * Anime Lovers
    * Theory Fans

The website needs to enable the user to:

* Register/Login to an account

* Create a theory
* Edit a theory of their making
* Delete a theory of their making
* Browse and Discover new theories 

* View Theories containint this information:
    * Theory Title
    * Theory Author
    * Theory Content

## 2. Scope

A scope was defined to identify what needed to be done in order to align features with the strategy previously defined. This was broken into two categories:

* Content Requirements 
    * The user will be looking for:
        * Upload their own theories
        * Edit their own theories
        * Delete their own theories
        * Easy Navigation 
        * A suitable theme

* Functionality Requirements
    * The user will be able to:
        * Register/Login to an account
        * Create a theory
        * Edit the theory they created
        * Delete the theory they created
        * Discover New Theories

## 3. Structure

The information architecture was organized in order to ensure that users could navigate through the site with ease and efficiency, with the following results:

The user will start in the home page then have the ability to look at theories form the get go without the need to make an account. When the user decides they want to create a theory they will be required to create an account. Users will also only be able edit and delete their own theories.

## 4. Skeleton

The Wireframe was created in [Figma](figma.com) with the user expirience in mind:

A lot of the content displayed in the wireframe was removed from the final site as the developer made the decision to maximize the navigation and thus improving the user expirience.

Home Page:
![Home Page](read.me-pictures/home-wireframe.png)

Theories Page:
![Theories Page](read.me-pictures/theories-wireframe.png)

Sub Categories Page:
![Sub Theory Page](read.me-pictures/subtheory-wireframe.png)

### Post Wireframe Changes 
While the developer used the wireframe for the main idea, aesthetic, and the desired design, there are several major differences between the mockups and the final application:

* Most notably, the content of the website was greatly reduced to greatly focus on the theory aspect of the page as the developer did not deem the other information displayed as important since it is a theory website and not an information/wiki the desired audience for the application will already have an extensive knowledge on the topic at hand. By cutting that much content the user experience was greatly improved as the theory navigation was made much easier.

* The log in and registration features were added later on as it was clear that users will want to be able to edit and delete their theories and for security reasons it couldn't be accessible to everyone and thus the create an account feature was implemented.

## 5. Surface
* **Color Scheme**
    * The chosen color scheme was specifically chosen to compliment the colors of the Anime.

![Color Scheme](read.me-pictures/color-scheme.png)

* **Typography**
    * The main font chosen is [Piedra](https://fonts.google.com/specimen/Piedra?query=piedra). It has a very old and piraty look to it which is the main theme of One Piece! 

    * The logo uses the [Pirata](https://fonts.google.com/specimen/Pirata+One?query=pirata) font since it's the most Pirate themed font.

* Imagery 
 * The imagery used throught the project was taken from google images mostly as the developer does not own the rights to the One Piece anime. 

[Back to top ⇧](#table-of-contents)

## Data Schema

For this project, [MongoDB](https://www.mongodb.com/) was used to store the datasets. within the created database, the collections can be divided into two types:

### Users Collection 
* When registering an account, the user provides:
    * Username (Unique Identifier)
    * Password (hashed)

### Theories Collections

* When creating a theory the user will have the option to choose what category the theory will go into:
     * World Theories
     * Character Theories
     * Devil Fruit Theories
     * Story Theories
     * Crew Theories
     * Mischellaneous Theories

* All these different categories are their own collections in orde to separate the different theories and not have them all mixed up in one big collection. 

* When creating a theory the user provides: 
    * Category in which they wish their theory be stored
    * A title for their theory
    * The theory itself or as labeled as the content

# Features 
## Design Features
Each page of the website is fully responsive and has an adaptable navbar so it can be utilized to it's full capicity when being viewed from any device.

* At the top of the page there is a navbar which allows acess to all the other pages in the website and it's content changes depending whether the user has created an account or has logged in displaying the Profile and Log Out buttons. 

* The Footer displays the same amount of content with one exception the social links which will take the user to a page related to the topic in the respective social media platform.

* Throught the website the use of the class **box** is utilized to display the orange box that wrappes all the content throught the page to give the page a more vibrant look all throughout.

* The use of Banners is used when navigating throught the theories to give the viewer a feel of what type of content to expect if the category title wasn't enough of a hint.

* Each category has a small thumbnail that reflects on the type of theories that will be found there.

* The sub theory categories each contain their own banner related to the topic they're displaying. Each one consists of a title, a create button that takes the user to the create page and the theories, which are displayed utilizing the above mentioned box to match the theme of the site.

* The create and edit pages both consist of a form wrapped around the **box** class and it contains an input to write the title, and the content of the theory as well as an option tab where the user can choose what category they would like their theory to be in.

## Features to Implement in the Future
* Display Picture
    * Give users the option to inser profile images to better express themselves.

* Image Upload 
    * This feature would be mainly used when writing a theory give the users the ability to insert pictures to better explain their theory and use as examples when making a point.

* Search Bar
    * This feature would be implemented when the number of theories inside of the website starts to impact the navigation of the page if there are too many theories it will become harder to go back and look for old theories a user might've liked

* Comments
    * A big part of sharing theories with a community is to recieve feed back and have a conversation/discussion about the theory and it could be a great user engagement.

[Back to top ⇧](#table-of-contents)

# Issues and Bugs 

## **Commits**
* **Very Important**
    * When reviewing the project with the mentor it was noticed that the commits were saved in an unorthodox way and that caused all of the commit messages to be reassigned to "add".
    The mentor pointed out this error and the rest of the commits where done properly unfortunately this mistake was noticed until the very last meeting where most of the progress was already done and the damage was irreversible.

## Index.html
* The boxes throught the Index page don't match in height depending on the device they're seen on. The developer tried to increase the height of the boxes but it left a huge empty space that took away from the overall look of the page so he opted to leave the boxes so be different heights rather having huge white spaces throught

## Banners 
* Some of the banner displayed in the sub theories are over extended if viewed from big displays as the developer couldn't find theme apropriate images that were the required size and the required resolution. 

[Back to top ⇧](#table-of-contents)

# Technologies Used
## Languages 
* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Tools 
* **Gitpod**
    * Git Pod was used as the preferred IDE.

* [Git Hub](https://github.com/)
    * Git Hub was used to store the project repository.

* [Heroku](https://id.heroku.com/login)
    * Heroku was used to deploy the website

* [Figma](https://www.figma.com/)
    * Used to create the wireframe during the design phase of the project

* [Photoshop](https://www.photoshop.com/en)
    * To edit the website mockup, create the color pallette and edit the favicon.

* [Favicon](https://favicon.io/)
    * Used to create the icon displayed in the tab

* [Font Awesome](https://fontawesome.com/)
    * Used to add the icons used throughout the website


## Libraries
* [Bootstrap](https://getbootstrap.com/)
    * Used as the css framework used to implement the responsiveness of the site.

*


* []()
* []()
* []()
* []()
* []()






