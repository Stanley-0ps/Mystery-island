# Mystery Island — The Lost Lighthouse

A Python-based text adventure game where players explore a mysterious island, collect useful items, manage their energy, overcome obstacles, and discover the Lost Lighthouse.

## Features

- **Player Setup:** Enter your name and age at the beginning of the game.
- **Island Exploration:** Explore five locations:
  - Beach
  - Jungle
  - Cave
  - Old Bridge
  - Lighthouse
- **Inventory System:** Collect and manage items.
- **Item Collection:** Find a lantern at the Beach and a rope in the Jungle.
- **Location Requirements:**
  - Cave requires a lantern.
  - Old Bridge requires a rope.
  - Lighthouse requires both a lantern and a rope.
- **Energy Management:** Travelling between locations consumes energy.
- **Player Status:** Check your current energy, location, and inventory.
- **Replay System:** Start another game after finishing or quitting.

## Requirements

- Python 3.8 or later
- No external Python packages required.

## Project Structure

```text
Mystery-Island/
│
├── main.py
├── tests/
│   └── test_game.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone <https://github.com/Stanley-0ps/Mystery-island.git>
```

2. Enter the project directory:

```bash
cd Mystery-island
```

3. Start the game:

```bash
python3 main.py
```

## How to Play

1. Enter your name and age.
2. Choose an option from the main menu.
3. Select locations to explore.
4. Collect the lantern and rope.
5. Manage your energy carefully.
6. Meet the requirements to enter restricted locations.
7. Reach the Lighthouse to win!

## Running Tests

The project includes automated unit tests using Python's built-in `unittest` framework.

Run the tests with:

```bash
python3 -m unittest discover -s tests -v
```

### Test Coverage

The eight tests cover:

| Test | What it checks |
|---|---|
| Item collection | Items can be collected |
| Duplicate prevention | Items cannot be collected twice |
| Empty inventory | Empty inventory displays correctly |
| Inventory display | Collected items are displayed |
| Jungle travel | Location and energy update correctly |
| Cave restriction | Lantern is required |
| Bridge restriction | Rope is required |
| Lighthouse victory | Both items allow the player to win |

**Latest test result:** 8 tests passed.

## Technologies Used

- Python 3
- `unittest`
- `unittest.mock`

## Learning Outcomes

This project demonstrates practical use of:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Global variables and program state
- Exception handling
- Modules and imports
- Unit testing

## Author

Developed as part of the Learn2Earn Python challenge.

## License

This project is intended for educational purposes.
