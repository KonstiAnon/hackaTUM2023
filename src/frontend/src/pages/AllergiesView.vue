<script setup>
  import CardToggle from 'src/components/CardToggle.vue';
  import PageHeader from 'src/components/PageHeader.vue';

    //todo fix this mess in the futur
  import celery from 'src/assets/icons/ic-no-celery.png'
  import nuts from 'src/assets/icons/ic-no-nuts.png'
  import gluten from 'src/assets/icons/icons8-no-gluten-96.png'
  import soy from 'src/assets/icons/icons8-no-soy-96.png'
  import peanuts from 'src/assets/icons/icons8-no-peanut-96.png'
  import dairy from 'src/assets/icons/icons8-dairy-96.png'
  import crustaceans from 'src/assets/icons/icons8-no-crustaceans-96.png'
  import fish from 'src/assets/icons/icons8-no-fish-96.png'

  // for now hardcode the allergies
  const allergies = [
    {
        "label":"No Nuts", 
        "ids":["57962a07b7e8697d4b3052fb", "63c00da4c4bb723852bbf3ee", "57962a07b7e8697d4b305302", "62cec8ddeaf1cc376f06a53b"], 
        "src":nuts
    },
    {
        "label":"No Celery",
        "ids" : ["57962a07b7e8697d4b3052fc", "5de91db7c7d1a818111194b2"],
        "src": celery
    },
    {
        "label":"No Wheat",
        "ids":["60368d89cdbdf450236ad8cd", "6203885f2cefe43adc5127c0"],
        "src":gluten
    },
    {
        "label":"No Soy",
        "ids":["57962a07b7e8697d4b3052f9", "5b0532aaae08b52eb9420552"],
        "src":soy
    },
    {
        "label":"No Peanuts",
        "ids":["5a9614ab30006c2c026cf562", "57962a07b7e8697d4b3052f8"],
        "src":peanuts
    },
    {
        "label":"No Dairy",
        "ids":["57962a07b7e8697d4b3052fa", "5acf97b7ae08b54d88061162"],
        "src":dairy
    },
    {
        "label":"No Crustaceans",
        "ids":["57962a07b7e8697d4b3052f4", "5acf967d30006c4cbc61d152"],
        "src":crustaceans
    },
    {
        "label":"No Fish",
        "ids":["57962a07b7e8697d4b3052f7", "5acf974c30006c4d667f88f1"],
        "src":fish
    }
];  

</script>

<template>
    <PageHeader header="Begin Your Quest!" description="Share allergies for a personalized food adventure." :progress="0.25">
        <div class="row justify-center">
            <template v-for="allergie in allergies" :key="allergie.label">
                <card-toggle :label="allergie.label" :src="allergie.src" />
            </template>
        </div>
    </PageHeader>
    <div class="navigation absolute-bottom" >
        <q-btn round size="17px" color="secondary" icon="arrow_right_alt" to="skill"/>
    </div>
</template>

<style scoped>
.navigation {
  margin: 50px;
  text-align: right;
}
</style>



