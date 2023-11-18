<script setup>
  import ProgressBar from 'src/components/ProgressBar.vue';
  import ButtonToggle from 'src/components/ButtonToggle.vue';
  import PageHeader from 'src/components/PageHeader.vue';

  import level1 from 'src/assets/icons/flames.png'
  import level2 from 'src/assets/icons/flamesx2.png'
  import level3 from 'src/assets/icons/flamesx3.png'

  // for now hardcode the allergies
  const allergies = [
    {
        "label":"Kitchen Crusader", 
        "src":level1
    },
    {
        "label":"Cooking Connoisseur",
        "src": level2
    },
    {
        "label":"Eoicurean Expert",
        "src":level3
    },
];
</script>

<template>
  <progress-bar />
    <PageHeader header="Select Your Skill Level" description="Ready to enter the realm of cooking? Pick your expertise level.">
        <div class="row justify-center">
            <template v-for="allergie in allergies" :key="allergie.label">
                <button-toggle :label="allergie.label" :src="allergie.src" />
            </template>
        </div>
    </PageHeader>
    <div class="navigation absolute-bottom" >
        <q-btn round size="17px" color="primary" icon="arrow_right_alt" to="tinder"/>
    </div>
</template>

<style scoped>
.navigation {
  margin: 50px;
  text-align: right;
}
</style>



