# TBC Culinary

<p>A Python project that scrapes recipes from kulinaria.ge, extracts data, and stores it in MongoDB.</p>
<p>After scraping and storing recipes in MongoDB, the following statistics are displayed to users :</p>

1. **Average number of ingredients**
2. **Average number of preparation steps per recipe**
3. **Recipe with the most portions(prints its name and url)**
4. **Author with the most recipes**


### Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

#

### Features

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
- Run queries and display results to the users.

#

### Prerequisites

- <img src="readme/assets/python.png" width="25" style="position: relative; top: 8px" /> _Python @3.X and up_

- MongoDB (installed locally or using a cloud service like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))

- Libraries:
  - `aiohttp` (for making asynchronous web requests)
  - `beautifulsoup4` (for parsing HTML)
  - `pymongo` (for interacting with MongoDB)
  - `asyncio` (for managing asynchronous operations)

- Other packages that comes with python: Re


#

### Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NikaKhiz/TBCulinary.git
    cd TBCulinary
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
    or

    ```bash
    python3 -m venv venv
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

**Run scripts**:
  - Simply run the `main.py` file:

  ```bash
  python main.py
  ```
  or

  ```bash
  python3 main.py
  ```

### After that program will scrap the data from kulinaria.ge, save extracted information in db, run queries and display the results in terminal!!!


### Project Structure

```bash
├─── readme
│   ├─── assets
- .gitignore
- database_generator.py
- main.py
- queries.py
- query_strings.py
- readme.md
- requirements.txt
- schemas.txt
- scraper.txt
- utils.py
```