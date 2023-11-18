<template>
  <div class="app_view">
    <router-view />
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App'
})
</script>

<style lang="sass">

@import './css/app.sass'

body
  background-color: #07061e

.app_view
  max-width: $max-width
  max-height: $max-height
  display: flex
  margin: auto
  border-radius: 5px
  background-color: #fff
</style>
