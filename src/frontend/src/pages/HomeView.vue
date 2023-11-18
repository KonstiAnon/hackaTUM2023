<script setup>
  import ProgressBar from 'src/components/ProgressBar.vue';
</script>

<template>
  <progress-bar />
    <div class="page">
      <div class="content absolute-center">
        <img
          alt="Quasar logo"
          src="~assets/logo.png"
          style="width: 200px; height: 200px"
        />
        <div class="header">Begin Your Quest!</div>
        <div class="description">Welcome to a flavorful journey! Discover your tastes through a fun quest.
          Share your preferences, from allergies to skills, and uncover personalized culinary experiences
          tailored just for you.</div>
      </div>
    </div>
    <div class="navigation absolute-bottom" >
        <q-btn round size="17px" color="primary" icon="arrow_right_alt"/>
    </div>
</template>

<style >
.page {
  text-align: center;
}

.header {
  font-size: 40px;
  font-weight: bolder;
}

.description {
  font-size: 18px;
  hyphens: auto; 
	text-align: justify;
}

.content {
  width: 310px;
  content: center;
}

.navigation {
  margin: 50px;
  text-align: right;
}
</style>



