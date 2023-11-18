<script setup>
import Card from "components/RecipeCard.vue";

const mockData = {
  id: 1,
  name: "Chicken Stuff",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}
</script>

<template>
  <q-page class="flex flex-center">
    <Card :recipe="mockData"/>
  </q-page>
</template>

<style scoped></style>
