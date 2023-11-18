<script setup>
import CardStack from "components/CardStack.vue";

const mockData = [{
  id: 1,
  name: "Chicken Stuff",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
},{
  id: 2,
  name: "Chicken Stuff2",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
},{
  id: 3,
  name: "Chicken Stuff3",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
},{
  id: 4,
  name: "Chicken Stuff4",
  skill: 1,
  img: "https://hips.hearstapps.com/hmg-prod/images/fennel-roasted-chicken-and-peppers-1639692168.jpg",
  other: undefined
}]
</script>

<template>
  <div class="flex flex-center">
    <CardStack :recipes="mockData"/>
  </div>
</template>

<style scoped></style>
