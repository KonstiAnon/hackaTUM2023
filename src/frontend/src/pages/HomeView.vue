<script setup>
import ProgressBar from 'src/components/ProgressBar.vue';
</script>

<template>
  <div class="full-height">
    <progress-bar/>
      <div class="flex justify-center q-pa-md self-center">
        <div class="content">
          <img
            alt="Quasar logo"
            src="~assets/logo.png"
            style="width: 200px; height: 200px"
          />
          <div class="header">Begin Your Quest!</div>
          <div class="description">Welcome to a flavorful journey! Discover your tastes through a fun quest.
            Share your preferences, from allergies to skills, and uncover personalized culinary experiences
            tailored just for you.
          </div>
        </div>
      </div>
      <div class="navigation absolute-bottom">
        <q-btn round size="17px" color="primary" icon="arrow_right_alt"/>
      </div>
    </div>
</template>

<style>

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
  text-align: center;
}

.navigation {
  margin: 50px;
  text-align: right;
}
</style>



