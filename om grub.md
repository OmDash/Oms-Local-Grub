Om’s Local Grub
Video Demo: <Add your demo link here>
Description

Om’s Local Grub is a simple yet polished Flask web application that helps users discover nearby restaurants using the Yelp Fusion API. By entering a city, neighborhood, or ZIP code, users receive an organized grid of restaurant cards showing names, ratings, and addresses—all pulled in real time from Yelp’s database. The goal is to combine clean UI design with practical data integration, allowing people to find local eats quickly.

Motivation

As someone passionate about both technology and food culture, I wanted to create a small web app that simplifies restaurant discovery without the clutter of large commercial platforms. This project also let me explore API handling, environment security, and Flask routing, reinforcing my skills in full-stack web development.

How It Works

When the user submits a location through the search form on the homepage, a POST request is sent to the Flask backend. The server receives the request, adds the Yelp API key securely from a .env file, queries Yelp’s endpoint /businesses/search, and returns a filtered JSON response. The frontend (written in HTML, CSS, and vanilla JavaScript) dynamically updates the results grid, creating interactive restaurant cards.

Project Structure
├── app.py               # Flask server, routes, API logic
├── templates/
│   └── index.html       # Main page with form + results grid
├── static/              # Optional for CSS/JS extraction
├── .env                 # Stores YELP_API_KEY
└── requirements.txt     # Flask, requests, python-dotenv

Design Choices

Flask + Requests: Lightweight framework ideal for small web apps.

Environment Variables: Protects API keys and enables deployment flexibility.

Fetch API (Client Side): Simplifies asynchronous updates without reloading the page.

Minimal UI: A modern layout with a gradient background, rounded cards, and hover effects for clarity and engagement.

Challenges and Lessons

Configuring and testing the Yelp API required managing request limits and handling edge cases, such as empty results or invalid locations. I also learned to structure Flask projects cleanly and separate static files for scalability. Styling the interface taught me to balance simplicity and readability.

Future Improvements

Add filters for price, distance, and “open now.”

Integrate map visualization (Leaflet or Google Maps).

Deploy on Render or Railway with a proper production setup.

Improve error handling and pagination.

Conclusion

Om’s Local Grub demonstrates how a straightforward concept—finding nearby restaurants—can be turned into a functional, full-stack web application. It showcases my understanding of API integration, frontend-backend communication, and user experience design.