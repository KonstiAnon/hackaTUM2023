<script setup>
import RecipeCard from "components/RecipeCard.vue";
import {computed} from "vue";

const props = defineProps({
  recipes: {
    type: Array,
    required: true
  }
})

const reversedRecipes = computed(() => {
  return props.recipes.slice().reverse()
})
</script>

<template>
      <div class="stack">
        <RecipeCard v-for="recipe in reversedRecipes" :recipe="recipe" :key="recipe.id" class="card"/>
      </div>
</template>

<style lang="sass" scoped>
.stack
  display: grid
  grid-template-columns: 1fr

  // first should be a bit bigger to stand out
.card:nth-last-child(1)
  transform: scale(1.05)

// second child should be rotated to the left slightly
.card:nth-last-child(2)
  transform: translateX(-15px) rotate(-10deg)

// third child should be rotated to the right slightly
.card:nth-last-child(3)
  transform: translateX(10px) rotate(10deg)

.card
  grid-row-start: 1
  grid-column-start: 1
  transition: transform 0.5s
</style>
