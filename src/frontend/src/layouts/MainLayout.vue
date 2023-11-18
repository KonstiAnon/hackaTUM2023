<template>
  <q-layout view="lHh Lpr lFf" container class="my-layout shadow-2 rounded-borders">
    <BrandHeader />

    <q-page-container style="flex-grow: 1">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import BrandHeader from 'src/components/BrandHeader.vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    BrandHeader
},

  setup () {
  }
})
</script>

<style lang="sass" scoped>

@import '../css/app.sass'

.my-layout
  height: $max-height
  background-color: white
  display: flex

</style>
