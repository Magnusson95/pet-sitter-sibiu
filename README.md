# Pet Sitter Sibiu

An eCommerce site for the owner of Pet Sitter Sibiu. The site will be an opportunity for the business owner to present the services available, offer a background to the company and provide customers with the opportunity to pay for these services.

![Image](https://images.unsplash.com/photo-1554080353-a576cf803bda?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2134&q=80)

---

# Contents

1. [UX](#ux)
2. [Features](#Features)
3. [Technologies](#Technologies)
4. [Languages](#Languages)
5. [Libraries](#Libraries)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)

## UX

### User Stories
##### Viewing and Navigation:
- "As a shopper, I want to view a list of products"
- "As a shopper, I want to view products in detail"
- "As a shopper, I want to see what's in my bag quickly"
- "As a shopper, I want to see photos of what Pet Sitter Sibiu does"

##### Registration and User Accounts:
- "As a Site User, I want to create an account"
- "As a Site User, I want to log in and log out"
- "As a Site User, I want to recover forgotten passwords"
- "As a Site User, I want to see a personal profile page"
- "As a Site User, I want to see my old orders"
- "As a Site User, I want to have my billing details populate automatically"
- "As a Site User, I want to be able to give feedback in a review"
- "As a Site User, I want to update my billing details"
- "As an admin, I want users to require an email confirmation to register"

##### Purchasing and Checkout:
- "As a Shopper, I want to pick my service type, animal to be cared for and number of sessions in one quick view"
- "As a Shopper, I want to confirm everything in my bag before checking out"
- "As a Shopper, I want to remove or adjust how many sessions of each item are in my bag"
- "As a Shopper, I want to add my payment information"
- "As a Shopper, I want to have a secure checkout"
- "As a Shopper, I want to get a confirmation of my order"
- "As a Shopper, I want to receive an email with my order for my own records"

##### Admin and Store Management
- "As the store owner, I want to add products"
- "As the store owner, I want to edit products"
- "As the store owner, I want to delete products"
- "As the store owner, I want to add photos to a collage"

### Design Choices

- Pagination style with distinct pages for each section
- A collage showing previous clients.
- A big call to action in the home page taking customers directly to the services offered. This is overlayed on top of a full view animal picture to really give a feel for the outdoor pet services that are provided.
- Browns (#42332C) and Golds (#F2CDB3) were primarily used to give an earthy, outdoor feel.
- Leckerli is used for the logo to give a playful, creative feel.
- Lemonada is the main font family used which is well suited to large font sizes which feature throughout the page and blends well with the laidback style of the website.
- The navbar is hidden away on smaller screens to keep a clean view.

### Wireframes

I used [Framer](https://framer.com/) to create detailed wireframes for each page at a mobile level to keep with the Mobile First design approach. Framer is interactive, allowing me to get a feel for the types of interactions I wanted to provide users.

As is to be expected certain elements present in the wireframes did not make it into the project itself but may yet do so further down the line. For example, the user admin page is all provided in one form, on one page, rather than being paginated - this provides a quicker, easier user experience.

You can find my wireframes [here](https://github.com/Magnusson95/Pet-Sitter-Sibiu/tree/master/wireframes).

## Features

### Existing Features

- **Navbar/Sidenav Links** - The navbar and sidnav links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'About Us', 'Our Services', 'Login' and 'Register' links are shown. When the user is logged in, the 'Home', 'About Us', 'Our Services', 'My Account' (dropping down to 'Product Management' if super user, and 'Profile' and 'Logout') and 'Bag' (with bag subtitle) links are shown.
- **Index Links/Buttons** - The links and buttons on the services page vary depending on whether the user is logged in as a super user or not. If a super user is logged in, the 'Adjust' and 'Delete' links are shown in the Service cards.
- **Checkout Buttons** - The links and buttons on the checkout page vary depending on whether the user is logged in or not. If a user is logged in, they can save the form details to their profile. If they are not logged in they see links to register or log in.
- **Flash Messages** - Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users.
- **Login** - Allows existing users to login to their account. The username field accepts either the username or email address associated with a particular account. I've included authorization checks to verify the username/email address and password against the details stored in the database before users can be logged in.
- **Register** - Allows new users to register for a free account. I've included checks to ensure that the username and email address don't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes. Upon successful registration, users receive an email link that they must click on to confirm registration.
- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Reset Password** - Allows users to reset their password. Upon entering their email address, the user will receive an email containing a link to reset their password. The email link takes the user to a page where they can reset their password, providing the new password meets Django's standard requirements.
- **Profile Page** - When logged in, users can visit their profile page to view a list of their order history, or edit their shipping and billing details.
- **Edit Profile** - In the user's profile page, the 'Edit Profile' button triggers a modal with a form. The form pre-populates the user's details, which they can edit.
- **Previous Orders** - In the user's profile page, the 'Order history' sections displays a list of the user's previous orders. The user can click the order ID to view the full details of that particular order.
- **Services** - All services are displayed in the 'Services' page. Tickets are displayed in ascending order of upload date.
- **Service Preview Cards** - Each preview card shows the relevant service's name and some quick info (price, description, a couple bullet points). Clicking the service card takes the user to that service's page with its full details.
- **Pagination** - The collage page uses pagination. The previous page button is only available if there is a previous page. The next page button is only available if there is a next page.
- **View Service Detail** - Read operation. Displays the services's full details on a page. From here, users can use the form to select animal and quantity to add to their bag.
- **Super User Privileges** - Allows the super user (admin) to edit or delete reviews, services and order history and add photos for the collage.
- **Add Service** - Create operation. Accessible to superusers from their account navbar. All form fields are required. 
- **Adjust Service Button** - The 'Adjust' button is available only if a super user is logged in. Clicking it takes the user to the 'Adjust service' page for that particular service.
- **Adjust Service** - Update operation. Service details are pre-populated in the relevant form fields, which the user is able to edit if required. Upon form submission, the database is updated with the new values.
- **Delete Service Button** - The 'Delete' button is available only if a super user is logged in. Clicking it deletes that particular service from the database.
- **Reviews** - Allows the user to post a review. This form is only available if the user is logged in and is found in their profile page. The form field is required for successful form submission. Upon submission, the user's review is displayed in the 'Testimonials' section on the home page.
- **Cancel Buttons** - Cancels the relevant action and takes the user back to their profile.
- **Custom Success Messages** - I've included custom 200 success messages and handlers to let users know what changes they are making on the site.
- **Custom Error Messages** - I've included custom 404 and 500 error messages and error handlers to catch these errors.

### Features Left to Implement

- **Contact form**
- **Search by service name**
- **Super User Photo Upload Form for Collage**

## Technologies

- [Github](https://github.com/) to host this project's respositories.
- [Gitpod](https://gitpod.io/) IDE of choice for development.
- [Git](https://en.wikipedia.org/wiki/Git) for version control
- [Google Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools) for testing and troubleshooting.
- [Coolors](https://coolors.co/) for colour schemes.
- [AWS S3](https://s3.console.aws.amazon.com/) to host static and media files
- [Heroku](https://www.heroku.com) as the hosting platform to deploy my site.
- [W3C Markup Validation](https://validator.w3.org/) used to validate HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) used to validate CSS.

## Languages

- [**HTML**](https://en.wikipedia.org/wiki/HTML)
    - **HTML**... The building blocks of the pages.
- [**CSS**](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
    - **CSS** is used to style the page, with a base.css applying throughout and individual app css files where required.
- [**Javascript**](https://en.wikipedia.org/wiki/JavaScript) 
    - Project uses **Javascript** to add interactivity, with inline or individual app js files where required.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**Django**](https://www.djangoproject.com/)
    - The project uses **Django** as the Python web framework.
- [**Stripe API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for logging and upvoting Feature Requests. The project uses Stripe's test payment functionality.

## Libraries

- [Font Awesome](https://fontawesome.com/) for icons.
- [Google Fonts](https://fonts.google.com/) used for fonts.
- [jQuery](https://jquery.com/) used for easier integration of Javascript.
- [Bootstrap](https://getbootstrap.com/) for styling.

## Testing

### Internet Browsers

The same process of opening up the live page and meticulously clicking all links, buttons, and re-sizing of windows was utilized in the following browsers:

- Google Chrome - Main browser of choice for development.
- Microsoft Edge – All working as intended besides flex at minimum width
- Mozilla Firefox - No issues. Everything works as intended.
- Safari - All working as intended.

The site has been tested physically on a number of mobile devices including:

- iPhone 5, 7, 10 and 11
- Google Pixel
- Galaxy S9.

Various examples of multiple screen sizes on different pages of the site can be found [here](https://github.com/Magnusson95/Pet-Sitter-Sibiu/tree/master/wireframes)

Javascript tested through user testing during each stage of writting. Including confirmation of API connection, API verification, API customisation and user testing of jQuery with Google Chrome Developer Tools.

Speed was also tested using [Pingdom](https://tools.pingdom.com/#5c7e3a4008c00000) and the site received a performance grade of 80/100

### Automated Testing

Various test files have been added to attempt to pull pages and see if they exist.
Tests run on views to check authentication running correctly when users are logged in (i.e. can see 'my account' links but not 'login' link).
Tests run to create and pull Services from the database.
Tests run to attempt payment statuses.

### Stripe Testing

Stripe payments were attempted with every type of test card from all regions to check zip/postcode field still worked depending on country (as format and requirement changes depending on country). A list of these cards can be found [here](https://stripe.com/docs/testing#international-cards). Every card passed.

### Issues and Resolutions

Webhooks sending 500 response errors due to mismatching of postal code in billing and shipping, reintroduced shipping from the intent during the test to check if order exists in the model.
Webhooks not sending whilst in gitpod due to sharing restrictions in the workspace.

### Known Issues

- All responsiveness working on Microsoft Edge except minimum flex view.

## Deployment

Pet Sitter Sibiu was developed on GitPod, using git and GitHub to host the repository.

**When deploying Pet Sitter Sibiu using GitHub Pages be sure to follow these steps:**

1. Navigate to '/Magnuson95/Pet-Sitter-Sibiu' or alternatively click
2. In the top navigation click on 'settings'.
3. Scroll down to the GitHub Pages area.
4. Select 'Master Branch' from the 'Source' dropdown menu.
5. Click to confirm my selection.
6. Pet Sitter Sibiu should now be live on GitHub Pages.

**In order to run Pet Sitter Sibiu locally be sure to follow these steps whilst still on Github:**

1. Navigate to '/Magnusson95/Pet-Sitter-Sibiu' or alternatively click [here](https://github.com/Magnusson95/Pet-Sitter-Sibiu).
2. Click the green 'Clone or Download' button.
3. Copy the url in the dropdown box.
4. Using your IDE of choice open up your preferred terminal.
5. Navigate to your desired file location.
6. Copy the following code and input it into your terminal to clone Pet Sitter Sibiu.

`git clone https://github.com/Magnusson95/Pet-Sitter-Sibiu.git`

## Credits

### Content

- All content was created by me or Anita (owner of Pet Sitter Sibiu).

### Media

- Collage photos created by Anita.
- Backgrounds and Service photos provided by [Wallhere](https://wallhere.com/).
- Icons provided by [PNG Tree](https://pngtree.com/free-logo-png).