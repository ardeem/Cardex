# Cardex

This is a Pokemon TGC management and inventory web app.

## Tech Stack
Backend:

Python 3.x + FastAPI
SQLAlchemy 2.0 + SQLite
Uvicorn ASGI server
Frontend:

React 19 + Vite 7
React Router DOM 7
dnd-kit (drag & drop)
Tailwind CSS 3
Framer Motion 11
axios 1.7

# Back End

Use a Pydantic backend server to interface between the database and the frontend
Create data models for decks and cards, both would have UUID's, additionally the card model would have a card ID such as TWM 13 to interact with API's to pull card information from TCGDex

The deck model would contain card UUID's, as they would have the ability to create decks from the universe of all cards
The card model would include all cards available in English expansions, and would include details such as the card ID, whether it is available in inventory, where it is located if it is available in inventory.

# Front End

It will be a Vite.js and React.js application for JavaScript
Styling will use Tailwind.css

## User Flow

The start page would be the library that contains all of the cards available in my inventory, and eventually we will have functions for sorting and filtering. This page will also have a section/modal to add new cards to add to my library/inventory.

From the start page, we can navigate to the "Decks" page, which has premade decks that I've made and it will allow me to create new decks to add. When I want to create a new deck, I imagine having a split screen page with avaialble cards from my inventory on the left, and dragging it to the right to create my new deck.