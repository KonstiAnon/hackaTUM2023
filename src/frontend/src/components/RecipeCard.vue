<script setup>
import {symOutlinedGrocery, symOutlinedUndo} from '@quasar/extras/material-symbols-outlined'
import {ref} from "vue";

const props = defineProps({
  recipe: {
    type: Object,
    required: true
  }
})

const flipped = ref(false)

const flip = () => {
  flipped.value = !flipped.value
}
</script>

<template>
  <Transition name="flip">
    <q-card v-if="!flipped" class="front recipe-card">
      <q-img :src="recipe.img" :ratio="317/376">
        <div class="absolute-bottom row justify-between items-center">
          <div class="text-h6">{{ recipe.name }}</div>
          <q-card-actions align="right">
            <q-btn flat round dense :icon="symOutlinedGrocery" @click="flip"/>
          </q-card-actions>
        </div>
      </q-img>
    </q-card>

    <q-card v-else class="back recipe-card">
      <q-img :src="recipe.img" :ratio="317/376" img-class="back-image">
        <q-card-actions align="right" class="absolute-bottom">
          <q-btn flat round dense :icon="symOutlinedUndo" @click="flip"/>
        </q-card-actions>
      </q-img>
    </q-card>
  </Transition>

</template>

<style lang="sass" scoped>
.recipe-card
  width: 100%
  width: 317px
  border-radius: 5px

::v-deep .back-image
  filter: blur(50px)

.flip-enter-active
  transition: all 0.4s ease


.flip-leave-active
  display: none


.flip-enter-from, .flip-leave-to
  transform: rotateY(180deg)
  opacity: 0


</style>
