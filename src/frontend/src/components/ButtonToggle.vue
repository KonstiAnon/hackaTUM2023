<template>
<label class="card row">
    <img :src="this.src" />
    <input type="radio">
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
    width: 100%
    height: 60px
    margin: 4px
    padding: 10px 8px 6px 8px
    position: relative
    align-items: center
    border: 1px solid $secondary
    border-radius: 5px
    text-align: center
    cursor: pointer
    color: $secondary
    font-size: 18px

    input
        position: absolute
        opacity: 0
        cursor: pointer
        height: 0
        width: 0

    img
        width: 56px
        height: 28px
        margin: 4px
        filter: saturate(0)

.card:has(input:checked)
    background-color: $primary
    color: white
    border-color: $secondary

    img
        filter: saturate(1)


    
        
    
</style>
  