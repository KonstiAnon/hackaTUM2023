<template>
    <div class="progressbar">
        <q-linear-progress :value="0.2" />
    </div>
</template>

<script setup>

</script>

<style lang="sass">
.q-linear-progress
    overflow: unset

.q-linear-progress__model
    background-color: #437849
    &:before
        content: ' '
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
  