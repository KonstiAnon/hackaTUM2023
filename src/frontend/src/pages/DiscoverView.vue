<script setup>
import Card from "components/RecipeCard.vue";
import CardStack from "components/CardStack.vue";
import PageHeader from "src/components/PageHeader.vue";
import {ref} from "vue";
import RecipeCard from "components/RecipeCard.vue";

const mockData = ref([{
  id: 1,
  name: "Tacos mit Räuchertofu",
  skill: 1,
  img: "https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_1100,q_30,w_2600/hellofresh_s3/image/HF_Y23_R33_W05_DE_R4484-1_KB_Main_low-99964e18.jpg",
  other: undefined
}, {
  id: 2,
  name: "BBQ Burritos",
  skill: 1,
  img: "https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_1100,q_30,w_2600/hellofresh_s3/image/HF_Y23_R04_W13_DE_L4529-1_Main_low-2df9ba9f.jpg",
  other: undefined
}, {
  id: 3,
  name: "Elsässer Flammkuchen",
  skill: 1,
  img: "https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_1100,q_30,w_2600/hellofresh_s3/image/HF220706_R30_W35_DE_EXP2953-10_MB_Main_low-ded2657c.jpg",
  other: undefined
}, {
  id: 4,
  name: "Smokey Hähnchenfilet",
  skill: 1,
  img: "https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_1100,q_30,w_2600/hellofresh_s3/image/R38_W46_DE_R4806-1_Main_low-1832fd6d.jpg",
  other: undefined
}, {
  id: 5,
  name: "Chorizo-Kartoffelpfanne",
  skill: 1,
  img: "https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_1100,q_30,w_2600/hellofresh_s3/image/rauchige-argentinos-kartoffelpfanne-mit-peperoni-8f40a537-9a422e72.jpg",
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
