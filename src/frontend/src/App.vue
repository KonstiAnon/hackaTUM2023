<template>
    <div class="q-pa-md app_view">
      <router-view/>
    </div>
</template>

<script>
import {defineComponent} from 'vue'

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
  min-height: 100vh
  display: flex
  margin: auto
</style>
