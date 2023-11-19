<script setup>
import Card from "components/RecipeCard.vue";
import CardStack from "components/CardStack.vue";
import PageHeader from "src/components/PageHeader.vue";
import {ref} from "vue";

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


const decide = (like) => {
  // remove 1st element
  mockData.value.shift()
}

</script>

<template>
      <PageHeader header="Matching Time" description="Discover Your Taste Buds' Soulmate!" :progress="0.75">
        <div class="flex justify-center">
          <CardStack :recipes="mockData"/>
          <q-btn round size="17px" color="secondary" icon="favorite" @click="decide(true)"/>
        </div>
    </PageHeader>
</template>

<style scoped>
</style>
