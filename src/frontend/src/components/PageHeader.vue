<script>
import { defineComponent, ref } from 'vue'
import ProgressBar from 'src/components/ProgressBar.vue';

export default defineComponent({
    name: 'MainLayout',
    components: {
        ProgressBar
    },        
    props: {
        header: String,
        description: String,
        progress: Number
    },
    setup () {
    }
})

</script>

<template>
  <progress-bar :progress="progress" />
      <div class="content">
        <div class="header">{{ this.header }}</div>
        <div class="description">{{ this.description }}</div>
      </div>
        <div class="content">
            <slot />
        </div>
</template>

<style scoped>

.header {
  font-size: 30px;
  font-weight: bolder;
}

.description {
  font-size: 18px;
  height: 50px;
}

.content {
  margin: 25px 40px;
}
</style>



