<script setup>
import {defineProps} from "vue";

// define props
defineProps({
  recipe: Object,
});

</script>

<template>
  <!--show image from recipe.image_url and like and dislike button. Like and dislike button should trigger event in parent -->
  <!--  make the like and dislike buttons next to each other and use a cross and heart icon (fontawesome, red and green)-->

  <div>
    <h3>{{ recipe.title }}</h3>
    <img :src="recipe.image_url" width="500" alt="recipe image">
    <div class="buttons">
      <button id="dislike" @click="$emit('dislike')">Dislike</button>
      <button id="like" @click="$emit('like')">Like</button>
    </div>
  </div>

</template>

<style scoped>
  .buttons button {
    margin: 5px;
  }

  #like {
    background-color: green;
  }

  #dislike {
    background-color: red;
  }
</style>