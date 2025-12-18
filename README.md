# Cardex

This is a Pokemon TCG management and inventory web app.

## Tech Stack

**Backend:**
*   **Language:** Python 3.x
*   **Framework:** FastAPI
*   **Database:** SQLite + SQLAlchemy 2.0 (ORM)
*   **Server:** Uvicorn
*   **External API:** TCGDex SDK (for card metadata)
*   **API Documentation:** Swagger UI (built-in to FastAPI)

**Frontend:**
*   **Framework:** React 19 + Vite 7
*   **Routing:** React Router DOM 7
*   **Styling:** Tailwind CSS 3
*   **Animations:** Framer Motion 11
*   **HTTP Client:** axios 1.7

## Project Architecture

The application follows a client-server architecture.
*   **Backend:** Acts as the source of truth for the user's **Inventory** and **Decks**. It also acts as a proxy/cache for the **TCGDex API**.
*   **Frontend:** A Single Page Application (SPA) interacting with the FastAPI backend.
*   **Database:** A local SQLite database file (`cardex.db`) stored within the project directory.

### Data Strategy
To keep the application simple and performant:
1.  **Card Metadata:** We will leverage the `tcgdex-sdk` to fetch card details (images, stats, sets).
2.  **Caching:** We will implement a local cache (in SQLite) for card metadata to minimize API calls. When a card is viewed or added, we save its metadata locally.
3.  **Inventory:** Stores specific instances of cards owned by the user (linking to the cached metadata).

### Deck Association Logic
*   **Deck:** A container for cards.
*   **InventoryItem:** A specific physical card owned by the user (has a unique UUID).
*   **DeckCard:** A many-to-many association table linking `Deck` and `InventoryItem`.
    *   **Logic:** To add a card to a deck, we link a specific `InventoryItem` UUID to the `Deck` UUID.
    *   **Multiples:** If a user wants 3 Pikachus in a deck, they must have 3 distinct Pikachu `InventoryItem` records in their inventory. We link each of those 3 unique UUIDs to the deck. This ensures we don't add more cards to a deck than we physically own.

## Implementation Plan

### Phase 1: Backend Core & TCGDex Integration
**Goal:** Establish the API, database connection, and verify with Swagger UI.

- [x] **Project Setup**
    - [x] Initialize FastAPI project structure.
    - [x] Configure SQLite database connection (local file).
- [x] **TCGDex Integration**
    - [x] Create a service wrapper around `tcgdex-sdk`.
    - [x] Implement caching: Check DB `CardMetadata` first, then fetch from API if missing.
- [x] **Database Models**
    - [x] `CardMetadata`: Stores static info (ID, Name, Image URL, Set) from TCGDex.
    - [x] `InventoryItem`: Represents a physical card (UUID, Condition, Location, Foreign Key to `CardMetadata`).
    - [x] `Deck`: Represents a collection (UUID, Name).
    - [x] `DeckCard`: Association table (Deck UUID, InventoryItem UUID).
- [ ] **API Endpoints**
    - [ ] `GET /cards/search`: Search cards via TCGDex (cache results).
    - [ ] `POST /inventory`: Add a card to inventory.
    - [ ] `GET /inventory`: List all owned cards.
    - [ ] `GET /decks`: List all decks.
    - [ ] `POST /decks`: Create a new deck.
    - [ ] `POST /decks/{id}/cards`: Add/Remove cards from a deck.
- [ ] **Verification**
    - [ ] Verify all endpoints using Swagger UI (`http://localhost:8000/docs`).

### Phase 2: Frontend Foundation & Library
**Goal:** View and manage the card collection.

- [ ] **Frontend Setup**
    - [ ] Initialize Vite + React + Tailwind.
    - [ ] Setup React Router.
- [ ] **Library View (Home)**
    - [ ] Fetch and display cards from `GET /inventory`.
    - [ ] Implement grid layout for cards.
- [ ] **Add Card Interface**
    - [ ] Create a modal/page to search for cards.
    - [ ] Connect to `GET /cards/search`.
    - [ ] "Add to Inventory" button (creates `InventoryItem`).

### Phase 3: Deck Builder
**Goal:** Create and manage decks using a split-screen interface.

- [ ] **Deck Management UI**
    - [ ] Page to list existing decks.
    - [ ] Button to create a new deck.
- [ ] **Deck Editor UI**
    - [ ] **Split Screen Layout:**
        -   **Left Panel (Inventory):** List of available cards in inventory (not currently in other decks).
        -   **Right Panel (Deck):** Cards currently in the deck.
    -   **Interaction:**
        -   **Search:** Search bar in the Left Panel to find specific cards in inventory.
        -   **Add (+):** Button on inventory items to move them to the deck.
        -   **Remove (-):** Button on deck items to move them back to inventory.
- [ ] **Deck Persistence**
    - [ ] Save deck composition changes to backend immediately or on "Save".

### Phase 4: Refinement & Polish
**Goal:** Improve user experience.

- [ ] **Filtering & Sorting**
    - [ ] Filter inventory by Set, Type, or Rarity.
- [ ] **Card Details**
    - [ ] Detailed view of a card (attacks, HP, etc.) on click.
- [ ] **Inventory Locations**
    - [ ] Add field to specify where a card is stored (e.g., "Binder 1", "Box A").
