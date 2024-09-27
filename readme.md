# TBC Culinary

A Python project to scrape recipes from kulinaria.ge, extract data, and store it in MongoDB

## Features

- Asynchronously scrapes recipe details including:
  - Recipe name
  - Recipe URL
  - Category and Subcategory names & URLs
  - Image URL
  - Brief description
  - Author name
  - Number of servings
  - Ingredients list
  - Preparation steps
- Automatically stores data in MongoDB for further analysis.

## Requirements

- Python 3.x
- MongoDB (installed locally or using a cloud service like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))
- Libraries:
  - `aiohttp` (for making asynchronous web requests)
  - `beautifulsoup4` (for parsing HTML)
  - `pymongo` (for interacting with MongoDB)
  - `asyncio` (for managing asynchronous operations)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NikaKhiz/TBCulinary.git
    cd TBCulinary
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

5. **MongoDB Setup**:
    - If you haven’t installed MongoDB locally, either [download and install MongoDB](https://www.mongodb.com/try/download/community) or use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to create a cloud-based database.
    - Make sure MongoDB is running, or your connection to MongoDB Atlas is properly set up.

## Usage

**Run the scraper**:
    - Simply run the `main.py` file:
    ```bash
    python main.py
    ```
    - The scraper will automatically extract recipe data and store it in your MongoDB database.

## MongoDB Queries

After scraping and storing recipes in MongoDB, the following statistics are fetched when you run the project:
1. **Average number of ingredients**
2. **Average number of preparation steps per recipe**
3. **Recipe with the most portions(prints its name and url)**
4. **Author with the most recipes**
