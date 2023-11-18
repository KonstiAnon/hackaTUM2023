<template>
  <q-layout view="lHh Lpr lFf">
    <BrandHeader />

    <q-page-container>
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
    BrandHeader,
  },

  setup () {
  }
})
</script>

<style lang="sass" scoped>

@import '../css/app.sass'

</style>
