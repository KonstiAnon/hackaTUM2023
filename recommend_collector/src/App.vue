<script setup>
// fetch the recipes from the API
import {ref} from "vue";
import Tinder from "./components/Tinder.vue";

const id = ref("");

const recipes = ref([]);

// current recipe data
const currentRecipe = ref(null);

// loading indicator
const loading = ref(true);

const popRandom = () => {
  // pop a random recipe from the recipes array
  const index = Math.floor(Math.random() * recipes.value.length);
  currentRecipe.value = recipes.value[index];
  recipes.value.splice(index, 1);
};

fetch("http://localhost:3000/recipes")
    .then((response) => response.json())
    .then((data) => {
      id.value = data.id;
      recipes.value = data.recipes;
      popRandom();
      loading.value = false;
    });

const postFavoring = (user_id, recipe_id, like) => {
  const body = JSON.stringify({
    user_id: user_id,
    recipe_id: recipe_id,
    like: like,
  });

  // post the favoring to the API
  // likes is a boolean, also pass the user_id and recipe_id
  fetch("http://localhost:3000/like", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: body,
  })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
}

const like = (like) => {
  // like or dislike the current recipe
  postFavoring(id.value, currentRecipe.value.id, like);
  // get new recipe
  popRandom();
}
</script>

<template>
  <div>
    <h1>Recommend Collector</h1>
    <p v-if="loading">Loading...</p>
    <div v-else>
      <div v-if="currentRecipe">
        <Tinder :recipe="currentRecipe" @like="like(true)" @dislike="like(false)"/>
      </div>
      <div v-else>
        <p>No more recipes</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
