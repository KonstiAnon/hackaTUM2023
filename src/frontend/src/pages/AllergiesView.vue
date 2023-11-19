<script setup>
  import ProgressBar from 'src/components/ProgressBar.vue';
  import CardToggle from 'src/components/CardToggle.vue';

  import nuts from 'src/assets/icons/ic-no-nuts.png'

  // for now hardcode the allergies
  const allergies = [
    {
        label: "No Nuts",
        id: [60],
        src: nuts,
    },
    {
        label: "No Nuts",
        id: [60],
        src: nuts,
    },
    {
        label: "No Nuts",
        id: [60],
        src: nuts,
    },
    {
        label: "No Nuts",
        id: [60],
        src: nuts,
    },
  ];  

</script>

<template>
  <progress-bar />
    <div class="page">
      <div class="content">
        <div class="header">Begin Your Quest!</div>
        <div class="description">Share allergies for a personalized food adventure.</div>
      </div>
        <div class="content">
            <div v-for="allergie in allergies" :key="allergie.label">
                <card-toggle :label="allergie.label" :src="allergie.src" />
            </div>
        </div>
    </div>
    <div class="navigation absolute-bottom" >
        <q-btn round size="17px" color="primary" icon="arrow_right_alt"/>
    </div>
</template>

<style >
.page {

}

.header {
  font-size: 30px;
  font-weight: bolder;
}

.description {
  font-size: 18px;
}

.content {
  margin: 25px 40px;
}

.navigation {
  margin: 50px;
  text-align: right;
}
</style>



