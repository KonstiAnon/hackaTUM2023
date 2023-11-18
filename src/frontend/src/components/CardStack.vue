<script setup>
  import RecipeCard from "components/RecipeCard.vue";

  defineProps({
    recipes: {
      type: Array,
      required: true
    }
  })
</script>

<template>
<!--  // stack cards on top of each other using the recipecard component. They are all skewed a bit-->
<!--  // to the right and down to give the impression of a stack of cards.-->

  <div class="stack">
    <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" class="card"/>
  </div>

</template>

<style lang="sass" scoped>

.stack
  display: grid
  grid-template-columns: 1fr

.card
  grid-row-start: 1
  grid-column-start: 1
</style>
