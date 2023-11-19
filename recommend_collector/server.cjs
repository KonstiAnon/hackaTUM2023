const uuidv4 = require('uuid').v4;
const sqlite3 = require('sqlite3').verbose();
const express = require('express');
const cors = require('cors');
const bodyParser = require("body-parser");

const db = new sqlite3.Database('./recommend.db');

// Create the likes table if it doesn't exist
const createLikesTable = `CREATE TABLE IF NOT EXISTS likes
                          (
                              id
                              INTEGER
                              PRIMARY
                              KEY
                              AUTOINCREMENT,
                              recipe_id
                              INTEGER
                              NOT
                              NULL,
                              user_id
                              TEXT
                              NOT
                              NULL,
                              like
                              BOOLEAN
                              NOT
                              NULL
                          )`;
db.serialize(() => {
    db.run(createLikesTable, (err) => {
        if (err) {
            console.log(err);
        }
    });
    // Create a unique index on recipe_id and user_id
    // This will prevent a user from liking the same recipe twice
    const createIndex = `CREATE UNIQUE INDEX IF NOT EXISTS recipe_user ON likes (recipe_id, user_id)`;
    db.run(createIndex, (err) => {
        if (err) {
            console.log(err);
        }
    });
});


// Load recipes from ../data/recipes.json and format them for the frontend
// Array of id, title, description, image_url`
const recipes = require('../data/recipes.json').map((recipe, index) => {
    return {
        id: recipe.id,
        title: recipe.name,
        description: recipe.description,
        image_url: `https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_1100,q_30,w_2600/hellofresh_s3${recipe.imagePath}`,
    }
});

const app = express();
app.use(cors());
app.use(bodyParser.json());

// endpoint for getting all recipes
// Also returns a random uuidv4 for the frontend to use
app.get('/recipes', (req, res) => {
    const id = uuidv4();
    res.json({id, recipes});
});

// endpoint for giving a like/dislike to a recipe based on recipe id and user id
// user id is a uuidv4
// recipe id is a string
// like is a boolean
app.post('/like', (req, res) => {
    // get user_id, recipe_id and like from the request body
    const user_id = req.body.user_id;
    const recipe_id = req.body.recipe_id;
    const like = req.body.like;
    // log
    console.log(`User ${user_id} ${like ? 'liked' : 'disliked'} recipe ${recipe_id}`);
    // insert the like into the database
    const sql = `INSERT INTO likes (recipe_id, user_id, like)
                 VALUES (?, ?, ?)`;
    db.run(sql, [recipe_id, user_id, like], (err) => {
        if (err) {
            console.log(err);
            res.sendStatus(500);
        } else {
            // empty json response
            res.json({});
        }
    });
});


// create app
app.listen(3000, () => {
    console.log('Server listening on port 3000');
});