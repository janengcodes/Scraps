CREATE TABLE users(
    username VARCHAR(20) NOT NULL,  /* VARCHAR means it can be any number of characters up to the num in parenthesis */
    fullname VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    filename VARCHAR(64) NOT NULL,
    password VARCHAR(256) NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(username)
);

CREATE TABLE recipes(
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64) NOT NULL,
    ingredient_ids INTEGER[] NOT NULL,
    instructions NVARCHAR(5000) NOT NULL
);

CREATE TABLE ingredients(
    
);

CREATE TABLE pantry(
    username VARCHAR(20) NOT NULL 
    ingredient_id
    FOREIGN KEY(username)
        REFERENCES users(username)
        ON DELETE CASCADE
);
