<template>
    <div class="progressbar">
        <q-linear-progress :value="this.progress" />
    </div>
</template>

<script>
import { defineComponent, ref } from 'vue';

    export default defineComponent({
        name: 'ProgressBar', 
        props: {
            progress: Number
        },
        setup () {
        }
    })
</script>

<style lang="sass">
.q-linear-progress
    overflow: unset

.q-linear-progress__model
    background-color: #437849
    &:before
        background-image: url('src/assets/logo_wt.png')
        position: absolute
        background-size: 40px 16px
        display: inline-block
        width: 40px
        height: 16px
        right: -5px
        top: -6px
        z-index: 100

</style>
  