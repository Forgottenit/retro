# Retro

## About Site

Click here to view [Retro](https://forgottenit-retro.herokuapp.com/) (CTRL + Click to open in a new browser tab).

<img src="amiresponsive.png">


# UX - User Experience

## User Stories

<details>
<summary><b>Site User</b></summary>

1. As a site user, I want to be able to browse through various records and CDs so that I can decide what to purchase.

2. As a site user, I want to be able to filter and sort my search results so that I can find specific items easily.

3. As a site user, I want to be able to add records to a wishlist or favorites list, so that I can remember them for later.

4. As a site user, I want to be able to add items to a shopping cart, so that I can purchase multiple items at once.

5. As a site user, I want to be able to view my shopping cart and make adjustments (add/remove items, change quantities), so that I have control over what I'm purchasing.

6. As a site user, I want to be able to securely checkout using Stripe, so that I can easily and safely make a purchase.

7. As a site user, I want to be able to create an account, so that I can save my shipping information and preferences.

8. As a site user, I want to be able to subscribe to a newsletter, so that I can receive updates and special offers.

9. As a site user, I want to be able to follow the site on social media, so that I can follow updates and special offers.

10. As a site user, I want the site to ensure data security, so that my information is kept safe.


</details>

<details>
<summary><b>Site Admin</b></summary>

1. As a site admin, I want to be able to manage user accounts so that I can handle any issues that arise.

2. As a site admin, I want to be able to view and manage all orders, so that I can check if operations are functioning correctly.

3. As a site admin, I want to be able to assist users with their accounts, so that they can have the best experience possible.

4. As a site admin, I want to be able to update the site's content, such as sales, new items and announcements, so that users are kept informed.

5. As a site admin, I want to be able to handle security threats and issues, to ensure the website and user data are safe.

6. As a site admin, I want to manage the inventory, so that I can create new items, edit existing ones, or delete out-of-stock items from the site.

7. As a site admin, I want to manage inventory, so that I can track stock levels and add items before they run out.

8. As a site admin, I want to track the website performance, so that I can monitor page load times and analytics to ensure a good user experience.

9. As a site admin, I want to access sales data, so that I can analyze trends, identify popular or unpopular items, and plan future inventory purchases or sales.

10. As a Site Admin, I want to manage user accounts and access control, so that I can ensure the security and integrity of the site.

</details>

<details>
<summary><b>Site Owner</b></summary>

1. As a site owner, I want to be able to track sales and inventory on my B2C e-commerce site, so that I can manage my business.

2. As a site owner, I want to be able to add or remove items from the store so that I can update my products.

3. As a site owner, I want to be able to adjust prices and add sales promotions so that I can attract more customers, encourage repeat purchases or sell unsold stock.

4. As a site owner, I want to be able to view user behavior data, so that I can improve the user experience and make informed business decisions.

5. As a site owner, I want to be able to send newsletters to subscribers, so that I can keep them engaged and informed about new products or promotions and updates to create an ongoing relationship with them.

6. As a site owner, I want to have a system that alerts me when my stock is running low or completely sold so that I can order more stock in time.

7. As a Site Owner, I want to provide a secure login functionality, so that users can access their accounts and engage with the site.
</details>

<details>
<summary><b>Site Marketer</b></summary>

1. As a marketing specialist, I want to create engaging content for a Facebook page to generate interest, potential sales and boost our social media presence.

2. As a marketing specialist, I want to create and send newsletters to subscribers, to inform them about new products, promotions, and other relevant updates and to encourage client retention.

3. As a marketing specialist, I want to maintain a current and optimized sitemap.xml file, to improve the website visibility and indexing on search engines as part of our SEO strategy.

4. As a marketing specialist, I want to maintain a correctly configured robots.txt file, to guide which parts of the site to crawl or not and improve our SEO performance.

5. As a marketing specialist, I want to perform keyword research and SEO analysis to improve the site's visibility on search engines.

6. As a marketing specialist, I want to monitor the website performance on search engines, to identify opportunities for improvement.

7. As a marketing specialist, I want to analyze website traffic and user behavior, to make data-driven decisions about site improvements and marketing strategies.

8. As a marketing specialist, I want to make sure each webpage has a clear and compelling description (optimizing meta tags) so that when people see our site in search results, it will be appealing to them.

9. As a marketing specialist, I want to set up the right labels for links going to other sites (implement rel attributes for external links), so that search engines can understand our site better and it doesn't negatively affect our visibility in search results.
</details>
<br>

# Methodology

<details><summary><b>Agile Methodology</b></summary>

 

Creating an e-commerce website involves many different parts and can is a complex process. A system is required to manage and visualize the workflow, to deliver a successful project.

A Kanban board has been created on GitHub Projects to streamline the development process. GitHub Projects is a tool for developers to create a task management and progress visualization system, linked to a repository. It's an excellent way to maintain oversight of the entire project, track the status of various tasks and issues, and manage time effectively.

In this project, the Kanban board has been split into different columns: "Could Have", User Stories", "Todo", "In Progress", "Verify", and "Done". These headings represent different stages of the workflow.

- "Could Have": This column represents Issues or Tasks that could enhance the site but are not required and are to be worked on only once the site is complete, User Stories have been met and testing and documentation is finished. 

- "User Stories": This column represents features or functionalities that are required, broken down into tasks.  The User Stories are broken down into "Site User", "Site Admin", "Site Owner" and "Site Marketer". These are a checklist to ensure all the stakeholder needs are met. These are later broken down as required, into issues and tasks. 

- "Todo": This column includes tasks that need to be completed. Once a new task has been identified, it's added to this list.

- "In Progress": When work begins on a task, it's moved into this column and given a "Milestone" date for completion. This is to ensure optimal time management is used. 

- "Verify": Once a task is complete, it's moved here for testing and review as required. 

- "Done": After a task has been reviewed and no further changes are required, it's moved to the "Done" column.

Each task is labeled with a specific category like 'html', 'javascript', 'styling', 'authentication', 'bug', etc., to identify the nature of the work. Labels such as 'Must Have', 'Should Have', 'Could Have', and 'Won't Fix' are applied to tasks as required, based on the MoSCoW method. This method is used in project management to prioritize work items.

- 'Must Have': These items are essential for the project and must be included.
- 'Should Have': Important items but not critical.
- 'Could Have': Desirable items but not necessary. They are included if time allows.
- 'Won't Fix': Issues that are known to not be included in the final project, whether due to resources or time constraints. These could be included in a future iteration.

An example of the issues created:

'INITIAL SETUP'. The issue details the task: "As a Site Admin, I can display my music site so that customers can view it". This task outlines the acceptance criteria and related tasks, including creating basic HTML for the website, linking Bootstrap, creating a landing page, and more.

Using this workflow and labeling system provides many benefits. It allows for effective time management, facilitates a smooth workflow, enables easy identification of requirements and offers clarity on the task or issue status.

It follows an agile development approach offering a good foundation for organizing, prioritizing, and managing project tasks which, in turn, leads to a more efficient and successful project.

The [Kanban Board](https://github.com/users/Forgottenit/projects/4) can be found here.



<img src="kanban-board.png">
</details>

<details><summary><b>Business Methodology</b></summary>


For the creation of this e-commerce website, the methodology adopted revolves around a Business-to-Consumer (B2C) approach. The decision to use a B2C model is primarily due to the nature of the service the site provides - selling records and CDs directly to individual customers.

Using a B2C approach provides several distinct advantages:

Direct Interaction with Customers: Unlike B2B, B2C allows for direct interaction with the end-user. This interaction provides invaluable insights into customer behavior, preferences, and feedback, informing product development, marketing strategies, and overall business direction.

Greater Market Potential: B2C markets typically have a larger base of potential customers compared to B2B. This can lead to higher sales volumes and, potentially, higher revenue.

Brand Building: B2C marketing allows for direct brand-consumer relationships, providing opportunities to build brand loyalty and recognition among end consumers.

The user stories were carefully crafted to align with this B2C methodology, focusing on a user-friendly experience for individual consumers:

Users can easily browse through various records and CDs, filter and sort results, and add items to a wishlist or shopping cart, offering a seamless shopping experience.
The site provides a secure checkout process, fostering trust and encouraging repeat purchases.
Users can create an account to save their shipping information and preferences, increasing convenience for repeat customers.
The option to subscribe to a newsletter and follow the site on social media enables the business to maintain ongoing engagement with customers.
The Site Admin and Site Owner user stories focus on managing user accounts, orders, and inventory, ensuring a smooth operational process to maintain a positive user experience.

From a business perspective, this B2C approach and the corresponding user stories offer several benefits:

Improved Customer Understanding: Direct interactions with customers through a B2C model provide a deeper understanding of their needs and behaviors, which can inform business strategies.

Increased Sales Opportunities: By making the shopping process as seamless and user-friendly as possible, customers are more likely to make purchases, potentially boosting sales.

Customer Retention: Providing secure, convenient features like saved shipping information and account creation can increase customer retention.

Marketing Opportunities: The ability to engage with customers through newsletters and social media presents numerous opportunities for marketing, promotions, and building customer relationships.

Overall, using a B2C approach for this e-commerce site can facilitate a direct, beneficial relationship with customers, potentially leading to increased sales, customer loyalty, and business growth.
</details>

<details><summary><b>Marketing Methodology</b></summary>


The marketing methodology for this e-commerce site is designed to effectively reach and engage its target audience of individual customers, aligning with the overall Business-to-Consumer (B2C) approach.

Key aspects of this methodology include:

Search Engine Optimization (SEO): The site is optimized for visibility on search engines, using tools like sitemap.xml and robots.txt files, meta tag optimization, proper use of rel attributes for external links, and ongoing SEO analysis.

Social Media Engagement: A Facebook page for the site is maintained to reach potential customers where they already spend their time online, keeping them engaged with regular, relevant content.

Email Marketing: Customers are encouraged to sign up for a newsletter, through which they can receive regular updates about new products, promotions, and other news.

Data-Driven Decision Making: Website traffic and user behavior are monitored and analyzed to understand what works and what doesn't in terms of site functionality and marketing strategies.

The benefits of this marketing methodology in a B2C context include:

Increased Visibility: By ensuring the site is easily discoverable via search engines, the likelihood of attracting new customers is significantly increased.

Customer Engagement: Engaging with customers through social media and email newsletters allows for regular communication, building relationships, and keeping the business top-of-mind.

Personalization: Gathering and analyzing data about user behavior allows for more personalized marketing, which can increase engagement and conversion rates.

Informed Decision Making: The use of data-driven decision making enables the site owner to make informed choices about site improvements, inventory management, and marketing strategies.

In summary, the marketing methodology complements the B2C approach by focusing on reaching and engaging individual consumers through multiple channels, ultimately aiming to drive traffic, increase conversions, and build customer loyalty.
</details>
<br> 


# Design and Development

The development process integrates robust User Experience (UX) principles with reliable back-end technologies.

The site is developed using [Django](https://www.djangoproject.com/) for the back-end, [Bootstrap](https://getbootstrap.com/) for the front-end, and is hosted on [Heroku](https://heroku.com/). [Bootstrap](https://getbootstrap.com/), a powerful, mobile-first, front-end framework, is used for creating the site's responsive and appealing design. It offers a variety of pre-designed components that ensure consistency across the site while speeding up the development process.

Wireframes were utilized to ensure a clear, logical structure for each page, enhancing usability. The color scheme and typography, chosen deliberately, create a visually pleasing and consistent aesthetic across the site, reinforcing brand identity and promoting a positive user experience.

Responsive design has been implemented, making the site easily accessible and functional across a variety of devices, including desktop, tablet, and mobile. This expands the site's reach and ensures a positive user experience regardless of how users access the site.

In terms of security, the site utilizes [Django](https://www.djangoproject.com/) AllAuth for user authentication and authorization, providing an extra layer of protection. Django AllAuth is a trusted, comprehensive authentication solution that enables secure user sign-ups, logins, and password resets.

The site also employs defensive design principles, including form validation and error handling, to guide users through the site and prevent misuse. User input fields are validated both client-side and server-side to prevent malicious or incorrect data from being submitted. Clear error messages guide the users to correct their mistakes.

[Stripe](https://stripe.com/ie), incorporated for payment processing, encrypts sensitive payment information to offer a secure and trusted online payment solution for customers. Stripe's security protocols protect sensitive payment information, maintaining trust and ensuring compliance with financial regulations.

All Sensitive site and user data are further protected through the use of environment variables, which keep key pieces of information out of the site's code and thus inaccessible. The site's server configuration on [Heroku](https://heroku.com/) also employs config vars to further enhance data security.

Data protection is a priority, and the site adheres to the General Data Protection Regulation [GDPR](https://gdpr.eu/privacy-notice/) standards. Measures are in place to inform users about how their data will be used and protected, ensuring transparency and building user trust.

By integrating solid design principles with robust security measures and responsive design, the site delivers an e-commerce platform that is secure, visually pleasing, easy to navigate, and accessible across multiple devices. This fosters customer engagement and supports the success of the business.

</details>

## UX/UI Design
<details>
<summary><b>Wireframes</b></summary>

Wireframes were created using [Balsamiq](https://balsamiq.com/)  

The design, layout, and functionality of the site have been inspired by successful e-commerce platforms such as [The Record Hub](https://therecordhub.com), [Golden Discs](https://goldendiscs.ie), [Vinyl8](https://www.vinyl8.com), and [Music Zone](https://musiczone.ie/shop). These sites were singled out for their modern, user-friendly design, easy navigation, and their efficient approach to displaying a vast amount of product information.




<details>
  <summary>Home Page</summary>
  
  <img src="home-page.png" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>
</details>
<details>
<summary><b>Colours</b></summary>


[Coolors](https://coolors.co) 

Coolors was used to generate a colour palette that is aesthetically pleasing and provides a high level of contrast for readability. The main colours used in the site are:

#FFFFFF White, used for the background colour
#FEFEFE, used for secondary elements
<img src="colours.png" width=600>
</details>
<details>
<summary><b>Typography</b></summary>
The primary font used on the site is sourced from Google Fonts. A Sans-serif font is used as a backup to ensure that the site remains legible and visually consistent on all platforms.

<img src="fonts.png" width=200>
</details>
<br>

## Database Design

<details><summary><b>Entity Relationship Diagram</b></summary>
The database structure was visualized using an Entity Relationship Diagram (ERD) made using [Figma](https://www.figma.com/). This helped to understand and implement relationships between different entities in the database effectively.




<img src="erd.png">
</details>

## Security Features and Defensive Design

<details><summary><b>User Authentication</b></summary>
User authentication is managed by Django's built-in user authentication system, with Django-AllAuth added for handling user signup, login, and password reset functionality.

</details>
<details><summary><b>User Authorisation</b></summary>
Django's built-in user authorization features are used to control access to certain areas of the site depending on the user's role and logged-in status.
</details>
<details><summary><b>Form Validation</b></summary>
Form validation is performed using Django's built-in form validation features, ensuring that all user input is correctly formatted before being processed.
</details>
<details><summary><b>Security-Sensitive Information</b></summary>
All sensitive information, such as API keys and database connection strings, is stored in environment variables, which are not included in the source code. This is managed using Django's built-in environment variable handling features and the Heroku platform's config vars feature.
</details>
<details><summary><b>Payments</b></summary>
All payment processing is handled using the [Stripe](https://stripe.com) payment platform, ensuring that all financial transactions are secure and reliable.
</details>
<details>
<summary><b>Disclaimer and Privacy Policy</b></summary>
The site includes a standard disclaimer and privacy policy, in line with best practices for ecommerce sites. GDPR considerations are taken into account in the design of the site and the handling of user data, following the guidance provided by [GDPR.eu](https://gdpr.eu/privacy-notice/).
</details>
<details><summary><b>Images and Media</b></summary>
All images and other media files are stored and served using the [Cloudinary](https://cloudinary.com/) platform, ensuring high performance and reliability.
</details>
<details><summary><b>Front-End Framework</b></summary>
The site uses the [Bootstrap](https://getbootstrap.com/) front-end framework to ensure a responsive and modern user interface. Bootstrap's grid system is used to ensure that the site displays correctly on all screen sizes.
</details>

# Features
## Existing Features
### Browser Tabs
favicon 
favicon  generated from  [RealFaviconGenerator](https://realfavicongenerator.net/). 

<img src="" width=800>

### Logo
The logo using [Wix](https://www.wix.com/). 
<img src="logo.png" width=200>

### Navigation Bar



<img src="" width=800>


* Home - Available to all 
* Sign Up - Available not logged in
* Log In - Available not logged in
* Log Out - Available logged in
* 

Small screens

<img src="" width=380>



### Footer
links to Facebook, Twitter, Instagram
Clicking on any of these icons opens a new browser tab so that users navigate back easily.

<img src="" width=500>


### Sign Up Page

<img src="" width=800>



### Log In Page

<img src="" width=800>



### Log Out Page

<img src="" width=800>


### Home Page

<img src="" width=800>



<img src="" width=800>

### 

<img src="" width=800>



<img src="" width=800>



### 



#### Section

<img src="" width=800>



<img src="" width=350>



<img src="" width=350>



<img src="" width=350>



### Warning messages


### 

### Modal



### Error Pages 400 403 404 500
Custom HTML pages for HTTP 400, 403, 404 and 500 errors. 


## Features Left to Implement

While regular software updates and patches are not a part of this project's scope, they would be crucial in a real-world setting to keep the site's software secure and protect against new vulnerabilities.

# Technologies Used

## Languages
* [HTML]() 
* [CSS]() .
* [Python](https://www.python.org/) 
* [JavaScript]() 

## Frameworks, Libraries and Tools Used within the Application
* [Django](https://www.djangoproject.com/) 
* [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) 
* [Wix](https://www.wix.com/) 
* [RealFaviconGenerator](https://realfavicongenerator.net/) 
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://jquery.com/) 
* [ElephantSQL](https://www.elephantsql.com/) 
* [Cloudinary](https://cloudinary.com/) 
* [Git](https://git-scm.com/) 
* [GitHub](https://github.com/) was used to 
* [Gitpod](https://www.gitpod.io/) was used to 
* [Heroku](https://id.heroku.com/login) was used to 
* [Google Fonts](https://fonts.google.com/) was used
* [Font Awesome](https://fontawesome.com/) was used 
* [JSON Formatter](https://jsonformatter.curiousconcept.com/#) was used to format JSON files
* [Black](https://pypi.org/project/black/) was used as a Python formatter

## Other Online Tools used
* [Balsamiq](https://balsamiq.com/) wireframes 
* [Figma](https://www.figma.com/) database image
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) screen sizes/ social login ???.
* [Wave Web Accessibility Evaluation Tools](https://wave.webaim.org/)  test accessiblity.
* [Coolors](https://coolors.co)  colours
* [Remove Background](https://www.remove.bg/) background from the logos.
* [Am I Responsive](https://ui.dev/amiresponsive) was used 
* [Compressor.io](https://compressor.io/) compress the images used in the application and README.
* [Grammarly](https://app.grammarly.com/)  grammatical 

## Validators
* [W3C HTML Validator](https://validator.w3.org/) used to validate HTML codes.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)used to validate CSS codes.
* [JSHint](https://jshint.com/) was used to validate JavaScript codes.
* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate Python codes.

<br>

# Testing


<details><summary><b>BUGS/ERRORS:</b></summary>

### Commited Development Database to GitHub

During the development process, the development databse was accidentally commited to GitHub, this was due to db.sqlite3 being in the GitIgnore, as opposed to *.sqlite3. As the project was still in the development process, and all keys had been stored in env.py, which was in the gitignore, the risk of personal or sensitive data being available was not as high as it could have been. But still a possibly large issue. To rectify this, the following steps were taken. 

- 

# https://codepen.io/corenominal/pen/rxOmMJ
# https://djecrety.ir/
CHANGED DJANGO KEY ALSO IN HEROKU, DELETED ALL USERS, CREATED NEW SUPERUSERS, ALL KEYS WERE STORED IN ENV.PY WHICH WAS IN GITIGNORE
# Git rm -r --cached db.sqlite3


### Failed to build backports.zoneinfo
* Problem: Apparent version incompatibility between Python 3.11 and backports.zoneinfo
* Issue: Can not deploy on Heroku
* Fix: In requirements, change:
 ```python 
 backports.zoneinfo==0.2.1
 ``` 
 to 
```python 
 backports.zoneinfo;python_version<"3.9"
``` 

###  ALLOWED_HOSTS = ["forgottenit-retro.herokuapp.com", "localhost", ".gitpod.io"]
* Problem: Page not rendering ("DisallowedHost"), I needed to add the site ('8000-forgottenit-retro-s9wz1pwll0t.ws-eu100.gitpod.io') to allowed hosts.
* Issue: The site '8000-forgottenit-retro-s9wz1pwll0t.ws-eu100.gitpod.io' at the ws-eu100 section increments over time (i.e. "ws-eu99" then "ws-eu100" etc.). So adding it only temporarily fixed the issue. i.e.
```python
ALLOWED_HOSTS = [
    "forgottenit-retro.herokuapp.com",
    "localhost",
    "8000-forgottenit-retro-s9wz1pwll0t.ws-eu100.gitpod.io",
]

```
- "8000-forgottenit-retro-s9wz1pwll0t.ws-eu100.gitpod.io" would have to be changed regularly. This was just an issue in Development (as it wouldn't affect the Production site on Heroku) but it was still an issue.
* I had thought having "localhost" would suffice but it did not. I tried using "*.gitpod.io" and "*.*.gitpod.io" but they didn't work, finally I tried just ".gitpod.io" and that worked.

```python
ALLOWED_HOSTS = [
    "forgottenit-retro.herokuapp.com",
    "localhost",
    ".gitpod.io",
]

```
### SEARCH Queries
* Problem: Couldn't filter by Genre for Albums
* Solution:
 - The issue related to Case Sensitivity of the filtering, as the genres are stored as lowercase letters, the filter search wasn't taking this into account, this was solved by:
```python
  albums.filter(genres__name__icontains=genre_query)
```
 - This lead to another issue as some artists have multiple keywords in their genres that are duplicated, i.e. Folk Rock, Rock, Country Rock etc for the same album, so "Rock" as a Genre filter would display the same album multiple times, this was overcome by using:
```python
  albums.filter(genres__name__icontains=genre_query).distinct()
```
 .distinct() leading to the album being displayed just once.  

 * Follow Up: A further Bug arose due to an Album having multiple Artists, so the Album displayed multiple times, once for each artist, for the same filter. So .distinct() was removed and as each album has a unique Album Id, a set was created, so that the album would only display once. 

 Also, for **pagination**, this proved difficult, as when a genre returned multiple pages, the pararmeters were lost when the next page was clicked, leading to all Albums being displayed. To overcome this 

 - First create a modifiable copy of the GET parameters: params = request.GET.copy(). request.GET contains all of the parameters passed in the URL, but it's an immutable object, meaning you cannot modify it. Therefore, a copy is made, which is mutable and can be modified.
 - Remove the 'page' parameter: page_number = params.pop("page", None). The pop() function removes the specified key ('page') from the dictionary and returns its value. If the key is not found, it returns the default value specified (None in this case). This is done because the 'page' parameter doesn't need to be included in the filter search parameters.
 - Turn parameters into URL format: params_str = params.urlencode(). This prepares filters to be put in the URL. URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits, making them safe for transmission over the internet.
 - Pagination: paginator = Paginator(albums, 18) creates a Paginator object. The Paginator takes two arguments: the list of items to be paginated (albums in this case), and the number of items to be displayed per page (18 in this case). page_number = request.GET.get("page") gets the current page number from the GET parameters. albums = paginator.get_page(page_number) gets the specific page of albums.
 - Pass to template: params_str is sent to the template. It's added to pagination URLs to keep filters when changing pages.


- ### Required CSRF_TRUSTED_ORIGINS for Django 4.2
* Problem: Page not rendering CSRF verification failed.
* Using:

```python
 Django==4.2.2
```

* Solution: [DJANGO](https://docs.djangoproject.com/en/4.2/ref/settings/)
 - "A list of trusted origins for unsafe requests (e.g. POST)."

```python
CSRF_TRUSTED_ORIGINS = [
    "https://forgottenit-retro.herokuapp.com",
    "https://localhost",
    "https://8000-forgottenit-retro-s9wz1pwll0t.ws-eu100.gitpod.io",
    "https://.gitpod.io",
]
```

Added CSRF_TRUSTED_ORIGINS to settings.py, NB: "https://" is required, unlike ALLOWED_HOSTS. 

* ### Crispy forms
* Problem: Submit button not working on login templates when using Crispy Forms
 - First I tried Stack Overflow, a possible solution to the issue was to use a context processor ("accounts.context_processors.login_ctx.login_form_ctx"), [Stack Overflow](https://stackoverflow.com/questions/39197723/how-to-move-singup-signin-templates-into-dropdown-menu/39235634#39235634). This did not work for me.
 - Next, I rendered the form using {{ form }} (the form submitted with this render) and compared the elements using "Inspect" in Chrome to the {% crispy form %} and noticed that when using Crispy forms as {% crispy form %} in the HTML the "submit" button was rendered outside the form. I copied the submit element into the form and it worked. Unfortunately, I was unable to ascertain why this was the case. I am using:
 ```python
 Django==4.2.2
 django-allauth==0.54.0
 django-crispy-forms==2.0
 ```
- I found a solution at [Stack Overflow](https://stackoverflow.com/questions/30355040/submit-button-no-longer-works-with-django-crispy-forms). By simply using the crispy filter {{ form|crispy }} the form was then rendered correctly. 
</details>

<details><summary><b>Testing:</b></summary>

```python
From: webmaster@localhost
To: forgottenit2@gmail.com
Date: Tue, 20 Jun 2023 15:26:31 -0000
Message-ID: <168727479171.4895.12410208213484624068@localhost>

Hello from Retro!

You are receiving this e-mail because you or someone else tried to signup for an
account using e-mail address:

forgottenit2@gmail.com

However, an account using that e-mail address already exists.  In case you have
forgotten about this, please use the password forgotten procedure to recover
your account:

http://8000-forgottenit-retro-s9wz1pwll0t.xxx.gitpod.io/xxx/xxx/xxx/


```

</details>
<br>

# Deployment
The live deployed application - [Retro](https://forgottenit-retro.herokuapp.com/) (CTRL + Click to open in a new browser tab).

<details><summary><b>Initial Setup and Deployment</b></summary>


1. **Create a New GitHub Repository**
    - Navigate to the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template).
    - Click on the "Use this template" button.
    - Give your repository a name and click "Create repository from template."
    
2. **Open GitPod Workspace**
    - Navigate to your new GitHub repository.
    - Click on the GitPod button to start a new GitPod workspace. 

3. **Install Django and Supporting Libraries**
    - In your GitPod terminal, type `pip3 install django gunicorn` to install Django and Gunicorn.
    - To help Django work with PostgreSQL (used by Heroku for databases), install `dj-database-url` and `psycopg2` by entering `pip3 install dj_database_url psycopg2` in the terminal.
    - Cloudinary [Cloudinary](https://cloudinary.com/about) is a cloud service that stores a web application's image management. To add it, enter `pip3 install dj3-cloudinary-storage` in the terminal.

4. **Create a requirements.txt File**
    - In your terminal, type `pip3 freeze > requirements.txt` to generate a list of your project's dependencies. This will be used by Heroku to identify what Python packages are required to run your project.

5. **Create a New Django Project**
    - In your terminal, type `django-admin startproject 'project_name' .` Replace "project_name" with your chosen name for the project.
    - The `.` at the end is important as it sets the current directory (the workspace root) as the place to create the new Django project.

6. **Create a New Django App**
    - In your terminal, type `python3 manage.py startapp 'app_name'` to create a new app within your Django project. Replace "app_name" with your chosen name for the app.

7. **Register the New Django App**
    - Open the `settings.py` file located inside your Django project's directory.
    - Scroll down to the `INSTALLED_APPS` section and add your app's name at the bottom. Your `INSTALLED_APPS` should now look something like this:
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        'app_name',  # Replace "app_name" with the name of your app
    ]
    ```
    - Save the `settings.py` file. Django now knows about your new app and will include it in its operations.

8. **Apply Database Migrations**
    - Django comes with a built-in database abstraction layer that allows you to create your database schema based on your data models. To apply these migrations, in the terminal, type `python3 manage.py migrate`.
    - This command will apply all pending migrations to your database, effectively syncing your database schema with your current Django project's data models.

9. **Start the Django Development Server**
    - Finally, to verify that everything is set up correctly, let's start the Django development server. In the terminal, type `python3 manage.py runserver`.
    - Visit the provided localhost URL in the browser. If everything is set up correctly, you should see the Django welcome screen.
10. **Create a Heroku App**
    - Navigate to the [Heroku](https://dashboard.heroku.com/login) website. 
    - Once logged in, click on the "New" button on the top right corner, and then click "Create new app."
    - Enter a unique name for your app, select your nearest region and then click "Create App."
    - [Retro](https://forgottenit-retro.herokuapp.com/) is available by clicking this link.

11. **Create an ElephantSQL Database**
    - Go to the [ElephantSQL](https://www.elephantsql.com/) website and create an account if you haven't done so.
    - After logging in, click on "Create New Instance" on the dashboard.
    - Enter a name for your instance, select the "Tiny Turtle" free plan, and click "Select Region."
    - Choose the region closest to you and click "Review."
    - Confirm the details and click "Create instance."
    - You'll be directed to your instance's dashboard. Under the "Details" tab, find the "URL" section and click the copy button. You'll need this URL in the next step.

12. **Create an env.py File**
    - In your terminal, type `touch env.py` to create a new file named env.py in your root directory.
    - Open the env.py file and add the following lines of code:
    ```python
    import os
    os.environ["DATABASE_URL"] = "your_database_url"  # replace "your_database_url" with the URL you copied from ElephantSQL
    os.environ["SECRET_KEY"] = "your_secret_key"  # replace "your_secret_key" with your Django project's secret key
    ```
    - Save the file and make sure it's included in your .gitignore file to prevent it from being pushed to your GitHub repository.

13. **Add SQLite Database to .gitignore File**
    - Open your .gitignore file and add the following line of code:
    ```python
    *.sqlite3
    ```
    - This prevents any SQLite database from being pushed to your GitHub repository. Sqlite3 is used in the development stage, ElephantSql will be used for production.

14. **Modify settings.py File**
    - In your settings.py file, import the necessary libraries and environment variables at the top of the file:
    ```python
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
        import env
    ```
    - Replace the Django-provided secret key with your secret key environment variable:
    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ```
    - Comment out the original DATABASES variable and replace it with the following:
    ```python
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    ```
    - These changes set up your Django project to use the ElephantSQL database. This is for production with Heroku deployment, sqlite3 is used in the development stage. 
  
15. **Migrate Database Structure to ElephantSQL Database**
    - To create the necessary tables in your ElephantSQL database, run the following command in your terminal:
    ```python
    python manage.py migrate
    ```
    - You can verify this by going to your ElephantSQL instance's dashboard and checking the "Browser" tab.

16. **Push Changes to GitHub**
    - To save your changes to your GitHub repository, run the following commands in your terminal:
    ```python
    git add .
    git commit -m "your_commit_message"  # replace "your_commit_message" with a short description of your changes
    git push
    ```
    - Now your changes are saved on GitHub.

17. **Set Up Cloudinary**
    - Visit the [Cloudinary](https://cloudinary.com/) website and create an account if you don't have one already.
    - From your Dashboard, you'll see your Cloudinary API environment variable. Click to copy it.
    - Open your env.py file and add the following line of code:
    ```python
    os.environ["CLOUDINARY_URL"] = "your_cloudinary_url"  # replace "your_cloudinary_url" with the URL you copied from Cloudinary
    ```
    - Save the file. This will allow your Django project to connect to your Cloudinary storage.

18. **Set Up Heroku Config Vars**
    - Go to the dashboard of your Heroku app, and navigate to the "Settings" tab.
    - Scroll down to the "Config Vars" section and click on the "Reveal Config Vars" button.
    - Enter the following key-value pairs:
      - Key: `DATABASE_URL`, Value: your ElephantSQL URL
      - Key: `SECRET_KEY`, Value: your Django secret key
      - Key: `PORT`, Value: `8000`
      - Key: `CLOUDINARY_URL`, Value: your Cloudinary URL
      - Key: `DISABLE_COLLECTSTATIC`, Value: `1`  (This is temporary and will be removed when deploying the full project. It is to prevent Heroku from collecting static files, which it does by default)
    - These Config Vars will allow Heroku to properly deploy your Django project.

19. **Update settings.py**
    - Open your settings.py file and add the following lines of code:
    ```python
    INSTALLED_APPS = [
        ...
        ...
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
        'your_app_name',  # replace "your_app_name" with your Django app's name
    ]
    ```
    - Add the following lines of code to tell Django that you're using Cloudinary to store media and static files for cloud-based image handling.:
    ```python
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```
    - Also, tell Django where your templates are stored by adding the following lines of code:
    ```python
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            'APP_DIRS': True,
            ...
        },
    ]
    ```
    - Lastly, add the following line of code to allow connections from your Heroku app and your local machine:
    ```python
    ALLOWED_HOSTS = ['your_heroku_app_name.herokuapp.com', 'localhost']  # replace "your_heroku_app_name" with your Heroku app's name

    #required CSRF_TRUSTED_ORIGINS for Django 4.2, https:// is required
    CSRF_TRUSTED_ORIGINS = ['https://your_heroku_app_name.herokuapp.com','https://8000-your_local_development_site.com']
    ```

20. **Create Static Files**
    - In your project's root directory, create three new folders: `media`, `static`, and `templates`. This is where you'll store your static files and templates. Template folders will later be added to specific apps as required, along with css etc.

21. **Create a Procfile**
    - In your project's root directory, create a file named `Procfile` (no extension).
    - In the Procfile, add the following line of code:
    ```python
    web: gunicorn 'your_project_name'.wsgi  # replace "your_project_name" with your Django project's name
    ```
    - This file is necessary for running your app on Heroku. Gunicorn is a WSGI (Web Server Gateway Interface) HTTP server for Python web applications.

22. **Push Changes to GitHub**
    - To save your changes to your GitHub repository, run the following commands in your terminal:
    ```python
    git add .
    git commit -m "your_commit_message"  # replace "your_commit_message" with a short description of your changes
    git push
    ```

23. **Connect Heroku to GitHub**
    - Go to your Heroku app's dashboard and navigate to the "Deploy" tab.
    - In the "Deployment method" section, click on the "GitHub" button.
    - Connect your GitHub account if you haven't done so, and in the "Connect to GitHub" section, search for your GitHub repository and click "Connect."

24. **Deploy Your App**
    - Scroll down to the "Manual Deploy" section, select your GitHub branch (`main`), and click "Deploy Branch."
    - Wait for Heroku to finish deploying your app, and then click "View".
    - It is also optional to select Automatic Deploys.
</details>
<details><summary><b>Setting up Spotify Album Application</b></summary>

## Setting up the Django Spotify Album Retrieval

 This application allows you to fetch and display album data from the Spotify API. To implement, please follow the following steps.

### Prerequisites

Ensure you have the following:

- Python installed on your system.
- A Spotify developer account. If you don't have one, you can create a new account at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
- Spotify API credentials (Client ID and Client Secret).

### Steps

1. **Register for a Spotify API Key:**
   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and register for an account if you don't have one.
   - Log in to the dashboard with your Spotify account.
   - Accept the Terms of Service to gain access to the API.
   - Click on "Create an App" and fill out the form to register a new application. This will generate your Spotify API Key.

2. **Set up the Environment:**
   - Create a new file named `env.py` in the root directory of the project.
   - Open the `env.py` file and add the following lines:
     ```python
     import os
     
     os.environ["SPOTIFY_CLIENT_ID"] = "<your-client-id>"
     os.environ["SPOTIFY_CLIENT_SECRET"] = "<your-client-secret>"
     ```
     Replace `<your-client-id>` and `<your-client-secret>` with your actual Spotify API credentials.

3. **Implement Authentication and API Request Functions:**
   - Open the `spotify_data.py` file.
   - Implement the `get_auth_token()` function to authenticate API requests using the Spotify API credentials.
   - Implement the `get_album_details(album_ids)` function to fetch album details from the Spotify API.
   - Implement the `search_albums(query)` function to search for albums based on a query.
   - Implement the `get_album_ids(query)` function to retrieve album IDs from the search results.

4. **Fetch Album Data from the Spotify API:**
   - In your application code, use the implemented functions from `spotify_data.py` to fetch album data from the Spotify API.
   - You can retrieve album data based on artist name or any other criteria supported by the Spotify API.

5. **Store Fetched Album Data as Fixtures:**
   - Create a JSON file (e.g., `albums.json`) to store the fetched album data as fixtures.
   - Open the JSON file and load existing fixture data if available.
   - Append the new album data to the fixtures, ensuring there are no duplicates based on album IDs.
   - Save the updated fixtures back to the JSON file.

6. **Create a Django View Function:**
   - Open the `views.py` file.
   - Create a Django view function that reads the fixture data from the JSON file.
   - Parse the fixture data and pass it to the template context for rendering.

7. **Pass Fixture Data to the HTML Template:**
   - Create an HTML template (e.g., `album.html`) to display the album details.
   - Use Django template tags and loops to iterate over the fixture data and generate dynamic HTML content.
   - Pass the fixture data to the HTML template from the Django view function.

8. **Update the URL Configuration:**
   - Open the `urls.py` file.
   - Add a URL pattern to map the created view function to a URL endpoint.
   - This allows the application to handle requests and display the album details when accessing the corresponding URL.

9. **Test the Application:**
   - Start the Django development server by running the command `python manage.py runserver` in your terminal or command prompt.
   - Access the album page in a web browser by navigating to the appropriate URL.
   - Verify that the albums are displayed correctly and the functionality is working as expected.

10. **Optional - Enhancements and Customization:**
    - Customize the HTML template (`album.html`) and CSS styles to match your desired design.
    - Implement additional features such as pagination or filtering based on user input.

11. **Update the HTML Template:**
    - Modify the HTML template (`album.html`) to include the necessary HTML structure and styling.
    - Test the template to ensure the correct display of album information.

12. **Create a Form for Updating Albums:**
    - Add an HTML form to the `album.html` template.
    - Configure the form to submit a POST request to the `update_albums` view function.
    - Include an input field for the artist name.
    - Add a submit button to trigger the update.

13. **Implement the `update_albums` View Function:**
    - In the `views.py` file, create a view function named `update_albums` to handle the form submission.
    - Extract the artist name from the submitted form data.
    - Call the `create_fixtures(artist_name)` function from `spotify_data.py` to update the fixtures with new albums.
    - Redirect the user back to the album page after updating the fixtures.

14. **Update the URL Configuration:**
    - Open the `urls.py` file.
    - Add a URL pattern to map the `update_albums` view function to a URL endpoint.

15. **Test the Entire Application:**
    - Start the Django development server using the command `python manage.py runserver`.
    - Access the album page in a web browser and verify the correct display of albums.
    - Test the form submission by entering different artist names and checking if the fixtures are updated accordingly.

16. **Error Handling and Edge Cases:**
    - **This is a "Could Have", it depends on the functionality of the site and whether "store" items will be static or not.**

    - Implement error handling for API request failures and invalid artist names.
    - Handle scenarios where the fixture file is missing or empty.
    - Add appropriate error messages or fallback behavior to ensure a smooth user experience.


</details>
<details><summary><b>Local Deployment</b></summary>


If you wish to run this project locally on your machine, please follow the steps outlined below:

1. **Clone the Repository:**

    To make a copy of the project's repository on GitHub on your local machine, you can clone it. Replace `<repository_url>` with the actual URL of the repository and `<project_name>` with the name of the project directory that you cloned:

    ```
    # Clone the repository
    git clone <repository_url>
    # Change directory to the cloned project
    cd <project_name>
    ```

2. **Install Dependencies:**

    The project requires several Python libraries and packages to function correctly. The list of these can be found in the `requirements.txt` file. If you're using a virtual environment, ensure it's activated. Install the dependencies using pip with the following terminal command:

    ```
    pip3 install -r requirements.txt
    ```

3. **Configure Environment Variables:**

    This project uses environment variables to keep sensitive information secure. Create a new file named `env.py` at the root level of the project, and populate it with your data. Replace the placeholders with your actual Cloudinary API key, ElephantSQL database URL, and your chosen secret key:

    ```python
    import os

    os.environ.setdefault("CLOUDINARY_URL", '<enter your Cloudinary API key here>')
    os.environ.setdefault("DATABASE_URL", '<enter your ElephantSQL database URL here>')
    os.environ.setdefault("SECRET_KEY", '<enter your secret key here>')
    os.environ['DEVELOP'] = '1'  # for local environment only
    ```

    Remember to add the `env.py` file to the `.gitignore` file to prevent your sensitive data from being exposed.

4. **Migrate the Database:**

    Ensure you have a running PostgreSQL server that Django can connect to. Apply the migrations to create your database schema:

    ```
    python3 manage.py migrate
    ```
5. **Start the Project Locally:**

    If you're using a virtual environment, remember to activate it whenever you're running the project. With the project cloned, dependencies installed, environment variables set, and the database migrated, you can now start the project locally with the following commands:

    ```
    # Make migration
    python3 manage.py makemigrations
    # Apply the migrations
    python3 manage.py migrate
    # Create a superuser for the Django admin interface
    python3 manage.py createsuperuser
    # Start the Django development server
    python3 manage.py runserver
    ```

6. **Forking the Repository on GitHub:**

    You can fork the repository, which creates a copy of it in your own GitHub account:

    - Open GitHub and navigate to the project repository.
    - Click on the "Fork" button at the top of the page, which creates a new copy of the repository under your GitHub account.

7. **Cloning the Repository on GitHub:**

    To create a local clone of your forked repository, follow the steps below:

    - Navigate to the forked repository in your GitHub account.
    - Click the "Code" button, then under the "HTTPS" tab of the "Clone" section, click the clipboard icon to copy the URL.
    - Open a terminal window and navigate to the directory where you want the clone to reside.
    - Type "git clone", then paste the URL you copied from GitHub.
    - Press "Enter", and a local clone will be created.
</details>
<br>

# Credits
* [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) for API album retrieval.
* [Djecrety](https://djecrety.ir/) for secret Key
## Design 

* [The Record Hub](https://therecordhub.com)
* [Golden Discs](https://goldendiscs.ie)
* [Vinyl8](https://www.vinyl8.com)
* [Music Zone](https://musiczone.ie/shop)
## Content
* 

## Media
* [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)

## Code
* Django Documentation 
	* [DJANGO ](https://docs.djangoproject.com/)
* Code Institute
* 
* 
* 
	


# Acknowledgements

* 
* 
* 
* 
