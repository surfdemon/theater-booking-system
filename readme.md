# Booking Management system


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

