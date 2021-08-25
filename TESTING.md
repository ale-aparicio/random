![Website Mockup](read.me-pictures/website-mockup.jpg)
# Testing
[Return to READ.me](README.md)

[Live Project Here!](https://straw-facts.herokuapp.com/)

[View Repository](https://github.com/ale-aparicio/straw-facts)

## Table Of Contents

1. [Testing User Theories](#Testing-User-Theories)
2. [Manual Testing](#Manual-Testing)
    1. [Common Element Testing](#Common-Element-Testing)
    2. [Page Elements Testing](#Page-Element-Testing)
3. [Automated Testing](#Automated-Testing)
    1. [Code Validation]()
    2. [Browser Validation]()
4. [User Testing](#User-Testing)

# Testing User Stories

User stories were tested to make sure the needs and demands of the user were being met, this is what our testing results: 

## General User

1. **As a General User, I want to discover all sorts of theories.**

    * Theories have been categorized so that the user can easily find the type of theory they're more interested in.

## Non-Registered User
    
1. **As a Non-Registered User, I want to be able to quickly create an account.**

    * A Non-Registered User can click the Sign Up Button to create an account located in both the footer and in the header.

    * Users just need to Create a username of their liking and a password of their liking.

    * Once registered, users will be redirected to their profile page. 

## Registered User 

1. **As a Registered User, I want to log into my account and have full access to all the features the site has to offer.**

    * User can click the Log In button and quickly access their account.

    * Once Logged In Users have full access to all the site's features

    * Users can click on the create button found in either the Header, Footer, or inside every theory category.

    * Users can now create a theory of their choose

    * Users can edit the theories they have created

    * Users can delete the theories they have created

    * User's theories will now display on their profile page if they have created any

## Administrative Account Holder:

1. **As an Admin Account Holder I want to be able to edit, delete any theory**

    * As an Admin I have the ability to bypass the normal user limitations giving me access to edit, and delete all theories if need be.

# Manual Testing
## Common Element Testing 
### Index.html:
Manual testing for the Home Page was conducted in the following manner:

* Clicked the Logo to make sure it redirected me back to the home page.

* Tried the Theories button in the header and footer to make sure it would take me to the theories page to select a category.

* Tried the Create button without being signed in to and it redirected me to the log in screen since you have to be logged in to create a theory. 

* Tried the Log In and Sign Up buttons in the header and footer and both took me to their respective pages

* After Signing in the log in and sign up buttons no longer were displaying and were changed to the profile and log out buttons respectively.

* Checked the Categories linked under the news box to make sure they all redirected me to their appropriate page.

### Theory.html:
Manual testing for the Theory Page was conducted in the following manner:

* Tried all the Categories and to check if they all redirected to the correct pages

### []_theories.html
Manual testing for the Sub Theories Pages were conducted in the following manner:

* Clicked on all the theories made sure they were all display the correct information

* Create button only works if the user is signed in

* Delete and Edit buttons only display for the user who created the theory and they both work as intended

### add_theory.html

* Theory adds with the correct information to the correct category.

### edit_theory.html

* All changes are updated into the database.

# Automated Testing

* The Html was run through the [W3C Validator](https://validator.w3.org/) and all errors marked were solved

* The CSS was tested through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and all errors marked were solved.

* My Python code was tested through [PEP8 Online](https://jigsaw.w3.org/css-validator/) and all the errors and warnings were solved.

# Browser Validator

* The Website was tested on the following browers and worked flawlessly:

Safari

Mozilla Firefox

Google Chrome

Internet Explorer

# User Testing

* Friends and family members all reviewed the website and pointed out spelling mistakes, bugs, and errors that they expiriencing.

* All errors and complaints have been solved.