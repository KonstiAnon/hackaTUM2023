<script setup>
import Card from "components/RecipeCard.vue";
import CardStack from "components/CardStack.vue";
import PageHeader from "src/components/PageHeader.vue";
import {ref} from "vue";
import RecipeCard from "components/RecipeCard.vue";

const mockData = ref([{
  id: 1,
  name: "Chicken Stuff 1",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}, {
  id: 2,
  name: "Chicken Stuff 2",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}, {
  id: 3,
  name: "Chicken Stuff 3",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}, {
  id: 4,
  name: "Chicken Stuff 4",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}, {
  id: 5,
  name: "Chicken Stuff 5",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}, {
  id: 6,
  name: "Chicken Stuff 6",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}, {
  id: 7,
  name: "Chicken Stuff 7",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}])

</script>

<template>
      <PageHeader header="Discover Recipes" description="We're sure you'll love those!" :progress="0.75">
        <div class="flex justify-center">
          <q-scroll-area class="my-scroll">
            <RecipeCard v-for="recipe in mockData" :recipe="recipe" :key="recipe.id" class="card"/>
          </q-scroll-area>
        </div>
    </PageHeader>
</template>

<style lang="sass" scoped>
.my-scroll
  width: 100%
  height: 600px

.card
  padding-bottom: 20px
</style>
