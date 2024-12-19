# Booking Management system

![amireponsive](https://github.com/user-attachments/assets/2948d27b-2bab-4634-b473-a2dfee4bc8e8)

## Overview

This is a booking system for a local music venue. This system allows for the venue to manage reservations for events allowing customers to make accounts then sign up to events
provided there are enough tickets remaining.

The live site is available  [here](https://miners-lantern-b436a12bd6f4.herokuapp.com/).

## Target audience
The target audience for this is venues that need to manage event attendance as well as individuals who want to browse and book events.

# User Stories

## User Story: As a user, I want to make an account

### Acceptance Criteria:

User can access a registration form
User must enter username
User must enter password that meets security requirements
User must confirm matching password
User can log in with created credentials
System validates duplicate emails/usernames
Error messages display for invalid inputs

## User Story: As a user, I want to make a booking

### Acceptance Criteria:

User must be logged in to make booking
User can select number of guests
System prevents booking if capacity exceeded
User receives booking confirmation message
Booking appears in user's booking list
Event capacity updates after successful booking
Total price calculated based on guests

## User Story: As a user, I want to create events from the admin panel

### Acceptance Criteria:

Admin access required
Form includes all required event fields
Image upload functionality
Published/unpublished option available
Validation for required fields
Confirmation on successful creation
Event immediately visible in admin panel

## User Story: As a user, I want to edit my bookings

### Acceptance Criteria:

User can edit only future bookings
User can modify guest numbers within capacity
System recalculates total price if guests changed
User receives confirmation message of change
Booking updates with new details

## User Story: As a user, I want to cancel a booking

### Acceptance Criteria:

User can cancel only future bookings
Cancellation requires confirmation
Event capacity updates after cancellation
Cancelled bookings removed form list

## User Story: As a user, I want to view my bookings

### Acceptance Criteria:

Bookings display event name, date, time
Bookings show number of guests and total price
Bookings sorted by date (upcoming first)
Booking status clearly displayed

## User Story: As an Admin, I want to edit upcoming events

### Acceptance Criteria:

Admin can edit only future events
All event fields editable
Changes don't affect existing bookings
Edit history maintained
Validation prevents invalid changes

## User Story: As a user, I want to see available events

### Acceptance Criteria:

Events page shows all upcoming events
Each event displays title, date, time, price
Available capacity shown for each event
Past events not displayed
Events sorted by date
Event details page accessible for each event

## User Story: As a user, I want to view the home page to understand what the venue offers

### Acceptance Criteria:

Hero section with venue image
Clear venue name and tagline
Featured/upcoming events section
Brief venue description
Quick links to booking system
Call-to-action for bookings
Navigation to other key pages
Social media links
Location preview/map
Responsive image gallery
Latest news/updates section

## User Story: As a user, I want the website to be responsive across all devices

### Acceptance Criteria:

Website adapts to mobile devices (320px and up)
Website adapts to tablets (768px and up)
Website adapts to desktop screens (1024px and up)
Navigation menu collapses to hamburger on mobile
Images scale appropriately across devices
Text remains readable at all screen sizes

## User Story: As a user, I want the website to be accessible

### Acceptance Criteria:

ARIA labels implemented where needed
Proper heading hierarchy (h1-h6)
Sufficient color contrast ratios
Alt text for all images

## User Story: As a user, I want to view the about page to learn more about the venue's history, offerings and submit a new event

### Acceptance Criteria:

Detailed venue history
Mission/vision statement
Venue facilities list
Team/staff introduction section
High-quality venue photos
Types of events hosted
Venue capacity information
Parking/transport information
Accessibility information
Contact form
FAQ section
Testimonials section
Form to add new event

# Agile
Throughout the project we followed the agile methodoloy. We set up a project board for assignment of taks between team members and prioritised creating the  minimum viable product
![agile board](https://github.com/user-attachments/assets/7c7a0f9f-9e8c-4a46-8da9-bfd9fbe055a0)

As well as the project board we also spent time ensuring our entity relationship diagram was well thought out and would lead to the creation of a database that would enable us to fufill our user story requirements.
![Entity realtionship diagram](https://github.com/user-attachments/assets/72adc638-c6f7-4c4e-bd03-dc8bae254857)


# Design
## Wireframes.
Balsamiq was used to create wireframes to determine the basic layout of the app.
![New Wireframe 1](https://github.com/user-attachments/assets/8c569a78-07bc-4ca8-bf24-64ef2c4cf881)
![New Wireframe 3](https://github.com/user-attachments/assets/3fdd68f1-a2da-49cd-8624-b258fc31f927)
![New Wireframe 2](https://github.com/user-attachments/assets/2610f37f-b631-4c6e-b344-ce7cafb6997e)

## Accessibility.
Accessibility was consdidered throuhgout the design process influencing descisions on fonts and colour schemes. Fonts were chosen with readability as a priority. 
### Font
The font chosen was roboto due to its modern look and its readability.
![font](https://github.com/user-attachments/assets/9d980fa7-14b4-4060-b98a-e9b6bcf67580)

### Colours
We went with the following colour scheme as it provides good contrast to make text readable but also has a grey background colour as white backgrounds can look harsh on a white monitor. The green provides a nice accent colour.
![colourscheme](https://github.com/user-attachments/assets/d84acb6b-9448-40de-bd3c-1354a37e8996)

The accessibility of the colour scheme was also validated using an online checker provided by web aim: https://webaim.org/resources/contrastchecker/
This validated that the contrast was good enough to ensure readability and that It was compliant with web content accessibility guidelines.
![contrast checker](https://github.com/user-attachments/assets/063efa43-8eed-496a-ab6f-c61e68fa1384)

# Features

<details>
<summary>Home Page</summary>

![Hero Seciton](https://github.com/user-attachments/assets/4cd380c9-cbf7-4e1f-a84f-4d476c8bccd9)
![Book Now button](https://github.com/user-attachments/assets/d5259ff9-a982-4d1f-b02c-64fcc08bcdc0)
![upcomingevents](https://github.com/user-attachments/assets/b8184bcd-70ed-4775-bae8-26e1d71d3945)

</details>

<details>
<summary>Events</summary>
 
![eventspage](https://github.com/user-attachments/assets/74ab4cc9-33ea-4f0b-a4f0-0e5ab5b86b1c)
![eventbooking](https://github.com/user-attachments/assets/5392cc20-984c-4292-a584-fec4ab1b480e)
![bookingconfirmation](https://github.com/user-attachments/assets/8dcc946d-268d-4103-8af5-57be192fb01e)

</details>

<details>
<summary>Bookings</summary>

![manageyourbookings](https://github.com/user-attachments/assets/ab183fc5-d78d-4436-8a1b-38e9838d7107)
![updateyourbooking](https://github.com/user-attachments/assets/6303699c-c7cc-4a16-a8ac-abacf472ca2b)
![deleteyourbooking](https://github.com/user-attachments/assets/af5613ad-9e6b-426b-b9ed-c8f0a2b6bfee)

</details>

<details>
<summary>About</summary>
 
![aboutpage](https://github.com/user-attachments/assets/20291078-ca82-4203-893a-ca06f49745c5)
![newsletterconfrimation](https://github.com/user-attachments/assets/664df1ce-f53c-4af7-ac00-86228f98ab97)

</details>

# Technologies/Languages/Frameworks Used 


<img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/><img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/><img src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/><img src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/><img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/><img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/><img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/><img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

### Other:
**PostgreSQL** - Database management system<br>
**Cloudinary** - Cloud-based image storage<br>
**Whitenoise** - For serving static files directly from Django<br>
**Django Crispy Forms** - Form rendering<br>
**GitHub Projects** - Project management and tracking<br>
**Balsamiq** - Wireframes and design prototypes<br>

# Testing and validation

# Lighthouse results

Gernal scoring across pages was good, some room for improvment on preformance due to large images.

![lighthouse](https://github.com/user-attachments/assets/fdd7260c-4701-4fee-87cd-61a6023e441e)
![lighthousemobile](https://github.com/user-attachments/assets/ec3bbd81-c5e0-491f-b34e-5a1fd328f72a)

# Manual Testing

## Account Management Testing

| Feature | Test Case | Steps | Expected Result | Pass/Fail |
|---------|-----------|-------|-----------------|-----------|
| Account Creation | Valid Registration | 1. Navigate to register page<br>2. Enter valid details<br>3. Submit form | Account created and confirmation email sent | [Pass] |
| | Invalid Email | 1. Enter invalid email format<br>2. Submit form | Error message shown | [Pass] |
| | Duplicate Email | 1. Enter existing email<br>2. Submit form | Error message about existing account | [Pass] |
| | Password Mismatch | 1. Enter different passwords<br>2. Submit form | Error message about non-matching passwords | [Pass] |
| Login | Valid Login | 1. Enter correct credentials<br>2. Submit | Successfully logged in and redirected | [Pass] |
| | Invalid Login | 1. Enter incorrect credentials<br>2. Submit | Error message shown | [Pass] |

## Booking Management Testing

| Feature | Test Case | Steps | Expected Result | Pass/Fail |
|---------|-----------|-------|-----------------|-----------|
| Create Booking | Valid Booking | 1. Select event<br>2. Enter valid guest number<br>3. Submit | Booking confirmed message shown | [Pass] |
| | Exceed Capacity | 1. Select event<br>2. Enter guests > capacity<br>3. Submit | Error message shown | [Pass] |
| View Bookings | Booking List | 1. Navigate to My Bookings<br>2. Check all bookings visible | All bookings displayed correctly | [Pass] |
| Edit Booking | Valid Edit | 1. Select booking<br>2. Modify details<br>3. Save | Changes saved and confirmed | [Pass] |
| Cancel Booking | Cancel Future | 1. Select future booking<br>2. Cancel<br>3. Confirm | Booking cancelled message shown| [Pass] |

## Event Management Testing

| Feature | Test Case | Steps | Expected Result | Pass/Fail |
|---------|-----------|-------|-----------------|-----------|
| View Events | Event List | 1. Navigate to events page<br>2. Check display | All events listed | [Pass] |
| | Event Details | 1. Select event<br>2. View details | All information displayed correctly | [Pass] |
| Create Event | Valid Creation | 1. Enter all details<br>2. Upload image<br>3. Submit | Event created and visible | [Pass] |
| | Invalid Creation | 1. Submit without required fields | Error messages shown | [Pass] |
| Edit Event | Valid Edit | 1. Modify event details<br>2. Save changes | Changes saved and visible | [Pass] |

## Admin Testing

| Feature | Test Case | Steps | Expected Result | Pass/Fail |
|---------|-----------|-------|-----------------|-----------|
| Admin Access | Create Admin | 1. Create admin account<br>2. Verify privileges | Admin access granted | [Pass] |
| | Access Control | 1. Test restricted areas<br>2. Verify permissions | Appropriate access levels | [Pass] |
| | User Management | 1. View user list<br>2. Modify user details | Changes saved successfully | [Pass] |

## Responsive Design Testing

| Device | Test Case | Steps | Expected Result | Pass/Fail |
|--------|-----------|-------|-----------------|-----------|
| Mobile | Layout | 1. Test on 320px+ screens<br>2. Check all features | Proper mobile layout | [Pass] |
| Tablet | Layout | 1. Test on 768px+ screens<br>2. Check all features | Proper tablet layout | [Pass] |
| Desktop | Layout | 1. Test on 1024px+ screens<br>2. Check all features | Proper desktop layout | [Pass] |

## Accessibility Testing

| Feature | Test Case | Steps | Expected Result | Pass/Fail |
|---------|-----------|-------|-----------------|-----------|
| Visual | Contrast | 1. Check color contrast<br>2. Verify readability | Meets WCAG standards | [Pass] |
| Forms | Labels | 1. Check all form fields<br>2. Verify aria-labels | All forms properly labeled | [Pass] |


# Validation

## HTML

1. First validaiton

![htmlerror](https://github.com/user-attachments/assets/5409d09d-0c14-4e2d-a873-97a21c594309)

 - Errors shown on the carousel due to blank attibutes for inactive slides. To fix, else statements added for inactive slides.

## CSS

![cssvalid](https://github.com/user-attachments/assets/ea2de487-375c-4f91-973a-02c9d105c066)

## Python

![pylint](https://github.com/user-attachments/assets/6ad01ed4-549f-4907-9606-492ae426772e)


# Deployment
The application was deployed to Heroku using Gunicorn. A Procfile was created containing the instructions to run the server. A file called requirements.txt  was also used to install all the dependancies needed to run the app. An external database was used instead of the built in heroku one.
 

The live site is available [here](https://miners-lantern-b436a12bd6f4.herokuapp.com/).

# Development Team

- **Robert Beach**
[GitHub](https://github.com/surfdemon)

- **Zara Samm:**
[GitHub](https://github.com/ZASamm)

- **Becky Williams**
[GitHub](https://github.com/BeckyW-Design)

- **Richard Hallam:**
[GitHub](https://github.com/Richard-Hallam)


## Attributions

- AI used to assist with text for content generation, bug fixes, coding assitance and user stories. [Chat GPT](https://chatgpt.com/) & [Claude](https://claude.ai/)

- Font awesome used for any icons present and fonts used from google fonts

- Images used from [Pexels](https://www.pexels.com/)

- [Canva](https://www.canva.com/en_gb/) used for logo  design.

- [Lucidchart](https://www.lucidchart.com/pages/database-diagram/database-schema) used for Database Schema.

- [Stackoverflow](https://stackoverflow.co/), [W3Schools](https://www.w3schools.com/) and relevent technlogoy documentation used for bug and issue look ups.

- Githut copilot used for assistance.


# Reflection on Development process.

## Successes

Our team of four achieved several key successes during this project:

### Team Collaboration

- Demonstrated effective communication throughout the development process
- Organised clear task distribution among team members
- Maintained regular check-ins to ensure everyone was on track
- Achieved good balance of skills across the team

### Project Management

- Adhered to our planned timeline
- Fulfilled all core functionality requirements
- Successfully implemented all main user stories
- Maintained manageable scope for our four-day timeframe

### Technical Implementation

- Developed clean, simple codebase that's easy to maintain
- Achieved successful integration of Django with Bootstrap
- Completed smooth deployment to Heroku
- Created responsive design that works well across devices

## Challenges

- Brief learning curve with Django
- Quickly overcame through pair programming and knowledge sharing
- Transformed into a good learning experience for the whole team

## Final Thoughts

The Miner's Lantern booking system project was a successful demonstration of what can be achieved with clear goals and good teamwork. Key takeaways include:

### Project Approach

- Keeping the scope simple proved the right decision
- Focus on core functionality yielded positive results
- Clean, functional design served the purpose well

### Team Dynamics

- Four-person team size worked brilliantly for this project
- Everyone maintained clear roles and responsibilities
- Good mixture of skills among team members

### Future Improvements

- Established solid foundation for adding more features
- Opportunity to add more advanced booking features
- We are aware the Parallax scrolling on the home page does not work with IOS, this is something we would look to update with the next realese.
