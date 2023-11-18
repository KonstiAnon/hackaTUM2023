<template>
<label class="card">
    <img :src="this.src" />
    <input type="checkbox" checked="checked">
    <div class="text">{{ label }}</div>
</label>
</template>

<script lang="js">

export default {
  props: {
    label: String,
    src: String
  }
}

</script>

<style lang="sass" scoped>
.card
    width: 50%
    max-width: 140px
    display: block
    padding: 10px 8px 6px 8px
    position: relative
    border: 1px solid $disabled
    border-radius: 5px
    text-align: center
    cursor: pointer
    color: $disabled
    font-size: 18px

    input
        position: absolute
        opacity: 0
        cursor: pointer
        height: 0
        width: 0

    img
        width: 30px
        margin: 4px
        filter: saturate(0)

.card:has(input:checked)
    background-color: $primary
    color: white

    img
        filter: saturate(1)


    
        
    
</style>
  